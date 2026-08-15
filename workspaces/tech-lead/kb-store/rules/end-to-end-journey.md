---
title: Agent Team — journey flow
status: reference
updated_at: 2026-08-08
---

# Agent Team — journey flow

> Visual view of [human trio operating system](../rules/operating-model.md) and [90/10 operating model](operating-model-90-10.md) · [Phase-separated flows](journey-by-phase.md) · [multi-agent workflows](../../../../workflows/README.md).

Each stage with collaboration between agents has a detailed contract in the [workflow map](../../../../workflows/README.md): [intake](../../../../workflows/00-intake-and-triage.md), [discovery](../../../../workflows/01-discovery-and-research.md), [product and UX](../../../../workflows/02-product-and-ux-planning.md), [specification](../../../../workflows/03-technical-specification.md), [implementation](../../../../workflows/04-autonomous-implementation.md), [validation](../../../../workflows/05-adversarial-validation.md), [PR](../../../../workflows/06-pr-and-merge.md), [approval](../../../../workflows/07-release-candidate-validation.md), [production](../../../../workflows/08-production-release-and-observation.md), [knowledge](../../../../workflows/09-knowledge-curation.md) and [continuous improvement](../../../../workflows/10-continuous-improvement.md).

## Development journey

```mermaid
TD flowchart
    START([Need, problem or opportunity])

    subgraph PRODUCT["Product and discovery"]
        S0["0. Backlog and triage<br/>Intake Agent + Product Manager Agent"]
        G0{{"Automatic gate<br/>context, owner, duplicity and risk"}}

        S1["1. Discovery<br/>PM + UX Specification + Tech Lead"]
        G1{{"Automatic gate<br/>Complete PB, evidence and risks"}}
        H1{"H1 · Is it worth investing?"}

        S2["2. Product Planning<br/>PM + Adversarial PM"]
        G2{{"Automatic gate<br/>Clear, testable and traceable PRD"}}
        H2{"H2 · Is this what we will build?"}
    end

    subgraph DESIGN["Decision and technical specification"]
        S3["3. Technical Specification<br/>Specification TL + Adversarial TL"]
        G3{{"Automatic gate<br/>SPEC, ADR, tasks, risks and trade-offs"}}
        D3{"Is there a new ADR,<br/>exception or risk R3/R4?"}
        H3{"H3 · Do we accept<br/>the trade-offs?"}
    end

    subgraph BUILD["Autonomous construction and validation"]
        S4["4. Implementation<br/>Orchestrator + Engineer Agents"]
        L4{{"Local hooks<br/>pre-commit + pre-push"}}
        S5["5. Adversarial validation<br/>QA + Security + Architecture + Reviewer Agents"]
        G5{{"CI fast + deep lanes<br/>all checks required"}}
    end

    subgraph DELIVERY["Integration, approval and production"]
        S6["6. PR + evidence pack<br/>PR Agent + Reviewer Agents"]
        H4{"H4 · Can we integrate?"}
        M6["Protected merge<br/>ruleset + checks + approvals"]

        S7["7. Automated approval<br/>preview, smoke, E2E and evidence"]
        G7{{"Release candidate gate<br/>validated acceptance criteria"}}

        D8{"R3/R4 risk or<br/>critical exposure?"}
        H5{"H5 · Can we expose<br/>the risk in production?"}
        S8["8. Production<br/>progressive rollout + rollback"]
        G8{{"Post-deploy gate<br/>SLOs, errors and product metrics"}}
    end

    subgraph LEARNING["Knowledge and continuous improvement"]
        S9["9. Knowledge base<br/>Knowledge Agent"]
        NOTE["Sessions + feedback + metrics<br/>failures + retries + escalations"]
        CLOCK([Weekly run])
        S10["10. Auto Dream<br/>continuous work system analysis"]
        D10{"Sensitive memory, P0/P1<br/>or gate change?"}
        H6{"H6 · Did the system learn<br/>correctly?"}
        LEARN{"Result type"}
        MEM["Learning validated<br/>update MEMORY.md"]
        IMP["Failure or friction<br/>generate demand for improvement"]
        TYPES["Process · harness · skill · script<br/>gate · automation · flow"]
    end

    END([Cycle delivered and observed])

    START --> S0 --> G0
    G0 -- "approved" --> S1
    G0 -- "incomplete" --> S0

    S1 --> G1
    G1 -- "approved" --> H1
    G1 -- "gap" --> S1
    H1 -- "forward" --> S2
    H1 -- "adjust" --> S1
    H1 -- "postpone or terminate" --> S0

    S2 --> G2
    G2 -- "approved" --> H2
    G2 -- "ambiguity" --> S2
    H2 -- "approve" --> S3
    H2 -- "review product" --> S2

    S3 --> G3
    G3 -- "technical gap" --> S3
    G3 -- "approved" --> D3
    D3 -- "yes" --> H3
    D3 -- "no" --> S4
    H3 -- "accept" --> S4
    H3 -- "review decision" --> S3

    S4 --> L4
    L4 -- "failed" --> S4
    L4 -- "approved" --> S5
    S5 --> G5
    G5 -- "failed" --> S4
    G5 -- "approved" --> S6

    S6 --> H4
    H4 -- "code adjustments" --> S4
    H4 -- "scope adjustments" --> S2
    H4 -- "approve" --> M6
    M6 --> S7 --> G7
    G7 -- "failed" --> S4
    G7 -- "approved" --> D8

    D8 -- "no · R0/R1" --> S8
    D8 -- "yes" --> H5
    H5 -- "approve" --> S8
    H5 -- "review release" --> S7
    S8 --> G8
    G8 -- "regression" --> ROLLBACK["Rollback or automatic pause"]
    ROLLBACK --> S4
    G8 -- "healthy" --> S9 --> END

    S0 -. "telemetry" .-> OBS
    S1 -. "telemetry" .-> OBS
    S2 -. "telemetry" .-> OBS
    S3 -. "telemetry" .-> OBS
    S4 -. "telemetry" .-> OBS
    S5 -. "telemetry" .-> OBS
    S6 -. "telemetry" .-> OBS
    S7 -. "telemetry" .-> OBS
    S8 -. "telemetry" .-> OBS
    S9 -. "telemetry" .-> OBS

    CLOCK --> S10
    NOTE --> S10 --> D10
    D10 -- "yes" --> H6 --> LEARN
    D10 -- "no or automatic sampling" --> LEARN
    LEARN -- "it worked and can be reused" --> MEM
    LEARN -- "went wrong or generated friction" --> IMP
    IMP --> TYPES
    TYPES -- "new prioritizable demand" --> S0
    MEM -. "context for next cycle" .-> S1

    classDef agent fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef knowledge fill:#f3e8ff,stroke:#9333ea,color:#3b0764,stroke-width:1.5px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;
    classDef failure fill:#fee2e2,stroke:#dc2626,color:#450a0a,stroke-width:1.5px;

    class S0,S1,S2,S3,S4,S5,S6,S7,S8 agent;
    class G0,G1,G2,G3,D3,L4,G5,M6,G7,D8,G8,D10 automation;
    class H1,H2,H3,H4,H5,H6 human;
    class S9,OBS,CLOCK,S10,LEARN,MEM,IMP,TYPES knowledge;
    class START,END terminal;
    class ROLLBACK failure;
```

## How to read the stream

- **Blue:** work performed by Agent Teams
- **Green:** automations, gates, hooks and policy decisions
- **Yellow:** human decision checkpoints
- **Purple:** knowledge, telemetry and Auto Dream
- **Red:** regression and recovery path
- **Continuous line:** delivery flow
- **Dotted line:** knowledge collection or reuse

## Human interventions

- **H1:** confirm whether the problem deserves investment
- **H2:** confirm scope, experience and expected result
- **H3:** evaluate only exceptional or high-risk technical decisions
- **H4:** authorize integration according to risk class
- **H5:** authorize critical exposure in production
- **H6:** validate sensitive learning, P0/P1 demands and gate changes

## Closing the cycle

- Knowledge Agent records delivery-specific knowledge
- Auto Dream analyzes all sessions weekly
- Validated learnings update `MEMORY.md`
- Failures and friction generate traceable demands in the backlog
- Demands can improve process, harness, skills, scripts, gates or flow
- The backlog restarts the cycle with better knowledge and controls
