# Context — Checkout

After a timeout, the customer does not know whether the payment was completed nor whether a new attempt is safe. UX must make processing, output and recovery understandable without promising behavior that the system does not guarantee.

## Outcome received

Enable safe replay and reduce uncertainty about double billing.

## Known restrictions

- provider confirmation can be asynchronous;
- content cannot expose internal details or sensitive data;
- states need to work with keyboard and assistive technology.
