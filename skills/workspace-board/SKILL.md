---
name: workspace-board
description: Seleciona, assume e reconcilia Work Items com o `BOARD.md` de um workspace. Use ao escolher trabalho elegível, mudar o estado de uma missão, registrar bloqueio, preparar revisão ou encerrar uma entrega.
---

# Board do workspace

## Regras de autoridade

- `BOARD.md` é uma visão consolidada; o arquivo do Work Item é a fonte autoritativa de estado, owner, escopo, dependências e evidências.
- Nunca mova um card apenas para refletir expectativa. Primeiro atualize ou confirme o Work Item; depois reconcilie o board e `STATUS.md` quando o contrato local o exigir.
- Não assuma, altere ou encerre item pertencente a outro agente sem divisão explícita de responsabilidade.

## Fluxo

1. Leia o board e selecione somente item elegível para a fase: dependências resolvidas, owner humano, escopo, risco e critério de conclusão definidos.
2. Abra o Work Item e confirme fontes de entrada, repositório, branch/base/worktree quando houver código, e gates aplicáveis.
3. Registre a assunção no Work Item antes de modificar artefatos. Ao bloquear, documente causa, impacto, evidência e próximo owner.
4. Antes de cada transição, confirme os critérios do novo estado. Para `done`, exija evidência de todos os critérios; para entrega parcial, mantenha o estado que reflita a pendência.
5. Reconcilie `BOARD.md` como índice e atualize `STATUS.md` com o estado verificável. Produza handoff quando a responsabilidade mudar.

## Resultado esperado

No envelope de saída, informe `work_item_id`, estado anterior e atual, evidência dos gates e próximo owner. Declare qualquer divergência entre board, Work Item e estado real como bloqueio ou risco.
