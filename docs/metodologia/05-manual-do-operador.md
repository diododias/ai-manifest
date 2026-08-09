#05 — Operator’s manual

> How to operate in practice: what to open, in what order, how to dispatch, how to read an output and how to intervene without breaking the flow.

The previous pages describe the model. This describes **usage**. It answers the question of those who sit down to work and need to know what to do first — and, above all, what to do when something doesn't go as the contract stipulated.

The principle that organizes everything here: **you operate by exception.** Healthy flow doesn't need you. What comes to you is a decision, a block or an anomaly — and for each one there is a valid response, a mandatory record and a limit to what can be done without involving another person.

---

## The day, in order

The sequence below applies to the three roles. What changes is the content, not the order.

1. **Daily Briefing.** Open `.coordination/daily/<data>.md`, produced by [☀️ Daily Loop](../loops/11-daily-operations.md). Read the *blocked* section first and answer the one that has a deadline today. The remaining sections are reading, not action.
2. **Pending checkpoints.** Respond to accumulated H. Each one arrives with an evidence pack; if it hasn't arrived, it's not ready to be responded to — returning it for that reason is a valid response.
3. **Open escalations.** Check what has stopped waiting for a decision. An unanswered escalation for more than one daily cycle reappears prominently in the following day's briefing.
4. **Dispatch.** Start what was prioritized, with the complete mission identity.
5. **Nothing else.** If after that there is nothing waiting for you, the flow is healthy. Monitoring ongoing execution is not an operation — it is anxiety with the appearance of rigor.

### What each role opens

| Paper | First | After |
|---|---|---|
| **PM** | product blocks and pending H1/H2 | sorting queue, improvements awaiting ordering |
| **UX** | Pending H2 and experience acceptances | items in discovery awaiting evidence |
| **Tech Lead** | technical escalations, H3/H4/H5 | gates health, rollout items, harness |

---

## Dispatch a mission

A mission should only be performed with full identity. **Missing field is blank authorization** — the agent will fill in the gap with the most plausible assumption, and the assumption will only appear in the critique or, worse, in the CI gate.

| Block | What to declare |
|---|---|
| Identification | mission, Work Item, step and agent role |
| Authority | human sponsor and owner of the decision |
| Direction | objective, expected result, scope and **out of scope** |
| Sources | canonical sources, input and output artifacts |
| Verification | acceptance criteria and applicable gates |
| Limits | risk class, authorized autonomy, tools, permissions and budget |
| Stop | stopping condition and for those who climb |

Before shipping, the item must satisfy the *Definition of Ready* described in [Papers](01-papeis.md). Dispatching without it doesn't speed up anything: it transfers the ambiguity to the inside of the execution, where discovering it costs an external turn.

The most neglected field is **out of scope**. It is not redundant with the scope: it is what prevents the agent from solving an adjacent problem that no one asked for, and which now needs to be revised.

---

## Read an output without rereading the execution

Every mission ends in a standardized envelope. It exists so that no one needs to reread the entire session to find out what happened.

| Field | What to watch out for |
|---|---|
| `status` | `completed`, `partial` or `blocked` — `partial` requires reading of pending issues |
| `confidence` | `low` should never be approved without additional verification |
| `skills_used` | unused sticky skill is a sign of a reinvented procedure |
| `sources_used` | non-canonical source is a sign of context reconstructed by assumption |

### Read an evidence pack

The evidence pack supports the decision. Efficient reading follows three movements, in this order: **delta** (what has changed since the last time you looked), **pending** (what remains open and why) and **evidence** (the raw result of the gates, consulted only if something in the previous two does not add up).

Package quality testing is objective: **can someone else redo the check without asking anyone who produced it?** If you need additional context, what you got is a summary, not evidence — and returning it for that reason is the correct answer.

---

## Respond to an escalation

An agent escalates when it encounters a contradictory or unowned requirement, confidence below the threshold, two or more correction attempts without progress, change outside the approved scope, need for new access, non-reproducible failure, irreversible decision, or divergence between agents without objective tiebreaker criteria.

There are five valid answers. Choosing between them is the most frequent operation of the model.

| Answer | When | What to register |
|---|---|---|
| **Decide** | the information exists and the decision is yours | the decision and the reason |
| **Clarify** | context is missing, and the agent can go with it | enlightenment as part of the artifact, not as a message |
| **Reduce scope** | some of the work is executable and some is not | new out of scope, explicitly |
| **Return to a previous loop** | the problem was born before this stage | the question that prompted the return |
| **Close** | item should not proceed | the reason, and the bond if it was absorbed by another item |

What is **not** a valid answer: having them try again without changing anything. If nothing has changed at the input, the output will be the same, and the cost of the return is real.

---

## Intervene without breaking the flow

Interventions are normal and expected. What makes them safe is the registration — an unregistered intervention disappears from the history and distorts the telemetry that [🌙 Dream Loop](../loops/10-continuous-improvement.md) uses to improve the design of the loops.

| Intervention | Effect | Who can | Registration |
|---|---|---|---|
| **Stop** a loop in progress | interrupts before next handoff | loop owner | reason and state in which it stopped |
| **Revert** a rollout | removes exposure | Tech Lead | observed signal and decision |
| **Reduce scope** | preserves partial advance | PM | new out of scope |
| **Increase risk** | adds gates and approvals | any of the trio | what motivated the increase |
| **Open exception** | releases the advance with declared debt | Tech Lead | ADR with term and reversion plan |
| **Downgrade autonomy** | reintroduces checkpoints | Tech Lead | the metric that motivated |

About the finer line: **making an exception is different from ignoring the gate.** The exception declares the debt, names the deadline and describes how to get out of it. A bypass without these three elements is no exception — it is the gate ceasing to exist for that case, and nothing in the system will register this.

And about the last one: **decreasing autonomy is normal operation**, not failure. Autonomy rises through evidence and descends through the same route. A system in which it only goes up is measuring poorly.

---

## What to do when the model seems to get in the way

Three recurring situations, with the correct reading of each one.

**"The checkpoint arrived without what I need to decide."** The evidence pack is incomplete. Returning is the correct answer, and returning is a given: if it happens frequently, the problem is with the package template, not the step. Forward as improvement.

**"The gate failed something that is okay."** It's a false positive, and false positives are measured. A gate with a high index is not rigor — it is noise that trains the team to ignore the signal. Record the occurrence and take the change from the gate to the appropriate path, which requires an independent reviewer.

**"I would resolve this faster by hand."** Probably yes, once. The relevant question is whether the case repeats itself. If so, it is a missing skill or automation, and resolving it manually is what prevents this from appearing. If not, resolving it by hand is legitimate — as long as the result reaches the canonical source like any other artifact.

---

## What to never do

| Never | Why |
|---|---|
| Approve without evidence pack | approval is now based on the summary of whoever produced |
| Leaving a checkpoint unanswered as a form of refusal | silence is not approval, but it is also not a decision — the item just for |
| Expand the scope of an ongoing mission | the risk was classified according to the original scope |
| Edit an approved artifact without reopening the decision | material change invalidates related approval |
| Resolve a domain conflict by consensus without owner | reappears as a rework in the first dispute |
| Change a gate within the flow it is evaluating | is the definition of a judge in his own case |

---

*Previous: [Rhythms and cadences](04-ritmos-e-cadencias.md) · Next: [Commented journey](06-jornada-comentada.md).*
