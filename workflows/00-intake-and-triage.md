---
title: Workflow 00 — intake and screening
status: proposed
updated_at: 2026-08-09
---

# Workflow 00 — intake and screening

> [🚦 Triage Loop](../docs/loops/00-intake-and-triage.md) executable block: converts a raw input into a trackable Work Item ready for Product Manager decision, without transforming automatic normalization into priority or approval.

This workflow links the loop contract to the agent contracts and the workspace state. It doesn't end because the agents responded; ends when the consolidated output, evidence, authoritative state and next owner are coherent with each other.

---

## Block result

A successful execution leaves a single Work Item in the PM workspace, with localizable sources, uncertainties preserved, and an explicit decision requested from the Product Manager. No parallel contributions are treated as final output before Intake Agent consolidation.

The block is considered closed only when these four layers agree:

| Layer | Closing condition |
|---|---|
| **Loop** | the screening gate passed or the failure was recorded with a defined destination |
| **Agents** | each mission delivered an envelope; the Intake Agent consolidated facts, divergences and gaps |
| **Workspace** | Work Item was updated before `BOARD.md` and `STATUS.md`; transit points to the canonical source |
| **Decision** | the PM received an objective question and his decision was recorded or explicitly pending |

If one of these conditions is missing, the execution is `partial` or `blocked`, never `completed`.

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 0 — input |
| **Execution unit** | an entry identified by `mission_id`; distinct entries do not share session folder or transient state |
| **Consolidates** | [Intake Agent](../agents/intake-agent/AGENT.md) |
| **Collaborate** | [Meeting Context Agent](../agents/meeting-context-agent/AGENT.md), when the origin is a meeting; [Product Manager Agent](../agents/product-manager-agent/AGENT.md), for product context |
| **Human owner** | Product Manager |
| **Workspace owner** | `<pm-workspace>`; by default, `workspaces/pm` |
| **Input** | request, incident, feedback, opportunity or meeting context pack |
| **Canonical output** | `<pm-workspace>/projects/<project>/work-items/<WI-id>.md` |
| **Content gate** | explicit problem, origin, project, owner and minimum context; known duplicates linked |
| **Block Gate** | content gate + envelopes + persisted evidence + reconciled Work Item/board/status + recorded decision or handoff |
| **Dominant lap** | external — material gap becomes a question for the origin or the PM, never an assumption by the agent |
| **Next loop** | [🔦 Discovery and research](01-discovery-and-research.md), only when the PM authorizes progress |

---

## Workspace preconditions and resolution

Before distributing missions, the workflow executor preflights in the order below. Preflight is authoritative reading and resolution; still does not change priority, state, or canonical artifact.

1. Set `mission_id`, sponsor, objective, scope, received sources, known risk, permissions and stopping condition.
2. Solve `<pm-workspace>` and read `README.md`, `AGENTS.md` and `WORKSPACE.md`.
3. Query allowed memory with `workspace-memory`, treating it only as context; confirm current status in canonical sources.
4. Find `<project>` by portfolio, `BOARD.md` or explicit reference. The slug is not just inferred from the name of a repository or a feature.
5. If the project exists, read `projects/<project>/README.md`, `CONTEXT.md` and `STATUS.md`; Search for related Work Items before creating another one.
6. Create a unique session folder in `projects/<project>/plans/assets/00-intake-and-triage/<YYYY-MM-DD>-<mission-id>/` for raw material and drafts.

If project or owner cannot be resolved, the entry remains in `<pm-workspace>/.coordination/inbox/`, with origin, lock and next assignee. A generic directory is not created in `projects/` to get around the gap.

### Minimum opening envelope

```yaml
mission_id: "TRIAGE-<id>"
work_item_id: null # populated when the item is found or created
workflow: "00-intake-and-triage"
phase: "intake"
sponsor: "product-manager"
objective: "<problema a normalizar>"
scope: []
sources: []
acceptance_criteria: []
risk: "<conhecido ou unknown>"
permissions: []
stop_conditions: []
workspace: "<pm-workspace>"
project: "<slug ou unresolved>"
mode: "execute | dry-run"
```

