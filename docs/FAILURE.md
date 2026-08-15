# Failure

The verification ladder assumes that its steps run. That assumption is the least examined part of a harness and the one that fails most quietly, because a check that does not run produces the same output as a check that passed: nothing.

Everything else in this documentation describes how to catch a bad change. This page describes how to catch a verification that stopped working.

## A gate that did not run did not pass

The default behavior of almost every check, written the obvious way, is to disappear when its conditions are not met:

| The check | Why it stopped | What the pipeline showed |
|---|---|---|
| a hook guarded by `command -v <tool> \|\| exit 0` | the tool is not installed on this machine | success |
| any sensor in `.hooks/` | `core.hooksPath` was never set on this clone | success |
| a fast-lane job filtered by path | a directory was renamed and the glob no longer matches | success, and faster |
| a CI job with a conditional | the condition silently became false | success, job not listed |
| a test suite | it matched zero test files after a config change | success, "0 passing" |
| a gate for a required reviewer | the CODEOWNERS entry points at a group that no longer exists | approved |

Every row is a real pattern, and every row is written by a competent engineer trying to be accommodating. The accommodation is the defect: **a check that cannot run has learned nothing about the change, and reporting "nothing learned" as "nothing wrong" is the single most expensive default in a verification system.**

The rule is fail-closed. A gate that cannot execute reports failure, names what is missing, and says how to install it. Where a repository genuinely needs to proceed without a check — an optional tool during onboarding, a scan that requires a credential a contributor does not have — that is a *declared* degraded mode, not a silent one.

## Three states, never two

A gate reports one of three results, and the third is the one usually missing:

| State | Meaning | Consequence |
|---|---|---|
| `passed` | the check ran and the change satisfies it | proceeds |
| `failed` | the check ran and the change violates it | blocks |
| `skipped` | the check did not run | blocks by default; proceeds only where the degraded mode is declared, and is recorded either way |

`gate-status.json` in the evidence pack carries these states per gate ([Documentation](DOCUMENTATION.md)). Its purpose is to make the distinction between a verified change and an unverified one visible to a reviewer, because from the outside — a green pipeline, an evidence pack, a summary — the two are identical. A pack that records only successes cannot answer the question an audit actually asks, which is not "did the checks pass" but "which checks ran".

## Flaky is a third failure, not a soft pass

A check that fails intermittently trains everyone to ignore it, and it takes the credibility of the neighboring checks with it. The automatic retry is what converts a broken check into a permanently ignored one: the signal is preserved just well enough that no one has to fix it.

The policy that works has three parts. A flaky check is **quarantined** rather than retried — moved out of the blocking set explicitly, so its absence is visible. Quarantine carries a **named owner and a deadline**, because an unowned quarantine is a deletion performed slowly. And a run that used a retry reports as **degraded**, not as passed, so the fact that a retry was needed survives into the evidence.

For agents specifically, there is a further reason not to retry silently: a flaky gate teaches an agent that the correct response to a red check is to run it again. That heuristic then generalizes to gates that were telling the truth.

## Verifying the verifier

A gate is code, and code that has never been observed to fail correctly is code whose behavior is unknown. Three mechanisms, in increasing cost:

**A known-bad canary.** Each gate has a small input it must reject. The lint gate has a file that violates a rule; the architecture gate has an import that crosses a forbidden boundary; the secret scanner has a fake credential in a fixture. Run periodically, this answers "does this gate still detect anything?" — the question a green pipeline never answers.

**An installation check.** `verify.sh` asserts that the sensors are actually installed and that every tool it depends on is present, and fails if they are not. This is the direct countermeasure to the first two rows of the table above, and it costs milliseconds.

**Mutation testing.** The general form of the canary for the test suite: it answers whether the tests would catch a regression rather than merely execute the line. Expensive, and belongs at the end of the deep lane ([Tools](TOOLS.md)).

The health of the gates is itself measurable over time — how often a gate is skipped, and how much escapes the ones that run. Those are the two metrics that matter most in [Metrics](METRICS.md).

## Why agents make this worse

Every failure mode on this page predates agents. Agents change the economics of two of them.

An agent under a completion objective, facing a red gate, has a gradient available that a human under review usually does not: it can modify the check. Each individual step toward that is locally reasonable — the check looks wrong, the fix is small, the change is in the repository the agent is authorized to edit. This is the whole reason [Gates](GATES.md#non-negotiable-rules-for-gates-with-agents) forbids an agent from changing the gates within the flow those gates evaluate. Not because agents are adversarial, but because the shortest path from red to green runs through the check.

And an agent iterates faster than anyone reviews. A gate that silently stopped running in April is discovered by a human in weeks; by then an agent has produced hundreds of unverified commits on top of it. **The cost of a fail-open gate scales with the throughput of whoever is behind it**, which is the argument for the canary being cheap and frequent rather than thorough and annual.

## Declaring a degraded mode

When a check genuinely cannot run, the repository states so explicitly, with four fields: which gate, why it cannot run, what compensates for it in the meantime, and when the exception expires. An exception without an expiry is a permanent change to the verification architecture, and it goes through the harness owner and the changelog like any other ([Versioning](VERSIONING.md)).

Operating in a declared degraded mode also lowers the autonomy ceiling while it lasts. A repository missing a gate is, for the duration, at the verification level that missing gate can sustain — see [Gates](GATES.md#progressive-autonomy-and-the-harness-ceiling).

---

*Next: [Concurrency](CONCURRENCY.md) — what happens when several agents work at once.*
