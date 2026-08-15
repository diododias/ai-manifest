---
name: "code-review"
description: "Revisa mudanças de código contra SPEC, testes e riscos, produzindo achados acionáveis sem modificar o código. Use antes de revisão humana ou quando o usuário pedir uma revisão técnica de uma feature ou PR."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Revisar o código de forma adversarial antes de chegar a revisores humanos, verificando conformidade com a SPEC, qualidade e cobertura de testes.

## Contrato de artefatos

Resolva artefatos conforme [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`
- **Obrigatório:** código implementado (diff da branch)
- **Obrigatório:** testes executados
- **Opcional:** descrição do PR (se já existe)

## Execution Steps

### 1. Coletar contexto

- Leia a SPEC — requisitos técnicos e critérios de aceite.
- Descubra a base do PR (`gh pr view --json baseRefName`) ou a branch configurada no repositório; então use `git diff <base>...HEAD`. Não presuma `main` ou `develop`.
- Leia testes criados/modificados.

### 2. Revisão em camadas

#### A. Conformidade com SPEC
Para cada bloco implementado:
- O código implementa o que a SPEC define?
- Critérios de aceite técnicos (CT-XX) são atendidos?
- Modelo de dados está correto?
- Contratos de interface batem com a SPEC?

#### B. Qualidade do Código
- Código segue convenções do repositório?
- Funções/métodos são claros e bem nomeados?
- Não há code duplication desnecessária?
- Tratamento de erros adequado?
- Edge cases tratados?

#### C. Segurança
- Input validation presente?
- Secrets/credenciais hardcoded?
- SQL injection, XSS, CSRF?
- Aut autorização/autenticação adequada?

#### D. Performance
- Queries N+1?
- Operações bloqueantes?
- Cache adequado?
- Memória/loop infinitos potenciais?

#### E. Testes
- Todos os CT-XX têm teste?
- Testes são significativos (não apenas passam)?
- Edge cases testados?
- Mocks/stubs adequados?

### 3. Classificar achados

- **BLOCKER:** Deve ser corrigido antes do PR (bug, security, SPEC violation)
- **REVIEW:** Revisores devem verificar (design, padrão, performance)
- **SUGGESTION:** Melhoria opcional (refactoring, otimização)
- **PRAISE:** Código bem escrito (reforço positivo)

### 4. Gerar relatório

Gere `teamwork/plan/feature-plan-<feature-slug>/code-review.md`:

```markdown
# Code Review — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>
**Branch:** <nome da branch>
**Commits:** <quantidade>

---

## Resumo

| Categoria | Quantidade |
|-----------|-----------|
| 🔴 BLOCKER | X |
| 🟠 REVIEW | X |
| 🟡 SUGGESTION | X |
| 🟢 PRAISE | X |

**Recomendação:** ✅ Aprovar / 🔄 Revisar / ❌ Rejeitar

---

## Conformidade com SPEC

| Bloco | CT-XX | Status | Observação |
|-------|-------|--------|------------|
| ... | CT-01 | ✅ / ⚠️ / ❌ | ... |

---

## Achados

### 🔴 BLOCKER

#### B-01: <Título>
- **Arquivo:** `caminho/linha`
- **Problema:** <descrição>
- **Sugestão:** <como corrigir>

### 🟠 REVIEW

#### R-01: <Título>
...

### 🟡 SUGGESTION

#### S-01: <Título>
...

### 🟢 PRAISE

#### P-01: <Título>
<o que está bem e por quê>

---

## Cobertura de Testes

| CT-XX | Critério | Teste | Status |
|-------|----------|-------|--------|
| CT-01 | ... | ... | ✅ / ❌ |

---

## Material de Homologação

<se solicitado, gere material seguindo template do time>

### Resumo da Mudança
<o que mudou e por quê>

### Como Testar
<passos de validação>

### Impacto
<áreas afetadas, riscos>

---

## Recomendação Final

<justificativa da recomendação>
```

### 5. Reportar no chat

- Resumo: X blockers, Y review, Z sugestões.
- Recomendação: aprovar, revisar ou rejeitar.
- Bloqueios que precisam de resolução.

## Convenções

- Revisão é adversarial — tente encontrar problemas.
- Nunca silencie blockers — sempre reporte.
- Praise é importante — reforça boas práticas.
- Português para documentação.
- Material de homologação segue template do time quando solicitado.

## Done When

- [ ] Revisão em todas as camadas executada
- [ ] Conformidade com SPEC verificada
- [ ] Achados classificados (BLOCKER/REVIEW/SUGGESTION/PRAISE)
- [ ] `code-review.md` gerado
- [ ] Recomendação de aprovação/revisão/rejeição reportada
