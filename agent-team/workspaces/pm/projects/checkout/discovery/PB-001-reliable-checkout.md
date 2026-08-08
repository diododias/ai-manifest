---
id: PB-001
project: checkout
status: approved
owner: product-manager
updated_at: 2026-08-08
---

# Recuperação confiável do pagamento

## Problema

Após timeout, o cliente não sabe se pode tentar novamente sem ser cobrado duas vezes.

## Evidência do exemplo

Hipótese ilustrativa baseada em relatos de suporte; um workspace real deve vincular fontes e baseline antes da aprovação.

## Outcome

Permitir repetição segura e tornar o resultado compreensível para o cliente.

## Perguntas para os parceiros

- UX: quais estados e mensagens sustentam uma recuperação compreensível?
- Tech Lead: como garantir idempotência sob retry e concorrência?
