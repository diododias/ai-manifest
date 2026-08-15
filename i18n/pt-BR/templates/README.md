# Templates

Catálogo central de todos os templates de artefato documentados no repositório, organizados por papel.

## PM — [`pm/`](pm/README.md)

- [`product-brief.md`](pm/product-brief.md)
- [`prd.md`](pm/prd.md)
- [`decision-brief.md`](pm/decision-brief.md)

## Tech Lead — [`tech-lead/`](tech-lead/README.md)

- [`adr.md`](tech-lead/adr.md)
- [`plan.md`](tech-lead/plan.md)
- [`spec.md`](tech-lead/spec.md)
- [`work-item.md`](tech-lead/work-item.md)
- [`handoff.md`](tech-lead/handoff.md)

## UX — [`ux/`](ux/README.md)

- [`research-plan.md`](ux/research-plan.md)
- [`ux-spec.md`](ux/ux-spec.md)
- [`validation-report.md`](ux/validation-report.md)
- [`design.md`](ux/design.md) — componentes visuais, tokens, estados e comportamentos

Em qualquer um dos três, copie o template para o projeto e substitua os campos entre `<...>`.

## Templates que não vivem aqui

Templates que são artefato de uma skill específica ficam dentro da própria skill, não neste catálogo — fazem parte da [anatomia de skill](../skills/README.md#3-anatomia-de-uma-skill) e são referenciados por caminho relativo de dentro do `SKILL.md`.

- [`skills/business-discovery/templates/`](../skills/business-discovery/templates/) — `requisitos.md`, `roteiro-agenda.md`, `exemplo-preenchido.md`

## Originais e sincronização

Este catálogo é uma **cópia** dos templates de cada workspace. A fonte de cada arquivo continua sendo o original dentro do respectivo workspace:

| Papel | Original |
|---|---|
| PM | [`workspaces/pm/docs/templates/`](../workspaces/pm/docs/templates/README.md) |
| Tech Lead | [`workspaces/tech-lead/kb-store/templates/`](../workspaces/tech-lead/kb-store/templates/README.md) |
| UX | [`workspaces/ux/docs/templates/`](../workspaces/ux/docs/templates/README.md) |

Como são duas cópias independentes, uma mudança em um template precisa ser replicada manualmente no outro lado (`templates/<papel>/` ↔ `workspaces/<papel>/docs/templates/`) para não divergir.
