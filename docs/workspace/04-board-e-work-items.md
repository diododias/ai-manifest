#04 — Board and Work Items

> Why `BOARD.md` is not the source of truth for a workspace, what file it is, and how multiple agents update the same work without overwriting each other.

---

## Why the board is not the main database

`BOARD.md` provides a consolidated view of what's happening in a workspace — useful for a quick read, but dangerous as an authoritative record. Multiple agents editing the same text file at the same time increases the risk of conflict and silent overwrite, exactly the coordination failure described in [Workspace Harness](03-harness-do-workspace.md). Therefore, `BOARD.md` is treated as a **regenerable index**, never as the origin of the data.

```markdown
#Board

Consolidated vision. The authoritative state remains in the file for each Work Item.

## Implementation

- [`WI-031` — Idempotence in payment processing](projects/checkout/work-items/WI-031.md) — checkout
```

## The source of truth is one file per Work Item

Each unit of work is a file in `projects/<project>/work-items/`, and it is this file — not the board — that records state, owner, scope, dependencies, and evidence.

```markdown
---
id: WI-031
title: Implement idempotence in payment processing
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

## Objective

Prevent duplicate processing of payment events.

## Acceptance criteria

- [ ] Repeated events do not generate new charges
- [ ] State remains consistent after retry

## Evidence

Registered in `execution/evidence/WI-031.md`.

## History

- 2026-08-08 14:00 — item taken over by `agent-backend`.
```

A complete example, with history and evidence linked to a real plan, is in [`workspaces/tech-lead/projects/checkout/work-items/WI-031.md`](../../workspaces/tech-lead/projects/checkout/work-items/WI-031.md). The skill [`workspace-board`](../../skills/workspace-board/SKILL.md) is the procedure that applies exactly this authority rule: first updates or confirms the Work Item, and only then reconciles the board.

## Allowed states

The `status` values must be stable and always written in the same way, because this is what allows `BOARD.md` to be automatically consolidated from the Work Items.

```text
backlog · refinement · ready · planning · implementation · review · validation · blocked · done · cancelled
```

`blocked` is not a state like the others — it is an exception. A blocked Work Item must record cause, impact, person responsible for resolution and next action, in the way that [Methodology](../METODOLOGIA.md) requires of any block that depends on human decision.

## Identifiers

Stable identifiers are what allow you to automate any check about your workspace — from counting open items to auditing traceability.

| Entity | Format |
|---|---|
| Project | stable slug, for example `checkout` |
| Plan | `PLAN-NNN` |
| Work Item | `WI-NNN` |
| ADR | `ADR-NNN` |
| Handoff | `HANDOFF-<work-item>-<origem>-<destino>.md` |

When identifiers may collide between projects, the project prefix — `CHK-WI-031` — is adopted.

## Containment between agents

The risk in a multi-agent workspace is the silent overwriting of the board, not the individual Work Item — each Work Item already belongs to a single responsible agent. The rules below exist to make each conflict visible before it destroys another agent's work.

| Rule | Avoid |
|---|---|
| Each active mission has a single responsible agent, registered in the Work Item | two agents editing the same artifact without explicit division |
| The board is consolidated by a coordinating agent, not freely edited by everyone | concurrent writing conflict in the same file |
| Transient findings are in separate files, never in a single shared log | a large file becomes a guaranteed point of conflict |
| A Work Item is only marked `done` with evidence of all acceptance criteria | status advancement by printing, not by proof |

That last rule connects this page to the rest of the documentation: a completed Work Item without evidence is exactly the kind of "done" that [Gatekeeper Loop](../loops/06-pr-and-merge.md) and the human checkpoints of [Methodology](../metodologia/02-checkpoints-humanos.md) exist to prevent.

---

*Previous: [Workspace harness](03-harness-do-workspace.md) · Back to hub: [Workspace](../WORKSPACE.md).*
