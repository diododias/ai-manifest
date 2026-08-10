---
title: Workflow 07 — release candidate approval
status: proposed
updated_at: 2026-08-09
---

# Workflow 07 — release candidate approval

> [🎭 Rehearsal Loop](../docs/loops/07-release-candidate-validation.md) executable block: proves in a representative environment that the integrated artifact delivers the approved product and experience behavior.

Approval does not repeat code review. It compares promise and reality using the same immutable artifact that can make it into production. Release Agent prepares and checks the environment; Product Validation Agent consolidates the acceptance matrix; PM and UX keep the decision human.

---

## Block result

A closed run exactly identifies the release candidate, environment, data, criteria, and evidence. Each difference is classified as a defect, scope/experience gap, environment limitation or accepted risk; no absence becomes informal approval.

| Layer | Closing condition |
|---|---|
| **Loop** | product/UX criteria executed in a representative environment |
| **Agents** | Release has proven provenance/environment; Product Validation consolidated without giving human acceptance |
| **Workspaces** | PM, UX and Tech Lead persisted evidence in their own domains, linked by RC/Work Item |
| **Artifact** | digest/approved version is the same as the one eligible for production; there was no rebuild |
| **Decision** | owners accepted RC or registered return/pending with owner and deadline |

---

## Operating contract

| Contract | Definition |
|---|---|
| **Step** | 7 — release and operation |
| **Execution unit** | an immutable release candidate identified by `release_candidate_id` and digest |
| **Consolidates** | [Product Validation Agent](../agents/product-validation-agent/AGENT.md) |
| **Prepares environment** | [Release Agent](../agents/release-agent/AGENT.md) |
| **Human Owners** | PM for value; UX for experience; stakeholder only when defined in the criteria |
| **Input** | integrated artifact, PRD, UX spec, criteria, environment, secure data, risk and technical evidence |
| **Exit** | approval report/matrix, environmental evidence, demo and approved/returned RC |
| **Content gate** | each criterion validated or classified with an explicit plan; differences and limitations recorded |
| **Block Gate** | content + immutable provenance + proven environment/data + multiworkspace state + human decision |
| **Dominant lap** | external — defect returns to Ralph; scope/UX gap returns to Studio |
| **Next workflow** | [08 — production and observation](08-production-release-and-observation.md) |

---

## Release candidate preflight

1. Resolve Work Item, PR/merge, release candidate, version/digest, source and signature when applicable.
2. Prove that the candidate was produced from the integrated commit and that the promotion mechanism does not require rebuild.
3. Resolve approved PRD and UX spec, criteria and reviews used in Gatekeeper.
4. Prepare environment manifest: version, relevant configuration, dependencies, flags, migrations and known differences in relation to production.
5. Provision synthetic/anonymized data and secure permissions; Sensitive real data is not copied for convenience.
6. Define execution matrix, owners and stopping condition; Insufficient environment or criteria blocks before “accept”.
7. Create common `mission_id` and evidence folders in the three workspaces.

### Opening envelope

```yaml
mission_id: "REHEARSAL-<id>"
work_item_id: "<WI-id>"
workflow: "07-release-candidate-validation"
release_candidate:
  id: "<RC-id>"
  version: "<version>"
  digest: "<digest>"
  source_commit: "<sha>"
environment:
  id: "<preview-or-staging>"
  manifest: "<path>"
criteria:
  product: []
  ux: []
risk: "<classe>"
permissions: []
stop_conditions: []
```

---

## Mission plan

```mermaid
TD flowchart
    A[immutable RC + criteria] --> B[Release Agent<br/>provenance, environment and data]
    B --> C1[Product Validation<br/>product, smoke and E2E]
    B --> C2[Product Validation<br/>UX, states and accessibility]
    C1 --> D[Consolidate matrix<br/>criterion-evidence]
    C2 --> D
    D --> E{Differences?}
    E -- defect --> F[Ralph + Red Team + Gatekeeper]
    E -- scope/UX --> G[Studio Loop]
    E -- environment --> H[Correct environment and repeat]
    E -- none/bounded --> I[PM + UX decide RC]
    I -- approved --> J[Handoff to Canary Loop]
```

| Mission | Responsible | Output |
|---|---|---|
| M1 — prepare RC | ReleaseAgent | proof of provenance, environment manifest, data and deployment smoke |
| M2 — validate product | Product Validation Agent | outcome, requirements, smoke/E2E and functional differences |
| M3 — validate experience | Product Validation Agent, consulting UX | flows, states, content, accessibility and visual comparison when applicable |
| M4 — consolidate | Product Validation Agent | criterion-evidence matrix and classification of differences |
| M5 — demonstrate | Release + Product Validation | proportional demo/recording, without replacing evidence |
| M6 — decide | Human PM and UX | approve RC, return, accept authorized pending or close |

