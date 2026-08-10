#06 — Commented journey

> The entire cycle seen from human points: where a person enters, what made them enter and what happens if they say no.

This page stitches. It doesn't describe the mechanics of any steps — that's in [`loops/`](../loops/README.md), a file by contract — and it doesn't redefine agent authority. What it shows is the **set**: the twelve steps grouped into five blocks, with the human checkpoints positioned and the return paths visible.

The point to note on the first reading is the **amount of yellow** in the diagram. There are six human decision points throughout the cycle, and two of them are conditional. Everything else is run by agents or checked by automation. It is this proportion that the model tries to sustain — and it is what degrades first when gates become loose or artifacts become ambiguous.

---

## The cycle, through human points

```mermaid
TD flowchart
    START([Need, problem or opportunity])

    subgraph B1["Block 1 · Product and discovery"]
        L0["🚦 Triage<br/>step 0"]
        L1["🔦 Scout<br/>step 1"]
        H1{"H1 · Is it worth investing?"}
        L2["🎨 Studio<br/>step 2"]
        H2{"H2 · Is this what we will build?"}
    end

    subgraph B2["Block 2 · Technical specification"]
        L3["🗺️ Drafting<br/>step 3"]
        D3{"New ADR, exception<br/>or risk R3/R4?"}
        H3{"H3 · Do we accept<br/>the trade-off?"}
    end

    subgraph B3["Block 3 · Construction and validation"]
        L4["🔁 Ralph<br/>step 4"]
        L5["⚔️ Red Team<br/>step 5"]
        G5{{"Sensors and CI<br/>fast and deep lane"}}
    end

    subgraph B4["Block 4 · Integration and delivery"]
        L6["🚪 Gatekeeper<br/>step 6"]
        H4{"H4 · Can we integrate?"}
        L7["🎭 Rehearsal<br/>step 7"]
        D8{"R3/R4 risk or<br/>critical exposure?"}
        H5{"H5 · Can we<br/>expose the risk?"}
        L8["🐤 Canary<br/>step 8"]
    end

    subgraph B5["Block 5 · Knowledge and improvement"]
        L9["🗄️ Archivist<br/>step 9"]
        L11["☀️ Daily<br/>step 11"]
        L10["🌙 Dream<br/>step 10"]
        H6{"H6 · Did the system<br/>learn correctly?"}
    end

    START --> L0 --> L1 --> H1
    H1 -- "forward" --> L2
    H1 -- "adjust" --> L1
    H1 -- "postpone or terminate" --> L0
    L2 --> H2
    H2 -- "approve" --> L3
    H2 -- "review product" --> L2
    L3 --> D3
    D3 -- "yes" --> H3
    D3 -- "no" --> L4
    H3 -- "accept" --> L4
    H3 -- "review decision" --> L3
    L4 --> G5 --> L5
    G5 -- "failed" --> L4
    L5 --> L6 --> H4
    H4 -- "approve" --> L7
    H4 -- "code adjustment" --> L4
    H4 -- "scope adjustment" --> L2
    L7 --> D8
    D8 -- "no · R0/R1" --> L8
    D8 -- "yes" --> H5
    H5 -- "approve" --> L8
    H5 -- "review release" --> L7
    L8 --> L9

    L4 -. "sessions".-> L11
    L5 -. "sessions".-> L11
    L9 -. "telemetry".-> L10
    L11 -. "hypotheses" .-> L10
    L11 -. "improvements".-> L0
    L10 --> H6
    H6 -. "prioritizable demands" .-> L0

    classDef loop fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef knowledge fill:#f3e8ff,stroke:#9333ea,color:#3b0764,stroke-width:1.5px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;

    class L0,L1,L2,L3,L4,L5,L6,L7,L8 loop;
    class G5,D3,D8 automation;
    class H1,H2,H3,H4,H5,H6 human;
    class L9,L10,L11 knowledge;
    class START terminal;
```

| Color | Nature |
|---|---|
| 🔵 Blue | loop executed by agents |
| 🟢 Green | verification or decision by policy |
| 🟡 Yellow | human decision |
| 🟣 Purple | knowledge, memory and improvement |

Solid line indicates delivery flow; dotted line, knowledge collection or reuse. **Back arrows matter as much as forward arrows** — they show where a failure sends work back, which is why a loose gate in an early step is costly several steps later.

---

## The five blocks

Each block groups loops that answer the same question. The table is the set map; the execution contract for each line is in the linked file.

