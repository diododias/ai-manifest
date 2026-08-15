---
title: Agent Team — 90/10 operating model
status: proposed
updated_at: 2026-08-08
---

# Agent Team — 90/10 operating model

> Practical breakdown of [Agent Team — human trio operating system](../rules/operating-model.md) · [Full visual flow](end-to-end-journey.md) · [Flows per phase](journey-by-phase.md) · [multi-agent workflows](../workflows/README.md).

The subsections of the operational flow indicate what must be done; [workflows](../workflows/README.md) describe how agents collaborate, handoff, criticize and consolidate each output.

## Purpose of the model

- Automate approximately 90% of operational work
- Reserve human time for value, risk and responsibility decisions
- Make agents produce, criticize, correct and prove the work
- Replace extensive reviews with short, evidence-oriented checkpoints
- Allow more autonomy as the flow demonstrates security

## What does 90% automated mean

- 90% of activities carried out without manual intervention
- Does not mean 90% of decisions are delegated to agents
- Does not eliminate human responsibility for product and production
- Does not authorize agents to bypass gates or expand their own access
- It should not be measured only by number of tasks
- Must reduce human time without increasing failures, risk or rework

## Division of responsibility

- **Agents do:** research, synthesis, specification, code, tests and evidence
- **Automations do:** deterministic validations, blocking and traceability
- **Humans make:** priority, irreversible choices, exceptions and acceptance
- **System does:** routing, recording, observation and scheduling

---

## Central principle: decision review

- The human does not review the entire process
- The human answers an objective question at each checkpoint
- The system presents recommended decisions, alternatives, risks and evidence
- The review has an expected time and explicit criteria
- Lack of response does not equate to approval
- Material change invalidates the related approval

## Evidence pack presented to the human

- Decision requested in one sentence
- Recommendation of agents
- Alternatives considered
- Main risks and trade-offs
- Changes since the last checkpoint
- Evidence of executed gates
- Pending issues, exceptions and confidence level
- Links to complete artifacts, code and execution

---

## Risk classification

### R0 — minimum

- Documentation, text and formatting
- No change in behavior
- No data, secrets or contracts
- Automatic merge after gates
- Human review by sampling

### R1 — low

- Internal refactoring or localized change
- Behavior covered by existing tests
- No migration, security or critical integration
- A short human approval on PR
- Automatic deployment with observation

### R2 — medium

- New product behavior
- Change of internal contract or integration
- Reversible but relevant impact
- Product or Code Owner approval
- Automated canary and rollback

### R3 — high

- Persisted data, migrations or public contracts
- Authentication, authorization, secrets or privacy
- Payments, availability or critical operation
- Human product and technical approvals
- Explicit approval before production

### R4 — critical

- Regulatory, financial or destructive impact
- Irreversible or far-reaching action
- Manually reviewed change plan and rollback
- Double approval and segregation of duties
- Human monitoring during release

## Classification rules

- One agent proposes the risk and another agent tries to increase it
- The greatest justified risk prevails
- Manual risk reduction requires recorded justification
- Scope change recalculates risk
- Sensitive paths automatically elevate risk
- Unresolved questions prevent classification as R0 or R1

---

## End-to-end operational flow

### 0. Entry and screening

- **Agents:** Intake Agent + Product Manager Agent
- **Automations:**
  - validate mandatory fields
  - identify duplication and dependencies
  - relate demand, product and repository
  - classify type and initial risk
- **Output:** Work Item with context, proposed priority and owner
- **Automatic gate:** complete item, traceable and without known duplication
- **Human action:** prioritize or reject the item
- **Expected human time:** 2–5 minutes

### 1. Multi-agent Discovery

- **Agent Team:**
  - Product Manager Agent
  - UX Specification Agent
  - Tech Lead Discovery Agent
- **Execution:**
  - agents investigate in parallel
  - each agent records hypotheses and evidence
  - Product Manager Agent consolidates `PB.md`
  - the other agents criticize the synthesis
