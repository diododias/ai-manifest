---
id: SPEC-001
project: checkout
status: approved
owner: agent-architecture
requirement: REQ-001
updated_at: 2026-08-08
---

# Idempotência de pagamento

## Contrato

- A entrada exige `Idempotency-Key` não vazia.
- A primeira tentativa reserva a chave antes da cobrança.
- Tentativa equivalente concluída retorna o status e corpo persistidos.
- Tentativa conflitante retorna `409`.
- Tentativas concorrentes não podem chamar o provedor mais de uma vez.

## Validação

Testes unitários cobrem equivalência e conflito; teste de integração cobre concorrência com armazenamento real; evidências ficam ligadas ao `WI-031`.
