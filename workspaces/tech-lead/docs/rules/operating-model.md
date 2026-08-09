---
title: Agent Team — operating system of the human trio
status: canonical
updated_at: 2026-08-08
---

# Agent Team — operating system of the human trio

> Canonical view of the Agent Team for a team led by **Product Manager, UX and Tech Lead**. Related details: [90/10 operating model](rules/operating-model-90-10.md) · [full visual flow](operations/end-to-end-journey.md) · [flows per phase](operations/journey-by-phase.md) · [multi-agent workflows](workflows/README.md) · [Tech Lead workspace](architecture/tech-lead-workspace.md).

> Agents: [detailed catalog and contracts](agents/catalog.md) · [Meeting Context Agent for transcriptions](agents/meeting-context-agent.md).

## 1. Purpose

Transform a business need into validated software through a small human core that directs a workforce of specialized agents.

The model must:

- combine specialized agents, people and automations
- keep decisions, code and documentation in sync
- produce evidence at all stages of the cycle
- scale delivery without losing security and governance
- reserving human attention for intent, judgment, risk and responsibility
- make execution, validation and evidence collection progressively autonomous
- improve the work system itself with each cycle

The human trio does not attempt to perform all the work manually. It operates the system:

- **Product Manager:** drives value, priority and business results
- **UX:** drives user understanding, experience and quality of use
- **Tech Lead:** directs feasibility, architecture, technical quality and operational risk
- **Agents:** research, propose, implement, criticize, validate and document
- **Automations:** perform deterministic checks, blocking and traceability

---

## 2. Operating principles

- People define priority, restrictions, limits of autonomy and final approval.
- Agents perform specialized work and produce evidence.
- Each stage has an entrance, exit, human owner and passage criteria.
- The human responsible decides; the primary agent prepares and recommends.
- Whoever produces a change is not solely responsible for validating it.
- Relevant disagreements between agents are resolved by the human owner of the domain.
- The stage ends with a coherent artifact, not with isolated analyses.
- The repository contains rules and executable context of the product.
- Harness transforms patterns into repeatable checks.
- Small, reversible and traceable changes reduce risk and rework.
- Asynchronous communication is the default; Meeting exists to decide, not to narrate status.
- Human approval must receive synthesis, alternatives, risks and evidence, not raw context.
- A material change invalidates the related approval.
- Lack of response never equates to approval.
- Autonomy increases only when metrics and gates demonstrate security.

## 3. Agent Teams operating model

- Each phase can activate a temporary team of specialized agents.
- The [agent catalog](agents/catalog.md) defines the contracts and limits of each role.
- Each agent analyzes the problem based on an explicit responsibility.
- A primary agent conducts and consolidates the phase artifact.
- Adversarial agents look for ambiguities, gaps, risks and weak assumptions.
- Contributions and disagreements are recorded before consolidation.
- The human owner intervenes in decisions regarding value, experience, risk or exception — not in every execution.
- The context passes between phases through versioned artifacts and evidence packs.
- Agents receive minimum access, limited scope and objective stop condition.

### Minimum mission structure for agents

- objective and expected result
- context and canonical sources
- scope and out of scope
- input artifact
- output artifact
- acceptance criteria
- mandatory gates
- authorized tools and permissions
- risk class
- escalation condition
- human owner of the decision

---

## 4. The human trio

### 4.1 Product Manager — owner of value and priority

#### Responsibilities

- maintain vision, objectives, outcomes and roadmap
- order the backlog by value, urgency, risk and learning
- formulate the problem before committing to a solution
- identify stakeholders, commercial restrictions and expected results
- define scope, out of scope and success criteria
- ensure traceability between problem, investment, delivery and result
- decide to advance, adjust, postpone or close an item
- approve value with stakeholders and record pending issues
- prioritize improvements originating from telemetry
- operate intake, discovery, research, planning and product validation agents

#### Recurring inputs

- business strategy and objectives
- customer and stakeholder needs
- UX research and evidence
- product and operation metrics
- Tech Lead restrictions, risks and estimates
- approval and production feedback
- incidents, flow cost and improvement opportunities

#### Recurring outputs

- ordered and owned backlog
- objective and expected outcome
- `PB.md` approved
- `PRD.md` consolidated
- explicit scope and out-of-scope
- success metrics and criteria
- decisions H1, H2 and product acceptance
- priority of improvement demands
- communication of results to stakeholders

#### It is not the sole responsibility of the PM

- design the experience yourself
- define architecture or technical solution
- approve technical exception without Tech Lead
- replace user evidence with stakeholder opinion

### 4.2 UX — owner of the experience and evidence about the user

#### Responsibilities

- plan and execute research proportional to risk
- represent users’ needs, context and limitations
- map journeys, flows, tasks and friction points
- define principles of experience, content and interaction
- specify nominal, empty, loading, error, permission and recovery states
- ensure accessibility, consistency and usability
- produce prototypes with the fidelity necessary to decide
- validate hypotheses before and after implementation
- monitor the quality of experience in approval and production
- operate research agents, synthesis, UX writing, prototyping and heuristic evaluation

