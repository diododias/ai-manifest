---
name: workspace-projects
description: Localiza a fonte canonica de um projeto e atualiza somente o artefato pertencente ao dominio correto. Use quando uma missao mencionar `projects/`, CONTEXT.md, STATUS.md, requisitos, UX, planos, Work Items, evidencias ou repositorios ligados a um projeto.
---

# Projetos do workspace

## Entrada no projeto

1. Localize o projeto pelo portfolio, `BOARD.md` ou referencia explicita. Nao infira o slug somente pelo nome de um repositorio.
2. Leia `projects/<project>/README.md`, `CONTEXT.md` e `STATUS.md` antes de agir. Confirme o owner do dominio e os links para entradas de PM, UX e Tech Lead.
3. Consulte `engineering/repositories.yaml` ou o registro equivalente antes de abrir ou alterar codigo. Leia tambem as instrucoes locais do repositorio.

## Fonte canonica e destino

- Mantenha valor, prioridade e requisitos no workspace de PM; pesquisa, fluxos e validacao de experiencia no de UX; arquitetura, planos, implementacao e risco no do Tech Lead.
- Use snapshots apenas como entrada identificada. Siga o link para a fonte canonica antes de tomar decisoes ou atualiza-la.
- Grave artefatos persistentes em `projects/<project>/`; use `coordination/` somente para transito temporario e handoff. Nao duplique informacao autoritativa entre workspaces.
- Relacione Work Item, repositorio, branch, base, worktree, evidencias e handoffs no artefato que os governa.

## Fechamento

Atualize apenas o artefato autorizado e mantenha links para as fontes consultadas. Se a missao atravessar dominios, prepare um handoff rastreavel para o owner seguinte em vez de editar a fonte alheia.
