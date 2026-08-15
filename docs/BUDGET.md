# Budget

Every gate described so far blocks something that is wrong. This one blocks something that is merely not worth it — which is why it is the constraint most often left out, and the only one that fails upward while every indicator stays green.

An agent that loops for four hours on a two-line fix has broken no rule. The tests pass, the diff is clean, the evidence pack is complete. Nothing in the verification ladder has an opinion about the fact that the change cost more than the problem.

## Four dimensions, not one

| Dimension | Bounds | Runs out as |
|---|---|---|
| **Cost** | spend per Work Item | the finance question, and the easiest to measure |
| **Turns** | iterations before stopping | the non-convergence signal — an agent making no progress usually still makes attempts |
| **Wall-clock** | elapsed time before stopping | a hung tool or an external wait that will never return |
| **Context** | how much of the window a session has consumed | coherence loss, which shows up as quality decay rather than as an error |

The last one is the one that behaves unlike a budget and matters most for quality. Cost, turns and time degrade linearly and stop at a limit. Context degrades in a way the agent cannot self-report: a session that has consumed most of its window does not announce that it has started to lose the thread, it simply begins to contradict decisions it made earlier in the same task. Treating context as a budget with a threshold — checkpoint the state, start clean, carry forward the conclusions rather than the transcript — converts an invisible quality problem into a visible operational one.

## Exhaustion is an escalation, not a crash

A budget with no defined exhaustion behavior is worse than no budget, because it produces its damage at the least recoverable moment: mid-change, mid-migration, half a refactor applied.

Three behaviors are possible, and the default is the third:

**Abort.** Discard and stop. Correct only where the work is genuinely stateless, which after any file has been written is rarely true.

**Deliver partial.** Legitimate, but only against a contract: the work must be in a state that is coherent on its own — compiles, passes the gates for what it does contain, and touches nothing it left half-done. Partial delivery without that contract is not a delivery, it is an interrupted one.

**Escalate.** Stop, reach a resumable state, and hand back to a person with what was done, what remains, and what the obstacle was. This is the default because it is the only one that preserves the option to choose the other two.

The requirement common to all three is that **exhaustion is planned for, not detected**. An agent approaching its limit must reserve enough of the remaining budget to stop cleanly — writing the state, producing the evidence, leaving the tree consistent. A limit that is discovered at the moment it is crossed leaves exactly the mess it was meant to prevent. Budget exhaustion is listed as an [escalation condition](RULES.md#escalation-conditions) for this reason.

## What degrades, and what never does

Under pressure there is always something to drop. The order is not negotiable:

| Drop first | Never drop |
|---|---|
| Scope — deliver less, completely | Verification of what was delivered |
| Optional test levels flagged "on demand" | Test levels the change type makes mandatory |
| Exploration and alternatives considered | The evidence pack |
| Polish, refactoring adjacent to the change | The escalation, when a condition is met |

The line underneath: **reduce what is delivered, never how well it is verified.** A cheaper unverified change is not a cheaper change — it moves the cost to whoever finds the defect, at a worse exchange rate. An agent that cannot complete a change within budget *and* verify it has met an escalation condition, not a reason to skip the gate.

This is also the point where the budget interacts with autonomy. Lowering verification to fit a budget lowers the harness level for that change, and with it the autonomy the change was eligible for ([Gates](GATES.md#progressive-autonomy-and-the-harness-ceiling)).

## Budgets compose, and adversarial loops multiply

A per-agent budget is not a per-Work-Item budget. A loop with a producing agent, two adversarial reviewers and a revision round runs the item's budget several times over, and each participant is individually within its limit.

Two budgets are therefore declared:

- **Per agent invocation** — bounds a single run and is what `.agent/settings.json` carries.
- **Per Work Item** — bounds the total across every agent and every round the item consumes, and is the one that reflects what the work was worth.

Loops also need a stop condition that does not depend on success. An adversarial round can always find another objection; a critic can always request another revision. Without a maximum number of rounds, "converged" is indistinguishable from "still going", and the natural end state of an unbounded review loop is the budget running out rather than the work being right. The round limit is a convergence control first and a cost control second.

## Declaring and observing

The limits live in `.agent/settings.json` ([Permissions](PERMISSIONS.md)), because a budget is an operational limit like any other and changing it is a harness change.

Setting them requires data the repository will not have on day one. Start by measuring: the cost, turns and time of work items that were accepted without incident give the distribution, and the limit goes at its upper edge rather than at its mean — a budget set at the average stops half of the healthy work. **Cost per accepted Work Item** — not cost per run, which improves whenever quality drops — is the number that tells whether the system is getting cheaper or just faster at producing rework ([Metrics](METRICS.md)).

---

*Next: [Versioning](VERSIONING.md) — what happens to past approvals when the harness itself changes.*
