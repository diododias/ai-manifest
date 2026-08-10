---
title: Tech Lead example workspace
status: example
owner: tech-lead
updated_at: 2026-08-08
---

# Tech Lead Workspace

This directory embodies the architecture described in [`docs/diagrams/tech-lead-workspace.md`](docs/diagrams/tech-lead-workspace.md). The `checkout` project, the `acme` organization and their states are fictitious data used to show the complete flow.

## Start here

1. Load the context for AIs in [`README.md`](README.md).
2. Read the mandatory rules in [`AGENTS.md`](AGENTS.md).
3. See the portfolio at [`docs/portfolio/PROJECTS.md`](docs/portfolio/PROJECTS.md) and the summary at [`BOARD.md`](BOARD.md).
4. Enter the project by [`projects/checkout/CONTEXT.md`](projects/checkout/CONTEXT.md) and [`projects/checkout/STATUS.md`](projects/checkout/STATUS.md).
5. Locate the code in [`projects/checkout/engineering/repositories.yaml`](projects/checkout/engineering/repositories.yaml).
6. Assume a file at [`projects/checkout/work-items/`](projects/checkout/work-items/README.md).

## Where every piece of information belongs

| Information | Source of truth |
|---|---|
| Portfolio and priority | `docs/portfolio/PROJECTS.md` and `BOARD.md` |
| Project context and status | `projects/<projeto>/CONTEXT.md` and `STATUS.md` |
| Product Requirements | `../pm/projects/<projeto>/requirements/`; `product/` contains only input snapshots |
| Experience | `../ux/projects/<projeto>/`; `ux/` location contains only integration pointers |
| Decisions and technical specifications | `projects/<projeto>/engineering/` |
| Execution strategy | `projects/<projeto>/plans/` |
| Job status | `projects/<projeto>/work-items/` |
| Evidence of completion | `projects/<projeto>/execution/evidence/` |
| Clones and worktrees | `repos/` |
| Temporary coordination | `..coordination/` |
| Resumable, non-authoritative context | `memory.md` |

## Structure

```text
tech-lead/
├── README.md
├── AGENTS.md
├── WORKSPACE.md
├──BOARD.md
├── docs/ # patterns, playbooks, templates and portfolio
├── projects/ # source of truth for each project
├── repos/ # registry and local checkouts ignored by Git
├── ..coordination/ # temporary cross communication
├── memory.md # workspace operational memory
└── archive/ # global material disabled
```

## Copying the example

Replace dummy data, keep one folder per project, and don't version clones, secrets, or volatile state. Directories that do not already have artifacts are represented by `README.md`; they can be removed when the first real artifact is created.
