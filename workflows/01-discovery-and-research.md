---
title: Workflow 01 — discovery and research
status: proposed
updated_at: 2026-08-09
---

# Workflow 01 — discovery and research

> [🔦 Scout Loop](../docs/loops/01-discovery-and-research.md) executable block: investigates problem, user and feasibility in parallel and converges into a `PB.md` that preserves uncertainty.

Discovery does not exist to confirm the requested feature. It reduces uncertainties that would change the decision to invest and makes visible what is not yet known. The block connects independent PM, UX, and Tech Lead investigations to the three workspaces without duplicating canonical sources.

---

## Block result

A closed execution produces a consolidated `PB.md`, trackable contributions by domain and an H1 evidence pack capable of answering: what problem exists, for whom, what observable change matters, what evidence supports this and what risks could still invalidate the investment.

| Layer | Closing condition |
|---|---|
| **Loop** | product, experience and feasibility investigations completed within timebox |
| **Agents** | independent contributions delivered; adversarial criticism resolved or explicitly pending |
| **Workspaces** | PM, UX and Tech Lead persisted only in their domains and linked the artifacts through the same Work Item |
| **Decision** | H1 received recommendation, alternatives, risks, evidence and open questions |

Without evidence pack persisted and without H1 decision recorded, the workflow does not transition to planning.

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 1 — product and discovery |
| **Execution unit** | a prioritized Work Item and a discovery question, identified by `mission_id` |
| **Consolidates** | [Product Manager Agent](../agents/product-manager-agent/AGENT.md) |
| **Collaborate** | [UX Specification Agent](../agents/ux-specification-agent/AGENT.md); [Tech Lead Discovery Agent](../agents/tech-lead-discovery-agent/AGENT.md); [Adversarial Product Manager](../agents/adversarial-product-manager-agent/AGENT.md) when there is a candidate hypothesis or proposal |
| **Human Owners** | PM for the investment; UX by evidence of experience; Tech Lead for feasibility reading |
| **Input** | Work Authorized item, discovery question, data, searches, restrictions, risk and timebox |
| **Exit** | `PB.md`, research, initial journey, feasibility note, findings and evidence pack H1 |
| **Content gate** | problem, user, outcome, desired experience, initial feasibility and uncertainties covered |
| **Block Gate** | content + independence of missions + linked canonical sources + treated findings + registered H1 |
| **Dominant lap** | average — adversarial criticism tries to invalidate the hypothesis before the decision |
| **Next workflow** | [02 — product and UX planning](02-product-and-ux-planning.md), only with favorable H1 |

---

## Preflight multiworkspace

1. Confirm in the Work Item the entry decision, human owner, discovery question, risk, timebox and stopping criteria.
2. Solve `<pm-workspace>`, `<ux-workspace>` and `<tech-lead-workspace>`; read local contracts and project `CONTEXT.md`/`STATUS.md`.
3. Confirm that the PM Work Item is the unit that connects the missions; UX or Tech Lead auxiliary items reference this identifier, without copying its authoritative state.
4. Recover allowed memory with `workspace-memory` and confirm each material information in the canonical sources.
5. Set the same discovery question for the three agents and only adapt the domain cut-off. Different questions produce answers that do not converge.
6. Create a unique session folder per workspace in `projects/<project>/plans/assets/01-discovery-and-research/<date>-<mission-id>/`.

Preflight blocks when the item has not been authorized, the question already assumes a solution, the project/owner is ambiguous or research data processing is not allowed.

### Opening envelope

```yaml
mission_id: "DISCOVERY-<id>"
work_item_id: "<WI-id>"
workflow: "01-discovery-and-research"
question: "<pergunta comum em termos de problema>"
sponsor: "product-manager"
owners:
  product: "<owner>"
  ux: "<owner>"
  technical: "<owner>"
sources: []
timebox: "<limite>"
risk: "<classe>"
permissions: []
stop_conditions: []
mode: "execute | dry-run"
```

---

## Mission plan

```mermaid
TD flowchart
    A[Work Item + common question] --> B1[PM Agent<br/>problem, value, outcome]
    A --> B2[UX Agent<br/>user, journey, research]
    A --> B3[TL Discovery<br/>feasibility, dependencies, risk]
    B1 --> C[PM Agent<br/>Initial PB]
    B2 --> C
    B3 --> C
    C --> D{Material hypothesis<br/>or candidate proposal?}
    D -- yes --> E[Adversarial PM<br/>invalidation attempt]
    D -- no --> F[PM Agent<br/>final consolidation]
    E --> F
    F --> G{Block gate}
    G -- correctable gap --> B1
    G -- risk/decision --> H[H1 human]
    H -- invest --> I[Studio Loop]
    H -- adjust --> A
    H -- postpone/terminate --> J[Record decision and return condition]
```

| Mission | Responsible | Parallelism | Own exit |
|---|---|---|---|
| M1 — problem and outcome | Product Manager Agent | M2 and M3 | problem hypothesis, segment, value, outcome and candidate metrics |
| M2 — user and experience | UX Specification Agent | M1 and M3 | evidence, current/desired journey, research limitations and gaps |
| M3 — initial feasibility | Tech Lead Discovery Agent | M1 and M2 | dependencies, restrictions, unknowns, risk and recommended spikes |
| M4 — first consolidated | Product Manager Agent | after M1–M3 | `PB.md` without erasing differences |
| M5 — adversarial attack | Adversarial independent PM | after M4, when triggered | findings with excerpt, impact, severity and evidence |
| M6 — response and evidence pack | Product Manager Agent | after M5 | answers by finding and decision package H1 |
| M7 — decision | Human Product Manager | after block gate | invest, adjust, postpone or terminate |

