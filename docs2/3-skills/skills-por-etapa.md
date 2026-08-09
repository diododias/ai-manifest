---
title: Skills por etapa da jornada
status: canonical
updated_at: 2026-08-09
---

# Skills por etapa da jornada

> Qual procedimento produz o artefato de cada fase, como bugs entram fora da sequência e por que as skills de publicação são tratadas à parte.

## A tradução direta da jornada para procedimentos

Cada etapa da jornada tem a skill que produz o seu artefato. Se você já conhece a jornada de [Gates e cerimônias](../2-modelo-operacional/gates-e-cerimonias.md), esta página é a tradução dela para procedimentos executáveis: onde antes você via "etapa de especificação", agora vê a skill concreta que gera o `SPEC.md`.

| Etapa | Skill | Entrega |
|---|---|---|
| 01 · Discovery | `business-discovery` | requisitos de negócio acumulativos, com baseline, changelog e lacunas |
| 02 · Produto e UX | `write-feature` | histórias fatiadas, vinculadas a regras e critérios |
| 02 · Produto e UX | `review-prd` | PRD com objetivos, regras e critérios de sucesso rastreáveis |
| 03 · Especificação | `technical-discovery` | visão técnica: componentes, dependências, riscos e decisões abertas |
| 03 · Especificação | `create-spec` | SPEC com contratos, riscos e critérios técnicos verificáveis |
| 03 · Especificação | `refine-spec` | plano sequencial de blocos testáveis e suas dependências |
| 03 · Especificação | `review-spec` | lacunas, ambiguidades e riscos da SPEC antes da aprovação |
| 03 · Especificação | `review-cross-prd-spec` | cobertura, conflitos e decisões pendentes entre PRD e SPEC |
| 04 · Implementação | `implement` | um bloco do plano implementado, com validação incremental |
| 04 · Implementação | `dev-flow` | condução de ponta a ponta quando a entrega não exige fase a fase |
| 04 · Implementação | `test-integration-local` | cobertura faltante criada e critérios mapeados a testes |
| 05 · Validação | `code-review` | achados acionáveis contra SPEC, testes e riscos |
| 06 · PR e merge | `commit` · `update-pr` · `check-pr` | mudança registrada, descrita e verificada |
| 09 · Conhecimento | `update-docs` | documentação alinhada ao entregue, com desvios registrados |

## Correção de defeito: um par que roda fora da sequência

Bugs não seguem a jornada linear — eles aparecem quando aparecem. Por isso têm um par de skills próprio, e a separação entre elas é deliberada. `analyse-bug` rastreia a causa raiz e documenta o impacto **sem tocar em código**. Só depois `fix-bug` implementa a correção, com teste de regressão.

Essa ordem parece burocrática até você entender o motivo: corrigir antes de entender o impacto é como nasce a maior parte das regressões. A disciplina de analisar primeiro protege contra a "correção" que conserta o sintoma e quebra outra coisa.

## Skills de publicação: liberdade para executar, autorização para publicar

Um subconjunto de skills toca Git e GitHub — `commit`, `update-pr`, `check-pr` — e por isso recebe tratamento especial: elas só executam **mediante pedido explícito**. Um agente pode implementar, testar e preparar tudo com liberdade dentro do escopo do Work Item, mas criar commit, abrir PR ou fazer merge são ações separadas, cada uma exigindo autorização.

A tabela abaixo torna essa fronteira precisa — é a mesma assimetria que sustenta os níveis de autonomia do modelo.

| Ação | Exige pedido explícito |
|---|---|
| Criar branch, worktree e alterar código local | não, dentro do escopo autorizado do Work Item |
| Criar issue, commit, push, PR, merge e limpeza de worktree | sim, cada uma separadamente |
| Alterar requisitos ou status de PRD/SPEC aprovados | sim, com decisão registrada |
| Mover um Work Item para `done` | não, mas só com evidência para todos os critérios |

## Por que "usar todas que se aplicam" importa

Um agente que ignora uma skill aplicável reintroduz exatamente o problema que as skills existem para resolver: variação entre execuções. Por isso a regra não admite exceção conveniente. Se duas skills se aplicam à mesma missão, ambas rodam. E quando o agente conclui a missão, ele declara no resultado e no handoff quais skills usou — tornando auditável se o procedimento correto foi seguido.

## Continue por aqui

Você já sabe qual skill roda em cada momento. Para entender como uma skill é construída por dentro — e criar as suas —, vá para [Anatomia de uma skill](anatomia-de-uma-skill.md).
