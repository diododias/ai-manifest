# Permissions

The permission layer defines which tools the agent is authorized to invoke, with what limits, and what requires human authorization before proceeding. This definition is structural — it doesn't live in prompt statements, but in versioned files within the repository.

The reason it cannot live in the prompt is not that agents disobey. It is that the prompt and the agent are the same system: an instruction that says "do not force-push" is evaluated by the process it constrains, and a process under pressure to finish will find the reading of that instruction that lets it finish. Permission has to be enforced by something that is not the agent.

## `.agent/settings.json`

The `settings.json` file declares the operational limits of the agent in that repository: which tools are allowed, which are explicitly prohibited, which models can be used, and what the stopping conditions are. An agent that does not find this file should treat the repository as not authorized for unattended operation.

```json
{
  "tools": {
    "allowed": ["read_file", "write_file", "run_tests", "run_lint"],
    "ask": ["install_dependency", "write_migration"],
    "denied": ["delete_branch", "force_push", "modify_ci", "modify_hooks"]
  },
  "models": {
    "default": "claude-sonnet-5"
  },
  "budget": {
    "max_cost_per_work_item_usd": 2.00,
    "max_turns": 40
  },
  "escalation": {
    "max_retries_before_escalation": 2
  }
}
```

Three properties of this file carry most of its value.

**Undeclared is denied.** The `allowed` list is exhaustive, not illustrative. A tool that is not named is forbidden, in the same way that [an absent `mcps.json` means zero scope](MCPS.md). The alternative — deny-listing what is dangerous — requires having imagined every dangerous thing in advance, and the list is only ever complete in retrospect.

**There are three verdicts, not two.** `ask` is the one that makes the model usable: it covers the operations that are legitimate in most cases and expensive in the rest, where blocking outright would push the agent into a workaround and allowing outright would remove the only moment a person could object. An operation that is always fine belongs in `allowed`; one that is never fine belongs in `denied`; everything else is an `ask`, and a permission model with an empty `ask` list is usually one that has been tuned for silence rather than for control.

**The escalation block contains no confidence threshold.** Self-reported confidence is not calibrated and not comparable between models; a number like `0.85` in a configuration file produces the appearance of a control with none of the mechanism. Stopping conditions are facts about the work — attempts without progress, scope exceeded, owner missing — and they are listed in [Rules](RULES.md#escalation-conditions).

### Wildcards grant the worst member of their family

The most common way a permission model fails is not a missing rule. It is a pattern that looked narrow:

| Written as | Also grants |
|---|---|
| `git *` | `push --force`, `reset --hard`, `branch -D`, `clean -fd` |
| `npm run *` | every script in `package.json`, including ones added later by a dependency bump |
| `docker *` | mounting the host filesystem into a container |
| `curl *` | sending any file in the repository to any host |

Each of these was written to allow something ordinary and quietly authorizes something irreversible. Two rules follow. Enumerate subcommands rather than command families — `git status`, `git diff`, `git log`, not `git *`. And where a family genuinely has to be allowed, pair the allow with an explicit deny for its destructive members, so that adding a permission never silently widens the blast radius.

The same reasoning applies to path scope: `read_file` over the whole tree includes the `.env` that someone will add next quarter.

### Permissions are per role, not per repository

A repository does not have one agent. The reviewer, the implementer and the release agent need different scopes, and collapsing them into a single profile grants every agent the union of what any agent needs — which is how a review agent ends up able to push.

Scope is therefore declared per agent role, and the role is bound to the identity that role writes under ([Documentation](DOCUMENTATION.md#identity-and-provenance)). This is also what makes "whoever proposes does not approve" enforceable rather than aspirational: the approving role does not hold the permission to have written the change.

## `.agent/permissions.md`

The `permissions.md` file describes, in natural language, what requires human authorization in that specific repository. It complements `settings.json` with the judgment that no JSON can capture: when the situation is ambiguous enough to stop.

Typical categories covered by this file include paths that require ownership before making any changes, operations that alter persisted state (migrations, schemas, secrets), irreversible actions with a limited rollback window, and any changes that affect the verification gates themselves.

The redundancy between the two files is intentional and it is the same pattern used for MCPs: **JSON protects the technical scope; Markdown protects judgment in the borderline case.** JSON cannot express "this table is small enough to migrate in place, unless it is the accounts table". Markdown cannot stop a call.

## Changing a permission is changing a gate

Permissions are part of the verification architecture, so the rule from [Gates](GATES.md#non-negotiable-rules-for-gates-with-agents) applies without exception: an agent does not widen its own scope inside the flow that scope constrains. A permission change is a harness change — it goes through the harness owner, it is versioned, and it is recorded in the changelog with the reason ([Versioning](VERSIONING.md)).

The failure mode this prevents is the one that looks like progress: a blocked agent, two attempts from finishing, editing the file that blocks it. Every individual step is reasonable. The result is a repository whose permission model records what agents wanted rather than what the team decided.

---

*Next: [Tools](TOOLS.md) — the tooling index and where each check runs.*
