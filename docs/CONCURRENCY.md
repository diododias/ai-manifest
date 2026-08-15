# Concurrency

Most of a harness can be designed as if one agent worked on one Work Item at a time. That assumption survives the first pilot and fails in production, because the reason to operate agents at all is that several of them run at once.

Concurrency does not introduce new gates. It attacks the meaning of the ones that exist: **a gate verifies a change against a base, and with several agents in flight, the base is no longer the thing that gets merged.**

## Evidence has a shelf life

An evidence pack is a claim about a specific state of the world: this change, on this base commit, satisfied these checks. The claim is true when produced. It stays attached to the change while the base moves underneath it.

Git resolves the textual part of this and nothing else. Two changes can merge cleanly, pass every check individually, and be wrong together — one adds a call site to a function whose contract the other narrowed, one adds a row to a table the other just started reading, one relaxes a validation the other now depends on. **No conflict marker appears, because nothing conflicts textually.** The agent did not err; the verification simply answered a question about a base that no longer exists.

Freshness is therefore a property the merge gate has to check, not a courtesy:

| Since the evidence was produced | Verdict |
|---|---|
| the base did not move | evidence is current |
| the base moved, no overlap with what the change touched or read | current, merge proceeds |
| a file the change touched also changed | stale — re-run the affected lane |
| a shared contract, schema or public interface changed | stale — re-run the affected lane, whether or not the diffs overlap |
| a rule, gate or dependency changed | stale — re-run the full lane ([Versioning](VERSIONING.md)) |
| the freshness window expired | stale, regardless of what changed |

The window exists because "no overlap" is computed from what the tooling can see, and the set of things a change actually depends on is always larger than the set of files it edits. A window measured in hours — short enough that the world has not moved, long enough that a normal review does not expire — bounds how wrong the overlap analysis is allowed to be.

The rule that follows: **the last gate before integration re-validates against the state being integrated into, not against the state the work started from.** A merge queue that builds each change against the queue head is the standard implementation, and it is the reason merge queues exist for human teams too — agents only raise the frequency at which the problem occurs.

## Claiming work

Two agents that pick up the same Work Item produce two solutions, both valid, and neither of them wrong in a way a gate can detect. The waste is invisible until review, where a person discovers that the second implementation exists.

A claim is a lease, not a lock: it names the agent, the Work Item, the region of the code it expects to touch, and an expiry. The expiry is what distinguishes a lease from a deadlock — an agent that dies mid-task must not hold a region forever, and no human should have to clear it by hand.

| Element | Why |
|---|---|
| The Work Item | prevents duplicate work on the same objective |
| The declared region | surfaces the collision before the work, not at merge |
| The expiry | a crashed agent releases automatically |
| The base commit | the input for the freshness check above |

The declared region is necessarily approximate — an agent does not know everything it will touch before it starts. It is still worth declaring, because the failure it prevents is the expensive one: two agents refactoring the same module in incompatible directions for an hour each.

## Ordering what cannot be parallel

Some sequences are serial regardless of how many agents are available. Making the constraint explicit is cheaper than discovering it during a merge:

- **A migration and the code that depends on it.** The expand-migrate-contract order is a sequence, and each step is a separate integration.
- **A contract change and its consumers.** The producer merges the compatible version first; the consumer follows; the removal is a third change.
- **Anything touching the harness itself.** A rule, gate or permission change serializes against everything in flight, because it invalidates their evidence.

The third case is the one that surprises. A harness change is not a normal change with a different reviewer — it is a change that retroactively alters what every open Work Item has proven. This is why it goes through the harness owner outside the normal flow, and why it is versioned.

## What the trio owes the system

Three things stay human decisions no matter how many agents are running, because each requires knowing the intent behind the work rather than its diff:

**How many agents may hold the same subsystem.** Parallelism has a ceiling per area of the code, below the ceiling set by the budget.

**Which conflicts are resolved and which are escalated.** A textual conflict can be resolved by whoever touched it last. A semantic divergence — two agents that implemented incompatible readings of the same requirement — is a specification defect, and merging either side hides it.

**Whether duplicated work is discarded or reconciled.** Discarding is usually right and never automatic.

None of these can be inferred from the repository, which is why they belong in the workspace layer and not here. What belongs here is the machinery that makes them visible in time to decide: leases, freshness and an ordered integration point.

---

*Next: [Budget](BUDGET.md) — the constraint that fails upward when nothing is broken.*
