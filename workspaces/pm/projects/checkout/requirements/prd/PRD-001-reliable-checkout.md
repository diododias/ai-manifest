---
id: PRD-001
project: checkout
status: approved
owner: product-manager
source: PB-001
updated_at: 2026-08-08
---

# Checkout confiável

## Resultado

O cliente pode repetir uma tentativa após timeout sem nova cobrança para a mesma operação.

## Requisitos

- Repetições equivalentes retornam o resultado original.
- Uma tentativa conflitante não altera o pagamento original.
- A experiência comunica processamento, sucesso, falha e recuperação.

## Fora de escopo

Troca de provedor e redesenho integral do checkout.

## Aceite

PM valida o comportamento de produto; UX valida experiência e acessibilidade; Tech Lead valida integridade técnica e risco operacional.
