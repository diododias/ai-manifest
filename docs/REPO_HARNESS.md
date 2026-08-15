# 1. Application Repository Harness

---

## Overview

The **repo harness** converts the tacit knowledge of the repository into versioned files that the agent reads on its own and into checks that run without asking for a license. It lives inside the code repository, travels with the clone, and exists to answer four questions before the agent needs to act:

1. What is this repository?
2. How are things done here?
3. What do I need to prove before I can say I'm done?
4. What can I not touch without authorization?

The harness is organized into five cumulative layers. Order matters: Each layer eliminates a specific class of failure, and building out of sequence produces expensive failures.

| Layer | Answers | Materializes in |
|---|---|---|
| **Context** | what this repository is and what rules apply | `AGENTS.md`, `docs/rules/` |
| **Procedure** | how to perform a recurring task the right way | `skills/`, scripts |
| **Verification** | what needs to be true before moving forward | sensors, CI, merge policies |
| **Permission** | what this agent can do and what requires a person | `.agent/`, environments |
| **Evidence** | how to prove later that it was correct | evidence pack, logs, artifacts |

It's also worth understanding what a harness **isn't**. It is not the CI pipeline — the pipeline is just one possible implementation of the verification layer. It is not the architectural documentation itself — it points to it. And it's not about how the work is organized outside of the code: that's the responsibility of the workspace of whoever coordinates the agents.

## The five layers under load

The five layers describe a harness that is being built. A harness that is being *operated* — several agents, real traffic, a repository that keeps changing — needs four properties that no single layer owns, because each of them is a way for the layers to be present and still not hold:

| Property | The failure it answers |
|---|---|
| **Trust** | the agent read something hostile and treated it as an instruction |
| **Resilience** | the verification did not run, and its silence was read as approval |
| **Coordination** | the evidence was valid, against a base that has since moved |
| **Economy** | nothing broke, and the work cost more than it was worth |

They are properties rather than layers because they cannot be built in sequence after the others: each one is a question asked *of* the five layers, and a harness that never asks them is not an earlier-stage harness — it is one whose gaps have not surfaced yet.

---

## Index

**Foundations**

- [Permissions](PERMISSIONS.md) — what the agent may invoke, what requires a person, and why it cannot live in the prompt
- [Tools](TOOLS.md) — tooling index: LSP, verification, navigation, context management
- [Rules](RULES.md) — desired state, entry contract (`AGENTS.md`), escalation and reversibility
- [Sensors](SENSORS.md) — local versioned checks (pre-commit, pre-push)
- [Gates](GATES.md) — verification architecture from commit to deploy and autonomy levels
- [Documentation](DOCUMENTATION.md) — ADRs, evidence pack, identity and provenance
- [MCPs](MCPS.md) — Model Context Protocol servers, scopes and authorization
- [Skills](SKILLS.md) — catalog of verifiable procedures from the repository

**Operating under load**

- [Trust](TRUST.md) — untrusted content, injection, exfiltration and the harness as a supply chain
- [Failure](FAILURE.md) — fail-closed, the gate that did not run, flaky checks, verifying the verifier
- [Concurrency](CONCURRENCY.md) — several agents at once, evidence freshness and integration order
- [Budget](BUDGET.md) — cost, turns, context, and what degrades when they run out
- [Versioning](VERSIONING.md) — the harness has versions, and a change invalidates past approvals

**Related overview**

- [Maturity](MATURITY.md) — the squad-wide evolution from opportunistic assistance to adaptive operation
- [Metrics](METRICS.md) — the balanced panel for product, delivery, stability and human-AI collaboration

These are cross-cutting views of the full development system, not additional harness layers.

---

*Next: [Permissions](PERMISSIONS.md) — the layer that cannot be enforced by asking.*
