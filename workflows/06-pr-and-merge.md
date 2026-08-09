---
title: Workflow 06 — PR and merge
status: proposed
updated_at: 2026-08-09
---

# Workflow 06 — PR and merge

> [🚪 Gatekeeper Loop](../docs/loops/06-pr-and-merge.md) executable block: transforms a validated baseline into an auditable integration proposal and proves that only the approved head reached the protected branch.

The PR is a decision interface, not a second implementation or an evidence pack dump. It highlights behavior, hotspots, risk, evidence, exceptions, and rollback so that Code Owners can decide H4 without rebuilding previous work.

---

## Block result

A closed execution links Work Item, commits, PR, checks, reviews, H4 decision and merge result. The validated head, the approved head and the integrated head need to form a verifiable chain; Current remote state always takes precedence over local memory or snapshot.

| Layer | Closing condition |
|---|---|
| **Loop** | updated base, green required CI, valid approvals and resolved exceptions |
| **Agents** | PR Agent synthesized/routed; reviewers and Code Owners maintained independent authority |
| **Platform** | branch protection/ruleset was consulted and the merge occurred only by policy |
| **Workspace** | Work Item, internal review, `STATUS.md` and board reflect remote status |
| **Proof** | integrated commit is expected descendant/head on target branch or blocking is explicit |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 6 — construction and validation |
| **Execution unit** | one PR per coherent set of Work Items and validated baseline |
| **Consolidates** | [PR Agent](../agents/pr-agent/AGENT.md) |
| **Collaborate** | Reviewer Agents and Code Owners required by paths, risk and policy |
| **Human owner** | Code Owner or Tech Lead depending on branch protection and risk class |
| **Input** | validated commits/diff, evidence pack Red Team, checks, risk, base/head and publication authorization |
| **Exit** | Trackable PR, H4 review/decision and proven merge or reproducible block |
| **Content gate** | description, criteria, hotspots, risk, checks, rollback, out of scope and full links |
| **Integration Gate** | head current validated; IC green; updated base; valid approvals; no pending exception |
| **Dominant lap** | external — adjustment returns to Ralph Loop and revalidates in the Red Team |
| **Next workflow** | [07 — approval](07-release-candidate-validation.md), after proven merge |

---

## Remote Preflight

1. Resolve Work Item, repository, branch/base, commits and evidence pack; confirm authorization to open/update PR.
2. Consult current remote status: target branch, published head, existing PR, checks, reviews, conflicts and ruleset.
3. Prove that PR's `head_commit` is the same as the one validated by the Red Team. Divergence locks the opening as “ready”.
4. Identify Code Owners of paths, risk approvals, CI lanes and merge/auto-merge policy.
5. Detect duplicate PR for branch/Work Item before creating another one.
6. Confirm rollback plan, migrations/deployment order and sensitive files.
7. Register the transition to `review` and the PR identifier in the Work Item only after the platform confirms the operation.

### Opening envelope

```yaml
mission_id: "GATEKEEPER-<id>"
work_item_id: "<WI-id>"
workflow: "06-pr-and-merge"
repository: "<repo-id>"
base_branch: "<base>"
head_branch: "<head>"
validated_head: "<sha>"
validation_run_id: "<REDTEAM-id>"
risk: "<classe>"
required_checks: []
required_approvals: []
code_owners: []
permissions:
  open_or_update_pr: false
  enable_auto_merge: false
  merge: false
stop_conditions: []
```

---

## Mission plan

```mermaid
TD flowchart
    A[Head validated + evidence pack] --> B[PR Agent<br/>remote preflight]
    B --> C[PR Agent<br/>opens/updates PR + hotspots]
    C --> D1[CI Checks]
    C --> D2[Reviewer Agents]
    C --> D3[Code Owners]
    D1 --> E[PR Agent<br/>reconciles state]
    D2 --> E
    D3 --> E
    E --> F{New material commit?}
    F -- yes --> G[Ralph + Red Team]
    G --> C
    F -- no --> H{Gate H4/politics}
    H -- blocked --> I[Scaling]
    H -- approved --> J[Merge protected]
    J --> K[Try integration<br/>and update workspace]
```

| Mission | Responsible | Output |
|---|---|---|
| M1 — reconcile baseline | PR Agent | base/head/validation run and current policy |
| M2 — publish summary | PR Agent | title, behavior, risks, hotspots, evidence, rollback and out of scope |
| M3 — check | CI and Reviewer Agents | checks and comments in the current head |
| M4 — decide | Code Owners/Tech Lead | H4 or automatic result allowed by policy |
| M5 — integrate | authorized platform/actor | merge according to protected strategy |
| M6 — check | PR Agent | PR/commit/branch target and workspace reconciled |

Checks and reviews can occur in parallel, but their validity is indexed by `head_sha`. Any new commit opens a new validity review before the gate.

---

## PR Description Contract

The description summarizes:

