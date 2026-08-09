# Individual loop contracts

This directory contains documentation for the 12 steps of the journey, one file per loop. The general concept — what a loop is, the three loops, how agents, skills, tools, MCPs, sensors and gates fit into each loop — is in [Loops — How Loops Work](../LOOPS.md); Here are the specific contracts.

## How to read a contract

Each file follows the same structure, and reading in the order below answers the questions in the sequence in which they normally arise:

| Section | Reply |
|---|---|
| **Operating contract** | what comes in, who consolidates, who challenges, what comes out, which gate and which human owner |
| **Sequence** | the order of the missions, what runs in parallel and where each turn ends |
| **Handoffs** | what crosses the border at entry and exit |
| **What this loop doesn't do** | the explicit limits of the step and the reason for each |
| **Typical faults** | the recurring failure mode and the symptom by which it is recognized |
| **Artifacts and where they live** | the canonical destination of each exit and what is just transit |
| **Scaling** | the stopping condition and the human owner of the decision |

Every loop fulfills, in addition to these particularities, the **common contract**: six mandatory items, a single consolidating agent, criticism by an independent instance, handoff that separates fact from hypothesis, and an artifact that is only considered delivered when it reaches the canonical source. An individual contract should be read as "the common contract, plus these particulars".

## Entry

Receives what arrives from outside and organizes the work of others.

| # | Loop | Codename | Consolidate |
|---:|---|---|---|
| 0 | [Intake and screening](00-intake-and-triage.md) | 🚦 Triage Loop | Intake Agent |

## Product and discovery

They structure the problem before any solution, with the production/criticism pair already present.

| # | Loop | Codename | Consolidate |
|---:|---|---|---|
| 1 | [Discovery and research](01-discovery-and-research.md) | 🔦Scout Loop | Product Manager Agent |
| 2 | [Product and UX planning](02-product-and-ux-planning.md) | 🎨 Studio Loop | Product Manager + UX Specification |

## Specification

Converts the approved product into an executable technical strategy.

| # | Loop | Codename | Consolidate |
|---:|---|---|---|
| 3 | [Technical specification](03-technical-specification.md) | 🗺️ Drafting Loop | Specification Tech Lead Agent |

## Construction and validation

Where the separation between producing and approving becomes more visible — and where the three turns rotate faster.

| # | Loop | Codename | Consolidate |
|---:|---|---|---|
| 4 | [Standalone implementation](04-autonomous-implementation.md) | 🔁Ralph Loop | Orchestrator Agent |
| 5 | [Adversarial validation](05-adversarial-validation.md) | ⚔️ Red Team Loop | QA / Validation Agent |
| 6 | [PR and merge](06-pr-and-merge.md) | 🚪 Gatekeeper Loop | PR Agent |

## Release and operation

They confirm value in a representative environment and expose change in a controlled way.

| # | Loop | Codename | Consolidate |
|---:|---|---|---|
| 7 | [Approval](07-release-candidate-validation.md) | 🎭 Rehearsal Loop | Product Validation Agent |
| 8 | [Production and observation](08-production-release-and-observation.md) | 🐤 Canary Loop | ReleaseAgent |

## Knowledge and improvement

They close the longest loop: the one that has the work system itself as an object.

| # | Loop | Codename | Consolidate |
|---:|---|---|---|
| 9 | [Knowledge curation](09-knowledge-curation.md) | 🗄️ Archivist Loop | Knowledge Agent |
| 10 | [Telemetry and continuous improvement](10-continuous-improvement.md) | 🌙Dream Loop | Auto Dream Agent |
| 11 | [Daily Operation](11-daily-operations.md) | ☀️ Daily Loop | Auto Dream Agent |

Loops 10 and 11 are the only ones that rotate by calendar, and not by Work Item. The [comparison between the two windows](11-daily-operations.md#daily-and-weekly--why-there-are-two-loops) explains why there are two circuits and not one.

---

## Failure paths

A failed gate does not interrupt the journey: it returns work to a specific loop. This map is the answer to "what if I don't pass?".

| Loop | Correctable fault back to | Decision returns to |
|---|---|---|
| 🚦 Triage | request origin | PM |
| 🔦 Scout | the loop itself, with new question | H1 — invest, adjust, postpone or terminate |
| 🎨 Studio | 🔦 Scout, if evidence is missing | H2 — PM and UX |
| 🗺️ Drafting | 🎨 Studio, if the requirement is ambiguous | H3 — Tech Lead |
| 🔁 Ralph | the agent himself, within the limit of attempts | Tech Lead |
| ⚔️ Red Team | 🔁 Ralph | Tech Lead, for exception |
| 🚪 Gatekeeper | 🔁 Ralph + revalidation in 🥊 | H4 — Code Owner |
| 🎭 Rehearsal | 🔁 Ralph, if it's a defect; 🎨 Studio, if scope | PM or UX |
| 🐤 Canary | rollback and 🔁 Ralph | H5 — Tech Lead; PM co-approves R3/R4 |
| 🗄️ Archivist | hypothesis remains identified as such | domain owner |
| 🌙Dream | hypothesis under observation | H6 — trio |
| ☀️ Daily | hypothesis under observation until new evidence | workspace owner; improvement follows the PM via 🚦 Triage |
