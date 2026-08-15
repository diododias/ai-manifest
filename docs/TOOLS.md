# Tools

This page is the tooling index of the harness: which categories of tool an agent needs, what each one buys, and where on the verification ladder it runs. It answers *what to install*.

It does not answer *what the agent is allowed to invoke* — that is the permission layer, and it lives in [Permissions](PERMISSIONS.md). The distinction matters because the two age at different rates: a permission model is a property of the method and changes rarely, while a tool recommendation has a shelf life measured in months. Keeping them in one document made the stable half inherit the volatility of the other.

> **Reference index, reviewed 2026-08.** The named tools are the current default for each category at the time of this revision, not a mandate. A repository adopts the row that matches its stack and its gate placement. When a recommendation ages out, the category and the placement criterion around it stay valid — replace the name, keep the reasoning.

## `scripts/verify.sh`

The `verify.sh` script is the single entrypoint for all local checks. Hooks, CI and agent call the same script. Without this centralization, local and CI verification diverge — and the divergence appears in the most expensive form: the agent delivers, the CI fails, and no one can reproduce locally.

A single entrypoint and a sensor that returns in seconds are conflicting requirements unless the scope is an argument. The script takes one:

| Invocation | Covers | Called by |
|---|---|---|
| `verify.sh --staged` | only what is in the index | pre-commit |
| `verify.sh --affected` | the changed paths and what depends on them | pre-push |
| `verify.sh --full` | everything, no path selection | CI, and locally before requesting review |

The stages below are the `--full` body; the narrower modes run the same stages over a smaller file set. Keeping the selection inside the script — rather than letting each hook implement its own — is what stops local verification from quietly drifting away from CI.

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

As the repository matures past HL1, `verify.sh` typically grows additional stages beyond these four base gates — mutation coverage, dead code, and circular dependency checks are the most common additions. Each stage should stay an independent script (`test:mutation`, `deadcode:check`, `deps:circular`) so a failing stage can be run, skipped or debugged in isolation:

```bash
echo "→ mutation testing"
npm run test:mutation

echo "→ dead code"
npm run deadcode:check

echo "→ circular dependencies"
npm run deps:circular
```

These stages are more expensive than lint or typecheck and belong in pre-push or CI, not pre-commit — see [Sensors](SENSORS.md) and [Gates](GATES.md) for the placement criterion.

## LSP, lint and formatting

The Language Server Protocol (LSP) is the channel through which the agent receives real-time diagnostics without having to invoke a compiler or test runner. A repository with LSP configured returns type errors, invalid references, and lint warnings the moment the code is written — not the next time `verify.sh` runs.

Lint and deterministic formatting (Prettier, Black, gofmt) are not style checks: they are the first defense against divergence between what the agent generates and what the repository accepts. The configuration must be shared — `.eslintrc`, `pyproject.toml`, `.editorconfig` — and versioned along with the code. When lint and formatting run in pre-commit as sensors, the correction cycle is inside the agent machine.

Biome and Ruff are the current generation of these checks: single-binary, Rust-based tools that replace ESLint+Prettier (Biome, for JS/TS/JSON/CSS) or flake8+Black (Ruff, for Python) with one configuration file and order-of-magnitude faster runs. They are not mandatory — ESLint and Black remain valid choices — but a repository defining its lint stack today should default to them unless a plugin only exists in the older ecosystem.

## Typecheck and static analysis

Typecheck is a sensor, not a gate: it runs locally, in seconds, and belongs in pre-commit alongside lint — the cheapest layer of the verification ladder ([Sensors](SENSORS.md)). It is the cheapest way to catch broken contracts between modules. TypeScript (`tsc --noEmit`), mypy or Pyright, rustc and equivalents must be run before testing — a type error makes test results ambiguous.

Static analysis goes beyond type: it checks data flow, prohibited dependencies between modules (ArchUnit, dependency-cruiser) and patterns that lint does not capture. The result of a well-configured static analysis is that the agent knows, before opening a PR, whether the change violates an architectural boundary declared in the rules.

