# 4. Loops

---

## Overview — How Loops Work

A **loop** is the collaboration contract for a stage of the journey: who executes it, in what order, what crosses the boundary between agents and what condition needs to be true to move forward. It's what the literature calls *multi-agent workflow* — and this manifesto calls it a loop because the word better describes what actually happens.

A workflow, in common usage, suggests a conveyor belt: it enters on one side, leaves on the other. A loop with agents does not behave like this. It spins. The agent tries, the sensor fails, the agent corrects, the critic contests, the consolidator responds, the gate returns. **Successful execution is the case where the spin converges quickly, not the case where there was no spin.** A process designed for the treadmill treats each turn as an exception and does not instrument any of them; a process designed as a loop declares where the correction happens and how much it costs.

### What a loop is — and what it isn't

Three layers of the harness answer different questions, and confusing them produces documentation that no one can execute.

| Layer | Reply | Where do you live |
|---|---|---|
| **Skill** | *how* a recurring task is performed correctly | [`SKILLS.md`](SKILLS.md), `skills/<skill>/SKILL.md` |
| **Agent** | *who* executes, under what authority and with what limits | [`AGENTES.md`](AGENTES.md), [`agentes/`](agentes/README.md) |
| **Loop** | *in what order*, what crosses the border and when to stop | this page, [`loops/`](loops/README.md) |

A loop does not redefine any agent's contract, does not expand anyone's autonomy and does not create its own gates. He composes pieces that already exist. When a loop needs permission that the agent doesn't have, the problem is with the agent's contract — not the loop.

### The three laps

Every loop contains three nested circuits, with costs of different orders of magnitude. Recognizing them is what allows you to decide where a check should live.

| Return | Circuit | Typical frequency | Cost | Who closes |
|---|---|---|---|---|
| **Internal** | agent ↔ local sensors | dozens per mission | seconds | the agent himself |
| **Average** | consolidation ↔ independent review | one to three per stage | minutes to hours | the consolidating agent |
| **External** | gate ↔ previous step or human owner | zero to two per stage | hours to days | the CI gate or the owner |

The principle that follows from this applies to the design of any loop: **a detectable failure in the inner loop that only appears in the outer loop costs three orders of magnitude more and consumes human judgment that should be elsewhere.** Every check has a natural loop. Placing it further out than necessary is the most common — and most expensive — defect in loop design.

There is also a fourth round, of a much longer period, in which **the work system is the object of the work**. It rotates by calendar, and not by Work Item, in two windows: the [☀️ Daily Loop](loops/11-daily-operations.md) reads the previous day's sessions and converts what happened into memory, improvement and signaling to the owner; [🌙 Dream Loop](loops/10-continuous-improvement.md) reads the period with aggregated telemetry and independent critique, and feeds back into the design of the loops themselves.

### Anatomy of a loop

A loop carries no knowledge of its own. It coordinates versioned layers that [repo harness](REPO_HARNESS.md) makes available — the same ones that an agent consumes, now seen in the step dimension.

| Element | Define | If missing |
|---|---|---|
| **Input** | required artifacts and criteria for starting | the loop starts on incomplete material and discovers it in the review |
| **Missions** | what runs in sequence and what runs in parallel | concurrent work collides or serializes unnecessarily |
| **Consolidation** | the only agent responsible for the exit | the output becomes a pile of isolated answers |
| **Handoffs** | what crosses the boundary between agents | the next agent reconstructs the context by guess |
| **Exit gate** | what needs to be true to move forward | the judgment of "ready" rests with whoever produced it |
| **Scaling** | stopping condition and human owner of the decision | the agent decides on his own what is not up to him |

The absence of any of these six items makes the loop unexecutable by an agent without prior human negotiation. That's why they are mandatory in every [`loops/`](loops/README.md) file.

### The iteration cycle — from dispatch to handoff

The practical question is how agents, skills, tools, MCPs, sensors and gates fit together during a single turn. The sequence below is the same in any loop; What changes is who executes it and against which gate.

