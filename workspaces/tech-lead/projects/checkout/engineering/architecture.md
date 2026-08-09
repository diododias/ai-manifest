# Current state of the architecture

`checkout-api` exposes payment creation, persists its state, and calls an external provider. Idempotence will be enforced at the application boundary and guaranteed by a unique constraint on storage.

```mermaid
flowchart LR
    C["Cliente"] --> A["Checkout API"]
    A --> D[("Banco")]
    A --> P["Provedor de pagamento"]
```

The diagram records the topology, not the operational state of local checkouts.
