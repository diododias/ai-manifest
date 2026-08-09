---
name: review-prd
description: Consolidates requirements and stories into a PRD with trackable goals, rules, and success criteria. Use after discovery and product refinement, before technical specification.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Consolidate the PRD Plan based on the written stories and `requisitos.md`, validating that all requirements are covered.

## Artifact contract

Before creating the PRD, follow [the shared agreement](../references/workflow-contract.md).

## Inputs

- **Required:** `teamwork/plan/feature-plan-<feature-slug>/historias.md`
- **Required:** `business-discovery/<feature-slug>/requisitos.md`
- **Optional:** transcription of the refinement agenda (for additional context)

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from artifacts.
- Check if the input files exist.

### 2. Load context

- Read `historias.md` — basis for the PRD.
- Read `requisitos.md` — baseline requirements for coverage validation.

### 3. Consolidate the PRD

Create `.agents/prd/<feature-slug>/PRD.md` (create directories if necessary) in the format:

```markdown
# PRD — <Feature Name>

**Feature:** <slug>
**Status:** 🟡 Under review
**Date:** <YYYY-MM-DD>
**Author:** PM (via review-prd)

---

## 1. Objective

<clear description of the business problem that the feature solves, extracted from the context of the stories and requirements>

## 2. Stories

| ID | Title | Priority | Requirements |
|----|------------|------------|------------|
| HIST-01 | ... | P1 | RN-XX, US-1 |
| HIST-02 | ... | P2 | RN-YY, US-2 |

### HIST-01: <Title>

<context, acceptance criteria, dependencies — copy from historias.md>

## 3. Success Criteria

| ID | Metric | Target | History |
|----|---------|------|----------|
| SC-01 | ... | ... | HIST-XX |

## 4. Business Rules

| ID | Rule | Example | Scenario |
|----|-------|---------|---------|
| RN-01 | ... | ... | <Gherkin scenario> |

## 5. Out of Scope

<items explicitly out of scope, taken from requirements.md>

## 6. Gaps and Issues

| ID | Description | Status |
|----|-----------|--------|
| DA-01 | ... | ⏳ Open |

## 7. Flows

### Happy Path
<main flow>

### Exceptions
<exception flows and edge cases>

## 8. Glossary

| Term | Definition |
|-------|-----------|
| ... | ... |
```

### 4. Validate coverage

Compare PRD against `requisitos.md`:

- Are all US-X linked to at least one story?
- Do all RN-XX appear in the PRD?
- Are all SC-XX story-bound?
- Have Gaps/DA-XX been transferred?

List covered and not covered.

### 5. Report in chat

- Summary: X consolidated stories, Y linked rules, Z SC defined.
- List of requirements not covered (if any).
- PRD status (ready for review / needs adjustments).

## Conventions

- PRD follows the team's standard format.
- Each story maintains traceable link to requirements (RN, US, SC).
- Status: 🟡 Under review → 🟢 Approved → ✅ Implemented.
- Portuguese. Gherkin pt-BR for scenarios.

##DoneWhen

- [ ] `PRD.md` created in `.agents/prd/<feature-slug>/`
- [ ] Validated coverage: all `requisitos.md` requirements mapped
- [ ] Gaps/DA-XX transferred to pending section
- [ ] Summary reported in chat
