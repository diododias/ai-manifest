# Requirements — <Feature name>

- **Epic:** <epic> · **Status:** 🟡 under discovery
- **Updated:** YYYY-MM-DD · **Schedules:** [YYYY-MM-DD]
- **Participants:** <names>

## Context & objective
<What pain solves, for whom, what is the expected result. 2–4 lines. The metric
with number is in Success criteria (SC-XX).>

## Glossary / domain
- **<Term>** — <definition>. Check *(exists)* if it is already a system entity,
  *(new)* is born here. When the agenda sets, register identity/uniqueness
  and key attributes.

## User stories & scenarios
> Each story carries its scenarios in **Given · When ·
> Then). **So** is the observable result — if the agenda didn’t work, it’s a gap; no
> invent the result.

- **US-1** *(Priority: P1)* As <role>, I want <action>, for <benefit>.
  - *Independent test:* <how to validate this story alone> *(optional)*
  - **Scenarios:**
    1. **Given** <initial state>, **When** <action>, **Then** <observable result>.
    2. *(exception)* **Given** <state>, **When** <action>, **Then** <treatment>.

## Business rules
> Write each RN with precondition + trigger + system response, then clause
> missing becomes a gap (don't make it up). Obligation marker = "<system> **must**
> <response>". Patterns:
> - **Ubiquitous:** the <system> must <response>. *(always active, no keyword)*
> - **State:** **While** <precondition>, <system> must <response>.
> - **Event:** **When** <trigger>, <system> must <response>.
> - **Optional:** **Where** <feature/variant present>, <system> must <response>.
> - **Unwanted:** **If** <trigger>, **then** <system> should <response>.
> - **Composite:** **While** <pre>, **when** <trigger>, the <system> must <response>.
>
> The structured rule = the obligation; the Gherkin **Given/When/Then** (in Scenarios)
>= the example that tests it. "When/Then" appear in both layers — the RN is
> declarative and has "must"; the scenario is the sequence Given→When→Then. Each RN
> needs a concrete example and ≥1 scenario that verifies it (RN ↔ US screening).
- **RN-1** When <trigger>, <system> must <response>. *Ex: <concrete/numeric example>.* *(checks: US-1 scenario 1)*

## Flows
**Happy:** <journey end to end>.
**Exceptions / edge cases:** <errors, limits, invalid states, concurrency, empty>.

## Success criteria (measurable)
> Business results, with numbers and without technology. Unlike the scenario (which is
> binary/testable); here is the target that tells you whether the feature worked.
- **SC-1** <metric with target>. *Ex: 30% of subscribers convert within 7 days.*

## Out of scope
<Which is explicitly NOT supposed to be done.>

## Open questions
- **DA-1** <question>? *(owner: <who> · deadline: <when>)*

## ⚠️ Gaps detected in transcription
<References cited but not defined; rules without example; scenarios without "Then"
clear; vague adjectives without numbers ("quick", "easy"); RN without a scenario that
check. Each with "confirm".>

## Changelog by schedule
- **YYYY-MM-DD** — <delta: what entered / changed / contradicted>.
