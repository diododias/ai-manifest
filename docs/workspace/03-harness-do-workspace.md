# 03 — Harness do workspace

> O que torna um workspace operável por agentes de forma repetível: as convenções, as skills de base e as garantias de coordenação quando vários agentes trabalham ao mesmo tempo.

---

## O que "harness do workspace" significa

A palavra *harness* já apareceu em outras seções da documentação, e vale defini-la aqui com precisão, porque ela tem dois sentidos que não podem se confundir. Um harness, de forma geral, é o conjunto de arquivos, convenções e verificações que torna um espaço **compreensível e seguro** para um agente operar sem que alguém precise recitar o contexto a cada sessão.

O **harness do workspace** é esse conjunto aplicado ao espaço de trabalho do trio — o que organiza o trabalho do agente *fora* do código. Ele é diferente do [repo harness](../REPO_HARNESS.md), que vive dentro do repositório de código e converte conhecimento tácito em arquivos versionados e verificações automatizadas. A regra de decisão que separa os dois é a mesma introduzida no [hub desta seção](../WORKSPACE.md): se a informação continua verdadeira quando outro time clona o repositório de código, ela é repo harness; se ela descreve como o trabalho está organizado — quais projetos existem, quem faz o quê esta semana, em qual Work Item —, ela é workspace.

## As convenções que o workspace impõe

O harness do workspace se materializa nas convenções já apresentadas nas páginas anteriores desta seção, agora reunidas sob um nome comum. São elas que permitem a um agente chegar a um workspace desconhecido e operar corretamente, sem negociação prévia.

| Convenção | O que garante |
|---|---|
| **Cadeia de resolução** | um agente sempre resolve onde trabalhar pelo caminho `workspace do owner → projects/<project> → Work Item → fontes canônicas`, nunca por adivinhação |
| **Separação entre persistente e trânsito** | fontes canônicas em `projects/`; auxiliares em `.coordination/` e `memory.md` — descrita em detalhe em [Estrutura do workspace](01-estrutura-do-workspace.md) |
| **Isolamento de sessão** | cada execução usa sua própria pasta em `plans/assets/`, de modo que reexecuções não se sobrescrevem |

## As skills de base são o harness em ação

Aqui as peças se encaixam. As três skills de base — [`workspace-memory`](../../skills/workspace-memory/SKILL.md), [`workspace-projects`](../../skills/workspace-projects/SKILL.md) e [`workspace-board`](../../skills/workspace-board/SKILL.md), catalogadas em [Skills](../SKILLS.md) — são, na prática, o harness do workspace executável. Elas não produzem o entregável de nenhuma fase da jornada; elas garantem que o agente respeite as convenções do workspace antes de produzir qualquer coisa.

| Skill de base | Convenção que aplica |
|---|---|
| `workspace-memory` | retomar contexto e nunca tratar `memory.md` como fonte canônica |
| `workspace-projects` | localizar a fonte canônica correta em `projects/` e isolar assets por sessão |
| `workspace-board` | assumir e reconciliar Work Items com evidência, sem sobrescrever trabalho alheio |

Por isso elas figuram entre as regras universais de todo agente, descritas em [Agentes](../AGENTES.md#as-regras-universais): sem elas, o harness do workspace seria apenas uma convenção documentada, não uma convenção seguida.

## Quando vários agentes operam ao mesmo tempo

O harness do workspace ganha importância extra quando **vários agentes** trabalham em paralelo. As falhas que aparecem nesse cenário não são de qualidade — são de coordenação, e cada uma tem uma contramedida específica.

| Falha de coordenação | O que acontece | Contramedida |
|---|---|---|
| Sobrescrita silenciosa | dois agentes editam o mesmo arquivo; o último a salvar vence | um arquivo por unidade de trabalho; worktree por Work Item quando houver código |
| Contenção em arquivo comum | vários agentes atualizam o mesmo board ou log | consolidação por um único agente coordenador |
| Perda de rastro | não se sabe qual agente produziu o quê | autoria e versão registradas em cada artefato |
| Handoff perdido | trabalho fica preso em trânsito, sem chegar à fonte canônica | handoff só se conclui quando o artefato chega à fonte canônica |

Note o paralelo com o repo harness: lá, o mesmo tipo de problema — vários agentes sobre o mesmo código — é resolvido por worktree limpo e identidades distintas por agente, exigidos a partir do nível HL3 descrito em [Gates](../GATES.md). A ideia é a mesma dos dois lados da fronteira: **isolar a execução para que a colaboração não vire colisão.**

---

*Anterior: [Ownership entre workspaces](02-ownership-entre-workspaces.md) · Próximo: [Board e Work Items](04-board-e-work-items.md).*
