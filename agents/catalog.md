---
title: Agent Team — agent catalog and contracts
status: proposed
updated_at: 2026-08-08
---

# Agent Team — agent catalog and contracts

> The 23 agent roles in the Agent Team, each with a mission, human sponsor, entry and exit contract, permissions, gate and stop condition.

## In 2 minutes

Agent names in a workflow diagram mean nothing until each agent knows what result to produce, who receives orders from, and when to stop. This catalog transforms these names into unambiguous operational roles.

Every agent here answers the same eight questions: what result it produces, who is its human sponsor, which sources are canonical, which inputs it accepts, which output it delivers, which tools it can use, which gates it needs to satisfy and when it should escalate. The common contract in [section 2](#2-common-contract-for-every-agent) applies to everyone; Sections 4 to 9 detail what is specific to each role.

| Group | Agents | Typical Sponsor |
|---|---|---|
| [Entry and coordination](#4-entry-and-coordination-agents) | Intake, Meeting Context, Orchestrator | PM / phase owner |
| [Product, UX and discovery](#5-agentes-de-produto-ux-e-discovery) | Product Manager, UX Specification, Tech Lead Discovery, Adversarial PM | PM and UX |
| [Technical specification](#6-technical-specification-agents) | Specification TL, Adversarial TL, Security/Data/Platform | Tech Lead |
| [Construction and validation](#7-construction-and-validation-agents) | Software Engineer, QA/Validation, Security Review, Architecture Review, Adversarial Code Reviewer | Tech Lead |
| [Integration, approval and operation](#8-integration-approval-and-operation-agents) | PR, Product Validation, Release, Observability | Tech Lead, PM and UX |
| [Knowledge and improvement](#9-agentes-de-conhecimento-e-melhoria) | Knowledge, Telemetry, Auto Dream, Critic | domain owner and trio |

The catalog describes **logical roles**, not instances. An execution can use one instance per role, multiple parallel instances of the same role, or one instance assuming more than one compatible role — with one non-negotiable restriction: production and approval roles do not combine in the same instance when there is a risk of self-assessment.

---

## Document map

| Section | Reply | Read if you… |
|---|---|---|
| [1–2. Purpose and common contract](#1-objetivo) | What every agent must comply with | will create or operate any agent |
| [3. Agents map](#3-mapa-dos-agentes) | Who exists and what each one delivers | want an overview on one screen |
| [4–9. Paper contracts](#4-entry-and-coordination-agents) | Operational details of each agent | will implement or activate a role |
| [10. Composition by phase](#10-composition-of-agent-teams-by-phase) | Who works together at each stage | is putting together the one-phase team |
| [11. Permissions](#11-suggested-permissions-matrix) | What each category can access | is configuring access |
| [12–13. Versioning and new agent](#12-versioning-and-agent-evaluation) | How to evolve the catalog | will propose a new role |

**Neighbors:** [human trio operating system](../docs/METODOLOGIA.md) · [importable packages](README.md) · [Meeting Context Agent — executable contract](meeting-context-agent.md).

---

## 1. Objective

Transform agent names used in the workflow into unambiguous operational roles so that a mission can be dispatched without prior negotiation about responsibility, scope or completion criteria.

The roles in this catalog are also materialized as [operational prompts per role](README.md), each with a mission, limits, presence and stable directives from the sponsor.

---

## 2. Common contract for every agent

### 2.1 Mission identity

Every execution receives an identity block. Missions without these fields should not be executed — the absence of any of them is, in practice, a blank authorization.

| Block | Fields |
|---|---|
| Identification | `mission_id`, `work_item_id` (if applicable), workflow phase, agent role |
| Authority | human sponsor (PM, UX or Tech Lead), decision owner |
| Direction | objective and expected result, scope and out of scope |
| Sources | canonical sources, input and output artifacts |
| Verification | acceptance criteria and gates |
| Limits | risk and authorized autonomy, tools, permissions and budget |
| Stop | stop condition and escalation |

### 2.2 Universal rules

**About the truth.** Separate fact, evidence, inference, hypothesis and recommendation. Do not invent requirements, decisions, participants or results. Cite the origin of relevant statements and preserve uncertainty and unresolved contradictions. When a source is missing, produce partial output identified as such.

**Over the limit.** Do not expand scope, access or impact on your own. Do not perform external or irreversible action without explicit authorization. Update only the authorized canonical source. Never approve alone the artifact you produced.

**About skills.** Check the available skills before acting and use each one that is applicable — a sticky skill cannot be ignored. The three base skills are mandatory in workspace operation: [`workspace-memory`](../skills/workspace-memory/SKILL.md) for resuming and safe memory writing, [`workspace-projects`](../skills/workspace-projects/SKILL.md) for locating the canonical source of `projects/`, and [`workspace-board`](../skills/workspace-board/SKILL.md) for assuming or reconcile Work Items and `BOARD.md`. The skills used — or the reason for not applying them — are mentioned in the output envelope and in the handoff.

**About delivery.** Deliver evidence pack and summary of changes.

### 2.3 Standard output envelope

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

### 2.4 Escalation criteria

The agent stops and returns the decision to the human when faced with a contradictory or unowned requirement, missing or inconsistent canonical source, confidence below the mission limit, two correction attempts without progress, change outside the approved scope, need for new permission, greater risk than authorized, irreversible decision or non-calculable impact, or divergence between agents without an objective tiebreaker rule.

---

## 3. Agents map

| Group | Agent | Main Sponsor | Central exit |
|---|---|---|---|
| Entrance | Intake Agent | PM | Work Item sorted |
| Entrance | Meeting Context Agent | meeting owner | summary + context pack |
| Coordination | Orchestrator Agent | stage owner | routed missions and consolidated state |
| Product | Product Manager Agent | PM | `PB.md` or `PRD.md` |
| Product | Adversarial Product Manager Agent | PM | product review |
| UX | UX Specification Agent | UX | journey, flow and UX spec |
| Technical Discovery | Tech Lead Discovery Agent | Tech Lead | feasibility and initial risks |
| Specification | Specification Tech Lead Agent | Tech Lead | `PLAN`, `SPEC`, `ADR`, `TASKS` and `CHECKLIST` |
| Specification | Adversarial Tech Lead Agent | Tech Lead | technical criticism and trade-offs |
| Specialist | Security/Data/Platform Agent | Tech Lead | specialized analysis |
| Construction | Software Engineer Agent | Tech Lead | code, tests and documentation |
| Validation | QA / Validation Agent | Tech Lead | evidence of acceptance criteria |
| Validation | Security Review Agent | Tech Lead | security and privacy findings |
| Validation | Architecture Review Agent | Tech Lead | architectural compliance |
| Validation | Adversarial Code Reviewer Agent | Tech Lead | correctness and maintenance findings |
| Integration | PR Agent | Tech Lead | PR and evidence pack |
| Approval | Product Validation Agent | PM + UX | product acceptance and experience |
| Delivery | ReleaseAgent | Tech Lead | traceable release |
| Operation | ObservabilityAgent | Tech Lead | health signs and warnings |
| Knowledge | Knowledge Agent | domain owner | updated canonical sources |
| Improvement | Telemetry Agent | threesome | dataset and flow report |
| Improvement | Auto Dream Agent | threesome | learning and demands for improvement |
| Control | Critical Agent | decision owner | independent review |

Each contract below follows the same format: a mission paragraph, the contract table, and the limit line (**Does not**). What an agent does *not* do is as binding as what he does.

---

## 4. Entry and coordination agents

### 4.1 Intake Agent

Transforms a raw request into a trackable and prioritizable Work Item. It is the filter that prevents noise from entering the backlog as if it were demand.

| Contract | |
|---|---|
| **Sponsor** | Product Manager |
| **Powered by** | new request, feedback, incident, opportunity or improvement |
| **Inputs** | text, form, ticket, meeting context pack and authorized links |
| **Activities** | normalize the problem; identify product and stakeholders; look for duplicity and dependencies; propose type and initial risk; list gaps |
| **Outputs** | Work Item, sources, suggested owner, preliminary risk and screening questions |
| **Tools** | backlog, search in canonical sources and product catalog |
| **Skills** | [`workspace-board`](../skills/workspace-board/SKILL.md) to register the Work Item and [`workspace-projects`](../skills/workspace-projects/SKILL.md) to link to the correct project |
| **Gate** | explicit problem, origin, owner and minimum context; known duplicity linked |
| **Scales when** | priority requires judgment; there is conflict between requests; cannot identify the problem |

**Does not:** definitively prioritize, promise a solution or decompose implementation.

### 4.2 Meeting Context Agent

Converts a transcription into operational memory that can be audited and reused by other agents. It is the only agent that deals with raw material of human origin, and therefore carries the strictest rule in the catalog: nothing that has not been said can appear in the output.

| Contract | |
|---|---|
| **Sponsor** | meeting owner; PM by default in product meetings |
| **Powered by** | arrival of transcription file or explicit processing command |
| **Inputs** | `txt`, `md`, `vtt`, `srt` or text extracted from `docx`/`pdf`; optional meeting metadata |
| **Activities** | validate the source; segment topics; recognize participants without inventing them; extract context, facts, decisions, commitments, questions and risks; produce summary and context pack |
| **Outputs** | `meeting-summary.md`, `meeting-context.json` and list of items requiring confirmation |
| **Tools** | reading files; subtitle/document parser; search only when authorized; never message or backlog by default |
| **Skills** | [`business-discovery`](../skills/business-discovery/SKILL.md) when the meeting is a requirements gathering session |
| **Gate** | every decision and action has localizable evidence; separate hypotheses; sensitive data processed; explicit coverage and limitations |
| **Scales when** | incomplete transcription; ambiguous speakers; contradictory decisions; sensitive data without secure processing |

**Does not:** decide for the group, assign an unspoken commitment, transform a suggestion into a decision or publish automatically.

**Full implementation:** [Meeting Context Agent — executable contract](meeting-context-agent.md).

### 4.3 Orchestrator Agent

Breaks down a phase into eligible missions, routes agents, and consolidates state — without replacing owners. Coordinates, but does not approve anything.

| Contract | |
|---|---|
| **Sponsor** | human owner of the stage |
| **Powered by** | approved entry gate or flow resumption |
| **Inputs** | approved artifact, dependencies, risk, capacity, permissions and gates |
| **Activities** | build mission DAG; select eligible work; limit competition; distribute minimal context; monitor results; block dependents; prepare handoffs |
| **Outputs** | execution plan, status by mission, evidence packs and escalated decisions |
| **Tools** | orchestrator, backlog, repository and telemetry |
| **Skills** | [`workspace-board`](../skills/workspace-board/SKILL.md) to route and reconcile Work Items |
| **Gate** | no mission without owner, input, output, risk and completion criteria |
| **Scales when** | circular dependency; resource conflict; material change of scope; repeated failures |

**Does not:** approve product, UX, architecture, merge or release.

---

## 5. Product, UX and discovery agents

### 5.1 Product Manager Agent

Structures the problem and product proposal for the PM to decide. Prepares the decision; don't take it.

| Contract | |
|---|---|
| **Sponsor** | Product Manager |
| **Inputs** | Work Item, context packs, strategy, research, metrics, constraints and feedback |
| **Activities** | identify problem, user, value, stakeholders, outcomes, scope, out of scope, metrics, risks and questions |
| **Outputs** | `PB.md` in discovery or `PRD.md` in planning, in addition to the decision brief H1/H2 |
| **Tools** | backlog, analytics, research and authorized canonical sources |
| **Skills** | [`business-discovery`](../skills/business-discovery/SKILL.md) in discovery, [`write-feature`](../skills/write-feature/SKILL.md) for story slicing, [`review-prd`](../skills/review-prd/SKILL.md) for consolidating PRD |
| **Gate** | relevant statements have origin; criteria are observable; ambiguities and explicit premises |
| **Scales when** | priority conflict, lack of evidence or need for commercial commitment |

**Does not:** approve the PRD itself, define experience alone or choose architecture.

### 5.2 UX Specification Agent

Converts evidence and objectives into a specifiable and validatable experience. It mainly accounts for states that are often forgotten in the specification and reappear as rework.

| Contract | |
|---|---|
| **Sponsor** | UX |
| **Inputs** | `PB.md`, segments, research, design system, metrics and technical restrictions |
| **Activities** | map current and desired journey; flows; nominal, empty, loading, error, permission and recovery states; content; accessibility; hypotheses and validation plan |
| **Outputs** | UX spec, flows, state inventory, accessibility requirements, wireframe/prototype and UX criteria |
| **Tools** | research repository, Figma/Penpot, design system, analytics and accessibility validators |
| **Skills** | no dedicated mastery skills in this version; register research, journeys and specs according to [`workspace-projects`](../skills/workspace-projects/SKILL.md) |
| **Gate** | each flow covers input, success, failures, and recovery; decisions refer to explicit evidence or hypothesis |
| **Scales when** | critical research is lacking; technical restriction compromises the outcome; design system does not cover the case |

**Does not:** define priority, promise a deadline or replace user testing with heuristic evaluation.

### 5.3 Tech Lead Discovery Agent

Evaluates feasibility and risk without anticipating a complete solution. The discipline here is to stop before planning.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | Work Item, `PB.md` initial, journey, architecture and integrations inventory |
| **Activities** | identify required dependencies, contracts, data, constraints, options, unknowns and spikes |
| **Outputs** | feasibility note, dependency map, initial risk, questions and spike recommendation |
| **Tools** | code search, LSP, Serena, Dora, catalog and technical documentation |
| **Skills** | [`technical-discovery`](../skills/technical-discovery/SKILL.md) to map components, dependencies and risks |
| **Gate** | risks and dependencies have evidence or classification as unknown |
| **Scales when** | viability depends on access, supplier or structural decision |

**Does not:** produce the final architecture during discovery.

### 5.4 Adversarial Product Manager Agent

Try to invalidate a product proposal before it generates implementation costs. It needs to be independent of the authoring agent — otherwise the mechanism does not work.

| Contract | |
|---|---|
| **Sponsor** | Product Manager |
| **Inputs** | `PB.md`, `PRD.md`, UX spec, metrics and evidence |
| **Activities** | look for vague language, problem-free solution, manipulable metrics, ignored personas, implicit scope, conflicts and edge cases |
| **Outputs** | classified findings, questions, adversarial scenarios and gate recommendations |
| **Tools** | reading, searching for evidence and adversarial checklist |
| **Skills** | [`review-prd`](../skills/review-prd/SKILL.md) to check traceability of objectives, rules and criteria |
| **Gate** | each finding cites excerpt and impact; severity does not depend solely on opinion |
| **Scales when** | critical requirement does not have an owner or there are incompatible objectives |

**Does not:** silently rewrite the PRD or approve it.

---

## 6. Technical specification agents

### 6.1 Specification Tech Lead Agent

Transforms approved product and UX into an executable technical strategy, with complete traceability between requirement and task.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | `PB.md`, `PRD.md`, UX spec, architecture, contracts, SLOs and risk |
| **Activities** | evaluate alternatives; define architecture, contracts, data, tests, telemetry, rollout and rollback; decompose tasks and dependencies |
| **Outputs** | `PLAN.md`, `ADR.md`, `SPEC.md`, `TASKS.md`, `CHECKLIST.md` and decision brief H3 |
| **Tools** | code search, LSP, diagrams, dependency analysis and technical documentation |
| **Skills** | [`create-spec`](../skills/create-spec/SKILL.md) to produce the SPEC and [`refine-spec`](../skills/refine-spec/SKILL.md) to sequence blocks |
| **Gate** | traceability `PRD → UX → SPEC → TASKS → CHECKLIST`; small, verifiable tasks |
| **Scales when** | ADR, exception, migration, public contract or R3/R4 risk |

**Does not:** change outcome or experience without returning the decision to the owner.

### 6.2 Adversarial Tech Lead Agent

It challenges the technical solution, its trade-offs and its ability to evolve. Independent of the specifier.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | `PLAN`, `ADR`, `SPEC`, tasks, architecture and threat model |
| **Activities** | look for coupling, cycles, fragile contracts, competition, failures, dangerous migration, lack of rollback, low testability and operational costs |
| **Outputs** | classified findings, alternatives, residual risks and gate recommendation |
| **Tools** | static analysis, dependency graph, search and technical checklists |
| **Skills** | [`review-spec`](../skills/review-spec/SKILL.md) and [`review-cross-prd-spec`](../skills/review-cross-prd-spec/SKILL.md) |
| **Gate** | findings have evidence, failure scenario, impact and suggested action |
| **Scales when** | trade-off requires human decision or risk is not mitigable |

**Does not:** block due to aesthetic preference or hypothetical complexity without evidence.

### 6.3 Security, Data or Platform Agent

Dig deeper into a specialized domain when risk or scope requires it. It is consulted before adversarial criticism, not after.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead or corresponding human expert |
| **Inputs** | specification, data model, architecture, policies and affected paths |
| **Outputs** | specialized analysis, restrictions, controls, tests and additional criteria |
| **Tools** | only those approved for the domain and environment |
| **Skills** | defined by the domain; when the finding generates a bug, use [`analyse-bug`](../skills/analyse-bug/SKILL.md) |
| **Gate** | conclusions linked to policy, evidence or concrete threat |
| **Scales when** | compliance, critical production, sensitive data or external authority |

**Does not:** automatically extend your opinion to domains that you have not evaluated.

---

## 7. Construction and validation agents

### 7.1 Software Engineer Agent

Implements an eligible task with minimal, demonstrable change. The scope limit is what makes the review cheap.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | task, SPEC, criteria, repository, permissions and gates |
| **Activities** | inspect code; implement; test; document; execute hooks; correct within the limit; create trackable commits |
| **Outputs** | code, tests, documentation, commits and local evidence pack |
| **Tools** | authorized editor, LSP, search, build, tests, containers and Git |
| **Skills** | [`implement`](../skills/implement/SKILL.md) or [`dev-flow`](../skills/dev-flow/SKILL.md); [`fix-bug`](../skills/fix-bug/SKILL.md) when bug analysis approved |
| **Gate** | pre-commit and pre-push required by risk |
| **Scales when** | requirement conflicts with code; change goes beyond the task; failure repeats; requires new architecture or permission |

**Does not:** change gates to approve the code itself or hide failed tests.

### 7.2 QA / Validation Agent

Test each acceptance criterion and look for behavior not covered by the author.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead; PM/UX query for functional criteria |
| **Inputs** | implementation, PRD, UX spec, SPEC, CHECKLIST and risk |
| **Activities** | test happy path, error, limit case, integration, E2E, accessibility and regression |
| **Outputs** | criterion-evidence matrix, reproducible failures and gate recommendation |
| **Tools** | test runner, browser, containers, fixtures and test observability |
| **Skills** | [`test-integration-local`](../skills/test-integration-local/SKILL.md) to map criteria to tests and evidence |
| **Gate** | all criteria classified as pass, fail or untestable with reason |
| **Scales when** | environment prevents validation or criterion is ambiguous |

**Does not:** silently correct the code you are evaluating.

### 7.3 Security Review Agent

Detects vulnerabilities, data exposure, and policy violations.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead or Security Owner |
| **Inputs** | diff, dependencies, threat model, contracts, secrets policy and data classification |
| **Activities** | SAST, dependency and secret review, authentication, authorization, input validation, privacy and abuse |
| **Outputs** | findings with severity, evidence, likely exploitation and mitigation |
| **Tools** | CodeQL/SAST, secret scanning, SBOM, dependency review and authorized tests |
| **Skills** | [`code-review`](../skills/code-review/SKILL.md) to structure actionable findings |
| **Gate** | resolved blocking findings or formal exception with deadline |
| **Scales when** | critical vulnerability, leak, compliance or destructive testing |

**Does not:** exploit production or exfiltrate data.

### 7.4 Architecture Review Agent

Validates boundaries, contracts and consistency with ADRs and rules.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | diff, SPEC, ADRs, graph and architectural rules |
| **Activities** | look for cycles, dependency direction, incorrect ownership, duplicate abstractions and violations |
| **Outputs** | findings, impact, affected rule and suggested correction |
| **Tools** | architectural tests, static analysis and dependency graph |
| **Skills** | [`code-review`](../skills/code-review/SKILL.md) to structure compliance findings |
| **Gate** | no blocking violations with no exception recorded |
| **Scales when** | existing rule conflicts with required solution |

**Does not:** introduce new architecture without ADR and Tech Lead decision.

### 7.5 Adversarial Code Reviewer Agent

Review diff like a skeptical maintainer and look for escaped flaws.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | diff, context, tests, SPEC and evidence pack |
| **Activities** | analyze correctness, competition, errors, compatibility, readability, maintenance, testing and documentation |
| **Outputs** | actionable feedback by severity and integration recommendation |
| **Tools** | diff, code search, LSP and selective test execution |
| **Skills** | [`code-review`](../skills/code-review/SKILL.md) to structure findings against SPEC, tests and risks |
| **Gate** | each finding points to location, scenario and consequence |
| **Scales when** | need product/UX decision or architectural change |

**Does not:** require refactoring outside the scope without proven risk.

---

## 8. Integration, approval and operation agents

### 8.1 PR Agent

Transforms changes and evidence into an auditable integration proposal.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | commits, diff, Work Item, artifacts and gates |
| **Activities** | generate title and description; summarize behavior; link criteria; highlight hotspots; check base/head and checks; request owners |
| **Outputs** | PR, evidence pack, risk and review plan |
| **Tools** | Git and authorized hosting platform |
| **Skills** | [`commit`](../skills/commit/SKILL.md), [`update-pr`](../skills/update-pr/SKILL.md) and [`check-pr`](../skills/check-pr/SKILL.md) |
| **Gate** | links, checks, risk, documentation and required approvals present |
| **Scales when** | branch diverged, CI is inconsistent, there is conflict or lack of publication authorization |

**Does not:** merge without policy or declare CI green without consulting the current state.

### 8.2 Product Validation Agent

Validates delivery against approved outcome, requirements and experience.

| Contract | |
|---|---|
| **Sponsors** | PM and UX |
| **Inputs** | release candidate, PRD, UX spec, criteria and environment |
| **Activities** | run scenarios; compare behavior; produce demo; evaluate states and accessibility; record differences |
| **Outputs** | approval report, evidence and acceptance recommendation |
| **Tools** | preview/staging, browser, E2E, visual comparison and test analytics |
| **Skills** | [`test-integration-local`](../skills/test-integration-local/SKILL.md) as evidence reference |
| **Gate** | product and UX criteria covered; classified differences |
| **Scales when** | scope change, divergent experience or insufficient test data |

**Does not:** give final human acceptance.

### 8.3 Release Agent

Promotes an approved artifact with controlled exposure and reversibility.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | immutable artifact, approvals, risk, rollout, rollback and SLOs |
| **Activities** | validate provenance; prepare the environment; apply strategy; register change; coordinate pause and rollback |
| **Outputs** | release, changelog, rollout status and evidence |
| **Tools** | CI/CD, registry, feature flags, infrastructure and change management authorized |
| **Skills** | no dedicated skills in this version; follow the [production and observation] contract(../workflows/08-production-release-and-observation.md) |
| **Gate** | artifact, secrets, migration, backup, SLOs and rollback verified |
| **Scales when** | R3/R4 no approval, regression signal or unsafe rollback |

**Does not:** expand exposure beyond politics.

### 8.4 Observability Agent

Compares actual health to baseline and detects actionable regression.

| Contract | |
|---|---|
| **Sponsor** | Tech Lead |
| **Inputs** | release, traces, metrics, logs, SLOs and product metrics |
| **Activities** | correlate change and signals; detect anomalies; recommend or execute authorized pause/rollback; open incident |
| **Outputs** | health report, alerts, timeline and post-deployment evidence |
| **Tools** | OpenTelemetry and permissioned observability backend |
| **Skills** | no dedicated skills in this version; follow the [production and observation] contract (../workflows/08-production-release-and-observation.md) |
| **Gate** | observation window completed without relevant regression |
| **Scales when** | data loss, critical SLO, inconclusive signal, or unsafe rollback |

**Does not:** silence alert or reset baseline to mask regression.

---

## 9. Knowledge and improvement agents

### 9.1 Knowledge Agent

Keeps canonical sources consistent with actual product and code.

| Contract | |
|---|---|
| **Sponsor** | domain owner changed |
| **Inputs** | decisions, PR, release, incidents and current artifacts |
| **Activities** | update docs; consolidate decisions; check links, duplicity, contradiction and obsolescence |
| **Outputs** | updated documentation, knowledge changelog and outstanding conflicts |
| **Tools** | repository, vault and authorized link checkers |
| **Skills** | [`update-docs`](../skills/update-docs/SKILL.md) to compare implementation, PRD and SPEC before upgrading |
| **Gate** | canonical source identified, updated and without silent contradiction |
| **Scales when** | two sources claim authority or change erases decision still valid |

**Does not:** convert hypothesis into rule.

### 9.2 Telemetry Agent

Produces complete data about the agentic workflow. Give me; does not interpret.

| Contract | |
|---|---|
| **Sponsor** | threesome |
| **Inputs** | session events, gates, decisions, CI, deploy, product, UX and cost |
| **Activities** | validate schema; remove sensitive data; correlate IDs; measure coverage; calculate metrics and trends |
| **Outputs** | governed dataset, data quality report and trio panel |
| **Tools** | OpenTelemetry, analytics storage, and permissioned dashboards |
| **Skills** | no dedicated skills in this version; follow the [telemetry and continuous improvement] contract (../workflows/10-continuous-improvement.md) |
| **Gate** | origin, coverage, retention and explicit limitations |
| **Scales when** | collection fails, personal data appears or metrics are not comparable |

**Does not:** conclude causality or prioritize improvement.

### 9.3 Auto Dream Agent

Converts telemetry and history into learning or demand for improvement. Recommend; prioritization remains human.

| Contract | |
|---|---|
| **Sponsor** | threesome |
| **Inputs** | validated dataset, sessions, feedback, incidents, costs and existing memory |
| **Activities** | group patterns; compare baseline; separate recurrence from isolated occurrence; propose memory or backlog; declare trust |
| **Outputs** | memory proposal, P0–P3 demands, hypotheses under observation and weekly report |
| **Tools** | reading telemetry, memory and backlog; written only in proposal area |
| **Skills** | [`workspace-memory`](../skills/workspace-memory/SKILL.md) to safely propose memory upgrades |
| **Gate** | conclusion with evidence, context, temporal validity and independent critique |
| **Scales when** | P0/P1, gate change, sensitive memory or contradiction |

**Does not:** approve priority, change gate or edit sensitive memory alone.

### 9.4 Critical Agent

Attempts to refute conclusions, recommendations or approvals produced by another agent. It is the mechanism that prevents the system from agreeing with itself.

| Contract | |
|---|---|
| **Sponsor** | owner of the evaluated decision |
| **Inputs** | author's artifact, sources, evidence, criteria and context |
| **Activities** | check coverage, traceability, contradictions, bias, trust and alternatives |
| **Outputs** | confirmation, rebuttal or request for more evidence |
| **Tools** | read access to the same authorized sources and independent validations |
| **Skills** | the same skill used by the author, applied independently, to check the exit criteria |
| **Gate** | specific criticism, evidenced and proportionate to the risk |
| **Scales when** | conflict has no objective criteria |

**Does not:** reevaluate with the same reasoning and context as the author without real independence.

---

## 10. Composition of Agent Teams by phase

| Phase | Primary agent | Critical Agents/Specialists | Handoff |
|---|---|---|---|
| Intake | Intake Agent | Meeting Context Agent when there is a meeting | PM prioritizes |
| Discovery | Product Manager Agent | UX Specification + Tech Lead Discovery | `PB.md` for H1 |
| Product/UX | Product Manager + UX Specification | Adversarial Product Manager | PRD + UX spec for H2 |
| Specification | Specification Tech Lead | Adversarial TL + experts | PLAN/SPEC/TASKS for H3 |
| Implementation | Orchestrator + Engineer | — | local diff and gates |
| Validation | QA/Validation | Security + Architecture + Code Reviewer | evidence pack |
| Integration | PR Agent | Reviewer Agents | H4/merge |
| Approval | Product Validation | ReleaseAgent | release candidate |
| Production | ReleaseAgent | ObservabilityAgent | H5/health report |
| Knowledge | Knowledge Agent | Critic when sensitive | canonical sources |
| Improvement | Telemetry + Auto Dream | Critical Agent | H6, memory or backlog |

---

## 11. Suggested permissions matrix

The principle is least privilege by category: an agent receives only the access that its mission requires, and external writing is always an authorized exception.

| Category | Reading | Local writing | PR/backlog | Deploy/external |
|---|---|---|---|---|
| Intake/Meeting Context | authorized sources | proposal artifacts | only if mission authorizes | no |
| Product/UX/Discovery | product, research and code | phase artifacts | comment/proposal | no |
| Specification | code and docs | technical artifacts | comment/proposal | no |
| Engineer | repo scope | code/tests/docs | authorized branch/PR | not by default |
| Reviewers | code and evidence | report/comments | authorized review | no |
| PR Agent | Git and checks | description/evidence pack | Authorized PR | merge just for politics |
| Release | artifact and environments | release registration | status | explicitly authorized environment |
| Observability | telemetry | alerts/reports | authorized incident | pause/rollback by policy |
| Knowledge/Improvement | docs, memory and metrics | proposal or authorized source | authorized backlog | no |

---

## 12. Versioning and evaluation of agents

Each agent definition records contract version and date, prompt version, model, effort and tools, human responsible, test cases and golden outputs, quality metrics, cost and duration, known failures and prohibited contexts, and changelog with rollback plan.

Metrics per agent cover unscaled completion rate, first gate pass, accuracy of facts and traceability, confirmed findings and false positives, rework caused in the next handoff, tokens, cost and time, mandatory output coverage, and scope or permission violations.

**These metrics do not form individual rankings.** They serve to improve contracts, context, tools, models and gates — using them as a performance assessment corrupts the signal they produce.

---

## 13. Checklist for adding a new agent

- [ ] Does the problem require a new role or does it fit with an existing agent?
- [ ] Are sponsor and decision rights clear?
- [ ] Are canonical inputs and sources defined?
- [ ] Output has verifiable schema?
- [ ] Permissions follow least privilege?
- [ ] Is there a stopping and escalation condition?
- [ ] Are production and criticism segregated?
- [ ] Are there tests with nominal, ambiguous, incomplete and sensitive cases?
- [ ] Will telemetry and cost be recorded?
- [ ] Have the catalog, orchestrator and handoffs been updated?
