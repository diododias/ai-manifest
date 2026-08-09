---
title: Workflow 08 — production and observation
status: proposed
updated_at: 2026-08-09
---

# Workflow 08 — production and observation

> [🐤 Canary Loop](../docs/loops/08-production-release-and-observation.md) executable block: promotes the approved release candidate through exposure stages and uses independent signals to fast forward, pause or roll back.

The Release Agent executes the policy; the Observability Agent judges health against a baseline set before rollout. Separating execution and interpretation prevents the desire to conclude from transforming regression into “probable noise”.

---

## Block result

A closed execution proves which artifact was exposed, in what proportion, with what authorizations and signs, and why the exhibition advanced or retreated. The loop only ends after the post-deploy window; “deploy accepted by the platform” is the beginning of the observation, not the conclusion.

| Layer | Closing condition |
|---|---|
| **Loop** | all authorized stages have passed their health gates or rollback/pause has been completed |
| **Agents** | Release executed; Observability interpreted without moving baseline or silencing alert |
| **Platform** | release/digest, configuration, exposure and result were consulted/recorded |
| **Workspace** | Work Item, health report, changelog, `STATUS.md` and board are reconciled |
| **Learning** | deviations and decisions generated candidates linked to evidence, without automatic promotion to knowledge |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 8 — release and operation |
| **Execution unit** | a `release_id` + digest + exposure strategy + declared window |
| **Consolidates operation** | [Release Agent](../agents/release-agent/AGENT.md) |
| **Interprets health** | [Observability Agent](../agents/observability-agent/AGENT.md) |
| **Human owner** | Tech Lead; PM co-approves R3/R4 and product material impact |
| **Input** | Approved RC, rollout/rollback, SLOs, metrics, alerts, baseline and authorizations |
| **Exit** | release, health report, changelog, timeline and rollback/pause/incident when applicable |
| **Pre-exposure gate** | provenance, environment, secrets, migration, backup, rollback capacity and H5/policy |
| **Gate by internship** | signals within limits during minimum window; critical alert explained or exposure stopped |
| **Final gate** | post-deploy window complete with no relevant regression and persisted state |
| **Dominant lap** | external — each stage observes production; regression returns by pause/rollback |
| **Next workflow** | [09 — knowledge curation](09-knowledge-curation.md), for learning candidates |

---

## Production preflight

1. Confirm `release_id`, RC/digest approved, source commit, H4 registration and Rehearsal acceptance.
2. Consult the current state of the target environment, current release, concurrent changes and operational window.
3. Verify authorized secrets without exposing values, config compatibility, migrations, backups and tested rollback/roll-forward capacity.
4. Capture baseline before exposure: SLOs, errors, latency, saturation, product metrics and comparable windows.
5. Set stages, percentages/cohorts, minimum duration, health gates, thresholds, pause/rollback triggers and incident owner.
6. Confirm external authorizations and H5 according to risk. R3/R4 never go into production due to silence.
7. Open evidence pack/timeline before the first external action.

### Opening envelope

```yaml
mission_id: "CANARY-<id>"
work_item_id: "<WI-id>"
workflow: "08-production-release-and-observation"
release:
  id: "<release-id>"
  candidate_id: "<RC-id>"
  version: "<version>"
  digest: "<digest>"
  source_commit: "<sha>"
environment: "<production-target>"
risk: "<classe>"
strategy:
  type: canary | feature_flag | progressive | full
  stages: []
baseline_window: "<range>"
observation_window: "<duration>"
health_gates: []
rollback_triggers: []
permissions: []
approvals: []
stop_conditions: []
```

---

## Mission and internship plan

```mermaid
TD flowchart
    A[RC approved + baseline] --> B{H5/policy satisfied?}
    B -- no --> C[Block and climb]
    B -- yes --> D[Release Agent<br/>exposes stage N]
    D --> E[Observability Agent<br/>compares signals]
    E --> F{Health gate}
    F -- healthy and full window --> G{More internships?}
    G -- yes --> D
    G -- no --> H[Close post-deploy window]
    F -- critical/threshold alert --> I[Pause exposure]
    I --> J{Safe rollback?}
    J -- yes --> K[Rollback + evidence]
    J -- no --> L[Incident + human owner]
    H --> M[Changelog, status and handoff]
```

| Mission | Responsible | Output |
|---|---|---|
| M1 — prepare release | ReleaseAgent | pre-exposure checks and materialized plan |
| M2 — capture baseline | ObservabilityAgent | window, queries, values ​​and limitations |
| M3 — exhibit internship | ReleaseAgent | action, cohort/percentage, version and timestamp confirmed by the platform |
| M4 — observe internship | ObservabilityAgent | comparison, anomalies, trust and recommendation |
| M5 — decide transition | policy/Tech Lead according to risk | fast forward, hold, pause or reverse |
| M6 — reply regression | Release + Observability + incident owner | containment, rollback/roll-forward, timeline and impact |
| M7 — close window | ReleaseAgent | final release, changelog, health report and reconciled status |