Missing material field is not filled in for convenience. It becomes a question, partial result or block, depending on the impact on the gate.

---

## Mission plan

```mermaid
TD flowchart
    A[Input + mission_id] --> B[Preflight<br/>workspace, project and sources]
    B --> C{Origin is meeting?}
    C -- yes --> D[Meeting Context Agent<br/>auditable context pack]
    C -- no --> E[Intake Agent<br/>normalizes problem]
    D --> E
    E --> F1[Intake Agent<br/>duplicities and dependencies]
    E --> F2[Product Manager Agent<br/>product, value and stakeholders]
    F1 --> G[Intake Agent<br/>consolidates candidate]
    F2 --> G
    G --> H{Content gate}
    H -- failed --> I[Correction, question<br/>or block]
    H -- passed --> J[Persist Work Item<br/>e evidence pack]
    J --> K[Reconcile STATUS and BOARD]
    K --> L{PM's decision}
    L -- forward --> M[Handoff for Scout Loop]
    L -- clarify --> N[Return to origin]
    L -- reject/duplicate --> O[Close with reason and link]
```

### Dependencies and parallelism

| Mission | Responsible | Depends on | Can run in parallel with | Delivery |
|---|---|---|---|---|
| M0 — resolve execution | workflow executor | initial envelope | nothing | workspace, project, sources and limits confirmed |
| M1 — extract meeting | Meeting Context Agent | M0; only if there is a meeting | nothing, because it creates structured input | summary, context pack and points to be confirmed |
| M2 — normalize problem | Intake Agent | M0 and M1 when applicable | nothing | problem with no presumed solution and initial gap map |
| M3a — track relationships | Intake Agent | M2 | M3b | duplications, dependencies and related sources |
| M3b — enrich product | Product Manager Agent | M2 | M3a | product, stakeholders, claimed value and business questions |
| M4 — consolidate | Intake Agent | M3a and M3b | nothing | a single Work Item candidate |
| M5 — verify and persist | Intake Agent | M4 | nothing | gate, Work Item and evidence pack |
| M6 — reconcile state | executor with `workspace-board` | M5 | nothing | Work Item, `STATUS.md` and `BOARD.md` coherent |
| M7 — decide destination | Product Manager | M6 | nothing | advance, clarify, postpone or close |

M3a and M3b can run in parallel because they produce separate contributions. Neither edits the Work Item during this phase; only the Intake Agent writes the consolidated in M4/M5.

---

## Responsibilities and limits

| Participant | Do it in this block | Can't do |
|---|---|---|
| **Meeting Context Agent** | separates facts, speeches, provisional decisions, commitments and points without confirmation | transform suggestion into decision, attribute uncertain authorship or create the final Work Item |
| **Intake Agent** | normalizes, tracks sources, searches for duplications/dependencies, preserves gaps and consolidates | definitively prioritize, promise solution, estimate or decompose implementation |
| **Product Manager Agent** | adds product context, stakeholder, claimed value and business questions | approve own contribution or register priority on behalf of human PM |
| **Human Product Manager** | decides to move forward, clarify, postpone, absorb as duplicity or close | have the decision inferred from silence or lack of response |
| **Executor/orchestrator** | open quests, apply dependencies, gather envelopes and reconcile block | replace consolidator, hide divergence or decide by human owner |

A solution suggested by the source can be recorded as request data, but not as a problem definition nor as a team commitment.

---

## Skills and minimum context per mission

Each agent inventories the available skills before acting and records the exact names in `skills_used`. In this workflow, the baseline is:

