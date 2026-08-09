---
title: Agent Team — catálogo de skills
status: canonical
updated_at: 2026-08-09
---

# Catálogo de skills

> As 22 skills do Agent Team, o que cada uma garante e em que ponto da jornada ela é obrigatória.

## Em 2 minutos

Um agente sem skill improvisa. Ele inventa o nome do artefato, escolhe sozinho onde gravar, decide na hora o que conta como evidência — e o resultado é um repositório onde cada execução seguiu uma convenção diferente. Uma skill é o oposto disso: um procedimento nomeado, com entrada, saída e critério de conclusão, que produz o mesmo formato de artefato toda vez que roda.

Por isso a regra da operação é curta e sem exceção: **verificar as skills disponíveis antes de agir e usar todas as que se aplicam**. Uma skill aderente à missão não pode ser ignorada, e o agente cita no Work Item, no handoff e no resultado quais usou — ou o motivo de nenhuma se aplicar.

As skills se dividem em três naturezas. As **de base** governam a operação do workspace e valem para qualquer missão, em qualquer papel. As **de domínio** correspondem a uma etapa específica da jornada e produzem o artefato daquela etapa. As **de publicação** tocam Git e GitHub, e por isso só executam mediante pedido explícito.

| Natureza | Skills | Quando se aplicam |
|---|---|---|
| **Base de workspace** | `workspace-memory`, `workspace-projects`, `workspace-board` | toda missão, sempre |
| **Discovery e produto** | `business-discovery`, `write-feature`, `review-prd` | etapas 01–02 |
| **Especificação técnica** | `technical-discovery`, `create-spec`, `refine-spec`, `review-spec`, `review-cross-prd-spec` | etapa 03 |
| **Implementação e validação** | `dev-flow`, `implement`, `test-integration-local`, `code-review` | etapas 04–05 |
| **Correção de defeito** | `analyse-bug`, `fix-bug` | fora do ciclo, sob demanda |
| **Publicação** | `commit`, `update-pr`, `check-pr` | etapa 06, só com autorização |
| **Conhecimento** | `update-docs` | etapa 09 |

---

## Mapa deste documento

