---
title: Workspace de exemplo de UX
status: example
owner: ux
updated_at: 2026-08-08
---

# Workspace de UX

Este exemplo organiza evidências de usuário, jornadas, fluxos, especificações, protótipos, acessibilidade e validação. O projeto `checkout` é fictício e se conecta aos exemplos de PM e Tech Lead.

## Navegação

1. Carregue [`README.md`](README.md) e [`AGENTS.md`](AGENTS.md).
2. Consulte [`BOARD.md`](BOARD.md).
3. Entre em [`projects/checkout/README.md`](projects/checkout/README.md).
4. Use os padrões em [`docs/standards/`](docs/standards/README.md), o playbook e os templates.

## Estrutura

```text
ux/
├── README.md
├── AGENTS.md
├── WORKSPACE.md
├── BOARD.md
├── docs/          # padrões, playbooks e templates
├── projects/      # pesquisa e experiência por projeto
├── coordination/  # recrutamento, handoffs e decisões temporárias
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
