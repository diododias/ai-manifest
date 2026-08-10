# Payment retry flow

```mermaid
TD flowchart
    A["Confirm payment"] --> B["Processing"]
    B -->|"Confirmed"| C["Success"]
    B -->|"Known fault"| D["Error with safe action"]
    B -->|"Timeout"| E["See result"]
    E -->|"Done"| C
    E -->|"Not started"| F["Try again with the same operation"]
    E -->|"Undetermined"| G["Wait and check again"]
```

Indeterminate states should not suggest a new operation with a different identity.
