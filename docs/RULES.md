# Rules

Rules describe desired state, not procedure. "Domain modules must not import infrastructure" is a rule. "To add an adapter, create the interface in X and the implementation in Y" is a skill. The confusion between the two produces long rules that no one reads and vague skills that you can't execute.

Every rule carries the reason along with it. This is not editorial courtesy: an agent who knows the reason for a rule correctly decides in the edge case that the rule did not predict, while an agent who only knows the rule either applies it blindly or ignores it.

## Rules files

The rules are divided into separate files, each covering a different front. This separation is a context budget decision: rules are read on demand according to the task, not loaded in their entirety during every execution.

| File | Defines |
|---|---|
| `docs/rules/architecture.md` | modules, boundaries, permitted and prohibited dependencies |
| `docs/rules/coding.md` | conventions, accepted standards, naming, dependency injection |
| `docs/rules/testing.md` | mandatory levels by type of change |
| `docs/rules/security.md` | data, secrets, authentication, privacy |
| `docs/rules/operations.md` | SLOs, observability, rollout, rollback |

What `security.md` must answer is not a general policy statement but four operational questions: which data classes exist in this repository and which of them the agent may read; where secrets live and why the agent never holds a production credential; what a test runs against when the real data is regulated (synthetic or anonymized, never production); and which changes are security-relevant enough to require a named reviewer. A `security.md` that does not answer these is a policy document, not a rule file.

## `AGENTS.md` — the entry contract

`AGENTS.md` is read before any action, which makes each line of it a fixed cost per execution. It responds to what the agent needs to act correctly on the first attempt, and delegates the rest via pointer. Its blocks are:

| Block | Content | Common error |
|---|---|---|
| Identity | what the service does and for whom, in three sentences | rewrite the product pitch |
| Commands | install, build, test, verify, run local | list commands that no one uses anymore |
| Borders | what cannot be changed without authorization | describe the entire architecture |
| Verification | what needs to go through before considering it ready | duplicate CI configuration |
| Escalation | the conditions under which the decision is stopped and returned | omit — it's the most forgotten block |
| Pointers | where rules, ADRs, skills and evidence are located | inline the pointed content |

The escalation block is what is most lacking and what matters most. Without it, an agent faced with a contradictory requirement chooses an interpretation and follows through — and the choice only appears in the review, when the work has already been done.

## Escalation conditions

The agent must stop and return the decision in any of the following situations:

- Contradictory requirement or without defined owner
- Two or more correction attempts without progress on the same failure
- Change outside the approved scope
- Need for new permission or external access
- Non-reproducible failure or inconsistent evidence
- Irreversible decision, or one whose blast radius cannot be calculated — see [Reversibility](#reversibility-is-an-entry-requirement)
- Divergence between agents without objective tiebreaker criteria
- Budget for the work item exhausted before the completion gate — see [Budget](BUDGET.md)

Every condition on this list is observable by a third party from the outside: a missing owner, a repeated failure, a diff that leaves the declared scope. This is deliberate. **A model's self-reported confidence is not an escalation criterion** — it is not calibrated, it is not comparable between models, and a numeric threshold in a configuration file produces the appearance of a control without the mechanism of one. Escalation triggers on facts about the work, never on how sure the agent says it is.

## Reversibility is an entry requirement

Rollback is usually treated as a post-deploy concern. For a repository operated by agents it is an admission criterion: whether a change is allowed to be produced autonomously depends on how it is undone.

| Class | Undo path | Rule |
|---|---|---|
| Pure code change behind existing tests | revert the commit | autonomous |
| Behavior change reaching users | flag off, then revert | flag is a precondition of the change, not a follow-up |
| Additive schema change | revert the code, leave the column | autonomous only if the migration is backward compatible |
| Destructive schema or data change | restore from backup | never autonomous — named owner plus ADR |
| Change to a rule, sensor, gate or CI configuration | revert plus re-verification of what passed meanwhile | harness owner, outside the flow that the gate evaluates |

The rule underneath the table: **a change that cannot be undone with one command requires human authorization and an ADR recording why it was accepted anyway.** An agent that cannot classify its own change into one of these rows has already met an escalation condition.

## The testing strategy as a rule

The testing strategy deserves to be highlighted because it is the rule that the gates translate directly into blocking. The complete ladder is:

```
unit → architecture → integration → contract → end-to-end → accessibility → mutation
```

The rule defines which levels are mandatory per type of change. Without this mapping, the agent either writes too few tests — and the gate fails late — or writes too many tests, increasing the cost per delivery without gaining security.

The mapping belongs in `docs/rules/testing.md` and is specific to each repository. The matrix below is the reference shape it takes — a starting point to adapt, not a standard to copy:

| Type of change | Mandatory | On demand | Runs at |
|---|---|---|---|
| Internal refactor, no behavior change | unit, architecture | mutation on the touched module | pre-commit, pre-push |
| New domain rule | unit, architecture | — | pre-commit, pre-push |
| New or changed module boundary | unit, architecture | — | pre-push, deep lane |
| Change to a published API or event | contract, integration | end-to-end | deep lane |
| Change to persistence or schema | integration, contract | end-to-end | deep lane |
| Change to a user-facing flow | end-to-end, accessibility | — | deep lane |
| Change to authentication, authorization or secret handling | unit, integration, contract | mutation on the touched module | deep lane, named reviewer |
| Dependency upgrade | the full ladder for the affected paths | — | deep lane |

Two properties make this matrix usable rather than decorative. Each row names the gate the level runs at, so the [positioning criterion](GATES.md#where-each-check-belongs) is already resolved and the agent does not re-derive it per task. And the "on demand" column exists so that an expensive level is a deliberate request with a stated reason, never a default that inflates every delivery.

---

*Next: [Sensors](SENSORS.md) — the local checks that run before the code leaves the machine.*
