# 2. Agents

---

## Overview — How Agents Work

An agent is a process that receives a delimited mission, reads a versioned context, performs authorized work with declared tools, submits the result to objective checks and returns a standardized envelope to the human owner. None of these five steps are optional, and it is the combination of them—not the model's capabilities—that determines whether the agent is trustworthy.

The starting point is a simple observation: **a name on a diagram is not a role**. "Security Review Agent" is just a label until you define what it reads, what it delivers, which gate it needs to satisfy and in what condition it stops and scales. The agent catalog exists to convert labels into unambiguous operational roles so that a mission can be dispatched without prior negotiation about responsibility, scope, or completion criteria.

### Anatomy of an agent — what it consumes

An agent does not carry its own knowledge about the repository. Everything it knows comes from versioned layers that [repo harness](REPO_HARNESS.md) makes available. Each layer answers a distinct question, and the absence of any one of them produces a specific class of failure.

| Input | Reply | Where do you live | If missing |
|---|---|---|---|
| **Rules** | what is the desired state and why | [`docs/rules/`](RULES.md), `AGENTS.md` | the agent chooses a plausible convention and diverges from the repository |
| **Skills** | how to perform a recurring task the right way | [`skills/<skill>/SKILL.md`](SKILLS.md) | the procedure is reinvented with each execution, with unstable results |
| **Tools** | what you can invoke and with what limits | [`.agent/settings.json`](TOOLS.md) | any action appears authorized |
| **MCPs** | how to reach external systems and under what scope | [`.agent/mcps.json`](MCPS.md) | external effects occur before the local gate detects |
| **Sensors** | what needs to go through before the code leaves the machine | [`.hooks/`](SENSORS.md) | the cheap error only appears on the CI, an entire lap later |
| **Gates** | what needs to be true to advance to the next stage | [CI, merge, environment, post-deploy](GATES.md) | the judgment of "ready" rests with whoever produced it |
| **Evidence** | how to prove later that it was correct | [`docs/evidence/<work-item>/`](DOCUMENTATION.md) | approval is based on agent summary, not facts |
| **Memory** | what has already been decided in previous sessions | `workspace-memory`, `MEMORY.md` | context is reconstructed by guesswork each session |

It is worth clarifying the most confusing distinction in the group. **Rule describes desired state; skill describes procedure.** "Domain modules do not matter from infrastructure" is rule. "To add an adapter, create the interface in X and the implementation in Y" is a skill. Treating one like the other produces long rules that no one reads and vague skills that you can't execute.

### The mission execution cycle

Every execution — of any role, at any stage — follows the same sequence.

**1. Mission Identity.** The agent receives a full identity block. The absence of any field is, in practice, a blank authorization, and therefore an incomplete mission should not be executed.

| Block | Fields |
|---|---|
| Identification | `mission_id`, `work_item_id` (if applicable), workflow phase, agent role |
| Authority | human sponsor (PM, UX or Tech Lead), decision owner |
| Direction | objective and expected result, scope and out of scope |
| Sources | canonical sources, input and output artifacts |
| Verification | acceptance criteria and gates |
| Limits | risk and authorized autonomy, tools, permissions and budget |
| Stop | stop condition and escalation |

**2. Context reading.** The agent reads `AGENTS.md`, the rules applicable to the task, the relevant ADRs, and the workspace memory. Reading is on demand: rules are not loaded in their entirety with each execution, because context is the scarcest resource in a session.

**3. Skills check.** Before acting, the agent inventories the available skills and uses all that apply. A skill that adheres to the mission cannot be ignored, and the skill used — or the reason for not applying it — is recorded in the output envelope. This is what makes it auditable whether the correct procedure was followed.

**4. Authorized execution.** The agent acts within the declared scope, preferring local and reversible checks. Does not expand access, scope or impact on its own, and does not take external or irreversible action without explicit authorization.

**5. Gates.** Local sensors and IC gates evaluate the result by objective criteria. The agent does not declare success: it runs the check and records what it returned.

**6. Output envelope.** The mission ends in a standardized format, which allows the orchestrator and human owner to understand the outcome without re-reading the entire execution.

