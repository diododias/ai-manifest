---
title: Workflow 03 — technical specification
status: proposed
updated_at: 2026-08-09
---

# Workflow 03 — technical specification

> [🗺️ Drafting Loop](../docs/loops/03-technical-specification.md) executable block: transforms the approved product and UX baseline into a technical strategy, isolatable tasks and criteria that the next steps can execute and verify without renegotiation.

The Drafting Loop is the boundary between intention and execution. Your product is not just a `SPEC`: it is a coherent package in which `PRD → UX → SPEC → TASKS → CHECKLIST` maintains explicit traceability, writers, dependencies and stopping conditions.

---

## Block result

A closed execution leaves the active plan, specification, structural decisions, eligible tasks and validation checklist synchronized. Ralph Loop must be able to distribute tasks without two agents competing for the same file or contract; the Red Team should be able to prove coverage using the checklist without asking the author what he meant.

| Layer | Closing condition |
|---|---|
| **Loop** | alternatives, contracts, data, tests, telemetry, rollout and rollback were treated proportionally to the risk |
| **Agents** | experts contributed before critique; Adversarial independent TL attacked the package; specifier responded findings |
| **Workspace** | plan, SPEC, ADR, reviews, Work Items, `STATUS.md`, `MEMORY.md` and board are reconciled |
| **Next execution** | tasks have possible owner, dependencies, writing scope, repository and evidence of completion |
| **Decision** | H3 was recorded when there was an ADR, exception, public contract, migration or R3/R4 risk |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 3 — specification |
| **Execution unit** | Work Product/UX item with baseline H2 and technical `mission_id` |
| **Consolidates** | [Specification Tech Lead Agent](../agents/specification-tech-lead-agent/AGENT.md) |
| **Specializes** | [Security, Data & Platform Specialist](../agents/specialist-security-data-platform-agent/AGENT.md), by explicit domain and risk |
| **Challenge** | [Adversarial Tech Lead](../agents/adversarial-tech-lead-agent/AGENT.md), independent of specifier |
| **Human owner** | Tech Lead |
| **Input** | `PB.md`, `PRD.md`, UX spec, architecture, repositories, contracts, SLOs, policies and risk |
| **Exit** | `PLAN`, `SPEC`, `TASKS`, `CHECKLIST`, ADR and testing strategies, observability, rollout and rollback |
| **Content gate** | full traceability, small/verifiable tasks and critical trade-offs/gaps addressed |
| **Block Gate** | content + independent critique + persistence/reconciliation + eligibility of Work Items + H3 when applicable |
| **Dominant lap** | average — the solution is attacked before any task becomes `ready` |
| **Next workflow** | [04 — standalone implementation](04-autonomous-implementation.md) |

---

## Technical Preflight

1. Resolve the Tech Lead, project and Work Item workspace; read `AGENTS.md`, `WORKSPACE.md`, `CONTEXT.md`, `STATUS.md` and memory allowed.
2. Fix approved revisions of `PRD.md` and UX spec. Contradiction or ambiguous requirement returns to Studio Loop.
3. Consult `engineering/repositories.yaml`, local repository instructions, current architecture, contracts, ADRs, SLOs and applicable policies.
4. Confirm risk class, permissions, specialized domains, and H3 triggers. The agent does not reduce risk to avoid checkpoint.
5. Create session folder in `plans/assets/03-technical-specification/<date>-<mission-id>/`; drafts and transcripts remain there until the gate.
6. Record in the Work Item the assumption of the mission and the technical baseline before changing artifacts.

### Opening envelope

```yaml
mission_id: "DRAFTING-<id>"
work_item_id: "<WI-id>"
workflow: "03-technical-specification"
baseline:
  prd: "<path@revision>"
  ux_spec: "<path@revision>"
  architecture: []
repositories: []
risk: "R0 | R1 | R2 | R3 | R4"
specialist_domains: []
h3_triggers: []
permissions: []
stop_conditions: []
mode: "execute | dry-run"
```

