---
name: "update-pr"
description: "Monta e, mediante confirmação, atualiza a descrição de um pull request com contexto, testes e desvios. Use quando o usuário pedir para preparar ou editar a descrição de um PR aberto."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Atualizar a descrição do PR com contexto completo, o que foi implementado, testado e desvios documentados.

## Contrato de artefatos e publicação

Resolva os caminhos conforme [o contrato compartilhado](../references/workflow-contract.md).
Primeiro apresente a descrição proposta; só execute `gh pr edit` após
confirmação explícita. Só adicione labels que existam no repositório e tenham
sido solicitadas.

## Inputs

- **Obrigatório:** PR aberto (número ou branch)
- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`
- **Obrigatório:** contexto das tasks implementadas
- **Opcional:** `teamwork/plan/feature-plan-<feature-slug>/desvios.md`

## Execution Steps

### 1. Localizar o PR

- Se `$ARGUMENTS` contém número, use-o.
- Caso contrário, encontre o PR da branch atual:
  ```bash
  gh pr list --head <branch-name> --json number,title
  ```

### 2. Coletar contexto

- Leia a SPEC — contexto técnico.
- Leia `desvios.md` se existir — desvios documentados.
- Extraia lista de commits:
  ```bash
  gh pr view <number> --json commits
  ```
- Identifique arquivos modificados:
  ```bash
  gh pr diff <number> --stat
  ```

### 3. Montar descrição do PR

Gere a descrição seguindo template do time:

```markdown
## Resumo

<descrição objetiva do que esta PR faz e por quê>

## Contexto

<problema de negócio que a feature resolve, referenciando PRD>

## O que foi implementado

- [x] <item 1>
- [x] <item 2>
- [ ] <item 3> (se entrega parcial)

## Como testar

<passos concretos de validação>

1. <passo 1>
2. <passo 2>
3. <resultado esperado>

## Testes executados

- [ ] Unitários: <resultado>
- [ ] Integração: <resultado>
- [ ] E2E: <resultado> (se aplicável)

## Desvios documentados

<se houver desvios do planejado, documente aqui>
<referencie desvios.md se extenso>

## Artefatos

- PRD: `.agents/prd/<feature>/PRD.md`
- SPEC: `.agents/spec/<feature>/SPEC.md`
- Tracking: `teamwork/plan/feature-plan-<name>/tracking.md`

## Checklist

- [ ] Código segue convenções do repositório
- [ ] Testes passando
- [ ] PRD/SPEC atualizados (se aplicável)
- [ ] Sem secrets ou dados sensíveis
- [ ] Documentation atualizada (se aplicável)

Closes #N
```

### 4. Atualizar o PR após confirmação

```bash
gh pr edit <number> --body-file <arquivo-temporario-confirmado>
```

### 5. Adicionar labels solicitadas (se aplicável)

```bash
gh label list
gh pr edit <number> --add-label "<label-existente-e-solicitada>"
```

### 6. Reportar no chat

- Número e título do PR.
- Resumo do que foi preenchido.
- Status (pronto para review / precisa de ajustes).

## Convenções

- Descrição do PR é a fonte de contexto para revisores.
- Sempre referencie a issue com `Closes #N` ou `Refs #N`.
- Desvios devem ser transparentes — não esconda.
- Português para documentação.

## Done When

- [ ] Descrição do PR atualizada com template completo
- [ ] Contexto, implementação, testes e desvios documentados
- [ ] Referência à issue incluída
- [ ] Labels aplicadas (se aplicável)
- [ ] Status reportado no chat
