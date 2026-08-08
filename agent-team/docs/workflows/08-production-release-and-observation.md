---
title: Workflow — produção e observação
status: proposed
updated_at: 2026-08-08
---

# Workflow — produção e observação

Libera um release candidate com exposição controlada e usa sinais operacionais para avançar, pausar ou reverter. O Release Agent executa a política; o Observability Agent interpreta e evidencia a saúde.

| Aspecto | Contrato |
|---|---|
| Entrada | release candidate aprovado, rollout/rollback, SLOs, alertas e autorizações |
| Consolida | Release Agent |
| Colabora | Observability Agent |
| Saída | versão liberada, health report, changelog e rollback/pausa quando aplicável |
| Owner humano | Tech Lead; PM coaprova R3/R4 |
| Gate | ambiente autorizado, migração compatível e janela pós-deploy sem regressão relevante |

```mermaid
flowchart LR
    A[Release candidate] --> B{Política exige H5?}
    B -- sim --> C[H5: aprovar exposição]
    B -- não --> D[Release Agent\ncanary, flag ou rollout]
    C --> D
    D --> E[Observability Agent\nSLOs, erros e baseline]
    E --> F{Saúde do rollout}
    F -- saudável --> G[ampliar e concluir]
    F -- regressão --> H[pausar ou rollback]
    H --> I[Implementação ou incidente]
```

## Sequência

1. O Release Agent verifica artefato, ambiente, secrets autorizados, migração, backup e capacidade de rollback.
2. H5 é aplicado conforme o risco; R3/R4 requerem aprovação explícita antes de produção.
3. O Release Agent executa a estratégia autorizada. O Observability Agent compara erros, latência, SLOs e métricas de produto com o baseline.
4. Sinal de regressão dispara pausa ou rollback conforme política, com evidence pack para o Tech Lead; estabilidade completa a janela pós-deploy.

## Escalonamento

Escalar quando rollback automático não for seguro, os sinais forem contraditórios ou o impacto exceder o plano de mitigação. O agente não pode manter exposição crescente diante de alerta crítico não explicado.
