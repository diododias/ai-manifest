---
title: Workflow bindings — Tech Lead workspace
status: example
owner: tech-lead
updated_at: 2026-08-08
---

# Workflows enabled in the Tech Lead workspace

This directory references [canonical catalog](../../../../workflows/README.md). It records local version, permissions, and integrations; does not replicate definitions or receive execution output.

| Workflow | Technical paper | Persistent Font |
|---|---|---|
| [Discovery](../../../../workflows/01-discovery-and-research.md) | feasibility, dependencies and initial risk | `projects/<project>/engineering/architecture/` |
| [Specification](../../../../workflows/03-technical-specification.md) | consolidates plan, ADR, spec and tasks | `projects/<project>/plans/active/`, `engineering/specs/`, `engineering/adr/`, `work-items/` |
| [Implementation](../../../../workflows/04-autonomous-implementation.md) | orchestrates isolated tasks and changes | `projects/<project>/work-items/`, `execution/evidence/`, `repos/worktrees/` |
| [Validation and PR](../../../../workflows/05-adversarial-validation.md) | consolidates technical review and integration | `projects/<project>/execution/reviews/` and `execution/evidence/` |
| [Release and observation](../../../../workflows/08-production-release-and-observation.md) | rollout, health and rollback | `projects/<project>/execution/evidence/` and `LEARNINGS.md` (candidates) |
| [Knowledge and improvement](../../../../workflows/10-continuous-improvement.md) | consolidates telemetry and proposals | `projects/<project>/LEARNINGS.md` |

`..coordination/` only maintains traffic status. Persistent handoffs are in `projects/<project>/execution/handoffs/`; code and worktrees are in `repos/`, never in `projects/`.
