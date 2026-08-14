# Templates

Central catalog of all artifact templates documented in the repository, organized by role.

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
- [`design.md`](ux/design.md) — visual components, tokens, states and behaviors

In any of the three, copy the template to the project and replace the fields with `<...>`.

## Templates that don't live here

Templates that are an artifact of a specific skill are within the skill itself, not in this catalog — they are part of the [skill anatomy](../skills/README.md#3-anatomy-of-a-skill) and are referenced by relative path from within `SKILL.md`.

- [`skills/business-discovery/templates/`](../skills/business-discovery/templates/) — `requisitos.md`, `roteiro-agenda.md`, `exemplo-preenchido.md`

## Originals and sync

This catalog is a **copy** of the templates for each workspace. The source of each file remains the original within the respective workspace:

| Paper | Original |
|---|---|
| PM | [`workspaces/pm/docs/templates/`](../workspaces/pm/docs/templates/README.md) |
| Tech Lead | [`workspaces/tech-lead/kb-store/templates/`](../workspaces/tech-lead/kb-store/templates/README.md) |
| UX | [`workspaces/ux/docs/templates/`](../workspaces/ux/docs/templates/README.md) |

As there are two independent copies, a change in a template needs to be manually replicated on the other side (`templates/<papel>/` ↔ `workspaces/<papel>/docs/templates/`) to avoid divergence.
