# Business Discovery

Levantamento de requisitos de negócio a partir de agendas com a PM, de forma
**acumulativa**: cada reunião atualiza um documento vivo por feature, em vez de
um resumo solto por transcrição.

## Por que

Como você e a PM já compartilham histórico, a agenda fala só um pedaço da
demanda e referencia coisas sem definir. Transcrição + resumo one-shot fica
raso. Aqui, o contexto das agendas anteriores fica no documento, e as
referências não resolvidas viram lacunas explícitas — não suposições escondidas.

## Fluxo

1. **Antes da agenda** — preencha `templates/roteiro-agenda.md`. Ele força
   explicitar o contexto implícito (o maior ganho de assertividade).
2. **Durante** — grave e siga o roteiro. Peça à PM exemplos concretos das regras
   e que diga "regra de negócio:" antes de cada uma.
3. **Depois** — gere a transcrição e rode a skill:
   `/business-discovery <caminho-da-transcrição>`.
4. **Revise** — confira a seção `⚠️ Gaps detectados` e as `DA-XX`: é a lista de
   perguntas pra levar na próxima agenda.

## Estrutura

```
business-discovery/
  README.md                      este arquivo
  templates/
    roteiro-agenda.md            pauta pra preparar a agenda
    requisitos.md                formato do documento de saída (em branco)
    exemplo-preenchido.md        referência preenchida (fake)
  <feature-slug>/
    requisitos.md                documento vivo, atualizado a cada agenda
```

A skill que orquestra isso vive em `.claude/skills/business-discovery/`.

## Convenções

- `RN-XX` regras de negócio · `US-X` user stories (prioridade P1/P2/P3) ·
  `SC-XX` critérios de sucesso mensuráveis · `DA-X` dúvidas em aberto.
- Regras (RN) estruturadas (pré-condição + gatilho + resposta +
  "o sistema **deve**"); cenários de aceite em Gherkin pt-BR: **Dado / Quando / Então**.
- Status: 🟡 em descoberta · 🟢 pronto pra especificar · ✅ virou spec.
- Changelog do `requisitos.md` é **append-only** — preserva o histórico de como
  o entendimento evoluiu entre agendas.
- O formato espelha o PRD produzido pela skill `review-prd` (ver "Handoff pra
  review-prd e create-spec" no SKILL.md) — a feature 🟢 alimenta `/review-prd`
  e depois `/create-spec` direto.
