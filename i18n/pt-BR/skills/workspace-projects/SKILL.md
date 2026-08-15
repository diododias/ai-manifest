---
name: workspace-projects
description: Localiza a fonte canônica de um projeto, atualiza somente o artefato pertencente ao domínio correto e organiza assets de sessão isolados por execução. Use quando uma missão mencionar `projects/`, CONTEXT.md, STATUS.md, requisitos, UX, planos, Work Items, evidências, transcrições, printscreens ou repositórios ligados a um projeto.
---

# Projetos do workspace

## Entrada no projeto

1. Localize o projeto pelo portfólio, `BOARD.md` ou referência explícita. Não infira o slug somente pelo nome de um repositório.
2. Leia `projects/<project>/README.md`, `CONTEXT.md` e `STATUS.md` antes de agir. Confirme o owner do domínio e os links para entradas de PM, UX e Tech Lead.
3. Consulte `engineering/repositories.yaml` ou o registro equivalente antes de abrir ou alterar código. Leia também as instruções locais do repositório.

## Fonte canônica e destino

- Mantenha valor, prioridade e requisitos no workspace de PM; pesquisa, fluxos e validação de experiência no de UX; arquitetura, planos, implementação e risco no do Tech Lead.
- Use snapshots apenas como entrada identificada. Siga o link para a fonte canônica antes de tomar decisões ou atualizá-la.
- Grave artefatos persistentes em `projects/<project>/`; use `.coordination/` somente para trânsito temporário e handoff. Não duplique informação autoritativa entre workspaces.
- Relacione Work Item, repositório, branch, base, worktree, evidências e handoffs no artefato que os governa.

## Assets de sessão

- Todo material de uma execução — tanto o que o humano traz quanto o que a IA gera antes do gate — vai em `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`, nunca solto em `plans/` nem misturado com o artefato final.
- A regra de corte não é quem gerou, mas se passou pelo gate: antes do gate vai para `plans/assets/`, depois do gate vai para o destino canônico (`engineering/`, `product/`, `ux/`, `plans/active/`).
- `<workflow>` identifica o workflow ou a skill que gerou o material (ex.: `00-intake-and-triage`, `business-discovery`, `technical-discovery`). `<session-id>` é um identificador curto e único da execução (mission_id ou run id); nunca reaproveite a pasta de uma sessão anterior, mesmo que o resultado tenha sido descartado.
- Use subpastas por tipo dentro da pasta da sessão somente quando houver mais de um arquivo do mesmo tipo: `transcripts/` (transcrições de reuniões ou sessões), `drafts/` (rascunhos intermediários gerados pela IA), `screenshots/`, `emails/`, `documents/`. Um único arquivo pode ficar na raiz da pasta da sessão.
- Assets não são fonte canônica: são evidência de apoio e rastro auditável. A conclusão, decisão ou requisito extraído vai para o artefato do domínio correto; referencie o caminho do asset em vez de copiar o conteúdo bruto.
- Reviews adversariais não ficam em `plans/assets/` — são artefatos formais com gate próprio e vão para `execution/reviews/<tipo>-<id>.md`.
- Se a execução for repetida por resultado insatisfatório, crie uma nova pasta de sessão e registre no `STATUS.md` ou no Work Item qual sessão sustenta a versão vigente do artefato. Sessões descartadas continuam no histórico, mas deixam de ser referenciadas.

## Fechamento

Atualize apenas o artefato autorizado e mantenha links para as fontes consultadas. Se a missão atravessar domínios, prepare um handoff rastreável para o owner seguinte em vez de editar a fonte alheia.
