---
title: Agent Team — operational prompts by role
status: proposed
updated_at: 2026-08-08
---

# Agent operational prompts

> The 23 roles in the catalog, materialized as self-contained, runtime-independent prompts.

## In 2 minutes

The [catalog](catalog.md) defines what each agent should do. This directory delivers agents **ready to use**: one folder per paper, with a single prompt that brings together the operational contract, presence and stable policies of the sponsor.

`AGENT.md` is the paper's only source of executable instructions. Each `AGENT.md` contains all the role's execution, output and persistence rules. Sources, local rules and skills are only read when they are mission specific.

```text
<agent-id>/
└── AGENT.md # single prompt: mission, limits, presence and stable directives
```

Don't precreate working memory: it comes from real facts and decisions. Secrets, credentials and `.env` files do not belong in these versioned folders.

A runtime can load the file directly, or an orchestrator can provide its contents as paper instructions. The folder assumes no commands, syncable identity, or configuration of a specific tool.

---

## Materialized catalog

| Agent | Identity | Sponsor |
|---|---|---|
| [`intake-agent`](intake-agent/AGENT.md) | Intake Agent | Product Manager |
| [`meeting-context-agent`](meeting-context-agent/AGENT.md) | Meeting Context Agent | meeting owner |
| [`orchestrator-agent`](orchestrator-agent/AGENT.md) | Orchestrator Agent | human owner of the stage |
| [`product-manager-agent`](product-manager-agent/AGENT.md) | Product Manager Agent | Product Manager |
| [`ux-specification-agent`](ux-specification-agent/AGENT.md) | UX Specification Agent | UX |
| [`tech-lead-discovery-agent`](tech-lead-discovery-agent/AGENT.md) | Tech Lead Discovery Agent | Tech Lead |
| [`adversarial-product-manager-agent`](adversarial-product-manager-agent/AGENT.md) | Adversarial Product Manager Agent | Product Manager |
| [`specification-tech-lead-agent`](specification-tech-lead-agent/AGENT.md) | Specification Tech Lead Agent | Tech Lead |
| [`adversarial-tech-lead-agent`](adversarial-tech-lead-agent/AGENT.md) | Adversarial Tech Lead Agent | Tech Lead |
| [`specialist-security-data-platform-agent`](specialist-security-data-platform-agent/AGENT.md) | Security, Data & Platform Specialist Agent | Tech Lead or specialist |
| [`software-engineer-agent`](software-engineer-agent/AGENT.md) | Software Engineer Agent | Tech Lead |
| [`qa-validation-agent`](qa-validation-agent/AGENT.md) | QA & Validation Agent | Tech Lead |
| [`security-review-agent`](security-review-agent/AGENT.md) | Security Review Agent | Tech Lead or Security Owner |
| [`architecture-review-agent`](architecture-review-agent/AGENT.md) | Architecture Review Agent | Tech Lead |
| [`adversarial-code-reviewer-agent`](adversarial-code-reviewer-agent/AGENT.md) | Adversarial Code Reviewer Agent | Tech Lead |
| [`pr-agent`](pr-agent/AGENT.md) | PR Agent | Tech Lead |
| [`product-validation-agent`](product-validation-agent/AGENT.md) | Product Validation Agent | Product Manager and UX |
| [`release-agent`](release-agent/AGENT.md) | ReleaseAgent | Tech Lead |
| [`observability-agent`](observability-agent/AGENT.md) | ObservabilityAgent | Tech Lead |
| [`knowledge-agent`](knowledge-agent/AGENT.md) | Knowledge Agent | domain owner |
| [`telemetry-agent`](telemetry-agent/AGENT.md) | Telemetry Agent | threesome |
| [`auto-dream-agent`](auto-dream-agent/AGENT.md) | Auto Dream Agent | threesome |
| [`critic-agent`](critic-agent/AGENT.md) | Critical Agent | decision owner |

---

## Usage

Read the `AGENT.md` of the chosen role and give the agent the mission identity, input artifacts, and authorized permissions. The prompt does not replace these inputs: it defines how the role works after receiving them.

---

## Safety and operation

**Isolation.** Each agent needs its own state and working directory when running in parallel. The prompt does not create a sandbox or grant permissions: configure them at runtime.

**Credentials.** Do not store tokens, OAuth, keys, `.env`, sessions, or credentials in these folders. They are versioned.

**Exposure.** Configure channel bindings only after reviewing identity, access, and public behavior.

**Independence.** Authorship and critique papers use independent instances whenever there is a risk of self-evaluation — it's the same rule as [catalog](catalog.md#3-mapa-dos-agentes), and ignoring it nullifies the value of adversarial agents.

---

## Auxiliary register

[`registry.yaml`](registry.yaml) is a paper inventory, intended for automation and auditing. It is not a runtime manifest.
