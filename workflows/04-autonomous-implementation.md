---
title: Workflow 04 — autonomous implementation
status: proposed
updated_at: 2026-08-09
---

# Workflow 04 — autonomous implementation

> [🔁 Ralph Loop](../docs/loops/04-autonomous-implementation.md) executable block: executes small, independent tasks in parallel, each rotating against objective local gates and under explicit retry, scope, and write limits.

The Orchestrator coordinates the DAG and consolidates state; he doesn't write code. Each Software Engineer Agent has exactly one mission, one Work Item and one writing surface. Parallelism only exists when dependencies and writer scopes prove independence.

---

## Block result

A closed round delivers trackable diffs, commits when authorized, tests/documentation and local evidence per Work Item. Dependents only become eligible after evidence of the predecessor exists; green gate makes the change ripe for adversarial attack, never approved.

| Layer | Closing condition |
|---|---|
| **Loop** | each mission ended against its own sensors and criteria, within the budget |
| **Agents** | Engineers preserved scope; Orchestrator consolidated state and dependencies, not code |
| **Repositories** | branch/base/worktree and pre-existing state are registered; competing writers did not collide |
| **Workspace** | Work Items and Evidence were updated before `STATUS.md` and `BOARD.md` |
| **Handoff** | Red Team receives diffs, baselines, raw results, pending issues and out of scope |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 4 — construction and validation |
| **Execution unit** | one eligible task per Engineer mission; a round adds independent missions |
| **Consolidates status** | [Orchestrator Agent](../agents/orchestrator-agent/AGENT.md) |
| **Implement** | one or more [Software Engineer Agents](../agents/software-engineer-agent/AGENT.md) |
| **Human owner** | Tech Lead, by policy and exception |
| **Input** | Work Items `ready`, SPEC/baseline, criteria, repositories, permissions, risk and gates |
| **Exit** | diffs, tests, docs, authorized commits, local evidence packs and consolidated handoff |
| **Gate per mission** | local sensors required by risk + task criteria approved and recorded |
| **Gate of the round** | terminal missions reconciled; correct dependencies; no collision/silent expansion; handoff complete |
| **Dominant lap** | internal — retry of the same agent against objective gate, with limit of attempts and time |
| **Next workflow** | [05 — adversarial validation](05-adversarial-validation.md) |

---

## Round Preflight

1. Read plan, SPEC, TASKS, CHECKLIST and Work Items; assemble DAG with real dependencies.
2. Select only items `ready`, without `blocked_by`, with human owner, risk, criteria, repository and permissions defined.
3. Resolve each repository by `engineering/repositories.yaml`; Read local instructions and check Git status before any edits.
4. Preserve pre-existing changes and register branch, base, worktree and authorized paths in the Work Item.
5. Detect collisions: two missions that write the same file, contract, migration or external resource do not run in parallel without explicit splitting.
6. Set concurrency limit, budget, attempts, sensors, stopping condition and commit/push policy per mission.
7. Register the assumption in the Work Item and create a transient state in `.coordination/active/<mission-id>.md`.

Code and tests are never written to `plans/assets/`; live in worktree. Preflight is blocking when local state cannot be safely preserved or the task requires missing decision.

### Mission envelope

```yaml
mission_id: "RALPH-<id>"
work_item_id: "<WI-id>"
workflow: "04-autonomous-implementation"
task_id: "<TASK-id>"
baseline:
  spec: "<path@revision>"
  commit: "<sha>"
repository:
  id: "<repo-id>"
  branch: "<branch>"
  base_branch: "<base>"
  worktree: "<absolute-or-bound-path>"
write_scope: []
dependencies: []
acceptance_criteria: []
sensors: []
risk: "<classe>"
permissions: []
retry:
  max_attempts: 2
  time_budget: "<limit>"
stop_conditions: []
```

---

## Scheduler and mission plan

```mermaid
TD flowchart
    A[TASKS + Work Items] --> B[Orchestrator<br/>DAG + eligibility + locks]
    B --> C1[Engineer A<br/>worktree A]
    B --> C2[Engineer B<br/>worktree B]
    B --> C3[Engineer C<br/>worktree C]
    C1 --> D1{Sensors A}
    C2 --> D2{Sensors B}
    C3 --> D3{Sensors C}
    D1 -- correctable --> C1
    D2 -- correctable --> C2
    D3 -- correctable --> C3
    D1 -- passed --> E[Orchestrator<br/>reconciles DAG]
    D2 -- passed --> E
    D3 -- passed --> E
    D1 -- limit/decision --> F[Escalation]
    D2 -- limit/decision --> F
    D3 -- limit/decision --> F
    E --> G[Single handoff to Red Team]
```

### Mission cycle

1. confirm baseline, Git status and writing scope;
2. read before editing and formulate the smallest change that satisfies the task;
3. implement affected code, tests and documentation;
4. execute sensors in the order defined by the harness and risk;
5. record commands, environment, results and artifacts in the evidence pack;
6. in case of correctable failure, explain the cause and delta of the next attempt before retry;
7. when passing, create trackable commit if authorized and issue envelope;
8. When exceeding limit or discovering new decision, stop and climb without loosening gate.

Orchestrator unblocks dependents only after step 7 and evidence persistence. Engineer's textual response does not satisfy dependency.

