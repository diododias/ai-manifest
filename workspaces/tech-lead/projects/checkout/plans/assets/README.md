# Assets de sessão

Material de uma execução de workflow — tanto o que o humano traz quanto o que a IA gera no processo — fica aqui, isolado por sessão, nunca solto em `plans/` nem misturado ao artefato final canônico.

## O que vai aqui

| Tipo | Exemplos |
|---|---|
| **Material de entrada** (humano traz) | transcrições de reuniões, e-mails, PDFs, screenshots, documentos Word |
| **Output intermediário da IA** | rascunho do SPEC antes da revisão adversarial, análise exploratória de arquitetura, notas de discovery não consolidadas |

A distinção relevante não é quem gerou, mas se o artefato **já passou pelo gate** do workflow. Antes do gate → `plans/assets/`. Depois do gate → destino canônico (`engineering/`, `product/`, `ux/`, `plans/active/`).

## Convenção

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: nome do workflow ou da skill que gerou o material, por exemplo `03-technical-specification` ou `technical-discovery`.
- `<session-id>`: identificador curto e único da execução (`mission_id` ou run id). Reexecutar o workflow por resultado insatisfatório cria uma **nova** pasta; a anterior permanece no histórico, mas deixa de ser referenciada pelo artefato vigente.
- Subpastas por tipo dentro da pasta da sessão, somente quando houver mais de um arquivo do mesmo tipo:
  - `transcripts/` — transcrições de reuniões ou sessões
  - `drafts/` — rascunhos intermediários gerados pela IA antes do gate
  - `screenshots/` — prints de tela
  - `emails/` — e-mails relevantes
  - `documents/` — PDFs, Word e afins

## Regras

- `plans/assets/` não é fonte canônica. A conclusão, decisão ou requisito extraído vai para `engineering/`, `product/`, `ux/` ou o plano em `plans/active/`; o asset fica como rastro auditável, referenciado por caminho.
- Nunca reaproveite a pasta de uma sessão anterior, mesmo que o resultado tenha sido descartado — isso evita colisão quando o mesmo workflow roda de novo para o mesmo projeto.
- O `STATUS.md` ou o Work Item correspondente indica qual sessão sustenta a versão vigente de um artefato, quando isso não for óbvio pelo link direto.
- Reviews adversariais **não ficam aqui** — são artefatos formais com gate próprio e vão para `execution/reviews/`.

## Exemplo

```text
plans/assets/03-technical-specification/2026-08-08-a1c9f2/
├── transcripts/
│   └── revisao-arquitetura-idempotencia.md   ← reunião trazida pelo humano
└── drafts/
    └── SPEC-001-v0.md                         ← rascunho da IA antes da revisão adversarial
```

Ver [`03-technical-specification/2026-08-08-a1c9f2/`](03-technical-specification/2026-08-08-a1c9f2/README.md) para a sessão que sustenta `plans/active/PLAN-014.md`.
