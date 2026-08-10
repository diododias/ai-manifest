---
name: dev-flow
description: Guides the safe flow of developing a task, from planning to local delivery and publication proposal. Use when the user requests end-to-end coordination of an implementation, fix, or feature.
---

# Skill: Development flow

This skill guides the standard flow when pulling a task, from planning to delivery
location. Handle issue creation, commit, push, PR, merge and worktree cleanup
as separate actions, performed only when authorized by the user.

## Objective

Ensure each task follows the flow:

1. PLAN
2. TRACKING (if requested)
3. IMPLEMENTATION
4. TEST
5. COMMIT (if authorized)
6. PROPOSE PUBLICATION
7. PR/MERGE (if authorized)
8. TERMINATE SAFELY
9. NEXT TASK

## Usage

When starting a task, follow these steps in order and confirm each step before
to move on to the next. Repository local convention overrides examples
branch, CI or issue below.

## Security and artifact contract

Follow [shared agreement](../references/workflow-contract.md). Before
any external effect, present the target and ask for explicit authorization:
create/edit issue, commit, push, open/edit PR, apply labels, merge,
close issue or remove worktree. Never discard, stash or remove changes
user to leave the tree clean.

### 1. PLAN
- Read the task and understand the scope, acceptance criteria and restrictions.
- Identify dependencies and possible impacts on modules/backend/storefront.
- Define what must be done in a small checklist.
- Choose/validate the correct branch name if it doesn't already exist.

### 2. TRACKING (if requested)
- If the demand already has an issue, use it as a reference.
- If the user requests tracking, propose an issue with title and body before creating it.
- Use `gh issue create` with an objective title and body containing:
  - **Context**: the "why" of the demand.
  - **Scope**: `- [ ]` checklist with each deliverable (allows visible partial closure).
  - **Acceptance criteria**: how to validate.
- Capture the issue number (`#N`) when it exists; do not invent or require an issue to implement locally.

```bash
gh issue create \
  --title "feat(scope): short description" \
  --body "$(cat <<'EOF'
## Context
<why>

## Scope
- [ ] item 1
- [ ] item 2

## Acceptance criteria
- ...
EOF
)"
```

- If the task already has an issue, reuse it. Propose the assignment of person responsible, but do not edit it without authorization.

### 3. IMPLEMENT
- Write the code to solve the problem simply and clearly.
- Prefer small changes and incrementally increase the scope.
- Follow repository conventions and existing architecture.
- If you need to change the backend and frontend, make small and organized commits.

### 4. TEST
- Create or update tests to cover new functionality or fix.
- Run relevant local tests (`pnpm test` in the right package or specific test case).
- Ensure that there is no regression in the affected areas.

### 5. COMMIT (if authorized)
- Make clear commits in Portuguese, using the repository standard:
  - `feat(...)`, `fix(...)`, `chore(...)`, `test(...)`
- The commit text must describe what was changed.
- Include `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>` when applicable.
- Reference the issue in the commit footer when useful: `Refs #N`.

### 6. PROPOSE PUBLICATION
- Summarize the diff, tests and current branch. Propose the necessary commit and publication.
- Do not assume that there is automatic CI, branch `develop` or issue linked.

### 7. PR/MERGE (if authorized)
- Open or update the PR only after explicit authorization.
- Discover the base branch in the repository configuration or in the PR; don't pin `develop`.
- **Mandatory**: the body of the PR must contain an auto-close keyword pointing to the issue:
  - `Closes #N` — closes the issue when merging the PR (complete delivery).
  - `Refs #N` — reference without closing (partial delivery; manually mark items `- [x]` completed in the issue).
- Explain the change, where to test and which test cases were executed.
- Mark the PR for review.

```bash
gh pr create\
  --base <branch-base-committed> \
  --title "feat(scope): description" \
  --body "$(cat <<'EOF'
## Summary
<what changed and why>

## How to test
- ...

Close-ups #N
EOF
)"
```

 - Before merging, confirm required checks, approvals, base branch and the SHA of the PR.
 - Never push directly to a protected branch; use the PR merge mechanism after authorization.
 - For partial delivery, propose updating the issue; do not change it without authorization.

### 8. END SAFELY
- Enter `git status` and leave unrelated changes intact.
- Only remove temporary artifacts created in this task and only with authorization.
- Do not remove worktree, do not stash and do not discard changes as an automatic step.

### 9. NEXT TASK
- Update `TRACKING.md` (status, test count, NEXT → DONE).
- Check if the issue has been closed (or partially updated).
- Do not choose or start a new task without a user request.
- Start the next PLANNING cycle.

## Quick summary

- Plan first.
- Create or update issue only when requested.
- Implement with minimum viable focus.
- Test before committing.
- Propose commit, PR or merge with target and evidence; execute only with authorization.
- Preserve the working tree and close by reporting its status.
