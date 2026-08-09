---
title: Agent Team — workflows multiagente
status: proposed
updated_at: 2026-08-08
---

# Workflows multiagente

Um workflow é o contrato de colaboração entre dois ou mais agentes dentro de uma etapa da jornada. Ele define a sequência de missões, os artefatos que atravessam as fronteiras, a forma de convergir contribuições independentes e o ponto em que uma decisão deve ser escalada ao humano responsável.

Os workflows detalham a colaboração. Eles não substituem os contratos individuais do [catálogo de agentes](../agents/catalog.md), a autoridade do [modelo operacional](../operating-model.md) nem os gates do [modelo 90/10](../operations/operating-model-90-10.md).

## Onde o workflow vive e onde a execução acontece

`docs/workflows/` é o **catálogo canônico e versionado** dos workflows reutilizáveis. Ele não recebe artefatos de uma execução concreta.

Cada usuário ou papel executa o workflow dentro de seu próprio workspace. A instalação desse workspace deve conter `docs/workflows/` para registrar os workflows habilitados, sua versão, permissões, integrações e adaptações locais. Essa camada local referencia o workflow canônico — não o copia nem passa a ser fonte de verdade concorrente.

```text
<workspace-do-usuario>/
├── docs/
│   └── workflows/              # bindings locais para docs/workflows/
├── projects/
│   └── <project>/              # artefatos persistentes de uma execução
├── coordination/               # handoffs e bloqueios temporários
├── memory/                     # contexto retomável, nunca fonte canônica
└── repos/                      # somente no workspace técnico, quando aplicável
```

Antes de iniciar uma missão, o agente resolve: `workspace do owner → projects/<project> → Work Item → fontes canônicas`. Ele nunca grava no catálogo global um `PB`, `PRD`, plano, evidência ou handoff de uma execução.

## Localização dos artefatos por workflow

Os nomes abaixo usam `<pm-workspace>`, `<ux-workspace>` e `<tech-lead-workspace>` para representar workspaces individuais, e `<project>` para o identificador comum entre eles.

| Workflow | Fontes e artefatos persistentes | Trânsito temporário |
|---|---|---|
| Intake | `<pm-workspace>/projects/<project>/work-items/` | `<pm-workspace>/coordination/inbox/` e `handoffs/` |
| Discovery e research | PM: `<pm-workspace>/projects/<project>/discovery/`; UX: `<ux-workspace>/projects/<project>/research/` e `journeys/`; viabilidade técnica: `<tech-lead-workspace>/projects/<project>/engineering/architecture/` | `coordination/handoffs/` de cada workspace |
| Produto e UX | PM: `<pm-workspace>/projects/<project>/requirements/prd/`, `strategy/`, `decisions/`; UX: `<ux-workspace>/projects/<project>/flows/`, `specifications/`, `prototypes/` e `validation/` | handoffs em `<pm-workspace>/projects/<project>/handoffs/` e `<ux-workspace>/projects/<project>/handoffs/` |
| Especificação técnica | `<tech-lead-workspace>/projects/<project>/plans/active/`, `engineering/specs/`, `engineering/adr/` e `work-items/` | `execution/handoffs/` |
| Implementação | `<tech-lead-workspace>/projects/<project>/work-items/`, `execution/evidence/` e `repos/worktrees/<org>/<repo>/<work-item>/` | `coordination/active/` e `execution/handoffs/` |
| Validação e PR | `<tech-lead-workspace>/projects/<project>/execution/reviews/` e `execution/evidence/` | `coordination/blockers/` para exceções ativas |
| Homologação | PM: `<pm-workspace>/projects/<project>/validation/`; UX: `<ux-workspace>/projects/<project>/validation/`; Tech Lead: `<tech-lead-workspace>/projects/<project>/execution/evidence/` | handoff para release |
| Produção e observação | `<tech-lead-workspace>/projects/<project>/execution/evidence/`, `learnings/candidates/` e o registro autorizado de release | incidente, alerta e rollback em `coordination/` até serem promovidos |
| Conhecimento e melhoria | fonte canônica do domínio; Tech Lead: `projects/<project>/learnings/{candidates,accepted}/`; PM: novo item em `projects/<project>/work-items/` | propostas e hipóteses em `coordination/`, até decisão do owner |

`coordination/` e `memory/` são auxiliares: um handoff só se torna concluído quando seu artefato final está na fonte canônica do projeto. Se uma subpasta necessária ainda não existir, ela deve ser criada sob `projects/<project>/` no workspace que detém o domínio — nunca sob o catálogo global ou como diretório genérico de outro usuário.

## Mapa da jornada

| Etapa | Workflow | Agente que consolida | Agentes que colaboram ou desafiam |
|---:|---|---|---|
| 0 | [Intake e triagem](00-intake-and-triage.md) | Intake Agent | Product Manager Agent; Meeting Context quando houver reunião |
| 1 | [Discovery e research](01-discovery-and-research.md) | Product Manager Agent | UX Specification; Tech Lead Discovery; Adversarial PM quando houver proposta candidata |
| 2 | [Planejamento de produto e UX](02-product-and-ux-planning.md) | Product Manager Agent + UX Specification | Adversarial Product Manager; especialistas de pesquisa, conteúdo ou prototipação |
| 3 | [Especificação técnica](03-technical-specification.md) | Specification Tech Lead | Adversarial Tech Lead; Security/Data/Platform quando necessário |
| 4 | [Implementação autônoma](04-autonomous-implementation.md) | Orchestrator Agent | Software Engineer Agents |
| 5 | [Validação adversarial](05-adversarial-validation.md) | QA / Validation Agent | Security Review; Architecture Review; Adversarial Code Reviewer |
| 6 | [PR e merge](06-pr-and-merge.md) | PR Agent | Reviewer Agents |
| 7 | [Homologação](07-release-candidate-validation.md) | Product Validation Agent | Release Agent |
| 8 | [Produção e observação](08-production-release-and-observation.md) | Release Agent | Observability Agent |
| 9 | [Curadoria de conhecimento](09-knowledge-curation.md) | Knowledge Agent | Critic Agent quando a alteração for sensível |
| 10 | [Telemetria e melhoria contínua](10-continuous-improvement.md) | Auto Dream Agent | Telemetry; Observability; Critic Agent |

## Contrato comum

Todo workflow deve explicitar:

- artefatos de entrada e critérios para iniciá-lo;
- missões, dependências e se podem ser executadas em paralelo;
- único agente responsável por consolidar a saída;
- handoffs com fatos, evidências, hipóteses, riscos e perguntas em aberto;
- gate de saída e destino em caso de falha;
- condição de escalonamento e owner humano da decisão.

O orquestrador distribui contexto mínimo e controla dependências. Ele não substitui o consolidado do agente primário nem a decisão do owner humano. Agentes de crítica devem ser instâncias independentes de quem produziu o artefato avaliado.

## Convenções de execução

- Toda missão usa o envelope de saída do [catálogo](../agents/catalog.md#23-envelope-padrão-de-saída).
- Um handoff referencia artefatos versionados e não copia o contexto inteiro.
- Uma contribuição não vira decisão pelo simples fato de estar no consolidado: divergências e riscos residuais permanecem explícitos.
- Nova informação material devolve o workflow ao agente responsável pela revisão; ela também invalida a aprovação relacionada quando a política determinar.
- O workflow termina com artefato coerente e evidence pack, não com respostas isoladas dos agentes.
- O binding local em `<workspace>/docs/workflows/` declara a versão do workflow canônico e pode restringir ferramentas, permissões e integrações; ele não pode ampliar autonomia ou alterar gates sem a decisão prevista no modelo operacional.