```text
Orchestrator dispatches mission full identity, minimal context, budget
  │
  ├─▶ Agent reads the AGENTS.md versioned context, applicable rules, ADRs, memory
  │
  ├─▶ inventory skills and apply the corresponding skills/<skill>/SKILL.md
  │
  ├─▶ invokes tools and MCPs in the authorized scope .agent/settings.json, .agent/mcps.json
  │
  ├─▶ local sensors evaluate .hooks/ ◀── internal loop: correct and repeat
  │
  ├─▶ independent critic challenges adversarial agent ◀── average turn
  │
  ├─▶ CI gate decides fast lane, deep lane by objective criteria
  │
  ├─▶ evidence.sh packages the evidence docs/evidence/<work-item>/
  │
  ├─▶ output envelope returns to orchestrator status, confidence, skills_used
  │
  └─▶ handoff crosses the artifact boundary in the canonical source ◀── external loop
```

Each link accounts for a class of failure, and removing any one of them doesn't make the loop faster — it moves the failure to a more expensive loop.

| Link | Prevents | If removed, the fault appears |
|---|---|---|
| Versioned context | the agent invents a plausible convention | in criticism, such as pattern divergence |
| Skill | the procedure is reinvented with each execution | in the handoff, as an unstable result |
| Scope of tools and MCPs | external effects occur before verification | in production, as an incident |
| Sensors | cheap mistake travel to CI | a full lap later, at the CI gate |
| Independent review | whoever produced it declares their work ready | at approval or at the customer |
| Gate | "ready" be an impression | after the merge, how to rework |
| Evidence | approval is based on agent summary | in the audit, when no one can redo it |
| Envelope | the orchestrator rereads the entire performance | as loss of context between steps |

### Consolidation and criticism

Two structural principles run through all loops.

**Each loop has exactly one agent that consolidates.** Parallel contributions converge into a single artifact under nominal responsibility. A contribution does not become a decision because it is consolidated: divergences and residual risks remain explicit in the final artifact, they are not resolved by omission.

**Criticism always comes from an instance independent of whoever produced it.** It is not a formality of process — it is the only defense against the structural incentive that an agent has to approve their own work. An adversarial agent produces traceable findings with evidence, severity and suggested action; it does not rewrite the criticized artifact.

### Handoff — what crosses the border

A handoff carries five things, always separated from each other: verifiable **facts**, referenced **evidence**, unconfirmed **hypotheses**, known **risks** and open questions. The separation exists because the fusion of these categories is how a hypothesis becomes a requirement without anyone having decided on it.

A handoff references versioned artifacts instead of copying context. And a handoff is only complete when the final artifact has arrived at the **canonical source** of the domain — `.coordination/` and `memory.md` are transit, never destination.

### Where the loop lives and where execution happens

`docs/loops/` is the **canonical and versioned catalog**. It receives no execution artifacts — no `PB`, `PRD`, plan, evidence, or handoff from a concrete round is recorded here.

Each owner runs the loop within their own workspace:

```text
<workspace-do-owner>/
├── docs/loops/ # local bindings: enabled version, permissions, adaptations
├── projects/<project>/ # persistent artifacts from a run
├── .coordination/ # handoffs and temporary blocks
├── memory.md # resumable context, never canonical source
└── repos/ # only in technical workspace, when applicable
```

Before starting a mission, the agent resolves `owner workspace → projects/<project> → Work Item → canonical sources`.

Local binding declares the canonical loop version and can **restrict** tools, permissions, and integrations. It cannot expand autonomy or change gates without the decision foreseen in the operational model. This asymmetry is intentional: local adaptation must be able to tighten, never loosen.

### Dry-run mode

A loop can be executed without generating persistent artifacts. Activate with `mode: dry-run` at the start of the mission or prefix the command with `--dry-run`.

The agent performs reasoning, analysis, and drafting as normal, and can print what it *would* have generated. Does not create or modify files in `projects/`, `engineering/`, or `execution/`, and does not update `BOARD.md`, `STATUS.md`, Work Items, or handoffs. It serves to explore an unknown loop, test an approach before committing it, or validate the agent's behavior without side effects.

---

## Loops available

