---
id: ADR-001
project: checkout
status: accepted
owner: tech-lead
updated_at: 2026-08-08
---

# Persist the result by idempotence key

## Context

Timeouts and redelivery may repeat a request after the provider has already processed the charge.

## Decision

Persist key, request fingerprint and result. The key is unique; equivalent repetition returns the saved result and conflicting content is rejected.

## Consequences

The solution prevents duplication within the retention window, but requires an expiration policy, single index, and explicit concurrency handling.