## Codebase navigation and understanding

An agent that browses the repository blindly — searching by string, opening files sequentially — wastes context without precision. Codebase understanding tools convert this cost into a targeted operation.

**Serena** ([oraios/serena](https://github.com/oraios/serena)) offers semantic navigation over the repository: finding declarations, listing implementations of an interface, mapping references of a symbol. Instead of grep, the agent uses `find_symbol`, `find_implementations`, `find_referencing_symbols` — and gets to the right point without linear scanning. It runs as an MCP server, operates at the symbol level across TypeScript, Python, Java, C# and more, and is the recommended starting point for any discovery task before implementation.

**dora-cli** complements Serena with a layer of observability over the development process itself — not the codebase, but how it was produced. It calculates the four DORA metrics (deployment frequency, lead time for changes, change failure rate, time to restore) directly from git and GitHub history. In repositories with multiple agent sessions operating in parallel, this is the signal that shows whether the pace of change is actually improving delivery, not just producing more commits.

**Graphify** goes a layer deeper than Serena: instead of point queries on demand, it builds a persistent knowledge graph of the entire repository up front — code, SQL schemas, configs and docs — using local AST parsing (tree-sitter), with zero LLM calls and nothing leaving the machine. The payoff shows up on large or unfamiliar repositories, where a single graph query replaces dozens of exploratory reads. It's a heavier setup than Serena and is worth adopting once discovery cost — not implementation cost — becomes the bottleneck.

## Reduction and context management

Context is the scarcest resource of an agent session. Loading it without criteria — entire files when only one symbol is needed, complete history when only the delta matters, raw command output when only the failure line matters — is the most direct path to long sessions that lose coherence.

**RTK** ([rtk-ai](https://github.com/rtk-ai)) is a single-binary CLI proxy that intercepts the output of common developer commands — `pytest`, `cargo test`, `go test` and 30+ others — and filters, compresses and reformats it before it reaches the agent's context. It strips boilerplate and redundant lines with sub-10ms overhead, typically removing 60–90% of the noise from a command's raw output.

**Repomix** packages an entire repository — respecting `.gitignore` — into a single AI-friendly file with per-file token counts and optional tree-sitter compression. It is the right tool when the task needs a one-shot snapshot of the codebase rather than incremental symbol lookups; Serena and Graphify remain preferable for targeted, repeated queries.

**Headroom** operates as a proxy or MCP server that compresses tool outputs, logs, files and RAG chunks before they reach the model, keeping the compressed originals retrievable on demand (compress-cache-retrieve). Reported reduction is 60–95% on structured output like JSON and logs, and around 20% on general coding-agent traffic.

A repository without any of these tools transfers the responsibility for deciding what to remember to the agent — and this decision, made without explicit instruction, tends toward excess.

## Structural code health

Lint and typecheck catch syntax-level and contract-level problems. A separate class of tool is needed for problems that are only visible at the level of the dependency graph or the design itself — problems that compile cleanly and pass every test, yet make the codebase harder to change safely over time.

**Circular dependencies.** Madge generates a visual dependency graph for JS/TS projects and flags cycles directly — it only catches direct cycles, not cycles that pass through a third module. `dependency-cruiser`, already covered above for architecture boundaries, also validates cycles and can be wired into ESLint via `eslint-plugin-dependency-cruiser`. `eslint-plugin-import`'s `no-cycle` rule catches the same class of problem inline during lint, without a separate tool. Python repositories use **import-linter** to enforce layered architecture and forbid cycles between modules — the same role ArchUnit plays for Java.

**Dead code.** **Knip** is the current default for JS/TS: it finds unused exports, unused files and unused dependencies by analyzing the manifest and source together, with an auto-fix mode and CI-friendly output (`ts-prune` covered a narrower slice of the same problem and is now in maintenance — prefer Knip for new setups). **Vulture** does the equivalent for Python via AST analysis with confidence scoring, which matters given how often Python's dynamic patterns produce false positives. **depcheck** narrows the scope further, to unused entries in `package.json` alone.

**SOLID and design smells.** SonarQube/SonarLint is the multi-language default and the one most repositories should start with, since it already covers lint, security and code smell in one pass. Where deeper design-level detection is needed: NDepend measures SOLID adherence directly for .NET; DesigniteJava classifies Java code smells by which design principle they violate; PMD and Checkstyle catch convention and complexity issues in Java that often correlate with SOLID violations even though they don't name the principle explicitly.

These checks are more expensive to interpret than lint — a circular dependency or a SOLID violation requires a judgment call about refactor scope, not just a fix. They belong in the deep CI lane described in [Gates](GATES.md), not pre-commit.

## Secrets and dependency risk

Two checks in this class differ from everything above in one respect: they fail on things the agent did not write.

**Secret scanning** is the only check on the ladder whose failure a later gate cannot undo. A credential that reaches the remote is compromised even after a revert, so the check runs before the object leaves the machine. **gitleaks** is the common default — single binary, regex plus entropy, fast enough for pre-commit; **trufflehog** goes further by verifying whether a found credential is live, which is worth its extra runtime in CI rather than in a hook. The platform's own push protection is the second line, never the first: it catches what the local sensor missed, and it catches it after the object exists.

**Dependency and supply chain checks** answer a question the repository's own tests cannot: whether the code it pulls in is safe to run. **Dependabot** or **Renovate** keep versions current and open the upgrade as a reviewable change; the review still applies, because an automated upgrade is a change like any other. **npm audit**, **pip-audit** and **osv-scanner** report known vulnerabilities against the manifest, and an **SBOM** (syft, or the platform's native generator) records what actually shipped, which is what an incident response needs and no lockfile provides after the fact. **Semgrep** and **CodeQL** cover the SAST slice — patterns that are dangerous rather than merely wrong.

Placement follows the usual criterion with one exception. Secret scanning is cheap and goes in pre-commit; SAST, SBOM and vulnerability scanning are expensive and belong in the deep lane. The exception is a dependency change: adding or upgrading a dependency runs the full set for that path before merge, because that is the moment the risk enters the repository, and because — as [Trust](TRUST.md#the-harness-is-a-supply-chain) covers — a new dependency of the *harness itself* is code with access to the agent's session.

## Tests, containers and observability

Tests are the most expensive layer of verification to run and most expensive to ignore. The separation between levels — unit, integration, contract, end-to-end — defines which tool is available at which gate. Unit tests run without external dependencies and belong to pre-commit. Integration tests require services and belong to pre-push or CI.

Mutation testing is the gate that answers a question coverage cannot: whether the existing tests would actually catch a regression, not just execute the line. **Stryker** covers JS/TS and, separately, .NET via Roslyn analyzers, with threshold-based CI gating (high/low/break) and HTML reporting. **PIT** is the equivalent for Java, with incremental analysis to keep runs fast on large suites. **mutmut** covers Python, with a `--CI` flag that produces pipeline-appropriate exit codes. Mutation testing is the most expensive item on the [testing ladder](RULES.md#the-testing-strategy-as-a-rule) and belongs at the end of the deep CI lane, run on a schedule or before merge — never per commit.

Containers (Docker, Testcontainers) are the mechanism that makes integration tests reproducible without shared state. A repository that doesn't use containers to isolate integration tests introduces environment dependency — and the agent that locally reproduces what the CI will run needs the same environment, not an approximation.

Observability — structured logs, distributed traces, baseline metrics — closes the post-deploy verification cycle. The difference between a deployment and a controlled rollout is that the second has a baseline defined beforehand and an objective rollback criterion if the baseline is violated. The agent does not decide rollback: it reads the observability signal and escalates if the criterion is met.

## Git hooks and local automation

Sensors need an installation mechanism that survives a fresh clone without manual setup. The default described in [Sensors](SENSORS.md) is native Git hooks versioned in `.hooks/` and activated with `git config core.hooksPath .hooks` — language-agnostic, zero dependencies, and the right default for polyglot or non-JS repositories.

**Husky** is the equivalent for JS/TS-centric repositories: it installs hooks automatically via an npm `prepare` script, so every `npm install` re-syncs `.husky/` without a manual `git config` step, and it is the convention most JS/TS contributors already expect. Adopt Husky over the native `.hooks/` approach when the repository is JS/TS-only and the onboarding friction of a manual `git config` step outweighs the value of staying language-agnostic; keep native hooks in any repository that mixes stacks or where hook logic needs to stay portable outside the npm ecosystem.

---

## All tools cited, classified by type of use

The table below consolidates every tool named in this document. It is a reference index, not a mandate — a repository adopts the row that matches its stack and gate placement, not the entire table.

| Tool | Type of use | Stack / notes |
|---|---|---|
| Serena | Codebase navigation | symbol-level, MCP server, multi-language |
| LSP (language server) | Codebase navigation | real-time diagnostics, IDE-level |
| Graphify | Knowledge graph / repo mapping | local AST (tree-sitter), 40+ languages, one-time build |
| dora-cli | Process observability / DORA metrics | reads git + GitHub history |
| RTK | Context reduction | CLI proxy, compresses command output |
| Repomix | Context reduction | one-shot repo packaging for LLM input |
| Headroom | Context reduction | proxy/MCP, compress-cache-retrieve |
| ESLint / Prettier | Lint & formatting | JS/TS |
| Biome | Lint & formatting | JS/TS/JSON/CSS, single binary |
| Black | Formatting | Python |
| Ruff | Lint & formatting | Python, single binary |
| gofmt | Formatting | Go |
| `tsc --noEmit` | Typecheck | TypeScript |
| mypy / Pyright | Typecheck | Python |
| rustc | Typecheck | Rust |
| ArchUnit | Architecture boundaries | Java |
| dependency-cruiser | Architecture boundaries / circular dependencies | JS/TS |
| import-linter | Architecture boundaries / circular dependencies | Python |
| Madge | Circular dependencies | JS/TS, direct cycles only |
| `eslint-plugin-import` (`no-cycle`) | Circular dependencies | JS/TS, inline with lint |
| Knip | Dead code / unused dependencies | JS/TS, successor to ts-prune |
| ts-prune | Dead code (legacy) | JS/TS, maintenance mode — prefer Knip |
| Vulture | Dead code | Python, AST + confidence score |
| depcheck | Unused dependencies | JS/TS, `package.json` scope only |
| SonarQube / SonarLint | SOLID / code smell / security | multi-language |
| gitleaks | Secret scanning | single binary, fast enough for pre-commit |
| trufflehog | Secret scanning | verifies whether a found credential is live; CI |
| Push protection (platform) | Secret scanning | second line, after the object exists |
| Dependabot / Renovate | Dependency updates | opens each upgrade as a reviewable change |
| npm audit / pip-audit / osv-scanner | Known vulnerabilities | manifest-based, per stack |
| Semgrep / CodeQL | SAST | dangerous patterns, deep lane |
| syft (SBOM) | Supply chain inventory | records what actually shipped |
| NDepend | SOLID adherence | .NET |
| DesigniteJava | Design smell classification | Java |
| PMD / Checkstyle | Convention / complexity | Java |
| Test runner (Jest, Vitest, pytest, `go test`, ...) | Unit & integration tests | per stack |
| Stryker | Mutation testing | JS/TS, .NET |
| PIT | Mutation testing | Java, incremental |
| mutmut | Mutation testing | Python, CI-friendly exit codes |
| Docker / Testcontainers | Container isolation | integration tests |
| Native Git hooks (`.hooks/` + `core.hooksPath`) | Local sensors / hooks | language-agnostic, repo default |
| Husky | Local sensors / hooks | JS/TS convention, npm-managed install |
| `scripts/verify.sh` (+ staged scripts) | Gate orchestration | single entrypoint for local checks and CI |

---

*Next: [Rules](RULES.md) — the desired state of the repository and the entry contract.*
