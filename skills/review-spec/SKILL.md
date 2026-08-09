---
name: review-spec
description: Reviews a SPEC against the PRD to find gaps, ambiguities, inconsistencies, and implementation risks. Use before approving the SPEC or starting the execution plan.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Analyze the SPEC in search of gaps, ambiguities and internal inconsistencies, generating a report of points to be resolved classified by severity.

## Artifact contract

Resolve PRD and SPEC as per [the shared contract](../references/workflow-contract.md).

## Inputs

- **Required:** `.agents/spec/<feature-slug>/SPEC.md`
- **Required:** `.agents/prd/<feature-slug>/PRD.md`

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from artifacts.
- Check if the input files exist.

### 2. Upload artifacts

- Read `SPEC.md` — key analysis.
- Read `PRD.md` — reference for coverage validation.

### 3. SPEC Analysis

Systematically check:

#### A. PRD Coverage
- Does each PRD story have a technical solution in SPEC?
- Is each business rule (RN-XX) handled?
- Does each success criterion (SC-XX) have a technical equivalent?

#### B. Internal Consistency
- Consistent terminology (same concept named the same)?
- Data model consistent with flows?
- Interface contracts aligned with the model?

#### C. Completeness
- Stories without technical acceptance criteria?
- Components without clear definition?
- Unhandled exception flows?

#### D. Ambiguity
- Vague terms ("fast", "scalable") without metrics?
- Unresolved placeholder (TODO, TKTK)?
- Pending technical decisions?

#### E. Feasibility
- External dependencies identified?
- Documented technical risks?
- Realistic effort estimate?

### 4. Sort by severity

- **CRITICAL:** Blocks implementation (unresolved story, invalid contract)
- **HIGH:** Impacts quality (unhandled exception, test not defined)
- **MEDIUM:** May cause rework (ambiguity, inconsistent terminology)
- **LOW:** Quality improvement (documentation, examples)

### 5. Generate report

Generates `teamwork/plan/feature-plan-<feature-slug>/review-spec.md`:

```markdown
# SPEC Review — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>
**SPEC:** .agents/spec/<feature-slug>/SPEC.md

---

## Summary

| Severity | Quantity |
|------------|-----------|
| 🔴 CRITICAL | X |
| 🟠HIGH | X |
| 🟡 MEDIUM | X |
| 🔵 LOW | X |

**Status:** 🔴 Blocked / 🟡 Necessary adjustments / 🟢 Approved

---

## Findings

### 🔴 CRITICAL

#### C-01: <Title>
- **Location:** SPEC §<section>
- **Problem:** <description>
- **Recommendation:** <how to solve>

### 🟠HIGH

#### H-01: <Title>
...

### 🟡 MEDIUM

#### M-01: <Title>
...

### 🔵 LOW

#### L-01: <Title>
...

---

## PRD Coverage → SPEC

| PRD History | At SPEC? | Note |
|-------------|----------|------------|
| HIST-01 | ✅ / ❌ | ... |

## Next Steps

- <actions to resolve CRITICAL>
- <actions to resolve HIGH>
- <general recommendations>
```

### 6. Report in chat

- Summary: X findings (Y critical, Z high).
- Blocks that need resolution before moving forward.
- General status (locked / adjustments / approved).

## Conventions

- Report is read-only — does not modify the SPEC.
- Classification by severity is subjective but must be consistent.
- Portuguese.

##DoneWhen

- [ ] `review-spec.md` generated in `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] All findings classified by severity
- [ ] PRD → SPEC coverage documented
- [ ] Status and next steps reported
