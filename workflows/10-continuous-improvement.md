---
title: Workflow 10 — telemetry and continuous improvement
status: proposed
updated_at: 2026-08-09
---

# Workflow 10 — telemetry and continuous improvement

> [🌙 Dream Loop](../docs/loops/10-continuous-improvement.md) executable block: compares the weekly behavior of the work system with a governed baseline and transforms patterns into validated learning or prioritizable demand.

The object of this workflow is loops, gates, handoffs and workspaces — not the individual evaluation of agents. Telemetry produces data and limitations; Auto Dream formulates hypotheses; Critic tries to refute them; the trio decides H6 when the proposal affects sensitive memory, critical priority, gate, policy or autonomy.

---

## Block result

A closed run produces a reproducible periodic report and gives each conclusion exactly one target: validated learning, improvement Work Item, or observation hypothesis. Generic observation without owner/criteria is not output.

| Layer | Closing condition |
|---|---|
| **Loop** | window, baseline, dataset, quality and analysis are identified |
| **Agents** | Telemetry did not infer causality; Auto Dream did not prioritize; Independent critic evaluated generalization |
| **Workspaces** | technical report, memory and backlog remain in their correct sources/owners |
| **Decision** | H6 was performed when mandatory; PM orders demand in normal backlog |
| **Governance** | no proposal changed the gate/autonomy itself without owner and approval |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 10 — knowledge and improvement |
| **Cadence** | weekly and extraordinary after relevant incident |
| **Execution unit** | a closed window `period_id`, with comparable baseline and explicit data cut |
| **Consolidates** | [Auto Dream Agent](../agents/auto-dream-agent/AGENT.md) |
| **Produces data** | [Telemetry Agent](../agents/telemetry-agent/AGENT.md) |
| **Complements operation** | [Observability Agent](../agents/observability-agent/AGENT.md) |
| **Challenge** | [Critic Agent](../agents/critic-agent/AGENT.md), independent |
| **Human owner** | trio; PM orders backlog; domain owner decides execution |
| **Input** | events/sessions, gates, retries, feedback, incidents, costs, metrics, Daily hypotheses and previous demands |
| **Exit** | report, memory proposal, Work Items for improvement and hypotheses under observation |
| **Content gate** | evidence, context, trust, validity, privacy, quality and contradictions treated |
| **Block Gate** | content + critique + persisted destinations + H6/politics + reconciliation |
| **Dominant lap** | of the system — feeds back to the design of the other loops |

---

## Window Preflight

1. Fix `period_id`, start/end, timezone, included projects/workspaces and cutoff timestamp.
2. Freeze metrics and baseline definitions before observing the result. Changing the setting after viewing the data invalidates the comparison.
3. Inventory sources: sessions, envelopes, gates, CI, reviews, releases, incidents, costs, feedbacks and hypotheses from the Daily Loop.
4. Validate permissions, retention and minimization; remove secrets and personal data before making dataset available for analysis.
5. Correlate `mission_id`, `work_item_id`, `workflow`, gate, release and decision; measure coverage and orphan events.
6. Record collection and comparability failures. Dropping metrics caused by missing collection is a warning, not an improvement.
7. Confirm independent Critic and possible owners of the destinations.

### Opening envelope

```yaml
mission_id: "DREAM-<id>"
workflow: "10-continuous-improvement"
period:
  id: "<YYYY-Www>"
  start: "<timestamp>"
  end: "<timestamp>"
  timezone: "<tz>"
  cutoff: "<timestamp>"
scope:
  workspaces: []
  projects: []
baseline: "<period-or-version>"
metric_definitions: "<path@revision>"
sources: []
privacy_policy: "<path>"
h6_triggers: []
permissions: []
stop_conditions: []
```

---

## Mission plan

```mermaid
TD flowchart
    A[Window + sources + baseline] --> B[Telemetry<br/>governed dataset]
    A --> C[Observability<br/>releases, incidents and SLOs]
    B --> D{Enough quality?}
    D -- no --> E[Collection alert<br/>no completion]
    D -- yes --> F[Auto Dream<br/>patterns and hypotheses]
    C --> F
    F --> G[Independent critic<br/>rebuttal/generalization]
    G --> H[Auto Dream<br/>answers and confidence]
    H --> I{Destination}
    I -- learning --> J[Proposal to Archivist/MEMORY]
    I -- improvement --> K[Work Item via Triage]
    I -- low confidence --> L[Hypothesis under observation]
    J --> M{H6 required?}
    K --> M
    M -- yes --> N[Trio decides H6]
    M -- no --> O[Sampling/policy]
```

| Mission | Responsible | Output |
|---|---|---|
| M1 — govern data | Telemetry Agent | dataset, schema, source, coverage, retention, quality and limitations |
| M2 — operational context | ObservabilityAgent | releases, rollbacks, incidents, SLOs and health baselines |
| M3 — analyze system | Auto Dream Agent | patterns by loop/cause/impact, hypotheses and confidence |
| M4 — criticize | Critical Agent | contesting evidence, causality, sample, bias and generalization |
| M5 — consolidate destinations | Auto Dream Agent | learning, demand or hypothesis; never mixes the three |
| M6 — decide H6 | trio/system owner | accept, adjust, observe or reject sensitive proposals |
| M7 — persist | Knowledge/Intake owners | memory by Archivist gate; Work Item by Triage |

