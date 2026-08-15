# Maturity

Maturity here does not mean AI adoption. It is the demonstrated ability of a squad to turn a need into an observed outcome repeatedly, without losing control of quality, risk, cost or accountability.

The assessment unit is a **squad operating a product or value stream**. A repository is one subsystem of that operation; a model is one dependency. Neither can represent the maturity of the whole flow by itself.

## Three scales, three different decisions

This method uses three scales that interact but are not interchangeable:

- **M0–M5 describes the squad maturity profile.** It evaluates product, flow, engineering, knowledge, platform and human-AI governance. It identifies the operating constraint and the next capability to improve.
- **HL0–HL3 describes the repository harness.** It states what the repository can currently verify and therefore sets a technical ceiling for autonomy. The controls are defined in [Gates](GATES.md#progressive-autonomy-and-the-harness-ceiling).
- **A0–A4 describes autonomy in operation.** It records which transitions agents may execute without a person and which checkpoints remain mandatory for the current risk. The levels are defined in [Human checkpoints](metodologia/02-checkpoints-humanos.md#autonomy--how-many-checkpoints-there-are-today).

A high maturity profile does not authorize autonomy that the harness cannot verify. A squad may be M4 in product and flow while a repository at HL2 still limits technical autonomy to A2. The reverse also matters: HL3 verification does not justify delegating a pricing or privacy decision when product evidence or governance remains at M1.

The valid operating state is therefore contextual: maturity shows what the system can sustain broadly, the harness imposes the technical ceiling, and risk determines how much of that ceiling is used for a specific change.

## Rules of assessment

**Levels are cumulative within each dimension.** M3 evidence is invalid when an M1 or M2 capability it depends on no longer works.

**Observed behavior outranks declared process.** A policy, tool or document proves that a capability exists; it does not prove that representative work uses it or that it improves an outcome.

**The result is a profile, not an average.** `Product M3 · Flow M2 · Quality M3 · Knowledge M1 · Platform M2 · Governance M2` preserves the constraint. Averaging that profile into “M2.2” would hide that stale or undiscoverable context limits the whole system.

**Unknown is not zero and not green.** Missing telemetry produces an explicit confidence gap. It cannot support promotion, but it should not be converted into a fabricated score.

**Risk remains local to the decision.** Mature operation increases autonomy for bounded, reversible and observable work first. Irreversible, regulated or ambiguous decisions may retain human checkpoints at any maturity level.

Use a recent window that includes normal work and relevant exception paths. Low-frequency releases, migrations or incidents require a longer window than routine delivery; a convenient calendar interval is not evidence if it misses the behavior being assessed.

## The six dimensions

Each dimension receives its own level. The same squad can be advanced in one and constrained in another.

**Product and user value** measures whether work starts from an explicit problem and ends in an observed effect. Evidence connects the hypothesis, intended user, product outcome, harm guardrails and the decision taken after telemetry or feedback. Output volume, adoption without successful use and stakeholder opinion without observed behavior do not establish maturity.

**Flow and work design** measures whether a change can move through the system in small, visible and reversible batches. Evidence includes explicit states, controlled work in progress, blocked-time and aging signals, manageable batch size and known queues. The dimension is weak when AI accelerates production while work accumulates in review, integration or release.

**Engineering quality and reliability** measures whether the squad can change the system without transferring uncontrolled risk to users. Evidence includes deterministic local verification, clean-environment CI, independent gates, security controls, observability, SLOs, progressive exposure and exercised recovery. A green pipeline is insufficient when canaries cannot prove that its gates still reject known failures.

**Knowledge and data** measures whether people and agents retrieve current, authoritative and permitted context. Evidence covers canonical sources, decision history, ownership, provenance, freshness, data quality and trust boundaries. More indexed content is not maturity when sources conflict, sensitive data is exposed or stale context cannot be detected.

**Platform and automation** measures whether the supported path is reproducible, observable and cheaper than improvisation. Evidence includes self-service environments, stable interfaces, reusable workflows, permission boundaries, actionable failures and cost visibility. Automation that only works through specialist intervention or silently skips unavailable controls has not become a platform capability.

**Human-AI collaboration and governance** measures whether authority, review and escalation follow risk rather than convenience. Evidence includes an explicit AI stance, authorized tools and data, bounded roles, independent approval, traceable outputs, meaningful escalation and accountable owners. Fewer human interactions only indicate maturity when required decisions remain visible and escapes do not rise.

## The maturity ladder

The ladder below is applied separately to every dimension. A level describes how that capability is controlled, not a fixed inventory of tools.

Read a score as the intersection of a dimension and a control mechanism. `Knowledge M2` means authoritative context, provenance and freshness follow a shared path used by comparable work; it does not mean the squad is generically “at M2”. `Product M3` means product evidence closes a traceable loop from hypothesis to production outcome and back to a decision. The dimension defines **what** is being evaluated; the level defines **how reliably the system reproduces and governs it**.

### M0 — Opportunistic

Results depend on individual effort and implicit knowledge. AI use is personal, useful prompts and decisions are not recoverable, and success cannot be compared with a stable baseline. The main problem is not lack of automation; it is that the system cannot distinguish a repeatable capability from an isolated success.

Evidence for leaving M0 is basic observability of the chosen scope: a named owner, explicit outcome, versioned work, visible states and a baseline from consistent definitions. None of this grants autonomy; it makes later claims falsifiable.

### M1 — Assisted

Work is bounded and supervised. Context, acceptance criteria, ownership and sources of truth are explicit enough for an agent to assist, while people still verify every material decision and output. Common changes have a reproducible path and the squad records initial product, delivery and quality signals.

M1 is sustained when comparable work can be repeated by someone other than the person who established the path. Advancement requires showing where variation comes from — missing context, unstable execution, manual queues or weak checks — rather than hiding it inside individual expertise.

### M2 — Standardized

Recurring work follows shared contracts instead of personal prompting technique. Entry and exit criteria, risk classes, authorized tools, data boundaries and expected evidence are defined. Deterministic verification is automated; people concentrate on ambiguity, trade-offs and exceptions.

The proof of M2 is reduced variation, not compliance with a template. The standardized path must lower cycle time, toil or correction effort without increasing failed changes, escaped defects or policy exceptions. If the path is documented but routinely bypassed, the dimension remains at M1.

### M3 — Integrated

Product decisions, work execution, engineering verification, release and production observation form one traceable feedback loop. The squad can connect an observed outcome to the hypothesis, decision, change, evidence and operating conditions that produced it. Production learning returns to planning instead of ending in an isolated dashboard.

Agents may coordinate bounded work across tools because context, interfaces, permissions and output contracts are explicit. Human checkpoints exist where risk or ambiguity requires judgment, not wherever automation happens to stop. M3 requires several representative cycles with end-to-end traceability and independent controls that catch known failure modes.

### M4 — Governed autonomy

The system delegates reversible work within explicit policy. Specialized agents may operate concurrently, but authority remains bounded by role, risk class, data classification, environment and budget. Identity, provenance and evidence travel with every material change; progressive exposure and tested rollback limit the effect of a wrong decision.

People govern policies, outcomes, architecture and exceptions rather than supervising every step. M4 is demonstrated only when delegated authority reduces waiting or human effort over a sustained window while stability, security, value and accountability remain within guardrails. More unattended execution by itself proves nothing.

### M5 — Adaptive

The squad treats its operating system as an object of controlled improvement. Changes to models, prompts, context, routing, workflow and platform begin with a baseline and hypothesis, run inside guardrails and produce a keep, change or reverse decision. Routing may adapt to task, risk and cost because the evaluation contract is already stable.

Human attention moves toward direction, novel judgment and structural change; it does not disappear. M5 evidence is causal: better outcomes can be attributed to a controlled change in the system and remain better after the temporary effort of the experiment ends. Continuous change without attribution is drift, not adaptation.

## Evidence for promotion and regression

Promotion in a dimension requires three layers of evidence to agree:

- **Capability:** the practice, contract, platform path or control exists, is versioned and has an accountable owner.
- **Behavior:** representative work actually uses it, including failure, escalation and exception paths.
- **Outcome:** the intended value, speed, quality, cost or team effect improves while its guardrails remain healthy.

Capability without behavior is shelfware. Behavior without outcome is activity. Outcome without capability is an isolated result that the system cannot reliably reproduce.

Promotion applies to a named dimension, scope and evidence window; it is not a permanent certification. A material change in team, architecture, platform, policy or data invalidates the assumptions it touches. Repeated bypasses, stale context, missing telemetry, rising escapes or unexercised recovery justify regression until the capability is demonstrated again. A declared degraded mode also lowers the applicable harness ceiling while it lasts ([Failure](FAILURE.md#declaring-a-degraded-mode)).

## Reading a result

A usable assessment preserves enough context to drive a decision:

```text
Scope: checkout release flow
Window: 12 representative releases

Profile:
  Product M3 · Flow M2 · Quality M3
  Knowledge M1 · Platform M2 · Governance M2

Repository harness: HL2 → technical ceiling A2
Autonomy in operation: A1
Primary constraint: authoritative context is fragmented and freshness is unknown
```

This result does not say that the squad “is M2”. It says that integration and quality are ahead of the knowledge system, which prevents reliable reuse of context and makes broader delegation unsafe. Operating at A1 is valid because it stays below the HL2 ceiling; operating at A3 would be invalid even if the maturity profile were stronger.

The next intervention should target the lowest **risk-critical** constraint, not mechanically the lowest number. Its contract names an owner, intended effect, guardrail and review date. After the evidence window, the squad keeps, changes or reverses the intervention and reassesses only the dimensions it could have affected.

## Misuses that invalidate the model

- Treating purchased tools, enabled seats or model access as capability.
- Promoting a level because documents and pipelines exist, without observing their use and effect.
- Collapsing the profile into an average or using it to rank squads, people or agents.
- Assuming maturity can only increase or that every scope deserves the same autonomy.
- Using generated output, commits, pull requests or token volume as proxies for value.

---

*Next: [Metrics](METRICS.md) — the signals that govern promotion, regression and autonomy.*