#### Recurring inputs

- problem, audience and outcome defined with the PM
- behavior data, support and analytics
- technical constraints and opportunities informed by the Tech Lead
- design system and existing standards
- feedback from stakeholders and users
- results of experiments and approval

#### Recurring outputs

- research plan and evidence
- personas or segments when useful for the decision
- current journey and desired journey
- flows, wireframes and prototypes
- specification of UX, content, states and accessibility
- hypotheses and experiment risks
- UX acceptance criteria
- validation report and post-delivery recommendations

#### It is not the sole responsibility of UX

- decide business priority
- promise scope without alignment with PM and Tech Lead
- produce screens without explicit problems and hypotheses
- validate experience only by visual adherence

### 4.3 Tech Lead — owner of technical integrity and operational risk

#### Responsibilities

- assess feasibility and risk from discovery
- define architecture, contracts, integrations and data strategy
- register relevant alternatives, trade-offs and ADRs
- decompose the solution into small, independent and verifiable units
- define testing, observability, rollout and rollback strategy
- keep architectural boundaries, standards and technical debt under control
- define and evolve repository rules, hooks, gates, skills and harnesses
- protect security, privacy, reliability and maintainability
- decide technical exceptions and escalate R3/R4 risks
- operate specification, engineering, QA, security, architecture, review and release agents

#### Recurring inputs

- `PB.md`, `PRD.md` and UX specification
- existing architecture and contracts
- SLOs, incidents and technical telemetry
- inventory of platform dependencies and restrictions
- security, privacy and compliance requirements
- team capacity and operational cost

#### Recurring outputs

- feasibility and risk assessment
- `PLAN.md`, `SPEC.md`, `ADR.md`, `TASKS.md` and `CHECKLIST.md`
- implementation and testing strategy
- migration plan, rollout and rollback when applicable
- technical gates and evidence pack
- H3 decision and technical recommendation on H4/H5
- technical health backlog and harness improvements

#### It is not the exclusive responsibility of the Tech Lead

- redefine product objective for technical convenience
- choose experience without UX participation
- approve own architecture deviation without independent review
- transform every technical decision into a human meeting

### 4.4 Shared responsibility

The three are jointly responsible for:

- quality of the problem before the solution
- coherence between value, experience and viability
- explicit risks and traceable decisions
- observable acceptance criteria
- protection of data and users
- health of agentic flow
- learning after delivery

No person is a passive “translator” for another. PM, UX and Tech Lead bring decisions from their own domain and together build the contract that the agents will execute.

---

## 5. Decision rights

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
| Merge and release | Tech Lead by policy | PM + UX according to risk | CI, evidence pack, rollout and rollback |
| Risk exposure R3/R4 | PM + Tech Lead | UX when there is an impact on the user | impact, mitigation, observability and rollback |
| Improvement priority | domain owner; PM sorts the backlog | threesome | telemetry, frequency, impact and effort |
| Gate change | Tech Lead + independent reviewer | PM/UX if affected | false positives, covered risk and adoption plan |

### Tiebreaker rule

- value, priority and outcome: decides the PM
- experience, usability and accessibility: decides the UX
- architecture, security and reliability: decides the Tech Lead
- conflict between domains: record alternatives, impact and joint decision
- irreversible, regulatory or far-reaching risk: escalate to the sponsor or formal person responsible

---

## 6. Passage contract between the three professionals

| From | To | Inputs delivered | Expected receiver output |
|---|---|---|---|
| PM | UX | problem, segment, outcome, restrictions and questions | user evidence, journey, flow and experience criteria |
| PM | Tech Lead | problem, candidate scope, metrics and constraints | feasibility, risks, dependencies and technical options |
| UX | PM | evidence, needs, hypotheses and experience risks | scope/priority decision and PRD update |
| UX | Tech Lead | flow, states, content, accessibility and prototype | compatible contracts, tasks and implementation strategy |
| Tech Lead | PM | cost, risks, dependencies, alternatives and operational impact | investment decision, cut or sequencing |
| Tech Lead | UX | constraints, latency, data, platform and existing components | conscious adaptation of the experience without losing the outcome |
| Threesome | Agent Team | approved artifact, criteria, gates, risk and permissions | change executed, validated, documented and evidenced |
| Agent Team | Threesome | evidence pack, disagreements and pending decisions | approval, correction, postponement or escalation |

### Definition of Ready for agentic execution

- explicit problem and user
- defined outcome and metrics
- known human owner
- clear scope and out of scope
- enough UX flow and states for the task
- sufficient contracts and technical restrictions
- verifiable acceptance criteria
- risk class and defined gates
- authorized access and tools
- critical doubts resolved or explicitly addressed

### Definition of Done of the cycle

- product, UX and engineering criteria covered
- mandatory tests and gates approved
- architectural impact assessed
- known risks and limitations
- updated documentation and canonical sources
- human and automated approvals identified
- linked backlog, artifacts, commits, PR, release and telemetry
- rollout observed without relevant regression or with correction plan
- learnings and improvements forwarded to the correct loop

