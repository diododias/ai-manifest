---
title: Agent Team — jornada por fases
status: reference
updated_at: 2026-08-09
---

# Agent Team — jornada por fases

> O mesmo ciclo do [fluxo completo](end-to-end-journey.md), quebrado em cinco blocos que cabem em uma tela — ou em um slide.

## Em 2 minutos

O diagrama de ponta a ponta serve para ver o sistema inteiro; este documento serve para **discutir uma parte de cada vez**. Cada bloco traz seu escopo, seu diagrama isolado e as perguntas que costumam surgir naquela discussão.

A numeração das etapas é idêntica à do fluxo completo, então os dois documentos podem ser usados juntos sem tradução mental.

| Bloco | Etapas | Checkpoints | Artefatos centrais |
|---|---|---|---|
| [1 — Produto e descoberta](#bloco-1--produto-e-descoberta) | 0–2 | H1, H2 | `PB.md`, `PRD.md` |
| [2 — Especificação técnica](#bloco-2--especificação-técnica) | 3 | H3 (condicional) | `PLAN`, `ADR`, `SPEC`, `TASKS`, `CHECKLIST` |
| [3 — Construção e validação](#bloco-3--construção-e-validação) | 4–5 | nenhum (só exceção) | mudança pronta para PR |
| [4 — Integração e entrega](#bloco-4--integração-e-entrega) | 6–8 | H4, H5 | PR, release candidate, release |
| [5 — Conhecimento e melhoria](#bloco-5--conhecimento-e-melhoria-contínua) | 9–10 | H6 (condicional) | `MEMORY.md`, demandas de melhoria |

Os contratos de interação entre os agentes estão no [mapa de workflows](workflows/README.md).

---

## Mapa dos blocos

```mermaid
flowchart LR
    P1["Bloco 1<br/>Produto e descoberta<br/>Etapas 0–2"]
    P2["Bloco 2<br/>Especificação técnica<br/>Etapa 3"]
    P3["Bloco 3<br/>Construção e validação<br/>Etapas 4–5"]
    P4["Bloco 4<br/>Integração e entrega<br/>Etapas 6–8"]
    P5["Bloco 5<br/>Conhecimento e melhoria<br/>Etapas 9–10"]

    P1 --> P2 --> P3 --> P4 --> P5
    P5 -. "melhorias retornam ao backlog" .-> P1

    classDef phase fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    class P1,P2,P3,P4,P5 phase;
```

---

## Bloco 1 — produto e descoberta

Do registro de uma necessidade até a aprovação do que será construído. É o bloco onde mais evidência é produzida e onde um erro custa menos para corrigir.

| Escopo | |
|---|---|
| **Workflows** | [intake](workflows/00-intake-and-triage.md), [discovery e research](workflows/01-discovery-and-research.md), [planejamento de produto e UX](workflows/02-product-and-ux-planning.md) |
| **Etapas** | 0 backlog e triagem · 1 discovery multiagente · 2 planejamento de produto |
| **Checkpoints** | H1 e H2 |
| **Artefatos** | `PB.md` e `PRD.md` |

```mermaid
flowchart LR
    IN([Problema ou oportunidade])

    S0["0. Backlog e triagem<br/>Intake + PM Agents"]
    G0{{"Gate<br/>contexto, owner, duplicidade e risco"}}

    S1["1. Discovery<br/>PM + UX Spec + Tech Lead"]
    G1{{"Gate<br/>problema, usuário, experiência e viabilidade"}}
    H1{"H1 · Vale investir?"}

    S2["2. Planejamento<br/>PM + Adversarial PM"]
    G2{{"Gate<br/>clareza, aceite, escopo e métricas"}}
    H2{"H2 · É isto que<br/>construiremos?"}

    OUT([PRD aprovado])

    IN --> S0 --> G0
    G0 -- "incompleto" --> S0
    G0 -- "aprovado" --> S1 --> G1
    G1 -- "gap" --> S1
    G1 -- "aprovado" --> H1
    H1 -- "ajustar" --> S1
    H1 -- "adiar" --> S0
    H1 -- "avançar" --> S2 --> G2
    G2 -- "ambiguidade" --> S2
    G2 -- "aprovado" --> H2
    H2 -- "revisar" --> S2
    H2 -- "aprovar" --> OUT

    classDef agent fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;
    class S0,S1,S2 agent;
    class G0,G1,G2 automation;
    class H1,H2 human;
    class IN,OUT terminal;
```

### Foco da discussão

- O problema está claro antes de discutir solução?
- Usuário, experiência e viabilidade foram analisados juntos?
- O adversarial PM encontrou ambiguidades reais?
- Os humanos decidiram valor e escopo, não detalhes operacionais?

---

## Bloco 2 — especificação técnica

Transforma produto e UX aprovados em uma estratégia técnica executável, criticada antes de virar tarefa. H3 só é acionado por exceção — em fluxo normal, este bloco vai direto para a implementação.

| Escopo | |
|---|---|
| **Workflow** | [especificação técnica](workflows/03-technical-specification.md) |
| **Etapa** | 3 especificação e crítica técnica |
| **Checkpoint** | H3, condicional |
| **Artefatos** | `PLAN.md`, `ADR.md`, `SPEC.md`, `TASKS.md`, `CHECKLIST.md` |

```mermaid
flowchart LR
    IN([PRD aprovado])
    S3["3. Especificação técnica<br/>Specification TL"]
    ADV["Crítica técnica<br/>Adversarial TL"]
    G3{{"Gate<br/>rastreabilidade, riscos, tarefas e trade-offs"}}
    RISK{"Nova ADR, exceção<br/>ou risco R3/R4?"}
    H3{"H3 · Aceitamos<br/>os trade-offs?"}
    OUT([Especificação executável])

    IN --> S3 --> ADV --> G3
    G3 -- "gap" --> S3
    G3 -- "aprovado" --> RISK
    RISK -- "não" --> OUT
    RISK -- "sim" --> H3
    H3 -- "revisar" --> S3
    H3 -- "aceitar" --> OUT

    classDef agent fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;
    class S3,ADV agent;
    class G3,RISK automation;
    class H3 human;
    class IN,OUT terminal;
```

### Foco da discussão

- A solução responde ao PRD sem ampliar o escopo?
- Alternativas e trade-offs foram registrados?
- As tarefas podem ser implementadas e validadas isoladamente?
- H3 está reservado a decisões realmente estruturais ou arriscadas?

---

## Bloco 3 — construção e validação

O bloco mais autônomo do ciclo: em fluxo saudável, nenhuma pessoa é acionada entre a tarefa aprovada e o PR. Gates locais e CI é que decidem se o trabalho avança.

| Escopo | |
|---|---|
| **Workflows** | [implementação autônoma](workflows/04-autonomous-implementation.md), [validação adversarial](workflows/05-adversarial-validation.md) |
| **Etapas** | 4 implementação autônoma · 5 validação adversarial |
| **Checkpoints** | nenhum; intervenção humana somente por exceção |
| **Saída** | mudança pronta para PR |

```mermaid
flowchart LR
    IN([Tarefa elegível])
    S4["4. Implementação<br/>Orchestrator + Engineer Agents"]
    LOCAL{{"Hooks locais<br/>pre-commit + pre-push"}}
    S5["5. Validação adversarial<br/>QA + Security + Architecture"]
    CI{{"CI fast + deep lanes<br/>checks conforme risco"}}
    HUMAN["Escalonar com<br/>evidências e contexto"]
    OUT([Mudança pronta para PR])

    IN --> S4 --> LOCAL
    LOCAL -- "falhou" --> S4
    LOCAL -- "aprovado" --> S5 --> CI
    CI -- "falhou e corrigível" --> S4
    CI -- "falhou repetidamente" --> HUMAN
    HUMAN -- "decisão" --> S4
    CI -- "aprovado" --> OUT

    classDef agent fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;
    class S4,S5 agent;
    class LOCAL,CI automation;
    class HUMAN human;
    class IN,OUT terminal;
```

### Foco da discussão

- Quais falhas podem ser corrigidas automaticamente?
- Quais checks pertencem ao hook local ou à CI?
- A deep lane é acionada por risco e paths alterados?
- O escalonamento entrega uma decisão objetiva ao humano?

---

## Bloco 4 — integração e entrega

Do PR à observação em produção. É onde a classe de risco pesa mais: R0 atravessa o bloco quase sem parada, R4 exige dupla aprovação e acompanhamento humano.

| Escopo | |
|---|---|
| **Workflows** | [PR e merge](workflows/06-pr-and-merge.md), [homologação](workflows/07-release-candidate-validation.md), [produção e observação](workflows/08-production-release-and-observation.md) |
| **Etapas** | 6 PR e decisão de merge · 7 homologação automatizada · 8 produção e observação inicial |
| **Checkpoints** | H4 e H5 |

```mermaid
flowchart LR
    IN([Mudança validada])
    S6["6. PR + evidence pack<br/>PR + Reviewer Agents"]
    H4{"H4 · Podemos integrar?"}
    MERGE["Merge protegido<br/>checks + approvals"]
    S7["7. Homologação<br/>preview + E2E + evidências"]
    G7{{"Gate<br/>release candidate aprovado"}}
    RISK{"Política exige<br/>aprovação de produção?"}
    H5{"H5 · Podemos expor<br/>o risco?"}
    S8["8. Produção<br/>rollout progressivo"]
    HEALTH{{"Gate pós-deploy<br/>SLOs + métricas"}}
    BACK["Rollback ou<br/>pausa automática"]
    REWORK([Retorno à etapa 4])
    OUT([Entrega saudável])

    IN --> S6 --> H4
    H4 -- "ajustar" --> REWORK
    H4 -- "aprovar" --> MERGE --> S7 --> G7
    G7 -- "falhou" --> REWORK
    G7 -- "aprovado" --> RISK
    RISK -- "não" --> S8
    RISK -- "sim · R3/R4" --> H5
    H5 -- "revisar" --> S7
    H5 -- "aprovar" --> S8
    S8 --> HEALTH
    HEALTH -- "regressão" --> BACK
    BACK --> REWORK
    HEALTH -- "saudável" --> OUT

    classDef agent fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;
    classDef failure fill:#fee2e2,stroke:#dc2626,color:#450a0a,stroke-width:1.5px;
    class S6,S7,S8 agent;
    class MERGE,G7,RISK,HEALTH automation;
    class H4,H5 human;
    class IN,REWORK,OUT terminal;
    class BACK failure;
```

### Foco da discussão

- O evidence pack permite review sem ler todo o diff?
- H4 varia corretamente conforme a classe de risco?
- A homologação comprova critérios de aceite?
- Deploy e rollback foram automatizados antes de reduzir H5?

---

## Bloco 5 — conhecimento e melhoria contínua

O bloco que fecha o ciclo sobre o próprio sistema: registra o que a entrega ensinou e converte atrito recorrente em demanda priorizável.

| Escopo | |
|---|---|
| **Workflows** | [curadoria de conhecimento](workflows/09-knowledge-curation.md), [telemetria e melhoria contínua](workflows/10-continuous-improvement.md) |
| **Etapas** | 9 conhecimento específico da entrega · 10 Auto Dream semanal |
| **Checkpoint** | H6, condicional ou por amostragem |
| **Saídas** | `MEMORY.md` e demandas de melhoria |

```mermaid
flowchart LR
    IN([Entrega e sessões concluídas])
    S9["9. Conhecimento da entrega<br/>Knowledge Agent"]
    OBS["Sessões + feedback + gates<br/>falhas + retries + métricas"]
    WEEK([Agenda semanal])
    S10["10. Auto Dream<br/>análise do sistema de trabalho"]
    CRITIC["Critic Agent<br/>confirma ou contesta conclusões"]
    SENSITIVE{"Memória sensível, P0/P1<br/>ou mudança de gate?"}
    H6{"H6 · O sistema aprendeu<br/>corretamente?"}
    TYPE{"Resultado analisado"}
    MEMORY["Aprendizado validado<br/>atualizar MEMORY.md"]
    DEMAND["Falha ou atrito<br/>gerar demanda no backlog"]
    BACKLOG([Próximo ciclo])

    IN --> S9 --> OBS
    IN --> OBS
    WEEK --> S10
    OBS --> S10 --> CRITIC --> SENSITIVE
    SENSITIVE -- "sim" --> H6
    SENSITIVE -- "não ou amostragem" --> TYPE
    H6 -- "aprovar" --> TYPE
    H6 -- "mais evidências" --> S10
    TYPE -- "funcionou" --> MEMORY
    TYPE -- "deu errado" --> DEMAND
    MEMORY -. "contexto reutilizável" .-> BACKLOG
    DEMAND -- "melhoria priorizável" --> BACKLOG

    classDef agent fill:#dbeafe,stroke:#2563eb,color:#172554,stroke-width:1.5px;
    classDef automation fill:#dcfce7,stroke:#16a34a,color:#052e16,stroke-width:1.5px;
    classDef human fill:#fef3c7,stroke:#d97706,color:#451a03,stroke-width:2px;
    classDef knowledge fill:#f3e8ff,stroke:#9333ea,color:#3b0764,stroke-width:1.5px;
    classDef terminal fill:#f1f5f9,stroke:#475569,color:#0f172a,stroke-width:1.5px;
    class S9,S10,CRITIC agent;
    class SENSITIVE,TYPE automation;
    class H6 human;
    class OBS,WEEK,MEMORY,DEMAND knowledge;
    class IN,BACKLOG terminal;
```

### Foco da discussão

- O aprendizado possui evidência e contexto de aplicação?
- O Critic Agent é independente de quem gerou a conclusão?
- Problemas recorrentes viram demandas acionáveis?
- H6 protege somente mudanças sensíveis sem virar gargalo?
- As melhorias retornam efetivamente ao backlog?

---

## Legenda comum

| Cor | Significa |
|---|---|
| 🔵 Azul | Agent Teams e agentes especializados |
| 🟢 Verde | automações, gates, hooks e decisões por política |
| 🟡 Amarelo | decisão ou intervenção humana |
| 🟣 Roxo | conhecimento, telemetria e melhoria contínua |
| 🔴 Vermelho | recuperação ou rollback |
| ⚪ Cinza | entrada ou saída do bloco |

## Uso sugerido

Para apresentar a jornada completa, comece pelo mapa dos blocos e depois use um bloco por slide. A ordem que funciona melhor em discussão é falar primeiro dos objetivos e das decisões humanas de cada bloco, e só depois detalhar agentes, automações e gates — quem escuta precisa entender o porquê antes do mecanismo.

Mantenha a numeração alinhada ao [fluxo completo](end-to-end-journey.md): é o que permite alternar entre os dois documentos sem reexplicar o contexto.