| # | Block | Loops | Checkpoints | Core artifacts |
|---:|---|---|---|---|
| 1 | Product and discovery | [🚦 0](../loops/00-intake-and-triage.md) · [🔦 1](../loops/01-discovery-and-research.md) · [🎨 2](../loops/02-product-and-ux-planning.md) | H1, H2 | `PB.md`, `PRD.md` |
| 2 | Technical specification | [🗺️ 3](../loops/03-technical-specification.md) | H3, conditional | `PLAN`, `SPEC`, `ADR`, `TASKS` |
| 3 | Construction and validation | [🔁 4](../loops/04-autonomous-implementation.md) · [⚔️ 5](../loops/05-adversarial-validation.md) | none, except exceptions | move ready for PR |
| 4 | Integration and delivery | [🚪 6](../loops/06-pr-and-merge.md) · [🎭 7](../loops/07-release-candidate-validation.md) · [🐤 8](../loops/08-production-release-and-observation.md) | H4, H5 | PR, release candidate, release |
| 5 | Knowledge and improvement | [🗄️ 9](../loops/09-knowledge-curation.md) · [🌙 10](../loops/10-continuous-improvement.md) · [☀️ 11](../loops/11-daily-operations.md) | H6, conditional | `MEMORY.md`, demands for improvement |

### Block 1 — product and discovery

Answer **"is it worth solving this problem, and is this the problem?"**. This is where more evidence is produced and where an error costs less to correct. Concentrates two of the six checkpoints, deliberately: wrong decision here propagates throughout the rest of the cycle.

The owner is the PM, with UX as co-author in H2. The advancement criterion is that problem, user, value and experience are explicit and traceable to their origin.

### Block 2 — technical specification

Answers **"how to build, and what do we accept when choosing like this?"**. The only block with a single loop, and the only one whose checkpoint is conditional in nature: without new ADR, exception or high risk, there is no trade-off to accept, and the step goes straight to construction.

The owner is the Tech Lead. The advancement criteria is `PRD → SPEC → TASKS` traceability and critical gaps addressed.

### Block 3 — construction and validation

Answers to **"it was built, and someone independent attacked it?"**. It is the block without human checkpoint in the healthy flow — and that is what sustains the model. The turns here are internal and average: the agent corrects, the sensor disapproves, the critic contests, all in minutes.

The human only appears by exception: attempt limit reached, gate false positive or requirement gap discovered in validation. **A block 3 that frequently calls human is a symptom of a poorly executed block 1 or 2** — the requirement arrived ambiguous.

### Block 4 — integration and delivery

Answers to **"can we integrate, and can we expose the risk?"**. It concentrates the two checkpoints where the cost of making a mistake is highest and most visible. The weight of each one varies by risk class, according to the table in [Human checkpoints](02-checkpoints-humanos.md).

The advancement criterion has two parts that do not replace each other: green gates **and** registered decision of who has title.

### Block 5 — knowledge and improvement

Answers **"did the system learn, and did it learn correctly?"**. It closes the longest turns — those that have the work system itself as an object — and is the only block that rotates by calendar, not by Work Item.

Contains three loops with different windows: [🗄️ Archivist](../loops/09-knowledge-curation.md) records knowledge of a delivery; [☀️ Daily](../loops/11-daily-operations.md) reads the day; [🌙 Dream](../loops/10-continuous-improvement.md) reads the week with independent criticism and leads to H6. The departure of the three restarts the cycle through block 1 — with better context and controls than in the previous lap.

---

## If you don't pass

A failed gate does not interrupt the journey: it returns the work to a specific point. At the block level, the returns are these.

| Block | Correctable fault back to | Decision returns to |
|---|---|---|
| 1 | the block itself, with new question | PM, in H1 and H2 |
| 2 | block 1 if requirement is ambiguous | Tech Lead, in H3 |
| 3 | the block itself, within the attempt limit | Tech Lead, by exception |
| 4 | block 3, if it is a defect; block 1, if scope | Code Owner in H4; Tech Lead and PM in H5 |
| 5 | the hypothesis remains identified as such | trio, in H6 |

The per-loop map — more granular and used during execution — is in [`loops/README.md`](../loops/README.md#caminhos-de-falha).

The reading that matters: **the later the failure is detected, the further back it returns work.** A poorly defined scope discovered in H4 returns to block 1 and discards the work of three blocks. It's the economic argument for focusing rigor at the beginning.

---

*Previous: [Operator Manual](05-manual-do-operador.md) · Next: [Documentation Workflows](07-workflows-de-documentacao.md).*
