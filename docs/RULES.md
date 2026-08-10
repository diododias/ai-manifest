#Rules

Rules describe desired state, not procedure. "Domain modules don't matter infrastructure" is a rule. "To add an adapter, create the interface in X and the implementation in Y" is a skill. The confusion between the two produces long rules that no one reads and vague skills that you can't execute.

Every rule carries the reason along with it. This is not editorial courtesy: an agent who knows the reason for a rule correctly decides in the edge case that the rule did not predict, while an agent who only knows the rule either applies it blindly or ignores it.

## Rules files

The rules are divided into separate files, each covering a different front. This separation is a context budget decision: rules are read on demand according to the task, not loaded in their entirety during every execution.

| Archive | Define |
|---|---|
| `docs/rules/architecture.md` | modules, boundaries, permitted and prohibited dependencies |
| `docs/rules/coding.md` | conventions, accepted standards, naming, dependency injection |
| `docs/rules/testing.md` | mandatory levels by type of change |
| `docs/rules/security.md` | data, secrets, authentication, privacy |
| `docs/rules/operations.md` | SLOs, observability, rollout, rollback |

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

The scaling block is what is most lacking and what matters most. Without it, an agent faced with a contradictory requirement chooses an interpretation and follows through — and the choice only appears in the review, when the work has already been done.

## Escalation conditions

The agent must stop and return the decision in any of the following situations:

- Contradictory requirement or without defined owner
- Confidence below the threshold declared in `settings.json`
- Two or more correction attempts without progress
- Change outside the approved scope
- Need for new permission or external access
- Non-reproducible failure or inconsistent evidence
- Irreversible decision or non-calculable impact
- Divergence between agents without objective tiebreaker criteria

## The testing strategy as a rule

The testing strategy deserves to be highlighted because it is the rule that the gates translate directly into blocking. The complete ladder is:

```
unitary → architecture → integration → contract → end-to-end → accessibility → mutation
```

The rule defines which levels are mandatory per type of change. Without this mapping, the agent either writes too few tests — and the gate fails late — or writes too many tests, increasing the cost per delivery without gaining security.
