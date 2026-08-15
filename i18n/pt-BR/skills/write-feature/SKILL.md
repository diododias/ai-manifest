---
name: write-feature
description: Extrai e fatia histórias de produto a partir de requisitos e transcrição de refinamento, mantendo vínculo com regras e critérios. Use após a discovery quando for necessário preparar histórias para o PRD.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Transformar `requisitos.md` + transcrição da agenda de refinamento em histórias estruturadas, prontas para revisão e geração do PRD.

## Contrato de artefatos

Antes de criar histórias, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `business-discovery/<feature-slug>/requisitos.md`
- **Obrigatório:** transcrição da agenda de refinamento
- **Opcional:** nome/slug da feature (inferir de requisitos.md se não fornecido)

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira de `requisitos.md`.
- Verifique se `business-discovery/<feature-slug>/requisitos.md` existe.

### 2. Carregar contexto

- Leia `requisitos.md` por inteiro — é o baseline de requisitos.
- Leia a transcrição da agenda de refinamento.

### 3. Extrair histórias da transcrição

Identifique as histórias discutidas na agenda de refinamento. Para cada uma:

- **Contexto:** o que foi discutido, decisões tomadas, dependências citadas.
- **Critérios de aceite:** extraídos dos cenários Gherkin e regras de negócio associadas.
- **Dependências:** outras histórias, sistemas externos, times dependentes.
- **Tamanho estimado:** se discutido na agenda (P1/MVP vs incrementos).

### 4. Mapear para requisitos existentes

Para cada história, vincule:
- RN-XX (regras de negócio) que a história implementa
- SC-XX (critérios de sucesso) que a história contribui
- US-X (user story) do `requisitos.md` que ela detalha

### 5. Identificar histórias para fatiamento

Sinalize histórias que:
- São grandes demais para um sprint
- Acoplam múltiplos fluxos sem dependência
- Precisam de spike técnico antes

### 6. Gerar output

Crie o diretório `teamwork/plan/feature-plan-<feature-slug>/` (se não existir).

Gere `historias.md` no formato:

```markdown
# Histórias — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>
**Baseline:** business-discovery/<feature-slug>/requisitos.md
**Agenda:** <descrição da agenda de refinamento>

---

## HIST-01: <Título>

**Prioridade:** P1/P2/P3
**Requisitos vinculados:** RN-XX, US-X

### Contexto
<o que foi discutido na agenda, decisões, dependências>

### Critérios de Aceite
- [ ] CA-01: <critério mensurável>
- [ ] CA-02: <critério mensurável>

### Dependências
- <outras histórias, sistemas, times>

### Notas
<observações, riscos, pontos de atenção>

---

## HIST-02: <Título>
...
```

### 7. Reportar no chat

- Resumo: X histórias extraídas, Y com dependências, Z marcadas para fatiamento.
- Lista de histórias com prioridade e status.
- Pontos de atenção (histórias grandes, dependências bloqueantes).

## Convenções

- `HIST-XX` para IDs de histórias (sequencial).
- `CA-XX` para critérios de aceite por história.
- Prioridade: P1 = MVP, P2 = incremento, P3 = futuro.
- Português. Exemplos numéricos > descrições vagas.
- Histórias devem ser independentes quando possível.

## Done When

- [ ] `historias.md` gerado em `teamwork/plan/feature-plan-<feature-slug>/`
- [ ] Cada história vinculada a requisitos existentes (RN, US, SC)
- [ ] Histórias grandes sinalizadas para fatiamento
- [ ] Resumo reportado no chat
