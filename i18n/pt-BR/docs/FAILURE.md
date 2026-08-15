# Falha

A escada de verificação pressupõe que seus degraus rodam. Essa premissa é a parte menos examinada de um harness e a que falha mais silenciosamente, porque uma verificação que não roda produz a mesma saída de uma verificação que passou: nada.

Todo o resto desta documentação descreve como pegar uma mudança ruim. Esta página descreve como pegar uma verificação que parou de funcionar.

## Um gate que não rodou não passou

O comportamento padrão de quase toda verificação, escrita do jeito óbvio, é desaparecer quando suas condições não são atendidas:

| A verificação | Por que parou | O que o pipeline mostrou |
|---|---|---|
| um hook protegido por `command -v <tool> \|\| exit 0` | a tool não está instalada nesta máquina | sucesso |
| qualquer sensor em `.hooks/` | `core.hooksPath` nunca foi configurado neste clone | sucesso |
| um job de faixa rápida filtrado por caminho | um diretório foi renomeado e o glob não casa mais | sucesso, e mais rápido |
| um job de CI com condicional | a condição virou falsa em silêncio | sucesso, job não listado |
| uma suíte de testes | ela casou com zero arquivos de teste depois de uma mudança de configuração | sucesso, "0 passing" |
| um gate de pessoa revisora obrigatória | a entrada no CODEOWNERS aponta para um grupo que não existe mais | aprovado |

Toda linha é um padrão real, e toda linha é escrita por alguém competente tentando ser flexível. A flexibilidade é o defeito: **uma verificação que não consegue rodar não aprendeu nada sobre a mudança, e reportar "nada aprendido" como "nada errado" é o padrão mais caro de um sistema de verificação.**

A regra é fail-closed. Um gate que não consegue executar reporta falha, nomeia o que está faltando e diz como instalar. Quando um repositório genuinamente precisa seguir sem uma verificação — uma tool opcional durante o onboarding, um scan que exige uma credencial que a pessoa contribuidora não tem —, isso é um modo degradado *declarado*, não silencioso.

## Três estados, nunca dois

Um gate reporta um de três resultados, e o terceiro costuma ser o que falta:

| Estado | Significado | Consequência |
|---|---|---|
| `passed` | a verificação rodou e a mudança a satisfaz | segue |
| `failed` | a verificação rodou e a mudança a viola | bloqueia |
| `skipped` | a verificação não rodou | bloqueia por padrão; só segue onde o modo degradado está declarado, e é registrado nos dois casos |

O `gate-status.json` no evidence pack carrega esses estados por gate ([Documentation](DOCUMENTATION.md)). O propósito dele é tornar visível para quem revisa a distinção entre uma mudança verificada e uma não verificada, porque de fora — um pipeline verde, um evidence pack, um resumo — as duas são idênticas. Um pack que registra apenas sucessos não consegue responder à pergunta que uma auditoria de fato faz, que não é "as verificações passaram" e sim "quais verificações rodaram".

## Instável é uma terceira falha, não uma aprovação branda

Uma verificação que falha de forma intermitente treina todo mundo a ignorá-la, e leva junto a credibilidade das verificações vizinhas. A tentativa automática é o que converte uma verificação quebrada em uma permanentemente ignorada: o sinal é preservado só o suficiente para que ninguém precise consertá-lo.

A política que funciona tem três partes. Uma verificação instável é **posta em quarentena** em vez de repetida — retirada do conjunto bloqueante de forma explícita, para que sua ausência seja visível. A quarentena carrega **dono nomeado e prazo**, porque uma quarentena sem dono é uma remoção feita devagar. E uma execução que usou tentativa extra reporta como **degradada**, não como aprovada, para que o fato de ter sido necessária sobreviva na evidência.

Para agentes especificamente, há um motivo adicional para não repetir em silêncio: um gate instável ensina ao agente que a resposta correta a uma verificação vermelha é rodá-la de novo. Essa heurística depois generaliza para gates que estavam dizendo a verdade.

## Verificando o verificador

Um gate é código, e código que nunca foi observado falhando corretamente é código cujo comportamento é desconhecido. Três mecanismos, em custo crescente:

**Um canário reconhecidamente ruim.** Cada gate tem uma entrada pequena que precisa rejeitar. O gate de lint tem um arquivo que viola uma regra; o gate de arquitetura tem um import que cruza uma fronteira proibida; o scanner de segredos tem uma credencial falsa em uma fixture. Rodado periodicamente, isso responde "este gate ainda detecta alguma coisa?" — a pergunta que um pipeline verde nunca responde.

**Uma verificação de instalação.** O `verify.sh` afirma que os sensores estão de fato instalados e que toda tool da qual depende está presente, e falha se não estiverem. Essa é a contramedida direta às duas primeiras linhas da tabela acima, e custa milissegundos.

**Teste de mutação.** A forma geral do canário para a suíte de testes: responde se os testes pegariam uma regressão em vez de meramente executar a linha. Caro, e pertence ao fim da faixa profunda ([Tools](TOOLS.md)).

A saúde dos gates é, ela mesma, mensurável ao longo do tempo — com que frequência um gate é pulado, e quanto escapa dos que rodam. Essas são as duas métricas que mais importam em [Métricas](METRICS.md).

## Por que agentes pioram isso

Todo modo de falha desta página é anterior aos agentes. Agentes mudam a economia de dois deles.

Um agente sob um objetivo de conclusão, diante de um gate vermelho, tem um gradiente disponível que uma pessoa sob revisão normalmente não tem: ele pode modificar a verificação. Cada passo individual nessa direção é localmente razoável — a verificação parece errada, a correção é pequena, a mudança está no repositório que o agente está autorizado a editar. Essa é toda a razão pela qual [Gates](GATES.md#regras-inegociáveis-para-gates-com-agentes) proíbe um agente de alterar os gates dentro do fluxo que esses gates avaliam. Não porque agentes sejam adversariais, mas porque o caminho mais curto do vermelho ao verde passa pela verificação.

E um agente itera mais rápido do que qualquer pessoa revisa. Um gate que parou de rodar silenciosamente em abril é descoberto por uma pessoa em semanas; até lá, um agente produziu centenas de commits não verificados em cima dele. **O custo de um gate fail-open escala com a vazão de quem está atrás dele**, o que é o argumento para o canário ser barato e frequente, em vez de minucioso e anual.

## Declarando um modo degradado

Quando uma verificação genuinamente não consegue rodar, o repositório declara isso explicitamente, com quatro campos: qual gate, por que não consegue rodar, o que compensa nesse meio-tempo e quando a exceção expira. Uma exceção sem prazo é uma mudança permanente na arquitetura de verificação, e passa pelo dono do harness e pelo changelog como qualquer outra ([Versionamento](VERSIONING.md)).

Operar em um modo degradado declarado também baixa o teto de autonomia enquanto durar. Um repositório sem um gate fica, durante o período, no nível de verificação que o gate ausente consegue sustentar — ver [Gates](GATES.md#autonomia-progressiva-e-o-teto-do-harness).

---

*Próximo: [Concorrência](CONCURRENCY.md) — o que acontece quando vários agentes trabalham ao mesmo tempo.*
