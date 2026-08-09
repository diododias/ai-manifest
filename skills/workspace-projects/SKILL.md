---
name: workspace-projects
description: Localiza a fonte canonica de um projeto, atualiza somente o artefato pertencente ao dominio correto e organiza assets de sessao isolados por execucao. Use quando uma missao mencionar `projects/`, CONTEXT.md, STATUS.md, requisitos, UX, planos, Work Items, evidencias, transcricoes, printscreens ou repositorios ligados a um projeto.
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

## Assets de sessao

- Material bruto de uma execucao — transcricoes, printscreens, e-mails, PDFs, documentos Word e afins — vai em `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`, nunca solto em `plans/` nem misturado com o artefato final.
- `<workflow>` identifica o workflow ou a skill que gerou o material (ex.: `00-intake-and-triage`, `business-discovery`, `technical-discovery`). `<session-id>` e um identificador curto e unico da execucao (mission_id ou run id); nunca reaproveite a pasta de uma sessao anterior, mesmo que o resultado tenha sido descartado.
- Use subpastas por tipo dentro da pasta da sessao somente quando houver mais de um arquivo do mesmo tipo — `transcripts/`, `screenshots/`, `emails/`, `documents/`. Um unico arquivo pode ficar na raiz da pasta da sessao.
- Assets nao sao fonte canonica: sao evidencia de apoio. A conclusao, decisao ou requisito extraido vai para o artefato do dominio correto (PM, UX ou Tech Lead); referencie o caminho do asset em vez de copiar o conteudo bruto.
- Se a execucao for repetida por resultado insatisfatorio, crie uma nova pasta de sessao e registre no `STATUS.md` ou no Work Item qual sessao sustenta a versao vigente do artefato. Sessoes descartadas continuam no historico, mas deixam de ser referenciadas.

## Fechamento

Atualize apenas o artefato autorizado e mantenha links para as fontes consultadas. Se a missao atravessar dominios, prepare um handoff rastreavel para o owner seguinte em vez de editar a fonte alheia.
