# Versioning

The harness is the control code of the repository. It is the only part of the tree whose modification changes the meaning of work that was already finished: when a rule changes, every approval granted under the previous text was granted under a contract that no longer exists.

Ordinary code does not behave this way. A refactor does not retroactively unapprove last week's pull request. A rule change does, and a harness that is edited like documentation — improved in place, no version, no record — cannot answer the first question an audit asks: **under which rules was this accepted?**

## `HARNESS_VERSION` and the changelog

Two files, both in `.agent/`:

`HARNESS_VERSION` holds a single semantic version. `CHANGELOG.md` records, for each version, what changed, why, and — the field that distinguishes this from a normal changelog — **what it invalidates**.

The version numbers carry harness-specific meaning:

| Bump | Means | Consequence for work in flight |
|---|---|---|
| **Major** | something previously allowed is now forbidden, or a new gate blocks | open work items revalidate against the new rules before merge |
| **Minor** | a new rule, gate or skill that does not contradict the previous ones | new work adopts it; work in flight is unaffected |
| **Patch** | wording, examples, pointers, clarification with no change in meaning | nothing |

The distinction between minor and patch is the one that gets abused. If a reasonable agent could have behaved differently before and after the edit, it is not a patch — clarifying an ambiguous rule *changes* it, because the ambiguity was doing work.

## What a change invalidates

`attestation.json` records the SHA of every rule file the agent actually read ([Documentation](DOCUMENTATION.md#identity-and-provenance)). That field is the join key: given a changed rule, it identifies exactly which open work items were produced under the old text, without depending on anyone's memory of when the change landed.

| What changed | Invalidates |
|---|---|
| A rule file | evidence for open items whose attestation records the old SHA of that file |
| A gate, or a gate's configuration | evidence produced by the lane that gate belongs to |
| A sensor | nothing already in CI; the next local run picks it up |
| The permission model | any in-flight operation relying on a scope that narrowed |
| A skill | nothing retroactively — a skill is a procedure, not a criterion |
| The agent prompt or the model in use | nothing formally, but it is recorded, because it is the first thing an incident review asks about |

The middle rows show why this is worth the machinery: the blast radius of a harness change is almost never "everything", and a team without a way to compute it either revalidates everything — which is expensive enough that people stop changing the harness — or revalidates nothing, which is the status quo this page exists to replace.

## Changing the harness

A harness change follows the rule from [Gates](GATES.md#non-negotiable-rules-for-gates-with-agents): it is made by the harness owner, outside the flow that the change affects, and never by an agent inside the flow the gate evaluates.

The changelog entry states five things:

- **What** changed, as a diff reference
- **Why** — the failure that motivated it, ideally a specific incident or escape
- **What it invalidates**, using the table above
- **The transition** — how work in flight is handled
- **Who** approved it

The transition field is the one that determines whether the change survives contact with a working team. A new rule applied retroactively to everything in flight blocks every open item at once and gets reverted the same afternoon. The two workable shapes are *grandfathering* — the rule applies to work started after the version — and a *scheduled sweep*, where existing violations are recorded as known debt with an owner and a deadline. A rule with no transition plan is a rule that will be applied inconsistently, and inconsistent enforcement is worse than no rule, because it removes the agent's ability to predict what the gate will do.

## Two versions, not one

There is a version of *the method* — this manifesto, its layers and their contracts — and a version of *the harness of a given repository*, which is that repository's local instantiation. They move independently: a repository can sit three method versions behind and be perfectly consistent internally, and adopting a new method version is a deliberate migration rather than a fact that becomes true when someone reads a document.

`HARNESS_VERSION` therefore records both: the local harness version, and the method version it implements. The second is what makes a fleet of repositories comparable — it answers which repositories have adopted a new control and which have not, which is otherwise a question that can only be answered by reading each one.

---

*Next: [Metrics](METRICS.md) — how to tell whether any of this is working.*
