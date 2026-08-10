# Transcript — idempotence architecture review (fictitious)

Participants: Tech Lead, Specification Tech Lead Agent.

**Tech Lead:** the main risk is race between payment attempts with the same payload.

**Specification Tech Lead Agent:** I propose single idempotence key per attempt, with payload fingerprint comparison to detect divergent replay.

**Tech Lead:** aceito. Register as ADR-001 and cover with competition test.

Complete decisions and trade-offs are in `engineering/adr/ADR-001-idempotency-key.md`.
