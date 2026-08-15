---
name: "test-integration-local"
description: "Cria cobertura faltante e executa validação local com evidências rastreáveis. Use após implementar uma feature ou correção, quando for necessário mapear critérios de aceite a testes e relatar resultados."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Executar validação completa do código implementado — testes unitários, mutação, cobertura — e gerar evidências de que os critérios de aceite são atendidos.

## Contrato de artefatos

Antes de escrever evidências, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** código implementado (repositório local)
- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md` (critérios de aceite)
- **Obrigatório:** `teamwork/plan/feature-plan-<feature-slug>/plano-implementacao.md`
- **Opcional:** `teamwork/plan/feature-plan-<feature-slug>/tracking.md`

## Execution Steps

### 1. Identificar escopo de testes

- Leia a SPEC para extrair critérios de aceite técnicos (CT-XX).
- Leia o plano de implementação para identificar blocos implementados.
- Identifique arquivos modificados/criados.

### 2. Gerar casos de teste

Para cada critério de aceite técnico (CT-XX) sem cobertura:

- Crie teste unitário que valida o critério.
- Siga padrão de testes existente no repositório.
- Nomeie seguindo convenção do projeto.

Para fluxos de exceção:
- Teste caminhos de erro documentados na SPEC.
- Teste validações, limites e edge cases.

### 3. Executar testes unitários

```bash
# Detectar e executar testes do projeto
# Exemplos por ecossistema:
# Node.js: npm test / pnpm test / yarn test
# Python: pytest / python -m pytest
# Go: go test ./...
# Rust: cargo test
```

- Execute todos os testes, não apenas os novos.
- Verifique se há regressões.

### 4. Verificar cobertura (se disponível)

```bash
# Exemplos:
# Node.js: npx jest --coverage
# Python: pytest --cov
# Go: go test -cover ./...
# Rust: cargo tarpaulin
```

- Verifique se os arquivos modificados têm cobertura adequada.
- Identifique linhas/branches sem teste.

### 5. Testes de mutação (se disponível)

```bash
# Exemplos:
# Node.js: npx Stryker run
# Python: mutmut run
```

- Valide que testes realmente testam (não apenas passam).
- Corrija testes que não matam mutações.

### 6. Self-check dos critérios de aceite

Para cada CT (critério técnico) e seu CA de negócio relacionado, quando houver:

| CT | CA relacionado | Critério | Status | Evidência |
|----|---------------|----------|--------|-----------|
| CT-01 | CA-01 | <descrição> | ✅ / ❌ | <teste que valida> |
| CT-02 | CA-02 | <descrição> | ✅ / ❌ | <teste que valida> |

### 7. Gerar evidências

Crie `teamwork/plan/feature-plan-<feature-slug>/evidencias-teste.md`:

```markdown
# Evidências de Teste — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>

---

## Resultado dos Testes

### Unitários
- **Comando:** `<comando executado>`
- **Resultado:** ✅ X passando / ❌ Y falhando
- **Cobertura:** XX%

### Mutação (se aplicável)
- **Comando:** `<comando executado>`
- **Score:** XX% (X matados / Y total)

### Regressão
- **Testes existentes:** ✅ Todos passando / ❌ Falhas

---

## Cobertura por Critério de Aceite

| CT | CA relacionado | Critério | Teste | Status |
|----|---------------|----------|-------|--------|
| CT-01 | CA-01 | ... | teste_nome | ✅ |
| CT-02 | CA-02 | ... | teste_nome | ✅ |

---

## Arquivos Modificados e Cobertos

| Arquivo | Linhas | Cobertura |
|---------|--------|-----------|
| ... | ... | XX% |

---

## Pendências

- <testes que não foi possível executar>
- <cobertura faltante justificada>
```

### 8. Reportar no chat

- Resumo: X testes passando, Y falhando, Z cobertura.
- Critérios de aceite atendidos vs pendentes.
- Pronto para code review ou precisa de ajustes.

## Convenções

- Testes seguem padrão do repositório.
- Evidências são persistentes — ficam no repositório.
- Self-check é obrigatório antes de abrir PR.
- Português para documentação, inglês para código de teste.

## Done When

- [ ] Testes unitários executados e passando
- [ ] Cobertura verificada (se ferramenta disponível)
- [ ] Critérios de aceite self-checked com evidências
- [ ] `evidencias-teste.md` gerado
- [ ] Regressão verificada (testes existentes passando)
- [ ] Resultado reportado no chat
