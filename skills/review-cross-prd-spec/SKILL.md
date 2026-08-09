---
name: review-cross-prd-spec
description: Compares PRD and SPEC, identifying coverage, conflicts and pending decisions without changing the artifacts. Use before sprint planning or when you need to prove alignment between business and technical solution.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Validate alignment between PRD and SPEC, identifying PRD requirements not covered in SPEC and conflicts between the two artifacts.

## Artifact contract

Resolve PRD and SPEC as per [the shared contract](../references/workflow-contract.md).

## Inputs

- **Required:** `.agents/prd/<feature-slug>/PRD.md`
- **Required:** `.agents/spec/<feature-slug>/SPEC.md`

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from artifacts.
- Check if the input files exist.

### 2. Upload artifacts

- Read `PRD.md` — business perspective.
- Read `SPEC.md` — technical perspective.

### 3. Cross review

#### A. PRD Coverage → SPEC
For each element of the PRD, check if there is a corresponding element in the SPEC:

| PRD element | Type | At SPEC? | Note |
|-------------|------|----------|------------|
| HIST-01 | History | ✅ / ❌ / ⚠️ Partial | ... |
| RN-01 | Rule | ✅ / ❌ | ... |
| SC-01 | Success Criteria | ✅ / ❌ | ... |

#### B. PRD ↔ SPEC Conflicts
Identify where PRD and SPEC diverge:

- **Scope:** Does SPEC implement something outside the PRD? Does PRD ask for something not addressed in SPEC?
- **Behavior:** Does SPEC define different behavior than PRD describes?
- **Data:** SPEC data model supports all PRD flows?
- **Performance:** Are PRD non-functional requirements addressed in the SPEC?

#### C. Terminology Alignment
- Same terms used in both documents?
- Consistent meaning?

#### D. Technical Decisions vs Business Requirements
- The SPEC must not change business requirements (it can only refine how to implement).
- If the SPEC "changes" a requirement, it is a conflict — report it.

### 4. Generate report

Generates `teamwork/plan/feature-plan-<feature-slug>/review-cross.md`:

```markdown
# PRD Cross Review ↔ SPEC — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>
**PRD:** .agents/prd/<feature-slug>/PRD.md
**SPEC:** .agents/spec/<feature-slug>/SPEC.md

---

## Summary

| Category | Quantity |
|-----------|-----------|
| ✅ Aligned | X |
| ⚠️ Partially covered | X |
| ❌ Not covered (PRD → SPEC) | X |
| 🔴 Conflicts | X |

**Status:** 🔴 Conflicts found / 🟡 Adjustments required / 🟢 Aligned

---

## PRD Coverage → SPEC

### Stories
| PRD | SPEC | Status | Note |
|-----|------|--------|------------|
| HIST-01 | §4.1 | ✅ / ⚠️ / ❌ | ... |

### Business Rules
| RN | Status | SPEC ref | Note |
|----|--------|----------|------------|
| RN-01 | ✅ / ❌ | §... | ... |

### Success Criteria
| SC | Status | SPEC ref | Note |
|----|--------|----------|------------|
| SC-01 | ✅ / ❌ | §... | ... |

---

## Conflicts Detected

### CONFLICT-01: <Title>
- **PRD says:** <quote from PRD>
- **SPEC says:** <SPEC quote>
- **Type:** Scope / Behavior / Data / Performance
- **Recommendation:** <how to solve>

---

## Alignment Points

- <points where PRD and SPEC are well aligned>

## Recommendations

1. <recommended action>
2. <recommended action>

## Next Steps

- Resolve conflicts before sprint planning
- Update artifacts according to resolutions
```

### 5. Report in chat

- Summary: X aligned, Y partially covered, Z not covered, W conflicts.
- Conflicts that block sprint planning.
- Priority recommendations.

## Conventions

- Report is read-only — does not modify PRD or SPEC.
- Conflicts are always reported — never resolved silently.
- Portuguese.

##DoneWhen

- [ ] `review-cross.md` generated in `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] PRD coverage → Documented SPEC (stories, RN, SC)
- [ ] Conflicts detected and classified
- [ ] Recommendations and next steps reported