M1 and M2 can run in parallel. M3 only starts after the quality report; Auto Dream does not receive unminimized raw data.

---

## Metrics and secure usage

The report can measure per loop:

- lead/cycle time and waiting time;
- number of internal, medium and external turns;
- gate pass/fail/not-run and revalidations;
- blockages, escalations and causes;
- rework after H2/H3/H4;
- escaped defects, rollback and incidents;
- cost, evidence pack coverage and handoff quality;
- levels of autonomy and recorded human interventions.

These signals evaluate flow design. High external return rate may indicate poor entry or late gate; does not authorize agent ranking. Causality is hypothesized until there is sufficient testing/control.

---

## Contract of the three destinations

| Destination | Minimum content | Next Gate |
|---|---|---|
| learning | observation, context, evidence, scope, confidence, validity and future review | Archivist; H6 when sensitive |
| demand for improvement | symptom, frequency, impact, evidence, probable cause, acceptance criteria, recommended owner and risk | Triage; PM prioritizes in the same product queue |
| hypothesis under observation | question, current signal, missing evidence and promotion/discard status | next window or event defined |

Auto Dream does not edit sensitive memory alone, does not create definitive priority and does not change gate/policy/autonomy directly.

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| Telemetry | `technical-discovery`, `analyse-bug`, `update-docs` |
| Observability | `analyse-bug`, `technical-discovery`, `update-docs` |
| Auto Dream | `analyse-bug`, `technical-discovery`, `update-docs` |
| Critic | `review-prd`, `review-spec`, `code-review`, `review-cross-prd-spec` as per completion |

Each envelope records `skills_used`. Critic receives report, governed/aggregated dataset, definitions and hypotheses; does not receive personal data or the private narrative of Auto Dream.

---

## Multiworkspace persistence

| Artifact | Canonical source | Writer |
|---|---|---|
| report/dataset/quality | `<tech-lead-workspace>/projects/<project>/execution/telemetry/<period-id>.md` | Telemetry Agent |
| Dream report | `execution/telemetry/<period-id>-dream.md` | Auto Dream Agent |
| Critic review | `execution/reviews/dream-<period-id>.md` | Critical Agent |
| validated memory | `MEMORY.md` of the corresponding workspace | Knowledge Agent after gate/owner |
| demand for improvement | `<pm-workspace>/projects/<project>/work-items/<WI-id>.md` | Intake Agent after screening |
| open hypothesis | `.coordination/observations/` until next evidence | AutoDream; traffic |
| decision H6 | source of work system decisions | trio/owner |

Report does not replace Work Item. Improvement is only forwarded when it reaches intake; learning is only effective when you have passed the Archivist and been promoted.

---

## Gates

### Data and analytics gate

- [ ] window, cut, baseline and definitions are stable and comparable;
- [ ] origin, coverage, retention and limitations are explicit;
- [ ] secrets/personal data were removed before analysis;
- [ ] orphan events and collection failures are quantified;
- [ ] pattern, isolated occurrence, correlation, hypothesis and causality are separated;
- [ ] each conclusion has evidence, context, confidence and validity.

### Block execution gate

- [ ] Critic used an independent line and each challenge received a response;
- [ ] contradictory conclusions/low confidence were not promoted;
- [ ] each output has exactly one destination and owner;
- [ ] memory and backlog were updated by their workflows/owners, not by Auto Dream directly;
- [ ] H6 occurred for P0/P1, sensitive memory and all gate/policy/autonomy changes;
- [ ] report, reviews, decisions and destinations are linked by `period_id`.

---

## H6, failures and escalation

| Condition | Action |
|---|---|
| collection failure/drop | open telemetry alert; not complete improvement |
| personal data/secrets | stop, securely remove, and review access/retention |
| non-comparable metrics | mark `blocked/partial`; reset next window before collecting |
| low confidence/insufficient sample | maintain hypothesis as new evidence |
| P0/P1, sensitive memory, gate/policy/autonomy | H6 mandatory |
| low risk demand | follows policy/sampling, but enters Triage |
| unresolved contradiction | block automatic update and scale to trio |
| proposal relaxes gate that would evaluate it | independent review + human owner; never self-approval |

---

## Final envelope

```yaml
mission_id: "DREAM-<id>"
workflow: "10-continuous-improvement"
status: completed | partial | blocked
transition: period_closed | awaiting_h6 | data_quality_blocked
period_id: "<YYYY-Www>"
baseline: "<period-or-version>"
agents_run: []
skills_used: []
data_quality:
  coverage: "<value>"
  limitations: []
  privacy_incidents: []
patterns: []
hypotheses: []
learning_proposals: []
improvement_work_items: []
critic_findings:
  resolved: []
  open: []
h6:
  required: false
  decision: null
outputs_created: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`period_closed` requires that data, criticism, destinations and decisions are auditable; publishing a report does not equate to improving the system.
