#03 — Triggers and shots

> What triggers what, when, and what never triggers itself.

A loop catalog describes what happens **inside** each step. It doesn't answer the question that appears in the first week of operation: *what makes the next step start?* If the answer is "does anyone remember", the model is not agentic — it is a manual process with agents inside.

This page documents the flow nervous system. Every movement has a declared trigger, and every trigger belongs to one of three natures, with different properties.

| Nature | Origin | Property that defines it |
|---|---|---|
| **By event** | something changed state in the system | reacts immediately and does not depend on anyone remembering |
| **By calendar** | passed the time | happens even when there was no delivery |
| **Manual** | one person triggered | is always recorded, never implied |

The rule that cuts across all three: **a trigger that leaves no trace does not exist.** Every activation records origin, moment, mission dispatched and owner notified — this is what allows [🌙 Dream Loop](../loops/10-continuous-improvement.md) to measure the flow design instead of giving an opinion on it.

---

## Triggers per event

The most important column is the last one: **who knows**. A shot that triggers an agent without notifying anyone produces invisible work, and invisible work is what appears weeks later as a surprise.

| Event | Activate | Consolidate | Notify |
|---|---|---|---|
| Request, incident or feedback arrives | [🚦 Triage Loop](../loops/00-intake-and-triage.md) | Intake Agent | PM |
| Recorded meeting transcript | Meeting Context → [🚦 Triage](../loops/00-intake-and-triage.md) | Intake Agent | PM |
| Work Item prioritized by PM | [🔦 Scout Loop](../loops/01-discovery-and-research.md) | Product Manager Agent | PM and UX |
| Approved discovery gate | **H1** | — | PM or sponsor |
| H1 answered with "advance" | [🎨 Studio Loop](../loops/02-product-and-ux-planning.md) | PM + UX Specification | PM and UX |
| Approved Product Gate | **H2** | — | PM, with UX |
| H2 approved | [🗺️ Drafting Loop](../loops/03-technical-specification.md) | Specification Tech Lead | Tech Lead |
| New ADR, exception or R3/R4 risk detected | **H3** | — | Tech Lead |
| Approved specification, eligible tasks | [🔁 Ralph Loop](../loops/04-autonomous-implementation.md) | Orchestrator Agent | nobody, in healthy flow |
| Local sensor fails | internal return of the agent himself | the agent | nobody, within the limit of attempts |
| Attempt limit reached | escalation | Orchestrator | Tech Lead |
| Push with change ready | [⚔️ Red Team Loop](../loops/05-adversarial-validation.md) and CI | QA/Validation | nobody, if green |
| CI disapproves | back to [🔁 Ralph](../loops/04-autonomous-implementation.md) | Orchestrator | Tech Lead, if recurring |
| Adversarial validation approved | [🚪 Gatekeeper Loop](../loops/06-pr-and-merge.md) | PR Agent | Code Owners of the paths played |
| Open PR with green CI | **H4**, depending on risk | — | Code Owner |
| Merge completed | [🎭 Rehearsal Loop](../loops/07-release-candidate-validation.md) | Product Validation | PM and UX, if there is new experience |
| Release candidate approved | [🐤 Canary Loop](../loops/08-production-release-and-observation.md) | ReleaseAgent | Tech Lead |
| R3/R4 risk or critical exposure | **H5** | — | Tech Lead and PM |
| Observation window without regression | [🗄️ Archivist Loop](../loops/09-knowledge-curation.md) | Knowledge Agent | domain owner |
| Regression detected after deploy | automatic rollback and return to [🔁 Ralph](../loops/04-autonomous-implementation.md) | Release + Observability | Tech Lead, immediately |
| Incident in production | [🚦 Triage](../loops/00-intake-and-triage.md) with high priority | Intake Agent | PM and Tech Lead |

### Events that change the risk class

Some events do not trigger a loop: they change how many approvals the item will require. Recognizing them is what prevents a change from becoming dangerous without anything in the flow registering it.

| Event | Effect |
|---|---|
| Change touches sensitive path declared | automatically increases risk |
| Change alters rules, sensors or CI | automatically raises risk and requires independent reviewer |
| Scope changed after approval | recalculates risk and invalidates related approval |
| Relevant question remains open | prevents classification as R0 or R1 |

---

## Triggers by calendar

Two circuits rotate per time. They exist because what they observe — the state of the work system — does not generate its own event: an item that has been stopped for three days does not trigger anything on its own.