Missions M1–M3 do not edit the same file. Each agent persists its contribution in the domain's workspace; the PM references these sources when consolidating.

---

## Authority boundaries

| Participant | Authority on the block | Limit |
|---|---|---|
| **Product Manager Agent** | formulates problem/outcome and consolidates `PB.md` | does not decide H1 nor convert hypothesis into fact |
| **UX Specification Agent** | defines quality of user evidence and maps journey | does not change priority or replace search with heuristics without marking the limitation |
| **Tech Lead Discovery Agent** | assesses feasibility, dependencies and initial risk | does not choose final architecture or produce SPEC |
| **Adversarial PM** | tries to invalidate proposal and metrics | does not rewrite `PB.md` nor approve the review itself |
| **human PM** | decides investment and destination | silence is not approval; UX/TL conflict remains visible in the package |
| **Executor/orchestrator** | distributes context, applies timebox and reconciles envelopes | does not force consensus or replace consolidator/owners |

---

## Skills and minimal context

| Participant | Priority skills |
|---|---|
| all workspace agents | `workspace-memory`, `workspace-projects`, `workspace-board` when there is corresponding reading, writing or transition |
| Product Manager Agent | `business-discovery`, `write-feature` |
| UX Specification Agent | `business-discovery`, `write-feature`, `update-docs` |
| Tech Lead Discovery Agent | `technical-discovery`, `analyse-bug` when viability depends on existing behavior |
| Adversarial PM | `review-prd`, `review-cross-prd-spec`, `refine-spec` depending on the artifact attacked |

Each envelope records `skills_used` with exact names or the reason a domain skill does not apply. Personal data, full transcripts and private memory do not cross workspaces; handoffs carry synthesis, limitations, and authorized links.

---

## Consolidation without erasing uncertainty

`PB.md` maintains five separate classes:

1. observed evidence and its source;
2. agent's inference and its basis;
3. testable hypothesis and invalidation condition;
4. confirmed restriction and its owner;
5. open question, impact and responsible for answering it.

Conflict between domains is not resolved by voting. The PM consolidates the disagreement, describes its effect on H1, and requests a decision or new investigation. The technical note may recommend spike; cannot anticipate architecture. Research can disprove the hypothesized problem; This finding reopens the common question.

---

## Persistence and writing containment

| Artifact | Canonical source | Single Writer |
|---|---|---|
| `PB.md` | `<pm-workspace>/projects/<project>/discovery/PB.md` | Product Manager Agent |
| evidence and research plan | `<ux-workspace>/projects/<project>/research/` | UX Specification Agent |
| initial journey | `<ux-workspace>/projects/<project>/journeys/` | UX Specification Agent |
| feasibility note | `<tech-lead-workspace>/projects/<project>/engineering/architecture/<discovery-id>.md` | Tech Lead Discovery Agent |
| adversarial findings | `<pm-workspace>/projects/<project>/discovery/reviews/<review-id>.md` | Adversarial PM |
| evidence pack H1 | `<pm-workspace>/projects/<project>/discovery/evidence/<mission-id>.md` | Product Manager Agent, generated from contributions and gates |
| session material | `plans/assets/01-discovery-and-research/<date>-<mission-id>/` in the source workspace | mission agent |
| handoffs | `.coordination/handoffs/` until promotion | sender; always points to canonical source |

Closing first updates the domain artifacts, then `PB.md`, Work Item/`STATUS.md`, and lastly the affected boards. Cross snapshots are identified inputs, never a second source of truth.

---

## Block Gates

### Content

- [ ] discovery question is in terms of problem, not feature;
- [ ] problem, segment, outcome and desired experience have evidence or are marked as a hypothesis;
- [ ] research records method, sample, limitations, consent and trust when applicable;
- [ ] dependencies, restrictions and technical unknowns are tracked;
- [ ] metrics cannot improve without observable benefit to the user;
- [ ] risks, divergences and open questions survived consolidation.

### Block execution

- [ ] M1–M3 received the same question and returned independent envelopes;
- [ ] writers and canonical destinies were respected;
- [ ] adversarial criticism was carried out when the risk/proposal required it and each finding received a response;
- [ ] `PB.md`, Work Item, `STATUS.md` and boards point to the same state;
- [ ] evidence pack allows the PM to decide H1 without re-reading the sessions;
- [ ] H1 and its justification are registered before the transition.

---

## H1, failures and returns

| Result | Block status | Next action |
|---|---|---|
| invest | `completed` / `ready_for_planning` | register decision, criteria and handoff to Studio Loop |
| adjust question | `partial` | new round only on affected missions, with new attempt `mission_id` |
| critical evidence missing | `blocked` or `partial` | owner sets additional search, access or timebox |
| incompatible value and viability | `blocked` | present options and trade-offs to the PM/TL; do not choose silently |
| problem hypothesis refuted | `returned` | return to screening or reformulate the item without preserving favorite solution |
| postpone/terminate | `closed` | record reason, evidence and objective condition for reopening |

Two attempts without reducing material uncertainty terminate automatic retry and escalation. New information that changes the problem, user, outcome or risk invalidates the related H1.

---

## Final envelope

```yaml
mission_id: "DISCOVERY-<id>"
work_item_id: "<WI-id>"
workflow: "01-discovery-and-research"
status: completed | partial | blocked
transition: awaiting_h1 | ready_for_planning | returned | closed
workspaces_touched: []
agents_run: []
sources_used: []
skills_used: []
outputs_created: []
findings:
  resolved: []
  open: []
decisions_requested: []
decisions_recorded: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`ready_for_planning` requires explicit H1, persisted artifacts, and reconciled state in the workspaces involved.
