---
title: Ownership entre workspaces
status: canonical
updated_at: 2026-08-09
---

# Ownership entre workspaces

> Qual workspace é a fonte canônica de cada tipo de verdade, o que os demais recebem e como um agente busca contexto de outro domínio sem duplicá-lo.

## Uma verdade, um dono

O princípio que governa a relação entre os três workspaces é simples e rígido: **uma informação autoritativa não deve ser mantida em dois lugares**. Cada tipo de verdade tem exatamente um workspace dono, e os demais recebem apenas o que precisam — uma decisão aprovada, um handoff, um snapshot.

A razão é evitar o pior problema de documentação distribuída: duas versões da mesma verdade que divergem com o tempo, sem que ninguém saiba qual vale. Com um dono único por domínio, sempre há uma resposta para "qual é a versão correta?".

## O mapa de ownership

A tabela abaixo é a referência. Ela diz, para cada domínio de verdade, qual workspace é a fonte canônica e o que os outros dois recebem dele.

| Domínio | Fonte canônica | Os demais recebem |
|---|---|---|
| Valor, prioridade, outcome e requisitos | `pm/` | decisão aprovada e handoff de produto |
| Evidência de usuário, jornada e experiência | `ux/` | UX spec, critérios e handoff de experiência |
| Arquitetura, implementação e risco operacional | `tech-lead/` | viabilidade, contratos técnicos e evidence pack |

Repare que isso é a mesma [tabela de direitos de decisão](../2-modelo-operacional/trio-humano.md) do modelo operacional, agora expressa em termos de arquivos e pastas. O PM é dono do valor tanto na decisão quanto no disco; o UX, da experiência; o Tech Lead, da técnica. A organização física do trabalho espelha a autoridade humana.

## Como um agente busca contexto de outro domínio

Na prática, um agente frequentemente precisa de contexto que pertence a outro workspace. Um Software Engineer Agent, no workspace do Tech Lead, precisa consultar o PRD, que vive no workspace do PM. Como fazer isso sem criar uma cópia que vai divergir?

A regra tem duas opções, ambas seguras. A primeira é **seguir o link até a fonte** — ler o artefato onde ele realmente vive, no workspace dono. A segunda, quando o link direto não é viável, é usar um **snapshot identificado como não autoritativo** e confirmar sua validade antes de agir. O que nunca se faz é copiar a informação para o próprio workspace e passar a tratá-la como verdade local — porque no dia em que a original mudar, a cópia mente.

## Por que os exemplos são fictícios

Se você abrir os workspaces de exemplo do repositório, encontrará nomes, organizações, repositórios e estados fictícios. Isso é intencional: eles demonstram a estrutura, não o trabalho de produção de uma equipe real. Ao copiar a estrutura para o seu time, esses valores devem ser substituídos pelos seus.

## Continue por aqui

Você entende a estrutura e o ownership. Falta a peça que torna tudo isso *operável por agentes* de forma repetível — o [Harness do workspace](harness-do-workspace.md).
