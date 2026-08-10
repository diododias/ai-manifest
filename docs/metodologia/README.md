# Methodology pages

This directory contains the seven section pages. The general concept — why there is a layer of methodology above the harness and what the five commitments are — is in [Methodology — How Humans Operate It](../METODOLOGIA.md); Here are the operational details.

## The rule that governs all pages

No page in this section describes the mechanics of a step. Mission sequences, handoffs between agents and exit gates live in [`loops/`](../loops/README.md); authority and limit of each role live in [`agentes/`](../agentes/README.md); tools, sensors and CI live in [harness](../REPO_HARNESS.md). What is documented here is the **trigger**, the **human decision point** and **responsibility** — always with a link to the corresponding contract.

The practical test: If a paragraph in this section would remain correct if a loop changed its internal sequence, it is in the right place. If not, it is a duplicate and needs to become a link.

## How to read

| Page | Reply | Read if you… |
|---|---|---|
| [01 — Papers](01-papeis.md) | who owns which decision | will take on one of the three roles or don't know who to ask |
| [02 — Human checkpoints](02-checkpoints-humanos.md) | where a person enters and with what question | will answer an H, or draw the evidence pack |
| [03 — Triggers and shots](03-gatilhos-e-disparos.md) | what triggers what and when | want to understand how the system moves without someone pushing |
| [04 — Rhythms and cadences](04-ritmos-e-cadencias.md) | what happens every day and every week | will operate the routine, not a specific delivery |
| [05 — Operator's manual](05-manual-do-operador.md) | how to do it, in practice | is operating for the first time |
| [06 — Commented journey](06-jornada-comentada.md) | the entire cycle through human points | want the overall vision before the details |
| [07 — Documentation workflows](07-workflows-de-documentacao.md) | how documentation stays alive | will write, review or audit documentation |

## Trails by profile

**New operator — 20 minutes.** [Papers](01-papeis.md) → [Commented journey](06-jornada-comentada.md) → [Operator manual](05-manual-do-operador.md). In the end, you know who decides what, where it goes and what to do when something comes to you.

**Product Manager.** [Roles](01-papeis.md) → [Human checkpoints](02-checkpoints-humanos.md), with attention to H1, H2 and product acceptance → [Rhythms](04-ritmos-e-cadencias.md), for weekly screening and ordering of improvements.

**UX.** [Papers](01-papeis.md) → [Human checkpoints](02-checkpoints-humanos.md), with attention to H2 and acceptance of experience → [Commented journey](06-jornada-comentada.md), block 1.

**Tech Lead.** [Human checkpoints](02-checkpoints-humanos.md), with attention to H3, H4 and H5 → [Triggers and shots](03-gatilhos-e-disparos.md) → [Operator manual](05-manual-do-operador.md) → [Documentation workflows](07-workflows-de-documentacao.md). It is the role that also accounts for the harness, and therefore for the triggers it configures.

**Who will audit the model.** [Human checkpoints](02-checkpoints-humanos.md) → [Triggers and shots](03-gatilhos-e-disparos.md) → [Documentation workflows](07-workflows-de-documentacao.md). The three pages together answer whether any decision has an owner, evidence and trace.