The 12 loops are documented individually in **[`loops/`](loops/README.md)** — one file per step, with operational contract, sequence, handoffs, explicit limits, typical failures and destination of the artifacts.

Each loop has a codename. It's not decoration: a short name is what allows you to say "this is Red Team Loop's problem" without ambiguity in a conversation. Four of them — Ralph, Red Team, Canary and Dream — come from terms already established in engineering and agent practice; the rest follow the same record.

| # | Loop | Codename | Consolidate | Collaborate or challenge |
|---:|---|---|---|---|
| 0 | [Intake and screening](loops/00-intake-and-triage.md) | 🚦 **Triage Loop** | Intake Agent | Meeting Context; Product Manager |
| 1 | [Discovery and research](loops/01-discovery-and-research.md) | 🔦 **Scout Loop** | Product Manager Agent | UX Specification; Tech Lead Discovery; Adversarial PM |
| 2 | [Product and UX](loops/02-product-and-ux-planning.md) | 🎨 **Studio Loop** | Product Manager + UX Specification | Adversarial PM; research, content and prototyping |
| 3 | [Technical specification](loops/03-technical-specification.md) | 🗺️ **Drafting Loop** | Specification Tech Lead | Adversarial TL; Security/Data/Platform |
| 4 | [Standalone implementation](loops/04-autonomous-implementation.md) | 🔁 **Ralph Loop** | Orchestrator Agent | Software Engineer Agents |
| 5 | [Adversarial validation](loops/05-adversarial-validation.md) | ⚔️ **Red Team Loop** | QA / Validation Agent | Security Review; Architecture Review; Adversarial Code Reviewer |
| 6 | [PR and merge](loops/06-pr-and-merge.md) | 🚪 **Gatekeeper Loop** | PR Agent | Reviewer Agents; Code Owners |
| 7 | [Approval](loops/07-release-candidate-validation.md) | 🎭 **Rehearsal Loop** | Product Validation Agent | ReleaseAgent |
| 8 | [Production and observation](loops/08-production-release-and-observation.md) | 🐤 **Canary Loop** | ReleaseAgent | ObservabilityAgent |
| 9 | [Knowledge curation](loops/09-knowledge-curation.md) | 🗄️ **Archivist Loop** | Knowledge Agent | Critical Agent |
| 10 | [Telemetry and continuous improvement](loops/10-continuous-improvement.md) | 🌙 **Dream Loop** | Auto Dream Agent | Telemetry; Observability; Critic |
| 11 | [Daily Operation](loops/11-daily-operations.md) | ☀️ **Daily Loop** | Auto Dream Agent | Telemetry; Knowledge; Orchestrator; Intake |

---

## Versioning and evaluation

Each loop records contract version and date, agents and gates involved, human responsible, and changelog with rollback plan. Changing the sequence of a loop without changing its version breaks the local bindings that declare compatibility.

Metrics per loop cover: pass on the first pass of the output gate, number of turns per circuit (inner, average, outer), rework generated in the next loop, scaling rate and its cause, cycle time and cost per round, and confirmed versus false positive findings on the average turn.

**These metrics measure loop design, not agent performance.** A frequent outer loop indicates a poorly positioned gate or poorly defined input — it almost never indicates a bad agent. Using them as an individual assessment corrupts the signal they produce.

---

## Checklist for adding a new loop

- [ ] Does the step require a new loop or does it fit as a variation of an existing one?
- [ ] Are the six items of the common contract explicit?
- [ ] Is there exactly one consolidating agent appointed?
- [ ] Does the criticism come from an instance independent of who produces it?
- [ ] Is each check in the innermost loop in which it can be performed?
- [ ] Is the output gate verifiable without human judgment — and, when not, is the owner named?
- [ ] Do handoffs separate fact, evidence, hypothesis, risk and question?
- [ ] Is the canonical fate of each artifact declared?
- [ ] Does the gate failure path point to a specific loop?
- [ ] Does the loop work in `dry-run` without side effects?

---

*Previous: [Agents](AGENTES.md) · Detail: [individual loop contracts](loops/README.md) · Next: [Methodology](METODOLOGIA.md) — how humans operate it all.*