| Cadence | Activate | Consolidate | Delivery to |
|---|---|---|---|
| **Daily, start of the day** | [☀️ Daily Loop](../loops/11-daily-operations.md) | Auto Dream Agent | briefing to the workspace owner |
| **Weekly** | [🌙 Dream Loop](../loops/10-continuous-improvement.md) | Auto Dream Agent | H6, three of a kind |
| **Extraordinary, after relevant incident** | [🌙 Dream Loop](../loops/10-continuous-improvement.md) | Auto Dream Agent | H6, three of a kind |

The detail of what each cadence does is in [Rhythms and cadences](04-ritmos-e-cadencias.md). What matters here is the property: **one trigger per calendar cannot be silently skipped.** Collection failure opens alert; a day without data is a signal, not the absence of one.

---

## Manual shooting

There is a small set of actions that a person makes directly. All are recorded, and most are a way of **intervening in the flow**, not starting it.

| Action | Who can | Effect | Registration required |
|---|---|---|---|
| Prioritize or deprioritize a Work Item | PM | moves the item to the discovery queue, or removes it | reason for change |
| Return an artifact to a previous loop | checkpoint owner | reopens the stage with new question | the question that prompted the return |
| Request additional discovery | PM or UX | new round of [🔦 Scout](../loops/01-discovery-and-research.md) with declared scope | the gap to be closed |
| Open architectural exception | Tech Lead | releases the advance with declared debt | ADR with term and reversion plan |
| Pause or reverse a rollout | Tech Lead | interrupts the exhibition | observed signal and decision |
| Lower autonomy level | Tech Lead | reintroduces checkpoints | metric that motivated |
| Loop in `dry-run` | any owner | validates the contract without side effects | none, as there is no effect |

A comment on the penultimate item. **Downgrading autonomy is a normal model action**, not an admission of failure. Autonomy rises through evidence and descends through the same path; a system in which it only goes up is measuring poorly.

---

## What never fires alone

This is the list that defines the limit of the model. Each line has a structural reason, not a style preference.

| Never automatic | Why |
|---|---|
| Priority of a Work Item | priority is comparison between items, and comparison requires business intent |
| Scope approval | whoever proposed the scope has a structural incentive to approve it |
| Architectural exception | an exception that grants itself ceases to be an exception |
| Risk exposure R3/R4 | the cost of making mistakes is irreversible or far-reaching |
| Changing gate, rule or autonomy level | a system that relaxes verification itself converges to no verification |
| Closing an item due to duplicity | closing without explicit link makes the item disappear from the trail |
| Written in low-confidence learning `MEMORY.md` | inflated memory stops being read, and unread memory is worse than missing |

The general rule behind the seven lines: **automation decides the verifiable; person decides what is comparable and what is irreversible.**

---

## How a shot is executed

Every trigger — by event, calendar or human hand — goes through the same sequence before becoming work. It exists so that no mission can begin without declared authority.

1. The trigger is recorded with origin, time and affected item.
2. The Orchestrator assembles the **mission identity**: objective, scope and out-of-scope, canonical sources, acceptance criteria, gates, risk, authorized tools, budget, stopping condition and human owner.
3. The mission is dispatched to the corresponding loop consolidator agent.
4. The loop rotates according to your contract in [`loops/`](../loops/README.md).
5. The outgoing envelope returns to Orchestrator with status, confidence and skills used.
6. Handoff crosses the border: the artifact arrives at the canonical source and the owner is notified if there is a pending decision.

**A mission with any missing identity field should not be performed** — the absence is, in effect, a blank authorization. Details of the fields are in [Agents](../AGENTES.md).

---

## Typical failures of the firing system

| Failure | Symptom | Correction |
|---|---|---|
| Implicit trigger | a stage only begins when someone asks about it | declare the event that initiates it, or accept it as a cadence |
| Shooting without notification | work completed that no one knew was underway | every shot declares who is notified, even if it is "nobody" |
| Escalation without deadline | the item remains open indefinitely | escalation carries requested decision and deadline |
| Cadence skipped in silence | a day or a week disappears from the history | collection failure opens alert, never empty result |
| Undeclared reentry | work returns to a previous loop without registration | every return carries the question that motivated it |

---

*Previous: [Human Checkpoints](02-checkpoints-humanos.md) · Next: [Rhythms and Cadences](04-ritmos-e-cadencias.md).*
