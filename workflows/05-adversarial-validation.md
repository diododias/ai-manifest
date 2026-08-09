---
title: Workflow 05 — adversarial validation
status: proposed
updated_at: 2026-08-09
---

# Workflow 05 — adversarial validation

> [⚔️ Red Team Loop](../docs/loops/05-adversarial-validation.md) executable block: independent perspectives attack change in parallel and converge into a reproducible evidence pack, without allowing the consolidator to silence findings.

The author demonstrated that change can work; this workflow looks for how it fails. Coverage comes from `CHECKLIST.md`, contracts, and risk — not from tests chosen by the implementer.

---

## Block result

A closed round classifies each criterion as `passed`, `failed` or `not_testable` with reason, records findings by domain and proves revalidations. The QA Agent assembles the single view, but the source reviewer maintains authority over the finding itself.

| Layer | Closing condition |
|---|---|
| **Loop** | Mandatory coverage executed and no blockers open |
| **Agents** | QA, Code, Security and Architecture acted with independence and explicit boundaries |
| **Repository/CI** | validated diff and baseline correspond to the commits that will follow the PR |
| **Workspace** | reviews, evidence pack, Work Item, `STATUS.md` and board are reconciled |
| **Return** | material correction invalidates only affected evidence and returns to Ralph Loop with reproducible finding |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 5 — construction and validation |
| **Execution unit** | immutable set of commits/diffs by Work Item and `validation_run_id` |
| **Consolidates** | [QA & Validation Agent](../agents/qa-validation-agent/AGENT.md) |
| **Reviewers** | [Security Review](../agents/security-review-agent/AGENT.md); [Architecture Review](../agents/architecture-review-agent/AGENT.md); [Adversarial Code Reviewer](../agents/adversarial-code-reviewer-agent/AGENT.md) |
| **Human Owners** | Tech Lead; PM/UX for ambiguities in the criteria themselves; Security Owner for matching exceptions |
| **Input** | diff/commits, PRD, UX spec, SPEC, CHECKLIST, local evidence, risk and path matrix |
| **Exit** | independent reviews, criteria-evidence matrix, findings, CI and gate recommendations |
| **Content gate** | all mandatory checks approved and no blocking findings open |
| **Block Gate** | content + independence + stable baseline + reproducible evidence pack + reconciled state |
| **Dominant lap** | medium/outer — fixes return to Ralph Loop and CI runs lanes by risk/path |
| **Next workflow** | [06 — PR and merge](06-pr-and-merge.md) |

---

## Validation preflight

1. Fix `validation_run_id`, Work Item, repositories, commits/base and exact diff. New material commit invalidates the affected run.
2. Confirm that the author/implementing instance will not be used as an independent reviewer.
3. Read PRD, UX spec, SPEC, CHECKLIST, ADRs, policies and local evidence packs; record reviews.
4. Derive coverage matrix by requirement, path and risk class.
5. Select mandatory reviewers by policy. `not_applicable` requires path/risk-based justification; It is not a silent omission.
6. Resolve environments and permissions. Destructive testing, production or sensitive data requires specific authorization.
7. Create separate review files; No reviewer edits other people's code or reviews.

### Opening envelope

```yaml
validation_run_id: "REDTEAM-<id>"
work_item_id: "<WI-id>"
workflow: "05-adversarial-validation"
baseline:
  base_commit: "<sha>"
  head_commit: "<sha>"
  spec: "<path@revision>"
  checklist: "<path@revision>"
repositories: []
paths_changed: []
risk: "<classe>"
required_reviewers: []
required_ci_lanes: []
permissions: []
stop_conditions: []
```

---

## Mission plan

```mermaid
TD flowchart
    A[Immutable Baseline + CHECKLIST] --> B1[QA<br/>criteria and scenarios]
    A --> B2[Security<br/>threats and data]
    A --> B3[Architecture<br/>borders and contracts]
    A --> B4[Code Reviewer<br/>correctness and maintenance]
    B1 --> C[QA<br/>matrix + evidence pack]
    B2 --> C
    B3 --> C
    B4 --> C
    C --> D[CI<br/>fast/deep lanes]
    D --> E{Block gate}
    E -- finding fixable --> F[Ralph Loop]
    F --> G[Revalidate affected domains]
    G --> C
    E -- exception/divergence --> H[Human owner]
    E -- approved --> I[Gatekeeper Loop]
```

| Mission | Responsible | Independent cropping | Output |
|---|---|---|---|
| M1 — functional coverage | QA Agent | nominal, error, recovery, limit, integration, E2E, reachability and regression | criterion-evidence matrix and reproducible failures |
| M2 — security | Security Review | SAST, dependencies, secrets, authn/authz, input, privacy and abuse | domain findings and exceptions |
| M3 — architecture | Architecture Review | borders, direction of dependence, ADRs, contracts and ownership | violations/architectural recommendation |
| M4 — code | Adversarial Code Reviewer | correctness, concurrency, error, compatibility, maintenance, tests and docs | actionable comments by severity |
| M5 — consolidation | QA Agent | assembly, not a verdict on someone else's review | single evidence pack and explicit gaps |
| M6 — CI | automation | lanes required by risk/path | raw results linked to baseline |
| M7 — revalidation | source reviewer + QA | only domains/evidence invalidated by the fix | finding resolved, open or exception |