| Skill | When is it mandatory in the block | Expected result |
|---|---|---|
| `workspace-memory` | when starting or resuming the mission | context recovered and confirmed against canonical source |
| `workspace-projects` | when finding project, query `projects/` or persist artifact | canonical domain and destiny resolved; assets isolated per session |
| `workspace-board` | when finding, creating, assuming, blocking, or transitioning Work Item | Work Item updated before the board; explicit disagreements |
| `business-discovery` | when it is necessary to qualify problem, user or value without advancing to full discovery | delimited questions and hypotheses |
| `write-feature` | when the input needs to be structured as a product unit | verifiable structure without inventing priority or solution |
| `update-docs` | when confirmed meeting context is promoted to persistent artifact | documentation linked to the source and Work Item |

Non-applicable domain skill must be justified on the envelope; available and adherent skill cannot be silently omitted.

The executor gives each agent only what is necessary for its mission: identifiers, authorized sources, criteria, limits, canonical paths and relevant questions. Full memory, logs from other agents, and unrelated materials are not propagated by default.

---

## Work Item Consolidation

The Intake Agent consolidates contributions without erasing their nature. The Work Item separates:

- **facts and evidence**, each with a traceable origin;
- **inferences**, with author and basis;
- **hypotheses**, with a form of validation;
- **suggested solution**, if any, identified as the origin's request;
- **gaps and contradictions**, expressed as open questions;
- **duplicities and dependencies**, with links, not just names;
- **preliminary risk**, without converting automatic classification into authorization;
- **decision requested**, with nominal human owner.

While the priority decision is pending, the item remains in `refinement`; the agent does not invent a priority value to satisfy a template. After the PM's decision:

| Decision | Authoritative effect |
|---|---|
| advance | record decided priority, move to `backlog` or next authorized state and prepare handoff |
| ask for clarification | keep at `refinement`; if progress is prevented, record cause, impact, next owner and next action |
| absorb as duplicity | move to `cancelled` only after linking the item that absorbed it |
| reject or postpone | record decision, reason, owner and reopening condition; do not delete history |

---

## Persistence and writing containment

| Artifact | Destination | Who writes | Rule |
|---|---|---|---|
| raw material and drafts | `projects/<project>/plans/assets/00-intake-and-triage/<date>-<mission-id>/` | mission agent | one new folder per run; is never canonical source |
| summary/context pack | `projects/<project>/work-items/assets/<meeting-id>/` | Meeting Context Agent | mandatory when entering a meeting |
| Work Item | `projects/<project>/work-items/<WI-id>.md` | Intake Agent | authoritative source of owner, state, scope, dependencies and evidence |
| evidence pack | `projects/<project>/work-items/assets/<WI-id>/evidence-pack.md` | Intake Agent | generated from envelopes, gate and sources; not selectively assembled at the end |
| `STATUS.md` | `projects/<project>/STATUS.md` | authorized executor | summarizes the verifiable status of the project; does not contradict the Work Item |
| `BOARD.md` | workspace root | authorized executor | regenerable index; always reconciled after Work Item |
| questions and temporary handoffs | `.coordination/` | shipping agent | transit with deadline/owner; points to canonical artifact |

Parallel contributions use their own files or envelopes. No agent writes to a shared log or Work Item while the Intake Agent commits.

### Closing order

1. persist individual outputs and envelopes;
2. consolidate and update the Work Item;
3. register the gate and evidence pack;
4. reconcile `STATUS.md`;
5. regenerate or reconcile `BOARD.md`;
6. create handoff for the next owner pointing to the Work Item;
7. issue the final block envelope.

Failure after step 2 does not authorize faking completion. Resumption uses the same `mission_id`, checks the already persisted state and only completes what is missing.

---

## Gates and evidence

### Content gate

- [ ] the problem is understandable without depending on the solution requested;
- [ ] origin, author/date when available and links to material statements are recorded;
- [ ] project, affected product, human owner and known stakeholders are explicit;
- [ ] duplicates and dependencies were searched, with search scope and links found;
- [ ] preliminary risk, premises, contradictions and open questions are separated;
- [ ] the Work Item does not contain invented priority, commitment or approval.

