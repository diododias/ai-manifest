# Assets de sessão

Material bruto que sustenta as análises e discussões de um workflow — transcrições, printscreens, e-mails, PDFs, documentos Word e afins — fica aqui, isolado por execução, nunca solto em `plans/` nem misturado ao plano final.

## Convenção

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: nome do workflow ou da skill que gerou o material, por exemplo `03-technical-specification` ou `technical-discovery`.
- `<session-id>`: identificador curto e único da execução (`mission_id` ou run id). Reexecutar o workflow por resultado insatisfatório cria uma **nova** pasta; a anterior permanece no histórico, mas deixa de ser referenciada pelo artefato vigente.
- Subpastas por tipo (`transcripts/`, `screenshots/`, `emails/`, `documents/`) só quando houver mais de um arquivo do mesmo tipo na sessão.

## Regras

- `plans/assets/` não é fonte canônica. A conclusão, decisão ou requisito extraído vai para `engineering/`, `product/`, `ux/` ou o plano em `plans/active/`; o asset fica como rastro auditável, referenciado por caminho.
- Nunca reaproveite a pasta de uma sessão anterior, mesmo que o resultado tenha sido descartado — isso evita colisão quando o mesmo workflow roda de novo para o mesmo projeto.
- O `STATUS.md` ou o Work Item correspondente indica qual sessão sustenta a versão vigente de um artefato, quando isso não for óbvio pelo link direto.

## Exemplo

```text
plans/assets/03-technical-specification/2026-08-08-a1c9f2/
└── transcripts/
    └── revisao-arquitetura-idempotencia.md
```

Ver [`03-technical-specification/2026-08-08-a1c9f2/`](03-technical-specification/2026-08-08-a1c9f2/README.md) para a sessão que sustenta `plans/active/PLAN-014.md`.