M1–M4 run in parallel against the same baseline. If any mission changes the code, its independence has been broken and the run must be discarded/reopened.

---

## Ownership of findings

Every finding has a stable ID, reviewer, location, scenario, evidence, severity, impact, suggested action and status.

| Status | Who can assign | Requirement |
|---|---|---|
| `open` | source reviewer | sufficient evidence and reproduction |
| `resolved` | origin reviewer after revalidation | link to correction and new evidence |
| `exception` | authorized human owner | justification, deadline, compensation and residual risk |
| `false_positive` | source reviewer or policy owner | proof of inapplicability, never author preference |

QA does not close Security, Architecture or Code Review findings. Divergence without an objective rule remains in the evidence pack and scale.

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| QA | `test-integration-local`, `analyse-bug`, `update-docs` |
| Security | `code-review`, `technical-discovery`, `analyse-bug` |
| Architecture | `review-spec`, `code-review`, `technical-discovery` |
| Code Reviewer | `code-review`, `review-spec`, `analyse-bug` |

Each envelope records `skills_used`. Reviewers receive the same baseline and only the policies/contexts necessary for the domain. Results and author logs are secondary reference, not a substitute for independent reproduction.

---

## Criterion-evidence matrix

QA consolidates without over-summarizing:

| Criterion | Baseline | Procedure | Environment | Result | Evidence | Reviewer | Status |
|---|---|---|---|---|---|---|---|
| `<CHECK-id>` | `<sha>` | exact command/scenario | version/configuration | observed | raw link | agent | passed/failed/not_testable |

`not_testable` never equates to approved; records motive, impact and requested decision. The evidence pack must allow reproduction without conversation with the author or QA.

---

## Invalidation and revalidation

A material fix creates new `head_commit` and invalidates:

- tests that executed changed code/paths;
- findings whose reproduction depends on modified behavior;
- CI lanes whose input has changed;
- security/architectural conclusions affected by the new contract.

QA produces an impact map and requests proportional revalidation. Unaffected evidence can be preserved with justification and explicit composite baseline; copying the green status from the previous run is prohibited.

---

## Persistence and closing order

| Artifact | Destination | Writer |
|---|---|---|
| code review | `execution/reviews/code-<WI-id>.md` | Code Reviewer |
| security review | `execution/reviews/security-<WI-id>.md` | Security Reviewer |
| architecture review | `execution/reviews/architecture-<WI-id>.md` | Architecture Reviewer |
| consolidated evidence pack | `execution/evidence/<WI-id>.md` | QA Agent |
| reproducible logs/artifacts | `execution/evidence/<WI-id>/` | agent/production automation |
| Work Item | `work-items/<WI-id>.md` | authorized owner; links and status |
| active exceptions | `.coordination/blockers/` until decision/promotion | executor |
| `STATUS.md` and `BOARD.md` | workspace Tech Lead | authorized executor, after Work Item |

Order: persist individual reviews → generate matrix/evidence pack → incorporate CI → revalidate resolutions → update Work Item → `STATUS.md` → board → handoff to PR Agent. Open finding in any review blocks the gate.

---

## Gates

### Adversarial gate

- [ ] every mandatory item in the CHECKLIST is `passed`, `failed` or `not_testable` with reason;
- [ ] nominal scenarios, failures, recovery, thresholds and regression were independently derived;
- [ ] mandatory reviewers acted or have `not_applicable` justified;
- [ ] findings bring location, setting, consequence and reproduction;
- [ ] CI required by risk/path passed the same baseline;
- [ ] no blocker remains `open`.

### Block execution gate

- [ ] reviewer and implementer are independent instances;
- [ ] reviews were written separately and QA did not change other people's verdicts;
- [ ] material corrections had impact and revalidation recorded;
- [ ] evidence pack reproduces the verification and references raw results;
- [ ] Work Item, reviews, evidence, `STATUS.md` and board are coherent;
- [ ] handoff carries exact baseline, residual risks and valid exceptions.

---

## Returns and scaling

| Condition | Destination |
|---|---|
| correctable defect | Ralph Loop, with finding and playback |
| missing or ambiguous product/UX requirement | StudioLoop |
| inadequate contract/SPEC | Drafting Loop |
| false positive or divergence without rule | Tech Lead/policy owner |
| risk exception | authorized owner, with term and compensation |
| environment prevents mandatory testing | `blocked`; does not convert into approval |
| critical vulnerability/exposed data | Stop Testing, Securely Preserve Evidence, and Scale Immediately |

---

## Final envelope

```yaml
validation_run_id: "REDTEAM-<id>"
work_item_id: "<WI-id>"
workflow: "05-adversarial-validation"
status: completed | partial | blocked
transition: ready_for_pr | returned_to_implementation | returned_to_specification | escalated
baseline:
  base_commit: "<sha>"
  head_commit: "<sha>"
reviewers_run: []
reviewers_not_applicable: []
skills_used: []
outputs_created: []
checklist:
  passed: []
  failed: []
  not_testable: []
findings:
  open: []
  resolved: []
  exceptions: []
ci_lanes: []
evidence_invalidated: []
decisions_requested: []
risks: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`ready_for_pr` requires that the validated head is exactly the head delivered to the Gatekeeper Loop.
