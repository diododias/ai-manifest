# 5. Methodology

---

## Overview — How Humans Operate It

The previous four sections describe **the system**: what the repository needs to carry to be operable by agents, who the agents are and under what authority they act, what procedures they perform, and in what order they collaborate at each step of the journey. None of them answer the question a person asks on a Monday morning: **and me, what do I do?**

This is the gap that the methodology fills. It does not introduce any new concepts, does not expand anyone's autonomy and does not redefine any contract. It is the **glue**: it shows how the already documented layers behave when someone actually operates them — what triggers what, when a person is called, what they need to see to respond, and what happens if they don't respond.

The displacement that justifies the section is known. When agents take over code production, writing is no longer expensive; What gets expensive is deciding what to build, proving it was built right, and preventing decisions, code, and documentation from becoming separated. A team that does not deal with this displacement generates volume without confidence. The model's answer is an inversion: **the human core operates the system rather than performing the work.**

### Where is everything

The entire documentation reading rule fits in a table. Confusing these layers is what produces documentation that no one can execute — and is what this section avoids by linking rather than rewriting.

| Layer | Reply | Where do you live |
|---|---|---|
| **Harness** | what the repository needs to load to support all of this | [`REPO_HARNESS.md`](REPO_HARNESS.md) and neighbors |
| **Skill** | *how* a recurring task is performed correctly | [`SKILLS.md`](SKILLS.md) |
| **Agent** | *who* executes, under what authority and with what limits | [`AGENTES.md`](AGENTES.md), [`agentes/`](agentes/README.md) |
| **Loop** | *in what order*, what crosses the border and when to stop | [`LOOPS.md`](LOOPS.md), [`loops/`](loops/README.md) |
| **Methodology** | *who operates*, what triggers what and what demands people | this section |

A practical consequence: When a document in this section describes the internal sequence of a step, it is wrong by construction. Sequence is the subject of [`loops/`](loops/README.md). Here the trigger, the human decision point and the responsibility are documented — never the mechanics.

### The five commitments

Everything in this section derives from five commitments. They resolve the most common disputes in advance in a flow with agents, and each page forward is the operational deployment of one or more of them.

| Commitment | What does it prevent |
|---|---|
| **Whoever proposes does not approve** | that the incentive to declare one's work ready turns into approval |
| **Approval requires evidence, and silence never approves** | an item advances due to fatigue, deadline or lack of response |
| **Material change invalidates previous approval** | that a decision made about one artifact covers another |
| **Autonomy increases by metric, not by confidence** | that the perception that "it's working well" replaces the evidence that it is |
| **Artifact only exists in the canonical source** | that a decision lives in a temporary handoff and is lost in the next round |

### What does a person do, after all

The short answer, before the details: one person **decides**, **unlocks** and **fixes the system**. Does not track execution, does not review entire diff, does not narrate status.

| Activity | Frequency | Where is it documented |
|---|---|---|
| Respond to a decision checkpoint | per delivery, 3 to 6 times | [Human checkpoints](metodologia/02-checkpoints-humanos.md) |
| Read the daily briefing and unlock | daily, few minutes | [Rhythms and cadences](metodologia/04-ritmos-e-cadencias.md) |
| Respond to an escalation | by exception | [Operator Manual](metodologia/05-manual-do-operador.md) |
| Order improvements to the system itself | weekly | [Rhythms and cadences](metodologia/04-ritmos-e-cadencias.md) |
| Adjust gate, risk or autonomy | by Marco | [Human checkpoints](metodologia/02-checkpoints-humanos.md) |

---

## Section index

| Page | Reply |
|---|---|
| [Papers](metodologia/01-papeis.md) | who owns which decision, and how a tie is resolved |
| [Human checkpoints](metodologia/02-checkpoints-humanos.md) | where a person enters, with what question and for how long |
| [Triggers and shots](metodologia/03-gatilhos-e-disparos.md) | what triggers what, when, and what never fires alone |
| [Rhythms and cadences](metodologia/04-ritmos-e-cadencias.md) | what happens every day, every week and every milestone |
| [Operator Manual](metodologia/05-manual-do-operador.md) | how to operate in practice: dispatch, read output, intervene |
| [Commented journey](metodologia/06-jornada-comentada.md) | the entire cycle seen by human points |
| [Documentation workflows](metodologia/07-workflows-de-documentacao.md) | how documentation stays alive on its own |

The complete index, with reading tracks per profile, is in [`metodologia/README.md`](metodologia/README.md).

---

*Previous: [Loops](LOOPS.md) · Detail: [the seven pages of the methodology](metodologia/README.md) · Next: [Workspace](WORKSPACE.md) — where this work lives outside the code.*
