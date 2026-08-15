# Agent-Team — Documentation

> The pillars of an agentic team, from lowest to highest, like a pyramid: **harness → skills → agents → loops → methodology → workspace**. Each layer answers a different question and builds on the previous one; skipping a layer is what produces documentation that no one can execute.

## The pyramid

| # | Layer | Answers | Where it lives |
|---|---|---|---|
| 1 | **Harness** | what the repository needs to load to be operable by agents | [`REPO_HARNESS.md`](REPO_HARNESS.md) and neighbors |
| 2 | **Skills** | *how* a recurring task is performed correctly | [`SKILLS.md`](SKILLS.md) |
| 3 | **Agents** | *who* executes, under what authority and with what limits | [`AGENTES.md`](AGENTES.md), [`agentes/`](agentes/README.md) |
| 4 | **Loops** | *in what order* do agents collaborate and when to stop | [`LOOPS.md`](LOOPS.md), [`loops/`](loops/README.md) |
| 5 | **Methodology** | *who operates*, what triggers what and what demands people | [`METODOLOGIA.md`](METODOLOGIA.md), [`metodologia/`](metodologia/README.md) |
| 6 | **Workspace** | *where* every artifact of an execution lives, outside the code | [`WORKSPACE.md`](WORKSPACE.md), [`workspace/`](workspace/README.md) |

The base supports the top, not the other way around: a skill (2) is only verifiable if the harness (1) exists; an agent (3) is only trustworthy when it executes the skills that already exist over that harness; a loop (4) only coordinates agents and skills that already exist; methodology (5) does not introduce a new concept, it only explains how a person operates the four layers below; and the workspace (6) is the physical place where all this leaves a trace outside the code.

---

## 1. Application repository harness

The **repo harness** converts the tacit knowledge of the repository into versioned files that the agent reads on its own and into checks that run without asking for a license. Overview, the five cumulative layers (Context, Procedure, Verification, Permission, Evidence) and the four properties they need once the harness is operated (Trust, Resilience, Coordination, Economy) are in [`REPO_HARNESS.md`](REPO_HARNESS.md).

| Section | Answers | File |
|---|---|---|
| **Overview** | What is repo harness, the four questions it solves and the five cumulative layers | [`REPO_HARNESS.md`](REPO_HARNESS.md) |
| **Permissions** | which tools the agent may invoke, what requires human authorization, and why it cannot live in the prompt | [`PERMISSIONS.md`](PERMISSIONS.md) |
| **Tools** | the tooling index — verification, navigation, context management — and where each check runs | [`TOOLS.md`](TOOLS.md) |
| **Skills** | the catalog of verifiable procedures for recurring tasks that require judgment | [`SKILLS.md`](SKILLS.md) |
| **Rules** | the desired state of the repository — architecture, coding and testing — and the reason for each rule | [`RULES.md`](RULES.md) |
| **Hooks** | the local versioned checks (`.hooks/`) that run before the code leaves the agent machine | [`SENSORS.md`](SENSORS.md) |
| **Gates** | the commit-to-deploy verification architecture — local, CI, merge, environment, post-deploy | [`GATES.md`](GATES.md) |
| **Documentation** | `AGENTS.md`, ADRs, the evidence pack, and the identity that produced each artifact | [`DOCUMENTATION.md`](DOCUMENTATION.md) |
| **MCPs** | Model Context Protocol servers, authorized scopes and the difference for a local tool | [`MCPS.md`](MCPS.md) |

Seven further pages cover what the five layers need once the harness is operated rather than built — several agents at once, hostile input, checks that stop running, and a version history for the controls themselves.

| Section | Answers | File |
|---|---|---|
| **Trust** | which inputs are instructions and which are content; injection, exfiltration and supply chain | [`TRUST.md`](TRUST.md) |
| **Failure** | what happens when a gate does not run, and how a verification is itself verified | [`FAILURE.md`](FAILURE.md) |
| **Concurrency** | several agents in flight, evidence freshness and the order of integration | [`CONCURRENCY.md`](CONCURRENCY.md) |
| **Budget** | cost, turns, wall-clock and context — and what degrades when they run out | [`BUDGET.md`](BUDGET.md) |
| **Versioning** | the harness has a version, and changing it invalidates approvals granted before | [`VERSIONING.md`](VERSIONING.md) |
| **Metrics** | gate escape rate and the panel that raises or lowers the autonomy level | [`METRICS.md`](METRICS.md) |
| **Maturity** | the item-by-item checklist per level and the script that computes where a repository stands | [`MATURITY.md`](MATURITY.md) |

