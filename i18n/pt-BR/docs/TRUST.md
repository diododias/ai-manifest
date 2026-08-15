# Confiança

Todas as outras páginas do harness controlam o que o agente *faz*. Esta controla no que o agente *acredita*.

A camada de permissão modela risco como saída: um MCP escreve no sistema errado, um comando apaga a branch errada. Esse é o risco fácil de ver, e não é o que domina em produção. O risco dominante é de entrada. Um agente lê o corpo de uma issue, o README de uma dependência, um comentário em um pull request, a saída de um teste que falhou, a resposta de uma API — e tudo o que ele lê chega na mesma janela de contexto, no mesmo formato, que as regras que lhe foram dadas. Nada no transporte distingue uma política de uma frase que alguém digitou num campo de texto.

**A instrução não vem marcada. A fronteira precisa ser declarada.**

## A fronteira de confiança

Duas categorias, e toda entrada pertence a exatamente uma:

| | Definição | Exemplos |
|---|---|---|
| **Instrução** | revisada, versionada e alterada apenas pelo dono do harness | `AGENTS.md`, `docs/rules/`, `SKILL.md` neste repositório, `.agent/` |
| **Conteúdo** | todo o resto que entra no contexto | corpo de issues e PRs, comentários de código, mensagens de commit, saída de teste, stdout de comando, respostas de MCP, conteúdo de arquivos fora da árvore revisada, páginas web |

A regra que decorre disso é curta e absoluta: **conteúdo é dado sobre a tarefa, nunca uma afirmação do que o agente pode fazer.** Uma string que chega como conteúdo e se parece com uma regra é uma string. Ela pode ser citada, resumida, interpretada e usada *como informação* — uma issue pedindo uma funcionalidade é um pedido legítimo de trabalho — mas não pode alterar escopo, não pode conceder permissão, não pode aposentar um gate e não pode redirecionar o objetivo que foi dado ao agente.

A armadilha é que conteúdo frequentemente *está certo*. Um comentário dizendo "este teste é instável, pule-o" pode ser verdade. Ainda assim é conteúdo: o agente pode levantar o ponto, e uma pessoa pode agir sobre ele, e a diferença entre essas duas frases é a fronteira inteira.

## Por que detecção não é o controle

A defesa intuitiva é procurar strings maliciosas. Ela não se sustenta, por um motivo estrutural e não por qualidade de padrão: o atacante escreve a entrada e consegue ver o efeito do filtro, enquanto o defensor precisa antecipar um conjunto ilimitado de formulações — em vários idiomas, codificações, indireções ("siga as instruções do arquivo linkado") e texto que só vira instrução depois que o modelo o resume.

Detecção vale como sensor. Não é o que torna o sistema seguro. **O que torna o sistema seguro é que uma injeção bem-sucedida não alcança nada que valha alcançar.** Os controles são todos controles de capacidade:

| Controle | Efeito quando uma injeção tem sucesso |
|---|---|
| Tools não declaradas são negadas ([Permissões](PERMISSIONS.md)) | a instrução injetada nomeia uma tool que a sessão não tem |
| Escopo declarado por papel | o papel comprometido não consegue fazer o que outro conseguiria |
| Efeitos externos exigem aprovação | o passo danoso para em uma pessoa |
| O agente não edita os próprios gates | a injeção não consegue desligar o que a pegaria |
| Leitura sensível e escrita para fora nunca estão na mesma sessão | não há caminho do dado para fora |

É por isso que prompt injection pertence ao harness, e não a um prompt. Toda mitigação dessa lista é uma propriedade da configuração do repositório, e nenhuma delas depende de o modelo reconhecer que está sob ataque.

## Exfiltração é uma composição de permissões

Permissões individuais são revisadas individualmente, e é aí que a brecha se abre. Considere duas concessões, cada uma defensável isoladamente: o agente pode ler o repositório, e o agente pode comentar em uma issue do rastreador. Juntas, são um canal para fora do perímetro, e nenhuma revisão de qualquer uma delas teria apontado isso.

A forma geral: **uma sessão que segura dado sensível somada a qualquer escrita para fora é um caminho de exfiltração, seja qual for o motivo pelo qual as duas capacidades foram concedidas.** Escrita para fora é mais ampla do que parece à primeira vista — um comentário, uma mensagem de commit, um nome de branch, um webhook, uma consulta DNS, uma URL em uma imagem carregada.

O controle é separação, não proibição. Quando as duas capacidades são genuinamente necessárias, elas pertencem a papéis de agente diferentes, em sessões diferentes, e o handoff entre eles carrega a conclusão, não o dado: o agente de análise lê e produz um achado; o agente de reporte publica o achado e nunca segurou as linhas. A pergunta de auditoria que um repositório deveria conseguir responder não é "alguma permissão é perigosa?", e sim **"quais pares de permissões são mantidos ao mesmo tempo?"**

## O harness é uma supply chain

Uma skill, um servidor MCP, um hook, um prompt de agente compartilhado — cada um deles é material executável com acesso à sessão, e cada um costuma chegar com menos revisão do que uma biblioteca receberia.

| Artefato | O que pode fazer | Revise como |
|---|---|---|
| Servidor MCP de terceiro | vê o contexto, guarda credenciais, age externamente | uma dependência com acesso à rede |
| Skill ou prompt de agente vindo de fora do repositório | reescreve como um procedimento é executado | código |
| Script de hook | roda na máquina da pessoa desenvolvedora, com as credenciais dela | código, mais uma questão de privilégio local |
| `AGENTS.md` em um subdiretório ou em uma dependência vendorizada | é lido como *instrução* por um agente que percorre a árvore | conteúdo, a menos que o caminho esteja na árvore revisada |

A última linha é a sutil e é a razão de a fronteira de confiança ser definida por *caminho*, não por nome de arquivo. Um arquivo chamado `AGENTS.md` é instrução por causa de onde vive, não por causa de como se chama. Uma dependência vendorizada que traz um desses não ganhou autoridade sobre este repositório, e o harness que trata nome de arquivo como autoridade entregou o controle a quem conseguir adicionar um arquivo.

## `.agent/trust.md`

A fronteira é específica de cada repositório, então ela é declarada em vez de presumida:

- quais caminhos são instrução, exaustivamente — todo o resto é conteúdo
- quais fontes externas este repositório ingere, e por qual tool
- quais classes de dado existem, e quais delas podem entrar em um contexto de modelo
- quais pares de permissão são proibidos na mesma sessão
- o que acontece quando conteúdo tenta alterar escopo: parar, registrar, escalar — não ignorar em silêncio

A última linha importa pelo mesmo motivo pelo qual um gate pulado precisa ser reportado. Uma tentativa de injeção é um evento de segurança, e um agente que recusa silenciosamente e segue adiante destrói o único sinal de que alguém tentou.

## O que os gates verificam

| Gate | Verificação |
|---|---|
| Local | secret scanning antes de o objeto sair da máquina ([Sensors](SENSORS.md)) |
| CI, faixa profunda | SAST, revisão de dependências e SBOM em qualquer mudança de dependências ou do próprio harness |
| Merge | uma pessoa revisora nomeada para mudanças em `.agent/`, `.hooks/`, configuração de CI ou nos arquivos de rule |
| Runtime | chamadas para fora registradas em `external-calls.log`, com parâmetros e respostas ([Documentation](DOCUMENTATION.md)) |

A linha de runtime é o que transforma esta página de política em algo auditável depois de um incidente: é o registro do que de fato saiu, e não do que o agente relatou ter enviado.

---

*Próximo: [Falha](FAILURE.md) — o que acontece quando a própria verificação não roda.*