---

## 7. Human ceremonies

Ceremonies are decision points for the trio. Preparation, analysis, status updates and generation of artifacts are preferably handled by agents and automations.

### 7.1 Daily asynchronous pulse

- **Cadence:** daily; reading in up to 10 minutes per person
- **Participants:** PM, UX and Tech Lead
- **Preparation by agents:** flow status, changes, blockages, risk and required decisions
- **Inputs:** updated table, partial evidence packs, alerts and divergences
- **Agenda:** only blocks, new information and decision requests
- **Outputs:** owners, decision deadline and registered replanning
- **Should not become:** daily individual report meeting

### 7.2 Triage and priority

- **Cadence:** weekly, 30–45 minutes
- **Owner:** PM
- **Participants:** PM, UX and Tech Lead
- **Inputs:** new items, metrics, feedback, incidents, dependencies and capacity
- **Questions:** which problem comes in, which comes out and what needs discovery?
- **Outputs:** ordered backlog, owner, initial risk and upcoming discoveries
- **Gate:** minimally clear context, priority and responsible party

### 7.3 Discovery kickoff — H1

- **Cadence:** by opportunity; 30–45 minutes
- **Owner:** PM
- **Inputs:** consolidated intake, existing evidence and open questions
- **PM contribution:** problem, value, stakeholders and outcome
- **UX contribution:** gaps regarding user and research plan
- **Contribution from Tech Lead:** restrictions, dependencies and viability risk
- **Outputs:** discovery mission, initial `PB.md`, activated agents and timebox
- **Final decision:** move forward, adjust, postpone or close

### 7.4 Product and experience refinement — H2

- **Cadence:** per candidate item; 45–60 minutes
- **Owner:** PM; UX co-owner of the experience
- **Inputs:** `PB.md`, research, journey, prototype, proposed PRD and adversarial criticism
- **Questions:** Is this what we will build, for whom and with what result?
- **Outputs:** `PRD.md`, UX specification, acceptance criteria and approved scope
- **Gate:** critical gaps addressed, ambiguities reduced and measurable success

### 7.5 Solution and risk review — H3

- **Cadence:** on demand; mandatory for ADR, exception or high risk; 30–60 minutes
- **Owner:** Tech Lead
- **Inputs:** `PLAN.md`, `SPEC.md`, ADR, alternatives, threat model, test plan and adversarial criticism
- **PM contribution:** impact on outcome, deadline and scope
- **UX contribution:** impact on journey, content, accessibility and states
- **Outputs:** technical decision, accepted trade-offs, executable tasks and risks with owner
- **Gate:** traceability, critical gaps addressed and viable validation

### 7.6 Delivery review — H4

- **Cadence:** per increment or release candidate; 20–30 minutes
- **Owner:** PM for value; Tech Lead for technical integrity; UX for experience
- **Inputs:** demo prepared by agents, evidence pack, acceptance criteria and changes since H2/H3
- **Questions:** delivers the agreed outcome, works well and can it be integrated?
- **Outputs:** acceptance, adjustments, new items or justified rejection
- **Gate:** review approved, green IC and absence of blockers

### 7.7 Release decision — H5

- **Cadence:** per release; only synchronous when risk requires; 10–20 minutes
- **Owner:** Tech Lead; PM co-approves R3/R4
- **Inputs:** release candidate, risk, rollout, rollback, SLOs and health signals
- **Outputs:** release, pause, reduce exposure or return to implementation
- **Gate:** environment, secrets, migration, observability and rollback checked

### 7.8 Telemetry and improvement — H6

- **Cadence:** weekly, 45–60 minutes
- **Owner:** trio, with rotating facilitation
- **Inputs:** Auto Dream telemetry report, patterns, incidents, cost, feedback and proposals
- **Questions:** Did the system learn correctly and which improvement deserves investment?
- **Outputs:** validated memory, P0–P3 demands, owners, experiments and proposed process changes
- **Gate:** traceable evidence, separate learning hypothesis and revised sensitive change

### 7.9 Monthly system review

- **Cadence:** monthly, 60–90 minutes
- **Participants:** trio; sponsor or enablement when necessary
- **Inputs:** trends in outcome, quality, flow, cost, autonomy and false positives of gates
- **Outputs:** capacity adjustments, policies, tools, gates and autonomy level
- **Rule:** do not use an isolated metric to increase autonomy

### 7.10 Quarterly outcome review

- **Cadence:** quarterly, 60–90 minutes
- **Owner:** PM
- **Inputs:** outcomes, strategy, research, technical health, cost and accumulated learning
- **Outputs:** priorities for the next cycle, bets closed and capabilities to be developed

---

## 8. End-to-end development cycle

### 0. Intake and backlog screening

