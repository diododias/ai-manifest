---
name: write-feature
description: Extracts and slices product stories from requirements and refinement transcript, maintaining linkage to rules and criteria. Use after discovery when you need to prepare stories for PRD.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Transform `requisitos.md` + refinement schedule transcript into structured stories, ready for review and PRD generation.

## Artifact contract

Before creating stories, please follow [shared agreement](../references/workflow-contract.md).

## Inputs

- **Required:** `business-discovery/<feature-slug>/requisitos.md`
- **Required:** transcription of the refinement agenda
- **Optional:** feature name/slug (infer from requirements.md if not provided)

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from `requisitos.md`.
- Check if `business-discovery/<feature-slug>/requisitos.md` exists.

### 2. Load context

- Read `requisitos.md` in full — it is the requirements baseline.
- Read the transcript of the refinement agenda.

### 3. Extract stories from the transcript

Identify the stories discussed in the refinement agenda. For each:

- **Context:** what was discussed, decisions made, dependencies mentioned.
- **Acceptance criteria:** extracted from Gherkin scenarios and associated business rules.
- **Dependencies:** other stories, external systems, dependent teams.
- **Estimated size:** if discussed on the agenda (P1/MVP vs increments).

### 4. Map to existing requirements

For each story, link:
- RN-XX (business rules) that the story implements
- SC-XX (success criteria) that the story contributes
- US-X (user story) from `requisitos.md` that she details

### 5. Identify stories for slicing

Flag stories that:
- They are too big for a sprint
- Couple multiple flows without dependency
- Need technical spike first

### 6. Generate output

Create the `teamwork/plan/feature-plan-<feature-slug>/` directory (if it does not exist).

Generate `historias.md` in the format:

```markdown
# Stories — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>
**Baseline:** business-discovery/<feature-slug>/requisites.md
**Schedule:** <refinement schedule description>

---

## HIST-01: <Title>

**Priority:** P1/P2/P3
**Bound Requirements:** RN-XX, US-X

### Context
<what was discussed on the agenda, decisions, dependencies>

### Acceptance Criteria
- [ ] CA-01: <measurable criterion>
- [ ] CA-02: <measurable criterion>

### Dependencies
- <other stories, systems, teams>

### Notes
<observations, risks, points of attention>

---

## HIST-02: <Title>
...
```

### 7. Report in chat

- Summary: X stories extracted, Y with dependencies, Z marked for slicing.
- List of stories with priority and status.
- Points of attention (large stories, blocking dependencies).

## Conventions

- `HIST-XX` for story IDs (sequential).
- `CA-XX` for acceptance criteria per story.
- Priority: P1 = MVP, P2 = increment, P3 = future.
- Portuguese. Numerical examples > vague descriptions.
- Stories should be independent when possible.

##DoneWhen

- [ ] `historias.md` generated in `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] Each story linked to existing requirements (RN, US, SC)
- [ ] Large stories flagged for slicing
- [ ] Summary reported in chat