M3 and M4 are not parallel: first the platform confirms exposure; then the observer evaluates the window. M4 can read multiple signals in parallel, but produces a single recommendation with explicit divergences.

---

## Health gate by stage

Each stage states:

| Field | Function example |
|---|---|
| exposure/cohort | limits blast radius |
| start and minimum duration | prevents conclusion too early |
| comparable baseline | avoids attributing seasonality to the release |
| metrics and SLOs | defines operational and product success |
| thresholds/warning/critical | eliminates opportunistic interpretation |
| automatic decision allowed | pause/rollback only when authorized |
| owner to inconclusive signal | guarantees stopping with decision, not advancing through silence |

Baseline is not recalculated to accommodate regression. Changing the baseline during rollout requires a proven external reason and a new decision.

---

## Authority boundaries

| Participant | Do | Doesn't |
|---|---|---|
| ReleaseAgent | checks provenance, executes authorized stage, authorized pause/rollback and records release | expands exposure beyond politics or interprets a contradictory signal alone |
| ObservabilityAgent | correlates signals, compares baseline, recommends and only executes previously authorized pause/rollback | silence alert, reset baseline or approve release |
| Tech Lead/PM | authorize H5, exception and continuity in material risk | have consent inferred by absence |
| incident owner | takes command when impact exceeds rollout | leaves incident only in transient log after stabilization |

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| ReleaseAgent | `check-pr`, `update-pr`, `dev-flow`, `update-docs` |
| ObservabilityAgent | `analyse-bug`, `technical-discovery`, `update-docs` |

Each envelope records `skills_used`. Release receives artifact, policy and controls; Observability receives release/timeline, queries, SLOs and metrics. Secrets never go in envelopes/evidence packs.

---

## Persistence and evidence

| Artifact | Canonical source | Writer |
|---|---|---|
| release record/changelog | authorized release system | ReleaseAgent |
| health report and timeline | `<tech-lead-workspace>/projects/<project>/execution/evidence/<release-id>/health-report.md` | ObservabilityAgent |
| rollout evidence | `execution/evidence/<release-id>/rollout/` | ReleaseAgent |
| rollback evidence pack | `execution/evidence/<release-id>/rollback/` | Release + Observability |
| Work Item/STATUS/BOARD | workspace Tech Lead | authorized executor, after external status confirmed |
| apprenticeship candidates | `projects/<project>/LEARNINGS.md` | authorized owner; with links, not yet canonical knowledge |
| ongoing incident/alert | `.coordination/` until promotion | incident owner |

Every external action records intent, actor, non-secret parameters, platform response, timestamp and observed result. After stabilization, incident material is promoted to the official source; it doesn't just stay in `.coordination/`.

---

## Gates

### Pre-exposure gate

- [ ] approved digest is the digest to be promoted;
- [ ] environment, config, authorized secrets and concurrent changes were checked;
- [ ] migration/backup and rollback or roll-forward are executable;
- [ ] baseline, thresholds, stages and window are fixed;
- [ ] applicable owners, permissions and H5 are registered.

### Gate per stage/end

- [ ] platform confirmed intended version and exposure;
- [ ] minimum window elapsed and signals were compared to the baseline;
- [ ] warning/critical alerts have explanation/evidence or exposure has been paused;
- [ ] product and operation signs were considered according to risk;
- [ ] internship was only advanced by authorized policy/decision;
- [ ] final window ended without relevant regression.

### Block execution gate

- [ ] executor and interpreter remained separate;
- [ ] each stage is on the timeline with decision and evidence;
- [ ] rollback/pause was triggered when threshold required;
- [ ] release, health report, Work Item, `STATUS.md` and board agree;
- [ ] learning candidates preserve fact/hypothesis and links.

---

## Regression and scaling

| Condition | Action |
|---|---|
| critical alert not explained | pause immediately; do not expand exposure |
| regression with safe rollback | perform authorized rollback and prove recovery |
| unsafe rollback/irreversible migration | open incident and Tech Lead decides containment/roll-forward |
| contradictory signals | hold/pause exposure; Observability records trust and scale |
| data loss/critical SLO | immediate incident, secure preservation of evidence and communication |
| confirmed defect | Ralph Loop; new artifact goes through validation/PR/approval |
| impact exceeds plan | human owner takes over; automation does not expand scope of mitigation |

The loop does not close until health has been reestablished and proven, even if the rollback has been accepted by the platform.

---

## Final envelope

```yaml
mission_id: "CANARY-<id>"
work_item_id: "<WI-id>"
workflow: "08-production-release-and-observation"
status: completed | partial | blocked
transition: released_stable | rolled_back | paused | incident_open
release:
  id: "<release-id>"
  digest: "<digest>"
  source_commit: "<sha>"
  final_exposure: "<percent-or-cohort>"
stages: []
baseline: "<path>"
health_report: "<path>"
skills_used: []
alerts: []
rollback:
  executed: false
  evidence: null
incident: null
outputs_created: []
decisions_recorded: []
learning_candidates: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`released_stable` requires full window and confirmed external state; Successful deploy alone never satisfies the block.