| Seção | Responde | Leia se você… |
|---|---|---|
| [1. Skills de base](#1-skills-de-base) | O que vale para toda missão | vai operar em qualquer workspace |
| [2. Skills por etapa](#2-skills-por-etapa-da-jornada) | Qual skill roda em qual fase | está executando uma etapa |
| [3. Anatomia de uma skill](#3-anatomia-de-uma-skill) | Como uma skill é escrita | vai criar ou revisar uma skill |
| [4. Limites de autonomia](#4-limites-de-autonomia) | O que exige autorização humana | vai delegar execução a um agente |

**Vizinhos:** [modelo operacional](../docs/operating-model.md) · [workflows por etapa](../docs/workflows/README.md) · [catálogo de agentes](../docs/agents/catalog.md) · [contrato de artefatos](references/workflow-contract.md).

---

## 1. Skills de base

As três skills de base existem porque o erro mais caro de um agente não é escrever código ruim: é escrever o artefato certo no lugar errado, ou tratar memória operacional como fonte de verdade. Elas são obrigatórias em qualquer missão, antes de qualquer skill de domínio.

| Skill | Garante | Falha que ela previne |
|---|---|---|
| [`workspace-memory`](workspace-memory/SKILL.md) | Retomada de contexto e escrita segura de memória | agente tratar `memory.md` como fonte canônica |
| [`workspace-projects`](workspace-projects/SKILL.md) | Fonte canônica correta e assets isolados por sessão | conclusão gravada no domínio errado; sessões se sobrescrevendo |
| [`workspace-board`](workspace-board/SKILL.md) | Seleção, transição e reconciliação de Work Items | trabalho sem item, ou item movido para `done` sem evidência |

A ordem prática ao iniciar uma missão: `workspace-memory` para recuperar contexto, `workspace-board` para assumir o item, `workspace-projects` para localizar onde o artefato pertence — e só então a skill de domínio.

---

## 2. Skills por etapa da jornada

Cada etapa da jornada tem a skill que produz seu artefato. A tabela abaixo é a tradução direta dos [workflows](../docs/workflows/README.md) para procedimentos executáveis.

| Etapa | Skill | Entrega |
|---|---|---|
| [01 · Discovery](../docs/workflows/01-discovery-and-research.md) | [`business-discovery`](business-discovery/SKILL.md) | requisitos de negócio acumulativos, com baseline, changelog e lacunas |
| [02 · Produto e UX](../docs/workflows/02-product-and-ux-planning.md) | [`write-feature`](write-feature/SKILL.md) | histórias fatiadas, vinculadas a regras e critérios |
| [02 · Produto e UX](../docs/workflows/02-product-and-ux-planning.md) | [`review-prd`](review-prd/SKILL.md) | PRD com objetivos, regras e critérios de sucesso rastreáveis |
| [03 · Especificação](../docs/workflows/03-technical-specification.md) | [`technical-discovery`](technical-discovery/SKILL.md) | visão técnica: componentes, dependências, riscos e decisões abertas |
| [03 · Especificação](../docs/workflows/03-technical-specification.md) | [`create-spec`](create-spec/SKILL.md) | SPEC com contratos, riscos e critérios técnicos verificáveis |
| [03 · Especificação](../docs/workflows/03-technical-specification.md) | [`refine-spec`](refine-spec/SKILL.md) | plano sequencial de blocos testáveis e suas dependências |
| [03 · Especificação](../docs/workflows/03-technical-specification.md) | [`review-spec`](review-spec/SKILL.md) | lacunas, ambiguidades e riscos da SPEC antes da aprovação |
| [03 · Especificação](../docs/workflows/03-technical-specification.md) | [`review-cross-prd-spec`](review-cross-prd-spec/SKILL.md) | cobertura, conflitos e decisões pendentes entre PRD e SPEC |
| [04 · Implementação](../docs/workflows/04-autonomous-implementation.md) | [`implement`](implement/SKILL.md) | um bloco do plano implementado, com validação incremental |
| [04 · Implementação](../docs/workflows/04-autonomous-implementation.md) | [`dev-flow`](dev-flow/SKILL.md) | condução de ponta a ponta quando a entrega não exige fase a fase |
| [04 · Implementação](../docs/workflows/04-autonomous-implementation.md) | [`test-integration-local`](test-integration-local/SKILL.md) | cobertura faltante criada e critérios mapeados a testes |
| [05 · Validação](../docs/workflows/05-adversarial-validation.md) | [`code-review`](code-review/SKILL.md) | achados acionáveis contra SPEC, testes e riscos |
| [06 · PR e merge](../docs/workflows/06-pr-and-merge.md) | [`commit`](commit/SKILL.md) · [`update-pr`](update-pr/SKILL.md) · [`check-pr`](check-pr/SKILL.md) | mudança registrada, descrita e verificada |
| [09 · Conhecimento](../docs/workflows/09-knowledge-curation.md) | [`update-docs`](update-docs/SKILL.md) | documentação alinhada ao entregue, com desvios registrados |

**Correção de defeito.** Bugs entram fora da sequência, e por isso têm par próprio: [`analyse-bug`](analyse-bug/SKILL.md) rastreia causa raiz e documenta impacto **sem tocar em código**, e [`fix-bug`](fix-bug/SKILL.md) implementa a correção com teste de regressão. A separação é deliberada — corrigir antes de entender o impacto é como a maior parte das regressões nasce.

---

## 3. Anatomia de uma skill

Uma skill é um diretório com `SKILL.md` na raiz. O front matter declara `name` e `description`, e a descrição é o que determina se a skill será acionada: ela diz o que a skill faz e **em que situação usar**, porque é por esse texto que o agente decide se ela se aplica à missão em curso.

```text
skills/<nome>/
├── SKILL.md        # procedimento: entrada, passos, saída e critério de conclusão
├── README.md       # contexto adicional, quando o procedimento não se explica sozinho
├── templates/      # formatos de artefato que a skill produz
└── agents/         # configuração de agente específica, quando houver
```

Skills que compartilham convenções de artefato apontam para o [contrato de artefatos](references/workflow-contract.md), que define onde PRD, SPEC, planos e requisitos vivem e o que fazer quando o repositório consumidor diverge do layout padrão. A regra central dele: **a convenção local do repositório prevalece**, e o mapeamento é confirmado antes de escrever.

Diferente da documentação para humanos, `SKILL.md` é lido por um agente durante a execução. Listas densas e imperativas são intencionais ali — o [padrão de documentação](../docs/documentation-standard.md) se aplica aos documentos de leitura humana, não a estas instruções.

---

## 4. Limites de autonomia

Skills não ampliam permissão. Uma skill de implementação não autoriza publicar, e nenhuma delas decide sozinha o que vira baseline aprovado.

| Ação | Exige pedido explícito |
|---|---|
| Criar branch, worktree e alterar código local | não, dentro do escopo autorizado do Work Item |
| Criar issue, commit, push, PR, merge e limpeza de worktree | sim, cada uma separadamente |
| Alterar requisitos, critérios de aceite ou status de PRD/SPEC aprovados | sim, com decisão registrada |
| Mover um Work Item para `done` | não, mas só com evidência para todos os critérios |

Desvios em relação a um baseline aprovado vão para relatório, nunca para edição silenciosa do artefato. É essa assimetria — executar com liberdade, publicar sob autorização — que sustenta os níveis de autonomia descritos no [modelo 90/10](../docs/operating-model-90-10.md).