1. problem and altered behavior;
2. Work Items, PRD/UX/SPEC and validated baseline;
3. acceptance criteria and link to corresponding evidence;
4. hotspots: paths/sections that concentrate risk and why;
5. tests/checks performed, without pasting extensive logs;
6. impact on data, contracts, security, observability and operation;
7. rollout/rollback and integration order when applicable;
8. out of scope, residual risks and exceptions with deadline;
9. owners requested and H4 decision required.

If the reviewer needs to reread all the sessions or repeat the Red Team, the synthesis has failed. If it cannot reach the raw result via link, it hides evidence.

---

## Invalidation by new head

| Change after review | What invalidates |
|---|---|
| formatting proven to have no behavior | only checks defined by policy; registered justification |
| code/test/configuration | approvals and evidence of affected paths/behaviors |
| dependency, contract, schema or migration | Matching Security/Architecture/QA/CI and possibly H3/H4 |
| scope/outcome/UX | returns to Studio/Drafting, is not absorbed into PR |
| rebase/merge the base with material difference | checks/revalidation defined by harness |

PR Agent calculates impact and routes; does not preserve approval for convenience.

---

## Authority boundaries

| Participant | Do | Doesn't |
|---|---|---|
| PR Agent | opens/updates authorized PR, summarizes, consults remotely, requests owners and reconciles | implement fix, approve own PR, declare CI for memory or merge without policy |
| Reviewer Agent | review the contract cut in the current head | replaces Code Owner or changes code silently |
| Code Owner/Tech Lead | decides H4 according to risk/policy | has approval inferred due to lack of response |
| platform | applies checks, ruleset and merge strategy | has result reinterpreted by agent without current consultation |

Author and approver identities remain distinct and are enforced by the platform, not just by prompt.

---

## Skills and minimal context

| Participant | Priority skills |
|---|---|
| PR Agent | `check-pr`, `update-pr`, `commit`, `dev-flow` |
| agents operating workspace | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| technical reviewer activated | review skills for the contract itself, already registered in the Red Team |

Each envelope records `skills_used`. The PR Agent receives consolidated evidence pack and hotspots; does not receive private memory or full logs unnecessarily.

---

## Persistence and proof of integration

| Artifact | Destination | Rule |
|---|---|---|
| PR, checks, approvals and merge | code platform | remote state current source |
| Work Item | `work-items/<WI-id>.md` | link, base/head, status and decision |
| internal review | `execution/reviews/pr-<WI-id>.md` | material comments, resolutions, H4 and merge proof |
| evidence pack | existing Red Team source, referenced | do not duplicate in description |
| pending exception | `.coordination/blockers/` until formal promotion | term, owner and compensation |
| `STATUS.md` and `BOARD.md` | workspace Tech Lead | updated after remote confirmation |

After the merge, record: PR, strategy, resulting commit, observed target branch, timestamp and proof of ancestry/contains. The action is only completed when the platform confirms it; Request sent is not equivalent to merge.

---

## Gates

### PR Gate

- [ ] PR references Work Item and current artifacts;
- [ ] `head_sha` corresponds to the validated baseline;
- [ ] description presents behavior, criteria, hotspots, risk, evidence, rollback and out of scope;
- [ ] base is updated according to policy and there is no conflict;
- [ ] required checks are green in the current head;
- [ ] required approvals/Code Owners are valid;
- [ ] no pending exceptions or open findings were hidden.

### Block execution gate

- [ ] remote status was consulted immediately before the decision;
- [ ] new commit invalidated and reopened corresponding checks/reviews;
- [ ] H4/auto-merge comply with the current risk class and autonomy;
- [ ] lack of response was not counted as approval;
- [ ] merge was executed by an authorized and proven actor/policy;
- [ ] Work Item, review, `STATUS.md` and board reflect the remote result.

---

## Failures and escalation

| Condition | Destination |
|---|---|
| comment requires code | Ralph Loop + Red Team revalidation |
| comment reveals incorrect scope/UX | StudioLoop |
| comment reveals architectural decision | Drafting Loop/H3 |
| approval required unavailable | `blocked`; owner defines replacement/deadline according to policy |
| Inconsistent or non-reproducible CI | scale with runs, commits and environments; blind retry does not approve |
| conflict between reviewers | Code Owner/Tech Lead decides with explicit divergence |
| policy exception | authorized owner, with term and compensation |
| branch diverged or remote head changed | interrupt and redo preflight |

---

## Final envelope

```yaml
mission_id: "GATEKEEPER-<id>"
work_item_id: "<WI-id>"
workflow: "06-pr-and-merge"
status: completed | partial | blocked
transition: merged_ready_for_rc | returned_for_rework | awaiting_h4 | escalated
repository: "<repo-id>"
pull_request: "<url-or-id>"
base_branch: "<base>"
validated_head: "<sha>"
approved_head: "<sha>"
merge_commit: "<sha-or-null>"
remote_state_checked_at: "<timestamp>"
skills_used: []
checks: []
approvals: []
exceptions: []
outputs_created: []
decisions_recorded: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`merged_ready_for_rc` requires remote proof of approved head merge; PR “mergeable” or successful command is not enough.
