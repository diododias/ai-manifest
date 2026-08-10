#01 — Papers

> Who owns which decision, who needs to be consulted, and what to do when two owners disagree.

A model with agents multiplies the number of decisions made per unit of time. If the ownership of these decisions is not explicit, the effect is not paralysis — it is something worse: **decisions start to be made by omission**, within artifacts, by whoever was there at the time. This page exists so that no decision remains idle waiting for consensus and none is taken without a nominal person responsible.

The starting distinction is between executing and directing. The human trio does not attempt to do the agents' work manually; he operates the system that does it.

---

## The four actors

| Actor | Drives | Does not respond for |
|---|---|---|
| **Product Manager** | value, priority and business results | architecture, experience design |
| **UX** | user understanding, experience and quality of use | business priority, architecture choice |
| **Tech Lead** | feasibility, architecture, technical quality and operational risk | business value, experience decision |
| **Agents** | research, proposal, implementation, criticism, validation and documentation | any value, scope or exception decision |
| **Automations** | deterministic checks, blocking and traceability | judgment about what to do with a failure |

The first three lines describe people; the last two, capacity. Separation matters because **agents and automations do not have ownership** — they prepare, execute and prove. When an agent appears to have decided something relevant, either the decision was in fact mechanical, or their contract is poorly designed.

### Product Manager — owner of value and priority

Answer by "is it worth building this, now, for this result?". Maintains objectives and roadmap, orders the backlog by value, urgency, risk and learning, and **formulates the problem before committing to a solution**. In daily operations, it decides to advance, adjust, postpone or close an item, approves value with stakeholders and orders the improvements that telemetry produces.

Operates the product intake, discovery, planning and validation agents — [📥 Intake](../agentes/intake-agent.md), [📋 Product Manager](../agentes/product-manager-agent.md), [🥊 Adversarial PM](../agentes/adversarial-product-manager-agent.md) and [✅ Product Validation](../agentes/product-validation-agent.md).

**What is not exclusive to the PM:** designing the experience alone, defining a technical solution, approving a technical exception without the Tech Lead, or replacing user evidence with stakeholder opinion.

### UX — owner of the experience and evidence about the user

Answer by "does this solve the problem of whoever is going to use it, and does it solve it well?". Plan risk-proportional search, map journeys and friction points, and specify nominal, empty, loading, error, allow, and recovery states — the set that is often forgotten and reappears as rework three steps later.

Operates the [🧭 UX Specification](../agentes/ux-specification-agent.md) and participates in product reviews.

**What is not exclusive to UX:** define business priorities, choose architecture, or approve scope alone.

### Tech Lead — owner of technical integrity and operational risk

It answers by “is this viable, sustainable and safe to operate?”. Defines architecture, contracts and boundaries, establishes quality and observability standards, and classifies risk. It also **maintains the harness** — the rules, skills, sensors and gates that make the repository understandable and safe for agents. It is the only ownership that falls on the work system itself, and not on the product.

Operates the specification, implementation, review, security, and operation agents — from [📐 Specification Tech Lead](../agentes/specification-tech-lead-agent.md) to [🚀 Release](../agentes/release-agent.md).

**What is not exclusive to the Tech Lead:** define business value, decide experience, or absorb scope decisions alone.

### Shared responsibility

The three jointly account for the quality of the problem before the solution, for the coherence between value, experience and feasibility, for explicit risks and traceable decisions, for the protection of data and users, and for learning after delivery. Shared here means that **none of the three can approve alone** — not that responsibility is diluted.

---

## Decision rights

Reference to resolve "who decides this?". The minimum evidence column is the operational part of the table: a decision made without it is reversible by anyone consulted.

| Decision | Owner | Consulted | Minimal evidence |
|---|---|---|---|
| Priority and investment | PM | UX + Tech Lead | value, urgency, risk and opportunity cost |
| Problem and outcome | PM | UX + Tech Lead | problem evidence and outcome metrics |
| Journey and experience | UX | PM + Tech Lead | research, flow, prototype and UX criteria |
| Scope of delivery | PM | UX + Tech Lead | outcome, capacity, dependencies and risks |
| Architecture and implementation | Tech Lead | PM + UX | alternatives, trade-offs, risk and validation |
| Architectural exception | Tech Lead | affected owner | ADR, term, consequence and reversal plan |
| Product acceptance | PM | UX + stakeholder | product criteria and approval evidence |
| Experience acceptance | UX | PM + Tech Lead | UX, accessibility and validation criteria |
| Merge and release | Tech Lead, by policy | PM + UX according to risk | CI, evidence pack, rollout and rollback plan |
| Risk exposure R3/R4 | PM + Tech Lead | UX when there is an impact on the user | impact, mitigation, observability and rollback |
| System improvement priority | domain owner; PM sorts the backlog | threesome | telemetry, frequency, impact and effort |
| Gate change | Tech Lead + independent reviewer | PM and UX if affected | false positives, covered risk and adoption plan |

