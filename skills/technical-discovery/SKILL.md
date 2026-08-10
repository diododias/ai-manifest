---
name: technical-discovery
description: Prepares a technical vision based on the PRD, mapping components, dependencies, risks and open decisions. Use before a technical refinement agenda or writing a feature SPEC.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Generate the structured technical vision of the solution as a basis for discussion in the technical refinement agenda.

## Artifact contract

Before creating the technical view, follow [the shared agreement](../references/workflow-contract.md).

## Inputs

- **Required:** `.agents/prd/<feature-slug>/PRD.md`
- **Optional:** technical context of the team (existing architecture, stack, conventions)
- **Optional:** `requisitos.md` for additional context

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from the PRD.
- Check if the PRD exists.

### 2. Load context

- Read `PRD.md` — basis for technical analysis.
- Read `requisitos.md` if exists — additional business context.
- Identify existing stack, architecture and conventions in the repository.

### 3. Analyze technical impact

For each PRD story, evaluate:

- **Affected components:** which modules, services, APIs need to change.
- **External dependencies:** Third-party APIs, databases, queues.
- **Technical risks:** complexity, uncertainties, necessary spike.
- **Effort estimate:** relative (S/M/L/XL) based on complexity.

### 4. Map stack and decisions

- **Necessary technologies:** libs, frameworks, services.
- **Existing standards:** how to solve similar problems in the current code.
- **Open decisions:** points that require consensus for refinement.

### 5. Generate output

Create `teamwork/plan/feature-plan-<feature-slug>/visao-tecnica.md` in the format:

```markdown
# Technical Overview — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>
**PRD:** .agents/prd/<feature-slug>/PRD.md

---

## 1. Solution Summary

<high-level technical description of the approach>

## 2. Impact by Story

### HIST-01: <Title>

| Dimension | Detail |
|----------|------------|
| Components | <affected modules/services> |
| Dependencies | <External APIs, banks, queues> |
| Risk | 🟢 Low / 🟡 Medium / 🔴 High |
| Effort | S/M/L/XL |
| Open decisions | <what needs consensus> |

## 3. Stack and Technologies

| Need | Technology | Status |
|-------------|-----------|--------|
| ... | ... | Existing / New / Evaluate |

## 4. Standards and Conventions

- <repository standards that must be followed>
- <code conventions, tests, deployment>

## 5. Risks and Mitigations

| Risk | Impact | Mitigation |
|-------|--------|-----------|
| ... | ... | ... |

## 6. Questions for Refinement

- <points that require collective decision>
- <technical alternatives to consider>
- <dependencies on other teams>
```

### 6. Report in chat

- Summary: X components impacted, Y risks identified, Z open decisions.
- Risks of greater attention.
- Questions to lead to technical refinement.

## Conventions

- Internal Tech Lead document — not deliverable to the external team.
- Risk: 🟢 Low (known standard), 🟡 Medium (moderate complexity), 🔴 High (spike/uncertainty).
- Relative effort: S (< 1 day), M (1-3 days), L (3-5 days), XL (> 1 week).
- Portuguese.

##DoneWhen

- [ ] `visao-tecnica.md` created in `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] Each PRD story technically analyzed
- [ ] Documented open risks and decisions
- [ ] Summary reported in chat
