# Regras dos agentes

1. Leia `README.md`, `WORKSPACE.md` e este arquivo antes de iniciar uma missão.
2. Antes de atuar em um projeto, leia `CONTEXT.md` e `STATUS.md`.
3. Consulte `engineering/repositories.yaml` para localizar o código envolvido.
4. Leia as instruções locais de cada repositório antes de alterá-lo.
5. Crie ou assuma um Work Item antes de modificar artefatos.
6. Registre no Work Item o repositório, branch, base e worktree da missão.
7. Verifique o estado Git e preserve alterações preexistentes.
8. Não edite um artefato já assumido por outro agente sem divisão explícita.
9. Registre decisões duráveis, validações e evidências em suas fontes oficiais.
10. Produza um handoff ao transferir responsabilidade.
11. Não trate `memory.md` como fonte de verdade.
12. Só mova um item para `done` quando todos os critérios tiverem evidência.

## Skills obrigatórias

- Antes de agir, verifique as skills disponíveis e use todas as que forem aplicáveis; uma skill disponível e aderente à missão não pode ser ignorada. O [catálogo de agentes](../../docs/agents/catalog.md) lista as skills recomendadas por papel.
- Use `/workspace-memory` ao iniciar ou retomar uma missão e antes de registrar memória; use `/workspace-projects` ao consultar ou alterar `projects/`; use `/workspace-board` ao escolher, assumir, bloquear, transicionar ou encerrar um Work Item.
- Use também a skill de domínio disponível que corresponda ao trabalho. Cite, no Work Item, handoff ou resultado, os nomes exatos das skills usadas; se nenhuma skill de domínio se aplicar, registre o motivo.
- Grave transcrições, printscreens, e-mails, PDFs e outros materiais brutos de uma sessão em `projects/<project>/plans/assets/<workflow>/<data>-<session-id>/`, nunca soltos em `plans/` nem misturados com sessões anteriores. Ver [`workspace-projects`](../../skills/workspace-projects/SKILL.md).

## Fluxo mínimo

1. Escolha um item `ready` no `BOARD.md`.
2. Confirme dependências e assuma o item no arquivo correspondente.
3. Crie branch e worktree quando houver alteração de código.
4. Execute o plano, atualizando evidências e histórico.
5. Solicite revisão e validação.
6. Atualize `STATUS.md`, gere o handoff necessário e encerre o item.
