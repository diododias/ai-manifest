# Documentation

The harness documentation layer covers three distinct components: the `AGENTS.md` as an input contract, the ADRs as a record of decisions, and the evidence pack as an auditable trail of execution.

## `docs/adr/` — Architectural Decision Records

ADRs (Architecture Decision Records) record the decisions made, not the current rule. This distinction is fundamental: the rule in `architecture.md` says "domain modules do not matter infrastructure"; the corresponding ADR says why that decision was made, what was considered, and what it costs.

An agent that only reads rules knows what to do. An agent that also reads ADRs knows why — and decides correctly in the case of an edge that the rule did not predict.

The template for creating new ADRs is at [`templates/tech-lead/adr.md`](../templates/tech-lead/adr.md).

## `docs/evidence/` — The auditable trail

The evidence pack exists so that the approval of a change is based on verifiable facts, not on the impression that the agent's summary made.

Each unit of work generates its own directory in `docs/evidence/<work-item>/`. The minimum structure:

```
docs/evidence/<work-item>/
├── summary.md # what was done, what was checked
├── verify-output.txt # complete output of scripts/verify.sh
├── test-results/ # artifacts of executed tests
└── open-items.md # what remains open and why
```

The practical test of a well-constructed evidence pack: **can someone else redo the verification without asking anyone who produced it?** If additional context is needed, what exists is still a summary, not evidence.

The evidence pack must be generated automatically by the `scripts/evidence.sh` script, and not manually assembled by the agent at the end of the task. Manual evidence is selective in nature.

## The complete file structure

An HL3 level repository — the full maturity target — has the following structure:

```text
<repository>/
├── AGENTS.md # agent entry contract
├── README.md # human use: run, build, contribute
│
├── docs/
│ ├── rules/
│ │ ├── architecture.md # modules, boundaries, allowed dependencies
│ │ ├── coding.md # conventions, accepted and prohibited standards
│ │ ├── testing.md # required levels per change type
│ │ ├── security.md # data, secrets, authentication, privacy
│ │ └── operations.md # SLOs, observability, rollout, rollback
│ ├── adr/
│ │ └── ADR-NNN-<slug>.md # decisions and consequences
│ └── evidence/
│ └── <work-item>/ # evidence pack per work unit
│
├── skills/
│ └── <skill>/SKILL.md # executable procedures from repo
│
├── .agent/
│ ├── settings.json # allowed tools, limits, templates
│ ├── mcps.json # authorized MCP servers and scopes
│ └── permissions.md # what requires human in this repository
│
├── scripts/
│ ├── verify.sh # single entry of local checks
│ └── evidence.sh # collects and packages evidence
│
├── .hooks/ # versioned sensors (pre-commit, pre-push)
└── .ci/ # fast lane and deep lane
```

Repositories in HL1 or HL2 contain subsets of this tree. Maturity levels define which subset is sufficient for each level of autonomy.

## What each file carries

| Archive | Load | Does not load |
|---|---|---|
| `AGENTS.md` | how to operate the repo, commands, when to stop | detailed architecture, decision history |
| `docs/rules/*.md` | the rule and the reason for it | step-by-step execution instructions |
| `docs/adr/` | why the decision was made and what it costs | the resulting current rule |
| `skills/<skill>/SKILL.md` | verifiable walkthrough of a recurring task | general knowledge about the domain |
| `.agent/permissions.md` | what requires human authorization | team's global risk policy |
| `.agent/mcps.json` | authorized MCP servers and permitted scopes | credentials or environment configuration |
