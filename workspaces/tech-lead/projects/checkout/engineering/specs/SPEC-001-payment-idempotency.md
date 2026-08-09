---
id: SPEC-001
project: checkout
status: approved
owner: agent-architecture
requirement: REQ-001
updated_at: 2026-08-08
---

# Payment idempotence

## Contract

- Input requires non-empty `Idempotency-Key`.
- The first attempt reserves the key before charging.
- Completed equivalent attempt returns persisted status and body.
- Conflicting attempt returns `409`.
- Concurrent attempts cannot call the provider more than once.

## Validation

Unit tests cover equivalence and conflict; integration testing covers competition with real storage; evidence is linked to `WI-031`.