---

## Mission plan

```mermaid
TD flowchart
    A[PRD + UX + architecture + risk] --> B[Specification TL<br/>alternatives and starter package]
    B --> C{Specialized domain?}
    C -- yes --> D1[Security]
    C -- yes --> D2[Date]
    C -- yes --> D3[Platform]
    C -- no --> E[Integrate constraints]
    D1 --> E
    D2 --> E
    D3 --> E
    E --> F[Adversarial TL<br/>failure scenarios]
    F --> G[Specification TL<br/>answers and review]
    G --> H[Decompose TASKS + CHECKLIST]
    H --> I{Block gate}
    I -- ambiguous requirement --> J[Studio Loop]
    I -- ADR/exception/R3-R4 --> K[H3 Tech Lead]
    I -- default --> L[Work Items ready]
    K -- accept --> L
    K -- review --> B
```

| Mission | Responsible | Depends on | Delivery |
|---|---|---|---|
| M1 — alternatives and initial design | Specification TL | baseline | options, trade-offs, contracts, data, failures and operational strategy |
| M2 — specialized analysis | independent experts by domain | M1 | additional restrictions, controls, tests and criteria |
| M3 — domain integration | Specification TL | M2 | `PLAN`/`SPEC` candidates and proposed ADRs |
| M4 — technical attack | Adversarial TL | M3 | findings with evidence, scenario, impact, alternative and severity |
| M5 — answer | Specification TL | M4 | resolution or residual risk by finding; package review |
| M6 — decomposition | Specification TL | M5 | `TASKS`, `CHECKLIST` and Work Items with executable DAG |
| M7 — gate/H3 | automation + Tech Lead when triggered | M6 | approved technical baseline or explicit feedback |

Security, Data and Platform analyzes can run in parallel with each other, each with a declared boundary. Adversarial criticism only begins after accepted constraints have been incorporated; otherwise, it would evaluate an already obsolete solution.

---

## Decomposition contract

Each task that powers Ralph Loop states:

| Field | Why is it mandatory |
|---|---|
| objective and completion criteria | prevents agent from spinning without knowing when to stop |
| requirements/SPEC tracked | proves that the task implements something authorized |
| repository, paths and contracts affected | allows you to detect write collisions before distribution |
| dependencies and blocks | forms the actual execution DAG |
| expected inputs and outputs | defines the handoff boundary |
| tests and evidence | allows independent validation |
| risk and permissions | limits autonomy and external actions |
| retry/escalation condition | prevents infinite repetition |

Parallel tasks cannot have the same writer scope. When two changes need the same file or contract, they are serialized, merged, or given an explicit division of ownership.

---

## Authority boundaries

| Participant | Do | Doesn't |
|---|---|---|
| Specification TL | writes and consolidates plan, SPEC, tasks, checklist and ADR proposal | changes outcome/UX, approves the package itself or reduces risk |
| expert | issues opinion limited to the declared domain | extends completion to unevaluated domains or edits SPEC directly |
| Adversarial TL | models failures, couplings, migration, rollback, testing and operational cost | blocks due to aesthetic preference or rewrites the author's artifact |
| Human Tech Lead | decides H3, exceptions, risk and structural trade-offs | has presumed approval due to silence |
| executor/orchestrator | controls DAG, envelopes and reconciliation | choose architecture or close finding on behalf of the writer |

---

## Skills and minimal context

| Participant | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on the operation |
| Specification TL | `technical-discovery`, `create-spec`, `refine-spec`, `review-spec` |
| expert | `technical-discovery`, `analyse-bug`, `review-spec` |
| Adversarial TL | `review-spec`, `review-cross-prd-spec`, `technical-discovery` |

Each envelope records `skills_used`. Experts receive only SPEC candidate, policies, paths, and domain questions; the adversarial receives the integrated package and not the specifier's private reasoning.

---

## Traceability and coherence

The evidence pack maintains the chain:

```text
PB outcome
  → PRD requirement
    → UX flow/state
      → SPEC contract/behavior
        → TASK executable unit
          → CHECKLIST independent proof
```

Every link uses IDs or stable links. A `TASK` without a corresponding checklist item does not become `ready`; a checklist item without authorized behavior indicates extra scope. Changing a public contract, data model or migration strategy requires reviewing downstream links.

---

## Persistence and promotion order

| Artifact | Canonical source | Writer |
|---|---|---|
| active plan | `<tech-lead-workspace>/projects/<project>/plans/active/<PLAN-id>.md` | Specification TL |
| Final SPEC | `engineering/specs/<SPEC-id>.md` | Specification TL |
| ADR | `engineering/adr/<ADR-id>.md` | Specification TL after H3 decision when applicable |
| adversarial review | `execution/reviews/spec-<SPEC-id>.md` | Adversarial TL |
| expert opinion | `execution/reviews/<domain>-<SPEC-id>.md` | domain expert |
| Work Items | `work-items/<WI-id>.md` | Specification TL; state/ownership source |
| technical evidence pack | `execution/evidence/spec-<SPEC-id>.md` | generated from gates, reviews and traceability |
| drafts/transcriptions | `plans/assets/03-technical-specification/<date>-<mission-id>/` | session agent |
| status | `STATUS.md`, `BOARD.md`, `MEMORY.md` | authorized executor, in that order of authority |

Promotion: integrate experts → respond review → persist SPEC/ADR/PLAN → create Work Items → generate evidence pack → update `STATUS.md` and durable memory → reconcile `BOARD.md`. `MEMORY.md` records decisions and trade-offs with links; does not replace the above sources.

---

## Gates

### Technical gate

- [ ] there is at least one alternative discarded with cost and consequences;
- [ ] contracts, data, competition, security, observability, testing, rollout and rollback were covered proportionally to the risk;
- [ ] structural decisions have proposed/accepted ADR, never lost comment in SPEC;
- [ ] chain `PRD → UX → SPEC → TASKS → CHECKLIST` is complete;
- [ ] tasks are small, isolatable, ordered and verifiable;
- [ ] residual risks have explicit ownership and treatment.

### Block execution gate

- [ ] necessary specialists acted before the Adversarial TL;
- [ ] each finding has an answer, evidence and status;
- [ ] no reviewer changed the specifier artifact;
- [ ] parallel writer scopes do not collide;
- [ ] Work Items record dependencies, repositories, paths, gates and stopping conditions;
- [ ] plan, SPEC, ADR, Work Items, `STATUS.md`, memory and board are reconciled;
- [ ] H3 was executed only when triggered and its decision is linked to the baseline.

---

## H3, failures and returns

| Condition | Destination |
|---|---|
| standard package, without trigger H3 | Work Items `ready` for Ralph Loop |
| ADR, exception, public contract, migration or R3/R4 | Mandatory H3 with alternatives and recommendation |
| ambiguous requirement/UX | StudioLoop; not interpret technically |
| access, supplier or external policy | block and escalate to authorized owner |
| risk without sufficient mitigation | H3 may accept, revise or terminate; agent does not reclassify |
| critical finding open | specification remains under review |
| material change after gate | invalidate affected tasks/checklist and reopen the block |

---

## Final envelope

```yaml
mission_id: "DRAFTING-<id>"
work_item_id: "<WI-id>"
workflow: "03-technical-specification"
status: completed | partial | blocked
transition: awaiting_h3 | ready_for_implementation | returned_to_planning
baselines:
  prd: "<path@revision>"
  ux_spec: "<path@revision>"
  spec: "<path@revision>"
agents_run: []
specialist_domains: []
skills_used: []
outputs_created: []
work_items_created: []
dependency_dag: "<path>"
write_collisions: []
findings:
  resolved: []
  open: []
decisions_requested: []
decisions_recorded: []
risks: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`ready_for_implementation` requires that every eligible task is executable and verifiable without improvised architectural decision by the implementing agent.