- **Workflow:** [intake and screening](workflows/00-intake-and-triage.md)
- **Human Owner:** Product Manager
- **Agents:** Intake Agent + Product Manager Agent
- **Objective:** register, deduplicate, contextualize and prioritize needs
- **Inputs:** problem, opportunity, request, feedback, incident or improvement
- **Activities:** validate fields, relate product/repository, identify duplicity and propose risk
- **Outputs:** Prioritizable Work Item, initial context, owner and preliminary risk
- **Gate:** minimally clear problem, priority, traceability and person responsible
- **Ceremony:** screening and priority

### 1. Discovery

- **Workflow:** [discovery and research](workflows/01-discovery-and-research.md)
- **Human owner:** PM; UX and Tech Lead respond for their domains
- **Agent Team:** Product Discovery Team
  - Product Manager Agent
  - UX Specification Agent
  - Tech Lead Discovery Agent
- **Objective:** understand problem, user, context, value and initial feasibility
- **Inputs:** Work Prioritized item, data, existing searches, constraints and questions
- **Dynamics:** parallel investigation, recording of hypotheses, synthesis by the Product Manager Agent and criticism by others
- **Outputs:** `PB.md`, evidence, initial journey, restrictions, risks and open questions
- **Minimum content:** problem, users, journey, value, restrictions and risks
- **Gate:** problem validated, desired experience understood and initial feasibility assessed
- **Ceremony:** discovery / H1 kickoff

### 2. Product and experience planning

- **Workflow:** [product and UX planning](workflows/02-product-and-ux-planning.md)
- **Human owner:** PM for product; UX for experience
- **Agent Team:** Product Planning Team
  - Product Manager Agent
  - UX Specification Agent
  - Adversarial Product Manager Agent
  - research, content or prototyping agents when necessary
- **Objective:** transform the problem into a clear, testable and usable proposal
- **Inputs:** `PB.md`, user evidence, constraints and H1 decision
- **Dynamics:** proposal → UX prototype/specification → adversarial criticism → review → consolidation
- **Outputs:**
  - `PRD.md`
  - desired journey and flow
  - wireframe or prototype in the required fidelity
  - states, content and accessibility criteria
  - success and acceptance criteria
- **Minimum content:** objectives, users, journeys, scope, out of scope, requirements and metrics
- **Gate:** critical gaps addressed, ambiguities reduced and success criteria approved
- **Ceremony:** product and experience refinement / H2

### 3. Technical specification

- **Workflow:** [technical specification](workflows/03-technical-specification.md)
- **Human Owner:** Tech Lead
- **Agent Team:** Technical Specification Team
  - Specification Tech Lead Agent
  - Adversarial Tech Lead Agent
  - Security, Data or Platform Agent when the risk requires it
- **Objective:** define how to build, validate, release and operate the solution
- **Inputs:** `PB.md`, `PRD.md`, UX specification, architecture, contracts and SLOs
- **Dynamics:** specification → critical review → response to gaps → decision
- **Outputs:**
  - `PLAN.md` — implementation strategy
  - `ADR.md` — relevant architectural decisions
  - `SPEC.md` — behavior and technical contracts
  - `TASKS.md` — small execution units
  - `CHECKLIST.md` — verifiable acceptance criteria
  - test plan, rollout, rollback and observability according to risk
- **Minimum content:** architecture, alternatives, trade-offs, risks and validation
- **Gate:** critical gaps addressed, trade-offs recorded and executable tasks
- **Ceremony:** review of solution and risk / H3 when necessary

### 4. Implementation

- **Workflow:** [standalone implementation](workflows/04-autonomous-implementation.md)
- **Human Owner:** Tech Lead by policy and exception
- **Agents:** Orchestrator Agent + Software Engineer Agents
- **Support:** repo harness, skills and code tools
- **Objective:** implement one small task at a time
- **Inputs:** task, SPEC, criteria, context, permissions and gates
- **Activities:** code, tests, documentation, commits and evidence
- **Outputs:** functional change ready for validation and traceable diff
- **Gate:** quick local checks passed
- **Human action:** only in the event of a decision, exception or escalation

### 5. Adversarial validation

- **Workflow:** [adversarial validation](workflows/05-adversarial-validation.md)
- **Human Owner:** Tech Lead; PM and UX validate your criteria
- **Agents:** Validation / QA, Security, Architecture and Reviewer Agents
- **Support:** repo harness and reproducible environments
- **Objective:** prove adherence to the specification and look for flaws that the author did not find
- **Inputs:** change, PRD, UX spec, SPEC, CHECKLIST and risk class
- **Activities:** testing, security, architecture, accessibility, regression and mutation testing when applicable
- **Outputs:** evidence linked to criteria and classified findings
- **Gate:** complete checklist and absence of blockers

### 6. Code review, PR and merge decision

- **Workflow:** [PR and merge](workflows/06-pr-and-merge.md)
- **Human Owner:** Tech Lead or Code Owner depending on risk
- **Agents:** PR Agent + Reviewer Agent
- **Objective:** evaluate quality, risk, maintainability and readiness for integration
- **Inputs:** diff, commits, validation results and evidence pack
- **Activities:** code review, testing, architectural impact, contracts and documentation
- **Outputs:** Trackable PR, approval or adjustment requests
- **Gate:** approved review, green CI, updated branch and valid approvals
- **Ceremony:** delivery review / H4 when required by policy

