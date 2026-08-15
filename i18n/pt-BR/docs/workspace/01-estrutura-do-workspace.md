# 01 — Estrutura do workspace

> Os arquivos que todo workspace mantém, como `projects/` organiza cada iniciativa, e por que material bruto e trânsito temporário ficam separados da fonte canônica.

Um workspace desconhecido deveria ser navegável por qualquer agente sem que alguém precisasse explicar a convenção em voz alta. Esta página descreve o contrato mínimo que torna isso possível.

---

## Um workspace por papel

O trabalho do trio não mora em um único lugar compartilhado — cada papel tem sua própria raiz. Essa separação existe para que as responsabilidades não se misturem: o PM registra valor e requisitos, o UX registra evidência e experiência, o Tech Lead registra arquitetura e execução. Três raízes independentes evoluem sem pisar uma na outra, e cada uma corresponde ao domínio de decisão descrito em [Papéis](../metodologia/01-papeis.md).

```text
workspaces/
├── pm/           # valor, prioridade, requisitos e resultados de produto
├── ux/           # pesquisa, experiência, acessibilidade e validação
└── tech-lead/    # viabilidade, arquitetura, implementação e risco
```

## Os quatro arquivos que todo workspace mantém

Independentemente do papel, todo workspace mantém quatro peças. Conhecê-las é suficiente para se orientar em qualquer um dos três.

| Peça | Responde | Natureza |
|---|---|---|
| `AGENTS.md` | como operar neste workspace | contrato de operação |
| `BOARD.md` | quais Work Items estão em andamento | visão consolidada, nunca fonte de verdade |
| `memory.md` | onde retomo o contexto | auxiliar, nunca fonte canônica |
| `projects/<project>/` | os artefatos reais de cada iniciativa | fonte canônica |

Quando um agente inicia uma missão, ele lê o `AGENTS.md` do workspace, identifica as skills aplicáveis e segue a estrutura de `projects/` — em vez de inventar convenções próprias. É por isso que as skills de base descritas em [Skills](../SKILLS.md) são obrigatórias em toda missão de workspace: `workspace-memory`, `workspace-projects` e `workspace-board` ensinam o agente a navegar essa estrutura com segurança, e não apenas a descrevem.

## Onde os artefatos de uma execução vivem

Os artefatos persistentes de uma execução nunca ficam soltos nem espalhados por um catálogo global — eles vivem em `projects/<project>/`, no workspace dono do domínio. O PM registra ali discovery, PRD, decisões e Work Items; o UX registra research, jornadas, fluxos, especificações e validações; o Tech Lead registra planos em `plans/active/`, specs, ADRs, evidências, reviews e worktrees.

Um detalhe frequentemente confundido: `projects/` de um Work Item **não** fica na pasta local que referencia o catálogo de loops. Essa pasta — descrita em [Onde o loop vive e onde a execução acontece](../LOOPS.md#onde-o-loop-vive-e-onde-a-execução-acontece) — é apenas a camada de binding local: quais loops estão habilitados, em qual versão, com quais permissões. O trabalho real, o que de fato foi decidido e produzido, fica em `projects/`.

## Material bruto e trânsito: separados de propósito

Duas categorias de conteúdo ficam deliberadamente fora da fonte canônica, e entender por quê evita confusão recorrente.

O **material bruto** que sustenta as análises — transcrições, prints, e-mails, PDFs, documentos — fica em `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`. Cada execução usa sua própria pasta de sessão. Isso resolve um problema real e recorrente: reexecutar um loop porque o resultado não ficou bom **nunca** sobrescreve nem mistura o material da tentativa anterior. O asset permanece como rastro auditável, e a conclusão extraída dele vai para o artefato do domínio correto.

O **trânsito temporário** — handoffs e bloqueios em `.coordination/` — é só passagem. Como descrito em [Handoff — o que atravessa a fronteira](../LOOPS.md#handoff--o-que-atravessa-a-fronteira), um handoff só se conclui quando o artefato final chega à fonte canônica. `.coordination/` guarda o que está a caminho, não o que está pronto.

## Uma implementação de referência

Uma implementação navegável desta estrutura está em [`workspaces/`](../../workspaces/README.md), com uma raiz de exemplo para cada um dos três papéis. Os nomes, organizações, repositórios e estados que ali aparecem são fictícios — servem para demonstrar a estrutura, não o trabalho de produção de um time real. Ao adotar o modelo, esses valores devem ser substituídos pelos seus.

---

*Anterior: [Índice do workspace](README.md) · Próximo: [Ownership entre workspaces](02-ownership-entre-workspaces.md).*
