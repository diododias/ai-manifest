# Páginas do workspace

Este diretório contém as quatro páginas da seção. O conceito geral — o que é um workspace, a fronteira com o repo harness e as quatro peças que todo workspace mantém — está em [Workspace](../WORKSPACE.md); aqui ficam os detalhes operacionais.

## A regra que governa todas as páginas

Nenhuma página desta seção descreve a sequência de missões de uma etapa: isso vive em [`loops/`](../loops/README.md). Nenhuma define autoridade, sponsor ou direito de decisão de um papel: isso vive em [`agentes/`](../agentes/README.md) e em [`metodologia/`](../metodologia/README.md). Nenhuma redefine a mecânica de uma skill: isso vive em [`SKILLS.md`](../SKILLS.md). O que se documenta aqui é **onde cada artefato vive, quem é dono de qual verdade, e o que torna esse espaço operável por agentes** — sempre com link para o contrato correspondente quando o assunto pertencer a outra camada.

O teste prático é o mesmo usado nas demais seções da documentação: se um parágrafo desta seção continuaria correto mesmo que um loop mudasse sua sequência interna ou um agente ganhasse uma nova skill, ele está no lugar certo. Se não, ele é duplicata e precisa virar link.

## Como ler

| Página | Responde | Leia se você… |
|---|---|---|
| [01 — Estrutura do workspace](01-estrutura-do-workspace.md) | onde cada artefato de uma execução vive | está em dúvida sobre onde salvar algo |
| [02 — Ownership entre workspaces](02-ownership-entre-workspaces.md) | qual workspace é dono de qual verdade | precisa de contexto de outro domínio e não sabe se pode copiá-lo |
| [03 — Harness do workspace](03-harness-do-workspace.md) | o que torna o espaço operável por agentes | vai operar em paralelo com outros agentes no mesmo workspace |
| [04 — Board e Work Items](04-board-e-work-items.md) | como o trabalho é rastreado | vai assumir, atualizar ou reconciliar um Work Item |

## Trilhas por perfil

**Operador novo — 10 minutos.** [Estrutura do workspace](01-estrutura-do-workspace.md) → [Board e Work Items](04-board-e-work-items.md). Ao final, você sabe onde salvar o que produz e como declarar o que está fazendo.

**Quem vai criar ou revisar um workspace novo.** [Estrutura do workspace](01-estrutura-do-workspace.md) → [Harness do workspace](03-harness-do-workspace.md) → [Board e Work Items](04-board-e-work-items.md). As três juntas cobrem o contrato mínimo antes de qualquer automação.

**Quem opera entre papéis — PM, UX ou Tech Lead buscando contexto alheio.** [Ownership entre workspaces](02-ownership-entre-workspaces.md), com atenção à regra de "uma verdade, um dono" e às duas formas seguras de buscar contexto de outro domínio.

**Quem vai auditar múltiplos agentes operando ao mesmo tempo.** [Harness do workspace](03-harness-do-workspace.md) → [Board e Work Items](04-board-e-work-items.md). As duas páginas juntas respondem se uma sobrescrita silenciosa é possível na configuração atual.
