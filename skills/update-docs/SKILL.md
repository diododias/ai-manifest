---
name: "update-docs"
description: "Compares implementation, PRD and SPEC, records deviations and updates approved documentation. Use after validation of a delivery when it is necessary to preserve traceability between planned and delivered."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Synchronize PRD and SPEC with what was effectively implemented, documenting deviations and updating documentation.

## Artifact contract

Follow [shared agreement](../references/workflow-contract.md). No
rewrite requirements, acceptance criteria, or approval status to accommodate
the code: record the divergence first and only update the baseline after decision
explicit.

## Inputs

- **Required:** `.agents/prd/<feature-slug>/PRD.md`
- **Required:** `.agents/spec/<feature-slug>/SPEC.md`
- **Required:** implemented code
- **Optional:** `teamwork/plan/feature-plan-<feature-slug>/tracking.md`

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from the context.
- Check if the artifacts exist.

### 2. Upload artifacts

- Read `PRD.md` — planned release.
- Read `SPEC.md` — planned technical release.
- Analyze the implemented code (diff).

### 3. Identify deviations

Compare planned vs implemented:

| Artifact | Item | Planned | Implemented | Deviation |
|----------|------|-----------|-------------|--------|
| PRD | HIST-01 | ... | ... | ✅ Same / ⚠️ Different / ❌ Not implemented |
| SPEC | CT-01 | ... | ... | ... |

Classify deviations:
- **No deviation:** implementation identical to planned.
- **Minor deviation:** adjustment that does not impact requirements (refactor, rename).
- **Scope creep:** implemented something more or less.
- **Technical deviation:** different approach than planned.
- **Not implemented:** planned item that was left out.

### 4. Update PRD after registered decision

- Record the result and the link to `desvios.md` in the changelog.
- Mark stories as implemented only if the agreed criteria have been met.
- For scope or requirement deviation, preserve the baseline and record the decision, owner and date before changing it.

### 5. Update SPEC after registered decision

- Record evidence of the implementation and the link to `desvios.md` in the changelog.
- Change the solution or CTs only with explicit technical decision; Don't silently turn a deviation into a requirement.

### 6. Update README (if applicable)

- If the feature changes visible behavior, update README.
- If you add a dependency, document it.
- If setup/instructions change, update.

### 7. Generate deviation report

Generates `teamwork/plan/feature-plan-<feature-slug>/desvios.md`:

```markdown
# Deviations — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>

---

## Summary

| Type | Quantity |
|------|-----------|
| ✅ No diversion | X |
| ⚠️ Minor deviation | X |
| 🔵 Scope creep | X |
| 🟣 Technical deviation | X |
| ❌ Not implemented | X |

---

## Detailed Deviations

### <Item>
- **Artifact:** PRD / SPEC
- **Item:** <ID or name>
- **Planned:** <what was planned>
- **Implemented:** <what was done>
- **Impact:** <what is the impact of the deviation>
- **Justification:** <why the deviation>

---

## Necessary Actions

- <pending updates>
- <docs that need updating>
```

### 8. Report in chat

- Summary: X items without deviation, Y with deviation, Z not implemented.
- Deviations that need attention.
- Updated docs.

## Conventions

- Deviations are never deleted — documented for traceability.
- PRD and SPEC are sources of truth — they must reflect real implementation.
- Portuguese.

##DoneWhen

- [ ] PRD updated with status and deviations
- [ ] SPEC updated with status and deviations
- [ ] Updated README (if applicable)
- [ ] `desvios.md` generated
- [ ] Result reported in chat
