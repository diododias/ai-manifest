# Gates

The gate architecture defines where each check occurs in the trajectory of a Work Item, from commit to deployment. The goal is for cheap feedback to arrive first and for nothing that can be verified by machine to reach a person.

## The complete staircase

| Layer | Latency | Check | Failure blocks |
|---|---|---|---|
| **Local** (sensors) | seconds | deterministic checks, low cost | commit or push |
| **CI** | minutes | build, testing, security, architecture in a clean environment | merge |
| **Merge** | consolidated decision | approvals, status checks, automation provenance | integration |
| **Environment** | before exposure | secrets, branches and artifacts allowed, approval by risk | deploy |
| **Post-deploy** | observation window | comparison with baseline, regression, automatic rollback | rollout |

## Where each check belongs

The positioning criterion is the ratio between execution cost and failure frequency:

| If the check… | …belongs to | Why |
|---|---|---|
| runs in seconds and fails frequently | pre-commit | fixing costs almost nothing and the loop is immediate |
| need a container or external service | pre-push or CI | unfeasible with each commit |
| depends on clean environment or full build | CI | local result is not reliable |
| requires judgment on risk or trade-off | merge | it's decision, not verification |
| is only observable with real traffic | post-deploy | there is no way to anticipate |

Placing an expensive check early locks the agent on each commit. Placing a cheap check late wastes an entire turn of an agent to inform something that would be known in two seconds.

## CI — fast lane and deep lane

The repository's CI operates with two lanes, and the separation exists for economic reasons.

The **fast lane** runs with each push and returns the signal to the agent in minutes. It only covers the checks selected by the changed paths — it is not the full pipeline. A single, full pipeline turns every attempt into a long wait, and the idle agent costs as much as the wrong agent.

The **deep lane** runs before the merge or on schedule, and covers the entire battery: security, architecture, contracts, end-to-end testing. It exists to ensure that what passes through the fast lane also withstands more expensive verification.

The economics only hold if the fast lane's path selection is itself verified. A path filter that silently stops matching — a renamed directory, a new module outside the glob — converts the fast lane into a green light for unchecked code. Treat the filter as a gate that needs its own test, as described in [Failure](FAILURE.md#verifying-the-verifier).

## The environment gate

The environment layer is where the repository stops being a repository and starts being exposure. Three rules define it, and none of them is about the code:

**The agent never holds a production credential.** Deployment runs through an identity the agent can trigger but not impersonate — a pipeline with its own secrets, invoked by an authorized event. An agent that can read the production secret can exfiltrate it, and every downstream control assumes it cannot.

**Tests never run against production data.** Where the data is regulated, the environment provides a synthetic or anonymized set. "Read-only access to production" is not a mitigation: reading is the incident when the data is the asset.

**Approval scales with exposure, not with diff size.** A one-line change to an authentication path crosses a higher gate than a hundred-line change to an internal utility. The risk classification lives in `docs/rules/operations.md` and `docs/rules/security.md`; the gate reads it rather than re-deriving it.

## Non-negotiable rules for gates with agents

Three separations apply specifically when agents operate the repository, and cannot be relaxed:

The same agent does not produce and approve the change itself. This requires distinct and verifiable identities in the versioning system — prompt instructions are not enough, because protection needs to be structural. What that identity has to carry, and how it is attested, is in [Documentation](DOCUMENTATION.md#identity-and-provenance).

Agents do not change gates within the same flow that those gates evaluate. Without this separation, the path of least resistance for a blocked agent becomes loosening the blockage.

Changing rules, sensors or CI automatically increases the risk and requires the harness owner, outside of the normal flow. Because such a change also invalidates approvals granted under the previous version, it is versioned rather than merely reviewed — see [Versioning](VERSIONING.md).

## Progressive autonomy and the harness ceiling

Gates support increasing levels of autonomy. The central rule: **the harness level is the ceiling of autonomy, never its consequence**.

| Level | The repository has | Sustained autonomy |
|---|---|---|
| **HL0 — naked** | README, eventual tests, build CI | none — watched |
| **HL1 — readable** | `AGENTS.md`, minimum rules, `verify.sh`, pre-commit | A0–A1 |
| **HL2 — verifiable** | CI by risk and paths, branch protection, evidence pack | A2 |
| **HL3 — operable by team** | repo skills, clean worktree, identities per agent, environment gates and post-deploy | A3–A4 |

A repository in HL1 operating with A2 autonomy is not an advanced repository — it is a repository with a missing gate that no one has noticed yet.

The level is a claim about the repository, and a claim needs a way to be checked. What each level requires, item by item, and how a repository measures the level it is actually at, is in [Maturity](MATURITY.md).

## What the staircase does not cover

Three failure modes cross every layer of the staircase instead of sitting on one step, which is why each has its own document rather than a row in the table above:

| Failure mode | Why no single gate catches it | Where |
|---|---|---|
| The gate itself does not run, or passes for the wrong reason | it is the verification that failed, not the change | [Failure](FAILURE.md) |
| Evidence was valid when produced and the base moved underneath it | each gate passed, on a state that no longer exists | [Concurrency](CONCURRENCY.md) |
| The work consumed more than it was worth | nothing is broken, so nothing blocks | [Budget](BUDGET.md) |

---

*Next: [Documentation](DOCUMENTATION.md) — ADRs, evidence pack and the complete file structure.*
