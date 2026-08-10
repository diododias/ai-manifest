---
name: "update-pr"
description: "Assembles and, upon confirmation, updates the description of a pull request with context, tests, and branches. Use when the user asks to prepare or edit the description of an open PR."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Update the PR description with full context, what has been implemented, tested and documented deviations.

## Artifacts and publishing contract

Resolve the paths as per [the shared contract](../references/workflow-contract.md).
First present the proposed description; only run `gh pr edit` after
explicit confirmation. Only add labels that exist in the repository and have
been requested.

## Inputs

- **Required:** Open PR (number or branch)
- **Required:** `.agents/spec/<feature-slug>/SPEC.md`
- **Required:** context of implemented tasks
- **Optional:** `teamwork/plan/feature-plan-<feature-slug>/desvios.md`

## Execution Steps

### 1. Find the PR

- If `$ARGUMENTS` contains number, use it.
- Otherwise, find the PR of the current branch:
  ```bash
  gh pr list --head <branch-name> --json number,title
  ```

### 2. Collect context

- Read the SPEC — technical context.
- Read `desvios.md` if exists — deviations documented.
- Extract list of commits:
  ```bash
  gh pr view <number> --json commits
  ```
- Identify modified files:
  ```bash
  gh pr diff <number> --stat
  ```

### 3. Create PR description

Generate the description following the team template:

```markdown
## Summary

<objective description of what this PR does and why>

## Context

<business problem that the feature solves, referencing PRD>

## What was implemented

- [x] <item 1>
- [x] <item 2>
- [ ] <item 3> (if partial delivery)

## How to test

<concrete validation steps>

1. <step 1>
2. <step 2>
3. <expected result>

## Tests performed

- [ ] Units: <result>
- [ ] Integration: <result>
- [ ] E2E: <result> (if applicable)

## Documented deviations

<if there are deviations from plan, document here>
<reference deviations.md if extensive>

## Artifacts

- PRD: `.agents/prd/<feature>/PRD.md`
- SPEC: `.agents/spec/<feature>/SPEC.md`
- Tracking: `teamwork/plan/feature-plan-<name>/tracking.md`

##Checklist

- [ ] Code follows repository conventions
- [ ] Tests passing
- [ ] Updated PRD/SPEC (if applicable)
- [ ] No secrets or sensitive data
- [ ] Updated documentation (if applicable)

Close-ups #N
```

### 4. Update PR after confirmation

```bash
gh pr edit <number> --body-file <confirmed-temporary-file>
```

### 5. Add requested labels (if applicable)

```bash
gh label list
gh pr edit <number> --add-label "<label-existente-e-solicitada>"
```

### 6. Report in chat

- PR number and title.
- Summary of what was completed.
- Status (ready for review / needs adjustments).

## Conventions

- PR Description is the source of context for reviewers.
- Always reference the issue with `Closes #N` or `Refs #N`.
- Deviations must be transparent — do not hide.
- Portuguese for documentation.

##DoneWhen

- [ ] PR description updated with complete template
- [ ] Documented context, implementation, testing and deviations
- [ ] Reference to issue included
- [ ] Labels applied (if applicable)
- [ ] Status reported in chat
