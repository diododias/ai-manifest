# Permissões

A camada de permissão define quais tools o agente está autorizado a invocar, com que limites, e o que exige autorização humana antes de prosseguir. Essa definição é estrutural — não vive em afirmações de prompt, e sim em arquivos versionados dentro do repositório.

O motivo de não poder viver no prompt não é que agentes desobedeçam. É que o prompt e o agente são o mesmo sistema: uma instrução que diz "não faça force-push" é avaliada pelo processo que ela restringe, e um processo sob pressão para terminar encontrará a leitura daquela instrução que o deixa terminar. Permissão precisa ser imposta por algo que não seja o agente.

## `.agent/settings.json`

O arquivo `settings.json` declara os limites operacionais do agente naquele repositório: quais tools são permitidas, quais são explicitamente proibidas, quais modelos podem ser usados e quais são as condições de parada. Um agente que não encontra este arquivo deve tratar o repositório como não autorizado para operação sem acompanhamento.

```json
{
  "tools": {
    "allowed": ["read_file", "write_file", "run_tests", "run_lint"],
    "ask": ["install_dependency", "write_migration"],
    "denied": ["delete_branch", "force_push", "modify_ci", "modify_hooks"]
  },
  "models": {
    "default": "claude-sonnet-5"
  },
  "budget": {
    "max_cost_per_work_item_usd": 2.00,
    "max_turns": 40
  },
  "escalation": {
    "max_retries_before_escalation": 2
  }
}
```

Três propriedades deste arquivo concentram a maior parte do seu valor.

**O não declarado é negado.** A lista `allowed` é exaustiva, não ilustrativa. Uma tool que não é nomeada está proibida, do mesmo modo que [a ausência de `mcps.json` significa escopo zero](MCPS.md). A alternativa — listar o que é perigoso para negar — exige ter imaginado toda coisa perigosa de antemão, e a lista só fica completa em retrospecto.

**São três veredictos, não dois.** O `ask` é o que torna o modelo utilizável: ele cobre as operações que são legítimas na maior parte dos casos e caras no restante, em que bloquear de vez empurraria o agente para um contorno e permitir de vez removeria o único momento em que uma pessoa poderia objetar. Uma operação que é sempre aceitável pertence a `allowed`; uma que nunca é pertence a `denied`; todo o resto é um `ask`, e um modelo de permissão com a lista `ask` vazia costuma ser um modelo ajustado para o silêncio, não para o controle.

**O bloco de escalação não contém limiar de confiança.** Confiança autodeclarada não é calibrada nem comparável entre modelos; um número como `0.85` em um arquivo de configuração produz a aparência de um controle sem nenhum de seus mecanismos. Condições de parada são fatos sobre o trabalho — tentativas sem progresso, escopo excedido, dono ausente — e estão listadas em [Rules](RULES.md#condições-de-escalação).

### Curingas concedem o pior membro da família

A forma mais comum de um modelo de permissão falhar não é uma regra ausente. É um padrão que parecia estreito:

| Escrito como | Também concede |
|---|---|
| `git *` | `push --force`, `reset --hard`, `branch -D`, `clean -fd` |
| `npm run *` | todo script do `package.json`, inclusive os adicionados depois por uma atualização de dependência |
| `docker *` | montar o sistema de arquivos do host dentro de um contêiner |
| `curl *` | enviar qualquer arquivo do repositório para qualquer host |

Cada um deles foi escrito para permitir algo corriqueiro e silenciosamente autoriza algo irreversível. Duas regras decorrem disso. Enumere subcomandos em vez de famílias de comando — `git status`, `git diff`, `git log`, não `git *`. E, quando uma família genuinamente precisa ser permitida, acompanhe a permissão de uma negação explícita para seus membros destrutivos, de modo que adicionar uma permissão nunca alargue o raio de dano em silêncio.

O mesmo raciocínio vale para escopo de caminho: `read_file` sobre a árvore inteira inclui o `.env` que alguém vai adicionar no próximo trimestre.

### Permissões são por papel, não por repositório

Um repositório não tem um agente. O revisor, o implementador e o agente de release precisam de escopos diferentes, e colapsá-los em um único perfil concede a todo agente a união do que qualquer agente precisa — que é como um agente de revisão acaba conseguindo dar push.

O escopo é, portanto, declarado por papel de agente, e o papel é vinculado à identidade sob a qual aquele papel escreve ([Documentation](DOCUMENTATION.md#identidade-e-proveniência)). É isso também que torna "quem propõe não aprova" algo imponível, em vez de aspiracional: o papel que aprova não detém a permissão de ter escrito a mudança.

## `.agent/permissions.md`

O arquivo `permissions.md` descreve, em linguagem natural, o que exige autorização humana naquele repositório específico. Ele complementa o `settings.json` com o julgamento que nenhum JSON captura: quando a situação é ambígua o bastante para parar.

As categorias típicas cobertas por este arquivo incluem caminhos que exigem propriedade antes de qualquer alteração, operações que alteram estado persistido (migrações, schemas, segredos), ações irreversíveis com janela de rollback limitada e quaisquer mudanças que afetem os próprios gates de verificação.

A redundância entre os dois arquivos é intencional e é o mesmo padrão usado para MCPs: **o JSON protege o escopo técnico; o Markdown protege o julgamento no caso limítrofe.** JSON não consegue expressar "esta tabela é pequena o bastante para migrar no lugar, a menos que seja a tabela de contas". Markdown não consegue interromper uma chamada.

## Mudar uma permissão é mudar um gate

Permissões fazem parte da arquitetura de verificação, então a regra de [Gates](GATES.md#regras-inegociáveis-para-gates-com-agentes) vale sem exceção: um agente não alarga o próprio escopo dentro do fluxo que esse escopo restringe. Uma mudança de permissão é uma mudança de harness — passa pelo dono do harness, é versionada e é registrada no changelog com o motivo ([Versionamento](VERSIONING.md)).

O modo de falha que isso evita é o que se parece com progresso: um agente bloqueado, a duas tentativas de terminar, editando o arquivo que o bloqueia. Cada passo individual é razoável. O resultado é um repositório cujo modelo de permissão registra o que os agentes quiseram, não o que o time decidiu.

---

*Próximo: [Tools](TOOLS.md) — o índice de ferramentas e onde cada verificação roda.*
