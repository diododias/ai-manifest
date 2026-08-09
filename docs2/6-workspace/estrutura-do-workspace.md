---
title: A estrutura de um workspace
status: canonical
updated_at: 2026-08-09
---

# A estrutura de um workspace

> Os arquivos que todo workspace mantém, como `projects/` organiza cada iniciativa e por que material bruto e trânsito temporário ficam separados da fonte canônica.

## Um workspace por papel

O trabalho do trio não mora em um único lugar compartilhado — cada papel tem sua própria raiz. Essa separação existe para que as responsabilidades não se misturem: o PM registra valor e requisitos, o UX registra evidência e experiência, o Tech Lead registra arquitetura e execução. Três raízes independentes evoluem sem pisar uma na outra.

```text
workspaces/
├── pm/           # valor, prioridade, requisitos e resultados de produto
├── ux/           # pesquisa, experiência, acessibilidade e validação
└── tech-lead/    # viabilidade, arquitetura, implementação e risco
```

## Os quatro arquivos que todo workspace mantém

Independentemente do papel, todo workspace mantém quatro peças. Conhecê-las é o suficiente para se orientar em qualquer um dos três.

| Peça | Responde | Natureza |
|---|---|---|
| `AGENTS.md` | como operar neste workspace | contrato de operação |
| `BOARD.md` | quais Work Items estão em andamento | estado do trabalho |
| `memory.md` | onde retomo o contexto | auxiliar, nunca fonte canônica |
| `projects/<project>/` | os artefatos reais de cada iniciativa | fonte canônica |

Quando um agente inicia uma missão, ele lê o `AGENTS.md` do workspace, identifica as skills aplicáveis e segue a estrutura de `projects/` — em vez de inventar convenções próprias. É por isso que as três skills de base ([Skills de base](../3-skills/skills-de-base.md)) existem: elas ensinam o agente a navegar essa estrutura com segurança.

## Onde os artefatos de uma execução vivem

Os artefatos persistentes de uma execução nunca ficam soltos nem no catálogo global — eles vivem em `projects/<project>/`, no workspace dono do domínio. O PM registra ali discovery, PRD, decisões e Work Items; o UX registra research, jornadas, fluxos, especificações e validações; o Tech Lead registra planos em `plans/active/`, specs, ADRs, evidências, reviews e worktrees.

Um detalhe importante: `projects/` de um workflow **não** fica em `docs/workflows/`. A pasta `docs/workflows/` do workspace é apenas a camada de binding local — quais workflows estão habilitados, em qual versão, com quais permissões. O trabalho real fica em `projects/`.

## Material bruto e trânsito: separados de propósito

Duas categorias de conteúdo ficam deliberadamente fora da fonte canônica, e entender por quê evita confusão.

O **material bruto** que sustenta as análises — transcrições, prints, e-mails, PDFs, documentos — fica em `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`. Cada execução usa sua própria pasta de sessão. Isso resolve um problema real: reexecutar um workflow porque o resultado não ficou bom **nunca** sobrescreve nem mistura o material da tentativa anterior. O asset permanece como rastro auditável, e a conclusão vai para o artefato do domínio correto.

O **trânsito temporário** — handoffs e bloqueios em `.coordination/` — é só passagem. Como você viu em [Onde a execução acontece](../5-workflows/onde-a-execucao-acontece.md), um handoff só se conclui quando o artefato final chega à fonte canônica. `.coordination/` guarda o que está a caminho, não o que está pronto.

## Continue por aqui

Você sabe onde as coisas ficam dentro de um workspace. Falta entender como os três workspaces se relacionam — quem é dono de qual verdade. Vá para [Ownership entre workspaces](ownership-entre-workspaces.md).
