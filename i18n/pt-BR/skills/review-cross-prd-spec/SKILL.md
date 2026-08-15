---
name: review-cross-prd-spec
description: Compara PRD e SPEC, identificando cobertura, conflitos e decisões pendentes sem alterar os artefatos. Use antes do planejamento de sprint ou quando for necessário comprovar o alinhamento entre negócio e solução técnica.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Validar alinhamento entre PRD e SPEC, identificando requisitos do PRD não cobertos na SPEC e conflitos entre os dois artefatos.

## Contrato de artefatos

Resolva PRD e SPEC conforme [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `.agents/prd/<feature-slug>/PRD.md`
- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira dos artefatos.
- Verifique se os arquivos de entrada existem.

### 2. Carregar artefatos

- Leia `PRD.md` — perspectiva de negócio.
- Leia `SPEC.md` — perspectiva técnica.

### 3. Revisão cruzada

#### A. Cobertura PRD → SPEC
Para cada elemento do PRD, verifique se existe correspondente na SPEC:

| Elemento PRD | Tipo | Na SPEC? | Observação |
|-------------|------|----------|------------|
| HIST-01 | História | ✅ / ❌ / ⚠️ Parcial | ... |
| RN-01 | Regra | ✅ / ❌ | ... |
| SC-01 | Critério Sucesso | ✅ / ❌ | ... |

#### B. Conflitos PRD ↔ SPEC
Identifique onde PRD e SPEC divergem:

- **Escopo:** SPEC implementa algo fora do PRD? PRD pede algo não tratado na SPEC?
- **Comportamento:** SPEC define comportamento diferente do que o PRD descreve?
- **Dados:** Modelo de dados da SPEC suporta todos os fluxos do PRD?
- **Performance:** Requisitos não-funcionais do PRD são endereçados na SPEC?

#### C. Alinhamento de Terminologia
- Mesmos termos usados nos dois documentos?
- Significado consistente?

#### D. Decisões Técnicas vs Requisitos de Negócio
- A SPEC não deve alterar requisitos de negócio (só pode refinar como implementar).
- Se a SPEC "muda" um requisito, é conflito — reportar.

### 4. Gerar relatório

Gere `teamwork/plan/feature-plan-<feature-slug>/review-cross.md`:

```markdown
# Revisão Cruzada PRD ↔ SPEC — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>
**PRD:** .agents/prd/<feature-slug>/PRD.md
**SPEC:** .agents/spec/<feature-slug>/SPEC.md

---

## Resumo

| Categoria | Quantidade |
|-----------|-----------|
| ✅ Alinhados | X |
| ⚠️ Parcialmente cobertos | X |
| ❌ Não cobertos (PRD → SPEC) | X |
| 🔴 Conflitos | X |

**Status:** 🔴 Conflitos encontrados / 🟡 Ajustes necessários / 🟢 Alinhado

---

## Cobertura PRD → SPEC

### Histórias
| PRD | SPEC | Status | Observação |
|-----|------|--------|------------|
| HIST-01 | §4.1 | ✅ / ⚠️ / ❌ | ... |

### Regras de Negócio
| RN | Status | SPEC ref | Observação |
|----|--------|----------|------------|
| RN-01 | ✅ / ❌ | §... | ... |

### Critérios de Sucesso
| SC | Status | SPEC ref | Observação |
|----|--------|----------|------------|
| SC-01 | ✅ / ❌ | §... | ... |

---

## Conflitos Detectados

### CONFLITO-01: <Título>
- **PRD diz:** <citação do PRD>
- **SPEC diz:** <citação da SPEC>
- **Tipo:** Escopo / Comportamento / Dados / Performance
- **Recomendação:** <como resolver>

---

## Pontos de Alinhamento

- <pontos onde PRD e SPEC estão bem alinhados>

## Recomendações

1. <ação recomendada>
2. <ação recomendada>

## Próximos Passos

- Resolver conflitos antes do sprint planning
- Atualizar artefatos conforme resoluções
```

### 5. Reportar no chat

- Resumo: X alinhados, Y parcialmente cobertos, Z não cobertos, W conflitos.
- Conflitos que bloqueiam sprint planning.
- Recomendações prioritárias.

## Convenções

- Relatório é read-only — não modifica PRD nem SPEC.
- Conflitos são sempre reportados — nunca resolvidos silenciosamente.
- Português.

## Done When

- [ ] `review-cross.md` gerado em `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] Cobertura PRD → SPEC documentada (histórias, RN, SC)
- [ ] Conflitos detectados e classificados
- [ ] Recomendações e próximos passos reportados
