---
name: implement
description: Implements a block of a technical plan with incremental validation and updated tracking. Use when there is an approved implementation plan and SPEC; does not publish commits or PRs without explicit request.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Implement the code following the implementation plan, block by block, with incremental validation.

## Artifact contract

Resolve the plan, SPEC and tracking according to [the shared contract](../references/workflow-contract.md).

## Inputs

- **Required:** `teamwork/plan/feature-plan-<feature-slug>/plano-implementacao.md`
- **Required:** `.agents/spec/<feature-slug>/SPEC.md`
- **Required:** `teamwork/plan/feature-plan-<feature-slug>/tracking.md`
- **Optional:** specific block to implement (via `$ARGUMENTS`)

## Execution Steps

### 1. Find the feature and plane

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from the context.
- Read `plano-implementacao.md`, `SPEC.md` and `tracking.md`.

### 2. Identify block to implement

- If `$ARGUMENTS` specifies a block, implement only that one.
- Otherwise, implement the next uncompleted block of the plan.
- Check dependencies: dependent blocks must be ✅ before starting.

### 3. Implement the block

For each action within the block:

1. **Before writing code:**
   - Read existing files that will be modified.
   - Understand existing conventions, standards and imports.
   - Check for relevant existing tests.

2. **Write the code:**
   - Follow repository conventions.
   - Small, incremental changes.
   - Prefer modifying existing code rather than creating new code when possible.

3. **After each change:**
   - Check that the code compiles/runs without obvious errors.
   - Run lint/format if available.

### 4. Block validation

After implementing all block actions:

- Run relevant tests (if they exist).
- Validate against the block acceptance criteria in the plan.
- If there is an error, correct it before moving forward.

### 5. Update tracking

After completing the block:
- Update `tracking.md`: status → ✅, end date.
- If blocked: status → ❌, describe the block in the log.

### 6. Progression

- After completing a block, proceed to the next (respecting dependencies).
- If `$ARGUMENTS` asked for specific block, stop when finished.

### 7. Report in chat

- Summary: block implemented, files created/modified.
- Tests performed and results.
- Next recommended block.
- If blocked: description of the problem and suggestion.

## Rules

- **Don't skip blocks** — dependencies exist for a reason.
- **Validate incrementally** — don't accumulate changes without testing.
- **Follow the plan** — if you need to deviate, document it in the tracking.
- **Small commits** — propose a commit after each completed block; only use `/commit` when the user requests registration in Git.

##DoneWhen

- [ ] Block(s) implemented according to plan
- [ ] Code follows repository conventions
- [ ] Relevant tests performed
- [ ] updated tracking.md
- [ ] Next identified block (or completed feature)