## 2. Skills

A skill is the verifiable procedure for a recurring task that requires judgment — which distinguishes it from a script, which covers the deterministic. Before acting, an agent checks the available skills and uses all that apply to the mission. The catalog — workspace base skills, skills by stage of the journey and the limits of autonomy that no skill extends — is in [`SKILLS.md`](SKILLS.md); the executable procedures, one `SKILL.md` per skill, are in [`skills/`](../skills/README.md).

## 3. Agents

An agent is a process with a delimited mission, versioned context, declared tools, objective verification and a standardized output envelope. The concept — anatomy, what it consumes, when it scales — is in [`AGENTES.md`](AGENTES.md); the 23 individual contracts, grouped by phase (entry and coordination, product/UX/discovery, technical specification, construction and validation, integration/approval/operation, knowledge and improvement), are in [`agentes/`](agentes/README.md).

## 4. Loops

A loop is the collaboration contract for a stage of the journey: who executes it, in what order, what crosses the boundary between agents and what condition needs to be true to move forward. The concept — the three turns and how agents, skills, tools, MCPs, sensors and gates fit into each turn — is in [`LOOPS.md`](LOOPS.md); the 12 contracts for the stages of the journey, from intake to daily operation, are in [`loops/`](loops/README.md).

## 5. Methodology — Software Development Cycle

The methodology is the glue between the previous layers and the person operating the system on Monday morning: it doesn't introduce a new concept, it shows what triggers what, when a person is called, and what happens if they don't respond. The five commitments that govern the cycle (who proposes does not approve; approval requires evidence; material change invalidates previous approval; autonomy increases by metric; artifact only exists in the canonical source) are in [`METODOLOGIA.md`](METODOLOGIA.md); the seven operational pages — roles, human checkpoints, triggers, rhythms, operator manual, commented journey and documentation workflows — are in [`metodologia/`](metodologia/README.md).

## 6. Workspace

The workspace is the physical place where work actually happens: where a Work Item is opened, a decision becomes an artifact, an agent returns to context from a previous session. The border with the repo harness and the four pieces that every workspace maintains (`AGENTS.md`, `BOARD.md`, `memory.md`, `projects/`) are at [`WORKSPACE.md`](WORKSPACE.md); the four operational pages — structure, ownership between workspaces, workspace harness and board/Work Items — are in [`workspace/`](workspace/README.md).

---

## Languages

Every page in this index is published in English and Brazilian Portuguese from the same branch: the canonical text lives at these paths and `i18n/pt-BR/` mirrors them one to one. A page without a translation yet falls back to English and says so at the top, and drift between the two is measured by `uv run scripts/i18n.py status`. How to translate, stamp and add a locale is in [`i18n/README.md`](../i18n/README.md); the terminology that must stay consistent is in [`i18n/GLOSSARY.md`](../i18n/GLOSSARY.md).

---

## Where to start

| Do you want… | Read |
|---|---|
| Prepare a repository to be operated by agents | [Harness](REPO_HARNESS.md) → [Permissions](PERMISSIONS.md) → [Tools](TOOLS.md) → [Skills](SKILLS.md) → [Rules](RULES.md) → [Hooks](SENSORS.md) → [Gates](GATES.md) → [Documentation](DOCUMENTATION.md) → [MCPs](MCPS.md) |
| Find out which maturity level a repository is really at | [Maturity](MATURITY.md) → [Gates](GATES.md) → [Metrics](METRICS.md) |
| Operate agents in production, at volume | [Trust](TRUST.md) → [Failure](FAILURE.md) → [Concurrency](CONCURRENCY.md) → [Budget](BUDGET.md) → [Versioning](VERSIONING.md) |
| Understand the agent catalog | [Agents](AGENTES.md) → [individual contracts](agentes/README.md) |
| See the journey from end to end | [Loops](LOOPS.md) → [the 12 steps](loops/README.md) |
| Knowing what a person does, in practice | [Methodology](METODOLOGIA.md) → [operator manual](metodologia/05-manual-do-operador.md) |
| Knowing where to save what you produce | [Workspace](WORKSPACE.md) → [workspace structure](workspace/01-estrutura-do-workspace.md) |
