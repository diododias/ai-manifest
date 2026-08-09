---
title: Workflow 02 — product and UX planning
status: proposed
updated_at: 2026-08-09
---

# Workflow 02 — product and UX planning

> [🎨 Studio Loop](../docs/loops/02-product-and-ux-planning.md) executable block: transforms the approved issue into a verifiable product commitment and experience, without subordinating one canonical source to another.

This workflow has two consolidators and two authoritative artifacts: the Product Manager Agent responds to `PRD.md`; the UX Specification Agent responds to the UX spec. The result of the block is not either of them in isolation, but the traceable coherence between the two.

---

## Block result

A closed run leaves `PRD.md` and UX spec mutually consistent, verifiable criteria, recorded trade-off decisions, and an H2 evidence pack that shows the delta from H1. If a requirement exists in only one source, or if the artifacts point to different revisions, the block remains open.

| Layer | Closing condition |
|---|---|
| **Loop** | scope, out of scope, outcome, flows, states and validation are covered |
| **Agents** | PM and UX consolidated their artifacts; independent critic received response by finding |
| **Workspaces** | PM and UX sources are versioned, crossed by the same Work Item and reconciled on the boards |
| **Decision** | Human PM and UX received H2 with trade-offs and proven coherence |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 2 — product and discovery |
| **Execution unit** | a Work Item with favorable H1 and immutable baseline from `PB.md` approved |
| **Consolidates product** | [Product Manager Agent](../agents/product-manager-agent/AGENT.md) — `PRD.md` |
| **Consolidates experience** | [UX Specification Agent](../agents/ux-specification-agent/AGENT.md) — UX spec, flows and validation |
| **Challenge** | [Adversarial Product Manager](../agents/adversarial-product-manager-agent/AGENT.md), in independent instance |
| **Human Owners** | PM for product commitment; UX by experience |
| **Input** | `PB.md`, H1, user evidence, constraints and open hypotheses |
| **Exit** | `PRD.md`, UX spec, flows/states, proportional prototype, validation, reviews and evidence pack H2 |
| **Content gate** | `PB → PRD ↔ UX spec` traceability, measurable success and critical gaps addressed |
| **Block Gate** | content + cross review + writers preserved + multiworkspace state reconciled + H2 registered |
| **Dominant lap** | average — ambiguities, implicit scope, and borderline cases are attacked before H2 |
| **Next workflow** | [03 — technical specification](03-technical-specification.md), only with explicit H2 baseline |

---

## Preflight and baseline

1. Confirm H1, approved `PB.md`, Work Item, PM/UX owners, risk and stop condition.
2. Resolve PM and UX workspaces; read `CONTEXT.md`, `STATUS.md`, current artifacts and existing handoffs.
3. Record the exact revision of `PB.md` used as baseline. Material change in the problem or outcome is fed back into the Scout Loop rather than being silently absorbed.
4. Create a common `mission_id` and separate session folders in each workspace.
5. Define an initial traceability matrix with stable IDs for outcomes, requirements, flows, states and criteria.
6. Confirm who can approve prototype, additional research, sensitive content, and scope trade-offs.

### Opening envelope

```yaml
mission_id: "STUDIO-<id>"
work_item_id: "<WI-id>"
workflow: "02-product-and-ux-planning"
baseline:
  product_brief: "<path@revision>"
  h1_decision: "<path>"
owners:
  product: "<PM>"
  experience: "<UX>"
risk: "<classe>"
sources: []
permissions: []
stop_conditions: []
mode: "execute | dry-run"
```

---

## Mission plan and coherence barrier

```mermaid
TD flowchart
    A[PB + H1 + baseline] --> B1[PM Agent<br/>PRD candidate]
    A --> B2[UX Agent<br/>flows, states, validation]
    B1 --> C[Cross review<br/>PRD matrix ↔ UX]
    B2 --> C
    C --> D{Coherence achieved?}
    D -- no --> E1[PM corrects product]
    D -- no --> E2[UX corrects experience]
    E1 --> C
    E2 --> C
    D -- yes --> F[Adversarial PM<br/>independent attack]
    F --> G[PM + UX<br/>answers by finding]
    G --> H{Block gate}
    H -- evidence gap --> I[Scout Loop]
    H -- ready --> J[H2 PM + UX]
    J -- approved --> K[Baseline for Drafting Loop]
```

| Mission | Writer | Dependency | Output |
|---|---|---|---|
| M1 — product commitment | Product Manager Agent | baseline | outcome, scope, out of scope, metrics and criteria in `PRD.md` |
| M2 — complete experience | UX Specification Agent | baseline | journey, flows, states, content, accessibility, prototype and validation plan |
| M3 — cross review | PM + UX, each in its own artifact | M1 and M2 | matrix `requirement ↔ flow/state ↔ criterion ↔ verification method` |
| M4 — adversarial attack | Adversarial independent PM | M3 coherent | classified findings and gate recommendation |
| M5 — answer | PM and UX | M4 | resolution, risk acceptance or escalation by finding |
| M6 — H2 package | Product Manager Agent, with UX Agent attestation | M5 | delta, coherence, risks and requested decisions |
| M7 — decision | PM + UX humans | block gate | approved appointment, adjustment or return |

M1 and M2 can start in parallel. M3 is a barrier: no track advances to critique until the two artifacts point to the same revision and the matrix is ​​not complete.

---

## Competitive writing and authority