Two readings of this table are worth highlighting. **Gate change requires independent reviewer** — it is the only line in which the owner does not decide alone within the domain itself, because relaxing the verification that evaluates the work itself is the shortest path to the absence of verification. And **high risk exposure has two owners**, deliberately: neither the product nor the technique can expose the user alone.

---

## Tiebreaker rule

When the discussion stalls, the domain decides.

| Subject in dispute | Decide | Registration required |
|---|---|---|
| Value, priority and outcome | PM | discarded alternative and reason |
| Experience, usability and accessibility | UX | user evidence considered |
| Architecture, security and reliability | Tech Lead | trade-off accepted and ADR when structural |

The three recurring conflicts follow this rule without exception:

- **Scope versus deadline** belongs to the PM, who decides what comes out — not what is done halfway.
- **Experience versus feasibility** is resolved by conscious adaptation: the Tech Lead informs the restriction, the UX redesigns preserving the outcome, and the PM decides whether the reduced outcome is still valid.
- **Risk against speed** belongs to the Tech Lead when the risk is technical, and escalates to the sponsor when it is irreversible, regulatory or far-reaching. **Risk of this nature cannot be resolved within the trio.**

Which is not valid in either case: deciding by silent consensus. A tie recorded as "we continue like this" without a nominal owner reappears as a rework in the first challenge.

---

## Pass-through contracts

Each arrow between papers is a contract, not a conversation. The issuer delivers defined inputs; the receiver returns a defined result.

| From | To | Delivery | Wait back |
|---|---|---|---|
| PM | UX | problem, segment, outcome, restrictions and questions | user evidence, journey, flow and experience criteria |
| PM | Tech Lead | problem, candidate scope, metrics and constraints | feasibility, risks, dependencies and technical options |
| UX | PM | evidence, needs, hypotheses and experience risks | PRD scope and update decision |
| UX | Tech Lead | flow, states, content, accessibility and prototype | compatible contracts and implementation strategy |
| Tech Lead | PM | cost, risks, dependencies, alternatives and operational impact | investment decision, cut or sequencing |
| Tech Lead | UX | existing platform, latency, data and component constraints | conscious adaptation of the experience without losing the outcome |
| Threesome | agents | approved artifact, criteria, gates, risk and permissions | change executed, validated, documented and evidenced |
| Agents | threesome | evidence pack, disagreements and pending decisions | approval, correction, postponement or escalation |

### Definition of Ready for agentic execution

An item is only executed by agents when **problem and user are explicit, outcome and metrics are defined, human owner is known, scope and out-of-scope are clear**, UX flow and states sufficient for the task, sufficient contracts and technical restrictions, verifiable acceptance criteria, risk class and gates defined, authorized access and critical queries resolved or explicitly assumed.

Dispatching without this does not speed up delivery: it transfers the ambiguity into execution, where it costs an external turn to be discovered.

### Definition of Done of the cycle

The cycle closes when product, UX and engineering criteria are covered; approved mandatory tests and gates; assessed architectural impact; known risks and limitations; updated documentation and canonical sources; approvals identified; linked backlog, commits, PR, release and telemetry; rollout observed without relevant regression or correction plan; and learnings forwarded to the correct loop.

---

## Agents and their sponsors

Every agent has a human who is responsible for what they produce. The table serves the opposite of the most common question: not "what does this agent do", which is in [`agentes/`](../agentes/README.md), but **"when this goes wrong, who gets called?"**.

| Human | Sponsor | Matching loops |
|---|---|---|
| **PM** | Intake, Product Manager, Adversarial PM, Meeting Context, Product Validation | [🚦 Triage](../loops/00-intake-and-triage.md), [🔦 Scout](../loops/01-discovery-and-research.md), [🎨 Studio](../loops/02-product-and-ux-planning.md), [🎭 Rehearsal](../loops/07-release-candidate-validation.md) |
| **UX** | UX Specification | [🔦 Scout](../loops/01-discovery-and-research.md), [🎨 Studio](../loops/02-product-and-ux-planning.md) |
| **Tech Lead** | Tech Lead Discovery, Specification TL, Adversarial TL, Orchestrator, Software Engineer, QA, Security Review, Architecture Review, Adversarial Code Reviewer, PR, Release, Observability | [🗺️ Drafting](../loops/03-technical-specification.md) to [🐤 Canary](../loops/08-production-release-and-observation.md) |
| **Trio** | Knowledge, Telemetry, Auto Dream, Critic | [🗄️ Archivist](../loops/09-knowledge-curation.md), [🌙 Dream](../loops/10-continuous-improvement.md), [☀️ Daily](../loops/11-daily-operations.md) |

---

## The antipattern

**Decision with no nominal person responsible.** The symptom is recognizable: there is an approved artifact that no one can explain — the reason for a choice is not in the ADR, it is not in the PRD and it is not in the heads of any of the three people. This almost always arises from an implicit consensus at a previous stage, where the correct owner was not called.

The correction is not retroactive. An unowned decision is reopened with the correct owner, and the cost of this reopening is the metric that shows whether the decision rights matrix is ​​being used.

---

*Previous: [Methodology Index](README.md) · Next: [Human Checkpoints](02-checkpoints-humanos.md).*
