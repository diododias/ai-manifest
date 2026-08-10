---
name: workspace-board
description: Selects, assumes, and reconciles Work Items with the `BOARD.md` of a workspace. Use when choosing eligible work, changing the status of a mission, recording block, preparing review, or ending a delivery.
---

# Workspace board

## Authority Rules

- `BOARD.md` is a consolidated vision; the Work Item file is the authoritative source of state, owner, scope, dependencies, and evidence.
- Never move a card just to reflect expectations. First update or commit the Work Item; then reconcile the board and `STATUS.md` when the local contract requires it.
- Do not assume, change or close an item belonging to another agent without explicit division of responsibility.

## Flow

1. Read the board and select only the item eligible for the phase: dependencies resolved, human owner, scope, risk and completion criteria defined.
2. Open the Work Item and confirm input sources, repository, branch/base/worktree when there is code, and applicable gates.
3. Record the assumption in the Work Item before modifying artifacts. When blocking, document cause, impact, evidence, and next owner.
4. Before each transition, confirm the new state criteria. For `done`, require evidence of all criteria; for partial delivery, maintain the status that reflects the pending status.
5. Reconcile `BOARD.md` as index and update `STATUS.md` with the verifiable state. Produce handoff when responsibility changes.

## Expected result

In the output envelope, enter `work_item_id`, previous and current state, evidence of gates and next owner. Declare any divergence between board, Work Item and actual state as blocking or risk.
