#02 — Human checkpoints

> Where exactly a person enters, with what question, for how long and what they need to see to answer.

The principle that organizes this page: **the human does not review the process — he answers an objective question.** No one follows the entire diff or reads the PRD line by line. At each checkpoint, the system delivers the requested decision, the agents' recommendations, the discarded alternatives, the risks and the gate evidence. The person responds.

What makes this possible is not trust in the agent: it is the [gate architecture](../GATES.md). Five layers of verification filter out everything deterministic before anyone is called. **A checkpoint only exists where a machine cannot decide.** If a human is being called for something verifiable, the gate is in the wrong place — and that is a defect in the harness, not the checkpoint.

---

## The six checkpoints

| Milestone | Question | Trigger | Owner | Expected time |
|---|---|---|---|---:|
| **H1** | Is it worth investing in this problem? | approved discovery gate | PM or sponsor | 5–10 min |
| **H2** | Is this what we will build? | approved product gate | PM, with UX as co-author | 10–15 min |
| **H3** | Do we accept the trade-off? | new ADR, architectural exception or R3/R4 risk | Tech Lead or Domain Expert | 10–20 min |
| **H4** | Can we integrate? | Open PR with green CI, according to risk class | Code Owner of the path | 5–15 min |
| **H5** | Can we expose the risk? | approved release candidate, in R3/R4 or critical exposure | Tech Lead; PM coapproves | 3–10 min |
| **H6** | Did the system learn correctly? | weekly cycle of [🌙 Dream Loop](../loops/10-continuous-improvement.md) | work system owner | 10–20 min |

Combined, the six represent between 30 and 45 minutes of human time per medium-risk delivery. **H3 and H5 are conditional**: on a low-risk item with green gates, the cycle goes from H2 straight to H4 — three human decisions from problem to production.

### What each person decides

**H1 — is it worth investing?** Occurs after the [🔦 Scout Loop](../loops/01-discovery-and-research.md), over a consolidated `PB.md`. The person reviews the problem, user, value, constraints and risks, and decides to move forward, adjust the question, postpone or close. Terminating is a legitimate response and the cheapest of all at this point.

**H2 — is this what we will build?** It occurs after [🎨 Studio Loop](../loops/02-product-and-ux-planning.md), on top of a `PRD.md` already subjected to adversarial criticism. The review is about **decisions and gaps**, not about the entire document: what the criticism raised and how it was responded to. Decide to approve, reduce, expand or return.

**H3 — do we accept the trade-off?** Conditional. Only occurs when [🗺️ Drafting Loop](../loops/03-technical-specification.md) produces a new ADR, an architectural exception, or a high-risk change. The review covers the decision, discarded alternatives, and future impact—not the entire design. When there is no new structural decision, this checkpoint does not happen.

**H4 — can we integrate?** Occurs in the [🚪 Gatekeeper Loop](../loops/06-pr-and-merge.md), and the weight varies by risk class. The person reviews the evidence pack, the highest risk sections and exceptions — never the complete diff.

**H5 — can we expose the risk?** Conditional, in [🐤 Canary Loop](../loops/08-production-release-and-observation.md). Reviews impact, rollout plan, rollback and health signals. R0 and R1 continue without checkpoint when rollback is proven.

**H6 — did the system learn correctly?** The only checkpoint that does not deal with the product: it deals with the work system itself. Mandatory for sensitive memory changes, item P0/P1 and **any gate change**; by sampling in the remainder.

---

## What the person receives

A checkpoint without an evidence pack is not a decision: it is a request for trust. The package is generated automatically — evidence assembled manually at the end of the task is selective in nature.

| Item | Content |
|---|---|
| **Decision requested** | one sentence, in closed question format |
| **Recommendation** | the position of agents and their trust |
| **Alternatives** | what was considered and why it was discarded |
| **Risks and trade-offs** | what is accepted when approving |
| **Delta** | what has changed since the previous checkpoint |
| **Evidence** | result of the executed gates, with link to the raw output |
| **Pending issues** | open exceptions and declared confidence level |
| **Links** | complete artifacts, code and execution |

**delta** is the field that most reduces human time in the second pass: when an item returns for a new decision, the person reads what changed, not the entire set.

Details of the evidence pack's disk structure are in [Documentation](../DOCUMENTATION.md). The quality test is the same there and here: **can someone else redo the check without asking anyone who produced it?**

