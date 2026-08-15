# Metrics

The method states that autonomy increases by metric. This page names the metrics, because a rule that grants authority on evidence is only as good as the evidence it accepts — and "it has been working well" is not evidence, it is the absence of a signal that anything went wrong.

A distinction first, since the two are routinely conflated: DORA metrics measure *delivery* — how often, how fast, how safely the team ships. They say nothing about the harness. A repository can improve every DORA number by lowering its gates. What follows measures the verification system itself.

## The one that matters most

**Gate escape rate** — defects that passed every gate and were found later, per unit of delivered work.

It is the only metric that directly answers the question the harness exists to answer. Everything else is a leading indicator of it, and a green pipeline is not a substitute: a pipeline reports what the gates caught, and the escape rate reports what they did not.

Two properties make it usable. It is measured *per escape point* — found in review, in staging, in production, by a customer — because the cost differs by an order of magnitude at each step and the trend across them says which gate is weakening. And it is attributed to the gate that *should* have caught it, not to whoever wrote the change: the output of the measurement is a gate to fix, never a person to talk to.

## The rest of the panel

| Metric | Reads as | Degrades into, if optimized directly |
|---|---|---|
| **Escalation rate** | how often the agent stops and returns the decision | agents that never stop — see below |
| **Rework after merge** | change reopened or corrected within N days | smaller, more numerous work items |
| **Feedback latency per layer** | seconds at the sensor, minutes at the fast lane, hours at the deep lane | checks moved to a cheaper layer than they belong in |
| **Skip and degraded rate** | gates reported `skipped`, runs that needed a retry ([Failure](FAILURE.md)) | quarantines that are never revisited |
| **Cost per accepted Work Item** | total spend across every agent and round, divided by items accepted | quality dropped to make runs cheaper |
| **Evidence completeness** | packs a third party could re-verify unaided | template-filling |
| **Review latency vs. review depth** | time between a change being ready and a human deciding | approvals faster than the change could be read |

The escalation rate is the one that is misread most often. A high rate looks like an agent that cannot work independently, and sometimes is. A rate near zero is the alarming one: it means either that the repository has no ambiguity — which no repository has — or that the escalation conditions are not firing, and the agent is choosing an interpretation and proceeding every time it meets a contradiction. The failures that produces do not appear in this panel at all. They appear in the escape rate, weeks later.

The last row is the rubber-stamp detector. An approval issued faster than the diff could plausibly have been read is not an approval; it is a bottleneck resolving itself. It is worth measuring precisely because it is the control that degrades silently as agent throughput rises, and because the fix is never "read faster" — it is fewer, better-verified changes reaching the human gate.

## Metrics gate the level, in both directions

The maturity ladder is a claim about what a repository can verify. These metrics are how the claim is checked, and the check runs continuously rather than at promotion time:

**Promotion** requires the level's artifacts to exist ([Maturity](MATURITY.md)) *and* the panel to hold at the current level for a sustained window. Artifacts alone measure intent — a gate that exists and has never rejected anything has not been shown to work.

**Demotion** is the half that is usually missing, and it is what makes the ladder a control rather than a ceremony. A rising escape rate, a rising skip rate, or an escalation rate that collapses are each grounds for lowering autonomy until the cause is found. A ladder that only goes up records history, not capability.

## What not to measure

Three temptations, each of which produces a worse system than measuring nothing:

**Per-agent rankings.** Comparing agent roles by throughput or defect count optimizes the wrong unit. The output of this panel is a change to a contract, a rule, a tool or a gate — the harness is what improves, and an agent is only ever evidence about it. This is the same commitment the method makes about people, for the same reason.

**Volume.** Commits, lines, pull requests, tokens consumed. Every one of them rises when the system gets worse, and agents can produce any quantity of any of them on demand.

**Gate pass rate as a health signal.** A gate that always passes is either verifying nothing or being routed around, and both look like excellence on a dashboard.

## Where the numbers come from

Most of the panel is already recorded by the machinery of the previous pages, which is what makes it affordable: `gate-status.json` carries skip and degraded rates, `attestation.json` carries the rules and model each item was produced under, the evidence pack carries verification output, and the version control history carries rework and review latency. What has to be added deliberately is the escape — someone has to record, when a defect is found, which gate should have caught it. That single field is the difference between a panel that describes activity and one that measures verification.

---

*Next: [Maturity](MATURITY.md) — what each level requires, and how to find out where a repository actually stands.*
