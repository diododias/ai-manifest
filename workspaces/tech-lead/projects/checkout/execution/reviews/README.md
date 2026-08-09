# Reviews

Record here the review opinions generated during adversarial validation — both of the specification and the implementation. The Work Item's `review` state only ends when all pending issues are resolved.

## Naming convention

```text
execution/reviews/<tipo>-<id>.md
```

| Type | When to create | Example |
|---|---|---|
| `spec-<SPEC-id>` | Adversarial TL spec review (Round C) | `spec-SPEC-001.md` |
| `code-<WI-id>` | Code Reviewer in adversarial validation (Round E) | `code-WI-031.md` |
| `security-<WI-id>` | Security Review Agent (Round E) | `security-WI-031.md` |
| `architecture-<WI-id>` | Architecture Review Agent (Round E) | `architecture-WI-031.md` |
| `qa-<WI-id>` | QA/Validation Agent — consolidated evidence pack (Round E) | `qa-WI-031.md` |

## Minimum structure of a review file

```markdown
---
type: <spec|code|security|architecture|qa>
ref: <SPEC-id or WI-id>
reviewer: <agent name>
status: <open|resolved|exception>
date: <YYYY-MM-DD>
---

## Findings

| # | Severity | Description | Action | Resolution |
|---|---|---|---|---|

## Gate recommendation

<approved / goes back to implementation / exception to Tech Lead>
```

## Rules

- Each agent records its own file; QA Agent consolidates the evidence pack into `execution/evidence/<WI-id>.md`.
- An open find blocks the gate. Resolution requires referenced evidence, not just text.
- Spec reviews stay here even after the specification is approved — they are an auditable trail of the iteration.
