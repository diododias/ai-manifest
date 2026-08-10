# Session assets

Raw material that supports the analyzes and discussions of a workflow — transcriptions, printscreens, emails, PDFs, Word documents and the like — stays here, isolated by execution.

## Convention

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: name of the workflow or skill that generated the material, for example `01-discovery-and-research` or a user research session.
- `<session-id>`: short and unique identifier of the run (`mission_id` or run id). Re-executing the workflow due to unsatisfactory results creates a **new** folder; the previous one remains in the history, but is no longer referenced by the current artifact.
- Subfolders by type (`transcripts/`, `screenshots/`, `emails/`, `documents/`) only when there is more than one file of the same type in the session.

## Rules

- `plans/assets/` is not canonical source. The extracted conclusion, decision or requirement goes to `research/`, `journeys/`, `flows/` or `specifications/`; the asset remains as an auditable trail, referenced by path.
- Protect participant consent, privacy, and anonymization when archiving research transcripts and recordings.
- Never reuse the folder from a previous session, even if the result has been discarded.

## Example

```text
plans/assets/01-discovery-and-research/2026-08-08-c3d821/
└── transcripts/
    └── entrevista-usuario-retencao-pagamento.md
```

The above session fed [`research/evidence-summary.md`](../../research/evidence-summary.md).
