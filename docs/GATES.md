# Gates

The gate architecture defines where each check occurs in the trajectory of a Work Item, from commit to deployment. The goal is for cheap feedback to arrive first and for nothing that can be verified by machine to reach a person.

## The complete staircase

| Layer | Latency | Check | Failure blocks |
|---|---|---|---|
| **Location** (sensors) | seconds | deterministic checks, low cost | commit or push |
| **CI** | minutes | build, testing, security, architecture in a clean environment | merge |
| **Merge** | consolidated decision | approvals, status checks, automation provenance | integration |
| **Environment** | before the exhibition | secrets, branches and artifacts allowed, approval by risk | deploy |
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

Placing an expensive check early locks the agent on each commit. Placing a cheap check late wastes an entire turn of IC to inform something that would be known in two seconds.

## CI — fast lane and deep lane

The repository's CI operates with two lanes, and the separation exists for economic reasons.

The **fast lane** runs with each push and returns the signal to the agent in minutes. It only covers the checks selected by the changed paths — it is not a complete treadmill. A single, full treadmill turns every attempt into a long wait, and the idle agent costs as much as the wrong agent.

**deep lane** runs before the merge or on schedule, and covers the entire battery: security, architecture, contracts, end-to-end testing. It exists to ensure that what passes through the fast lane also withstands more expensive verification.

## Non-negotiable rules for gates with agents

Three separations apply specifically when agents operate the repository, and cannot be relaxed:

The same agent does not produce and approve the change itself. This requires distinct and verifiable identities in the versioning system — prompt instructions are not enough, because protection needs to be structural.

Agents do not change gates within the same flow that those gates evaluate. Without this separation, the path of least resistance for a blocked agent becomes loosening the blockage.

Changing rules, sensors or CI automatically increases the risk and requires the harness owner, outside of the normal flow.

## Progressive autonomy and the harness ceiling

Gates support increasing levels of autonomy. The central rule: **the harness level is the ceiling of autonomy, never its consequence**.

| Level | The repository has | Sustained autonomy |
|---|---|---|
| **HL0 — naked** | README, eventual tests, build CI | none — watched |
| **HL1 — readable** | `AGENTS.md`, minimum rules, `verify.sh`, pre-commit | A0–A1 |
| **HL2 — verifiable** | CI by risk and paths, branch protection, evidence pack | A2 |
| **HL3 — operable by team** | repo skills, clean worktree, identities per agent, environment gates and post-deploy | A3–A4 |

A repository in HL1 operating with A2 autonomy is not an advanced repository — it is a repository with a missing gate that no one has noticed yet.
