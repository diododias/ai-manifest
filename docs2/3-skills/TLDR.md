---
title: Skills — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Skills · TLDR

> A pista rápida da seção. Você vai entender o que é uma skill, por que ela é obrigatória, os três tipos que existem e como uma skill é escrita por dentro. Os detalhes ficam nas páginas ao final.

## O problema que a skill resolve

Um agente sem skill improvisa. Ele inventa o nome do artefato, escolhe sozinho onde gravar e decide na hora o que conta como evidência. O resultado é um repositório em que cada execução seguiu uma convenção diferente — e ninguém consegue mais confiar em nada sem reler tudo. Esse é o problema que a skill resolve.

Uma **skill** é o oposto da improvisação: um procedimento nomeado, com entrada, saída e critério de conclusão, que produz o mesmo formato de artefato toda vez que roda. Ela transforma "faça um review" em "faça este review, com estes passos, produzindo este artefato, que termina quando estes critérios forem satisfeitos".

## A regra e os três tipos

A regra de operação é curta e sem exceção: **verificar as skills disponíveis antes de agir e usar todas as que se aplicam**. Uma skill aderente à missão não pode ser ignorada, e o agente sempre cita quais usou — ou por que nenhuma se aplicava.

As skills se dividem em três naturezas, e saber distingui-las é metade do aprendizado.

| Natureza | O que fazem | Quando se aplicam | Você aprende em |
|---|---|---|---|
| **De base** | governam a operação do workspace | toda missão, sempre | [Skills de base](skills-de-base.md) |
| **De domínio** | produzem o artefato de uma etapa | na etapa correspondente | [Skills por etapa](skills-por-etapa.md) |
| **De publicação** | tocam Git e GitHub | só com autorização explícita | [Skills por etapa](skills-por-etapa.md) |

## Skills não ampliam permissão

Um mal-entendido comum vale corrigir desde já: **uma skill não concede poder**. Uma skill de implementação não autoriza publicar; nenhuma delas decide sozinha o que vira baseline aprovado. Executar com liberdade dentro do escopo, mas publicar apenas sob autorização — essa assimetria é o que sustenta os níveis de autonomia do modelo.

## Continue por aqui

Comece por [Skills de base](skills-de-base.md), que valem para qualquer missão. Depois veja [Skills por etapa](skills-por-etapa.md) para saber qual procedimento roda em cada fase, e feche com [Anatomia de uma skill](anatomia-de-uma-skill.md) se for criar ou revisar uma.