### 7. Approval

- **Workflow:** [approval](workflows/07-release-candidate-validation.md)
- **Human owners:** PM for value; UX for experience; stakeholder when necessary
- **Agents:** Release Agent + Product Validation Agent
- **Objective:** confirm value and behavior in the representative scenario
- **Inputs:** release candidate, acceptance criteria, environment and test data
- **Activities:** preview, smoke, E2E, accessibility, demonstration and evidence collection
- **Outputs:** acceptance, evidence and pending issues recorded
- **Gate:** validated acceptance criteria or explicit correction plan

### 8. Delivery and observation

- **Workflow:** [production and observation](workflows/08-production-release-and-observation.md)
- **Human Owner:** Tech Lead; PM co-approves exposure R3/R4
- **Agents:** Release Agent + Observability Agent
- **Objective:** release with controlled exposure and prove health in real use
- **Inputs:** approved release candidate, rollout plan, rollback, SLOs and alerts
- **Activities:** progressive deployment, feature flag when applicable, monitoring and comparison with baseline
- **Outputs:** released version, health signals, rollback/pause when necessary and changelog
- **Gate:** authorized environment, compatible migration and post-deploy window without relevant regression
- **Ceremony:** release decision / H5 according to risk

### 9. Knowledge base update

- **Workflow:** [knowledge curation](workflows/09-knowledge-curation.md)
- **Human owner:** domain owner changed
- **Agent:** Knowledge Agent
- **Cadence:** continuous + weekly automated review
- **Objective:** maintain documentation aligned with the real product
- **Inputs:** decisions, code, PR, approval, release and incidents
- **Activities:** consolidate decisions, learning and changes; look for contradictions and obsolescence
- **Outputs:** updated canonical sources and reusable knowledge
- **Gate:** current, traceable documentation without unresolved contradictions

## 10. Telemetry and continuous improvement — Auto Dream

- **Workflow:** [telemetry and continuous improvement](workflows/10-continuous-improvement.md)
- **Human owner:** trio; each demand returns to the domain owner
- **Agents:** Telemetry/Observability Agent + Auto Dream Agent + independent Critic Agent
- **Trigger:** continuous collection, weekly synthesis and extraordinary execution after relevant incident
- **Objective:** observe the work system, learn from evidence and improve the product, agents and flow
- **Scope:** product, UX, engineering, agents, prompts, process, harness, skills, scripts, tools, hooks, gates, documentation and workflow architecture
- **Ceremony:** telemetry and improvement / H6

### 10.1 Why “Telemetry and improvement”

“Auto Dream” describes a mechanism. “Telemetry and improvement” describes the operational outcome: seeing how the system behaves, distinguishing signal from noise, and converting evidence into learning or action.

Without telemetry, continuous improvement becomes opinion. Without returning to the backlog and memory, telemetry becomes a decorative dashboard.

### 10.2 Events and minimum correlation

Each relevant event must carry, where applicable:

- `work_item_id`, product and repository
- phase, agent, model, prompt/skill version and tool used
- session/run ID and timestamp
- input, output and execution status
- duration, tokens, cost and context size
- retry, fallback, blocking and scaling
- gate, result, evidence and duration
- human decision, owner and motive
- commit, PR, release and environment
- risk class and level of autonomy
- protection or anonymization of sensitive data

The recommended pattern is to instrument logs, metrics and correlational traces, with versioned taxonomy and retention policy.

### 10.3 Cycle inputs

- agent sessions and decisions
- evidence packs and human feedback
- failures, retries, blockages and escalations
- results from hooks, CI, approval and deployment
- incidents, rollbacks and escaped defects
- time, cost, quality, UX and autonomy metrics
- user feedback and product signals
- previously generated improvement demands

### 10.4 Automated pipeline

1. Collect sessions and events continuously.
2. Remove secrets and personal data before analysis.
3. Validate data completeness, correlation and quality.
4. Group events by stage, cause and type of impact.
5. Identify recurring patterns and isolated occurrences.
6. Compare results with baseline and previous periods.
7. Distinguish reusable learning from operational problems.
8. Look for duplicity, contradiction and obsolescence in memory.
9. Produce evidence and level of confidence for each conclusion.
10. Submit findings to an independent Critic Agent.
11. Consolidate confirmed items and keep inconclusive hypotheses under observation.

### 10.5 Loop A — validated learning

- identify what worked, for whom and in what context
- record evidence, origin, date and conditions of reuse
- check duplicity, contradiction and temporal validity
- propose inclusion, update or removal in `MEMORY.md`
- avoid transforming an isolated preference into a global rule
- require human approval for sensitive memory

#### Memory gate

- evidence linked to the conclusion
- explicit scope and context of application
- absence of secrets or personal data
- no unresolved contradictions
- actionable and reusable knowledge
- sensitive change reviewed by responsible person

