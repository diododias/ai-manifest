---
name: review-spec
description: Revisa uma SPEC contra o PRD para encontrar lacunas, ambiguidades, inconsistências e riscos de implementação. Use antes de aprovar a SPEC ou iniciar o plano de execução.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Analisar a SPEC em busca de gaps, ambiguidades e inconsistências internas, gerando relatório de pontos a resolver classificados por severidade.

## Contrato de artefatos

Resolva PRD e SPEC conforme [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`
- **Obrigatório:** `.agents/prd/<feature-slug>/PRD.md`

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira dos artefatos.
- Verifique se os arquivos de entrada existem.

### 2. Carregar artefatos

- Leia `SPEC.md` — análise principal.
- Leia `PRD.md` — referência para validação de cobertura.

### 3. Análise da SPEC

Verifique sistematicamente:

#### A. Cobertura do PRD
- Cada história do PRD tem solução técnica na SPEC?
- Cada regra de negócio (RN-XX) é tratada?
- Cada critério de sucesso (SC-XX) tem equivalente técnico?

#### B. Consistência Interna
- Terminologia consistente (mesmo conceito nomeado igual)?
- Modelo de dados coerente com os fluxos?
- Contratos de interface alinhados com o modelo?

#### C. Completude
- Histórias sem critérios de aceite técnicos?
- Componentes sem definição clara?
- Fluxos de exceção não tratados?

#### D. Ambiguidade
- Termos vagos ("rápido", "escalável") sem métrica?
- Placeholder não resolvido (TODO, TKTK)?
- Decisões técnicas pendentes?

#### E. Viabilidade
- Dependências externas identificadas?
- Riscos técnicos documentados?
- Estimate de esforço realista?

### 4. Classificar por severidade

- **CRITICAL:** Bloqueia implementação (história sem solução, contrato inválido)
- **HIGH:** Impacta qualidade (exceção não tratada, teste não definido)
- **MEDIUM:** Pode causar retrabalho (ambiguidade, terminologia inconsistente)
- **LOW:** Melhoria de qualidade (documentação, exemplos)

### 5. Gerar relatório

Gere `teamwork/plan/feature-plan-<feature-slug>/review-spec.md`:

```markdown
# Review da SPEC — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>
**SPEC:** .agents/spec/<feature-slug>/SPEC.md

---

## Resumo

| Severidade | Quantidade |
|------------|-----------|
| 🔴 CRITICAL | X |
| 🟠 HIGH | X |
| 🟡 MEDIUM | X |
| 🔵 LOW | X |

**Status:** 🔴 Bloqueado / 🟡 Ajustes necessários / 🟢 Aprovado

---

## Achados

### 🔴 CRITICAL

#### C-01: <Título>
- **Local:** SPEC §<seção>
- **Problema:** <descrição>
- **Recomendação:** <como resolver>

### 🟠 HIGH

#### H-01: <Título>
...

### 🟡 MEDIUM

#### M-01: <Título>
...

### 🔵 LOW

#### L-01: <Título>
...

---

## Cobertura PRD → SPEC

| História PRD | Na SPEC? | Observação |
|-------------|----------|------------|
| HIST-01 | ✅ / ❌ | ... |

## Próximos Passos

- <ações para resolver CRITICAL>
- <ações para resolver HIGH>
- <recomendações gerais>
```

### 6. Reportar no chat

- Resumo: X achados (Y críticos, Z alto).
- Bloqueios que precisam de resolução antes de avançar.
- Status geral (bloqueado / ajustes / aprovado).

## Convenções

- Relatório é read-only — não modifica a SPEC.
- Classificação por severidade é subjetiva mas deve ser consistente.
- Português.

## Done When

- [ ] `review-spec.md` gerado em `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] Todos os achados classificados por severidade
- [ ] Cobertura PRD → SPEC documentada
- [ ] Status e próximos passos reportados
