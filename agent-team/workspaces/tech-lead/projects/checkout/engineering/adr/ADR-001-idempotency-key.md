---
id: ADR-001
project: checkout
status: accepted
owner: tech-lead
updated_at: 2026-08-08
---

# Persistir o resultado por chave de idempotência

## Contexto

Timeouts e redelivery podem repetir uma solicitação depois de o provedor já ter processado a cobrança.

## Decisão

Persistir chave, impressão digital da requisição e resultado. A chave é única; repetição equivalente devolve o resultado salvo e conteúdo conflitante é rejeitado.

## Consequências

A solução impede duplicidade dentro da janela de retenção, mas exige política de expiração, índice único e tratamento explícito de concorrência.