### 10.6 Loop B — failure or opportunity for improvement

- describe symptom, impact and affected stage
- identify probable cause and evidence
- record frequency and reach
- propose corrective action and expected result
- generate traceable demand in the backlog
- relate sessions, executions and source incidents
- detect and link duplicates

Preserved and expanded types of improvements:

- product or experience
- process or ceremony
- harness
- skill or prompt
- script, tool or integration
- hook or gate
- workflow architecture
- documentation, context or memory
- observability, security or cost

#### Minimum demand structure

- problem-oriented title
- symptom and impact
- evidence and frequency
- root cause hypothesis
- proposed improvement
- measurable acceptance criteria
- suggested priority and risk class
- owner recommended
- links to related sessions and artifacts

#### Prioritization

- **P0:** critical risk, security or data loss
- **P1:** recurring failure that blocks the flow
- **P2:** rework, cost or low reliability
- **P3:** optimization and incremental improvement
- frequency does not replace impact
- Auto Dream recommends; the human owner decides and the PM orders the backlog

### 10.7 Trio Minimum Panel

#### Product and UX — PM + UX

- delivery outcome and adoption
- conversion or completion of the main task
- user errors, abandonment and time on task
- qualitative feedback and experience defects
- accessibility and UX criteria not met

#### Flow — trio

- lead time: backlog until approval
- cycle time: implementation until merge
- time per phase and time waiting for human decision
- pass rate on first pass per gate
- rework after validation or approval
- blocking, retries and escalations
- percentage of automated gates
- percentage of autonomous execution by risk class

#### Engineering — Tech Lead

- build, testing and CI failures
- post-delivery defects and regressions
- coverage of acceptance criteria
- change failure rate and recovery time
- architectural violations, security and dependencies
- false positives and time spent per gate

#### Agents and cost — trio

- tokens, cost and duration per phase, agent and delivery
- success rate without intervention
- number of attempts until completion
- failures by tool, skill, prompt and model
- quality of the evidence pack
- human time on exceptions and approvals
- currentness and use of the knowledge base

### 10.8 Cycle outputs

- `MEMORY.md` updated with validated learnings
- improvement demands created or enriched in the backlog
- short weekly report with patterns, trends and data quality
- updated work system metrics
- inconclusive hypotheses kept for future observation
- experiment with owner, baseline, deadline and success criteria

### 10.9 Completion Gate

- processed and traceable sources
- explicit data quality and gaps
- hypothesis-separated learnings
- relevant failures converted into demands
- duplicities and contradictions dealt with
- revised sensitive changes
- no confidential data improperly persisted

### 10.10 Failures of the cycle itself

- collection failure opens alert and silently prevents partial completion
- low confidence keeps the item as a hypothesis
- contradiction blocks automatic memory update
- demand without evidence remains as a draft
- agent cannot approve changes to the gates themselves
- Auto Dream incidents enter next analysis cycle

---

## 11. Evidence pack presented to people

Every human decision receives a short package:

- decision question in a sentence
- agent recommendation
- alternatives considered
- main risks and trade-offs
- changes since last approval
- evidence of the gates executed
- pending issues, exceptions and confidence level
- impact on product, experience and engineering
- links to full artifacts, code and execution

The evidence pack should allow you to decide without re-reading all the sessions, but preserving links for auditing.

---

## 12. Repo harness

### 12.1 Paper

- make the repository understandable for people and agents
- convert engineering standards into executable rules
- offer secure and repeatable paths to change
- reduce dependence on informal or individual context
- produce actionable feedback and auditable evidence

### 12.2 Skills

Native Agent Team skills, in [`skills/`](../skills/):

- `business-discovery`, `technical-discovery`, `write-feature`, `review-prd`, `create-spec`, `review-spec`, `review-cross-prd-spec`, `refine-spec` — discovery, specification and planning
- `implement`, `dev-flow`, `fix-bug`, `analyse-bug`, `test-integration-local` — implementation and validation
- `code-review`, `commit`, `update-pr`, `check-pr`, `update-docs` — review, publication and documentation
- `workspace-memory`, `workspace-projects`, `workspace-board` — trio workspace operation

Recommended extensions:

- intake and deduplication skill
- UX research and synthesis skill
- threat modeling and privacy skill
- migration, rollout and rollback skills
- incident response and post-mortem skills
- telemetry skill and agent evaluation
- documentation update and verification skill

Every skill must declare objective, inputs, outputs, allowed tools, stopping criteria, examples and tests.

### 12.3 Rules

- architecture and boundaries between modules
- conventions and object names
- accepted standards and prohibited standards
- dependency injection and composition
- gitflow and branching strategy
- validation and approval criteria
- ownership by paths and Code Owners
- risk classification and permissions per phase
- security, privacy and data usage
- SLOs, observability, rollout and rollback
- testing strategy:
  - unitary
  - architecture
  - integration / TAAC
  - contract
  - end-to-end
  - accessibility
  - mutation

