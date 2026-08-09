---
title: Agent Team — skills catalog
status: canonical
updated_at: 2026-08-09
---

# Skills catalog

> The 22 Agent Team skills, what each one guarantees and at what point in the journey it is mandatory.

## In 2 minutes

An agent without skills improvises. He invents the name of the artifact, chooses where to record it himself, decides on the spot what counts as evidence — and the result is a repository where each execution followed a different convention. A skill is the opposite of this: a named procedure, with input, output and completion criteria, that produces the same artifact shape every time it runs.

That's why the operation rule is short and without exception: **check the available skills before acting and use all that apply**. A skill that adheres to the mission cannot be ignored, and the agent mentions in the Work Item, in the handoff and in the result which ones he used — or the reason why none of them apply.

Skills are divided into three natures. The **base** rules govern the operation of the workspace and are valid for any mission, in any role. **domain** correspond to a specific stage of the journey and produce the artifact of that stage. **Publishing** touches Git and GitHub, and therefore only executes upon explicit request.

| Nature | Skills | When they apply |
|---|---|---|
| **Workspace base** | `workspace-memory`, `workspace-projects`, `workspace-board` | every mission, always |
| **Discovery and product** | `business-discovery`, `write-feature`, `review-prd` | steps 01–02 |
| **Technical specification** | `technical-discovery`, `create-spec`, `refine-spec`, `review-spec`, `review-cross-prd-spec` | step 03 |
| **Implementation and validation** | `dev-flow`, `implement`, `test-integration-local`, `code-review` | steps 04–05 |
| **Defect correction** | `analyse-bug`, `fix-bug` | off-cycle, on-demand |
| **Publication** | `commit`, `update-pr`, `check-pr` | stage 06, only with authorization |
| **Knowledge** | `update-docs` | step 09 |

---

## Map of this document

