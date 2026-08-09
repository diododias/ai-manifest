---
name: "fix-bug"
description: "Fixes a documented bug with regression testing and local validation. Use when there is evidence or analysis of a bug and the user asks for the fix to be implemented; commit and PR require publish request."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Implement the bug fix following the standard flow (implement → test → commit → PR), ensuring coverage per test.

## Inputs

- **Required:** `bugs/bug-<NOME-SLUG>.md` (bug analysis)
- **Required:** affected code (local repository)

## Execution Steps

### 1. Upload analysis

- Read `bug-<NOME>.md` — root cause and affected component.
- Identify files that need to be modified.

### 2. Check if there is a test that reproduces the bug

- Run existing tests for the affected component.
- Check if any tests already cover the scenario (and are failing or passing incorrectly).
- If there is no test that reproduces, create one before correcting (TDD).

### 3. Create regression test

Create test that:
- Reproduces the bug (should fail with current code).
- Validates correct behavior (should pass after correction).
- Follows repository testing standards.

### 4. Implement the fix

- Follow the direction suggested in the analysis (or adjust if necessary).
- Minimal, focused changes — don't refactor unnecessarily.
- Follow repository conventions.

### 5. Validate

- Run the regression test — it should pass.
- Run all component tests — there should be no regression.
- Check if the original bug is resolved.

### 6. Propose publication

After the correction is validated, inform the publication steps:

1. **Commit** — use `/commit` with message `fix(<scope>): <description>` + `Refs #<issue>` if the user requests a commit.
2. **PR** — use `/update-pr` or propose a new PR only if the user requests publication.

### 7. Update bug analysis

Update `bugs/bug-<NOME>.md`:
- Status: 🟡 Reviewed → ✅ Fixed
- Add correction date
- Reference the PR/commit

### 8. Report in chat

- Summary: bug fixed, root cause, change made.
- Regression test created.
- PR/commit referenced.
- If the correction is partial or needs follow-up.

## Conventions

- Always create test before fixing (or confirm that it exists).
- Fixes are minimal — do not refactor during the fix.
- Commit follows `fix(...)` pattern.
- If the bug has an issue, reference it in the commit and PR.
- Portuguese.

##DoneWhen

- [ ] Bug analysis loaded
- [ ] Regression test created (or existing validated)
- [ ] Correction implemented and validated
- [ ] Tests run without regression
- [ ] Next publication step informed
- [ ] Updated bug analysis with status ✅
- [ ] Result reported in chat
