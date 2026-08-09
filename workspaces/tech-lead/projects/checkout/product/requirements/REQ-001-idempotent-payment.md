---
id: REQ-001
project: checkout
status: approved
source: PRD-001
updated_at: 2026-08-08
---

# Pagamento idempotente

> Derivação técnica do snapshot de produto. Confirme o comportamento esperado no [PRD canônico do PM](../../../../../pm/projects/checkout/requirements/prd/PRD-001-reliable-checkout.md) antes de alterar a implementação.

Dada uma chave de idempotência válida, repetições semanticamente equivalentes devem retornar o resultado persistido da primeira tentativa e não criar nova cobrança.

Reutilizar a chave com conteúdo conflitante deve produzir erro de conflito e não alterar o resultado original.