```yaml
mission_id: "..."
agent_role: "..."
status: completed | partial | blocked
confidence: high | medium | low
sources_used: []
skills_used: []
outputs_created: []
decisions_requested: []
assumptions: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

Two fields deserve special attention. The `confidence` field forces the agent to declare how safe it is — and confidence below the mission threshold is itself an escalation condition. The `skills_used` field converts the procedural discipline into something verifiable by third parties.

### Universal rules

Four sets of rules apply to any agent, always. They resolve in advance the behaviors that most compromise trust.

**About the truth.** Separate fact, evidence, inference, hypothesis and recommendation. Do not invent requirements, decisions, participants or results. Cite the origin of relevant statements and preserve uncertainty and unresolved contradictions. When a source is missing, produce partial output identified as such rather than filling the gap with guesswork.

**Over the limit.** Do not expand scope, access or impact on your own. Do not perform external or irreversible action without explicit authorization. Update only the authorized canonical source. Never approve alone the artifact you produced.

**About the skills.** Check the available ones before acting and use each one that applies. The three base skills are mandatory in workspace operation: [`workspace-memory`](../skills/workspace-memory/SKILL.md) for resuming and safe memory writing, [`workspace-projects`](../skills/workspace-projects/SKILL.md) for locating the canonical source of `projects/`, and [`workspace-board`](../skills/workspace-board/SKILL.md) for assuming or reconciling Work Items.

**About delivery.** Always deliver the evidence pack and summary of changes, not just the raw artifact.

### Orchestration and teams per phase

Each phase of the workflow activates a **temporary team of agents, dissolved at the end**. This allows you to keep dozens of specializations available without any of them remaining idle: you don't pay for a Security Review Agent standing still — it only exists when the validation of a sensitive change requires it.

Within each team, the dynamics repeat themselves. A **primary agent** leads and consolidates the phase artifact. One or more agents **collaborate or challenge** based on explicit responsibility. **Adversarial** agents look for ambiguity, gaps, risks and fragile assumptions — always as instances independent of those who produced them.

| Phase | Primary agent | Critical agents or specialists | Handoff |
|---|---|---|---|
| Intake | Intake Agent | Meeting Context when there is a meeting | PM prioritizes |
| Discovery | Product Manager Agent | UX Specification + Tech Lead Discovery | `PB.md` for H1 |
| Product and UX | Product Manager + UX Specification | Adversarial Product Manager | PRD + UX spec for H2 |
| Specification | Specification Tech Lead | Adversarial TL + experts | PLAN/SPEC/TASKS for H3 |
| Implementation | Orchestrator + Software Engineer | — | local diff and gates |
| Validation | QA/Validation | Security + Architecture + Code Reviewer | evidence pack |
| Integration | PR Agent | Reviewer Agents | H4 / ​​merge |
| Approval | Product Validation | ReleaseAgent | release candidate |
| Production | ReleaseAgent | ObservabilityAgent | H5 / health report |
| Knowledge | Knowledge Agent | Critic when sensitive | canonical sources |
| Improvement | Telemetry + Auto Dream | Critical Agent | H6, memory or backlog |

Note the deliberate pattern: at almost every stage, those who consolidate are not those who criticize. This is not redundancy — it is the rule that **who proposes does not approve**, applied at the team level. An agent reviewing his own work would tend to confirm his own assumptions; structural independence, not the good faith of the model, is what makes the criticism worthwhile.

The Orchestrator Agent distributes minimal context and controls dependencies in the phases with parallelism, but there is a limit that is worth remembering: it **does not replace** the consolidation of the primary agent nor the decision of the human owner. The orchestrator organizes traffic; does not decide destiny.

Finally, the catalog describes **logical roles, not instances**. An execution can use one instance per role, multiple parallel instances of the same role, or one instance assuming more than one compatible role. The restriction that can never be broken: production and approval roles do not combine in the same instance when there is a risk of self-evaluation.

### Autonomy and scaling

The level of autonomy granted to an agent is not a configuration choice — it is a consequence of what the repository can verify. The central rule is that **the harness level is the ceiling of autonomy, never its consequence**. A repository in HL1 operating with A2 autonomy is not an advanced repository; it's a repository with a missing gate that no one has noticed yet. The levels are detailed in [Gates](GATES.md).

Within the authorized ceiling, the agent acts with initiative. Out of it, stop. The universal scheduling conditions are:

- Contradictory requirement or without defined owner
- Canonical source missing, inconsistent or claimed by two owners
- Confidence below the stated limit for the mission
- Two or more correction attempts without progress
- Change outside the approved scope
- Need for new permission or external access
- Risk greater than authorized for the mission
- Irreversible decision or non-calculable impact
- Divergence between agents without objective tiebreaker criteria

These conditions are not failures: they are the system working as designed. The logic behind them all is the same — **when the cost of making mistakes alone outweighs the cost of asking, the agent asks**.

### Permissions by category

The principle is least privilege: an agent receives only the access that its mission requires, and external writing is always an authorized exception.

| Category | Reading | Local writing | PR / backlog | Deploy / external |
|---|---|---|---|---|
| Intake and Meeting Context | authorized sources | proposal artifacts | only if the mission authorizes | no |
| Product, UX and Discovery | product, research and code | phase artifacts | comment or proposal | no |
| Specification | code and docs | technical artifacts | comment or proposal | no |
| Software Engineer | repository scope | code, tests and docs | authorized branch or PR | not by default |
| Reviewers | code and evidence | report and comments | authorized review | no |
| PR Agent | Git and checks | description and evidence pack | Authorized PR | merge just for politics |
| Release | artifact and environments | release registration | status | explicitly authorized environment |
| Observability | telemetry | alerts and reports | authorized incident | pause or rollback by policy |
| Knowledge and improvement | docs, memory and metrics | proposal or authorized source | authorized backlog | no |

### From logical role to executable agent

Each paper in this catalog is materialized in [`agents/<agent-id>/`](../agents/README.md) by a single prompt, independent of runtime:

```text
<agent-id>/
└── AGENT.md # mission, limits, presence and stable directives of the sponsor
```

`AGENT.md` is the paper's only source of executable instructions and includes universal rules, output, and persistence. Sources, local rules and skills are consulted only when they are specific to the mission; There is no consolidated prompt generated or runtime synchronization artifact.

---

## Available agents

The 23 roles are documented individually in **[`agentes/`](agentes/README.md)** — one file per agent, with the full operating agreement, explicit role limits, personality, and operating notes.

The official index, grouped by role in the journey, lives in this same directory: **[agents' contract index](agentes/README.md)**. He is the canonical source for the list; This page describes the common operation for all.

| Group | Papers | Typical Sponsor |
|---|---|---|
| [Input and coordination](agentes/README.md#entry-and-coordination) | Intake, Meeting Context, Orchestrator | PM and phase owner |
| [Product, UX and discovery](agentes/README.md#produto-ux-e-discovery) | Product Manager, UX Specification, Tech Lead Discovery, Adversarial PM | PM and UX |
| [Technical specification](agentes/README.md#technical-specification) | Specification TL, Adversarial TL, Security/Data/Platform | Tech Lead |
| [Construction and validation](agentes/README.md#construction-and-validation) | Software Engineer, QA, Security Review, Architecture Review, Adversarial Code Reviewer | Tech Lead |
| [Integration, approval and operation](agentes/README.md#integration-approval-and-operation) | PR, Product Validation, Release, Observability | Tech Lead, PM and UX |
| [Knowledge and improvement](agentes/README.md#conhecimento-e-melhoria) | Knowledge, Telemetry, Auto Dream, Critic | domain owner and trio |

---

## Versioning and evaluation

Each agent definition records contract version and date, prompt version, model, effort and tools, human responsible, test cases and golden outputs, quality metrics, cost and duration, known failures and prohibited contexts, in addition to a changelog with rollback plan.

Metrics per agent cover unscaled completion rate, first gate pass, accuracy of facts and traceability, confirmed findings and false positives, rework caused in the next handoff, tokens, cost and time, mandatory output coverage, and scope or permission violations.

**These metrics do not form individual rankings.** They serve to improve contracts, context, tools, models and gates — using them as a performance assessment corrupts the signal they produce.

---

## Checklist for adding a new agent

- [ ] Does the problem require a new role or does it fit an existing agent?
- [ ] Are sponsor and decision rights clear?
- [ ] Are canonical inputs and sources defined?
- [ ] Does the output have a verifiable schema?
- [ ] Do permissions follow least privilege?
- [ ] Is there a stopping and escalation condition?
- [ ] Are production and criticism segregated?
- [ ] Are there tests with nominal, ambiguous, incomplete and sensitive cases?
- [ ] Will telemetry and cost be recorded?
- [ ] Have the catalog, orchestrator and handoffs been updated?

---

*Previous: [Repository Harness](REPO_HARNESS.md) · Next: [individual agent contracts](agentes/README.md).*
