# API

## `POST /payments`

Cabeçalho obrigatório: `Idempotency-Key`.

Respostas relevantes: sucesso original ou repetido, `400` para chave ausente e `409` quando a mesma chave representa outra solicitação. O contrato publicável deve ser mantido no repositório da API e referenciado aqui.
