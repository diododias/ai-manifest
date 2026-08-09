---
id: PRD-001
project: checkout
status: approved
owner: product-manager
updated_at: 2026-08-08
---

# Reliable checkout

> Non-authoritative snapshot of technical input. See [Canonical PRD in PM workspace](../../../../../pm/projects/checkout/requirements/prd/PRD-001-reliable-checkout.md).

## Result

Customers can repeat an attempt after a timeout without the risk of double billing.

## Success metrics

No duplicate charges for requests with the same idempotence key during the supported window.

## Out of scope

Switching payment providers and visual redesign of the checkout.
