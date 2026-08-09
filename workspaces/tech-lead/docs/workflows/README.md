---
title: Bindings de workflows — workspace do Tech Lead
status: example
owner: tech-lead
updated_at: 2026-08-08
---

# Workflows habilitados no workspace do Tech Lead

Este diretório referencia o [catálogo canônico](../../../../workflows/README.md). Ele registra versão, permissões e integrações locais; não replica definições nem recebe saídas de execução.

| Workflow | Papel técnico | Fonte persistente |
|---|---|---|
| [Discovery](../../../../workflows/01-discovery-and-research.md) | viabilidade, dependências e risco inicial | `projects/<project>/engineering/architecture/` |
| [Especificação](../../../../workflows/03-technical-specification.md) | consolida plano, ADR, spec e tarefas | `projects/<project>/plans/active/`, `engineering/specs/`, `engineering/adr/`, `work-items/` |
| [Implementação](../../../../workflows/04-autonomous-implementation.md) | orquestra tarefas e mudanças isoladas | `projects/<project>/work-items/`, `execution/evidence/`, `repos/worktrees/` |
| [Validação e PR](../../../../workflows/05-adversarial-validation.md) | consolida review técnico e integração | `projects/<project>/execution/reviews/` e `execution/evidence/` |
| [Release e observação](../../../../workflows/08-production-release-and-observation.md) | rollout, saúde e rollback | `projects/<project>/execution/evidence/` e `LEARNINGS.md` (candidatos) |
| [Conhecimento e melhoria](../../../../workflows/10-continuous-improvement.md) | consolida telemetria e propostas | `projects/<project>/LEARNINGS.md` |

`..coordination/` mantém somente estado de trânsito. Handoffs persistentes ficam em `projects/<project>/execution/handoffs/`; código e worktrees ficam em `repos/`, nunca em `projects/`.
