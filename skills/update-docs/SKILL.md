---
name: "update-docs"
description: "Compara implementação, PRD e SPEC, registra desvios e atualiza documentação aprovada. Use após validação de uma entrega quando for necessário preservar rastreabilidade entre o planejado e o entregue."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Sincronizar PRD e SPEC com o que foi efetivamente implementado, documentando desvios e atualizando documentação.

## Contrato de artefatos

Siga [o contrato compartilhado](../references/workflow-contract.md). Não
reescreva requisitos, critérios de aceite ou status de aprovação para acomodar
o código: registre a divergência primeiro e só atualize o baseline após decisão
explícita.

## Inputs

- **Obrigatório:** `.agents/prd/<feature-slug>/PRD.md`
- **Obrigatório:** `.agents/spec/<feature-slug>/SPEC.md`
- **Obrigatório:** código implementado
- **Opcional:** `teamwork/plan/feature-plan-<feature-slug>/tracking.md`

## Execution Steps

### 1. Localizar a feature

- Se `$ARGUMENTS` contém slug, use-o. Caso contrário, infira do contexto.
- Verifique se os artefatos existem.

### 2. Carregar artefatos

- Leia `PRD.md` — versão planejada.
- Leia `SPEC.md` — versão técnica planejada.
- Analise o código implementado (diff).

### 3. Identificar desvios

Compare planejado vs implementado:

| Artefato | Item | Planejado | Implementado | Desvio |
|----------|------|-----------|-------------|--------|
| PRD | HIST-01 | ... | ... | ✅ Iguais / ⚠️ Diferente / ❌ Não implementado |
| SPEC | CT-01 | ... | ... | ... |

Classifique desvios:
- **Sem desvio:** implementação idêntica ao planejado.
- **Desvio menor:** ajuste que não impacta requisitos (refactor, rename).
- **Desvio de escopo:** implementou algo a mais ou a menos.
- **Desvio técnico:** abordagem diferente da planejada.
- **Não implementado:** item do planejado que ficou de fora.

### 4. Atualizar PRD após decisão registrada

- Registre o resultado e o link para `desvios.md` no changelog.
- Marque histórias como implementadas somente se os critérios acordados foram atendidos.
- Para desvio de escopo ou requisito, preserve o baseline e registre decisão, dono e data antes de alterá-lo.

### 5. Atualizar SPEC após decisão registrada

- Registre evidência da implementação e o link para `desvios.md` no changelog.
- Altere a solução ou os CTs somente com decisão técnica explícita; não transforme um desvio em requisito silenciosamente.

### 6. Atualizar README (se aplicável)

- Se a feature muda comportamento visível, atualize README.
- Se adiciona dependência, documente.
- Se muda setup/instruções, atualize.

### 7. Gerar relatório de desvios

Gere `teamwork/plan/feature-plan-<feature-slug>/desvios.md`:

```markdown
# Desvios — <Feature Name>

**Feature:** <slug>
**Data:** <YYYY-MM-DD>

---

## Resumo

| Tipo | Quantidade |
|------|-----------|
| ✅ Sem desvio | X |
| ⚠️ Desvio menor | X |
| 🔵 Desvio de escopo | X |
| 🟣 Desvio técnico | X |
| ❌ Não implementado | X |

---

## Desvios Detalhados

### <Item>
- **Artefato:** PRD / SPEC
- **Item:** <ID ou nome>
- **Planejado:** <o que estava planejado>
- **Implementado:** <o que foi feito>
- **Impacto:** <qual o impacto do desvio>
- **Justificativa:** <por que o desvio>

---

## Ações Necessárias

- <atualizações pendentes>
- <docs que precisam de update>
```

### 8. Reportar no chat

- Resumo: X itens sem desvio, Y com desvio, Z não implementados.
- Desvios que precisam de atenção.
- Docs atualizados.

## Convenções

- Desvios nunca são apagados — documentados para rastreabilidade.
- PRD e SPEC são fontes da verdade — devem refletir implementação real.
- Português.

## Done When

- [ ] PRD atualizado com status e desvios
- [ ] SPEC atualizada com status e desvios
- [ ] README atualizado (se aplicável)
- [ ] `desvios.md` gerado
- [ ] Resultado reportado no chat
