#BusinessDiscovery

Gathering business requirements from agendas with the PM, in order to
**accumulative**: each meeting updates one live document per feature, instead of
a loose summary by transcription.

## Why

As you and the PM already share a history, the agenda only talks about a part of the
demands and references things without defining. Transcript + one-shot summary remains
shallow. Here, the context of previous agendas remains in the document, and the
unresolved references become explicit gaps — not hidden assumptions.

## Flow

1. **Before the agenda** — fill in `templates/roteiro-agenda.md`. He forces
   make the implicit context explicit (the biggest gain in assertiveness).
2. **During** — record and follow the script. Ask the PM for concrete examples of the rules
   and say "business rule:" before each one.
3. **After** — generate the transcription and run the skill:
   `/business-discovery <transcript-path>`.
4. **Review** — check out the `⚠️ Gaps detectados` section and the `DA-XX`: this is the list of
   questions to take to the next agenda.

## Structure

```
business-discovery/
  README.md this file
  templates/
    script-agenda.md agenda to prepare the agenda
    requirements.md output document format (blank)
    example-preenchido.md filled reference (fake)
  <feature-slug>/
    requisites.md living document, updated every schedule
```

The skill that orchestrates this lives in `.claude/skills/business-discovery/`.

## Conventions

- `RN-XX` business rules · `US-X` user stories (priority P1/P2/P3) ·
  `SC-XX` measurable success criteria · `DA-X` open doubts.
- Structured rules (RN) (precondition + trigger + response +
  "the system **must**"); acceptance scenarios in Gherkin pt-BR: **Given / When / Then**.
- Status: 🟡 in discovery · 🟢 ready to specify · ✅ turned into spec.
- `requisitos.md` changelog is **append-only** — preserves history of how
  understanding evolved between agendas.
- The format mirrors the PRD produced by the skill `review-prd` (see "Handoff for
  review-prd and create-spec" in SKILL.md) — the 🟢 feature feeds `/review-prd`
  and then `/create-spec` straight.