| Section | Reply | Read if you… |
|---|---|---|
| [1. Base Skills](#1-skills-de-base) | Which is true for every mission | will operate in any workspace |
| [2. Skills per stage](#2-skills-por-etapa-da-jornada) | Which skill runs in which phase | is executing a step |
| [3. Anatomy of a skill](#3-anatomy-of-a-skill) | How a skill is written | are going to create or review a skill |
| [4. Autonomy limits](#4-limites-de-autonomia) | What requires human authorization | will delegate execution to an agent |

**Neighbors:** [operational model](../docs/METODOLOGIA.md) · [workflows per step](../workflows/README.md) · [agent catalog](../agents/catalog.md) · [artifact contract](references/workflow-contract.md).

---

## 1. Base skills

The three basic skills exist because an agent's most expensive mistake isn't writing bad code: it's writing the right artifact in the wrong place, or treating working memory as a source of truth. They are mandatory in any mission, before any mastery skill.

| Skill | Guarantee | Failure that it prevents |
|---|---|---|
| [`workspace-memory`](workspace-memory/SKILL.md) | Context recovery and secure memory writing | agent treat `memory.md` as canonical source |
| [`workspace-projects`](workspace-projects/SKILL.md) | Correct canonical source and isolated assets per session | conclusion written to the wrong domain; sessions overwriting themselves |
| [`workspace-board`](workspace-board/SKILL.md) | Selection, transition and reconciliation of Work Items | work without item, or item moved to `done` without evidence |

The practical order when starting a mission: `workspace-memory` to retrieve context, `workspace-board` to assume the item, `workspace-projects` to locate where the artifact belongs — and only then the mastery skill.

---

## 2. Skills per stage of the journey

Each stage of the journey has the skill that produces its artifact. The table below is the direct translation of [workflows](../workflows/README.md) into executable procedures.

| Step | Skill | Delivery |
|---|---|---|
| [01 · Discovery](../workflows/01-discovery-and-research.md) | [`business-discovery`](business-discovery/SKILL.md) | cumulative business requirements, with baseline, changelog and gaps |
| [02 · Product and UX](../workflows/02-product-and-ux-planning.md) | [`write-feature`](write-feature/SKILL.md) | sliced ​​stories, linked to rules and criteria |
| [02 · Product and UX](../workflows/02-product-and-ux-planning.md) | [`review-prd`](review-prd/SKILL.md) | PRD with traceable objectives, rules and success criteria |
| [03 · Specification](../workflows/03-technical-specification.md) | [`technical-discovery`](technical-discovery/SKILL.md) | technical vision: components, dependencies, risks and open decisions |
| [03 · Specification](../workflows/03-technical-specification.md) | [`create-spec`](create-spec/SKILL.md) | SPEC with verifiable contracts, risks and technical criteria |
| [03 · Specification](../workflows/03-technical-specification.md) | [`refine-spec`](refine-spec/SKILL.md) | sequential plan of testable blocks and their dependencies |
| [03 · Specification](../workflows/03-technical-specification.md) | [`review-spec`](review-spec/SKILL.md) | SPEC gaps, ambiguities and risks before approval |
| [03 · Specification](../workflows/03-technical-specification.md) | [`review-cross-prd-spec`](review-cross-prd-spec/SKILL.md) | coverage, conflicts and pending decisions between PRD and SPEC |
| [04 · Implementation](../workflows/04-autonomous-implementation.md) | [`implement`](implement/SKILL.md) | a block of the implemented plan, with incremental validation |
| [04 · Implementation](../workflows/04-autonomous-implementation.md) | [`dev-flow`](dev-flow/SKILL.md) | end-to-end driving when delivery does not require phase-by-phase |
| [04 · Implementation](../workflows/04-autonomous-implementation.md) | [`test-integration-local`](test-integration-local/SKILL.md) | missing coverage created and criteria mapped to tests |
| [05 · Validation](../workflows/05-adversarial-validation.md) | [`code-review`](code-review/SKILL.md) | actionable findings against SPEC, testing and risks |
| [06 · PR and merge](../workflows/06-pr-and-merge.md) | [`commit`](commit/SKILL.md) · [`update-pr`](update-pr/SKILL.md) · [`check-pr`](check-pr/SKILL.md) | change registered, described and verified |
| [09 · Knowledge](../workflows/09-knowledge-curation.md) | [`update-docs`](update-docs/SKILL.md) | documentation in line with what was delivered, with deviations recorded |

**Defect fix.** Bugs enter out of sequence, and therefore have their own pair: [`analyse-bug`](analyse-bug/SKILL.md) tracks root cause and documents impact **without touching code**, and [`fix-bug`](fix-bug/SKILL.md) implements the fix with regression testing. The separation is deliberate — correcting before understanding the impact is how most regressions are born.

---

## 3. Anatomy of a skill

A skill is a directory with `SKILL.md` at the root. The front matter declares `name` and `description`, and the description is what determines whether the skill will be activated: it says what the skill does and **in which situation to use it**, because it is through this text that the agent decides whether it applies to the current mission.

```text
skills/<name>/
├── SKILL.md # procedure: input, steps, output and completion criteria
├── README.md # additional context, when the procedure does not explain itself
├── templates/ # artifact formats that the skill produces
└── agents/ # specific agent configuration, when available
```

Skills that share artifact conventions point to [artifact contract](references/workflow-contract.md), which defines where PRD, SPEC, plans, and requirements live and what to do when the consuming repository diverges from the default layout. His central rule: **the local repository convention prevails**, and the mapping is committed before writing.

Unlike documentation for humans, `SKILL.md` is read by an agent at runtime. Dense, imperative lists are intentional there — the [documentation standard](../docs/metodologia/07-workflows-de-documentacao.md) applies to human-readable documents, not these instructions.

---

## 4. Limits of autonomy

Skills do not extend permission. An implementation skill does not authorize publishing, and none of them decides alone what becomes an approved baseline.

| Action | Requires explicit request |
|---|---|
| Create branch, worktree and change local code | no, within the authorized scope of the Work Item |
| Create issue, commit, push, PR, merge and worktree cleanup | yes, each one separately |
| Change requirements, acceptance criteria or approved PRD/SPEC status | yes, with registered decision |
| Move a Work Item to `done` | no, but only with evidence for all criteria |

Deviations from an approved baseline go to reporting, never to silent editing of the artifact. It is this asymmetry — executing with freedom, publishing under authorization — that sustains the levels of autonomy described in [model 90/10](../docs/GATES.md).
