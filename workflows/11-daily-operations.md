---
title: Workflow 11 — daily operation
status: proposed
updated_at: 2026-08-09
---

# Workflow 11 — daily operation

> [☀️ Daily Loop](../docs/loops/11-daily-operations.md) executable block: reads everything that has finished or remained in flight since the last cut and delivers decisions, risks, proposed memory and improvements with explicit destination to the owner.

The Daily Loop rotates by calendar, not by Work Item. Recording the day is not prioritizing it: Auto Dream separates and signals; Knowledge promotes memory through the correct gate; Intake transforms reproducible friction into Work Item; the owner decides.

---

## Block result

A closed execution leaves a short and orderly briefing, a safely advanced collection cursor and each observation forwarded to one of four destinations: owner decision, memory proposal, Work Item in intake or hypothesis under observation. Nothing survives just as a narrative in the briefing.

| Layer | Closing condition |
|---|---|
| **Loop** | full window has been collected and every assertion points to identifiable session/envelope/item |
| **Agents** | Telemetry collected; Orchestrator reconciled flight; Auto Dream classified; Knowledge/Intake promoted destinations |
| **Workspace** | briefing, memory, Work Items, locks and cursor agree with canonical sources |
| **Owner** | blocked and risks bring requested decision, impact and deadline |
| **Cadence** | cursor only advances after persistence; retry does not duplicate briefing, memory or Work Item |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 11 — knowledge and improvement |
| **Cadence** | daily, per workspace, even without delivery completed |
| **Execution unit** | window `(last_successful_cutoff, current_cutoff]` identified by `daily_run_id` |
| **Consolidates** | [Auto Dream Agent](../agents/auto-dream-agent/AGENT.md) |
| **Collection** | [Telemetry Agent](../agents/telemetry-agent/AGENT.md) |
| **Reconciles flight** | [Orchestrator Agent](../agents/orchestrator-agent/AGENT.md) |
| **Promotes memory** | [Knowledge Agent](../agents/knowledge-agent/AGENT.md) |
| **Receives improvements** | [Intake Agent](../agents/intake-agent/AGENT.md) |
| **Human owner** | workspace owner |
| **Input** | closed sessions, envelopes, gates, retries, escalations and items in flight since the last cut |
| **Exit** | briefing, memory proposals, Work Items, hypotheses and collection alert when necessary |
| **Content gate** | traceable claims; decisions with owner/deadline; improvements explicitly promoted or discarded |
| **Block Gate** | content + privacy + idempotent cursor + persisted destinations + briefing within budget |
| **Dominant lap** | of the system, with daily window |

---

## Preflight and cursor

1. Resolve workspace, owner, timezone, `daily_run_id`, last completed cut and current cut.
2. Read workspace rules, `BOARD.md`, active projects and `STATUS.md`; memory is only for context.
3. Check if there is already a run for the same window. Resumption completes the existing run; does not create another briefing.
4. Inventory session supplies/envelopes and in-flight items; record expected coverage before collection.
5. Establish a minimization/anonymization policy, validity of the briefing and owner's reading budget (target: up to 10 minutes).
6. Create transient state of the run without moving the success cursor.

### Opening envelope

```yaml
daily_run_id: "DAILY-<YYYY-MM-DD>-<workspace>"
workflow: "11-daily-operations"
workspace: "<workspace-id>"
owner: "<owner>"
window:
  start_exclusive: "<last-successful-cutoff>"
  end_inclusive: "<current-cutoff>"
  timezone: "<tz>"
sources_expected: []
briefing_budget:
  max_read_minutes: 10
privacy_policy: "<path>"
permissions: []
stop_conditions: []
```

Missing previous cursor requires explicit bootstrap with declared scope; does not authorize reading unlimited history. Collection failure does not move the cursor.

---

## Mission plan