- **Automations:**
  - validate `PB.md` structure
  - check links and sources
  - detect claims without evidence
  - identify questions and risks without owner
  - compare discovery with similar demands
- **Automatic gate:** problem, user, experience and feasibility covered

#### H1 human checkpoint — is it worth moving forward?

- **Responsible:** Product Manager / sponsor
- **Question:** does this problem deserve investment now?
- **Review:** problem, user, value, restrictions and risks
- **Decision:** move forward, adjust, postpone or close
- **Expected human time:** 5–10 minutes

### 2. Product planning

- **Agent Team:**
  - Product Manager Agent
  - Adversarial Product Manager Agent
- **Execution:**
  - Product Manager proposes `PRD.md`
  - adversarial agent looks for ambiguities and gaps
  - Product Manager responds and reviews the document
  - unresolved gaps are scaled
- **Automations:**
  - validate template and mandatory fields
  - detect vague or unmeasurable terms
  - require observable acceptance criteria
  - check traceability `PB → PRD`
  - check scope, out of scope and metrics
- **Automatic gate:** Complete PRD and adversarial criticism answered

#### Human Checkpoint H2 — is this what we will build?

- **Responsible:** Product Manager / stakeholder
- **Question:** Are scope, experience and success criteria correct?
- **Review:** decisions and gaps; not the document line by line
- **Decision:** approve, reduce, expand or return
- **Expected human time:** 10–15 minutes

### 3. Technical specification

- **Agent Team:**
  - Specification Tech Lead Agent
  - Adversarial Tech Lead Agent
- **Execution:**
  - specifier proposes architecture and decomposition
  - adversarial agent evaluates gaps, risks and trade-offs
  - decisions are consolidated in `ADR.md` and `SPEC.md`
  - work is divided into verifiable tasks
- **Automations:**
  - validate artifact structure
  - check traceability `PRD → SPEC → TASKS`
  - detect cycles and known architectural violations
  - identify sensitive contracts and paths
  - validate dependencies and order of tasks
  - generate threat model when applicable
- **Automatic gate:** consistent specification and critical gaps addressed

#### Human checkpoint H3 — exceptional technical decision

- **Required:** R3, R4, new ADR or architectural exception
- **Optional:** R0, R1 and R2 without new structural decision
- **Responsible:** Tech Lead / architect / domain expert
- **Question:** do we accept these trade-offs and residual risks?
- **Review:** decision, discarded alternatives and future impact
- **Expected human time:** 10–20 minutes

### 4. Standalone implementation

- **Agents:** Orchestrator Agent + Software Engineer Agents
- **Execution:**
  - select next eligible task
  - create isolated branch or worktree
  - implement minimal change
  - create or update tests
  - perform local validations
  - fix crashes automatically
  - log small, traceable commits
  - update affected documentation
- **Pre-commit gate:**
  - formatting, lint and typecheck
  - unit tests affected
  - fast architecture tests
  - secrets and prohibited files
  - basic consistency of artifacts
- **Pre-push gate:**
  - reproducible build
  - expanded test suite
  - minimum coverage and mutation delta
  - static analysis and dependencies
  - dead code and broken contracts
- **Automatic correction:** up to a limit of attempts and time
- **Escalation:** repeated failure, requirement conflict or high risk
- **Human action:** none during healthy flow

### 5. Adversarial validation

- **Agent Team:**
  - QA / Validation Agent
  - Security Review Agent
  - Architecture Review Agent
  - Adversarial Code Reviewer Agent
- **Execution:**
  - validate each acceptance criteria
  - test happy paths, errors and edge cases
  - compare implementation with `PRD` and `SPEC`
  - look for regressions, vulnerabilities and breaches
  - produce reproducible evidence
- **CI fast lane:**
  - lint, typecheck, unit tests and architecture
  - executed on every push
- **CI deep lane:**
  - integration, TAAC, mutation and security
  - executed according to risk, paths and impact
- **Automatic gate:** all mandatory checks approved
- **Human action:** only for false positive, exception or requirement gap

