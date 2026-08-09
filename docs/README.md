---
title: Agent Team — índice da documentação
status: canonical
updated_at: 2026-08-09
---

# Documentação do Agent Team

> Mapa de navegação da documentação, organizado por perfil de leitor e por profundidade.

## Em 2 minutos

A documentação do Agent Team tem quatro corpos que respondem a perguntas diferentes. Os **documentos de modelo operacional**, na raiz de `docs/`, explicam como o sistema pensa: papéis, direitos de decisão, gates e autonomia. **`workflows/`** explica como cada etapa da jornada é executada por um time de agentes. **`agents/`** define quem são esses agentes, com contrato e permissões. **`diagrams/`** mostra como o trabalho se organiza em disco.

Cada documento carrega duas camadas: um bloco "Em 2 minutos" no topo, para avaliação rápida, e o desenvolvimento completo abaixo. Você nunca precisa ler um documento inteiro para decidir se ele é relevante. Se preferir navegar tudo em uma única página, com busca e diagramas renderizados, abra [`site.html`](site.html) no navegador.

| Corpo | Responde | Estado predominante |
|---|---|---|
| [modelo operacional](operating-model.md) | Como o sistema funciona e quem decide o quê | `canonical` |
| [`workflows/`](workflows/README.md) | Como cada etapa é executada por agentes | `proposed` |
| [`agents/`](agents/catalog.md) | Quem são os agentes e quais contratos seguem | `proposed` |
| [`skills/`](../skills/README.md) | Quais procedimentos os agentes executam | `canonical` |
| [`diagrams/`](diagrams/tech-lead-workspace.md) | Como o trabalho se organiza em disco | `proposed` |

---

## Trilhas de leitura

### Trilha rápida — 15 minutos

Para quem já conhece workflows de desenvolvimento e quer avaliar o projeto antes de investir tempo. Leia apenas o bloco "Em 2 minutos" de cada documento.

| Ordem | Documento | O que você leva |
|---:|---|---|
| 1 | [README do repositório](../README.md) | a proposta e as três ideias centrais |
| 2 | [Fluxo da jornada](end-to-end-journey.md) | o ciclo completo em diagrama |
| 3 | [Workflows multiagente](workflows/README.md) | como uma etapa vira trabalho de agentes |
| 4 | [Catálogo de agentes](agents/catalog.md) | quais papéis existem e o que cada um entrega |

### Trilha completa — leitura de referência

Para quem vai operar, adaptar ou estender o framework.

| Ordem | Documento | Papel | Estado |
|---:|---|---|---|
| 1 | [Sistema operacional do trio humano](operating-model.md) | visão canônica do modelo | `canonical` |
| 2 | [Fluxo da jornada](end-to-end-journey.md) | visão de ponta a ponta | `reference` |
| 3 | [Jornada por fases](journey-by-phase.md) | diagramas segmentados por fase | `reference` |
| 4 | [Modelo operacional 90/10](operating-model-90-10.md) | gates, risco e autonomia progressiva | `proposed` |
| 5 | [Workflows multiagente](workflows/README.md) | colaboração, handoffs e convergência | `proposed` |
| 6 | [Catálogo de agentes](agents/catalog.md) | papéis, contratos e permissões | `proposed` |
| 7 | [Pacotes importáveis dos agentes](agents/README.md) | identidade, alma e contrato executável | `proposed` |
| 8 | [Catálogo de skills](../skills/README.md) | procedimentos executáveis por etapa | `canonical` |
| 9 | [Workspace do Tech Lead](diagrams/tech-lead-workspace.md) | organização do trabalho multiagente | `proposed` |

### Trilha de contribuição

| Documento | Quando usar |
|---|---|
| [Padrão de documentação](documentation-standard.md) | antes de escrever ou reescrever qualquer documento |
| [Anatomia de uma skill](../skills/README.md#3-anatomia-de-uma-skill) | antes de criar ou revisar uma skill |
| [Contrato de artefatos](../skills/references/workflow-contract.md) | ao definir onde uma skill lê e escreve artefatos |
| [Registro de workspaces](agents/registry.yaml) | inventário dos agentes materializados para importação |

---

## Fonte de verdade

O [sistema operacional do trio humano](operating-model.md) é a referência conceitual principal. Todos os demais documentos detalham partes específicas dele e devem permanecer compatíveis. Quando um conceito muda, a alteração entra primeiro nesse documento e só depois é propagada para os especializados.
