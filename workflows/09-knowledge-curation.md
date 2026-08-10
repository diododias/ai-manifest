---
title: Workflow 09 — knowledge curation
status: proposed
updated_at: 2026-08-09
---

# Workflow 09 — knowledge curation

> [🗄️ Archivist Loop](../docs/loops/09-knowledge-curation.md) executable block: transforms evidence of delivery, decision or incident into an update from the correct canonical source, without promoting temporary memory to the rule.

This workflow closes the gap between “the system has changed” and “the instructions now describe the real system”. Every update has an observable trigger, unique writer, human owner, evidence, scope, date and validity limit.

---

## Block result

A closed run updates exactly one authoritative source per concept, preserves history, and records what remains hypothesis. Sensitive, contradictory, or low-trust content goes through independent Critic before guiding future agents.

| Layer | Closing condition |
|---|---|
| **Loop** | change and evidence have been mapped to affected sources and contradictions resolved |
| **Agents** | Knowledge consolidated; Critic objected when triggered without editing the artifact |
| **Workspaces/repositories** | each owner wrote on their own domain; cross-links did not become authoritative copies |
| **Documentary cycle** | `proposed/canonical/superseded/archived` and successors are explicit |
| **Memory** | only points to canonical decisions/facts; hypotheses remain marked |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 9 — knowledge and improvement |
| **Execution unit** | a documentary trigger identified by `knowledge_change_id` |
| **Consolidates** | [Knowledge Agent](../agents/knowledge-agent/AGENT.md) |
| **Challenge** | [Critic Agent](../agents/critic-agent/AGENT.md) when change is sensitive, contradictory, broad or low confidence |
| **Human owner** | domain owner/source changed |
| **Input** | decisions, PRs, releases, approval, incidents, candidate learnings and current sources |
| **Exit** | updated canonical source or explicit proposal, review, knowledge changelog and pending conflicts |
| **Content gate** | origin, topicality, scope, validity and absence of silent contradiction |
| **Block Gate** | content + correct writer/owner + proportional criticism + links/state/reconciliation |
| **Dominant lap** | average — sensitive conclusion is challenged before promotion |
| **Next workflow** | [10 — continuous improvement](10-continuous-improvement.md) when the work system itself needs to change |

---

## Opening triggers

| Observable event | Candidate artifact | Consolidator/owner |
|---|---|---|
| architectural decision taken/reversed | new ADR; previous one is `superseded` | Specification TL / Tech Lead |
| convention adopted in the code | corresponding `docs/rules/` | agent who introduced / Tech Lead |
| procedure repeated and stabilized | `skills/<skill>/SKILL.md` | Domain knowledge / owner |
| build/test/run command changed | `AGENTS.md` in the same change set | Software Engineer / Tech Lead |
| public contract/amended scheme | rule, ADR and contract documentation | Specification TL / Tech Lead |
| incident with root cause | rule, ADR, skill or playbook | domain owner |
| learning validated by Daily/Dream | `MEMORY.md` and/or domain source | Knowledge / owner |
| gate, sensor, autonomy or policy changed | harness documentation + decision | Tech Lead + independent critic |

Entry without trigger/evidence remains candidate in `LEARNINGS.md` or `.coordination/`; is not promoted because it seems plausible.

---

## Authority Preflight

1. Fix `knowledge_change_id`, event, sources of evidence, affected concept, scope and owner.
2. Inventory all pages that claim authority over the concept; if two are canonical, block the promotion until ownership is resolved.
3. Read the current source, its links, status, history/successors and the real system it describes.
4. Query discovery-only memory and confirm each assertion in Work Items, decisions, code, release, or evidence.
5. Classify the proposal: factual correction, new rule, decision, procedure, learning, supersession or archiving.
6. Assess sensitivity/confidence and trigger Critic before canonical writing when necessary.
7. Resolve the domain writer. Knowledge Agent prepares handoff instead of editing source that belongs to another owner without authorization.

### Opening envelope

```yaml
mission_id: "ARCHIVIST-<id>"
knowledge_change_id: "KC-<id>"
workflow: "09-knowledge-curation"
trigger:
  type: "<event>"
  source: "<path-or-record>"
concept: "<concept>"
current_canonical_source: "<path-or-unresolved>"
target_source: "<path>"
domain_owner: "<owner>"
change_type: correction | rule | decision | procedure | learning | supersede | archive
confidence: high | medium | low
sensitivity: low | medium | high
evidence: []
permissions: []
stop_conditions: []
```

---

## Mission plan

```mermaid
TD flowchart
    A[Event + evidence] --> B[Knowledge Agent<br/>authority map]
    B --> C[Proposal + scope + validity]
    C --> D{Sensitive, contradictory<br/>or low confidence?}
    D -- yes --> E[Critic Agent<br/>independent rebuttal]
    D -- no --> F[Knowledge Gate]
    E --> G[Knowledge Agent<br/>replies criticism]
    G --> F
    F -- hypothesis/gap --> H[LEARNINGS or coordination]
    F -- owner conflict --> I[Scale to domain]
    F -- approved --> J[Domain writer<br/>promotes canonical source]
    J --> K[Validate links, status<br/>and consumers]
    K --> L[Update memory/indices by reference]
```

