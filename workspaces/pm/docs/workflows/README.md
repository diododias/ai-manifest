---
title: Workflow bindings — PM workspace
status: example
owner: product-manager
updated_at: 2026-08-08
---

# Workflows enabled in the PM workspace

This directory references [canonical catalog](../../../../workflows/README.md). It records local usage; does not replicate definitions or receive execution output.

| Workflow | Role of the PM | Persistent Font |
|---|---|---|
| [Intake](../../../../workflows/00-intake-and-triage.md) | screening owner | `projects/<project>/work-items/` |
| [Discovery](../../../../workflows/01-discovery-and-research.md) | value owner and H1 | `projects/<project>/discovery/` |
| [Product and UX](../../../../workflows/02-product-and-ux-planning.md) | consolidates PRD and H2 | `projects/<project>/requirements/prd/`, `strategy/`, `decisions/` |
| [Approval](../../../../workflows/07-release-candidate-validation.md) | decides product acceptance | `projects/<project>/validation/` |
| [Knowledge and improvement](../../../../workflows/09-knowledge-curation.md) | promotes product learning and prioritizes demand | project canonical source and `work-items/` |

Temporary handoffs use `..coordination/`; handoffs of a project use `projects/<project>/handoffs/`. The PM doesn't write technical plans to his workspace: he references artifacts from the Tech Lead's workspace.