### 12.4 Local hooks and gates

#### Pre-commit — quick feedback

- lint and formatting
- typecheck
- affected unit tests
- architectural tests
- consistency between code, PRD and SPEC

#### Pre-push — extended validation

- minimum coverage defined by the project
- dead code and blocking technical debt
- secret leak
- integration / TAAC in container
- impact on contracts and compatibility
- dependency review and licenses when applicable

#### CI — independent validation

- repeat critical gates in a clean environment
- perform build, testing, security and architecture
- select checks according to risk and changed paths
- generate auditable evidence
- prevent merge when there are blockers

#### Merge gate

- confirm approvals and status checks
- confirm provenance of automation
- prevent silent bypass and force push
- invalidate approval when diff changes materially

#### Ambient gate

- release secrets only after authorization
- restrict allowed branches and artifacts
- validate migration, backup and compatibility
- require approval according to risk
- integrate observability signals and change management

#### Post-deploy gate

- compare metrics with baseline
- stop rollout in case of regression
- automatically revert when safe
- open incident when human action is required

### 12.5 Rules for AI-based gates

- AI can recommend, explain and prioritize findings.
- Automatic blocking requires reproducible rule and verifiable evidence.
- Probabilistic finding requires independent confirmation.
- The same agent does not produce and approve the change itself.
- Agents do not change gates within the same evaluated flow.
- Changes in rules, hooks or CI automatically increase the risk.
- Bypass requires authorized person, reason, validity and correction plan.

### 12.6 Tools per capacity

Tools are implementation options; the flow contract should not depend on a specific brand.

#### Management, decision and collaboration

- backlog and roadmap manager: Linear, Jira, GitHub Projects or equivalent
- documents and decisions: Markdown in the repository, Obsidian, Notion or equivalent
- communication: Slack, Teams or equivalent
- decision record: versioned ADRs and decision log

#### Research, experience and design

- research and synthesis: research repository, Dovetail or equivalent
- flows and prototypes: Figma, FigJam, Penpot or equivalent
- design system: Storybook and versioned tokens
- evaluation: usability tests, axe/Lighthouse and visual regression

#### Code and understanding the codebase

- LSP, lint and formatting
- typecheck and static analysis
- Serena
-Dora
- structural search, dependency graph and architectural analysis
- reproducible development environments and containers

#### Reduction and context management

-RTK
- codebase indexes and authorized semantic retrieval
- compression of logs and evidence packs
- context budgets, tokens and cost per phase

#### Quality and safety

- testing and mutation testing frameworks suited to the stack
- SAST/code scanning, such as CodeQL or equivalent
- secret scanning
- dependency review, SBOM, vulnerabilities and licenses
- DAST and contract testing when applicable
- policy as code for deterministic rules

#### CI/CD and operation

- GitHub Actions, GitLab CI, Buildkite or equivalent
- preview environments and infrastructure as code
- feature flags and gradual rollout
- artifact registry and provenance/attestation
- progressive deployment, canary and automated rollback

#### Agent Team observability and telemetry

- OpenTelemetry to correlate logs, metrics and traces
- observability backend like Grafana stack, Datadog, New Relic or equivalent
- error tracking like Sentry or equivalent
- product analytics like PostHog, Amplitude or equivalent
- experimentation and evaluation of prompts/agents
- cost, quality, autonomy and flow dashboards

#### Portal and knowledge

- `PRD.md` — why and what will be delivered
- UX specification — journey, flow, states, content and accessibility
- `SPEC.md` — expected behavior and contracts
- `ADR.md` — architectural decisions and consequences
- `AGENTS.md` — operating instructions for agents
- `README.md` — usage, execution and repository overview
- history of PRs — changes, evidence and local decisions
- Backstage Software Catalog/TechDocs or equivalent for ownership, catalog and discovery at scale

### 12.7 Tool evaluation contract

Before adopting a tool, record:

- problem solving and owner
- stage, input and output met
- integration with canonical sources
- permissions, sent data and retention
- financial and cognitive cost
- API, automation and exportability
- evidence produced and audit capacity
- lock-in and exit plan
- success metric and review date

### 12.8 Official references for proposed extensions

