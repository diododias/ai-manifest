# Maturity

[Gates](GATES.md#progressive-autonomy-and-the-harness-ceiling) defines the rule: the harness level is the ceiling of autonomy, never its consequence. The A0–A4 autonomy levels are defined in [Human checkpoints](metodologia/02-checkpoints-humanos.md).

## Computed, not declared

Every requirement below is mechanically verifiable. The repository level is the highest level for which every requirement is currently satisfied.

Two constraints apply:

- **The level is the minimum, not the average.** One missing HL2 control keeps the repository at HL1.
- **Degraded mode lowers the level while it lasts.** A quarantined gate is a missing gate ([Failure](FAILURE.md#declaring-a-degraded-mode)).

## HL1 — readable

The agent can understand the repository and verify its work locally.

| Item | Checkable by |
|---|---|
| Root `AGENTS.md` with all six blocks | file exists; every heading is present; escalation is non-empty |
| `docs/rules/architecture.md` and `docs/rules/testing.md` | both files exist and are non-empty |
| Change type mapped to mandatory test levels | mapping exists ([Rules](RULES.md#the-testing-strategy-as-a-rule)) |
| `scripts/verify.sh` supports `--staged`, `--affected`, `--full` | each mode accepts `--help` or a dry run |
| Known-bad verification canary | `verify.sh` rejects the fixture |
| Tool availability asserted | removing a required tool fails instead of skipping |
| Pre-commit sensor installed through `.hooks/` | bootstrap sets `core.hooksPath=.hooks` |
| Secret scanning in pre-commit | fake-credential fixture is rejected |
| `.agent/settings.json` defines `allowed`, `ask`, `denied` and budget | file parses; `allowed` is non-empty; command families have no wildcard |

## HL2 — verifiable

A clean environment reproduces verification, and an independent reviewer can audit the result.

| Item | Checkable by |
|---|---|
| Separate CI fast and deep lanes | both configurations exist; the gated flow cannot edit them |
| Tested fast-lane path filters | filter test runs ([Failure](FAILURE.md#verifying-the-verifier)) |
| Protected default branch and required checks | platform API rejects direct push and reports required checks |
| `CODEOWNERS` covers `.agent/`, `.hooks/`, CI and `docs/rules/` | every path resolves to an existing owner |
| Evidence pack from `scripts/evidence.sh` | output contains `summary.md`, `verify-output.txt`, `gate-status.json` |
| Explicit gate states | `passed`, `failed` and `skipped` are all producible |
| MCP scope is explicit | `.agent/mcps.json` exists or zero authorized MCPs are declared |
| Instruction paths are exhaustive | `.agent/trust.md` enumerates them |
| Harness versioning | `HARNESS_VERSION` parses and `.agent/CHANGELOG.md` exists ([Versioning](VERSIONING.md)) |
| Architecture and secret canaries | both run on schedule and currently pass |

## HL3 — operable by a team

Multiple agents can operate concurrently without collapsing separation of duties.

| Item | Checkable by |
|---|---|
| Distinct identity per writing role | identities differ; commits are signed |
| Author cannot approve the same change | merge gate rejects the attempt |
| Merge attestation | missing or mismatched `attestation.json` blocks merge |
| Repository skills | recurring procedures exist in `skills/<skill>/SKILL.md` |
| No production credential on agents | inventory assigns deploy secrets only to pipeline identity |
| Post-deploy baseline and rollback criterion | criterion is declared and has been exercised |
| Evidence freshness before integration | merge queue rejects stale packs ([Concurrency](CONCURRENCY.md)) |
| Budget per Work Item | exhaustion escalates instead of truncating |
| Escape rate per gate | real findings populate the metric ([Metrics](METRICS.md)) |

## `harness-doctor`

`scripts/harness-doctor.sh` executes the checks and compares the computed ceiling with actual autonomy:

```text
HL1  readable          9/9   ✓
HL2  verifiable        8/10  ✗
     ✗ branch protection: default branch accepts direct push
     ✗ canary: no known-bad fixture for the architecture gate
HL3  operable by team  2/9   ✗

Level: HL1        Sustained autonomy: A0–A1
Currently operating at: A2   ← ceiling exceeded
```

Run it in the deep lane and on a schedule. Deleted owners, stale path filters and missing tools can lower the level without an explicit decision.

## Build order

The dependency order is strict:

1. `AGENTS.md` and rules before automation.
2. `verify.sh` and local sensors before CI.
3. Canaries before autonomy depends on green gates.
4. Evidence and attestation before concurrent agents.
5. Identity and branch protection before unattended merge.
6. Sustained metrics before level promotion.

---

*Next: [Agents](AGENTES.md) — how an agent works and the catalog of 23 roles.*
