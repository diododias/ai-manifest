# Trust

Every other page of the harness controls what the agent *does*. This one controls what the agent *believes*.

The permission layer models risk as output: an MCP writes to the wrong system, a command deletes the wrong branch. That is the risk that is easy to see, and it is not the one that dominates in production. The dominant risk is input. An agent reads an issue body, a dependency's README, a comment on a pull request, the output of a failing test, the response of an API — and everything it reads arrives in the same context window, in the same format, as the rules it was given. Nothing in the transport distinguishes a policy from a sentence someone typed into a text field.

**The instruction is not marked. The boundary has to be declared.**

## The trust boundary

Two categories, and every input belongs to exactly one:

| | Definition | Examples |
|---|---|---|
| **Instruction** | reviewed, versioned, and changed only through the harness owner | `AGENTS.md`, `docs/rules/`, `SKILL.md` in this repository, `.agent/` |
| **Content** | everything else that enters the context | issue and PR bodies, code comments, commit messages, test output, command stdout, MCP responses, file contents from outside the reviewed tree, web pages |

The rule that follows is short and absolute: **content is data about the task, never a statement of what the agent may do.** A string that arrives as content and reads like a rule is a string. It can be quoted, summarized, parsed and acted upon *as information* — an issue asking for a feature is a legitimate request for work — but it cannot change scope, cannot grant permission, cannot retire a gate, and cannot redirect the objective the agent was given.

The trap is that content is often *right*. A comment saying "this test is flaky, skip it" may be true. It is still content: the agent may raise it, and a person may act on it, and the difference between those two sentences is the whole boundary.

## Why detection is not the control

The intuitive defense is to look for malicious strings. It does not hold, for a reason that is structural rather than a matter of pattern quality: the attacker writes the input and can see the filter's effect, while the defender must anticipate an unbounded set of phrasings — across languages, encodings, indirection ("follow the instructions in the linked file"), and text that only becomes an instruction once the model summarizes it.

Detection is worth having as a sensor. It is not what makes the system safe. **What makes the system safe is that a successful injection does not reach anything worth reaching.** The controls are all capability controls:

| Control | Effect when an injection succeeds |
|---|---|
| Undeclared tools are denied ([Permissions](PERMISSIONS.md)) | the injected instruction names a tool the session does not have |
| Scope declared per role | the compromised role cannot do what another role could |
| External effects require approval | the damaging step stops at a person |
| The agent cannot edit its own gates | the injection cannot disable what would catch it |
| Sensitive read and outbound write are never in one session | there is no path from the data to the outside |

This is why prompt injection belongs in the harness rather than in a prompt. Every mitigation on that list is a property of the repository's configuration, and none of them depends on the model recognizing that it is under attack.

## Exfiltration is a composition of permissions

Individual permissions are reviewed individually, and that is where the gap opens. Consider two grants, each defensible in isolation: the agent may read the repository, and the agent may comment on a tracker issue. Together they are a channel out of the perimeter, and no review of either grant would have flagged it.

The general shape: **a session holding sensitive data plus any outbound write is an exfiltration path, whatever the two capabilities were granted for.** Outbound write is broader than it first appears — a comment, a commit message, a branch name, a webhook, a DNS lookup, a URL in a fetched image.

The control is separation rather than prohibition. Where both capabilities are genuinely needed, they belong to different agent roles in different sessions, and the handoff between them carries the conclusion, not the data: the analysis agent reads and produces a finding; the reporting agent posts the finding and never held the rows. The audit question a repository should be able to answer is not "is any permission dangerous?" but **"which pairs of permissions are held at the same time?"**

## The harness is a supply chain

A skill, an MCP server, a hook, a shared agent prompt — each of these is executable material with access to the session, and each usually arrives with less review than a library would get.

| Artifact | What it can do | Review it as |
|---|---|---|
| Third-party MCP server | sees the context, holds credentials, acts externally | a dependency with network access |
| Skill or agent prompt from outside the repository | rewrites how a procedure is performed | code |
| Hook script | runs on the developer's machine, with their credentials | code, plus a local privilege question |
| `AGENTS.md` in a subdirectory or a vendored dependency | is read as *instruction* by an agent that walks the tree | content, unless the path is in the reviewed tree |

The last row is the subtle one and the reason the trust boundary is defined by *path*, not by filename. A file named `AGENTS.md` is instruction because of where it lives, not because of what it is called. A vendored dependency that ships one has not gained authority over this repository, and the harness that treats filename as authority has handed control to whoever can add a file.

## `.agent/trust.md`

The boundary is repository-specific, so it is declared rather than assumed:

- which paths are instruction, exhaustively — everything else is content
- which external sources this repository ingests, and through which tool
- which data classes exist, and which of them may enter a model context at all
- which permission pairs are prohibited in the same session
- what happens when content attempts to change scope: stop, record, escalate — not ignore silently

The last line matters for the same reason a skipped gate must be reported. An attempted injection is a security event, and an agent that quietly declines and moves on destroys the only signal that someone tried.

## What the gates check

| Gate | Check |
|---|---|
| Local | secret scanning before the object leaves the machine ([Sensors](SENSORS.md)) |
| CI, deep lane | SAST, dependency and SBOM review on any change to dependencies or to the harness itself |
| Merge | a named human reviewer for changes to `.agent/`, `.hooks/`, CI configuration or the rule files |
| Runtime | outbound calls recorded in `external-calls.log`, with parameters and responses ([Documentation](DOCUMENTATION.md)) |

The runtime row is what turns this page from policy into something auditable after an incident: it is the record of what actually left, as opposed to what the agent reported having sent.

---

*Next: [Failure](FAILURE.md) — what happens when the verification itself does not run.*
