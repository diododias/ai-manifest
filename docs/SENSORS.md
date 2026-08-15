# Sensors

Sensors are checks that run locally, before the code leaves the agent's machine. They are the first layer of the verification ladder — the cheapest to run, the ones that return feedback the fastest.

## `.hooks/` — versioned with the repository

The sensors are in `.hooks/` and are versioned along with the code, so every clone carries the same checks the team runs.

```bash
# install the repository sensors — one time, per clone
git config core.hooksPath .hooks
```

Git does not activate versioned hooks on its own: `core.hooksPath` is local configuration, and a fresh clone runs no sensor until it is set. This one line is therefore part of setup, not a suggestion — it belongs in the bootstrap script and in the `AGENTS.md` commands block, and its absence is exactly the kind of silent gap that [Failure](FAILURE.md) exists to catch.

Versioned sensors eliminate the discrepancy between what the agent checks locally and what the team checks in CI — one of the most common sources of false positives and “works here, fails there.”

## Pre-commit

The pre-commit sensor runs with each commit and should complete in seconds. Its scope: deterministic and low-cost checks — formatting, linting, typecheck, affected unit tests and secret scanning.

Lint and typecheck are sensors, not gates — they are deterministic, run in seconds and fail often, which is exactly the profile of the local layer. Treating them as CI gates delays by minutes a signal the agent could have had before the commit.

Secret scanning belongs here for a different reason than the others. It is not placed early because it is cheap — it is placed early because it is the only check on the ladder whose failure cannot be undone by a later gate. A credential that reaches the remote is compromised even if the commit is reverted, so the check has to run before the object leaves the machine. `gitleaks` or `trufflehog` in pre-commit, and the platform's push protection as the second line, are the standard pairing.

A failure should indicate exactly what is wrong and how to fix it. A sensor that just says "failed" forces the agent to try again without information — each attempt wastes a cycle.

## Pre-push

The pre-push sensor runs before the push and tolerates more time. It's the right place for checks that need greater context: local integration tests, architecture checks between modules, and checking that `scripts/verify.sh` passes completely.

The positioning criterion is the ratio between execution cost and failure frequency. Cheap check that fails frequently: pre-commit. Check that needs more context or time: pre-push.

## Scope: how a single entrypoint stays fast

`scripts/verify.sh` is the single entrypoint for local checks ([Tools](TOOLS.md#scriptsverifysh)), and a sensor must return in seconds. Those two requirements only coexist if the entrypoint takes the scope as an argument:

| Invocation | Covers | Called by |
|---|---|---|
| `verify.sh --staged` | only what is in the index | pre-commit |
| `verify.sh --affected` | the changed paths and what depends on them | pre-push |
| `verify.sh --full` | everything, no path selection | CI, and locally before asking for review |

Without this contract the repository picks one of two failures: the hook calls the full script and the commit takes minutes, or the hook reimplements a narrower check and local verification quietly stops matching CI. The scope is an argument precisely so that the *logic* stays in one place while the *cost* varies by gate.

A sensor that is skipped must be reported as skipped, never as passed — see [Failure](FAILURE.md#a-gate-that-did-not-run-did-not-pass).

---

*Next: [Gates](GATES.md) — where each check belongs, from commit to deploy.*
