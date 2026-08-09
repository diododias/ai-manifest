---
title: Workflows — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Workflows · TLDR

> A pista rápida da seção. Você vai entender o que um workflow define que o catálogo de agentes não define, o contrato comum que todo workflow segue e onde a execução realmente acontece. Os detalhes ficam nas páginas ao final.

## O que acontece *entre* os agentes

A seção [Agentes](../4-agentes/TLDR.md) define cada papel isoladamente. Mas um papel sozinho não entrega nada — o valor aparece na colaboração. Um **workflow** define exatamente o que acontece *entre* os agentes: a sequência de missões, os artefatos que atravessam as fronteiras, como contribuições independentes convergem em um único artefato e o ponto em que uma decisão deve ser escalada ao humano.

Se o catálogo é o elenco, o workflow é o roteiro.

## Um contrato comum e uma jornada de 11 etapas

Todo workflow explicita seis coisas, e a ausência de qualquer uma torna o workflow inexecutável por um agente sem negociação humana.

| Item do contrato | Define |
|---|---|
| Entrada | artefatos de entrada e critérios para iniciar |
| Missões | dependências e o que pode rodar em paralelo |
| Consolidação | o único agente responsável pela saída |
| Handoffs | fatos, evidências, hipóteses, riscos e perguntas em aberto |
| Saída | gate de saída e destino em caso de falha |
| Escalonamento | condição de parada e owner humano |

A jornada tem 11 etapas, do intake à melhoria contínua. Cada uma é um workflow, com um agente que consolida e outros que colaboram ou desafiam. O detalhe está em [A jornada completa](a-jornada-completa.md).

## Catálogo e execução são coisas diferentes

A distinção que resolve a maior parte das dúvidas na prática: o **catálogo de workflows** é canônico e versionado; a **execução** acontece no workspace do owner, em `projects/<project>/`. Nada de uma execução concreta — nenhum `PRD`, plano ou evidência — é gravado no catálogo. Entender essa separação é o que evita que a documentação e o trabalho real se misturem. O tema é aprofundado em [Onde a execução acontece](onde-a-execucao-acontece.md).

## Continue por aqui

Comece por [O contrato de workflow](contrato-de-workflow.md) para o formato comum. Depois veja [A jornada completa](a-jornada-completa.md) e feche com [Onde a execução acontece](onde-a-execucao-acontece.md).
