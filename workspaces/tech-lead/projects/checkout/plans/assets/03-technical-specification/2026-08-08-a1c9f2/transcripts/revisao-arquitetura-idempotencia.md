# Transcrição — revisão de arquitetura de idempotência (fictícia)

Participantes: Tech Lead, Specification Tech Lead Agent.

**Tech Lead:** o risco principal é corrida entre tentativas de pagamento com o mesmo payload.

**Specification Tech Lead Agent:** proponho chave de idempotência única por tentativa, com comparação de impressão digital do payload para detectar replay divergente.

**Tech Lead:** aceito. Registrar como ADR-001 e cobrir com teste de concorrência.

Decisões e trade-offs completos estão em `engineering/adr/ADR-001-idempotency-key.md`.
