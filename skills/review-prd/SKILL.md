---
name: review-prd
description: Consolida requisitos e histórias em um PRD com objetivos, regras e critérios de sucesso rastreáveis. Use depois da discovery e do refinamento de produto, antes da especificação técnica.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Consolidar o PRD Plan a partir das histórias escritas e do `requisitos.md`, validando que todos os requisitos estão cobertos.

## Contrato de artefatos

Antes de criar o PRD, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `teamwork/plan/feature-plan-<feature-slug>/historias.md`
- **Obrigatório:** `business-discovery/<feature-slug>/requisitos.md`
- **Opcional:** transcrição da agenda de refinamento (para contexto adicional)

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira dos artefatos.
- Verifique se os arquivos de entrada existem.

### 2. Carregar contexto

- Leia `historias.md` — base para o PRD.
- Leia `requisitos.md` — baseline de requisitos para validação de cobertura.

### 3. Consolidar o PRD

Crie `.agents/prd/<feature-slug>/PRD.md` (crie os diretórios se necessário) no formato:

```markdown
# PRD — <Feature Name>

**Feature:** <slug>
**Status:** 🟡 Em revisão
**Data:** <YYYY-MM-DD>
**Autor:** PM (via review-prd)

---

## 1. Objetivo

<descrição clara do problema de negócio que a feature resolve, extraída do contexto das histórias e requisitos>

## 2. Histórias

| ID | Título | Prioridade | Requisitos |
|----|--------|------------|------------|
| HIST-01 | ... | P1 | RN-XX, US-1 |
| HIST-02 | ... | P2 | RN-YY, US-2 |

### HIST-01: <Título>

<contexto, critérios de aceite, dependências — copiar de historias.md>

## 3. Critérios de Sucesso

| ID | Métrica | Alvo | História |
|----|---------|------|----------|
| SC-01 | ... | ... | HIST-XX |

## 4. Regras de Negócio

| ID | Regra | Exemplo | Cenário |
|----|-------|---------|---------|
| RN-01 | ... | ... | <cenário Gherkin> |

## 5. Fora de Escopo

<itens explicitamente fora de escopo, extraídos de requisitos.md>

## 6. Gaps e Pendências

| ID | Descrição | Status |
|----|-----------|--------|
| DA-01 | ... | ⏳ Aberto |

## 7. Fluxos

### Happy Path
<fluxo principal>

### Exceções
<fluxos de exceção e edge cases>

## 8. Glossário

| Termo | Definição |
|-------|-----------|
| ... | ... |
```

### 4. Validar cobertura

Compare o PRD contra `requisitos.md`:

- Todas as US-X estão vinculadas a pelo menos uma história?
- Todas as RN-XX aparecem no PRD?
- Todos os SC-XX estão vinculados a histórias?
- Gaps/DA-XX foram transferidos?

Liste cobertos e não cobertos.

### 5. Reportar no chat

- Resumo: X histórias consolidadas, Y regras vinculadas, Z SC definidos.
- Lista de requisitos não cobertos (se houver).
- Status do PRD (pronto para revisão / precisa de ajustes).

## Convenções

- PRD segue o formato padrão do time.
- Cada história mantém vínculo rastreável com requisitos (RN, US, SC).
- Status: 🟡 Em revisão → 🟢 Aprovado → ✅ Implementado.
- Português. Gherkin pt-BR para cenários.

## Done When

- [ ] `PRD.md` criado em `.agents/prd/<feature-slug>/`
- [ ] Cobertura validada: todos os requisitos do `requisitos.md` mapeados
- [ ] Gaps/DA-XX transferidos para seção de pendências
- [ ] Resumo reportado no chat
