---
name: dev-flow
description: Guia o fluxo seguro de desenvolvimento de uma tarefa, do planejamento à entrega local e à proposta de publicação. Use quando o usuário pedir coordenação end-to-end de uma implementação, correção ou feature.
---

# Skill: Fluxo de desenvolvimento

Esta skill guia o fluxo padrão ao puxar uma task, do planejamento à entrega
local. Trate criação de issue, commit, push, PR, merge e limpeza de worktree
como ações separadas, executadas apenas quando autorizadas pelo usuário.

## Objetivo

Garantir que cada tarefa siga o fluxo:

1. PLAN
2. TRACKING (se solicitado)
3. IMPLEMENT
4. TEST
5. COMMIT (se autorizado)
6. PROPOR PUBLICAÇÃO
7. PR / MERGE (se autorizado)
8. ENCERRAR COM SEGURANÇA
9. PRÓXIMA TASK

## Uso

Quando iniciar uma task, siga estes passos em ordem e confirme cada etapa antes
de passar à seguinte. A convenção local do repositório prevalece sobre exemplos
de branch, CI ou issue abaixo.

## Segurança e contrato de artefatos

Siga [o contrato compartilhado](../references/workflow-contract.md). Antes de
qualquer efeito externo, apresente o alvo e peça autorização explícita:
criar/editar issue, commit, push, abrir/editar PR, aplicar labels, mergear,
fechar issue ou remover worktree. Nunca descarte, faça stash ou remova mudanças
do usuário para deixar a árvore limpa.

### 1. PLAN
- Leia a task e entenda o escopo, critério de aceitação e restrições.
- Identifique dependências e possíveis impactos nos módulos/backend/storefront.
- Defina o que deve ser feito em um checklist pequeno.
- Escolha/valide o branch name correto se ainda não existir.

### 2. TRACKING (se solicitado)
- Se a demanda já tem issue, use-a como referência.
- Se o usuário pedir rastreamento, proponha uma issue com título e corpo antes de criá-la.
- Use `gh issue create` com título objetivo e corpo contendo:
  - **Contexto**: o "porquê" da demanda.
  - **Escopo**: checklist `- [ ]` com cada entregável (permite fechamento parcial visível).
  - **Critério de aceitação**: como validar.
- Capture o número da issue (`#N`) quando ela existir; não invente nem exija issue para implementar localmente.

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

- Se a task já tem issue, reaproveite-a. Proponha a atribuição de responsável, mas não a edite sem autorização.

### 3. IMPLEMENT
- Escreva o código para resolver o problema de forma simples e clara.
- Prefira mudanças pequenas e incrementalmente aumente o escopo.
- Siga as convenções do repositório e a arquitetura existente.
- Se precisar mexer em backend e frontend, faça commits pequenos e organizados.

### 4. TEST
- Crie ou atualize testes para cobrir a nova funcionalidade ou correção.
- Execute testes locais relevantes (`pnpm test` no package certo ou caso de teste específico).
- Garanta que não há regressão nas áreas afetadas.

### 5. COMMIT (se autorizado)
- Faça commits claros e em português, usando o padrão do repositório:
  - `feat(...)`, `fix(...)`, `chore(...)`, `test(...)`
- O texto do commit deve descrever o que foi alterado.
- Inclua `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>` quando aplicável.
- Referencie a issue no rodapé do commit quando útil: `Refs #N`.

### 6. PROPOR PUBLICAÇÃO
- Resuma o diff, os testes e a branch atual. Proponha o commit e a publicação necessários.
- Não assuma que existe CI automático, branch `develop` ou issue vinculada.

### 7. PR / MERGE (se autorizado)
- Abra ou atualize o PR somente após autorização explícita.
- Descubra a branch-base na configuração do repositório ou no PR; não fixe `develop`.
- **Obrigatório**: o corpo do PR deve conter uma keyword de auto-close apontando para a issue:
  - `Closes #N` — fecha a issue ao mergear o PR (entrega completa).
  - `Refs #N` — referencia sem fechar (entrega parcial; marque manualmente os itens `- [x]` concluídos na issue).
- Explique a mudança, onde testar e quais casos de teste foram executados.
- Marque o PR para revisão.

```bash
gh pr create \
  --base <branch-base-confirmada> \
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

 - Antes de mergear, confirme checks requeridos, aprovações, branch-base e o SHA do PR.
 - Nunca faça push direto para branch protegida; use o mecanismo de merge do PR após autorização.
 - Para entrega parcial, proponha a atualização da issue; não a altere sem autorização.

### 8. ENCERRAR COM SEGURANÇA
- Informe `git status` e deixe mudanças não relacionadas intactas.
- Remova somente artefatos temporários criados nesta tarefa e apenas com autorização.
- Não remova worktree, não faça stash e não descarte alterações como etapa automática.

### 9. PRÓXIMA TASK
- Atualize `TRACKING.md` (status, contagem de testes, NEXT → DONE).
- Verifique se a issue foi fechada (ou parcialmente atualizada).
- Não escolha nem inicie uma nova task sem solicitação do usuário.
- Comece o próximo ciclo de PLANEJAMENTO.

## Resumo rápido

- Planejar primeiro.
- Criar ou atualizar issue somente quando solicitado.
- Implementar com foco mínimo viável.
- Testar antes de commitar.
- Propor commit, PR ou merge com alvo e evidências; executar apenas com autorização.
- Preservar a árvore de trabalho e encerrar reportando seu estado.
