---
title: Workflow bindings — UX workspace
status: example
owner: ux
updated_at: 2026-08-08
---

# Workflows enabled in the UX workspace

This directory references [canonical catalog](../../../../workflows/README.md). It records local usage; does not replicate definitions or receive execution output.

| Workflow | UX Role | Persistent Font |
|---|---|---|
| [Discovery](../../../../workflows/01-discovery-and-research.md) | research, journey and experience hypothesis | `projects/<project>/research/` and `journeys/` |
| [Product and UX](../../../../workflows/02-product-and-ux-planning.md) | flows, states, accessibility and UX spec | `projects/<project>/flows/`, `specifications/`, `prototypes/` and `validation/` |
| [Validation](../../../../workflows/05-adversarial-validation.md) | highlights UX criteria when activated | `projects/<project>/validation/` |
| [Approval](../../../../workflows/07-release-candidate-validation.md) | decides to accept experience | `projects/<project>/validation/` |
| [Knowledge and improvement](../../../../workflows/09-knowledge-curation.md) | promotes experiential learning | project canonical source |

Temporary handoffs use `..coordination/`; handoffs of a project use `projects/<project>/handoffs/`. UX does not duplicate PRD, technical plan or CI evidence: references PM and Tech Lead sources.