### 6. PR and merge decision

- **Agents:** PR Agent + Reviewer Agents
- **Automations:**
  - generate description and evidence pack
  - summarize changed behavior
  - highlight files and snippets of highest risk
  - request Code Owners according to paths
  - require status checks from the authorized source
  - invalidate approval after material change
- **Agents review:**
  - correctness and completeness
  - security and privacy
  - architecture and contracts
  - testing and maintainability
  - documentation and observability

#### H4 human checkpoint — can we integrate?

- **R0:** automatic merge; human sampling review
- **R1:** a quick review from the owner
- **R2:** an approval from the affected person responsible
- **R3:** technical approval + owner approval
- **R4:** double approval with segregation of duties
- **Human review:** evidence pack, hotspots and exceptions
- **Expected human time:** 5–15 minutes
- **Merge gate:** approvals required + green CI + updated branch

### 7. Automated approval

- **Agents:** Release Agent + Product Validation Agent
- **Environment:** preview or isolated staging
- **Automations:**
  - deploy the immutable artifact
  - secure data seed
  - smoke, E2E and synthetic tests
  - visual comparison when applicable
  - automatic validation of acceptance criteria
  - generation of demonstration and evidence
- **Human action:** review only new experience or R2+ change
- **Output:** release candidate approved or returned

### 8. Production release

- **Agents:** Release Agent + Observability Agent
- **Strategies:** feature flag, canary, blue/green or progressive rollout
- **Automatic gates:**
  - signed and traceable artifact
  - authorized environment and secrets
  - validated and compatible migration
  - verified backup and rollback
  - Configured SLOs and alerts

#### Human checkpoint H5 — can we expose the risk?

- **R0/R1:** automatic deploy
- **R2:** optional approval depending on the criticality of the product
- **R3/R4:** explicit approval before production environment
- **Responsible:** Product Owner + technical responsible when necessary
- **Review:** impact, rollout plan, rollback and health signs
- **Expected human time:** 3–10 minutes

### 9. Observation and learning

- **Agents:** Observability Agent + Knowledge Agent
- **Automations:**
  - monitor errors, latency, SLOs and product metrics
  - compare baseline and behavior after deploy
  - pause rollout or revert automatically
  - update changelog and documentation
  - record failures and new items in the backlog
- **Post-deploy gate:** observation window without relevant regression
- **Human action:** decision only when rollback is not safe or automatic

### 10. Continuous improvement — Auto Dream

- **Agent:** Auto Dream Agent
- **Trigger:** weekly schedule + extraordinary execution after relevant incident
- **Objective:** transform operational history into memory and concrete improvements
- **Scope:** product, agents, prompts, process, harness, skills, scripts, gates and flow

#### Cycle inputs

- Agent sessions and decisions
- Evidence packs and human feedback
- Failures, retries, blockages and escalations
- Results of hooks, CI, approval and deployment
- Incidents, rollbacks and escaped defects
- Metrics of time, cost, quality and autonomy
- Previously generated improvement demands

#### Automated pipeline

- Collect sessions and events for the week
- Remove secrets and personal data before analysis
- Group events by stage, cause and type of impact
- Identify recurring patterns and isolated occurrences
- Compare results with previous weeks
- Distinguish reusable learning from operational problems
- Look for contradictions with existing memory
- Produce evidence and confidence level for each conclusion
- Submit findings to an independent Critic Agent
- Consolidate only items that are confirmed or explicitly flagged as hypotheses

#### Path A — validated learning

- Identify what worked and in what context
- Record evidence and conditions of reuse
- Check duplicity, contradiction and temporal validity
- Propose inclusion, update or removal in `MEMORY.md`
- Preserve the origin and date of learning
- Do not transform an isolated preference into a global rule

#### Memory gate

- Evidence linked to conclusion
- Explicit scope and context of application
- Absence of secrets or personal data
- No unresolved contradiction
- Actionable and reusable knowledge
- Sensitive change requires human approval

#### Path B — failure or opportunity for improvement

