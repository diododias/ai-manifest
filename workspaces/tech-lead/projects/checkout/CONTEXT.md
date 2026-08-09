# Context — Checkout

## Problem and objective

Acme's dummy checkout receives payment events that can be resent. The project seeks to process them consistently and without duplicate charges.

## Users and stakeholders

- customers who complete purchases;
- financial operation and service;
- Payments team, responsible for the service.

## Scope

Includes the checkout API and its payment processing. Catalog, logistics and the external payment provider are out of scope.

## Current architecture

The `acme/checkout-api` service receives a command with an idempotence key, persists the result and integrates with the payment provider. The detailed decision is in [`engineering/adr/ADR-001-idempotency-key.md`](engineering/adr/ADR-001-idempotency-key.md).

## Restrictions

- redelivery is expected;
- the same key cannot produce two charges;
- evidence cannot expose personal data or credentials.
