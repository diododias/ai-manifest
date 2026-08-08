---
title: Workspace de exemplo do Product Manager
status: example
owner: product-manager
updated_at: 2026-08-08
---

# Workspace do PM

Este exemplo organiza portfólio, discovery, estratégia, requisitos, roadmap, decisões e validação de produto. O projeto `checkout` é fictício e se conecta aos exemplos de UX e Tech Lead.

## Navegação

1. Carregue [`README.md`](README.md) e [`AGENTS.md`](AGENTS.md).
2. Consulte [`docs/portfolio/PORTFOLIO.md`](docs/portfolio/PORTFOLIO.md) e [`BOARD.md`](BOARD.md).
3. Entre em [`projects/checkout/README.md`](projects/checkout/README.md).
4. Use os templates em [`docs/templates/`](docs/templates/README.md) e o fluxo em [`docs/playbooks/product-cycle.md`](docs/playbooks/product-cycle.md).

## Estrutura

```text
pm/
├── README.md
├── AGENTS.md
├── WORKSPACE.md
├── BOARD.md
├── docs/          # portfólio, padrões, playbooks e templates
├── projects/      # fonte de verdade de produto por projeto
├── coordination/  # entradas, decisões pendentes e handoffs temporários
├── memory/        # contexto retomável, não autoritativo
└── archive/       # material global desativado
```

## Envelope padrão

```yaml
mission_id: "<id>"
agent_role: "<papel>"
status: completed | partial | blocked
confidence: high | medium | low
sources_used: []
outputs_created: []
decisions_requested: []
assumptions: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```
