---
title: Bindings de workflows — workspace de UX
status: example
owner: ux
updated_at: 2026-08-08
---

# Workflows habilitados no workspace de UX

Este diretório referencia o [catálogo canônico](../../../../workflows/README.md). Ele registra o uso local; não replica definições nem recebe saídas de execução.

| Workflow | Papel de UX | Fonte persistente |
|---|---|---|
| [Discovery](../../../../workflows/01-discovery-and-research.md) | pesquisa, jornada e hipótese de experiência | `projects/<project>/research/` e `journeys/` |
| [Produto e UX](../../../../workflows/02-product-and-ux-planning.md) | fluxos, estados, acessibilidade e UX spec | `projects/<project>/flows/`, `specifications/`, `prototypes/` e `validation/` |
| [Validação](../../../../workflows/05-adversarial-validation.md) | evidencia critérios de UX quando acionado | `projects/<project>/validation/` |
| [Homologação](../../../../workflows/07-release-candidate-validation.md) | decide aceite de experiência | `projects/<project>/validation/` |
| [Conhecimento e melhoria](../../../../workflows/09-knowledge-curation.md) | promove aprendizado de experiência | fonte canônica do projeto |

Handoffs temporários usam `..coordination/`; handoffs de um projeto usam `projects/<project>/handoffs/`. UX não duplica PRD, plano técnico ou evidência de CI: referencia as fontes do PM e do Tech Lead.