---

## Locks and competition containment

| Resource | Rule |
|---|---|
| Work Item | one active agent owner per mission |
| worktree | exclusive per Work Item; does not reuse worktree from another mission |
| file/contract | writer scope declared; overlay serializes or blocks |
| migration/schema | one writer per order of application; dependents await |
| external service | competition limited by politics and proven idempotence |
| board/status | reconciled by Orchestrator after Work Items, not freely edited by Engineers |

Changing outside of `write_scope` requires pausing and reviewing the mission. It is not enough for the file to be “necessary”; expansion changes risk, parallelism, and review.

---

## Authority boundaries

| Participant | Do | Doesn't |
|---|---|---|
| Orchestrator | agenda, limits competition, blocks dependents, gathers envelopes and state | writes code, closes technical criteria or approves changes |
| Software Engineer | implements a task in the designated worktree and tests local gates | changes SPEC/scope, loosens gate or uses pre-existing work without authorization |
| Human Tech Lead | resolves architecture, exception, permission, and risk above mission | has a presumed decision due to inactivity |

Changing verification to make the code pass is a separate mission and needs its own authorization. Author and approver remain different instances.

---

## Skills and minimal context

| Participant | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| Orchestrator | `dev-flow`, `update-docs` |
| Software Engineer | `implement`, `fix-bug`, `test-integration-local`, `dev-flow`, `commit` depending on the task |

Each envelope records `skills_used`. The Engineer only receives his task, necessary SPEC/contract excerpts, paths, criteria and gates; does not receive full memory or independent tasks. Adherent skill cannot be omitted without justification.

---

## Evidence per mission

The local evidence pack records, at a minimum:

- baseline and initial commit;
- changed files and resulting diff/commit;
- acceptance criteria → test/sensor → result;
- exact commands, environment and timestamps;
- failures of each attempt and delta applied;
- updated documentation or verifiable justification;
- out of scope, residual risks and requested decisions.

The practical test is independent reproduction. “Passed locally” without command, environment and raw result is not evidence.

---

## Persistence and closure

| Artifact | Destination | Writer |
|---|---|---|
| code, tests and docs | `repos/worktrees/<org>/<repo>/<WI-id>/` | Mission Engineer |
| Work Item | `projects/<project>/work-items/<WI-id>.md` | mission owner; authoritative source |
| evidence pack | `projects/<project>/execution/evidence/<WI-id>/` | Engineer; consolidated by links |
| round status | `.coordination/active/<mission-id>.md` | Orchestrator; traffic |
| validation handoff | `projects/<project>/execution/handoffs/` | Orchestrator |
| `STATUS.md`, `MEMORY.md`, `BOARD.md` | Tech Lead workspace | Authorized Orchestrator, after Work Items |

Order: persist individual evidence → update Work Item → reconcile DAG → update `STATUS.md`/memory when applicable → reconcile board → promote handoff → remove/reference transient state as per policy. Orchestrator lists changes and evidence; does not combine quest code on its own.

---

## Gates

### Gate per mission

- [ ] baseline, branch, base, worktree and scope correspond to the Work Item;
- [ ] change remains within the task or expansion has been authorized;
- [ ] criteria have reproducible tests/evidence;
- [ ] pre-commit/pre-push hooks required by the risk were executed;
- [ ] affected documentation has been updated;
- [ ] flaws were not hidden and gates were not weakened;
- [ ] commit is traceable when the mission authorizes commit.

### Round gate

- [ ] Final DAG distinguishes `completed`, `partial` and `blocked` by mission;
- [ ] dependents only advanced after persistent evidence;
- [ ] there was no writer scope or worktree collision;
- [ ] all envelopes inform `skills_used`, sources, outputs, risks and gates;
- [ ] Work Items, evidence packs, `STATUS.md` and board are reconciled;
- [ ] handoff to the Red Team covers baselines, diffs, checklist, attempts, pending issues and out of scope.

---

## Retry, failures and escalation

| Condition | Action |
|---|---|
| deterministic and correctable failure within scope | retry from the same Engineer, recording cause and delta |
| same cause after two attempts | block; scale with options and evidence |
| requirement contradicts code/contract | stop and return to Specification TL/Tech Lead |
| change requires new architecture or permission | block before action |
| circular dependency | Orchestrator interrupts the round and requests replanning |
| third-party local change or discovered collision | preserve state; do not overwrite; reassign/serialize |
| risk exceeds mission | Tech Lead decides expansion, mitigation or return |

Round can end `partial` with independent missions completed, as long as blocked dependents and impact are explicit. It does not deliver to the Red Team a composition that depends on work that does not yet exist.

---

## Final round envelope

```yaml
mission_id: "RALPH-BATCH-<id>"
workflow: "04-autonomous-implementation"
status: completed | partial | blocked
transition: ready_for_adversarial_validation | awaiting_dependency | escalated
baseline_spec: "<path@revision>"
missions:
  completed: []
  partial: []
  blocked: []
repositories_touched: []
worktrees: []
skills_used: []
outputs_created: []
commits: []
evidence_packs: []
dependency_changes: []
write_collisions: []
decisions_requested: []
risks: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`ready_for_adversarial_validation` means “ready to be attacked”, not approved.
