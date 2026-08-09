---
title: Agentes — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Agentes · TLDR

> A pista rápida da seção. Você vai entender o que é um agente no Agent Team, o contrato comum que todos seguem, como se agrupam por função e quem trabalha junto em cada fase. Os detalhes ficam nas páginas ao final.

## Nome em diagrama não é papel

Um nome de agente em um diagrama de workflow não significa nada até que ele saiba qual resultado deve produzir, de quem recebe ordem e quando deve parar. "Security Review Agent" é só um rótulo até você definir o que ele lê, o que entrega, qual gate precisa satisfazer e em que condição escala para um humano.

O catálogo de agentes existe para transformar rótulos em **papéis operacionais inequívocos** — de modo que uma missão possa ser despachada sem negociação prévia sobre responsabilidade, escopo ou critério de conclusão.

## Um contrato comum e seis grupos

Todo agente responde às mesmas oito perguntas — qual resultado produz, quem é seu sponsor humano, quais fontes são canônicas, o que aceita de entrada, o que entrega, quais tools pode usar, quais gates satisfaz e quando escala. Esse é o [contrato comum](contrato-comum.md).

Os 23 papéis se organizam em seis grupos, por função na jornada.

| Grupo | Exemplos | Sponsor típico |
|---|---|---|
| Entrada e coordenação | Intake, Meeting Context, Orchestrator | PM / owner da fase |
| Produto, UX e discovery | Product Manager, UX Specification, Adversarial PM | PM e UX |
| Especificação técnica | Specification TL, Adversarial TL, Security/Data/Platform | Tech Lead |
| Construção e validação | Software Engineer, QA, Security Review, Code Reviewer | Tech Lead |
| Integração e operação | PR, Product Validation, Release, Observability | Tech Lead, PM e UX |
| Conhecimento e melhoria | Knowledge, Telemetry, Auto Dream, Critic | owner do domínio e trio |

O [catálogo por grupo](catalogo-por-grupo.md) detalha cada papel, e a [composição por fase](composicao-por-fase.md) mostra quem trabalha junto.

## Papéis lógicos, com uma restrição inegociável

O catálogo descreve **papéis lógicos**, não instâncias. Uma execução pode usar uma instância por papel, várias instâncias paralelas do mesmo papel, ou uma instância assumindo mais de um papel compatível. A restrição que nunca se quebra: **papéis de produção e de aprovação não se combinam na mesma instância** quando houver risco de autoavaliação. Quem produz não aprova.

## Continue por aqui

Comece por [Contrato comum](contrato-comum.md), a base que vale para todos. Depois explore o [Catálogo por grupo](catalogo-por-grupo.md) e feche com a [Composição por fase](composicao-por-fase.md).
