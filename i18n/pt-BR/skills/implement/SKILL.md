---
name: implement
description: Implementa um bloco de um plano técnico com validação incremental e tracking atualizado. Use quando houver plano de implementação e SPEC aprovados; não publica commits ou PRs sem pedido explícito.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Implementar o código seguindo o plano de implementação, bloco a bloco, com validação incremental.

## Contrato de artefatos

Resolva o plano, a SPEC e o tracking conforme [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** `teamwork/plan/feature-plan-<feature-slug>/plano-implementacao.md`
- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`
- **Obrigatório:** `teamwork/plan/feature-plan-<feature-slug>/tracking.md`
- **Opcional:** bloco específico para implementar (via `$ARGUMENTS`)

## Execution Steps

### 1. Localizar a feature e o plano

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira do contexto.
- Leia `plano-implementacao.md`, `SPEC.md` e `tracking.md`.

### 2. Identificar bloco a implementar

- Se `$ARGUMENTS` especifica um bloco, implemente apenas esse.
- Caso contrário, implemente o próximo bloco não concluído do plano.
- Verifique dependências: blocos dependentes devem estar ✅ antes de iniciar.

### 3. Implementar o bloco

Para cada ação dentro do bloco:

1. **Antes de escrever código:**
   - Leia os arquivos existentes que serão modificados.
   - Entenda convenções, padrões e imports existentes.
   - Verifique se há testes existentes relevantes.

2. **Escreva o código:**
   - Siga convenções do repositório.
   - Mudanças pequenas e incrementais.
   - Prefira modificar código existente a criar novo quando possível.

3. **Após cada mudança:**
   - Verifique se o código compila/roda sem erros óbvios.
   - Execute lint/format se disponível.

### 4. Validação do bloco

Após implementar todas as ações do bloco:

- Execute testes relevantes (se existirem).
- Valide contra os critérios de aceite do bloco no plano.
- Se houver erro, corrija antes de avançar.

### 5. Atualizar tracking

Após concluir o bloco:
- Atualize `tracking.md`: status → ✅, data de fim.
- Se bloqueado: status → ❌, descreva o bloqueio no log.

### 6. Progressão

- Após concluir um bloco, prossiga para o próximo (respeitando dependências).
- Se `$ARGUMENTS` pediu bloco específico, pare ao concluir.

### 7. Reportar no chat

- Resumo: bloco implementado, arquivos criados/modificados.
- Testes executados e resultado.
- Próximo bloco recomendado.
- Se bloqueado: descrição do problema e sugestão.

## Regras

- **Não pule blocos** — dependências existem por motivo.
- **Valide incrementalmente** — não acumule mudanças sem testar.
- **Siga o plano** — se precisar desviar, documente no tracking.
- **Commits pequenos** — proponha um commit após cada bloco concluído; só use `/commit` quando o usuário pedir o registro em Git.

## Done When

- [ ] Bloco(s) implementado(s) conforme plano
- [ ] Código segue convenções do repositório
- [ ] Testes relevantes executados
- [ ] tracking.md atualizado
- [ ] Próximo bloco identificado (ou feature concluída)
