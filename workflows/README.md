---
title: Agent Team — multi-agent workflows
status: proposed
updated_at: 2026-08-09
---

# Multi-agent workflows

> The collaboration contract between agents in each of the 12 stages of the journey: who does what, in what order, where each agent writes, what crosses the border and when to escalate.

## In 2 minutes

The [agent catalog](../agents/catalog.md) defines each role separately. A workflow defines what happens **between** them: the sequence of missions, the artifacts that cross boundaries, how independent contributions converge into a coherent output, and the point at which a decision should be escalated to the responsible human.

Workflows detail collaboration. They do not replace individual catalog contracts, the authority of the [methodology](../docs/METODOLOGIA.md), or the architecture of [gates](../docs/GATES.md). What each repository needs to load for these workflows to run with agents is in [Repo Harness](../docs/REPO_HARNESS.md).

Two distinctions resolve most doubts in practice:

| Distinction | What does it mean |
|---|---|
| **Catalog vs. execution** | `workflows/` is the canonical and versioned catalog; execution takes place in the owner's workspace, at `projects/<project>/`. Nothing from a performance is recorded in the catalogue. |
| **Canonical vs. traffic** | Persistent artifacts live in the domain's canonical source; `.coordination/` and `memory.md` are helpers and a handoff only ends when the final artifact has reached the canonical source. |

Each step has an explicit writer/consolidator for each output and agents that collaborate or challenge. Step 2 has two domain consolidators and a coherence barrier; in the others, a single agent consolidates the block. Criticism always comes from an instance independent of who produced the artifact.

---

## Dry-run mode

Workflows can be run in experimentation mode without generating persistent artifacts.

**How ​​to activate:** pass `mode: dry-run` at the start of the mission or prefix the command with `--dry-run`.

**Expected behavior:**
- The agent performs all reasoning, analysis and drafting normally.
- Does not create or modify files in `projects/`, `engineering/`, `execution/` or any other artifact folder.
- You can print what *would* have generated directly in the conversation.
- Does not update `BOARD.md`, `STATUS.md`, Work Items or handoffs.

**When to use:** explore an unknown workflow, test an approach before committing it, or validate agent behavior without side effects.

## Where the workflow lives and where execution happens

`workflows/` is the **canonical and versioned catalog** of reusable workflows. It does not receive artifacts from a concrete execution.

Each user or role runs the workflow within their own workspace. The installation of this workspace must contain `docs/workflows/` to register the enabled workflows, their version, permissions, integrations and local adaptations. This local layer references the canonical workflow — it does not copy it or become a competing source of truth.

```text
<user-workspace>/
├── docs/
│ └── workflows/ # local bindings for workflows/
├── projects/
│ └── <project>/ # persistent artifacts from a run
├── .coordination/ # handoffs and temporary blocks (hidden)
├── memory.md # agent resumable context, never canonical source
└── repos/ # only in technical workspace, when applicable
```

Before starting a mission, the agent resolves: `owner workspace → projects/<project> → Work Item → canonical sources`. It never writes to the global catalog a `PB`, `PRD`, plan, evidence or handoff of an execution.

## Location of artifacts by workflow

The names below use `<pm-workspace>`, `<ux-workspace>`, and `<tech-lead-workspace>` to represent individual workspaces, and `<project>` for the common identifier between them.

| Workflow | Persistent sources and artifacts | Temporary transit |
|---|---|---|
| Intake | `<pm-workspace>/projects/<project>/work-items/` | `<pm-workspace>/.coordination/inbox/` and `handoffs/` |
| Discovery and research | PM: `<pm-workspace>/projects/<project>/discovery/`; UX: `<ux-workspace>/projects/<project>/research/` and `journeys/`; technical feasibility: `<tech-lead-workspace>/projects/<project>/engineering/architecture/` | `.coordination/handoffs/` from each workspace |
| Product and UX | PM: `<pm-workspace>/projects/<project>/requirements/prd/`, `strategy/`, `decisions/`; UX: `<ux-workspace>/projects/<project>/flows/`, `specifications/`, `prototypes/` and `validation/` | handoffs in `<pm-workspace>/projects/<project>/handoffs/` and `<ux-workspace>/projects/<project>/handoffs/` |
| Technical specification | `<tech-lead-workspace>/projects/<project>/plans/active/`, `engineering/specs/`, `engineering/adr/` and `work-items/` | `execution/handoffs/` |
| Implementation | `<tech-lead-workspace>/projects/<project>/work-items/`, `execution/evidence/` and `repos/worktrees/<org>/<repo>/<work-item>/` | `.coordination/active/` and `execution/handoffs/` |
| Validation and PR | `<tech-lead-workspace>/projects/<project>/execution/reviews/` and `execution/evidence/` | `.coordination/blockers/` for active exceptions |
| Approval | PM: `<pm-workspace>/projects/<project>/validation/`; UX: `<ux-workspace>/projects/<project>/validation/`; Tech Lead: `<tech-lead-workspace>/projects/<project>/execution/evidence/` | handoff to release |
| Production and observation | `<tech-lead-workspace>/projects/<project>/execution/evidence/`, `LEARNINGS.md` (candidates) and the authorized release registration | incident, alert and rollback in `.coordination/` until promoted |
| Knowledge curation | canonical source of the domain, `projects/<project>/LEARNINGS.md` and `execution/reviews/knowledge-<id>.md` | proposals not decided on `.coordination/` |
| Continuous improvement | Tech Lead: `execution/telemetry/`; memory validated in the workspace; PM: `projects/<project>/work-items/` | hypotheses in `.coordination/observations/` |
| Daily operation | memory validated and Work Items promoted to respective workspaces | briefing on `.coordination/daily/`, hypotheses and daily cursor |

