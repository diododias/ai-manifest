# Workspace pages

This directory contains the four section pages. The general concept — what a workspace is, the boundary with the repo harness, and the four pieces that every workspace maintains — is in [Workspace](../WORKSPACE.md); Here are the operational details.

## The rule that governs all pages

No page in this section describes the one-step quest sequence: that lives in [`loops/`](../loops/README.md). None define the authority, sponsor or decision-making rights of a role: this lives in [`agentes/`](../agentes/README.md) and [`metodologia/`](../metodologia/README.md). None redefine the mechanics of a skill: this lives in [`SKILLS.md`](../SKILLS.md). What is documented here is **where each artifact lives, who owns which truth, and what makes this space operable by agents** — always with a link to the corresponding contract when the subject belongs to another layer.

The practical test is the same used in the other sections of the documentation: if a paragraph in this section would remain correct even if a loop changed its internal sequence or an agent gained a new skill, it is in the right place. If not, it is a duplicate and needs to become a link.

## How to read

| Page | Reply | Read if you… |
|---|---|---|
| [01 — Workspace structure](01-estrutura-do-workspace.md) | where every artifact from an execution lives | are in doubt about where to save something |
| [02 — Ownership between workspaces](02-ownership-entre-workspaces.md) | which workspace owns which truth | need context from another domain and don't know if you can copy it |
| [03 — Workspace harness](03-harness-do-workspace.md) | what makes space operable by agents | will operate in parallel with other agents in the same workspace |
| [04 — Board and Work Items](04-board-e-work-items.md) | how work is tracked | will assume, update, or reconcile a Work Item |

## Trails by profile

**New operator — 10 minutes.** [Workspace Structure](01-estrutura-do-workspace.md) → [Board and Work Items](04-board-e-work-items.md). In the end, you know where to save what you produce and how to declare what you are doing.

**Who will create or review a new workspace.** [Workspace Structure](01-estrutura-do-workspace.md) → [Workspace Harness](03-harness-do-workspace.md) → [Board and Work Items](04-board-e-work-items.md). The three together cover the minimum contract before any automation.

**Whoever operates between roles — PM, UX or Tech Lead seeking someone else's context.** [Ownership between workspaces](02-ownership-entre-workspaces.md), paying attention to the "one truth, one owner" rule and the two safe ways of seeking context from another domain.

**Who will audit multiple agents operating at the same time.** [Workspace Harness](03-harness-do-workspace.md) → [Board and Work Items](04-board-e-work-items.md). The two pages together answer whether a silent overwrite is possible in the current configuration.
