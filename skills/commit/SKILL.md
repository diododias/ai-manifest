---
name: "commit"
description: "Prepare and create a commit with explicit scope and repository conventions. Use when the user asks to commit changes to Git; only send to the remote if it asks for a push."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Create clear commits following repository conventions, with reference to the issue when applicable.

## Inputs

- **Required:** modified code (git status)
- **Optional:** personalized message via `$ARGUMENTS`
- **Optional:** issue number

## Execution Steps

### 1. Check status

```bash
git status
git diff --stat
```

- Identify all modified/created/deleted files.
- Check for files that should not be committed (secrets, temp).

### 2. Select files

- Add only files relevant to the feature.
- Never commit secrets, sensitive configs or temporary artifacts.
- Use `git add <file>` for explicit selection (avoid `git add .`).

### 3. Assemble commit message

Follow the repository convention:

```
<type>(<scope>): <short description>

<optional body>

Ref #<issue>
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

**Types:** `feat`, `fix`, `chore`, `test`, `refactor`, `docs`, `style`, `perf`

**Rules:**
- First line: max 72 characters, imperative, without period.
- Body: explains the “why” (not the “what”).
- Reference to issue: `Refs #N` (partial) or `Closes #N` (complete).
- Co-Authored-By: when applicable (I work with AI).

### 4. Execute commit

- Show selected files and proposed message before commit if the
  user has not explicitly authorized the commit.

```bash
git commit -m "feat(feature-slug): short description

Body of the commit explaining the change.

Refs #N"
```

### 5. Push

- Push only when the user explicitly requests it or when they
  you have authorized publishing as part of the task.
- Before uploading, confirm remote branch and that there are no files left
  listed in the index.

```bash
git push origin <branch-name>
```

- Do not assume that CI opens PR nor that the base is `develop`.
- If there is manual PR, propose the next step; do not open it implicitly.

### 6. Report in chat

- Short commit hash.
- Files included.
- Branch and push status.

## Conventions

- One logical commit = one unit of change.
- Does not output "WIP" or "temp" — clean first.
- Messages in Portuguese (or English if it is the repo's default).
- Always reference the issue when it exists.

##DoneWhen

- [ ] Correctly selected files
- [ ] Message follows repository convention
- [ ] Commit completed successfully
- [ ] Push completed, when requested
- [ ] Hash of the reported commit
