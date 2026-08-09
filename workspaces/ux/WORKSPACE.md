---
title: UX example workspace
status: example
owner: ux
updated_at: 2026-08-08
---

# UX Workspace

This example organizes user evidence, journeys, flows, specifications, prototypes, accessibility, and validation. The `checkout` project is fictional and connects to the PM and Tech Lead examples.

## Navigation

1. Load [`README.md`](README.md) and [`AGENTS.md`](AGENTS.md).
2. See [`BOARD.md`](BOARD.md).
3. Enter [`projects/checkout/README.md`](projects/checkout/README.md).
4. Use the patterns in [`docs/standards/`](docs/standards/README.md), the playbook and templates.

## Structure

```text
ux/
├── README.md
├── AGENTS.md
├── WORKSPACE.md
├──BOARD.md
├── docs/ # patterns, playbooks and templates
├── projects/ # research and experience by project
│ └── <project>/plans/assets/<workflow>/<data>-<session-id>/ # raw material isolated per session
├── ..coordination/ # recruitment, handoffs and temporary decisions
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
