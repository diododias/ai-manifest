#04 — Rhythms and cadences

> What happens every day, every week, and at every milestone — regardless of whether any deliverables are in progress.

The journey describes the path of **a** Work Item. Rhythm describes what happens **every day**, whether or not there has been delivery. They are different axes, and confusing them produces the most common error when adopting the model: believing that, without an item in flight, there is nothing to operate.

There is always something operating. Standstill items do not generate their own event, learning dispersed across sessions does not consolidate on its own, and the cost of recurring friction only appears when someone adds up the occurrences. That's what cadences are for.

| Cadence | What runs | Output | Human time |
|---|---|---|---:|
| **Daily** | [☀️ Daily Loop](../loops/11-daily-operations.md) | briefing, memory, items in intake | ≤ 10 min reading |
| **By delivery** | checkpoints H1–H5, by event | registered decision | 30–45 min per delivery R1/R2 |
| **Weekly** | backlog screening and [🌙 Dream Loop](../loops/10-continuous-improvement.md) + H6 | ordered backlog, validated learning | 40–65 min |
| **By landmark** | risk and autonomy review | upgrade, maintenance or downgrade | 30–60 min |

---

## Daily — the pulse

Every beginning of the day, [☀️ Daily Loop](../loops/11-daily-operations.md) reads the sessions closed since the last run and returns a short briefing to the owner. It's the only cadence that runs even on a day without any deliveries.

### What the loop does

He separates four natures that cannot be read together — what was completed, what was pending, what failed and for what reason, and what only one person can decide — and converts each one into a different destiny.

| Nature | Destination |
|---|---|
| Recurring pattern with session evidence | `MEMORY.md` update proposal |
| Reproducible friction | Work Item in [🚦 Triage Loop](../loops/00-intake-and-triage.md) |
| Pending decision or blockage | owner briefing |
| Isolated occurrence | hypothesis under observation, weekly cycle input |

### What the owner does

Reading lasts a few minutes and has a mandatory order, which is the same in which the briefing is assembled.

1. **Blocked** — needs decision today. Each item contains the requested decision and the deadline. This is the only part that requires immediate action.
2. **At risk** — will block if no one takes action. Decide now or consciously accept that it becomes a blockage.
3. **In progress** — informative. It exists so that the owner knows where the work is, not so that he can approve anything.

The agenda only covers blockages, new information and requests for decisions. **What this rhythm should not turn into:** a daily individual reporting meeting. Narrating status is the function of the asynchronous artifact; the person enters to unlock.

### What leaves here and doesn't come back

Two departures from the daily rhythm cross the border and start to live elsewhere: the memory update, which goes to `MEMORY.md`, and the improvement, which becomes a Work Item in the intake. **No improvement is recorded only in the briefing** — the briefing is valid for one day, and what only exists in it disappears.

---

## By delivery — the checkpoints

This cadence has no calendar: it is triggered by event, according to [trigger map](03-gatilhos-e-disparos.md). A low-risk item goes through three human decisions; an R3/R4 item crosses up to six.

The property to preserve is that **checkpoint does not wait for meeting**. It arrives at the owner with the evidence pack assembled and is responded to asynchronously. Scheduling a checkpoint for the next ceremony converts minutes of decision making into days of waiting — and is the most common cause of high lead time in teams that have adopted the model correctly everywhere else.

Details of each checkpoint are in [Human Checkpoints](02-checkpoints-humanos.md).

---

## Weekly — screening and learning

The week has two distinct moments, with different owners and objects. One looks at the product; the other, for the system that builds the product.

### Priority screening

Owner: PM. Receives new Work Items, metrics, feedback, incidents, dependencies and capacity; returns the ordered backlog, with owner and initial risk assigned, and the list of what needs discovery.

The gate is simple: each item that leaves the triage has a minimally clear context, priority and person responsible. An item that does not achieve this returns to its origin as a question — it does not enter the backlog as an unknown.

This is also where the improvements that the daily and weekly rhythm produced come into play. **The work system competes for priority with the product, in the same queue.** Maintaining two separate queues ensures that the second one is never served.

### 🌙 Dream Loop and H6

Owner: trio. [🌙 Dream Loop](../loops/10-continuous-improvement.md) observes how the other loops behaved during the week — how many laps they took, where they climbed, what they cost — and separates patterns from isolated occurrences, with mandatory independent criticism.

The output goes to **H6**, which decides whether the system learned correctly. It is mandatory for sensitive memory changes, item P0/P1 and any gate change; the rest follows by sampling.

The relationship between the two learning cadences is a feeding one: the diary records hypotheses with session evidence; the weekly confirms or discards them against baseline. The complete comparison is in [☀️ Daily Loop contract](../loops/11-daily-operations.md#daily-and-weekly--why-there-are-two-loops).

---

## By milestone — risk and autonomy

The longest cadence has no fixed periodicity: it happens when there is enough material to decide. Two revisions take place here.

**Autonomy level review.** Verifies that all escalation criteria are present simultaneously — observed volume, escaped defects, reliable rollback, low false positives, correctly classified risk, auditable evidence, and actually reduced human time. A single missing criterion maintains the level.

**Review of risk classes and gates.** Checks whether the classes still describe the reality of the product and whether each gate still pays its own cost. A gate with a high false positive rate is not rigor: it is noise that trains the team to ignore the signal.

Both require a reviewer independent of whoever operates the harness, for the same reason that appears in [Papers](01-papeis.md): relaxing the verification that evaluates the work itself is the shortest path to the absence of verification.

---

## The rule that crosses the four rhythms

**Meetings exist to decide, not to narrate status.** Preparation, analysis, state update and artifact generation are handled by agents and automations; the person enters at the moment of decision.

The practical test of any rhythm in this model: if the ceremony can be replaced by a document read asynchronously without loss, it should have been that document. There are few left — and they are exactly those in which two or three people need to decide **together**, because the decision is shared by construction.

---

*Previous: [Triggers and shots](03-gatilhos-e-disparos.md) · Next: [Operator's manual](05-manual-do-operador.md).*
