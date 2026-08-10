# 1. Application Repository Harness

---

## Overview

The **repo harness** converts the tacit knowledge of the repository into versioned files that the agent reads on its own and into checks that run without asking for a license. It lives inside the code repository, travels with the clone, and exists to answer four questions before the agent needs to act:

1. What is this repository?
2. How are things done here?
3. What do I need to prove before I can say I'm done?
4. What can I not touch without authorization?

The harness is organized into five cumulative layers. Order matters: Each layer eliminates a specific class of failure, and building out of sequence produces expensive failures.

| Layer | Reply | Materializes in |
|---|---|---|
| **Context** | what this repository is and what rules apply | `AGENTS.md`, `docs/rules/` |
| **Procedure** | how to perform a recurring task the right way | `skills/`, scripts |
| **Verification** | what needs to be true before moving forward | sensors, CI, merge policies |
| **Permission** | what this agent can do and what it requires people | `.agent/`, environments |
| **Evidence** | how to prove later that it was correct | evidence pack, logs, artifacts |

It's also worth understanding what a harness **isn't**. It is not the CI treadmill — the treadmill is just one possible implementation of the verification layer. It is not the architectural documentation itself — it points to it. And it's not about how the work is organized outside of the code: that's the responsibility of the workspace of whoever coordinates the agents.

---

## Index

- [Tools](TOOLS.md) — authoritative tools, LSP, codebase navigation, context management
- [MCPs](MCPS.md) — Model Context Protocol servers, scopes and authorization
- [Skills](SKILLS.md) — catalog of verifiable procedures from the repository
- [Rules](RULES.md) — desired state, entry contract (`AGENTS.md`) and escalation conditions
- [Sensors](SENSORS.md) — local versioned checks (pre-commit, pre-push)
- [Gates](GATES.md) — verification architecture from commit to deploy and autonomy levels
- [Documentation](DOCUMENTATION.md) — ADRs, evidence pack and complete file structure

---

*Next: [Agents](AGENTES.md) — how an agent works and the catalog of 23 roles.*