- Describe the observed symptom
- Identify probable cause and evidence
- Record frequency, impact and affected stage
- Propose corrective action and expected results
- Classify the type of improvement:
  - process
  - harness
  - skill or prompt
  - script or tool
  - hook or gate
  - workflow architecture
  - documentation or context
- Generate traceable demand in the backlog
- Relate sessions, executions and source incidents
- Detect and link duplicate demands

#### Minimum demand structure

- Problem-oriented title
- Symptom and impact
- Evidence and frequency
- Root cause hypothesis
- Proposed improvement
- Measurable acceptance criteria
- Suggested priority and risk class
- Recommended owner
- Links to related sessions and artifacts

#### Suggested prioritization

- **P0:** critical risk, security or data loss
- **P1:** recurring failure that blocks the flow
- **P2:** rework, cost or low reliability
- **P3:** optimization and incremental improvement
- Frequency does not replace impact in defining priority
- Auto Dream recommends; the human responsible controls the final priority

#### Human checkpoint H6 — did the system learn correctly?

- **Mandatory:** sensitive changes to `MEMORY.md`, P0/P1 and gate changes
- **By sampling:** low-risk learning and P2/P3 demands
- **Responsible:** owner of the Agent Team / Engineering Enablement
- **Question:** Are evidence, learning and proposed action reliable?
- **Decision:** approve, adjust, discard or request more evidence
- **Expected human time:** 10–20 minutes per weekly cycle

#### Cycle outputs

- `MEMORY.md` updated with validated learnings
- Improvement demands created or enriched in the backlog
- Short weekly report with patterns and trends
- Updated work system metrics
- Inconclusive hypotheses kept for future observation

#### Completion gate

- All sources processed and traceable
- Learning separated from hypotheses
- Relevant failures converted into demands
- Duplicities and contradictions dealt with
- Sensitive changes reviewed
- No confidential data improperly persisted

#### Failures of Auto Dream itself

- Collection failure opens alert, does not produce silent partial completion
- Low confidence keeps item as hypothesis
- Contradiction blocks automatic memory update
- Demand without evidence remains as a draft
- The agent cannot approve changes to the gates themselves
- Auto Dream incidents enter the next analysis cycle

---

## Summary of human checkpoints

| Checkpoint | Human decision | When | Expected time |
|---|---|---|---:|
| H1 | Is it worth investing? | After discovery | 5–10 min |
| H2 | Is this what we will build? | After PRD | 10–15 min |
| H3 | Do we accept the trade-off? | Only risk or structural decision | 10–20 min |
| H4 | Can we integrate? | Before the merge, according to risk | 5–15 min |
| H5 | Can we expose the risk? | Production R3/R4 | 3–10 min |
| H6 | Did the system learn correctly? | Auto Dream weekly cycle | 10–20 min |

## How to reduce reviews even further

- Combine H2 and H3 for small, well-known changes
- Eliminate H3 when there is no ADR, exception or relevant risk
- Apply H4 by sampling in R0 after reliable history
- Make H5 automatic in R0/R1 with proven rollback
- Show only differences since the last approval
- Direct the human to the hotspots, not the full diff
- Use Code Owners only for really sensitive paths
- Create different policies by risk and type of repository
- Measure false positives and remove worthless gates

---

## Gate architecture

### Local gate — seconds or a few minutes

- Immediate feedback to the agent
- Deterministic and low-cost checks
- Must offer clear correction instructions
- Failure blocks commit or push

### CI Gate — minutes

- Executed in a clean environment
- Confirms build, testing, security and architecture
- Selects checks according to risk and changed paths
- Failure blocks merge

### Merge gate — consolidated decision

- Confirms approvals and status checks
- Confirms the origin of the automation
- Prevents silent bypass and force push
- Invalidates approval when diff changes materially

### Ambient gate — controlled exposure

- Release secrets only after authorization
- Restricts allowed branches and artifacts
- Requires approval when risk determines
- Integrates observability signals and change management

### Post-deploy gate — actual behavior

