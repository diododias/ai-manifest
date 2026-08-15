# Agent-Team

**Agent-Team** is a manifesto: a set of documents that describe, in a complete and verifiable way, how a team of AI agents can collaborate in building software — from idea intake to production operation — with well-defined human decision points.

This repository does not contain an application to install or run. It contains **the specification of a working method**: roles, procedures, execution orders and governance rules, all versioned as text so that both people and agents can read and follow them without ambiguity.

If this is your first visit, think of this README as a guided introduction. It explains the central idea of ​​the project, how the content is organized and where to start reading — without requiring you to already know the vocabulary of the rest of the documentation.

---

## Interactive experience

Open [`index.html`](index.html) to explore the documentation in a dark interface, with global search, drilldown navigation, and an interactive six-layer pyramid. The file works locally, without a server.

HTML is generated from current Markdown — never edited as a parallel source:

```bash
uv run scripts/build-docs-site.py
```

---

## The central idea: a six-layer pyramid

The method is organized into six layers, from the most concrete to the most abstract. Each layer answers a different question and depends on whether the previous layer already exists — skipping one of them is, according to the manifesto itself, what produces documentation that no one can actually execute.

| # | Layer | Question that answers | Main document |
|---|---|---|---|
| 1 | **Harness** | What does the application repository need to load to be operated by agents? | [`docs/REPO_HARNESS.md`](docs/REPO_HARNESS.md) |
| 2 | **Skills** | *How* should a recurring task be performed correctly? | [`docs/SKILLS.md`](docs/SKILLS.md) |
| 3 | **Agents** | *Who* performs each task, under what authority and with what limits? | [`docs/AGENTES.md`](docs/AGENTES.md) |
| 4 | **Loops** | *In what order* do agents collaborate, and when to stop? | [`docs/LOOPS.md`](docs/LOOPS.md) |
| 5 | **Methodology** | *Who operates* the system on a day-to-day basis, and what does it require of a person? | [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) |
| 6 | **Workspace** | *Where* does each artifact of an execution live, outside of the code? | [`docs/WORKSPACE.md`](docs/WORKSPACE.md) |

A simple way to understand the relationship between the layers: **harness** is what makes a repository readable for an agent; **skills** are the recipes that keep a recurring procedure from being reinvented on each task; **agents** are those who do the work within this repository, following those recipes; **loops** define the order of a stage of the journey, from intake to deployment; the **methodology** explains what a person needs to decide along this path; and the **workspace** is the place, outside the code, where the decisions and artifacts of each execution are stored.

---

## Repository structure

```text
ai-manifest/
├── README.md # this file
├── docs/ # the method documentation — start here
│ ├── README.md # complete pyramid index, with reading tracks
│ ├── REPO_HARNESS.md # layer 1 — repository harness
│ ├── TOOLS.md # tools that an agent can invoke
│ ├── MCPS.md # MCP servers and authorized scopes
│ ├── SKILLS.md # layer 2 — procedure catalog
│ ├── RULES.md # desired state of repository and AGENTS.md
│ ├── SENSORS.md # local checks (pre-commit, pre-push)
│ ├── GATES.md # check commit to deploy, maturity levels
│ ├── DOCUMENTATION.md # ADRs and evidence pack
│ ├── AGENTS.md # layer 3 — how an agent works
│ ├── agents/ # the 23 individual agent contracts
│ ├── LOOPS.md # layer 4 — how the steps of the journey coordinate
│ ├── loops/ # the 12 stage contracts, from intake to daily operation
│ ├── METODOLOGIA.md # layer 5 — how a person operates the system
│ ├── methodology/ # the seven operational pages
│ ├── WORKSPACE.md # layer 6 — where the work lives outside the code
│ └── workspace/ # the four operational pages
├── agents/ # the executable prompts for each agent (AGENT.md)
├── skills/ # executable procedures (SKILL.md)
├── workflows/ # the executable version of the loops
├── templates/ # templates used by PM, UX and Tech Lead
├── workspaces/ # workspace examples for the three roles
├── i18n/ # translations: pt-BR mirror, UI strings and glossary
└── scripts/ # documentation support utilities
```

