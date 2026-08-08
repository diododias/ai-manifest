# Contexto — Checkout

## Problema e objetivo

O checkout fictício da Acme recebe eventos de pagamento que podem ser reenviados. O projeto busca processá-los com consistência e sem cobranças duplicadas.

## Usuários e stakeholders

- clientes que concluem compras;
- operação financeira e atendimento;
- time de Payments, responsável pelo serviço.

## Escopo

Inclui a API de checkout e seu processamento de pagamentos. Catálogo, logística e o provedor externo de pagamentos ficam fora do escopo.

## Arquitetura atual

O serviço `acme/checkout-api` recebe um comando com uma chave de idempotência, persiste o resultado e integra com o provedor de pagamentos. A decisão detalhada está em [`engineering/adr/ADR-001-idempotency-key.md`](engineering/adr/ADR-001-idempotency-key.md).

## Restrições

- redelivery é esperado;
- a mesma chave não pode produzir duas cobranças;
- evidências não podem expor dados pessoais ou credenciais.