- Compare metrics with the baseline
- Stops rollout in case of regression
- Automatically reverts when safe
- Open incident when human action is necessary

## Rules for AI-based gates

- AI can recommend, explain and prioritize findings
- Automatic blocking requires reproducible rule and verifiable evidence
- Probabilistic findings must undergo independent confirmation
- The same agent should not produce and approve the change itself
- Agents cannot change gates within the same evaluated flow
- Changes in rules, hooks or CI automatically increase risk
- Bypass requires authorized person, reason and correction deadline

---

## Escalation contract

- Contradictory or ownerless requirement
- Confidence below the defined limit
- Two or more correction attempts without progress
- Change outside the approved scope
- Need for new permission or external access
- Non-reproducible failure or inconsistent evidence
- Irreversible decision or non-calculable impact
- Divergence between agents without objective tiebreaker criteria

## Progressive autonomy

### Level A0 — assisted

- Humans approve all transitions
- Recommended for starting the pilot

### Level A1 — autonomous execution

- Agents perform implementation and validation
- Humans maintain H1, H2, H4 and H5

### Level A2 — merge due to risk

- R0 can do self-merge
- R1 receives short human review
- R2+ maintains specific owners

### Level A3 — controlled autonomous delivery

- R0/R1 deploy automatically
- Rollback and observability are mandatory
- Humans act in exceptions and high risks

### Level A4 — exception-oriented operation

- Healthy flow occurs without intervention
- Humans receive only relevant decisions and incidents
- Sampling audits verify the quality of the system

## Criterion to increase autonomy

- Minimum volume of deliveries observed
- Low rate of escaped defects
- Tested and reliable rollback
- Gates with few false positives
- Risk classified correctly
- Complete and auditable evidence
- Really reduced human time

---

## 90/10 model metrics

- Percentage of steps completed without intervention
- Human minutes per delivery
- Time waiting for human approval
- Rate of decisions returned due to lack of context
- Approval on the first pass of each gate
- Rework after H2, H3 and H4
- Defects escaped to production
- Automatic and manual rollbacks
- False positives per gate
- Cost of agents per delivery
- Lead time and cycle time
- Percentage of changes by risk class
- Traceability coverage between artifacts

## Suggested initial goal

- 80–90% of activities performed by agents
- Up to 30–45 human minutes per R1/R2 delivery
- No human approval based solely on trust in the agent
- 100% of merges protected by verifiable gates
- 100% of R3/R4 changes with defined owner and rollback
- Evolve to self-merge only after evidence from the pilot

---

## Model implementation

### Step 1 — minimum contract

- Define risk classes
- Define human responsible
- Create artifact templates
- Create evidence pack format
- Define escalation conditions

### Step 2 — minimum harness

- Configure `AGENTS.md`, rules and skills
- Implement pre-commit and pre-push
- Create fast lane and deep lane CI
- Protect branch and status checks
- Configure `CODEOWNERS` for sensitive paths

### Stage 3 — pilot controlled

- Choose a real R1 flow
- Initially operate in A0/A1 autonomy
- Measure human time and failures
- Adjust gates and templates
- Validate rollback and traceability

### Step 4 — routing automation

- Automatically classify risk
- Activate Agent Teams by stage
- Automatically produce evidence packs
- Request only the necessary reviewers
- Escalate exceptions with full context

### Stage 5 — progressive autonomy

- Release auto-merge to R0
- Release automatic deployment to R0/R1
- Expand by evidence, not by expectation
- Maintain human audit by sampling

---

## Operational references

- [GitHub Rulesets and rules available](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [NIST Secure Software Development Framework](https://www.nist.gov/publications/secure-software-development-framework-ssdf-version-11-recommendations-mitigating-risk)

## Next recommended breakdown

- Define the Work Item schema
- Create the evidence pack template
- Draw the matrix `risk × gates × approvals`
- Specify each agent's prompts and contracts
- Define the events that move the workflow
- Create the first reference repo harness
- Simulate an end-to-end R1 delivery
