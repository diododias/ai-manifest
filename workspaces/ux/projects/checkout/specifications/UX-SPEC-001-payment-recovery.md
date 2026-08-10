---
id: UX-SPEC-001
project: checkout
status: draft
owner: ux-specification-agent
reviewer: ux
source: RESEARCH-001
updated_at: 2026-08-08
---

# Payment recovery

## States

- **Processing:** blocks accidental resending and announces progress.
- **Success:** confirms result and next step.
- **Recoverable Fault:** explains the safe action available.
- **Indeterminate result:** does not state failure; offers consultation and guidance.
- **Conflict:** informs that the attempt does not correspond to the original operation and advises a safe return.

## Content

Use understandable and validated terms; do not expose the technical key, stack trace or internal state of the provider.

## Accessibility

- state change announced without moving focus unexpectedly;
- full keyboard operation;
- progress and results do not depend only on color;
- messages semantically associated with payment and action.

## UX criteria

- [ ] User distinguishes processing, success and indeterminate state.
- [ ] Safe retry preserves context and avoids duplicate operation.
- [ ] Failures provide understandable next action.
- [ ] Flow meets keyboard, focus and ad requirements.
