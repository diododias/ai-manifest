#02 — Ownership between workspaces

> Which workspace is the canonical source of each type of truth, what others receive, and how an agent seeks context from another domain without duplicating it.

Three independent workspaces only work if the question "which is the right version?" always have a unique answer. This page sets out the rule that ensures this.

---

## One truth, one owner

The principle that governs the relationship between the three workspaces is simple and rigid: **authoritative information should not be kept in two places**. Each type of truth has exactly one workspace owner, and the others receive only what they need to operate — an approved decision, a handoff, a snapshot.

The reason is to avoid the worst problem of distributed documentation: two versions of the same truth that silently diverge over time, without anyone knowing which one is valid. With a single owner per domain, there is always an objective answer to this question — the same reasoning that supports the "artifact only exists in canonical source" compromise described in [Methodology](../METODOLOGIA.md).

## The ownership map

The table below is the reference. It tells you, for each truth domain, which workspace is the canonical source and what the other two receive from it.

| Domain | Canonical source | The rest receive |
|---|---|---|
| Value, priority, outcome and requirements | `pm/` | approved decision and product handoff |
| User, journey and experience evidence | `ux/` | UX spec, criteria and experience handoff |
| Architecture, implementation and operational risk | `tech-lead/` | feasibility, technical contracts and evidence pack |

Note that this is the same [table of decision rights](../metodologia/01-papeis.md#decision-rights) from the methodology, now expressed in terms of files and folders. The PM owns the value in both the decision and the disk; UX, of experience; the Tech Lead, from the technique. The physical organization of work mirrors human authority — not by coincidence, but because one was designed from the other.

## How an agent fetches context from another domain

In practice, an agent often needs context that belongs to another workspace. A Software Engineer Agent, operating in the Tech Lead's workspace, needs to consult the PRD, which lives in the PM's workspace. How to do this without creating a copy that will diverge?

The rule allows two options, both safe.

| Option | When to use | Caution |
|---|---|---|
| **Follow the link to the source** | whenever the artifact is accessible | read where he really lives, in the owner's workspace — never reproduce the content |
| **Use a non-authoritative snapshot** | when the direct link is not viable | explicitly identify as non-authoritative and confirm validity before acting |

What is never done, in either option, is to copy the information to the workspace itself and start treating it as local truth. The day the original changes, the copy lies — and no one is told about it.

## Why the examples are fictitious

If you open the example workspaces in [`workspaces/`](../../workspaces/README.md), you will find fictitious names, organizations, repositories, and states. This is intentional: they demonstrate the structure, not the production work of an actual team. When copying the structure to your team, these values ​​must be replaced with yours — but the principle of single ownership does not change with the replacement.

---

*Previous: [Workspace Structure](01-estrutura-do-workspace.md) · Next: [Workspace Harness](03-harness-do-workspace.md).*