```mermaid
TD flowchart
    A[Daily window + sources] --> B1[Telemetry<br/>collects and anonymizes]
    A --> B2[Orchestrator<br/>items in flight and blocks]
    B1 --> C{Full coverage?}
    C -- no --> D[Collection alert<br/>cursor does not advance]
    C -- yes --> E[Auto Dream<br/>classifies observations]
    B2 --> E
    E --> F1[Blocked/at risk<br/>owner's briefing]
    E --> F2[Pattern with evidence<br/>memory proposal]
    E --> F3[Reproducible Friction<br/>Triage Work Item]
    E --> F4[Isolated occurrence<br/>weekly hypothesis]
    F2 --> G[Knowledge Agent<br/>gate and promotion]
    F3 --> H[Intake Agent<br/>Work Trackable Item]
    F1 --> I[Auto Dream<br/>final briefing]
    G --> I
    H --> I
    F4 --> I
    I --> J{Block gate}
    J -- passed --> K[Persist cursor<br/>and close run]
```

| Mission | Responsible | Output |
|---|---|---|
| M1 — collect window | Telemetry Agent | correlated sessions/envelopes, cost, gates, retries, coverage and limitations |
| M2 — reconcile flight | Orchestrator Agent | active items, time in state, dependencies, locks and pending decision |
| M3 — classify | Auto Dream Agent | completed, pending, failure/cause and human decision; four more operational destinations |
| M4 — promote memory | Knowledge Agent | input validated with origin/context/validity or proposal rejected |
| M5 — open improvement | Intake Agent | Work Item with symptom, evidence, impact, probable cause and recommended owner |
| M6 — assemble briefing | Auto Dream Agent | blocked → at risk → in progress, within budget |
| M7 — close run | executor | persisted artifacts/targets and atomically advanced cursor |

M1 and M2 run in parallel. M4 and M5 can also run in parallel after sorting, as they write different fonts. Auto Dream does not edit memory or backlog directly.

---

## Classification and destinations

| Nature observed | Criterion | Destination |
|---|---|---|
| decision/block | only owner can resolve and there is current impact | `bloqueado` briefing with question/deadline |
| upcoming risk | Evidence indicates it will block within declared horizon | briefing `em risco` with prevention possible |
| progress | status confirmed with no human action required | informative and compact briefing |
| recurring pattern | multiple sessions support the same contextual conclusion | proposal to Knowledge/Archivist; not direct writing |
| reproducible friction | identifiable symptom, steps/evidence and impact | Intake Work Item; PM prioritizes later |
| isolated occurrence | real evidence but recurrence/cause not confirmed | hypothesis for Dream Loop |
| noise/no action | does not change decision, memory, backlog or risk | discard recorded in the run, not in the briefing |

The same event can generate signaling and improvement, but uses crossed IDs to avoid becoming two truths.

---

## Briefing contract

The briefing is valid for one day and has a mandatory order:

1. **Blocked** — decision needed today; owner, question, options, recommendation, impact and deadline.
2. **At risk** — will block if no one takes action; evidence, horizon and preventive action.
3. **In progress** — relevant changes, next gates and operational information only.
4. **Destinations created** — links to proposed memory, Work Items and hypotheses; does not repeat the content.
5. **Run quality** — coverage, missing sources and limitations.

No blocks/risks, sections remain short and say “none identified with collected sources”; Collection failure produces warning, never empty certainty.

---

## Authority boundaries

| Participant | Do | Doesn't |
|---|---|---|
| Telemetry | collects, correlates, anonymizes and measures coverage | concludes cause or priority |
| Orchestrator | describes authoritative state, locks, and dependencies | decides destination/priority |
| Auto Dream | classifies, formulates hypotheses and consolidates briefing | edit memory, create priority or change gate/policy/autonomy |
| Knowledge | evaluates/promotes memory in the correct source | turns isolated hypothesis into rule |
| Intake | creates/relates Work Item trackable | definitely prioritize |
| workspace owner | responds to decisions and accepts/discards signaling | has an answer inferred by silence |

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| Telemetry | `technical-discovery`, `analyse-bug`, `update-docs` |
| Orchestrator | `dev-flow`, `update-docs` |
| Auto Dream | `analyse-bug`, `technical-discovery`, `update-docs` |
| Knowledge | `update-docs`, `refine-spec`, `technical-discovery` |
| Intake | `business-discovery`, `write-feature` |

