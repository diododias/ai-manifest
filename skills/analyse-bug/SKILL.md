---
name: analyze-bug
description: Analyzes evidence of a bug, traces root cause, and documents impact without implementing fixes. Use when receiving logs, prints, errors or descriptions of incorrect behavior.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Analyze the reported problem, track the root cause, identify affected components and generate structured documentation.

## Artifact contract

Before creating a report, follow [shared agreement](../references/workflow-contract.md).

## Inputs

- **Required:** evidence of the bug (log, print, description, error)
- **Optional:** additional context (when it happened, frequency, impact)

## Execution Steps

### 1. Collect evidence

- Collect all available information: logs, prints, stack traces, Description of expected vs. obtained behavior.
- If `$ARGUMENTS` is empty, ask the user for evidence.

### 2. Rate the bug

| Dimension | Option |
|----------|-----------|
| Severity | 🔴 Crash / 🟠 Functional / 🟡 UI / 🔵 Cosmetic |
| Impact | All users / Some / Edge case |
| Recurrence | Always / Flashing / Once |
| Component | Backend / Frontend / Infra / Database |

### 3. Track root cause

Analyze the evidence to identify:

- **Symptom:** what the user/system presents.
- **Immediate cause:** what in the code/config caused the symptom.
- **Root cause:** why the code/config was like this (lack of validation, race condition, etc.).

Use techniques:
- Stack trace → file → function → logic.
- Log analysis → sequence of events.
- Reproduction → steps to recreate.

### 4. Identify affected components

| Component | Archive | Function/Method | Impact |
|-----------|------------|---------------|---------|
| ... | ... | ... | ... |

### 5. Document the bug

Generate `bugs/bug-<NOME-SLUG>.md`:

```markdown
# Bug: <Title>

**ID:** BUG-<NNN>
**Date:** <YYYY-MM-DD>
**Severity:** 🔴/🟠/🟡/🔵
**Status:** 🟡 Analyzed

---

## Symptom

<what happens — observable behavior>

## Expected Behavior

<what should happen>

## Evidence

<logs, prints, stack traces — paste relevant excerpts>

## Root Cause

<technical analysis of why it happens>

## Affected Components

| Component | Archive | Function |
|-----------|------------|--------|
| ... | ... | ... |

## Steps to Reproduce

1. <step 1>
2. <step 2>
3. <step 3>

**Result:** <error/bug>
**Expected:** <correct behavior>

## Impact

- **Users:** <affects all/some/edge case>
- **Data:** <loss/corruption/data OK>
- **Performance:** <yes/no/light>

## Correction Suggestion

<fix direction — do not implement yet>

## References

- <related links, issues, PRs>
```

### 6. Report in chat

- Summary: symptom, root cause, severity.
- Affected components.
- Suggested correction path.
- If you need more information for a complete analysis.

## Conventions

- Never implement the fix — just analyze it.
- Document with evidence, not assumptions.
- Root cause is “why” — not “what” (symptom).
- Portuguese.

##DoneWhen

- [ ] Evidence collected and analyzed
- [ ] Root cause identified
- [ ] Affected components mapped
- [ ] `bug-<NOME>.md` generated in `bugs/`
- [ ] Summary reported in chat
