---
name: technical-discovery
description: Prepara uma visão técnica baseada no PRD, mapeando componentes, dependências, riscos e decisões abertas. Use antes de uma agenda de refinamento técnico ou de escrever a SPEC de uma feature.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Gerar a visão técnica estruturada da solução como base para a discussão na agenda de refinamento técnico.

## Contrato de artefatos

Antes de criar a visão técnica, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `.agents/prd/<feature-slug>/PRD.md`
- **Opcional:** contexto técnico do time (arquitetura existente, stack, convenções)
- **Opcional:** `requisitos.md` para contexto adicional

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira do PRD.
- Verifique se o PRD existe.

### 2. Carregar contexto

- Leia `PRD.md` — base para a análise técnica.
- Leia `requisitos.md` se existir — contexto de negócio adicional.
- Identifique stack, arquitetura e convenções existentes no repositório.

### 3. Analisar impacto técnico

Para cada história do PRD, avalie:

- **Componentes afetados:** quais módulos, serviços, APIs precisam de mudança.
- **Dependências externas:** APIs de terceiros, bancos de dados, filas.
- **Riscos técnicos:** complexidade, incertezas, spike necessário.
- **Estimativa de esforço:** relativa (S/M/L/XL) baseada em complexidade.

### 4. Mapear stack e decisões

- **Tecnologias necessárias:** libs, frameworks, serviços.
- **Padrões existentes:** como resolver problemas similares no código atual.
- **Decisões abertas:** pontos que precisam de consenso no refinamento.

### 5. Gerar output

Crie `teamwork/plan/feature-plan-<feature-slug>/visao-tecnica.md` no formato:

```markdown
# Visão Técnica — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>
**PRD:** .agents/prd/<feature-slug>/PRD.md

---

## 1. Resumo da Solução

<descrição técnica de alto nível da abordagem>

## 2. Impacto por História

### HIST-01: <Título>

| Dimensão | Detalhe |
|----------|---------|
| Componentes | <módulos/serviços afetados> |
| Dependências | <APIs externas, bancos, filas> |
| Risco | 🟢 Baixo / 🟡 Médio / 🔴 Alto |
| Esforço | S / M / L / XL |
| Decisões abertas | <o que precisa de consenso> |

## 3. Stack e Tecnologias

| Necessidade | Tecnologia | Status |
|-------------|-----------|--------|
| ... | ... | Existente / Nova / Avaliar |

## 4. Padrões e Convenções

- <padrões do repositório que devem ser seguidos>
- <convenções de código, testes, deploy>

## 5. Riscos e Mitigações

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| ... | ... | ... |

## 6. Questões para Refinamento

- <pontos que precisam de decisão coletiva>
- <alternativas técnicas a considerar>
- <dependências de outros times>
```

### 6. Reportar no chat

- Resumo: X componentes impactados, Y riscos identificados, Z decisões abertas.
- Riscos de maior atenção.
- Questões para levar ao refinamento técnico.

## Convenções

- Documento interno do Tech Lead — não é entregável para o time externo.
- Risco: 🟢 Baixo (padrão conhecido), 🟡 Médio (complexidade moderada), 🔴 Alto (spike/incerteza).
- Esforço relativo: S (< 1 dia), M (1-3 dias), L (3-5 dias), XL (> 1 semana).
- Português.

## Done When

- [ ] `visao-tecnica.md` criado em `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] Cada história do PRD analisada tecnicamente
- [ ] Riscos e decisões abertas documentados
- [ ] Resumo reportado no chat
