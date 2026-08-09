---
title: Workspace — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Workspace · TLDR

> A pista rápida da seção. Você vai entender o que é um workspace, como ele se organiza por papel, como o ownership é dividido entre workspaces e o que é o harness que o torna operável por agentes. Os detalhes ficam nas páginas ao final.

## Onde o trabalho realmente acontece

Depois de entender modelo, skills, agentes e workflows, falta o lugar onde tudo isso roda. Esse lugar é o **workspace**. Ele não é material de referência — é o ponto de trabalho onde cada papel humano e seus agentes executam o fluxo de verdade.

Existe um workspace por papel: `pm/`, `ux/` e `tech-lead/`. Cada um tem uma raiz independente para que seus contratos, exemplos e fontes de verdade evoluam sem misturar responsabilidades.

## As três engrenagens do workspace

Três ideias organizam qualquer workspace, e cada uma tem uma página própria.

| Engrenagem | O que resolve | Você aprende em |
|---|---|---|
| **Estrutura** | onde cada artefato de uma execução vive | [Estrutura do workspace](estrutura-do-workspace.md) |
| **Ownership** | qual workspace é dono de qual verdade | [Ownership entre workspaces](ownership-entre-workspaces.md) |
| **Harness do workspace** | o que torna o espaço operável por agentes | [Harness do workspace](harness-do-workspace.md) |

Cada workspace mantém um `AGENTS.md` (como operar), um `BOARD.md` (Work Items em andamento), um `memory.md` (retomada de contexto) e uma pasta `projects/<project>/` (os artefatos reais de cada iniciativa).

## Dois harnesses que não se confundem

Uma distinção fecha esta seção e conecta com a próxima. O **harness do workspace** organiza o trabalho do agente *fora* do código — Work Items, memória, projetos, coordenação. O **repo harness** vive *dentro* de cada repositório de código e viaja com o clone. A regra que separa os dois: se a informação continua verdadeira quando outro time clona o repositório, ela é repo harness; se ela é sobre como o trabalho está organizado esta semana, é workspace.

## Continue por aqui

Comece por [Estrutura do workspace](estrutura-do-workspace.md). Depois entenda o [Ownership entre workspaces](ownership-entre-workspaces.md) e feche com o [Harness do workspace](harness-do-workspace.md), que prepara o terreno para a seção do [repo harness](../7-repo-harness/TLDR.md).
