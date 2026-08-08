---
title: Workspace de exemplo do Tech Lead
status: example
owner: tech-lead
updated_at: 2026-08-08
---

# Workspace do Tech Lead

Este diretório materializa a arquitetura descrita em [`docs/architecture/tech-lead-workspace.md`](../../docs/architecture/tech-lead-workspace.md). O projeto `checkout`, a organização `acme` e seus estados são dados fictícios usados para mostrar o fluxo completo.

## Comece por aqui

1. Carregue o contexto para IAs em [`README.md`](README.md).
2. Leia as regras obrigatórias em [`AGENTS.md`](AGENTS.md).
3. Consulte o portfólio em [`docs/portfolio/PROJECTS.md`](docs/portfolio/PROJECTS.md) e o resumo em [`BOARD.md`](BOARD.md).
4. Entre no projeto por [`projects/checkout/CONTEXT.md`](projects/checkout/CONTEXT.md) e [`projects/checkout/STATUS.md`](projects/checkout/STATUS.md).
5. Localize o código em [`projects/checkout/engineering/repositories.yaml`](projects/checkout/engineering/repositories.yaml).
6. Assuma um arquivo em [`projects/checkout/work-items/`](projects/checkout/work-items/README.md).

## Onde cada informação pertence

| Informação | Fonte de verdade |
|---|---|
| Portfólio e prioridade | `docs/portfolio/PROJECTS.md` e `BOARD.md` |
| Contexto e estado do projeto | `projects/<projeto>/CONTEXT.md` e `STATUS.md` |
| Requisitos de produto | `../pm/projects/<projeto>/requirements/`; `product/` contém apenas snapshots de entrada |
| Experiência | `../ux/projects/<projeto>/`; `ux/` local contém apenas ponteiros de integração |
| Decisões e especificações técnicas | `projects/<projeto>/engineering/` |
| Estratégia de execução | `projects/<projeto>/plans/` |
| Estado do trabalho | `projects/<projeto>/work-items/` |
| Evidência de conclusão | `projects/<projeto>/execution/evidence/` |
| Clones e worktrees | `repos/` |
| Coordenação temporária | `coordination/` |
| Contexto retomável, não autoritativo | `memory/` |

## Estrutura

```text
tech-lead/
├── README.md
├── AGENTS.md
├── WORKSPACE.md
├── BOARD.md
├── docs/          # padrões, playbooks, templates e portfólio
├── projects/      # fonte de verdade de cada projeto
├── repos/         # registro e checkouts locais ignorados pelo Git
├── coordination/  # comunicação transversal temporária
├── memory/        # memória operacional do workspace
└── archive/       # material global desativado
```

## Copiando o exemplo

Substitua os dados fictícios, mantenha uma pasta por projeto e não versione clones, segredos ou estado volátil. Diretórios que ainda não possuem artefatos são representados por `README.md`; eles podem ser removidos quando o primeiro artefato real for criado.
