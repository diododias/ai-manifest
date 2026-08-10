---
name: "check-pr"
description: "Queries, without modifying, the status of a pull request, its revisions, resolved threads and checks. Use when the user requests status, pending issues or blocks of an open PR."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Check the current status of the PR review, identify pending issues and summarize what needs to be done.

## Inputs

- **Required:** Open PR (number or branch)

## Execution Steps

### 1. Find the PR

- If `$ARGUMENTS` contains number, use it.
- Otherwise, find the PR of the current branch:
  ```bash
  gh pr list --head <branch-name> --json number,title,state
  ```

### 2. Collect PR information

```bash
# General status
gh pr view <number> --json state,reviewDecision,mergedAt,closedAt,isDraft

# Reviews
gh pr view <number> --json reviews --jq '.reviews[] | {author: .author.login, state: .state, body: .body}'

# Thread repository
OWNER=$(gh repo view --json owner --jq '.owner.login')
REPO=$(gh repo view --json name --jq '.name')

# Inline threads (includes path, line and resolution)
gh api graphql -f query='query($owner:String!, $repo:String!, $number:Int!) { repository(owner:$owner, name:$repo) { pullRequest(number:$number) { reviewThreads(first:100) { nodes { isResolved comments(first:100) { nodes { author { login } body path line } } } } } } }' -f owner="$OWNER" -f repo="$REPO" -F number=<number>

# Check CI
gh pr checks <number>
```

### 3. Analyze status

#### Reviews
| Reviewer | Status | Action |
|---------|------------|------|
| reviewer1 | ✅ APPROVED | — |
| reviewer2 | 🔄 CHANGES_REQUESTED | Check comments |
| reviewer3 | ⏳ PENDING | Waiting |

#### Unresolved comments
| Comment | Archive | Line | Resolved? |
|-----------|------------|-------|------------|
| ... | ... | ... | ✅ / ❌ |

#### CI/CD
| Check | Status |
|-------|--------|
| build | ✅ / ❌ |
| test | ✅ / ❌ |
| lint | ✅ / ❌ |

### 4. Identify pending issues

- Unresolved inline threads; do not infer resolution from general comments.
- CI checks failing.
- Draft status (if applicable).
- Merge blockers (branch protection, missing approvals).

### 5. Generate summary

```markdown
# PR Status #<number> — <Title>

**Branch:** <branch>
**Status:** Open / Draft / Approved / Changes Requested

---

## Reviews

| Reviewer | Status | Date |
|---------|------------|------|
| ... | ... | ... |

## Pending

### Comments to be resolved
- [ ] <comment 1> — <file>:<line>
- [ ] <comment 2> — <file>:<line>

### CI/CD
- [ ] <check failed> — <error>

### Approvals
- ✅ X of Y approvals required

## Next Steps

1. <action 1>
2. <action 2>
```

### 6. Report in chat

- Summary: general status, approvals, pending issues.
- Comments that need action.
- CI checks that are failing.
- Estimation of ready for merge.

## Conventions

- Do not modify the PR — read only.
- Status is a snapshot at the time of the query.
- Portuguese.

##DoneWhen

- [ ] Verified PR status (reviews, comments, CI)
- [ ] Pending issues identified and listed
- [ ] Summary of next steps generated
- [ ] Status reported in chat