Each envelope records `skills_used`. Auto Dream receives already minimized data and the authoritative summary of items; does not receive secrets, unnecessary personal data, or private memory from another workspace.

---

## Idempotence and multi-agent writing

- `daily_run_id` and window are unique per workspace; retry resumes the same run.
- Each event/session has an ID and is only classified once per window.
- Knowledge deduplicates proposal by evidence/concept; Intake searches for existing Work Item before creating another.
- Writers remain separate: Auto Dream writes briefing/run; Knowledge writes memory; Intake writes Work Item; Orchestrator reconciles state.
- Cursor only advances after briefing and all mandatory destinations are persisted.
- Later correction creates errata linked to the briefing; does not silently rewrite daily history.

---

## Persistence

| Artifact | Destination | Validity/authority |
|---|---|---|
| daily briefing | `<workspace-owner>/.coordination/daily/<date>.md` | valid for one day; loop's own final artifact |
| run state/cursor | `.coordination/daily/state/` | idempotent cadence control |
| proposal/memory | corresponding `MEMORY.md` | only after Knowledge/owner; points to evidence |
| Work Improvement Item | `<pm-workspace>/projects/<project>/work-items/<WI-id>.md` | authoritative source after Triage |
| hypothesis under observation | `.coordination/observations/` | transit to Dream Loop |
| anonymized collection | `execution/telemetry/daily/<date>/` or equivalent governed registry | Dream input; declared retention |

The briefing is a legitimate exception in `.coordination/` because it expires. Everything that needs to survive the day must be in memory, Work Item or hypothesis explicitly forwarded.

---

## Gates

### Content gate

- [ ] window/cursor and font coverage are explicit;
- [ ] secrets/personal data were removed before analysis;
- [ ] every statement points to session, envelope, gate or Work Item;
- [ ] blocked/risks have owner, decision, impact and deadline;
- [ ] reproducible improvement turned to Work Item or recorded disposal;
- [ ] isolated hypothesis was not promoted to memory;
- [ ] briefing respects reading order and budget.

### Block execution gate

- [ ] writers and domains were respected;
- [ ] memory went through Knowledge and improvement went through Intake;
- [ ] Work Item, flight status and briefing do not contradict each other;
- [ ] retry/deduplication did not create duplicate outputs;
- [ ] all destinations are persisted before the cursor;
- [ ] gate/policy/autonomy change was sent to Dream/H6, never applied here.

---

## Failures and escalation

| Condition | Action |
|---|---|
| incomplete/failed collection | alert owner/Telemetry; keep cursor; not issue “no news” briefing |
| item blocked for more than one cycle | highlight at the top and escalate to owner with accumulated time |
| unresponsive escalation | repeat as blocked, without inventing decision |
| recurring improvement without Work Item | block target closure or record explicit disposal by owner |
| memory grows without validity | Knowledge revises/expires; do not accumulate by default |
| conflict between briefing and Work Item | Work Item expires; correct briefing and investigate collection |
| proposal affects gate/politics/autonomy | forward to Dream Loop/H6 |

---

## Final envelope

```yaml
daily_run_id: "DAILY-<YYYY-MM-DD>-<workspace>"
workflow: "11-daily-operations"
status: completed | partial | blocked
transition: briefing_ready | collection_blocked | destinations_pending
workspace: "<workspace-id>"
window:
  start_exclusive: "<timestamp>"
  end_inclusive: "<timestamp>"
coverage:
  expected: 0
  collected: 0
  missing: []
agents_run: []
skills_used: []
briefing: "<path>"
blocked_items: []
at_risk_items: []
memory_proposals: []
improvement_work_items: []
hypotheses_for_dream: []
discarded_observations: []
decisions_requested: []
outputs_created: []
cursor:
  advanced: false
  new_cutoff: null
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`briefing_ready` requires advanced cursor only after all targets; run with failed collection remains `collection_blocked`.