| Mission | Responsible | Output |
|---|---|---|
| M1 — map fonts | Knowledge Agent | authority, duplicity, obsolescence and consumers |
| M2 — propose change | Knowledge Agent | patch/proposal with origin, date, scope, validity and impact |
| M3 — criticize | Independent critic | confirmation, rebuttal or request for evidence |
| M4 — reply | Knowledge Agent | resolution by finding or preserved hypothesis |
| M5 — decide/promote | domain owner/writer | updated canonical source and correct documentary status |
| M6 — check | Knowledge Agent | links, references, absence of contradiction and changelog |
| M7 — reconcile context | Knowledge Agent | memory/indexes point to source, without duplicating true |

---

## Documentary life cycle

| Status | Use by agent | Transition |
|---|---|---|
| `proposed` | context; never current rule | owner approves to `canonical` or rejects |
| `canonical` | current source of the concept | new decision can supersede/archive |
| `superseded` | historical and rational; never current statement | points to canonical successor |
| `archived` | historical research | has no mandatory successor |

Document without `status` is treated as `proposed`. ADR is never rewritten to erase a previous decision: a new ADR to superseat and past/future league.

---

## Authority boundaries

| Participant | Do | Doesn't |
|---|---|---|
| Knowledge Agent | finds authority, proposes, consolidates, verifies and maintains links | convert hypothesis into rule or decide on someone else's domain |
| Critical Agent | tries to refute support, reach and confidence | uses the same reasoning as the author or edits criticized artifact |
| domain owner/writer | approves and promotes content in canonical destination | has presumed approval due to silence |
| future consumer/agent | follow only `canonical` | treats memory, `.coordination/` or `proposed` as rule |

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| Knowledge Agent | `update-docs`, `refine-spec`, `technical-discovery` |
| Critical Agent | `review-prd`, `review-spec`, `code-review`, `review-cross-prd-spec` depending on the source |

Each envelope records `skills_used`. The Critic receives proposal, evidence, criteria and current source; does not receive the author's private conclusion as fact.

---

## Persistence and promotion

| Artifact | Destination | Rule |
|---|---|---|
| canonical update | domain source | authorized sole writer |
| candidate/accepted learning | `<tech-lead-workspace>/projects/<project>/LEARNINGS.md` | candidate section does not guide as a rule |
| Critic review | `execution/reviews/knowledge-<id>.md` | when triggered |
| Successor ADR | `engineering/adr/<ADR-id>.md` | league and super headquarters, don't delete previous |
| proposal not decided | `.coordination/` | transit with owner/deadline |
| knowledge changelog | linked to `knowledge_change_id` | sources, before/after, consumers and gate |
| `MEMORY.md` | corresponding workspace | index/summary with link; never single house of decision |

Promotion: persist proposal/review → owner decides → writer updates source → validate links/consumers → mark previous document → record changelog → update memory/indexes by reference.

---

## Gates

### Knowledge gate

- [ ] trigger, source, data and owner are findable;
- [ ] concept has a single identified canonical source;
- [ ] text describes the actual state, not just intention/delivery history;
- [ ] scope, context and limit of validity are explicit;
- [ ] facts, inferences and hypotheses remain separate;
- [ ] contradictions have been resolved or block promotion;
- [ ] documentary status and successors are correct.

### Block execution gate

- [ ] Critic acted when sensitivity/confidence required;
- [ ] criticism has an independent line and answers by finding;
- [ ] writer and domain owner authorized the promotion;
- [ ] links, indexes, consumer agents/skills and related documentation have been checked;
- [ ] memory and `.coordination/` were not treated as final destination;
- [ ] Work Item/changelog/evidence allow you to audit the change.

---

## Failures and escalation

| Condition | Action |
|---|---|
| two sources claim authority | block and domain owner choose/consolidate |
| insufficient evidence | keep as hypothesis/candidate with next test |
| contradictory evidence | Critic + owner; do not select version silently |
| change erases valid decision | create successor/supersession, preserving history |
| politics, security or autonomy affected | mandatory independent review and human decision |
| missing writer/owner | blocked handoff; Knowledge does not assume dominance |
| implementation diverges from the rule | correct code or superseder rule by decision; never just “update docs” to legitimize deviation |

---

## Final envelope

```yaml
mission_id: "ARCHIVIST-<id>"
knowledge_change_id: "KC-<id>"
workflow: "09-knowledge-curation"
status: completed | partial | blocked
transition: canonical_updated | proposal_pending | hypothesis_preserved | owner_blocked
trigger: "<event>"
canonical_source: "<path>"
previous_source_state: "<state>"
new_source_state: "<state>"
domain_owner: "<owner>"
agents_run: []
skills_used: []
sources_used: []
outputs_created: []
consumers_checked: []
contradictions: []
critic_findings:
  resolved: []
  open: []
decisions_requested: []
decisions_recorded: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`canonical_updated` requires an identified current source, authorized owner, resolved contradictions and verifiable consumers.
