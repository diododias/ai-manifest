# Metrics

Metrics for an AI-first squad must answer a practical question: **is the team turning ideas into user value faster without transferring cost to quality, operations or people?** No single number can answer it. AI can increase output while stability falls, reduce coding time while review queues grow, or lower model cost while human correction becomes more expensive.

This page defines a balanced measurement system for a product squad. It combines product outcomes, flow, software delivery, reliability, quality, human-AI collaboration, economics and team health. The purpose is to improve the system, never to rank individuals or maximize activity.

## Define the measurement contract first

Every metric must have a contract before it enters a dashboard:

| Field | What must be explicit |
|---|---|
| **Question** | the decision this metric is expected to inform |
| **Definition and formula** | numerator, denominator, inclusion rules and what counts as success or failure |
| **Scope** | product, service, environment, work type and risk class represented |
| **Source** | system of record and how events are correlated |
| **Window and statistic** | calendar window, timezone, median or percentile, and treatment of partial data |
| **Owner and response** | who investigates and what action a meaningful change can trigger |
| **Guardrail** | the companion signal that prevents local optimization |

Change a definition only prospectively and annotate the time series. A trend assembled from different definitions is not a trend.

Five operating rules matter:

1. Read **counts and rates together**. Three failed deployments mean something different out of five deployments and out of five hundred.
2. Segment before comparing: service, risk, work type and degree of AI involvement can explain a change that a global average hides.
3. Prefer the median (P50) and tail percentiles such as P85 for time. A mean hides the few items that spend weeks blocked.
4. Compare the squad with its own baseline and target. Industry benchmarks are context, not a performance contract.
5. Treat missing, delayed or non-correlatable data as a visible metric-quality failure, never as zero.

## The minimum squad dashboard

A useful first dashboard fits on one screen. It contains an outcome, guardrails and enough diagnostic signals to explain movement:

| Area | Minimum signal | Question answered |
|---|---|---|
| **Product** | one primary outcome plus one harm or quality guardrail | did the delivered change help the user without causing an unacceptable side effect? |
| **Delivery** | total deployments, successful deployments and failed deployments | how much reached production, and how much required immediate intervention? |
| **Stability** | change fail rate and failed deployment recovery time | how often did delivery destabilize the service, and how quickly did the squad recover? |
| **Flow** | cycle time P50/P85, work-in-progress age and blocked time | where is work waiting, especially in the long tail? |
| **Quality** | escaped defects by severity and rework rate | how much supposedly finished work returned as correction? |
| **AI collaboration** | independent first-pass acceptance, human correction effort and escalation quality | is AI reducing total effort while remaining governable? |
| **Economics** | cost per accepted Work Item | is the whole system becoming more efficient, not merely each invocation? |
| **Team health** | review load, toil and a short friction pulse | is speed being financed by overload or hidden manual work? |

Start with these signals and add a metric only when a recurring decision cannot be made without it.

Here, a **Work Item** is an independently accepted unit of product or engineering change with explicit completion criteria. Keep that unit stable enough for comparisons between periods.

## Delivery and stability

The deployment family is the operational core. Define it per production service or releasable product; mixing a daily web service with a quarterly mobile release destroys comparability.

| Metric | Definition | Use |
|---|---|---|
| **Total deployments** | count of production deployments or user releases in the window | provides the denominator and shows delivery cadence |
| **Deployment frequency** | total deployments per unit of time, or the typical interval between deployments | normalizes cadence across reporting windows |
| **Successful deployments** | deployments that complete without change-related degradation requiring immediate remediation | distinguishes useful cadence from repeated recovery work |
| **Failed deployments** | deployments that cause degradation and require rollback, hotfix, fix-forward, patch or equivalent immediate intervention | exposes the absolute operational burden created by changes |
| **Change fail rate** | `failed deployments / total deployments × 100` | makes failure comparable across windows with different deployment volume |
| **Change lead time** | elapsed time from change committed to change successfully running in production; report P50 and P85 | shows how quickly committed work reaches users and reveals the slow tail |
| **Failed deployment recovery time** | elapsed time from a change-related impairment to restored service; report P50 and P85 | measures the recovery value stream rather than generic incident duration |
| **Deployment rework rate** | `unplanned corrective deployments / total deployments × 100` | shows how much deployment capacity is spent correcting user-facing defects |

