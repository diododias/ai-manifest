---
title: Bindings de workflows — workspace do PM
status: example
owner: product-manager
updated_at: 2026-08-08
---

# Workflows habilitados no workspace do PM

Este diretório referencia o [catálogo canônico](../../../../docs/workflows/README.md). Ele registra o uso local; não replica definições nem recebe saídas de execução.

| Workflow | Papel do PM | Fonte persistente |
|---|---|---|
| [Intake](../../../../docs/workflows/00-intake-and-triage.md) | owner da triagem | `projects/<project>/work-items/` |
| [Discovery](../../../../docs/workflows/01-discovery-and-research.md) | owner de valor e H1 | `projects/<project>/discovery/` |
| [Produto e UX](../../../../docs/workflows/02-product-and-ux-planning.md) | consolida PRD e H2 | `projects/<project>/requirements/prd/`, `strategy/`, `decisions/` |
| [Homologação](../../../../docs/workflows/07-release-candidate-validation.md) | decide aceite de produto | `projects/<project>/validation/` |
| [Conhecimento e melhoria](../../../../docs/workflows/09-knowledge-curation.md) | promove aprendizado de produto e prioriza demanda | fonte canônica do projeto e `work-items/` |

Handoffs temporários usam `coordination/`; handoffs de um projeto usam `projects/<project>/handoffs/`. O PM não grava planos técnicos em seu workspace: referencia os artefatos do workspace do Tech Lead.
