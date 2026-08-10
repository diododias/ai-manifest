#01 — Workspace structure

> The files that every workspace maintains, how `projects/` organizes each initiative, and why raw material and temporary transit are separated from the canonical source.

An unknown workspace should be navigable by any agent without someone having to explain the convention out loud. This page describes the minimum contract that makes this possible.

---

## One workspace per role

The trio's work doesn't live in a single shared place — each role has its own roots. This separation exists so that responsibilities do not get mixed up: the PM records value and requirements, the UX records evidence and experience, the Tech Lead records architecture and execution. Three independent roots evolve without stepping on each other, and each corresponds to the decision domain described in [Papers](../metodologia/01-papeis.md).

```text
workspaces/
├── pm/ # value, priority, requirements and product results
├── ux/ # search, experience, accessibility and validation
└── tech-lead/ # feasibility, architecture, implementation and risk
```

## The four files every workspace keeps

Regardless of role, every workspace maintains four pieces. Knowing them is enough to orient yourself in any of the three.

| Ask | Reply | Nature |
|---|---|---|
| `AGENTS.md` | how to operate in this workspace | operating contract |
| `BOARD.md` | which Work Items are in progress | consolidated vision, never source of truth |
| `memory.md` | where I return to the context | auxiliary, never canonical source |
| `projects/<project>/` | the actual artifacts of each initiative | canonical source |

When an agent starts a mission, they read the workspace's `AGENTS.md`, identify applicable skills, and follow the `projects/` structure — rather than inventing conventions of their own. This is why the base skills described in [Skills](../SKILLS.md) are mandatory in every workspace mission: `workspace-memory`, `workspace-projects` and `workspace-board` teach the agent how to navigate this structure safely, and not just describe it.

## Where the artifacts of an execution live

Persistent artifacts from a run are never loose or scattered across a global catalog — they live in `projects/<project>/`, in the workspace that owns the domain. The PM records discovery, PRD, decisions and Work Items there; UX records research, journeys, flows, specifications and validations; the Tech Lead records plans in `plans/active/`, specs, ADRs, evidence, reviews and worktrees.

An often confused detail: `projects/` of a Work Item is **not** in the local folder that references the loop catalog. This folder — described in [Where the loop lives and where execution happens](../LOOPS.md#where-the-loop-lives-and-where-execution-happens) — is just the local binding layer: which loops are enabled, in which version, with what permissions. The real work, what was actually decided and produced, is in `projects/`.

## Raw material and transit: separated on purpose

Two categories of content are deliberately left outside the canonical source, and understanding why avoids recurring confusion.

The **raw material** that supports the analyzes — transcripts, prints, emails, PDFs, documents — is in `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`. Each run uses its own session folder. This solves a real and recurring problem: rerunning a loop because the result was not good **never** overwrites or mixes the material from the previous attempt. The asset remains an auditable trace, and the conclusion drawn from it goes to the artifact in the correct domain.

The **temporary transit** — handoffs and blockages in `.coordination/` — is just passing through. As described in [Handoff — what crosses the border](../LOOPS.md#handoff--what-crosses-the-boundary), a handoff is only completed when the final artifact reaches the canonical source. `.coordination/` keeps what is on the way, not what is ready.

## A reference implementation

A browsable implementation of this structure is in [`workspaces/`](../../workspaces/README.md), with an example root for each of the three roles. The names, organizations, repositories and states that appear there are fictitious — they serve to demonstrate the structure, not the production work of a real team. When adopting the model, these values ​​must be replaced with your own.

---

*Previous: [Workspace index](README.md) · Next: [Ownership between workspaces](02-ownership-entre-workspaces.md).*
