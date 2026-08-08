---
name: workspace-board
description: Seleciona, assume e reconcilia Work Items com o `BOARD.md` de um workspace. Use ao escolher trabalho elegivel, mudar o estado de uma missao, registrar bloqueio, preparar revisao ou encerrar uma entrega.
---

# Board do workspace

## Regras de autoridade

- `BOARD.md` e uma visao consolidada; o arquivo do Work Item e a fonte autoritativa de estado, owner, escopo, dependencias e evidencias.
- Nunca mova um card apenas para refletir expectativa. Primeiro atualize ou confirme o Work Item; depois reconcilie o board e `STATUS.md` quando o contrato local o exigir.
- Nao assuma, altere ou encerre item pertencente a outro agente sem divisao explicita de responsabilidade.

## Fluxo

1. Leia o board e selecione somente item elegivel para a fase: dependencias resolvidas, owner humano, escopo, risco e criterio de conclusao definidos.
2. Abra o Work Item e confirme fontes de entrada, repositorio, branch/base/worktree quando houver codigo, e gates aplicaveis.
3. Registre a assuncao no Work Item antes de modificar artefatos. Ao bloquear, documente causa, impacto, evidencia e proximo owner.
4. Antes de cada transicao, confirme os criterios do novo estado. Para `done`, exija evidencia de todos os criterios; para entrega parcial, mantenha o estado que reflita a pendencia.
5. Reconcile `BOARD.md` como indice e atualize `STATUS.md` com o estado verificavel. Produza handoff quando a responsabilidade mudar.

## Resultado esperado

No envelope de saida, informe `work_item_id`, estado anterior e atual, evidencia dos gates e proximo owner. Declare qualquer divergencia entre board, Work Item e estado real como bloqueio ou risco.
