# 04 — Board e Work Items

> Por que `BOARD.md` não é a fonte de verdade de um workspace, qual arquivo é, e como vários agentes atualizam o mesmo trabalho sem se sobrescrever.

---

## Por que o board não é o banco de dados principal

`BOARD.md` oferece uma visão consolidada do que está em andamento em um workspace — útil para uma leitura rápida, mas perigosa como registro autoritativo. Vários agentes editando o mesmo arquivo de texto ao mesmo tempo aumentam o risco de conflito e sobrescrita silenciosa, exatamente a falha de coordenação descrita em [Harness do workspace](03-harness-do-workspace.md). Por isso, `BOARD.md` é tratado como **índice regenerável**, nunca como origem do dado.

```markdown
# Board

Visão consolidada. O estado autoritativo permanece no arquivo de cada Work Item.

## Implementation

- [`WI-031` — Idempotência no processamento de pagamentos](projects/checkout/work-items/WI-031.md) — checkout
```

## A fonte de verdade é um arquivo por Work Item

Cada unidade de trabalho é um arquivo em `projects/<project>/work-items/`, e é esse arquivo — não o board — que registra estado, owner, escopo, dependências e evidências.

```markdown
---
id: WI-031
title: Implementar idempotência no processamento do pagamento
project: checkout
status: implementation
priority: high
owner: agent-backend
reviewer: tech-lead
repositories:
  - id: checkout-api
    branch: feat/WI-031-payment-idempotency
    base_branch: main
    worktree: repos/worktrees/acme/checkout-api/WI-031
depends_on: []
blocked_by: []
updated_at: 2026-08-08T14:30:00-03:00
---

## Objetivo

Impedir processamento duplicado de eventos de pagamento.

## Critérios de aceite

- [ ] Eventos repetidos não geram nova cobrança
- [ ] Estado permanece consistente após retry

## Evidências

Registradas em `execution/evidence/WI-031.md`.

## Histórico

- 2026-08-08 14:00 — item assumido por `agent-backend`.
```

Um exemplo completo, com histórico e evidência ligados a um plano real, está em [`workspaces/tech-lead/projects/checkout/work-items/WI-031.md`](../../workspaces/tech-lead/projects/checkout/work-items/WI-031.md). A skill [`workspace-board`](../../skills/workspace-board/SKILL.md) é o procedimento que aplica exatamente esta regra de autoridade: primeiro atualiza ou confirma o Work Item, só depois reconcilia o board.

## Estados permitidos

Os valores de `status` devem ser estáveis e escritos sempre da mesma forma, porque é isso que permite consolidar `BOARD.md` automaticamente a partir dos Work Items.

```text
backlog · refinement · ready · planning · implementation · review · validation · blocked · done · cancelled
```

`blocked` não é um estado como os demais — é uma exceção. Um Work Item bloqueado deve registrar causa, impacto, responsável pela resolução e próxima ação, do jeito que a [Metodologia](../METODOLOGIA.md) exige de qualquer bloqueio que dependa de decisão humana.

## Identificadores

Identificadores estáveis são o que permite automatizar qualquer verificação sobre o workspace — de contagem de itens abertos a auditoria de rastreabilidade.

| Entidade | Formato |
|---|---|
| Projeto | slug estável, por exemplo `checkout` |
| Plano | `PLAN-NNN` |
| Work Item | `WI-NNN` |
| ADR | `ADR-NNN` |
| Handoff | `HANDOFF-<work-item>-<origem>-<destino>.md` |

Quando identificadores puderem colidir entre projetos, adota-se o prefixo do projeto — `CHK-WI-031`.

## Contenção entre agentes

O risco em um workspace multiagente é a sobrescrita silenciosa do board, não do Work Item individual — cada Work Item já pertence a um único agente responsável. As regras abaixo existem para tornar cada conflito visível antes que ele destrua trabalho de outro agente.

| Regra | Evita |
|---|---|
| Cada missão ativa tem um único agente responsável, registrado no Work Item | dois agentes editando o mesmo artefato sem divisão explícita |
| O board é consolidado por um agente coordenador, não editado livremente por todos | conflito de escrita concorrente no mesmo arquivo |
| Achados transitórios ficam em arquivos separados, nunca em um log compartilhado único | um grande arquivo vira ponto de conflito garantido |
| Um Work Item só é marcado `done` com evidência de todos os critérios de aceite | avanço de estado por impressão, não por comprovação |

Essa última regra conecta esta página ao restante da documentação: um Work Item concluído sem evidência é exatamente o tipo de "pronto" que o [Gatekeeper Loop](../loops/06-pr-and-merge.md) e os checkpoints humanos de [Metodologia](../metodologia/02-checkpoints-humanos.md) existem para impedir.

---

*Anterior: [Harness do workspace](03-harness-do-workspace.md) · Volta ao hub: [Workspace](../WORKSPACE.md).*
