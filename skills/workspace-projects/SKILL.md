---
name: workspace-projects
description: Finds the canonical source of a project, updates only the artifact belonging to the correct domain, and organizes isolated session assets by execution. Use when a mission mentions `projects/`, CONTEXT.md, STATUS.md, requirements, UX, plans, Work Items, evidence, transcripts, printscreens, or repositories linked to a project.
---

# Workspace projects

## Project entry

1. Locate the project by portfolio, `BOARD.md` or explicit reference. Do not infer the slug solely from the name of a repository.
2. Read `projects/<project>/README.md`, `CONTEXT.md` and `STATUS.md` before taking action. Confirm the domain owner and links to PM, UX and Tech Lead entries.
3. Consult `engineering/repositories.yaml` or the equivalent registry before opening or changing code. Also read the local repository instructions.

## Canonical source and target

- Maintain value, priority and requirements in the PM workspace; research, flows and validation of UX experience; architecture, plans, implementation and risk in the Tech Lead.
- Use snapshots only as identified input. Follow the link to the canonical source before making decisions or updating it.
- Write persistent artifacts to `projects/<project>/`; use `.coordination/` only for temporary transit and handoff. Do not duplicate authoritative information between workspaces.
- Relate Work Item, repository, branch, base, worktree, evidence and handoffs to the artifact that governs them.

## Session assets

- All material from an execution — both what the human brings and what the AI generates before the gate — goes into `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`, never released into `plans/` or mixed with the final artifact.
- The cutoff rule is not who generated it, but whether it passed through the gate: before the gate it goes to `plans/assets/`, after the gate it goes to the canonical destination (`engineering/`, `product/`, `ux/`, `plans/active/`).
- `<workflow>` identifies the workflow or skill that generated the material (e.g.: `00-intake-and-triage`, `business-discovery`, `technical-discovery`). `<session-id>` is a short and unique run identifier (mission_id or run id); never reuse the folder from a previous session, even if the result has been discarded.
- Use subfolders by type within the session folder only when there is more than one file of the same type: `transcripts/` (meeting or session transcripts), `drafts/` (AI-generated intermediate drafts), `screenshots/`, `emails/`, `documents/`. A single file can be located in the root of the session folder.
- Assets are not a canonical source: they are supporting evidence and an auditable trail. The extracted conclusion, decision, or requirement goes to the correct domain artifact; reference the asset path instead of copying the raw content.
- Adversarial reviews do not stay in `plans/assets/` — they are formal artifacts with their own gate and go to `execution/reviews/<tipo>-<id>.md`.
- If the execution is repeated due to unsatisfactory results, create a new session folder and register in `STATUS.md` or in the Work Item which session supports the current version of the artifact. Discarded sessions remain in the history, but are no longer referenced.

## Closing

Update only the authorized artifact and maintain links to consulted sources. If the mission crosses domains, prepare a traceable handoff for the next owner instead of editing someone else's source.
