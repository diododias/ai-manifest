#03 — Workspace Harness

> What makes a workspace operable by agents in a repeatable way: conventions, basic skills and coordination guarantees when several agents work at the same time.

---

## What "workspace harness" means

The word *harness* has already appeared in other sections of the documentation, and it is worth defining it here precisely, because it has two meanings that cannot be confused. A harness, in general, is the set of files, conventions and checks that makes an **understandable and safe** space for an agent to operate without someone having to recite the context every session.

The **workspace harness** is this set applied to the trio's workspace — what organizes the agent's work *outside* of the code. It is different from [repo harness](../REPO_HARNESS.md), which lives inside the code repository and converts tacit knowledge into versioned files and automated checks. The decision rule that separates the two is the same as the one introduced in [the hub of this section](../WORKSPACE.md): if the information remains true when another team clones the code repository, it is repo harness; If it describes how work is organized — what projects there are, who does what this week, under which Work Item — it is workspace.

## The conventions that the workspace imposes

The workspace harness materializes in the conventions already presented in the previous pages of this section, now brought together under a common name. They are what allow an agent to arrive at an unknown workspace and operate correctly, without prior negotiation.

| Convention | What guarantees |
|---|---|
| **Resolution chain** | an agent always decides where to work through the `owner workspace → projects/<project> → Work Item → canonical sources` path, never by guesswork |
| **Separation between persistent and transit** | canonical sources in `projects/`; helpers in `.coordination/` and `memory.md` — described in detail in [Workspace Structure](01-estrutura-do-workspace.md) |
| **Session isolation** | each run uses its own folder in `plans/assets/`, so reruns don't overwrite each other |

## Base skills are the harness in action

Here the pieces fit together. The three base skills — [`workspace-memory`](../../skills/workspace-memory/SKILL.md), [`workspace-projects`](../../skills/workspace-projects/SKILL.md) and [`workspace-board`](../../skills/workspace-board/SKILL.md), cataloged in [Skills](../SKILLS.md) — are, in practice, the harness of the executable workspace. They do not produce the deliverable for any phase of the journey; they ensure that the agent respects the workspace conventions before producing anything.

| Basic skill | Convention that applies |
|---|---|
| `workspace-memory` | resume context and never treat `memory.md` as a canonical source |
| `workspace-projects` | find the correct canonical source in `projects/` and isolate assets by session |
| `workspace-board` | assume and reconcile Work Items with evidence, without overwriting other people's work |

That's why they appear among the universal rules of every agent, described in [Agents](../AGENTES.md#as-regras-universais): without them, the workspace harness would just be a documented convention, not a followed convention.

## When several agents operate at the same time

The workspace harness gains extra importance when **several agents** work in parallel. The failures that appear in this scenario are not of quality — they are of coordination, and each one has a specific countermeasure.

| Coordination failure | What happens | Countermeasure |
|---|---|---|
| Silent overwrite | two agents edit the same file; the last one to save wins | one file per work unit; worktree by Work Item when there is code |
| Containment in common file | multiple agents update the same board or log | consolidation by a single coordinating agent |
| Loss of trail | it is not known which agent produced what | authorship and version recorded in each artifact |
| Lost handoff | work gets stuck in transit, without reaching the canonical source | handoff is only completed when the artifact reaches the canonical source |

Note the parallel with the repo harness: there, the same type of problem — multiple agents on the same code — is solved by clean worktree and distinct identities per agent, required from the HL3 level described in [Gates](../GATES.md). The idea is the same on both sides of the border: **isolate execution so that collaboration does not turn into collision.**

---

*Previous: [Ownership between workspaces](02-ownership-entre-workspaces.md) · Next: [Board and Work Items](04-board-e-work-items.md).*
