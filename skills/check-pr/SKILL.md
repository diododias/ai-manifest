---
name: "check-pr"
description: "Consulta, sem modificar, o estado de um pull request, suas revisões, threads resolvidas e checks. Use quando o usuário pedir status, pendências ou bloqueios de um PR aberto."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Verificar o status atual da revisão do PR, identificar pendências e resumir o que precisa ser feito.

## Inputs

- **Obrigatório:** PR aberto (número ou branch)

## Execution Steps

### 1. Localizar o PR

- Se `$ARGUMENTS` contém número, use-o.
- Caso contrário, encontre o PR da branch atual:
  ```bash
  gh pr list --head <branch-name> --json number,title,state
  ```

### 2. Coletar informações do PR

```bash
# Status geral
gh pr view <number> --json state,reviewDecision,mergedAt,closedAt,isDraft

# Reviews
gh pr view <number> --json reviews --jq '.reviews[] | {author: .author.login, state: .state, body: .body}'

# Repositório das threads
OWNER=$(gh repo view --json owner --jq '.owner.login')
REPO=$(gh repo view --json name --jq '.name')

# Threads inline (inclui caminho, linha e resolução)
gh api graphql -f query='query($owner:String!, $repo:String!, $number:Int!) { repository(owner:$owner, name:$repo) { pullRequest(number:$number) { reviewThreads(first:100) { nodes { isResolved comments(first:100) { nodes { author { login } body path line } } } } } } }' -f owner="$OWNER" -f repo="$REPO" -F number=<number>

# Check CI
gh pr checks <number>
```

### 3. Analisar status

#### Reviews
| Revisor | Status | Ação |
|---------|--------|------|
| reviewer1 | ✅ APPROVED | — |
| reviewer2 | 🔄 CHANGES_REQUESTED | Verificar comentários |
| reviewer3 | ⏳ PENDING | Aguardando |

#### Comentários não resolvidos
| Comentário | Arquivo | Linha | Resolvido? |
|-----------|---------|-------|------------|
| ... | ... | ... | ✅ / ❌ |

#### CI/CD
| Check | Status |
|-------|--------|
| build | ✅ / ❌ |
| test | ✅ / ❌ |
| lint | ✅ / ❌ |

### 4. Identificar pendências

- Threads inline não resolvidas; não infira resolução a partir de comentários gerais.
- Checks CI falhando.
- Draft status (se aplicável).
- Merge blockers (proteção de branch, approvals faltando).

### 5. Gerar resumo

```markdown
# Status do PR #<number> — <Título>

**Branch:** <branch>
**Estado:** Open / Draft / Approved / Changes Requested

---

## Reviews

| Revisor | Status | Data |
|---------|--------|------|
| ... | ... | ... |

## Pendências

### Comentários a Resolver
- [ ] <comentário 1> — <arquivo>:<linha>
- [ ] <comentário 2> — <arquivo>:<linha>

### CI/CD
- [ ] <check que falhou> — <erro>

### Aprovações
- ✅ X de Y aprovações necessárias

## Próximos Passos

1. <ação 1>
2. <ação 2>
```

### 6. Reportar no chat

- Resumo: status geral, aprovações, pendências.
- Comentários que precisam de ação.
- Checks CI que estão falhando.
- Estimativa de pronto para merge.

## Convenções

- Não modifique o PR — apenas leitura.
- Status é snapshot no momento da consulta.
- Português.

## Done When

- [ ] Status do PR verificado (reviews, comments, CI)
- [ ] Pendências identificadas e listadas
- [ ] Resumo de próximos passos gerado
- [ ] Status reportado no chat
