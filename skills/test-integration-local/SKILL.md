---
name: "test-integration-local"
description: "Creates missing coverage and performs local validation with traceable evidence. Use after implementing a feature or fix, when you need to map acceptance criteria to tests and report results."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Perform complete validation of the implemented code — unit tests, mutation, coverage — and generate evidence that the acceptance criteria are met.

## Artifact contract

Before writing evidence, please follow [the shared agreement](../references/workflow-contract.md).

## Inputs

- **Required:** implemented code (local repository)
- **Required:** `.agents/spec/<feature-slug>/SPEC.md` (acceptance criteria)
- **Required:** `teamwork/plan/feature-plan-<feature-slug>/plano-implementacao.md`
- **Optional:** `teamwork/plan/feature-plan-<feature-slug>/tracking.md`

## Execution Steps

### 1. Identify testing scope

- Read the SPEC to extract technical acceptance criteria (CT-XX).
- Read the implementation plan to identify implemented blocks.
- Identify modified/created files.

### 2. Generate test cases

For each technical acceptance criterion (CT-XX) without coverage:

- Create unit test that validates the criteria.
- Follow existing test patterns in the repository.
- Name it following the project convention.

For exception flows:
- Test error paths documented in SPEC.
- Test validations, limits and edge cases.

### 3. Run unit tests

```bash
# Detectar e executar testes do projeto
# Exemplos por ecossistema:
# Node.js: npm test / pnpm test / yarn test
# Python: pytest / python -m pytest
# Go: go test ./...
# Rust: cargo test
```

- Run all tests, not just new ones.
- Check for regressions.

### 4. Check coverage (if available)

```bash
# Exemplos:
# Node.js: npx jest --coverage
# Python: pytest --cov
# Go: go test -cover ./...
# Rust: cargo tarpaulin
```

- Verify that modified files have adequate coverage.
- Identify untested lines/branches.

### 5. Mutation testing (if available)

```bash
# Exemplos:
# Node.js: npx Stryker run
# Python: mutmut run
```

- Validate that tests actually test (not just pass).
- Fix tests that don't kill mutations.

### 6. Self-check of acceptance criteria

For each CT (technical criterion) and its related business CA, when applicable:

| CT | Related CA | Criterion | Status | Evidence |
|----|---------------|----------|--------|-----------|
| CT-01 | CA-01 | <description> | ✅ / ❌ | <test that validates> |
| CT-02 | CA-02 | <description> | ✅ / ❌ | <test that validates> |

### 7. Generate evidence

Create `teamwork/plan/feature-plan-<feature-slug>/evidencias-teste.md`:

```markdown
# Test Evidence — <Feature Name>

**Feature:** <slug>
**Date:** <YYYY-MM-DD>

---

## Test Result

### Unitary
- **Command:** `<executed command>`
- **Result:** ✅ X passing / ❌ Y failing
- **Coverage:** XX%

### Mutation (if applicable)
- **Command:** `<executed command>`
- **Score:** XX% (X killed / Y total)

### Regression
- **Existing tests:** ✅ All passing / ❌ Failures

---

## Coverage by Acceptance Criteria

| CT | Related CA | Criterion | Test | Status |
|----|---------------|----------|-------|--------|
| CT-01 | CA-01 | ... | test_name | ✅ |
| CT-02 | CA-02 | ... | test_name | ✅ |

---

## Modified and Covered Files

| Archive | Lines | Coverage |
|---------|--------|-----------|
| ... | ... | XX% |

---

## Pending

- <tests that could not be run>
- <justified missing coverage>
```

### 8. Report in chat

- Summary: X tests passing, Y failing, Z coverage.
- Acceptance criteria met vs pending.
- Ready for code review or needs adjustments.

## Conventions

- Tests follow the repository standard.
- Evidence is persistent — it stays in the repository.
- Self-check is mandatory before opening PR.
- Portuguese for documentation, English for test code.

##DoneWhen

- [ ] Unit tests run and passing
- [ ] Verified coverage (if tool available)
- [ ] Self-checked acceptance criteria with evidence
- [ ] `evidencias-teste.md` generated
- [ ] Regression checked (existing tests passing)
- [ ] Result reported in chat
