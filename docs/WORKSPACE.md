# 6. Workspace

---

## Overview — Where Work Lives

The previous five sections describe **the system**: what the repository needs to carry to be operable by agents, who the agents are and under what authority they act, how a recurring task is performed, in what order they collaborate at each step, and how the human core operates it all. The piece that they all presuppose without naming is missing: **the physical place where this work actually happens.**

This place is the **workspace**. It is not reference material — it is the work point where each human role and its agents actually execute the flow: where a Work Item is opened, where a decision becomes an artifact, where an agent returns to the context of a previous session. An agent who perfectly understands a loop and an agent's contract still doesn't know how to operate if he doesn't know where to read and where to write — this is the gap that this section closes.

There is one workspace per role: `pm/`, `ux/` and `tech-lead/`. Each has an independent root so that their contracts, examples and sources of truth evolve without mixing responsibilities. The separation mirrors the same distinction that organizes [Papers](metodologia/01-papeis.md): the PM records value and requirements, the UX records evidence and experience, the Tech Lead records architecture, execution and the harness itself.

### The frontier with repo harness

The question that most confuses those who come to this section is where the [repo harness](REPO_HARNESS.md) ends and where the workspace begins. The two layers appear redundant until the correct test is applied.

| Layer | Reply | Where do you live |
|---|---|---|
| **Repository Harness** | what the repository needs to load to be operable | [`REPO_HARNESS.md`](REPO_HARNESS.md) |
| **Skill** | *how* a recurring task is performed correctly | [`SKILLS.md`](SKILLS.md) |
| **Agent** | *who* executes, under what authority and with what limits | [`AGENTES.md`](AGENTES.md) |
| **Loop** | *in what order*, what crosses the border and when to stop | [`LOOPS.md`](LOOPS.md) |
| **Methodology** | *who operates*, what triggers what and what demands people | [`METODOLOGIA.md`](METODOLOGIA.md) |
| **Workspace** | *where* every artifact of an execution lives, outside the code | this section |

The decision rule is the same on all the following pages, and it is worth memorizing it before proceeding: **if the information remains true when another team clones the code repository, it belongs to the repo harness. If it describes how the work is organized this week — what projects there are, who does what, in which Work Item — it belongs in the workspace.** The repo harness organizes the agent's work *within* the code; the workspace organizes the agent's work *outside* of it. Neither replaces the other, and a competent agent needs both at the same time.

### The four pieces of any workspace

Regardless of role, every workspace maintains four pieces. Knowing them is enough to orient yourself in any of the three — and is the subject of the first page of this section.

| Ask | Reply | Nature |
|---|---|---|
| `AGENTS.md` | how to operate in this workspace | operating contract |
| `BOARD.md` | which Work Items are in progress | consolidated vision, never source of truth |
| `memory.md` | where I return to the context | auxiliary, never canonical source |
| `projects/<project>/` | the actual artifacts of each initiative | canonical source |

When an agent starts a mission, he reads the workspace's `AGENTS.md`, identifies the applicable skills — the three base skills described in [Skills](SKILLS.md) exist precisely to teach this navigation — and follows the structure of `projects/` instead of inventing his own conventions. A browsable implementation of these four parts is in [`workspaces/`](../workspaces/README.md), with example roots for the three roles.

---

## Section index

| Page | Reply |
|---|---|
| [01 — Workspace structure](workspace/01-estrutura-do-workspace.md) | the files that every workspace maintains and how `projects/` organizes each initiative |
| [02 — Ownership between workspaces](workspace/02-ownership-entre-workspaces.md) | which workspace owns which truth, and how to fetch context from another domain without duplicating it |
| [03 — Workspace harness](workspace/03-harness-do-workspace.md) | which makes the space operable by agents in a repeatable way, including several at the same time |
| [04 — Board and Work Items](workspace/04-board-e-work-items.md) | why `BOARD.md` is not the source of truth, and what is |

The complete index, with the rule that governs the four pages and reading tracks per profile, is in [`workspace/README.md`](workspace/README.md).

---

*Previous: [Methodology](METODOLOGIA.md) · Detail: [the four workspace pages](workspace/README.md).*
