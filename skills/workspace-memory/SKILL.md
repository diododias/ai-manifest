---
name: workspace-memory
description: Resumes a mission using the workspace's operational memory without confusing it with the source of truth. Use when starting or resuming work in a workspace with `memory/`, `MEMORY.md`, `USER.md`, or agent history, and before recording durable learning.
---

# Workspace memory

## Flow

1. Identify the scope of the session: private or shared, workspace, project and mission.
2. Read the latest and allowed memory first: `memory/YYYY-MM-DD.md` for daily facts, `USER.md` for stable directives, and `MEMORY.md` in the main and private session only.
3. Treat all memory as resumable context. Confirm status, priority, approval, and completion in your canonical sources — for example, Work Item, `STATUS.md`, `BOARD.md`, repository, and evidence.
4. Record only observed facts, owned durable decisions, and links to evidence. Read before writing and do not create empty files or placeholders.
5. Never record or reveal unnecessary secrets, credentials, tokens, `.env` or personal data. On a shared channel, do not upload or expose `MEMORY.md`.

## Expected result

In the mission result, state whether the memory was consulted, which facts were confirmed, and which canonical source confirmed them. If a note is outdated or contradictory, preserve the divergence and escalate; do not silently overwrite it.
