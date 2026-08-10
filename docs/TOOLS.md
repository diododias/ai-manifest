#Tools

The harness permission layer defines which tools the agent is authorized to invoke, with what limits, and what requires human authorization before proceeding. This definition is structural — it doesn't live in prompt statements, but in versioned files within the repository.

## `.agent/settings.json`

The `settings.json` file declares the operational limits of the agent in that repository: which tools are allowed, which are explicitly prohibited, which models can be used and what is the trust threshold below which the agent must scale. An agent that does not find this file should treat the repository as not authorized for unattended operation.

```json
{
  "tools": {
    "allowed": ["read_file", "write_file", "run_tests", "run_lint"],
    "forbidden": ["delete_branch", "force_push", "modify_ci"]
  },
  "models": {
    "default": "claude-sonnet-5",
    "max_cost_per_task_usd": 2.00
  },
  "escalation": {
    "confidence_threshold": 0.85,
    "max_retries_before_escalation": 2
  }
}
```

## `.agent/permissions.md`

The `permissions.md` file describes, in natural language, what requires human authorization in that specific repository. It complements `settings.json` with the judgment that no JSON can capture: when the situation is ambiguous enough to stop.

Typical categories covered by this file include paths that require ownership before making any changes, operations that alter persisted state (migrations, schemas, secrets), irreversible actions with a limited rollback window, and any changes that affect the verification gates themselves.

## `scripts/verify.sh`

The `verify.sh` script is the single input for all local checks. Hooks, CI and agent call the same script. Without this centralization, local and CI verification diverge — and the divergence appears in the most expensive form: the agent delivers, the CI fails, and no one can reproduce locally.

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "→ lint"
npm run lint

echo "→ typecheck"
npm run typecheck

echo "→ unit tests"
npm run test:unit

echo "→ architecture check"
npm run arch:check

echo "✓ verify.sh completed"
```

The script should produce actionable messages in case of failure — file, rule violated, and expected fix. A gate that only says "failed" transfers the work it existed to avoid to human review.

## LSP, lint and formatting

The Language Server Protocol (LSP) is the channel through which the agent receives real-time diagnostics without having to invoke a compiler or test runner. A repository with LSP configured returns type errors, invalid references, and lint warnings the moment the code is written — not the next time `verify.sh` runs.

Lint and deterministic formatting (Prettier, Black, gofmt) are not style checks: they are the first defense against divergence between what the agent generates and what the repository accepts. The configuration must be shared — `.eslintrc`, `pyproject.toml`, `.editorconfig` — and versioned along with the code. When lint and formatting run in pre-commit as sensors, the correction cycle is inside the agent machine.

## Typecheck and static analysis

Typecheck is the cheapest gate to catch broken contracts between modules. TypeScript (`tsc --noEmit`), mypy, rustc and equivalents must be run before testing — a type error makes test results ambiguous.

Static analysis goes beyond type: it checks data flow, prohibited dependencies between modules (ArchUnit, dependency-cruiser) and patterns that lint does not capture. The result of a well-configured static analysis is that the agent knows, before opening a PR, whether the change violates an architectural boundary declared in the rules.

## Codebase navigation and understanding

An agent that browses the repository blindly — searching by string, opening files sequentially — wastes context without precision. Codebase understanding tools convert this cost into a targeted operation.

**Serena** offers semantic navigation over the repository: finding declarations, listing implementations of an interface, mapping references of a symbol. Instead of grep, the agent uses `find_symbol`, `find_implementations`, `find_referencing_symbols` — and gets to the right point without linear scanning. Serena is the recommended starting point for any discovery task before implementation.

**Dora** complements Serena with a layer of observability over the development process itself: it tracks what was touched, what changed between sessions, and where the work stopped. In repositories with multiple agent sessions operating in parallel, Dora is the mechanism that prevents two sessions from working on the same region without coordination.

## Reduction and context management

Context is the scarcest resource of an agent session. Loading it without criteria — entire files when only one symbol is needed, complete history when only the delta matters — is the most direct path to long sessions that lose coherence.

**RTK (Repo Tool Kit)** is the repository context management toolset. It exposes selective reading operations — reading only the symbols relevant to the current task, retrieving the state of a previous session without reloading the entire history, and compressing already scanned evidence before it takes up space from what is still being worked on. A repository without RTK transfers the responsibility for deciding what to remember to the agent — and this decision, made without explicit instruction, tends toward excess.

## Tests, containers and observability

Tests are the most expensive layer of verification to run and most expensive to ignore. The separation between levels — unitary, integration, contract, end-to-end — defines which tool is available at which gate. Unit tests run without external dependencies and belong to pre-commit. Integration tests require services and belong to pre-push or CI.

Containers (Docker, Testcontainers) are the mechanism that makes integration tests reproducible without shared state. A repository that doesn't use containers to isolate integration tests introduces environment dependency — and the agent that locally reproduces what the CI will run needs the same environment, not an approximation.

Observability — structured logs, distributed traces, baseline metrics — closes the post-deploy verification cycle. The difference between a deployment and a controlled rollout is that the second has a baseline defined beforehand and an objective rollback criterion if the baseline is violated. The agent does not decide rollback: it reads the observability signal and scales if the criterion is met.
