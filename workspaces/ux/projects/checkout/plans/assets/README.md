# Assets de sessão

Material bruto que sustenta as análises e discussões de um workflow — transcrições, printscreens, e-mails, PDFs, documentos Word e afins — fica aqui, isolado por execução.

## Convenção

```text
plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/
```

- `<workflow>`: nome do workflow ou da skill que gerou o material, por exemplo `01-discovery-and-research` ou uma sessão de pesquisa com usuários.
- `<session-id>`: identificador curto e único da execução (`mission_id` ou run id). Reexecutar o workflow por resultado insatisfatório cria uma **nova** pasta; a anterior permanece no histórico, mas deixa de ser referenciada pelo artefato vigente.
- Subpastas por tipo (`transcripts/`, `screenshots/`, `emails/`, `documents/`) só quando houver mais de um arquivo do mesmo tipo na sessão.

## Regras

- `plans/assets/` não é fonte canônica. A conclusão, decisão ou requisito extraído vai para `research/`, `journeys/`, `flows/` ou `specifications/`; o asset fica como rastro auditável, referenciado por caminho.
- Proteja consentimento, privacidade e anonimização de participantes ao arquivar transcrições e gravações de pesquisa.
- Nunca reaproveite a pasta de uma sessão anterior, mesmo que o resultado tenha sido descartado.

## Exemplo

```text
plans/assets/01-discovery-and-research/2026-08-08-c3d821/
└── transcripts/
    └── entrevista-usuario-retencao-pagamento.md
```

A sessão acima alimentou [`research/evidence-summary.md`](../../research/evidence-summary.md).