Counts, rates and time must be read together. If deployments double from 50 to 100 and failures rise from 2 to 3, the **failed deployment count** worsened while the **change fail rate** improved from 4% to 3%. The correct conclusion is neither “quality improved” nor “quality worsened” in isolation: the squad delivered more frequently with a lower probability of failure per deployment, but created more absolute recovery events. User impact, severity and recovery time decide whether that trade-off is acceptable.

The current DORA delivery model groups change lead time, deployment frequency and failed deployment recovery time as throughput, and change fail rate plus deployment rework rate as instability. The definitions above follow that model while keeping the raw counts needed for squad operations.

## Flow and predictability

Delivery metrics start at commit, but many delays occur earlier. Flow metrics expose the whole path from committed work to observed outcome.

| Metric | Definition | Healthy interpretation |
|---|---|---|
| **End-to-end cycle time** | selected/started to accepted in production; P50 and P85 | both center and long tail fall without larger failure rates |
| **Work-in-progress age** | current age of every active item | old items trigger swarming or scope reduction before they become invisible inventory |
| **Blocked-time ratio** | `time blocked / total cycle time × 100` | reveals dependency and decision queues |
| **Flow efficiency** | `active time / total cycle time × 100` | distinguishes work effort from waiting |
| **Review wait time** | ready for review to first substantive review | detects the human queue created when AI raises change throughput |
| **Batch size** | changes, files or independently releasable behaviors per item or deployment | smaller, reversible batches should improve feedback and recovery |
| **Predictability** | share of items completed within the service expectation for their class | supports planning without converting estimates into individual quotas |

Throughput or story points alone are not outcome metrics. Closing more items can mean smaller tickets, split reporting or more low-value work.

## Quality, reliability and security

| Metric | Definition | Important segmentation |
|---|---|---|
| **Escaped defects** | defects found after the stage that should have detected them | detection stage, severity, failure mode and affected service |
| **Post-acceptance rework rate** | accepted items materially reopened or corrected within `N` days / accepted items | planned enhancement versus correction |
| **First-pass gate acceptance** | items accepted at an independent gate without material correction / evaluated items | gate type, change risk and AI involvement |
| **Service-level objective (SLO) attainment and error-budget consumption** | user-facing reliability against an agreed objective | service, user journey and burn window |
| **Recurring incident rate** | incidents repeating a known cause / incidents | cause class and whether the prior corrective action was completed |
| **Security escape rate** | confirmed vulnerabilities found after the control expected to catch them | severity, control and exposure |
| **Flaky verification rate** | non-deterministic check outcomes / check executions | test suite, owner and time to quarantine or repair |

A green pipeline is only evidence that the executed checks passed. Pair pass rates with escapes, canaries or known-bad tests so a check that silently verifies nothing cannot look healthy.

## Product value and learning

Every squad needs a primary outcome tied to the user behavior or result it exists to improve. The exact metric is product-specific: successful task completion, activation, retained use, conversion, time saved, error reduction or another observable outcome. Pair it with guardrails such as complaints, abandonment, accessibility, latency, privacy or support contacts.

Useful product and learning signals include:

| Metric | What it shows |
|---|---|
| **Outcome movement** | change in the selected user or business result against baseline |
| **Adoption with successful use** | users who not only access the capability but complete its intended task |
| **Experiment decision rate** | experiments that produce a keep, change or stop decision / completed experiments |
| **Time to validated learning** | hypothesis recorded to evidence-backed decision |
| **Support burden after change** | support contacts or complaints attributable to a release |

Deployment frequency without outcome movement describes an efficient feature factory, not a high-performing product squad.

## Human-AI collaboration

First classify AI involvement on each Work Item. A practical scale is `none`, `assisted` (AI proposes under direct execution), `delegated` (AI completes a bounded task) and `coordinated` (AI orchestrates several bounded tasks). This field is context for analysis, not a target to maximize.