M2 and M3 can run in parallel against the same RC/manifest, but write reports per domain. The consolidated matrix references both and never silently chooses between conflicting criteria.

---

## Provenance and representation

The gate checks two different properties:

| Property | Minimum proof |
|---|---|
| **immutability** | digest, source commit and build/promotion record link merge → RC → future release |
| **representativeness** | differences in config, data, services, flags, migrations and scale are enumerated and evaluated |

An environment can be representative without being identical; the difference needs to be known and not invalidate the tested criterion. Reconstructed artifact, “equivalent” by description or without digest does not pass.

---

## Classification of differences

| Class | Example | Return |
|---|---|---|
| implementation defect | behavior violates SPEC/approved criteria | Ralph → Red Team → Gatekeeper → new RC |
| product gap | expected behavior was never defined | Studio Loop / PM |
| experience gap | state, content or recovery missing from baseline | Studio Loop / UX |
| environment limitation | integration/data/config prevents proof | Release Agent corrects environment; repeat only affected criteria |
| known residual risk | difference accepted within authority | formal decision with owner, deadline and observation in production |

Product Validation recommends; does not change code, requirements or UX to “get it through”.

---

## Skills and minimal context

| Agent | Priority skills |
|---|---|
| all | `workspace-memory`, `workspace-projects`, `workspace-board` depending on operation |
| Product Validation | `review-prd`, `review-cross-prd-spec`, `update-docs` |
| ReleaseAgent | `check-pr`, `update-pr`, `dev-flow`, `update-docs` |

Each envelope records `skills_used`. Product Validation receives RC, criteria and links; Release receives provenance, environment and strategy. Sensitive data and private memory do not cross workspaces.

---

## Multiworkspace persistence

| Artifact | Canonical source | Writer |
|---|---|---|
| product matrix and recommendation | `<pm-workspace>/projects/<project>/validation/<WI-id>.md` | Product Validation Agent |
| UX validation | `<ux-workspace>/projects/<project>/validation/<WI-id>.md` | Product Validation Agent in the UX domain |
| manifest/environment evidence | `<tech-lead-workspace>/projects/<project>/execution/evidence/<WI-id>/release-candidate/` | ReleaseAgent |
| demo/recording | `<pm-workspace>/projects/<project>/validation/assets/<RC-id>/` | Product Validation/Release |
| owner decisions | PM/UX decision sources linked to the matrix | corresponding owner |
| release handoff | `.coordination/handoffs/` until promotion | ReleaseAgent; points to RC and sources |

Closing: persist technical/UX evidence → consolidate PM matrix → record decisions → update Work Items/`STATUS.md` in each domain → reconcile boards → promote release handoff.

---

## Gates

### RC Gate

- [ ] RC version/digest/source commit are verifiable and promoteable without rebuild;
- [ ] environment and differences for production are documented;
- [ ] test data is safe and sufficient;
- [ ] each PRD and UX criterion has a procedure, result and evidence;
- [ ] applicable success, failure, recovery and accessibility states have been exercised;
- [ ] differences were classified and not hidden by favorable demo.

### Block execution gate

- [ ] Release and Product Validation preserved their limits;
- [ ] PM/UX/Tech Lead persisted only in the corresponding domains;
- [ ] new RC invalidated previous candidate's results;
- [ ] accepted pending issue has owner, deadline, risk and observation plan;
- [ ] Work Items, matrices, evidence, status and boards are coherent;
- [ ] human approval references the exact RC/digest.

---

## Returns and scaling

| Condition | State/destination |
|---|---|
| insufficient environment/data | `blocked`; Release/owner fixes precondition |
| missing criteria or undefined behavior | StudioLoop; informal approval prohibited |
| reproducible defect | Ralph Loop with setting, impact and evidence |
| divergent experience | UX decides baseline correction or implementation |
| scope change | PM decides and related H2 is reopened |
| stakeholder disagrees without criteria | record feedback; PM/UX decide whether to change baseline |

---

## Final envelope

```yaml
mission_id: "REHEARSAL-<id>"
work_item_id: "<WI-id>"
workflow: "07-release-candidate-validation"
status: completed | partial | blocked
transition: approved_for_release | returned_to_implementation | returned_to_planning | environment_blocked
release_candidate:
  id: "<RC-id>"
  digest: "<digest>"
  source_commit: "<sha>"
environment_manifest: "<path>"
agents_run: []
workspaces_touched: []
skills_used: []
criteria:
  passed: []
  failed: []
  not_testable: []
differences: []
accepted_pendencies: []
decisions_recorded: []
outputs_created: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

`approved_for_release` requires human decision linked to approved digest; “green environment” does not replace product/UX acceptance.
