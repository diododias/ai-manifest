---
id: PRD-001
project: checkout
status: approved
owner: product-manager
updated_at: 2026-08-08
---

# Checkout confiável

> Snapshot não autoritativo de entrada técnica. Consulte o [PRD canônico no workspace de PM](../../../../../pm/projects/checkout/requirements/prd/PRD-001-reliable-checkout.md).

## Resultado

Clientes podem repetir uma tentativa após timeout sem risco de cobrança duplicada.

## Métrica de sucesso

Nenhuma cobrança duplicada para requisições com a mesma chave de idempotência durante a janela suportada.

## Fora de escopo

Troca de provedor de pagamentos e redesenho visual do checkout.