| Metric | Definition | What to watch |
|---|---|---|
| **AI reliance by activity** | share of relevant activities where the squad depends on AI to complete the work | reliance is more meaningful than prompts, messages or seat activation |
| **Independent first-pass acceptance** | AI-involved outputs accepted without material correction by a separate control | segment by task and risk; never let the producer self-approve |
| **Human correction effort** | review, repair and clarification time per accepted AI-involved item | catches “fast generation, slow cleanup” |
| **Autonomous completion within scope** | delegated items completed and accepted without unauthorized expansion / delegated items | pair with quality and escalation signals |
| **Escalation quality** | necessary escalations raised in time, plus missed and unnecessary escalations | a near-zero escalation rate may indicate silent guessing, not maturity |
| **Context retrieval success** | tasks that retrieved current authoritative context / tasks requiring it | pair with stale or conflicting-context incidents |
| **Evidence and provenance coverage** | accepted items with traceable inputs, outputs, checks and accountable owner / accepted items | coverage without independent validity becomes template filling |
| **AI safety exceptions** | permission, privacy, secret, scope or policy violations and near misses | report absolute count and severity; do not normalize serious violations away |

Compare AI involvement classes on outcome, cycle time, failure, rework, human effort and cost. “AI-assisted work is faster” is incomplete if its review time, defect escape or support burden rose.

## Economics and team health

**Cost per accepted Work Item** is the primary economic unit:

`(model + platform + CI + human review + correction + allocated incident cost) / accepted Work Items`

Keep infrastructure allocation pragmatic; directional consistency is more valuable than false accounting precision. Also track model and tool cost by activity, retry waste and cost of failed or abandoned work, but never optimize invocation cost while ignoring correction and incident cost.

Team health supplies the guardrail that system telemetry cannot:

- short, regular pulse on friction, cognitive load and confidence in the delivery system;
- time spent on toil, interruptions and avoidable waiting;
- review load and concentration, so one expert does not become the invisible gate for all AI output;
- knowledge distribution and ability to operate without a single person;
- protected time for learning, maintenance and improvement.

Use these signals at squad level with psychological safety and minimum cohort sizes. They are system diagnostics, not performance ratings.

## How to read the panel

| Observed movement | Likely interpretation | First investigation |
|---|---|---|
| throughput rises; stability and outcomes hold or improve | sustainable gain | identify the capability worth standardizing |
| deployments rise; failures, rework or support contacts rise faster | AI or automation amplified a weak delivery system | batch size, verification coverage and release controls |
| generation time falls; review wait and correction effort rise | work moved into the human queue | task boundaries, context quality and independent checks |
| AI cost falls; cost per accepted item rises | false economy | retries, rework, model routing and failure cost |
| delivery improves; product outcome stays flat | output is disconnected from value | prioritization, user evidence and experiment design |
| escalation approaches zero; scope or factual failures rise | the system is guessing silently | escalation conditions and ambiguity detection |
| averages improve; P85 worsens | the long tail is being hidden | blocked work, dependencies and work-type segmentation |

Metrics identify where to investigate; they do not prove causality. Change one material part of the system at a time, record the hypothesis and guardrails, and compare over a representative window.

## Collection and cadence

Use stable identifiers to connect work item, commit, build, deployment, incident, product event and AI execution. Minimize captured prompt or content data; collect classification, timing, cost, outcome and provenance unless deeper content is explicitly authorized.

| Cadence | Review |
|---|---|
| **Continuous / daily** | SLOs, error budget, failed deployments, security and safety events |
| **Weekly squad review** | flow, deployment counts, failures, rework, review load and blocked items |
| **Monthly improvement review** | product outcome, AI comparison, economics, team pulse and metric quality |
| **Quarterly** | maturity profile, target definitions, policy and platform investment |

Begin with four to six weeks of baseline, choose one bottleneck and define a target plus guardrails. Targets should express a desired system change — for example, “reduce cycle-time P85 by 20% while change fail rate and correction effort do not worsen” — rather than a naked volume quota.

## What not to use as productivity

- commits, pull requests, lines of code, story points, prompts or tokens produced;
- AI seat activation or percentage of AI-generated code;
- a single composite score that hides trade-offs;
- individual leaderboards for people or agents;
- gate pass rate without escape and canary evidence;
- utilization close to 100%, which removes the capacity to review, recover and learn.

Current DORA guidance defines five software-delivery performance metrics across throughput and instability, and its 2025 AI research emphasizes that AI amplifies the surrounding system. See [DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) and the [2025 State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/). The broader dashboard on this page adds the product, human, governance and economic signals a squad needs to interpret those delivery metrics in an AI-first environment.

---

*Next: [Maturity](MATURITY.md) — how these signals support a path from opportunistic assistance to governed, adaptive operation.*