`.coordination/` and `memory.md` are auxiliaries: a handoff only becomes complete when its final artifact is in the project's canonical source. If a required subfolder does not already exist, it must be created under `projects/<project>/` in the workspace that owns the domain — never under the global catalog or as another user's generic directory.

## Journey map

| Step | Workflow | Consolidating agent | Agents that collaborate or challenge |
|---:|---|---|---|
| 0 | [Intake and screening](00-intake-and-triage.md) | Intake Agent | Product Manager Agent; Meeting Context when there is a meeting |
| 1 | [Discovery and research](01-discovery-and-research.md) | Product Manager Agent | UX Specification; Tech Lead Discovery; Adversarial PM when there is a candidate proposal |
| 2 | [Product and UX planning](02-product-and-ux-planning.md) | Product Manager Agent + UX Specification | Adversarial Product Manager; research, content or prototyping specialists |
| 3 | [Technical specification](03-technical-specification.md) | Specification Tech Lead | Adversarial Tech Lead; Security/Data/Platform when necessary |
| 4 | [Standalone implementation](04-autonomous-implementation.md) | Orchestrator Agent | Software Engineer Agents |
| 5 | [Adversarial validation](05-adversarial-validation.md) | QA / Validation Agent | Security Review; Architecture Review; Adversarial Code Reviewer |
| 6 | [PR and merge](06-pr-and-merge.md) | PR Agent | Reviewer Agents |
| 7 | [Approval](07-release-candidate-validation.md) | Product Validation Agent | ReleaseAgent |
| 8 | [Production and observation](08-production-release-and-observation.md) | ReleaseAgent | ObservabilityAgent |
| 9 | [Knowledge curation](09-knowledge-curation.md) | Knowledge Agent | Critical Agent when the change is sensitive |
| 10 | [Telemetry and continuous improvement](10-continuous-improvement.md) | Auto Dream Agent | Telemetry; Observability; Critical Agent |
| 11 | [Daily Operation](11-daily-operations.md) | Auto Dream Agent | Telemetry; Knowledge; Orchestrator; Intake |

## Common contract

Every workflow explains the complete block. The absence of any item below makes the execution ambiguous, not idempotent or dependent on human negotiation.

| Item | Define |
|---|---|
| Unit and entrance | identifiers, baseline, artifacts and criteria to start |
| Preflight | authority, workspace, project, permissions, risk and stop condition |
| Missions | DAG, dependencies, parallelism and minimal context per agent |
| Writers and consolidation | who writes each source and who assembles the block output |
| Skills | applicable skills and exact registration in `skills_used` |
| Persistence | canonical sources, transit, and workspace reconciliation order |
| Gates | content gate and block closing gate with evidence |
| Handoffs | facts, evidence, hypotheses, risks and open questions |
| Retry and scaling | attempt limits, invalidation, stopping condition and human owner |
| End envelope | state, transition, outputs, decisions and proof of completion |

The block only closes when the loop, agents, canonical sources, workspace state, and next decision agree. The orchestrator distributes minimal context and controls dependencies — it does not replace the consolidater or the human owner's decision. Agents of criticism are always independent instances of who produced the evaluated artifact.

## Execution conventions

**Format.** Every mission uses the [catalog](../agents/catalog.md#23-standard-output-envelope) output envelope, and a handoff references versioned artifacts instead of copying the entire context.

**Convergence.** A contribution does not become a decision simply because it is included in the consolidated statement: divergences and residual risks remain explicit. The workflow ends with a coherent artifact and evidence pack, never with isolated responses from agents.

**Review.** New material information returns the workflow to the agent responsible for the review, and invalidates the related approval when policy determines.

**Local bindings.** The binding in `<workspace>/docs/workflows/` declares the canonical workflow version and can **restrict** tools, permissions, and integrations. It cannot expand autonomy or change gates without the decision foreseen in the operational model — this asymmetry is intentional.
