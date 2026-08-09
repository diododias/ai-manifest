---
title: Composição dos times por fase
status: canonical
updated_at: 2026-08-09
---

# Composição dos times por fase

> Como os papéis se combinam em times temporários a cada etapa, quem consolida a saída e por que a crítica vem sempre de uma instância independente.

## Times que se montam e se dissolvem

Uma ideia central do Agent Team é que **cada fase aciona um time temporário de agentes, dissolvido ao final**. Isso permite ter dezenas de especializações disponíveis sem manter nenhuma delas ociosa. Você não paga por um "Security Review Agent" parado — ele só existe quando a fase de validação de uma mudança sensível o exige.

Dentro de cada time, a dinâmica é sempre a mesma. Um **agente primário** conduz e consolida o artefato da fase. Um ou mais agentes **colaboram ou desafiam** a partir de uma responsabilidade explícita. E os agentes adversariais procuram ambiguidade, gaps, risco e suposição frágil — sempre como instâncias independentes de quem produziu.

## A composição etapa a etapa

A tabela abaixo mostra, para cada fase, quem consolida a saída, quem colabora ou critica, e o que atravessa a fronteira no handoff.

| Fase | Agente primário | Agentes críticos/especialistas | Handoff |
|---|---|---|---|
| Intake | Intake Agent | Meeting Context quando houver reunião | PM prioriza |
| Discovery | Product Manager Agent | UX Specification + Tech Lead Discovery | `PB.md` para H1 |
| Produto/UX | Product Manager + UX Specification | Adversarial Product Manager | PRD + UX spec para H2 |
| Especificação | Specification Tech Lead | Adversarial TL + especialistas | PLAN/SPEC/TASKS para H3 |
| Implementação | Orchestrator + Engineer | — | diff e gates locais |
| Validação | QA / Validation | Security + Architecture + Code Reviewer | evidence pack |
| Integração | PR Agent | Reviewer Agents | H4 / merge |
| Homologação | Product Validation | Release Agent | release candidate |
| Produção | Release Agent | Observability Agent | H5 / health report |
| Conhecimento | Knowledge Agent | Critic quando sensível | fontes canônicas |
| Melhoria | Telemetry + Auto Dream | Critic Agent | H6, memória ou backlog |

## Por que a crítica é sempre independente

Se você observar a tabela, notará um padrão deliberado: em quase toda fase, quem consolida não é quem critica. Na especificação, o Specification Tech Lead produz e o Adversarial Tech Lead ataca. Na validação, o Engineer implementou antes, e agora QA, Security, Architecture e Code Reviewer procuram o que ele não viu.

Isso não é redundância — é a primeira das três regras do modelo aplicada ao nível do time: **quem propõe não é quem aprova**. Um agente que revisasse o próprio trabalho tenderia a confirmar suas próprias suposições. A independência estrutural, e não a boa-fé do modelo, é o que faz a crítica valer.

## O papel do orquestrador

Em fases com paralelismo, o Orchestrator Agent distribui contexto mínimo e controla dependências — mas há um limite que vale gravar: ele **não substitui** o consolidado do agente primário nem a decisão do owner humano. O orquestrador organiza o trânsito; não decide o destino.

## Como isso vira execução real

Esta página descreve a composição lógica. O **como** ela roda — onde os artefatos são gravados, como um handoff se conclui, o que atravessa a fronteira em cada etapa — é o assunto da próxima seção. Se você quer entender o Agent Team em movimento, siga para [Workflows](../5-workflows/TLDR.md).
