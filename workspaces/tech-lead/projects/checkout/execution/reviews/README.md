# Reviews

Registre aqui os pareceres de revisão gerados durante a validação adversarial — tanto da especificação quanto da implementação. O estado `review` do Work Item só termina quando todas as pendências estiverem resolvidas.

## Convenção de nomenclatura

```text
execution/reviews/<tipo>-<id>.md
```

| Tipo | Quando criar | Exemplo |
|---|---|---|
| `spec-<SPEC-id>` | Adversarial TL review da especificação (Rodada C) | `spec-SPEC-001.md` |
| `code-<WI-id>` | Code Reviewer na validação adversarial (Rodada E) | `code-WI-031.md` |
| `security-<WI-id>` | Security Review Agent (Rodada E) | `security-WI-031.md` |
| `architecture-<WI-id>` | Architecture Review Agent (Rodada E) | `architecture-WI-031.md` |
| `qa-<WI-id>` | QA/Validation Agent — evidence pack consolidado (Rodada E) | `qa-WI-031.md` |

## Estrutura mínima de um arquivo de review

```markdown
---
type: <spec|code|security|architecture|qa>
ref: <SPEC-id ou WI-id>
reviewer: <nome do agente>
status: <open|resolved|exception>
date: <YYYY-MM-DD>
---

## Achados

| # | Severidade | Descrição | Ação | Resolução |
|---|---|---|---|---|

## Recomendação de gate

<aprovado / volta para implementação / exceção para Tech Lead>
```

## Regras

- Cada agente grava seu próprio arquivo; o QA Agent consolida o evidence pack em `execution/evidence/<WI-id>.md`.
- Um achado aberto bloqueia o gate. Resolução exige evidência referenciada, não apenas texto.
- Reviews de spec ficam aqui mesmo após a especificação ser aprovada — são rastro auditável da iteração.
