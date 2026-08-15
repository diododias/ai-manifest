# 6. Workspace

---

## Overview — Onde o Trabalho Vive

As cinco seções anteriores descrevem **o sistema**: o que o repositório precisa carregar para ser operável por agentes, quem são os agentes e sob qual autoridade agem, como uma tarefa recorrente é executada, em que ordem eles colaboram em cada etapa e como o núcleo humano opera tudo isso. Falta a peça que todas elas pressupõem sem nomear: **o lugar físico onde esse trabalho de fato acontece.**

Esse lugar é o **workspace**. Ele não é material de referência — é o ponto de trabalho onde cada papel humano e seus agentes executam o fluxo de verdade: onde um Work Item é aberto, onde uma decisão vira artefato, onde um agente retoma o contexto de uma sessão anterior. Um agente que entende perfeitamente um loop e o contrato de um agente ainda não sabe operar se não souber onde ler e onde escrever — é essa lacuna que esta seção fecha.

Existe um workspace por papel: `pm/`, `ux/` e `tech-lead/`. Cada um tem uma raiz independente para que seus contratos, exemplos e fontes de verdade evoluam sem misturar responsabilidades. A separação espelha a mesma distinção que organiza [Papéis](metodologia/01-papeis.md): o PM registra valor e requisitos, o UX registra evidência e experiência, o Tech Lead registra arquitetura, execução e o próprio harness.

### A fronteira com o repo harness

A pergunta que mais confunde quem chega a esta seção é onde termina o [repo harness](REPO_HARNESS.md) e onde começa o workspace. As duas camadas parecem redundantes até se aplicar o teste correto.

| Camada | Responde | Onde vive |
|---|---|---|
| **Harness do repositório** | o que o repositório precisa carregar para ser operável | [`REPO_HARNESS.md`](REPO_HARNESS.md) |
| **Skill** | *como* uma tarefa recorrente é executada corretamente | [`SKILLS.md`](SKILLS.md) |
| **Agente** | *quem* executa, sob qual autoridade e com qual limite | [`AGENTES.md`](AGENTES.md) |
| **Loop** | *em que ordem*, o que atravessa a fronteira e quando parar | [`LOOPS.md`](LOOPS.md) |
| **Metodologia** | *quem opera*, o que dispara o quê e o que exige gente | [`METODOLOGIA.md`](METODOLOGIA.md) |
| **Workspace** | *onde* cada artefato de uma execução vive, fora do código | esta seção |

A regra de decisão é a mesma em todas as páginas seguintes, e vale memorizá-la antes de prosseguir: **se a informação continua verdadeira quando outro time clona o repositório de código, ela pertence ao repo harness. Se ela descreve como o trabalho está organizado esta semana — quais projetos existem, quem faz o quê, em qual Work Item — ela pertence ao workspace.** O repo harness organiza o trabalho do agente *dentro* do código; o workspace organiza o trabalho do agente *fora* dele. Nenhum dos dois substitui o outro, e um agente competente precisa dos dois ao mesmo tempo.

### As quatro peças de qualquer workspace

Independentemente do papel, todo workspace mantém quatro peças. Conhecê-las é suficiente para se orientar em qualquer um dos três — e é o assunto da primeira página desta seção.

| Peça | Responde | Natureza |
|---|---|---|
| `AGENTS.md` | como operar neste workspace | contrato de operação |
| `BOARD.md` | quais Work Items estão em andamento | visão consolidada, nunca fonte de verdade |
| `memory.md` | onde retomo o contexto | auxiliar, nunca fonte canônica |
| `projects/<project>/` | os artefatos reais de cada iniciativa | fonte canônica |

Quando um agente inicia uma missão, ele lê o `AGENTS.md` do workspace, identifica as skills aplicáveis — as três skills de base descritas em [Skills](SKILLS.md) existem justamente para ensinar essa navegação — e segue a estrutura de `projects/` em vez de inventar convenções próprias. Uma implementação navegável dessas quatro peças está em [`workspaces/`](../workspaces/README.md), com raízes de exemplo para os três papéis.

---

## Índice da seção

| Página | Responde |
|---|---|
| [01 — Estrutura do workspace](workspace/01-estrutura-do-workspace.md) | os arquivos que todo workspace mantém e como `projects/` organiza cada iniciativa |
| [02 — Ownership entre workspaces](workspace/02-ownership-entre-workspaces.md) | qual workspace é dono de qual verdade, e como buscar contexto de outro domínio sem duplicá-lo |
| [03 — Harness do workspace](workspace/03-harness-do-workspace.md) | o que torna o espaço operável por agentes de forma repetível, inclusive vários ao mesmo tempo |
| [04 — Board e Work Items](workspace/04-board-e-work-items.md) | por que `BOARD.md` não é a fonte de verdade, e qual é |

O índice completo, com a regra que governa as quatro páginas e trilhas de leitura por perfil, está em [`workspace/README.md`](workspace/README.md).

---

*Anterior: [Metodologia](METODOLOGIA.md) · Detalhe: [as quatro páginas do workspace](workspace/README.md).*
