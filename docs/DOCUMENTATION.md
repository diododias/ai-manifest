# Documentation

The harness documentation layer covers three distinct components: the `AGENTS.md` as an input contract, the ADRs as a record of decisions, and the evidence pack as an auditable trail of execution.

## `docs/adr/` — Architectural Decision Records

ADRs (Architecture Decision Records) record the decisions made, not the current rule. This distinction is fundamental: the rule in `architecture.md` says "domain modules must not import infrastructure"; the corresponding ADR says why that decision was made, what was considered, and what it costs.

An agent that only reads rules knows what to do. An agent that also reads ADRs knows why — and decides correctly in the edge case that the rule did not predict.

The template for creating new ADRs is at [`templates/tech-lead/adr.md`](../templates/tech-lead/adr.md).

## `docs/evidence/` — The auditable trail

The evidence pack exists so that the approval of a change is based on verifiable facts, not on the impression that the agent's summary made.

Each unit of work generates its own directory in `docs/evidence/<work-item>/`. The minimum structure:

```
docs/evidence/<work-item>/
├── summary.md          # what was done, what was checked
├── attestation.json    # who produced it, under which harness version
├── verify-output.txt   # complete output of scripts/verify.sh
├── gate-status.json    # per gate: passed, failed, skipped — and why
├── external-calls.log  # MCP and network operations with parameters and responses
├── test-results/       # artifacts of executed tests
└── open-items.md       # what remains open and why
```

The practical test of a well-constructed evidence pack: **can someone else redo the verification without asking anyone who produced it?** If additional context is needed, what exists is still a summary, not evidence.

The evidence pack must be generated automatically by the `scripts/evidence.sh` script, and not manually assembled by the agent at the end of the task. Manual evidence is selective in nature.

Two of the files above exist because a pack that records only successes is not an audit trail. `gate-status.json` distinguishes *passed* from *skipped*, which is the difference between a verified change and an unverified one that looks identical from the outside ([Failure](FAILURE.md)). `external-calls.log` records what the agent did outside the repository, where a local gate cannot see it ([MCPs](MCPS.md#mcps-and-the-evidence-pack)).

## Identity and provenance

"Whoever proposes does not approve" is a property of the version control system or it is nothing. Prompt instructions cannot enforce it, because the same process that would obey them is the process being constrained. The harness therefore records, structurally, who produced each artifact.

Three things have to be true:

**The producing identity is distinct and authenticated.** Each agent role that can write commits does so under its own identity — a separate account or application credential, with signed commits. Approval by an identity that appears in the authorship of the same change is rejected by the merge gate, not by convention.

**The artifact carries what produced it.** `attestation.json` records the facts a reviewer needs and an agent cannot self-report credibly later: agent role, model and version, harness version, the SHA of every rule file actually read, the work item, and the base commit the work started from.

```json
{
  "work_item": "WI-1043",
  "agent": "software-engineer-agent",
  "model": "claude-sonnet-5",
  "harness_version": "2.4.0",
  "rules_read": { "docs/rules/architecture.md": "9f2c…", "docs/rules/testing.md": "41ab…" },
  "base_commit": "e7d1c9a",
  "produced_at": "2026-08-14T18:22:04Z"
}
```

**Provenance is verified, not trusted.** The merge gate checks the attestation against the commits it describes. An attestation that no one validates is documentation of an intention, and the failure mode of an unvalidated claim is that it is only wrong when it matters.

The `rules_read` field is what makes an approval auditable after the fact: it answers "under which rules was this accepted?" without depending on anyone's memory of what the repository looked like that week. It is also the join key with [Versioning](VERSIONING.md) — when a rule changes, this field identifies exactly which past approvals were granted under the old text.

## The complete file structure

An HL3 level repository — the full maturity target — has the following structure:

```text
<repository>/
├── AGENTS.md                    # agent entry contract
├── README.md                    # human use: run, build, contribute
│
├── docs/
│   ├── rules/
│   │   ├── architecture.md      # modules, boundaries, allowed dependencies
│   │   ├── coding.md            # conventions, accepted and prohibited standards
│   │   ├── testing.md           # required levels per change type
│   │   ├── security.md          # data, secrets, authentication, privacy
│   │   └── operations.md        # SLOs, observability, rollout, rollback
│   ├── adr/
│   │   └── ADR-NNN-<slug>.md    # decisions and consequences
│   └── evidence/
│       └── <work-item>/         # evidence pack per work unit
│
├── skills/
│   └── <skill>/SKILL.md         # executable procedures from repo
│
├── .agent/
│   ├── HARNESS_VERSION          # the version this repository's harness is at
│   ├── CHANGELOG.md             # what changed in the harness, and what it invalidates
│   ├── settings.json            # allowed tools, limits, budgets
│   ├── mcps.json                # authorized MCP servers and scopes
│   ├── identity.md              # which identity each agent role writes under
│   ├── trust.md                 # trusted and untrusted content in this repository
│   └── permissions.md           # what requires a human in this repository
│
├── scripts/
│   ├── verify.sh                # single entry of local checks
│   ├── evidence.sh              # collects and packages evidence
│   └── harness-doctor.sh        # reports repository-control readiness
│
├── .hooks/                      # versioned sensors (pre-commit, pre-push)
└── .github/workflows/           # fast lane and deep lane
```

The last path is the one to adapt: it is written as GitHub Actions because that is the common case, and it maps to `.gitlab-ci.yml` or the equivalent elsewhere. What matters is not the directory but that the two lanes are separate files and that neither is editable from inside the flow they gate.

Repositories at different HL verification levels contain subsets of this tree. [Gates](GATES.md#progressive-autonomy-and-the-harness-ceiling) defines the autonomy ceiling supported by those controls; [Maturity](MATURITY.md) assesses the broader squad operating model.

## What each file carries

| File | Carries | Does not carry |
|---|---|---|
| `AGENTS.md` | how to operate the repo, commands, when to stop | detailed architecture, decision history |
| `docs/rules/*.md` | the rule and the reason for it | step-by-step execution instructions |
| `docs/adr/` | why the decision was made and what it costs | the resulting current rule |
| `skills/<skill>/SKILL.md` | verifiable walkthrough of a recurring task | general knowledge about the domain |
| `.agent/identity.md` | which identity writes what, and who may approve it | credentials themselves |
| `.agent/trust.md` | which inputs are content and which are instructions | the threat model of the organization |
| `.agent/permissions.md` | what requires human authorization | team's global risk policy |
| `.agent/mcps.json` | authorized MCP servers and permitted scopes | credentials or environment configuration |

---

*Next: [MCPs](MCPS.md) — external systems, authorized scopes, and why they are a different kind of tool.*
