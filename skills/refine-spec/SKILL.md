---
name: refine-spec
description: Transforms an approved SPEC into a sequential plan for implementation, dependencies and tracking. Use before coding a feature to identify testable blocks and the safe order of execution.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Transform the SPEC into a step-by-step implementation plan, defining block order, dependencies and creating `tracking.md` to monitor execution.

## Artifact contract

Before creating a plan and tracking, follow [the shared contract](../references/workflow-contract.md).

## Inputs

- **Required:** `.agents/spec/<feature-slug>/SPEC.md`
- **Optional:** `.agents/prd/<feature-slug>/PRD.md` for context

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from SPEC.
- Check if the SPEC exists.

### 2. Load context

- Read `SPEC.md` in full — it's the technical plan.
- Read `PRD.md` if it exists — context of priorities.

### 3. Extract implementation blocks

From SPEC, extract:
- **Data models:** entities, relationships, migrations.
- **Services/business logic:** rules, validations, processing.
- **Interfaces/APIs:** endpoints, contracts.
- **Integrations:** external banks, queues, services.
- **Frontend (if applicable):** components, UI flows.

### 4. Define order of dependencies

Map dependencies between blocks:
- What needs to exist before what?
- Which blocks are independent (parallelizable)?
- What is the safest way to have something testable early?

### 5. Create sequential plan

Generates `teamwork/plan/feature-plan-<feature-slug>/plano-implementacao.md`:

```markdown
# Implementation Plan — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>
**SPEC:** .agents/spec/<feature-slug>/SPEC.md

---

## Implementation Sequence

### Block 1: <Name> (Foundation)
**Depends on:** None
**Files:** `path/to/file1`, `path/to/file2`
**What to do:**
1. <action 1>
2. <action 2>

**Test:** <how to validate this block>

---

### Block 2: <Name> (Core)
**Depends on:** Block 1
**Files:** `path/to/file3`
**What to do:**
1. <action 1>

**Test:** <how to validate>

---

### Block 3: <Name> (Parallelizable)
**Depends on:** Block 1
**Parallelizable with:** Block 4
**Files:** `path/to/file4`
**What to do:**
1. <action 1>

**Test:** <how to validate>

---

## Dependency Graph

```
Block 1 (Foundation)
├── Block 2 (Core)
├── Block 3 (Parallelizable) ─┐
└── Block 4 (Parallelizable) ─┘
                              └── Block 5 (Integration)
                                    └── Block 6 (Polishing)
```

## Safest Starting Point

<Block 1> — foundation without dependencies, allows immediate validation.

## Estimate

| Block | Effort | Dependencies |
|-------|--------|-------------|
| 1 | S | — |
| 2 | M | Block 1 |
| ... | ... | ... |

## Tracking

`tracking.md` will be created when starting the implementation.
```

### 6. Create tracking.md

Generate `teamwork/plan/feature-plan-<feature-slug>/tracking.md`:

```markdown
# Tracking — <Feature Name>

**Feature:** <slug>
**Start:** <YYYY-MM-DD>
**Status:** 🟡 In progress

---

## Progress

| Block | Status | Home | End | Notes |
|-------|--------|--------|-----|-------|
| 1 - Foundation | ⬜ Not started | — | — | |
| 2 - Core | ⬜ Not started | — | — | |
| 3 - ... | ⬜ Not started | — | — | |

**Caption:** ⬜ Not started | 🟡 In progress | ✅ Completed | ❌ Blocked

---

## Log

| Date | Event |
|------|--------|
| — | — |
```

### 7. Report in chat

- Summary: X blocks defined, Y dependencies mapped, Z parallelizable.
- Recommended starting point.
- Total estimate.

## Conventions

- Blocks organized by dependency order, not by file.
- Each block should be independently testable when possible.
- tracking.md is live — updated during implementation.
- Portuguese.

##DoneWhen

- [ ] `plano-implementacao.md` generated with sequenced blocks
- [ ] `tracking.md` created with initial status
- [ ] Mapped block dependencies
- [ ] Safest starting point identified
- [ ] Summary reported in chat
