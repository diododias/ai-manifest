---
title: Agent Team — workflows multiagente
status: proposed
updated_at: 2026-08-09
---

# Workflows multiagente

> O contrato de colaboração entre agentes em cada uma das 12 etapas da jornada: quem faz o quê, em que ordem, onde cada agente escreve, o que atravessa a fronteira e quando escalar.

## Em 2 minutos

O [catálogo de agentes](../agents/catalog.md) define cada papel isoladamente. Um workflow define o que acontece **entre** eles: a sequência de missões, os artefatos que atravessam as fronteiras, como contribuições independentes convergem em uma saída coerente, e o ponto em que uma decisão deve ser escalada ao humano responsável.

Os workflows detalham a colaboração. Eles não substituem os contratos individuais do catálogo, a autoridade da [metodologia](../docs/METODOLOGIA.md) nem a arquitetura de [gates](../docs/GATES.md). O que cada repositório precisa carregar para que esses workflows rodem com agentes está no [Repo Harness](../docs/REPO_HARNESS.md).

Duas distinções resolvem a maior parte das dúvidas na prática:

| Distinção | O que significa |
|---|---|
| **Catálogo vs. execução** | `workflows/` é o catálogo canônico e versionado; a execução acontece no workspace do owner, em `projects/<project>/`. Nada de uma execução é gravado no catálogo. |
| **Canônico vs. trânsito** | Artefatos persistentes vivem na fonte canônica do domínio; `.coordination/` e `memory.md` são auxiliares e um handoff só termina quando o artefato final chegou à fonte canônica. |

Cada etapa tem writer/consolidador explícito para cada saída e agentes que colaboram ou desafiam. A etapa 2 possui dois consolidadores de domínio e uma barreira de coerência; nas demais, um único agente consolida o bloco. A crítica sempre vem de uma instância independente de quem produziu o artefato.

---

## Modo dry-run

Workflows podem ser executados em modo de experimentação sem gerar artefatos persistentes.

**Como ativar:** passe `mode: dry-run` no início da missão ou prefixe o comando com `--dry-run`.

**Comportamento esperado:**
- O agente executa todo o raciocínio, análises e rascunhos normalmente.
- Não cria nem modifica arquivos em `projects/`, `engineering/`, `execution/` ou qualquer outra pasta de artefatos.
- Pode imprimir o que *teria* gerado diretamente na conversa.
- Não atualiza `BOARD.md`, `STATUS.md`, Work Items nem handoffs.

**Quando usar:** explorar um workflow desconhecido, testar uma abordagem antes de comprometê-la, ou validar o comportamento do agente sem efeitos colaterais.

## Onde o workflow vive e onde a execução acontece

`workflows/` é o **catálogo canônico e versionado** dos workflows reutilizáveis. Ele não recebe artefatos de uma execução concreta.

Cada usuário ou papel executa o workflow dentro de seu próprio workspace. A instalação desse workspace deve conter `docs/workflows/` para registrar os workflows habilitados, sua versão, permissões, integrações e adaptações locais. Essa camada local referencia o workflow canônico — não o copia nem passa a ser fonte de verdade concorrente.

```text
<workspace-do-usuario>/
├── docs/
│   └── workflows/              # bindings locais para workflows/
├── projects/
│   └── <project>/              # artefatos persistentes de uma execução
├── .coordination/              # handoffs e bloqueios temporários (oculto)
├── memory.md                   # contexto retomável do agente, nunca fonte canônica
└── repos/                      # somente no workspace técnico, quando aplicável
```

Antes de iniciar uma missão, o agente resolve: `workspace do owner → projects/<project> → Work Item → fontes canônicas`. Ele nunca grava no catálogo global um `PB`, `PRD`, plano, evidência ou handoff de uma execução.

## Localização dos artefatos por workflow

Os nomes abaixo usam `<pm-workspace>`, `<ux-workspace>` e `<tech-lead-workspace>` para representar workspaces individuais, e `<project>` para o identificador comum entre eles.

