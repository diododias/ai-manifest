---
name: refine-spec
description: Transforma uma SPEC aprovada em plano sequencial de implementação, dependências e tracking. Use antes de codificar uma feature para identificar blocos testáveis e a ordem segura de execução.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Transformar a SPEC em plano de implementação passo a passo, definindo ordem dos blocos, dependências e criando `tracking.md` para acompanhar execução.

## Contrato de artefatos

Antes de criar plano e tracking, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`
- **Opcional:** `.agents/prd/<feature-slug>/PRD.md` para contexto

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira da SPEC.
- Verifique se a SPEC existe.

### 2. Carregar contexto

- Leia `SPEC.md` por inteiro — é o plano técnico.
- Leia `PRD.md` se existir — contexto de prioridades.

### 3. Extrair blocos de implementação

Da SPEC, extraia:
- **Modelos de dados:** entidades, relações, migrations.
- **Services/lógica de negócio:** regras, validações, processamento.
- **Interfaces/APIs:** endpoints, contratos.
- **Integrações:** bancos externos, filas, serviços.
- **Frontend (se aplicável):** componentes, fluxos UI.

### 4. Definir ordem de dependências

Mapeie dependências entre blocos:
- O que precisa existir antes de quê?
- Quais blocos são independentes (paralelizáveis)?
- Qual o caminho mais seguro para ter algo testável cedo?

### 5. Criar plano sequencial

Gere `teamwork/plan/feature-plan-<feature-slug>/plano-implementacao.md`:

```markdown
# Plano de Implementação — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>
**SPEC:** .agents/spec/<feature-slug>/SPEC.md

---

## Sequência de Implementação

### Bloco 1: <Nome> (Fundação)
**Depende de:** Nenhum
**Arquivos:** `caminho/para/arquivo1`, `caminho/para/arquivo2`
**O que fazer:**
1. <ação 1>
2. <ação 2>

**Teste:** <como validar este bloco>

---

### Bloco 2: <Nome> (Core)
**Depende de:** Bloco 1
**Arquivos:** `caminho/para/arquivo3`
**O que fazer:**
1. <ação 1>

**Teste:** <como validar>

---

### Bloco 3: <Nome> (Paralelizável)
**Depende de:** Bloco 1
**Paralelizável com:** Bloco 4
**Arquivos:** `caminho/para/arquivo4`
**O que fazer:**
1. <ação 1>

**Teste:** <como validar>

---

## Grafo de Dependências

```
Bloco 1 (Fundação)
├── Bloco 2 (Core)
├── Bloco 3 (Paralelizável) ─┐
└── Bloco 4 (Paralelizável) ─┘
                              └── Bloco 5 (Integração)
                                    └── Bloco 6 (Polimento)
```

## Ponto de Início Mais Seguro

<Bloco 1> — fundação sem dependências, permite validação imediata.

## Estimativa

| Bloco | Esforço | Dependências |
|-------|---------|-------------|
| 1 | S | — |
| 2 | M | Bloco 1 |
| ... | ... | ... |

## Tracking

O `tracking.md` será criado ao iniciar a implementação.
```

### 6. Criar tracking.md

Gere `teamwork/plan/feature-plan-<feature-slug>/tracking.md`:

```markdown
# Tracking — <Feature Name>

**Feature:** <slug>
**Início:** <YYYY-MM-DD>
**Status:** 🟡 Em andamento

---

## Progresso

| Bloco | Status | Início | Fim | Notas |
|-------|--------|--------|-----|-------|
| 1 - Fundação | ⬜ Não iniciado | — | — | |
| 2 - Core | ⬜ Não iniciado | — | — | |
| 3 - ... | ⬜ Não iniciado | — | — | |

**Legenda:** ⬜ Não iniciado | 🟡 Em andamento | ✅ Concluído | ❌ Bloqueado

---

## Log

| Data | Evento |
|------|--------|
| — | — |
```

### 7. Reportar no chat

- Resumo: X blocos definidos, Y dependências mapeadas, Z paralelizáveis.
- Ponto de início recomendado.
- Estimativa total.

## Convenções

- Blocos organizados por ordem de dependência, não por arquivo.
- Cada bloco deve ser testável de forma independente quando possível.
- tracking.md é vivo — atualizado durante implementação.
- Português.

## Done When

- [ ] `plano-implementacao.md` gerado com blocos sequenciados
- [ ] `tracking.md` criado com status inicial
- [ ] Dependências entre blocos mapeadas
- [ ] Ponto de início mais seguro identificado
- [ ] Resumo reportado no chat
