---
title: Introdução ao Agent Team
status: canonical
updated_at: 2026-08-09
---

# Introdução ao Agent Team

> Por que o modelo existe, qual filosofia ele adota e quais conceitos você vai reencontrar em todas as seções seguintes.

## O deslocamento do gargalo

Vale começar por uma observação simples sobre o que muda quando um time adota agentes de IA para escrever código. Antes, o gargalo natural era a produção: escrever, testar e revisar código consome tempo, e é aí que a maioria dos times investe processo. Quando os agentes assumem boa parte dessa produção, esse gargalo encolhe — e outro, que sempre esteve lá, fica visível.

Esse outro gargalo tem três faces. A primeira é **decidir o que construir**: com capacidade de produção quase ilimitada, priorizar bem passa a valer mais do que produzir rápido. A segunda é **provar que foi construído certo**: um agente entrega código plausível com facilidade, e distinguir "plausível" de "correto" exige verificação estruturada. A terceira é **manter decisões, código e documentação sincronizados**: quando muita coisa é gerada rápido, a documentação e as decisões se descolam da realidade em semanas.

O Agent Team é um modelo operacional desenhado para atacar esse segundo gargalo. Ele não tenta fazer os agentes escreverem melhor — assume que escrevem bem o suficiente — e concentra energia em governar a operação ao redor.

## A inversão central: operar, não executar

A decisão de design mais importante do modelo é tratar o desenvolvimento como um sistema **operado** por três pessoas, e não **executado** por elas.

Isso significa que a atenção humana fica reservada para o que só uma pessoa deveria fazer: definir intenção, julgar valor, avaliar risco e assumir responsabilidade. A execução repetitiva — pesquisar, redigir especificação, implementar, testar, criticar, documentar — vai para os agentes. Duas consequências decorrem disso de propósito. As pessoas deixam de gastar tempo com execução mecânica, e a própria execução se torna progressivamente mais autônoma a cada ciclo.

A divisão de trabalho que torna isso possível é clara e sem sobreposição:

| Ator | Dirige |
|---|---|
| **Product Manager** | valor, prioridade e resultado de negócio |
| **UX** | entendimento do usuário, experiência e qualidade de uso |
| **Tech Lead** | viabilidade, arquitetura, qualidade técnica e risco operacional |
| **Agentes** | pesquisa, proposta, implementação, crítica, validação e documentação |
| **Automações** | verificações determinísticas, bloqueios e rastreabilidade |

Repare que os agentes **não decidem** — eles preparam a decisão. Um agente primário conduz e consolida o artefato de cada fase; agentes adversariais atacam a proposta em busca de ambiguidade, risco e suposição frágil; e o owner humano resolve as divergências que sobram.

## O que passa entre as fases: artefatos, não conversas

Em um time tradicional, muito contexto viaja por conversa: alguém explica na reunião, outro anota, um terceiro deduz. Isso não escala quando parte dos participantes são agentes, e mesmo entre humanos gera perda silenciosa de informação.

No Agent Team, cada passagem entre fases é um **contrato**, não um bate-papo. A fase declara o que recebe (entrada), o que produz (saída), quem responde por ela (owner humano) e qual critério objetivo autoriza avançar (gate). O contexto que atravessa a fronteira vem empacotado em artefatos versionados — um `PRD.md`, uma especificação de UX, um `SPEC.md` — acompanhados de um evidence pack curto que sustenta a decisão sem obrigar ninguém a reler sessões inteiras.

Um vocabulário mínimo aparece o tempo todo, e vale fixá-lo desde já:

| Termo | Significado |
|---|---|
| **Gate** | critério objetivo que autoriza um item a avançar de fase |
| **Evidence pack** | pacote curto que sustenta uma decisão humana |
| **Handoff** | passagem de contexto entre agentes ou fases, sempre por artefato |
| **Classe de risco (R0–R4)** | o peso de uma mudança; define quanta verificação ela exige |
| **Nível de autonomia (A0–A4)** | quanto o sistema roda sem intervenção humana |

## As três regras que você verá em toda parte

Três princípios resolvem, antecipadamente, as disputas mais comuns de um fluxo com agentes. Cada seção desta wiki é, no fundo, uma aplicação deles.

O primeiro é a **separação entre produzir e aprovar**: quem faz uma mudança nunca é o único responsável por validá-la. O segundo é a **integridade da evidência**: aprovação exige síntese, alternativas, riscos e provas — e ausência de resposta jamais equivale a aprovação. O terceiro é a **autonomia condicionada**: o sistema só ganha permissão para rodar mais sozinho quando métricas e gates demonstram que é seguro, e nenhum indicador isolado autoriza essa subida.

## Para onde ir agora

Você já tem o mapa mental do modelo. Se quiser experimentá-lo na prática, o [Quick start](quick-start.md) mostra como montar um piloto de três pessoas e rodar um ciclo completo. Se preferir aprofundar a lógica de decisão antes, vá para o [Modelo operacional](../2-modelo-operacional/TLDR.md).
