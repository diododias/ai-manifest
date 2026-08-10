# Individual agent contracts

This directory contains documentation for each of the 23 Agent Team roles, one file per agent. The general concept — what an agent is, what it consumes, how it performs a mission and when it scales — is in [Agents — How Agents Work](../AGENTES.md); Here are the specific contracts.

## How to read a contract

Each file follows the same structure, and reading in the order below answers the questions in the sequence in which they normally arise:

| Section | Reply |
|---|---|
| **Operating contract** | who sponsors, what the agent receives, what they deliver, what tools and skills they use, which gate satisfies and when they scale |
| **What this agent doesn't do** | the explicit limits of the role and the reason for each |
| **Presence and instincts** | the operational personality that guides judgment in unforeseen cases |
| **Operation notes** | role-specific decisions and pitfalls in practice |
| **Operational prompt** | where is the only executable statement from the paper in `agents/` |

Every agent fulfills, in addition to these particularities, the **common contract**: complete mission identity, universal rules of truth, limit, skills and delivery, standardized exit envelope and universal escalation conditions. An individual contract should be read as "the common contract, plus these particulars".

## Entry and coordination

They receive what arrives from outside and organize the work of others. None of them decide or approve: they prepare and route.

| Agent | Sponsor | Central exit |
|---|---|---|
| [📥 Intake Agent](intake-agent.md) | Product Manager | Work Item triaged and prioritized |
| [📝 Meeting Context Agent](meeting-context-agent.md) | meeting owner | transcript summary and context pack |
| [🎛️ Orchestrator Agent](orchestrator-agent.md) | human owner of the stage | routed missions and consolidated state |

## Product, UX and discovery

They structure the problem before any solution, with the production/criticism pair already present.

| Agent | Sponsor | Central exit |
|---|---|---|
| [📋 Product Manager Agent](product-manager-agent.md) | Product Manager | `PB.md` or `PRD.md` |
| [🧭 UX Specification Agent](ux-specification-agent.md) | UX | journey, flows and UX spec |
| [🔭 Tech Lead Discovery Agent](tech-lead-discovery-agent.md) | Tech Lead | feasibility and initial risks |
| [🥊 Adversarial Product Manager Agent](adversarial-product-manager-agent.md) | Product Manager | rated product review |

## Technical specification

They convert the approved product into an executable technical strategy.

| Agent | Sponsor | Central exit |
|---|---|---|
| [📐 Specification Tech Lead Agent](specification-tech-lead-agent.md) | Tech Lead | `PLAN`, `SPEC`, `ADR`, `TASKS`, `CHECKLIST` |
| [♟️ Adversarial Tech Lead Agent](adversarial-tech-lead-agent.md) | Tech Lead | technical criticism and trade-offs |
| [🧩 Security, Data & Platform Specialist Agent](specialist-security-data-platform-agent.md) | Tech Lead or specialist | specialized domain analysis |

## Construction and validation

The largest group, and where the separation between producing and approving is most visible.

| Agent | Sponsor | Central exit |
|---|---|---|
| [🛠️ Software Engineer Agent](software-engineer-agent.md) | Tech Lead | code, tests, documentation and commits |
| [🧪 QA & Validation Agent](qa-validation-agent.md) | Tech Lead | criterion-evidence matrix |
| [🛡️ Security Review Agent](security-review-agent.md) | Tech Lead or Security Owner | security and privacy findings |
| [🏛️ Architecture Review Agent](architecture-review-agent.md) | Tech Lead | architectural compliance |
| [🔎 Adversarial Code Reviewer Agent](adversarial-code-reviewer-agent.md) | Tech Lead | correctness and maintenance findings |

## Integration, approval and operation

They take the validated change to production and observe its health.

| Agent | Sponsor | Central exit |
|---|---|---|
| [🔀 PR Agent](pr-agent.md) | Tech Lead | PR and evidence pack |
| [✅ Product Validation Agent](product-validation-agent.md) | Product Manager and UX | approval report |
| [🚀 Release Agent](release-agent.md) | Tech Lead | traceable and reversible release |
| [📡 Observability Agent](observability-agent.md) | Tech Lead | health report and alerts |

## Knowledge and improvement

They close the cycle on the system itself.

| Agent | Sponsor | Central exit |
|---|---|---|
| [📚 Knowledge Agent](knowledge-agent.md) | domain owner | updated canonical sources |
| [📊 Telemetry Agent](telemetry-agent.md) | threesome | governed dataset and flow dashboard |
| [💭 Auto Dream Agent](auto-dream-agent.md) | threesome | learning and demands P0–P3 |
| [⚖️ Critic Agent](critic-agent.md) | decision owner | independent review |

---

*Return to [Agentes — How Agents Work](../AGENTES.md) · [Repository Harness](../REPO_HARNESS.md)*