- [GitHub Actions — workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows)
- [GitHub CodeQL — code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning)
- [GitHub — supply chain security](https://docs.github.com/en/code-security/concepts/supply-chain-security/supply-chain-security)
- [OpenTelemetry — metrics and correlation between signals](https://opentelemetry.io/docs/specs/otel/metrics/)
- [Backstage — Software Catalog](https://backstage.io/docs/features/software-catalog/)
- [Backstage — TechDocs](https://backstage.io/docs/features/techdocs/)

These references support the suggested capabilities; do not constitute an adoption decision. The choice must go through the evaluation contract above.

---

## 13. Governance and security

- minimum permissions per agent and per stage
- human approval for irreversible or external actions
- secrets outside of prompts, logs and artifacts
- personal data minimized, protected and retained by policy
- traceability between demand, decision, code and evidence
- record of authorship, tools, models and versions used
- clear criteria for interrupting, escalating or asking for a decision
- documented exceptions with deadline and person responsible
- segregation between production, validation and approval
- kill switch and credential revocation
- periodic audit of agent and integration permissions

### Escalation contract

Escalate when there is:

- contradictory or ownerless requirement
- confidence below the defined threshold
- two or more correction attempts without progress
- change outside the approved scope
- need for new permission or external access
- non-reproducible failure or inconsistent evidence
- irreversible decision or non-calculable impact
- divergence between agents without objective tiebreaker criteria

---

## 14. Risk classification and autonomy

### R0 — minimum

- documentation, text and formatting
- no change in behavior, data, secrets or contracts
- automatic merge after gates; human review by sampling

### R1 — low

- internal refactoring or localized change
- behavior covered by existing tests
- no migration, security or critical integration
- short approval and automatic deployment with observation

### R2 — medium

- new behavior or change in internal/integration contract
- reversible but relevant impact
- product or Code Owner approval; canary and rollback

### R3 — high

- persisted data, migrations, public procurement, authentication, privacy, payments or critical operation
- human product and technical approvals
- explicit approval before production

### R4 — critical

- regulatory, financial, destructive or far-reaching impact
- manually reviewed change plan and rollback
- double approval, segregation of functions and human monitoring

### Rules

- one agent proposes the risk and another tries to increase it
- the greatest justified risk prevails
- manual reduction requires recorded justification
- scope change recalculates risk
- sensitive paths automatically increase risk
- unresolved doubt prevents R0/R1

### Progressive autonomy

- **A0 — watched:** people approve all transitions
- **A1 — autonomous execution:** agents execute; people approve decisions and merge
- **A2 — merge by risk:** R0/R1 can merge by policy
- **A3 — controlled autonomous delivery:** low risk reaches production with proven rollback
- **A4 — exception-oriented:** healthy flow occurs without intervention; people treat decisions and anomalies

Increase autonomy only with sufficient history, low failure rate, reliable gates, few false positives, tested rollback and intact telemetry.

---

## 15. Model evolution

### Phase 1 — pilot assisted

- select a low-risk repository and stream
- define minimum roles, artifacts and gates
- maintain human approval on all transitions
- measure time, rework, cost and failures

### Phase 2 — standardization

- create reusable templates
- consolidate rules, skills, hooks and PR template
- define common entry and exit criteria
- document exceptions by repository type
- institute the trio ceremonies

### Phase 3 — automation

- automate routing between agents
- execute gates according to risk and type of change
- update statuses, artifacts and evidence automatically
- instrument end-to-end telemetry
- escalate to people only decisions and exceptions

### Phase 4 — scale and continuous improvement

- expand to other teams and repositories
- compare performance between flows without creating simplistic ranking
- evolve skills based on recurring failures
- review rules, metrics and knowledge weekly
- increase autonomy through evidence

---

## 16. Initial model metrics

- lead time: backlog until approval
- cycle time: implementation until merge
- approval rate in the first review and per gate
- rework after validation or approval
- defects and regressions after delivery
- coverage of acceptance criteria
- percentage of automated gates
- human time spent on exceptions and approvals
- cost per stage, agent, model and delivery
- currentness and use of the knowledge base
- outcome and adoption by delivery
- failures, retries and escalations per phase
- quality and completeness of the evidence pack
- false positives per gate
- percentage of self-employment by risk class

Metrics should guide investigation. None of them, in isolation, represents the productivity or quality of the trio.

---

## 17. Decisions still open

- tool that will orchestrate the Agent Team
- limits of autonomy of each role
- canonical format and life cycle of artifacts
- risk criteria by type of change
- mandatory gates per language and repository
- responsible for approving exceptions outside the trio
- environment strategy for integration and approval
- how to measure cost, quality and productivity gains
- how to version and distribute shared rules and skills
- where the canonical source of the stream telemetry will be located
- which tool will be the recording system for backlog and decisions
- retention policy for agent sessions and data
- which ceremonies can be eliminated after proven maturity

---

## 18. Next steps for the three-person pilot

1. Choose the repository and a real R1 case.
2. Appoint PM, UX and Tech Lead and register their decision rights.
3. Map the current flow and main bottlenecks.
4. Define the minimum set of agents and permissions.
5. Create minimal templates for `PB`, `PRD`, UX spec, `SPEC` and evidence pack.
6. Implement essential gates in the repo harness.
7. Instrument gate IDs, events, cost, duration and results.
8. Run a complete cycle from end to end.
9. Perform H6 with cycle data and create a maximum of three priority improvements.
10. Repeat for three cycles before increasing autonomy or adding ceremonies.

## Expected result

The trio maintains clear authority over product, experience, and technology, while agents absorb most of the operational research, production, critique, execution, validation, and documentation. The system does not depend on heroism or oral context: each passage has a contract, each decision has an owner, each delivery has evidence and each cycle leaves the next one safer, faster and more autonomous.