---

## The two locks

Two rules protect the entire mechanism. They are not label recommendations — they are conditions of approval validity.

**Silence is never approval.** Lack of response keeps the item at a standstill. Deadline pressure appears as a stopped and visible item, not as tacit progress. [☀️ Daily Loop](../loops/11-daily-operations.md) exists, in part, so that a stopped item appears the next day.

**Material change invalidates the related approval.** If the artifact changed materially after the endorsement, the endorsement does not cover the new version. What counts as material is defined by risk class and verified by automation — not by the assessment of who made the change.

---

## How risk changes the checkpoint

The risk class is what determines how many approvals the change requires and how much automation it can use. It is proposed by one agent and contested by another; **the highest justified risk prevails**.

| Class | Features | What does it require in H4 and H5 |
|---|---|---|
| **R0 — minimum** | documentation and formatting; no change in behavior, data or contracts | automatic merge after gates; sample review |
| **R1 — low** | refactoring or localized change covered by existing tests | a short owner review; automatic deployment with observation |
| **R2 — medium** | new product behavior or change in internal contract | approval of the affected person; automated canary and rollback |
| **R3 — high** | persisted data, migrations, public contracts, authentication, secrets, payments, availability | technical **and** product approval; explicit approval before production |
| **R4 — critical** | regulatory, financial or destructive impact; irreversible action | double approval with segregation of duties and monitoring during release |

Manual risk reduction requires recorded justification. Scope change recalculates risk. Sensitive paths automatically elevate risk. And **unresolved doubts prevent classification as R0 or R1** — the absence of information is a risk, not the absence of it.

---

## Autonomy — how many checkpoints there are today

The number of checkpoints is not fixed: it decreases as the system demonstrates that the gates are trustworthy. This is the only dimension of the model that moves deliberately over time.

| Level | The system does | The person does |
|---|---|---|
| **A0 — watched** | performs under supervision | approves all transitions |
| **A1 — autonomous execution** | implements and validates | keeps H1, H2, H4 and H5 |
| **A2 — merge due to risk** | auto-merge in R0 | short review in R1; specific owners in R2+ |
| **A3 — controlled autonomous delivery** | automatic deploy to R0/R1, with mandatory rollback | operates in exceptions and high risks |
| **A4 — exception-oriented** | operates healthy flow without intervention | receives decisions and incidents; sample audit |

**Increasing autonomy requires all criteria simultaneously:** minimum volume of deliveries observed, low rate of escaped defects, tested and reliable rollback, gates with few false positives, correctly classified risk, auditable evidence and actually reduced human time.

The restriction that closes the mechanism: **the harness imposes a ceiling on autonomy.** A repository without the corresponding verification layer does not sustain the level, regardless of the team's history. Details of maturity levels are in [Gates](../GATES.md).

---

## Where to safely cut checkpoint

Each cut below is only safe after history demonstrates that the corresponding gate is trustworthy. Cutting before that doesn't increase autonomy — it increases unobserved risk, which is the worst kind.

| Movement | Prerequisite |
|---|---|
| Combine H2 and H3 into small, known changes | standard already validated in previous cycles |
| Eliminate H3 when there is no ADR, exception or relevant risk | reliable risk rating |
| Apply H4 by sampling in R0 | low history of escaped defects |
| Make H5 automatic in R0/R1 | Proven rollback in production |
| Show only delta since last approval | evidence pack with delta |
| Direct the person to the hotspots, not the diff | risk analysis per section |
| Remove a valueless gate | measurement of false positives |

The sign that the cut was too early is not the incident: it is the **rework after the next checkpoint**. It appears first, and is the metric to watch.

---

## What degrades first

When this mechanism starts to fail, the symptom is not one more checkpoint. It is the human proportion rising silently, always for one of these three causes.

| Symptom | Probable cause | Where to fix |
|---|---|---|
| The person asks for the complete artifact before responding | evidence pack incomplete or without delta | [Documentation workflows](07-workflows-de-documentacao.md) |
| Checkpoints pile up unanswered | poorly formulated question, or wrong owner | [Papers](01-papeis.md) |
| The same decision comes back twice | material change without automatic invalidation | [Gates](../GATES.md) |

---

*Previous: [Papers](01-papeis.md) · Next: [Triggers and shots](03-gatilhos-e-disparos.md).*