The documentation is published in English and Brazilian Portuguese from this same branch. The canonical text is the tree above; `i18n/pt-BR/` mirrors the same paths, and [`i18n/README.md`](i18n/README.md) is the contract for keeping both in sync.

The rule of thumb to guide yourself: **`docs/` explains the concept and why; the sister folders (`agents/`, `skills/`, `workflows/`, `templates/`, `workspaces/`) contain the executable version of what `docs/` describes.** Reading a concept document before the corresponding artifact avoids applying a procedure without understanding the reason behind it.

---

## Where to start

The complete documentation, with the detailed index for each layer and reading tracks per profile, is at **[`docs/README.md`](docs/README.md)**. The table below is a shortcut to the most common objectives.

| If you want… | Start with… |
|---|---|
| Understand the project idea together | [`docs/README.md`](docs/README.md) |
| Prepare an application repository to be operated by agents | [Harness](docs/REPO_HARNESS.md) → [Tools](docs/TOOLS.md) → [Skills](docs/SKILLS.md) → [Rules](docs/RULES.md) → [Sensors](docs/SENSORS.md) → [Gates](docs/GATES.md) |
| Get to know the agent catalog and what each one does | [`docs/AGENTES.md`](docs/AGENTES.md) → [individual contracts](docs/agentes/README.md) |
| See the complete journey, from intake to deployment | [`docs/LOOPS.md`](docs/LOOPS.md) → [the 12 steps](docs/loops/README.md) |
| Knowing what is up to a person to decide, in practice | [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) → [operator manual](docs/metodologia/05-manual-do-operador.md) |
| Know where each artifact of a run should be saved | [`docs/WORKSPACE.md`](docs/WORKSPACE.md) → [workspace structure](docs/workspace/01-estrutura-do-workspace.md) |

---

## Essential concepts, in simple language

These five concepts appear in almost all documents in the repository. It's worth fixing them before moving on to the complete material.

**Skill.** The verifiable procedure for a recurring task that requires judgment — for example, how to investigate a bug or how to write a technical specification. A skill is different from a script because it covers criteria, not just deterministic criteria.

**Agent.** A process with a delimited mission: receives an objective, reads the necessary context, acts within authorized tools, submits the result to objective verification and returns a standardized report. A nice name on a diagram is not an agent — it only becomes one when these five parts are defined.

**Loop.** The collaboration contract for a stage of the journey: who participates, in what order, what passes from one agent to the other and what needs to be true to move forward. The name "loop", rather than "workflow", is intentional — the work rotates (tries, is corrected, is challenged, converges) instead of moving in a straight line.

**Methodology.** The layer that explains what a person actually does: when they are called upon to decide, what they need to see to respond, and what happens if they don't respond. Five commitments support this layer — among them, the most structural: **whoever proposes does not approve**.

**Workspace.** The physical place, outside the application code, where a Work Item is opened, a decision becomes an artifact, and an agent returns to the context of a previous session. There is one workspace per role — PM, UX, and Tech Lead — each with its own canonical source of truth.

---

## Repository maturity and agent autonomy

One principle runs through the entire manifesto: **the autonomy granted to an agent is never greater than what the repository can automatically verify.** A repository without sufficient gates should not operate with high-autonomy agents, even if it appears to be working well — the appearance of success is no substitute for verification.

| Level | The repository has | Sustained autonomy |
|---|---|---|
| **HL0 — naked** | just README, occasional tests, build CI | none — assisted work |
| **HL1 — readable** | `AGENTS.md`, minimum rules, verification script, pre-commit | low (A0–A1) |
| **HL2 — verifiable** | CI by risk, branch protection, evidence pack | average (A2) |
| **HL3 — operable by team** | repository skills, identities per agent, environment and post-deploy gates | high (A3–A4) |

The full breakdown — what each level requires and why — is at [`docs/GATES.md`](docs/GATES.md).

---

## How this repository evolves

Each layer has its own change checklist, explicit versioning and evaluation criteria — never used as an individual performance ranking, only to improve the contract, context and tools for each role. Before proposing a relevant change to a layer, it is worth reading the corresponding document to the end: each one ends with the checklist and versioning rules that apply to changes in that specific layer.

For the complete map, with all documents and reading tracks per profile, see **[`docs/README.md`](docs/README.md)**.
