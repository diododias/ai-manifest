---
id: PRD-001
project: checkout
status: approved
owner: product-manager
source: PB-001
updated_at: 2026-08-08
---

# Reliable checkout

## Result

The client can repeat an attempt after a timeout without being charged again for the same operation.

## Requirements

- Equivalent repetitions return the original result.
- A conflicting attempt does not change the original payment.
- Experience communicates processing, success, failure and recovery.

## Out of scope

Change of provider and complete redesign of the checkout.

## Accept

PM validates product behavior; UX validates experience and accessibility; Tech Lead validates technical integrity and operational risk.
