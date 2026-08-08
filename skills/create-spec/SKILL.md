---
name: create-spec
description: Cria uma SPEC técnica a partir de PRD, visão técnica e decisões de refinamento. Use depois do refinamento técnico quando a implementação precisar de componentes, contratos, riscos e critérios técnicos rastreáveis.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Gerar o SPEC Plan consolidando a solução técnica detalhada para cada história, com critérios de aceite técnicos e plano de implementação.

## Contrato de artefatos

Antes de criar a SPEC, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `.agents/prd/<feature-slug>/PRD.md`
- **Obrigatório:** `teamwork/plan/feature-plan-<feature-slug>/visao-tecnica.md`
- **Obrigatório:** transcrição da agenda técnica
- **Opcional:** `teamwork/plan/feature-plan-<feature-slug>/historias.md`

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira dos artefatos.
- Verifique se os arquivos de entrada existem.

### 2. Carregar contexto

- Leia `PRD.md` — requisitos e histórias.
- Leia `visao-tecnica.md` — análise técnica prévia.
- Leia a transcrição da agenda técnica — decisões e discussões.
- Leia `historias.md` se existir — contexto adicional.

### 3. Para cada história, definir a solução técnica

Estruture:

- **Abordagem técnica:** como resolver (padrões, algoritmos, integrações).
- **Componentes:** arquivos, módulos, classes, endpoints a criar/modificar.
- **Fluxo de implementação:** ordem das mudanças, dependências internas.
- **Critérios de aceite técnicos:** testes unitários, integração, performance.
- **Dados:** modelos, migrations, validações.

### 4. Definir contrato de interfaces (se aplicável)

Para APIs, endpoints ou contratos entre módulos:
- Request/response format
- Validações
- Códigos de erro

### 5. Gerar output

Crie `.agents/spec/<feature-slug>/SPEC.md` (crie os diretórios se necessário) no formato:

```markdown
# SPEC — <Feature Name>

**Feature:** <slug>
**Status:** 🟡 Em revisão
**Data:** <YYYY-MM-DD>
**PRD:** .agents/prd/<feature-slug>/PRD.md
**Autor:** Tech Lead (via create-spec)

---

## 1. Visão Geral da Solução

<descrição técnica consolidada da abordagem>

## 2. Stack e Dependências

| Necessidade | Tecnologia | Versão | Status |
|-------------|-----------|--------|--------|
| ... | ... | ... | Existente / Nova |

## 3. Modelo de Dados

### Entidades

#### <Entidade>
| Campo | Tipo | Validação | Obrigatório |
|-------|------|-----------|-------------|
| ... | ... | ... | Sim/Não |

### Relacionamentos
<descrição dos relacionamentos entre entidades>

### Migrations
<estrutura das migrations necessárias>

## 4. Solução por História

### HIST-01: <Título>

#### Componentes
| Arquivo | Tipo | Ação |
|---------|------|------|
| ... | ... | Criar / Modificar |

#### Fluxo de Implementação
1. <passo 1>
2. <passo 2>

#### Critérios de Aceite Técnicos
- [ ] CT-01: <critério técnico testável>
- [ ] CT-02: <critério técnico testável>

#### Testes
- Unitários: <o que testar>
- Integração: <o que testar>

---

## 5. Contratos de Interface (se aplicável)

### <Endpoint/Interface>
**Método:** GET/POST/...

**Request:**
```json
{ ... }
```

**Response:**
```json
{ ... }
```

**Erros:**
| Código | Descrição |
|--------|-----------|
| ... | ... |

---

## 6. Fluxo Geral de Implementação

### Fase 1: Setup
<inicialização, configs, dependências>

### Fase 2: Componentes Fundamentais
<modelos, services, middlewares>

### Fase 3+: Por História
<histórias em ordem de dependência>

## 7. Riscos Técnicos

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| ... | ... | ... |

## 8. Validação

### Cenários de Validação
<quickstart: como provar que funciona end-to-end>

## 9. Gaps e Pendências

| ID | Descrição | Status |
|----|-----------|--------|
| ... | ... | ⏳ Aberto |
```

### 6. Reportar no chat

- Resumo: X histórias com solução definida, Y componentes a criar/modificar, Z testes planejados.
- Riscos técnicos de maior atenção.
- Pronto para `review-spec`.

## Convenções

- SPEC é o contrato técnico — deve ser suficiente para um engenheiro implementar sem perguntas.
- CT-XX para critérios de aceite técnicos.
- Status: 🟡 Em revisão → 🟢 Aprovado → ✅ Implementado.
- Português. Código e nomes técnicos em inglês.

## Done When

- [ ] `SPEC.md` criado em `.agents/spec/<feature-slug>/`
- [ ] Cada história do PRD com solução técnica definida
- [ ] Modelo de dados documentado
- [ ] Contratos de interface definidos (se aplicável)
- [ ] Fluxo de implementação sequenciado
- [ ] Resumo reportado no chat
