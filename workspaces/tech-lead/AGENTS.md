# Agent rules

1. Read `README.md`, `WORKSPACE.md` and this file before starting a mission.
2. Before working on a project, read `CONTEXT.md` and `STATUS.md`.
3. See `engineering/repositories.yaml` to find the code involved.
4. Read the local instructions for each repository before changing it.
5. Create or assume a Work Item before modifying artifacts.
6. Register the mission's repository, branch, base and worktree in the Work Item.
7. Check Git status and preserve pre-existing changes.
8. Do not edit an artifact already taken over by another agent without explicit division.
9. Record durable decisions, validations and evidence in your official sources.
10. Produce a handoff when transferring responsibility.
11. Do not treat `memory.md` as a source of truth.
12. Only move an item to `done` when all criteria are supported.

## Mandatory skills

- Before acting, check the available skills and use all that apply; a skill available and adherent to the mission cannot be ignored. The [agent catalog](../../agents/catalog.md) lists recommended skills by role.
- Use `/workspace-memory` when starting or resuming a mission and before recording memory; use `/workspace-projects` when querying or changing `projects/`; use `/workspace-board` when choosing, taking over, blocking, transitioning, or terminating a Work Item.
- Also use the available domain skill that matches the job. Mention, in the Work Item, handoff or result, the exact names of the skills used; if no domain skills apply, record the reason.
- Record transcripts, screenshots, emails, PDFs and other raw materials from a session in `projects/<project>/plans/assets/<workflow>/<data>-<session-id>/`, never released into `plans/` or mixed with previous sessions. See [`workspace-projects`](../../skills/workspace-projects/SKILL.md).

## Minimum flow

1. Choose an item `ready` from `BOARD.md`.
2. Confirm dependencies and commit the item to the corresponding file.
3. Create branch and worktree when code changes.
4. Execute the plan, updating evidence and history.
5. Request review and validation.
6. Update `STATUS.md`, generate the necessary handoff and close the item.
