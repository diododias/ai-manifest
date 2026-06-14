# Skill: Fluxo de desenvolvimento

Esta skill guia o fluxo padrão ao puxar uma task, do planejamento até a próxima tarefa.

## Objetivo

Garantir que cada tarefa siga o fluxo:

1. PLAN
2. CREATE ISSUE
3. IMPLEMENT
4. TEST
5. COMMIT
6. OPEN PR (linkado à issue)
7. MERGE & AUTO-CLOSE
8. CLEAN WORKTREE
9. NEXT TASK

## Uso

Quando você iniciar uma task, siga estes passos em ordem e confirme cada etapa antes de passar à seguinte.

### 1. PLAN
- Leia a task e entenda o escopo, critério de aceitação e restrições.
- Identifique dependências e possíveis impactos nos módulos/backend/storefront.
- Defina o que deve ser feito em um checklist pequeno.
- Escolha/valide o branch name correto se ainda não existir.

### 2. CREATE ISSUE
- Toda demanda deve ter uma issue no GitHub para rastreio. Crie antes de implementar.
- Use `gh issue create` com título objetivo e corpo contendo:
  - **Contexto**: o "porquê" da demanda.
  - **Escopo**: checklist `- [ ]` com cada entregável (permite fechamento parcial visível).
  - **Critério de aceitação**: como validar.
- Capture o número da issue (`#N`) — será referenciado no PR.

```bash
gh issue create \
  --title "feat(escopo): descrição curta" \
  --body "$(cat <<'EOF'
## Contexto
<por que>

## Escopo
- [ ] item 1
- [ ] item 2

## Critério de aceitação
- ...
EOF
)"
```

- Se a task já tem issue, reaproveite e marque-se como assignee: `gh issue edit <N> --add-assignee @me`.

### 3. IMPLEMENT
- Escreva o código para resolver o problema de forma simples e clara.
- Prefira mudanças pequenas e incrementalmente aumente o escopo.
- Siga as convenções do repositório e a arquitetura existente.
- Se precisar mexer em backend e frontend, faça commits pequenos e organizados.

### 4. TEST
- Crie ou atualize testes para cobrir a nova funcionalidade ou correção.
- Execute testes locais relevantes (`pnpm test` no package certo ou caso de teste específico).
- Garanta que não há regressão nas áreas afetadas.

### 5. COMMIT
- Faça commits claros e em português, usando o padrão do repositório:
  - `feat(...)`, `fix(...)`, `chore(...)`, `test(...)`
- O texto do commit deve descrever o que foi alterado.
- Inclua `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>` quando aplicável.
- Referencie a issue no rodapé do commit quando útil: `Refs #N`.

### 6. OPEN PR (linkado à issue)
- Abra o PR com título e descrição objetivos.
- **Obrigatório**: o corpo do PR deve conter uma keyword de auto-close apontando para a issue:
  - `Closes #N` — fecha a issue ao mergear o PR (entrega completa).
  - `Refs #N` — referencia sem fechar (entrega parcial; marque manualmente os itens `- [x]` concluídos na issue).
- Explique a mudança, onde testar e quais casos de teste foram executados.
- Marque o PR para revisão.

```bash
gh pr create \
  --base develop \
  --title "feat(escopo): descrição" \
  --body "$(cat <<'EOF'
## Resumo
<o que mudou e por quê>

## Como testar
- ...

Closes #N
EOF
)"
```

### 7. MERGE & AUTO-CLOSE
- Após aprovação, mergeie o PR no `develop`:
  - Via CLI: `gh pr merge <num> --squash --delete-branch`.
  - Ou via merge local (fluxo padrão do projeto) seguido de `git push origin develop`.
- Com `Closes #N` no corpo, o GitHub fecha a issue automaticamente quando o PR é mergeado na branch padrão. Para PRs mergeados em `develop` (não-default), feche manualmente: `gh issue close N --comment "Entregue via PR #<pr-num>."`.
- Entrega parcial: marque os checkboxes `- [x]` na issue (`gh issue edit N --body ...`) e mantenha aberta para o restante.

### 8. CLEAN WORKTREE
- Antes de encerrar, garanta que `git status` está limpo.
- Remova artefatos temporários, arquivos de build locais ou testes quebrados.
- Remova a worktree: `ExitWorktree action: remove` ou `git worktree remove <path>`.
- Se houver algo pendente, commit/descartar/stash antes de mudar de task.

### 9. NEXT TASK
- Atualize `TRACKING.md` (status, contagem de testes, NEXT → DONE).
- Verifique se a issue foi fechada (ou parcialmente atualizada).
- Escolha a próxima task prioritária somente com a árvore de trabalho limpa.
- Comece o próximo ciclo de PLANEJAMENTO.

## Automação

- **Auto-close de issue ao mergear PR**: garantido pela keyword `Closes #N` / `Fixes #N` / `Resolves #N` no corpo do PR. Funciona nativo no GitHub quando o PR vai para a branch default. Para branches não-default (ex: `develop`), o fechamento exige `gh issue close` manual ou um workflow.
- **Workflow opcional** para fechar issues em merges em qualquer branch — criar `.github/workflows/close-linked-issues.yml`:

```yaml
name: close-linked-issues
on:
  pull_request:
    types: [closed]
jobs:
  close:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            const body = context.payload.pull_request.body || "";
            const re = /(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)/gi;
            const nums = [...body.matchAll(re)].map(m => Number(m[1]));
            for (const n of nums) {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: n,
                state: "closed",
              });
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: n,
                body: `Fechada pelo merge do PR #${context.payload.pull_request.number}.`,
              });
            }
```

- **Template de issue** (opcional): criar `.github/ISSUE_TEMPLATE/task.md` com os campos Contexto / Escopo / Critério de aceitação para padronizar.

## Resumo rápido

- Planejar primeiro.
- Abrir issue antes de implementar (rastreio obrigatório).
- Implementar com foco mínimo viável.
- Testar antes de commitar.
- PR sempre com `Closes #N` (ou `Refs #N` se parcial).
- Mergear → issue fecha sozinha (ou manualmente em branch não-default).
- Worktree limpa, próxima task.
