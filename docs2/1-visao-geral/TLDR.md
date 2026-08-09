---
title: Visão geral — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Visão geral · TLDR

> A pista rápida da seção. Em poucos minutos você entende o problema que o Agent Team resolve, a proposta central e por onde começar. Os detalhes ficam nas páginas ao final.

## Qual problema estamos resolvendo

Quando agentes de IA passam a produzir código, o gargalo de um time se desloca. Escrever deixa de ser caro. O que fica caro é **decidir o que construir, provar que foi construído certo e impedir que decisões, código e documentação se separem**. Um time pequeno que ignora esse deslocamento gera muito volume e pouca confiança.

O Agent Team existe para resolver exatamente esse segundo problema — não a geração de código, mas a operação em torno dela.

## A proposta em uma frase

A ideia central é uma inversão de papéis: **as pessoas operam o sistema em vez de executar o trabalho**. Um trio humano — Product Manager, UX e Tech Lead — define intenção, prioridade, risco e aprovação. Agentes especializados pesquisam, especificam, implementam, criticam, validam e documentam, sempre dentro de escopo autorizado. Entre uma fase e outra, o contexto não passa por conversa: passa por artefatos versionados com owner, gate e evidência.

| Peça | O que é | Você aprende em |
|---|---|---|
| **Trio humano** | PM, UX e Tech Lead, cada um dono de um domínio | [Modelo operacional](../2-modelo-operacional/TLDR.md) |
| **Skills** | procedimentos repetíveis que padronizam o trabalho | [Skills](../3-skills/TLDR.md) |
| **Agentes** | os papéis que executam pesquisa, código e crítica | [Agentes](../4-agentes/TLDR.md) |
| **Workflows** | como os agentes colaboram em cada etapa | [Workflows](../5-workflows/TLDR.md) |
| **Workspace** | onde o trio e os agentes pilotam o fluxo | [Workspace](../6-workspace/TLDR.md) |
| **Repo harness** | o que o repositório de código carrega para ser operável | [Repo harness](../7-repo-harness/TLDR.md) |

## As três regras que sustentam tudo

Todo o resto deriva de três regras. **Quem propõe não é quem aprova** — a crítica vem sempre de uma instância independente. **Aprovação exige evidência explícita** — silêncio nunca conta como aprovação. E **autonomia só cresce com prova** — gates e métricas precisam demonstrar que é seguro antes de o sistema rodar mais sozinho.

## Continue por aqui

Para entender a lógica antes de qualquer detalhe, leia a [Introdução](introducao.md). Quando quiser colocar a mão na massa e rodar um primeiro ciclo, siga o [Quick start](quick-start.md).
