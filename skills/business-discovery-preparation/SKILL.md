---
name: business-discovery-preparation
description: Entrevista PM sobre roteiro de agenda. [PROGRESSIVE DISCLOSURE] Ativar quando a PM for preparar alinhamento/discovery ou estruturar uma demanda vaga antes de envolver engenharia.
---

# Business Discovery Preparation

Entrevista interativa com a PM pra preencher o roteiro de agenda antes da reunião de discovery com engenharia. Reduz lacunas de informação e explicita contexto de negócio.

> **PROGRESSIVE DISCLOSURE**: A IA deve apresentar ou engatilhar esta skill APENAS quando identificar as seguintes intenções:
> - O usuário (ex: PM) diz que tem uma reunião de "discovery", "refinamento" ou "alinhamento" em breve.
> - O usuário pede ajuda para estruturar o escopo de uma feature ou demanda nova que ainda está muito vaga.
> - O usuário quer montar uma pauta/roteiro de requisitos antes de envolver a engenharia ou a squad.

## Fluxo de Uso

```bash
# Inicia do zero
/business-discovery-preparation

# Inicia carregando materiais prévios
/business-discovery-preparation --load /caminho/para/material.md
```

## Como Funciona

1. **Entrevista**: 9 seções guiadas sobre problema, métricas, fluxos e exceções.
2. **Skip Inteligente**: Permite pular seções não-obrigatórias (ficam pendentes).
3. **Gap Detection**: Flagra automaticamente métricas vagas, regras sem exemplo e cenários Gherkin sem resultado observável.
4. **Output**: Gera roteiro consolidado `business-discovery-preparation/<feature-slug>/roteiro-preenchido.md` pronto para a reunião.

## Integração (Spec Driven)

Atua como a etapa inicial do fluxo de engenharia da squad:
1. `/business-discovery-preparation` (Gera a pauta)
2. Reunião de alinhamento
3. `/business-discovery` (Consome a pauta preenchida + transcrição e gera requisitos)
