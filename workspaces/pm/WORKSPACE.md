---
title: Product Manager example workspace
status: example
owner: product-manager
updated_at: 2026-08-08
---

# PM Workspace

This example organizes portfolio, discovery, strategy, requirements, roadmap, decisions and product validation. The `checkout` project is fictional and connects to the UX and Tech Lead examples.

## Navigation

1. Load [`README.md`](README.md) and [`AGENTS.md`](AGENTS.md).
2. See [`docs/portfolio/PORTFOLIO.md`](docs/portfolio/PORTFOLIO.md) and [`BOARD.md`](BOARD.md).
3. Enter [`projects/checkout/README.md`](projects/checkout/README.md).
4. Use the templates in [`docs/templates/`](docs/templates/README.md) and the flow in [`docs/playbooks/product-cycle.md`](docs/playbooks/product-cycle.md).

## Structure

```text
pm/
├── README.md
├── AGENTS.md
├── WORKSPACE.md
├──BOARD.md
├── docs/ # portfolio, patterns, playbooks and templates
├── projects/ # product source of truth by project
│ └── <project>/plans/assets/<workflow>/<data>-<session-id>/ # raw material isolated per session
├── ..coordination/ # entries, pending decisions and temporary handoffs
├── memory.md # resumable context, non-authoritative
└── archive/ # global material disabled
```

## Standard envelope

```yaml
mission_id: "<id>"
agent_role: "<papel>"
status: completed | partial | blocked
confidence: high | medium | low
sources_used: []
outputs_created: []
decisions_requested: []
assumptions: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```