| Participant | Write | Does not write |
|---|---|---|
| Product Manager Agent | `PRD.md`, decisions and evidence pack H2 | UX spec, priority on behalf of human PM or technical solution |
| UX Specification Agent | research, flows, UX spec, prototypes and validation | `PRD.md`, commercial engagement or architecture |
| research/content/prototyping specialists | isolated contributions to UX Agent | competing versions of the UX spec |
| Adversarial PM | independent review | `PRD.md` or UX spec from the author |
| executor/orchestrator | envelopes, dependencies and reconciliation | canonical content belonging to PM/UX |

Restriction discovered in the flow returns to the PRD. New requirement in PRD returns to UX spec. Each owner changes their own artifact; Nobody solves coherence by editing someone else's source.

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` according to the operation performed |
| Product Manager Agent | `business-discovery`, `write-feature`, `review-prd`, `refine-spec` |
| UX Specification Agent | `business-discovery`, `write-feature`, `update-docs` |
| Adversarial PM | `review-prd`, `review-cross-prd-spec`, `refine-spec` |

The envelopes read `skills_used`. The PM receives UX evidence and constraints by reference; UX receives outcome, scope and criteria by reference. Raw materials, personal data, and private memory remain in the authorized workspace.

---

## Coherence matrix

The block maintains a versioned matrix in the evidence pack H2:

| Element | Should point to |
|---|---|
| outcome of `PB.md` | outcome and metrics of `PRD.md` |
| `PRD.md` requirement | corresponding flow/state in UX spec |
| UX spec status | expected behavior and requirement that justifies it |
| acceptance criteria | verification method, environment and owner |
| out of scope | explicit absence in flows or treatment as future extension |
| critical hypothesis | evidence, validation plan or risk decision |

The gate fails if an engineer still needs to choose which document to obey, if a criterion uses unobservable language, or if an error/recovery state has no defined behavior.

---

## Multiworkspace persistence

| Artifact | Canonical source | Single Writer |
|---|---|---|
| `PRD.md` | `<pm-workspace>/projects/<project>/requirements/prd/<PRD-id>.md` | Product Manager Agent |
| trade-off decisions | `<pm-workspace>/projects/<project>/decisions/<decision-id>.md` | Product Manager Agent after human decision |
| adversarial findings | `<pm-workspace>/projects/<project>/requirements/reviews/<review-id>.md` | Adversarial PM |
| flows | `<ux-workspace>/projects/<project>/flows/` | UX Specification Agent |
| UX spec | `<ux-workspace>/projects/<project>/specifications/<UXSPEC-id>.md` | UX Specification Agent |
| prototype | `<ux-workspace>/projects/<project>/prototypes/` | UX Specification Agent |
| validation plan/result | `<ux-workspace>/projects/<project>/validation/` | UX Specification Agent |
| evidence pack H2 | `<pm-workspace>/projects/<project>/requirements/evidence/<mission-id>.md` | Product Manager Agent; referenced UX attestation |
| persistent handoffs | `projects/<project>/handoffs/` of PM and UX | owner sender |
| session assets | `plans/assets/02-product-and-ux-planning/<date>-<mission-id>/` | session agent |

Closing: persist UX and PM sources, update the matrix, respond to findings, register H2, update Work Items/`STATUS.md` and only then reconcile both boards. Handoff to Tech Lead contains links and reviews; does not duplicate PRD/UX spec.

---

## Gates

### Product and UX gate

- [ ] `PB.md`, `PRD.md` and UX spec form a traceable chain;
- [ ] objective, scope, out-of-scope and metrics are observable;
- [ ] all flows cover entry, success, empty/loading, error, permission and recovery when applicable;
- [ ] content and accessibility are part of the criteria, not the subsequent finishing;
- [ ] each requirement has a corresponding flow/state and verification method;
- [ ] critical hypotheses have evidence, validation plan or risk accepted by authorized owner.

### Block execution gate

- [ ] PM and UX wrote only in their domains;
- [ ] matrix references current revisions of the two artifacts;
- [ ] each adversarial finding has an answer and evidence;
- [ ] material divergences were escalated, not leveled by the consolidator;
- [ ] Work Items, `STATUS.md` and boards of the two workspaces are coherent;
- [ ] evidence pack H2 shows delta from H1 and requested decisions;
- [ ] Human PM and UX registered H2 before technical handoff.

---

## H2, returns and scaling

| Condition | Destination |
|---|---|
| coherent product and experience; H2 approved | Drafting Loop with frozen baseline |
| UX contradicts problem hypothesis | Scout Loop, preserving new evidence |
| scope trade-off without objective criteria | joint decision of PM and UX |
| material technical restriction still unknown | Tech Lead Discovery query/spike before H2 |
| critical finding open | block remains `blocked`; no handoff as ready |
| material change after H2 | invalidate the related part of H2 and reopen M1/M2/M3 |

No agent approves the artifact itself. H2 decides compromise and trade-off; It's not a line-by-line editing session.

---

## Final envelope

```yaml
mission_id: "STUDIO-<id>"
work_item_id: "<WI-id>"
workflow: "02-product-and-ux-planning"
status: completed | partial | blocked
transition: awaiting_h2 | ready_for_specification | returned_to_discovery | closed
baselines:
  product_brief: "<path@revision>"
  prd: "<path@revision>"
  ux_spec: "<path@revision>"
agents_run: []
workspaces_touched: []
skills_used: []
outputs_created: []
traceability_gaps: []
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

`ready_for_specification` requires explicit H2, coherent reviews and resolvable handoff by the Tech Lead without additional oral interpretation.
