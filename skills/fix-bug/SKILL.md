---
name: "fix-bug"
description: "Corrige um bug documentado com teste de regressão e validação local. Use quando houver evidência ou análise de bug e o usuário pedir a implementação da correção; commit e PR exigem pedido de publicação."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Implementar a correção do bug seguindo o fluxo padrão (implement → test → commit → PR), garantindo cobertura por teste.

## Inputs

- **Obrigatório:** `bugs/bug-<NOME-SLUG>.md` (análise do bug)
- **Obrigatório:** código afetado (repositório local)

## Execution Steps

### 1. Carregar análise

- Leia `bug-<NOME>.md` — causa raiz e componente afetado.
- Identifique arquivos que precisam ser modificados.

### 2. Verificar se há teste que reproduz o bug

- Execute os testes existentes para o componente afetado.
- Verifique se algum teste já cobre o cenário (e está falhando ou passando incorretamente).
- Se não há teste que reproduza, crie um antes de corrigir (TDD).

### 3. Criar teste de regressão

Crie teste que:
- Reproduz o bug (deve falhar com o código atual).
- Valida o comportamento correto (deve passar após a correção).
- Segue padrão de testes do repositório.

### 4. Implementar a correção

- Siga a direção sugerida na análise (ou ajuste se necessário).
- Mudanças mínimas e focadas — não refatore desnecessariamente.
- Siga convenções do repositório.

### 5. Validar

- Execute o teste de regressão — deve passar.
- Execute todos os testes do componente — não deve haver regressão.
- Verifique se o bug original está resolvido.

### 6. Propor publicação

Após a correção estar validada, informe os passos de publicação:

1. **Commit** — use `/commit` com mensagem `fix(<escopo>): <descrição>` + `Refs #<issue>` se o usuário pedir um commit.
2. **PR** — use `/update-pr` ou proponha um novo PR somente se o usuário pedir publicação.

### 7. Atualizar análise do bug

Atualize `bugs/bug-<NOME>.md`:
- Status: 🟡 Analisado → ✅ Corrigido
- Adicione data de correção
- Referencie o PR/commit

### 8. Reportar no chat

- Resumo: bug corrigido, causa raiz, mudança realizada.
- Teste de regressão criado.
- PR/commit referenciado.
- Se a correção é parcial ou precisa de follow-up.

## Convenções

- Sempre crie teste antes de corrigir (ou confirme que existe).
- Correções são mínimas — não refatore durante o fix.
- Commit segue padrão `fix(...)`.
- Se o bug tem issue, referencie no commit e PR.
- Português.

## Done When

- [ ] Análise do bug carregada
- [ ] Teste de regressão criado (ou existente validado)
- [ ] Correção implementada e validada
- [ ] Testes executados sem regressão
- [ ] Próximo passo de publicação informado
- [ ] Análise do bug atualizada com status ✅
- [ ] Resultado reportado no chat
