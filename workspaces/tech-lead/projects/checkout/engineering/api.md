#API

## `POST /payments`

Mandatory header: `Idempotency-Key`.

Relevant answers: original or repeated success, `400` for missing key, and `409` when the same key represents another request. The publishable contract must be maintained in the API repository and referenced here.
