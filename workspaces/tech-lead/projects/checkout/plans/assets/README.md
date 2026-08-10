# Session assets

Material from a workflow execution — both what the human brings and what the AI generates in the process — stays here, isolated by session, never released into `plans/` nor mixed into the canonical final artifact.

## What's going on here

| Type | Examples |
|---|---|
| **Input material** (human brings) | meeting transcripts, emails, PDFs, screenshots, Word documents |
| **Intermediate AI output** | draft SPEC before adversarial review, exploratory architecture analysis, unconsolidated discovery notes |

The relevant distinction is not who generated it, but whether the artifact has passed the workflow gate. Before gate → `plans/assets/`. After gate → canonical destination (`engineering/`, `product/`, `ux/`, `plans/active/`).

## Convention

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: name of the workflow or skill that generated the material, for example `03-technical-specification` or `technical-discovery`.
- `<session-id>`: short and unique identifier of the run (`mission_id` or run id). Re-executing the workflow due to unsatisfactory results creates a **new** folder; the previous one remains in the history, but is no longer referenced by the current artifact.
- Subfolders by type within the session folder, only when there is more than one file of the same type:
  - `transcripts/` — transcripts of meetings or sessions
  - `drafts/` — AI-generated intermediate drafts before gate
  - `screenshots/` — screenshots
  - `emails/` — relevant emails
  - `documents/` — PDFs, Word and the like

## Rules

- `plans/assets/` is not canonical source. The extracted conclusion, decision or requirement goes to `engineering/`, `product/`, `ux/` or the plan in `plans/active/`; the asset remains as an auditable trail, referenced by path.
- Never reuse the folder from a previous session, even if the result has been discarded — this avoids collisions when the same workflow runs again for the same project.
- `STATUS.md` or the corresponding Work Item indicates which session holds the current version of an artifact, when this is not obvious from the direct link.
- Adversarial reviews **do not stay here** — they are formal artifacts with their own gate and go to `execution/reviews/`.

## Example

```text
plans/assets/03-technical-specification/2026-08-08-a1c9f2/
├── transcripts/
│ └── revisiono-arquitetura-idempotencia.md ← meeting brought by human
└── drafts/
    └── SPEC-001-v0.md ← draft AI before adversarial review
```

See [`03-technical-specification/2026-08-08-a1c9f2/`](03-technical-specification/2026-08-08-a1c9f2/README.md) for the session that underpins `plans/active/PLAN-014.md`.