| Workflow | Fontes e artefatos persistentes | Trânsito temporário |
|---|---|---|
| Intake | `<pm-workspace>/projects/<project>/work-items/` | `<pm-workspace>/.coordination/inbox/` e `handoffs/` |
| Discovery e research | PM: `<pm-workspace>/projects/<project>/discovery/`; UX: `<ux-workspace>/projects/<project>/research/` e `journeys/`; viabilidade técnica: `<tech-lead-workspace>/projects/<project>/engineering/architecture/` | `.coordination/handoffs/` de cada workspace |
| Produto e UX | PM: `<pm-workspace>/projects/<project>/requirements/prd/`, `strategy/`, `decisions/`; UX: `<ux-workspace>/projects/<project>/flows/`, `specifications/`, `prototypes/` e `validation/` | handoffs em `<pm-workspace>/projects/<project>/handoffs/` e `<ux-workspace>/projects/<project>/handoffs/` |
| Especificação técnica | `<tech-lead-workspace>/projects/<project>/plans/active/`, `engineering/specs/`, `engineering/adr/` e `work-items/` | `execution/handoffs/` |
| Implementação | `<tech-lead-workspace>/projects/<project>/work-items/`, `execution/evidence/` e `repos/worktrees/<org>/<repo>/<work-item>/` | `.coordination/active/` e `execution/handoffs/` |
| Validação e PR | `<tech-lead-workspace>/projects/<project>/execution/reviews/` e `execution/evidence/` | `.coordination/blockers/` para exceções ativas |
| Homologação | PM: `<pm-workspace>/projects/<project>/validation/`; UX: `<ux-workspace>/projects/<project>/validation/`; Tech Lead: `<tech-lead-workspace>/projects/<project>/execution/evidence/` | handoff para release |
| Produção e observação | `<tech-lead-workspace>/projects/<project>/execution/evidence/`, `LEARNINGS.md` (candidatos) e o registro autorizado de release | incidente, alerta e rollback em `.coordination/` até serem promovidos |
| Curadoria de conhecimento | fonte canônica do domínio, `projects/<project>/LEARNINGS.md` e `execution/reviews/knowledge-<id>.md` | propostas não decididas em `.coordination/` |
| Melhoria contínua | Tech Lead: `execution/telemetry/`; memória validada no workspace; PM: `projects/<project>/work-items/` | hipóteses em `.coordination/observations/` |
| Operação diária | memória validada e Work Items promovidos aos respectivos workspaces | briefing em `.coordination/daily/`, hipóteses e cursor diário |

`.coordination/` e `memory.md` são auxiliares: um handoff só se torna concluído quando seu artefato final está na fonte canônica do projeto. Se uma subpasta necessária ainda não existir, ela deve ser criada sob `projects/<project>/` no workspace que detém o domínio — nunca sob o catálogo global ou como diretório genérico de outro usuário.

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
| 11 | [Operação diária](11-daily-operations.md) | Auto Dream Agent | Telemetry; Knowledge; Orchestrator; Intake |

## Contrato comum

Todo workflow explicita o bloco completo. A ausência de qualquer item abaixo torna a execução ambígua, não idempotente ou dependente de negociação humana.

| Item | Define |
|---|---|
| Unidade e entrada | identificadores, baseline, artefatos e critérios para iniciar |
| Preflight | autoridade, workspace, projeto, permissões, risco e condição de parada |
| Missões | DAG, dependências, paralelismo e contexto mínimo por agente |
| Writers e consolidação | quem escreve cada fonte e quem monta a saída do bloco |
| Skills | skills aplicáveis e registro exato em `skills_used` |
| Persistência | fontes canônicas, trânsito e ordem de reconciliação do workspace |
| Gates | gate de conteúdo e gate de fechamento do bloco com evidência |
| Handoffs | fatos, evidências, hipóteses, riscos e perguntas em aberto |
| Retry e escalonamento | limites de tentativa, invalidação, condição de parada e owner humano |
| Envelope final | estado, transição, outputs, decisões e prova de conclusão |

O bloco só fecha quando loop, agentes, fontes canônicas, estado do workspace e próxima decisão concordam. O orquestrador distribui contexto mínimo e controla dependências — ele não substitui o consolidador nem a decisão do owner humano. Agentes de crítica são sempre instâncias independentes de quem produziu o artefato avaliado.

## Convenções de execução

**Formato.** Toda missão usa o envelope de saída do [catálogo](../agents/catalog.md#23-envelope-padrão-de-saída), e um handoff referencia artefatos versionados em vez de copiar o contexto inteiro.

**Convergência.** Uma contribuição não vira decisão pelo simples fato de estar no consolidado: divergências e riscos residuais permanecem explícitos. O workflow termina com artefato coerente e evidence pack, nunca com respostas isoladas dos agentes.

**Revisão.** Nova informação material devolve o workflow ao agente responsável pela revisão, e invalida a aprovação relacionada quando a política determinar.

**Bindings locais.** O binding em `<workspace>/docs/workflows/` declara a versão do workflow canônico e pode **restringir** ferramentas, permissões e integrações. Ele não pode ampliar autonomia nem alterar gates sem a decisão prevista no modelo operacional — essa assimetria é intencional.
