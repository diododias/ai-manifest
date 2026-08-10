---
name: create-spec
description: Creates a technical SPEC from PRD, technical vision and refinement decisions. Use after technical refinement when implementation requires traceable components, contracts, risks, and technical criteria.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Generate the SPEC Plan consolidating the detailed technical solution for each story, with technical acceptance criteria and implementation plan.

## Artifact contract

Before creating the SPEC, follow [the shared contract](../references/workflow-contract.md).

## Inputs

- **Required:** `.agents/prd/<feature-slug>/PRD.md`
- **Required:** `teamwork/plan/feature-plan-<feature-slug>/visao-tecnica.md`
- **Mandatory:** transcription of the technical agenda
- **Optional:** `teamwork/plan/feature-plan-<feature-slug>/historias.md`

## Execution Steps

### 1. Find the feature

- If `$ARGUMENTS` contains slug, use it. Otherwise, infer from artifacts.
- Check if the input files exist.

### 2. Load context

- Read `PRD.md` — requirements and stories.
- Read `visao-tecnica.md` — preview technical analysis.
- Read the transcript of the technical agenda — decisions and discussions.
- Read `historias.md` if it exists — additional context.

### 3. For each story, define the technical solution

Structure:

- **Technical approach:** how to solve (patterns, algorithms, integrations).
- **Components:** files, modules, classes, endpoints to create/modify.
- **Implementation flow:** order of changes, internal dependencies.
- **Technical acceptance criteria:** unit tests, integration, performance.
- **Data:** models, migrations, validations.

### 4. Define interface contract (if applicable)

For APIs, endpoints, or contracts between modules:
- Request/response format
- Validations
- Error codes

### 5. Generate output

Create `.agents/spec/<feature-slug>/SPEC.md` (create directories if necessary) in the format:

```markdown
# SPEC — <Feature Name>

**Feature:** <slug>
**Status:** 🟡 Under review
**Date:** <YYYY-MM-DD>
**PRD:** .agents/prd/<feature-slug>/PRD.md
**Author:** Tech Lead (via create-spec)

---

## 1. Solution Overview

<consolidated technical description of the approach>

## 2. Stack and Dependencies

| Need | Technology | Version | Status |
|-------------|-----------|--------|--------|
| ... | ... | ... | Existing / New |

## 3. Data Model

### Entities

#### <Entity>
| Field | Type | Validation | Mandatory |
|-------|------|-----------|-------------|
| ... | ... | ... | Yes/No |

### Relationships
<description of relationships between entities>

### Migrations
<structure of necessary migrations>

## 4. Solution by Story

### HIST-01: <Title>

#### Components
| Archive | Type | Action |
|---------|------|------|
| ... | ... | Create / Modify |

#### Implementation Flow
1. <step 1>
2. <step 2>

#### Technical Acceptance Criteria
- [ ] CT-01: <testable technical criterion>
- [ ] CT-02: <testable technical criterion>

#### Tests
- Unitary: <what to test>
- Integration: <what to test>

---

## 5. Interface Agreements (if applicable)

### <Endpoint/Interface>
**Method:** GET/POST/...

**Request:**
```json
{ ... }
```

**Response:**
```json
{ ... }
```

**Errors:**
| Code | Description |
|-----------|-----------|
| ... | ... |

---

## 6. General Implementation Flow

### Phase 1: Setup
<initialization, configs, dependencies>

### Phase 2: Fundamental Components
<models, services, middleware>

### Phase 3+: By History
<stories in order of dependency>

## 7. Technical Risks

| Risk | Impact | Mitigation |
|-------|--------|-----------|
| ... | ... | ... |

## 8. Validation

### Validation Scenarios
<quickstart: how to prove it works end-to-end>

## 9. Gaps and Issues

| ID | Description | Status |
|----|-----------|--------|
| ... | ... | ⏳ Open |
```

### 6. Report in chat

- Summary: X stories with a defined solution, Y components to create/modify, Z tests planned.
- Technical risks require greater attention.
- Ready for `review-spec`.

## Conventions

- SPEC is the technical contract — it should be enough for an engineer to implement without questions.
- CT-XX for technical acceptance criteria.
- Status: 🟡 Under review → 🟢 Approved → ✅ Implemented.
- Portuguese. Code and technical names in English.

##DoneWhen

- [ ] `SPEC.md` created in `.agents/spec/<feature-slug>/`
- [ ] Each PRD story with a defined technical solution
- [ ] Documented data model
- [ ] Defined interface agreements (if applicable)
- [ ] Sequenced implementation flow
- [ ] Summary reported in chat
