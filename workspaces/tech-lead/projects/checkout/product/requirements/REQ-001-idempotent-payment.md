---
id: REQ-001
project: checkout
status: approved
source: PRD-001
updated_at: 2026-08-08
---

# Idempotent payment

> Technical derivation of the product snapshot. Confirm expected behavior in [PM canonical PRD](../../../../../pm/projects/checkout/requirements/prd/PRD-001-reliable-checkout.md) before changing the implementation.

Given a valid idempotence key, semantically equivalent retries should return the persisted result of the first attempt and not create a new charge.

Reusing the key with conflicting content should produce a conflict error and not change the original result.