### Block closing gate

- [ ] all agents returned an envelope with `status`, `sources_used`, `skills_used`, outputs, risks and gates;
- [ ] the Intake Agent produced a single consolidated report and preserved material differences;
- [ ] canonical artifact and evidence pack were persisted and referenced;
- [ ] Work Item, `STATUS.md` and `BOARD.md` reflect the same state;
- [ ] the PM's decision is registered or there is `decision_requested` with owner and next action;
- [ ] handoff references artifacts instead of copying the entire context.

The content gate can pass while the human decision is pending. In this case, the Intake Agent mission may be `completed`, but the workflow transition remains `awaiting_human`; The item does not silently advance to the Scout Loop.

---

##Handoffs

| Direction | Minimum content |
|---|---|
| **Origin → workflow** | raw material, origin, date, author/requester when known and usage permissions |
| **Meeting Context → Intake** | context pack, localizable excerpts, decisions only when confirmed, authorship doubts and limitations |
| **Product Manager Agent → Intake** | product, stakeholder, claimed value, sources, hypotheses and questions; never definitive priority |
| **Intake → Human PM** | Work Item link, destination recommendation, alternatives, risks, gaps and objective decision question |
| **Workflow → Scout Loop** | Work Authorized item, PM decision, sources, preliminary risk, hypotheses and questions still open |

A handoff is not completed as long as it exists only in `.coordination/`. It ends when the recipient manages to resolve the Work Item and its evidence in the canonical source.

---

## Failures, retry and escalation

| Condition | Status | Action | Next Owner |
|---|---|---|---|
| unidentifiable problem | `partial` | return objective question and preserve input | origin or PM |
| unresolved project or owner | `blocked` | keep an entry in your inbox; do not create generic project | PM |
| incomplete transcription or ambiguous authorship | `partial` or `blocked` | mark limitations; request confirmation | meeting owner |
| sources contradict each other | `blocked` when material | record versions and impact; do not choose silently | PM |
| probable duplicity | `partial` until decision | link candidates and request absorption decision | PM |
| two attempts without closing the gap | `blocked` | end automatic retry with evidence of attempts | PM |
| risk over autonomy or insufficient permission | `blocked` | interrupt before action and request authorization | PM or domain owner |
| reconciliation failure between Work Item and board | `partial` | preserve Work Item as authority and fix index | workspace executor |

Escalation is not forwarding a vague conversation. Escalation records condition, impact, evidence, options, recommendation, necessary decision and nominal owner.

---

## Idempotence and resumption

- The same source event and the same `mission_id` do not create two Work Items. Resume searches for the already linked item and session folder.
- A technical retake of the same execution saves `mission_id` and folder. A deliberate retry receives new `mission_id` and new session folder, but updates the existing Work Item history when addressing the same issue.
- Duplicity is only terminated by explicit link; no items are deleted to "clean" the board.
- Memory can guide the search, but Work Item, `STATUS.md`, `BOARD.md` and evidence decide the current state.
- In `dry-run`, agents can show drafts and gates in the conversation, but cannot write in `projects/`, `.coordination/`, `STATUS.md`, or `BOARD.md`.

---

## Block end envelope

```yaml
mission_id: "TRIAGE-<id>"
work_item_id: "<WI-id>"
workflow: "00-intake-and-triage"
status: completed | partial | blocked
transition: awaiting_human | ready_for_discovery | returned | closed
workspace: "<pm-workspace>"
project: "<slug>"
agents_run: []
sources_used: []
skills_used: []
outputs_created: []
state_changes:
  work_item: "<before -> after>"
  status: "<before -> after>"
  board: "reconciled | pending | not_applicable"
decisions_requested: []
decisions_recorded: []
assumptions: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`completed` requires gate passed, evidence persisted, and state reconciled. `ready_for_discovery` also requires an explicit decision from the PM; silence never promotes the item.
