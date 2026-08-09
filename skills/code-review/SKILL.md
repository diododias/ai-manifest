---
name: "code-review"
description: "Reviews code changes against SPEC, tests and risks, producing actionable findings without modifying the code. Use before human review or when the user requests a technical review of a feature or PR."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Adversarially review code before it reaches human reviewers, verifying SPEC compliance, quality, and test coverage.

## Artifact contract

Resolve artifacts as per [shared contract](../references/workflow-contract.md).

## Inputs

- **Required:** `.agents/spec/<feature-slug>/SPEC.md`
- **Required:** implemented code (branch diff)
- **Required:** tests performed
- **Optional:** description of the PR (if it already exists)

## Execution Steps

### 1. Collect context

- Read the SPEC — technical requirements and acceptance criteria.
- Discover the base of the PR (`gh pr view --json baseRefName`) or the branch configured in the repository; then use `git diff <base>...HEAD`. Do not assume `main` or `develop`.
- Read created/modified tests.

### 2. Layered Review

#### A. SPEC Compliance
For each implemented block:
- Does the code implement what the SPEC defines?
- Are technical acceptance criteria (CT-XX) met?
- Is the data model correct?
- Do interface contracts match SPEC?

#### B. Code Quality
- Does the code follow repository conventions?
- Are functions/methods clear and well named?
- Is there no unnecessary code duplication?
- Adequate error handling?
- Edge cases treated?

#### C. Security
- Input validation present?
- Hardcoded secrets/credentials?
- SQL injection, XSS, CSRF?
- Proper authorization/authentication?

#### D. Performance
- Do you want N+1?
- Blocking operations?
- Adequate cache?
- Potential infinite memory/loop?

#### E. Tests
- Does all CT-XX have a test?
- Are tests meaningful (not just pass)?
- Edge cases tested?
- Suitable mocks/stubs?

### 3. Classify findings

- **BLOCKER:** Must be fixed before PR (bug, security, SPEC violation)
- **REVIEW:** Reviewers must check (design, standard, performance)
- **SUGGESTION:** Optional improvement (refactoring, optimization)
- **PRAISE:** Well-written code (positive reinforcement)

### 4. Generate report

Generates `teamwork/plan/feature-plan-<feature-slug>/code-review.md`:

```markdown
# Code Review — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>
**Branch:** <branch name>
**Commits:** <quantity>

---

## Summary

| Category | Quantity |
|-----------|-----------|
| 🔴 BLOCKER | X |
| 🟠 REVIEW | X |
| 🟡SUGGESTION | X |
| 🟢 PRAISE | X |

**Recommendation:** ✅ Approve / 🔄 Review / ❌ Reject

---

## SPEC Compliance

| Block | CT-XX | Status | Note |
|-------|-------|--------|------------|
| ... | CT-01 | ✅ / ⚠️ / ❌ | ... |

---

## Findings

### 🔴 BLOCKER

#### B-01: <Title>
- **File:** `path/line`
- **Problem:** <description>
- **Suggestion:** <how to fix>

### 🟠 REVIEW

#### R-01: <Title>
...

### 🟡 SUGGESTION

#### S-01: <Title>
...

### 🟢 PRAISE

#### P-01: <Title>
<what is ok and why>

---

## Test Coverage

| CT-XX | Criterion | Test | Status |
|-------|----------|-------|--------|
| CT-01 | ... | ... | ✅ / ❌ |

---

## Approval Material

<if requested, generate material following the team template>

### Change Summary
<what changed and why>

### How to Test
<validation steps>

### Impact
<affected areas, risks>

---

## Final Recommendation

<justification for recommendation>
```

### 5. Report in chat

- Summary: X blockers, Y review, Z suggestions.
- Recommendation: approve, review or reject.
- Blockages that need resolution.

## Conventions

- Review is adversarial — try to find problems.
- Never silence blockers — always report.
- Praise is important — reinforces good practices.
- Portuguese for documentation.
- Approval material follows the team template when requested.

##DoneWhen

- [ ] Review performed on all layers
- [ ] Verified SPEC compliance
- [ ] Classified findings (BLOCKER/REVIEW/SUGGESTION/PRAISE)
- [ ] `code-review.md` generated
- [ ] Approval/revision/rejection recommendation reported
