# Assets de sessão

Material bruto que sustenta as análises e discussões de um workflow — transcrições, printscreens, e-mails, PDFs, documentos Word e afins — fica aqui, isolado por execução.

## Convenção

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: nome do workflow ou da skill que gerou o material, por exemplo `00-intake-and-triage` ou `business-discovery`.
- `<session-id>`: identificador curto e único da execução (`mission_id` ou run id). Reexecutar o workflow por resultado insatisfatório cria uma **nova** pasta; a anterior permanece no histórico, mas deixa de ser referenciada pelo artefato vigente.
- Subpastas por tipo (`transcripts/`, `screenshots/`, `emails/`, `documents/`) só quando houver mais de um arquivo do mesmo tipo na sessão.

## Regras

- `plans/assets/` não é fonte canônica. A conclusão, decisão ou requisito extraído vai para `discovery/`, `requirements/`, `strategy/` ou `roadmap/`; o asset fica como rastro auditável, referenciado por caminho.
- Nunca reaproveite a pasta de uma sessão anterior, mesmo que o resultado tenha sido descartado.
- O `STATUS.md` ou o Work Item correspondente indica qual sessão sustenta a versão vigente de um artefato, quando isso não for óbvio.

## Exemplo

```text
plans/assets/business-discovery/2026-08-08-b7e410/
└── transcripts/
    └── agenda-discovery-checkout.md
```

A sessão acima alimentou [`discovery/PB-001-reliable-checkout.md`](../../discovery/PB-001-reliable-checkout.md).
