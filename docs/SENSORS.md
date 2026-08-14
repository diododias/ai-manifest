# Sensors

Sensors are checks that run locally, before the code leaves the agent's machine. They are the first layer of the verification ladder — the cheapest to run, the ones that return feedback the fastest.

## `.hooks/` — versioned with the repository

The sensors are in `.hooks/` and are versioned along with the code. Any clone installs without manual configuration.

```bash
# install sensors from the repository
git config core.hooksPath .hooks
```

Versioned sensors eliminate the discrepancy between what the agent checks locally and what the team checks in CI — one of the most common sources of false positives and “works here, fails there.”

## Pre-commit

The pre-commit sensor runs with each commit and should complete in seconds. Its scope: deterministic and low-cost checks — formatting, linting, typecheck, affected unit tests and checking for accidental secrets.

Lint and typecheck are sensors, not gates — they are deterministic, run in seconds and fail often, which is exactly the profile of the local layer. Treating them as CI gates delays by minutes a signal the agent could have had before the commit.

A failure should indicate exactly what is wrong and how to fix it. A sensor that just says "failed" forces the agent to try again without information — each attempt wastes a cycle.

## Pre-push

The pre-push sensor rotates before the push and tolerates more time. It's the right place for checks that need greater context: local integration tests, architecture checks between modules, and checking that `scripts/verify.sh` passes completely.

The positioning criterion is the ratio between execution cost and failure frequency. Cheap check that fails frequently: pre-commit. Check that needs more context or time: pre-push.
