# Session assets

Raw material that supports the analyzes and discussions of a workflow — transcriptions, printscreens, emails, PDFs, Word documents and the like — stays here, isolated by execution.

## Convention

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: name of the workflow or skill that generated the material, for example `00-intake-and-triage` or `business-discovery`.
- `<session-id>`: short and unique identifier of the run (`mission_id` or run id). Re-executing the workflow due to unsatisfactory results creates a **new** folder; the previous one remains in the history, but is no longer referenced by the current artifact.
- Subfolders by type (`transcripts/`, `screenshots/`, `emails/`, `documents/`) only when there is more than one file of the same type in the session.

## Rules

- `plans/assets/` is not canonical source. The extracted conclusion, decision or requirement goes to `discovery/`, `requirements/`, `strategy/` or `roadmap/`; the asset remains as an auditable trail, referenced by path.
- Never reuse the folder from a previous session, even if the result has been discarded.
- `STATUS.md` or the corresponding Work Item indicates which session supports the current version of an artifact, when this is not obvious.

## Example

```text
plans/assets/business-discovery/2026-08-08-b7e410/
└── transcripts/
    └── agenda-discovery-checkout.md
```

The above session fed [`discovery/PB-001-reliable-checkout.md`](../../discovery/PB-001-reliable-checkout.md).
