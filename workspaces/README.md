# Workspaces de exemplo

Esta área contém implementações concretas dos workspaces operacionais descritos na arquitetura do Agent Team.

Cada papel possui uma raiz independente para que seus contratos, exemplos e fontes de verdade possam evoluir sem misturar responsabilidades:

- [`tech-lead/`](tech-lead/README.md): viabilidade, arquitetura, implementação e risco operacional;
- [`ux/`](ux/README.md): pesquisa, experiência, acessibilidade e validação com usuários;
- [`pm/`](pm/README.md): valor, prioridade, requisitos e resultados de produto.

Os exemplos não são o workspace de produção de uma equipe. Nomes, organizações, repositórios e estados são fictícios e devem ser substituídos ao copiar a estrutura.

## Workflows dentro de cada workspace

Os contratos reutilizáveis ficam no [catálogo global de workflows](../docs/workflows/README.md). Cada workspace de usuário deve manter `docs/workflows/` como camada de binding local: quais workflows estão habilitados, qual versão canônica é usada, permissões, integrações e roteamento de handoffs.

Artefatos de uma execução não pertencem a `docs/workflows/`. Eles ficam em `projects/<project>/`, no workspace dono do domínio: o PM registra discovery, PRD, decisões e Work Items; UX registra research, jornadas, fluxos, especificações e validações; o Tech Lead registra planos em `projects/<project>/plans/active/`, specs, ADRs, evidências, reviews e worktrees. `coordination/` é somente trânsito temporário.

Material bruto que sustenta as análises e discussões de um workflow — transcrições, printscreens, e-mails, PDFs, documentos Word e afins — fica em `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`, em qualquer um dos três workspaces. Cada execução usa sua própria pasta de sessão; reexecutar um workflow por resultado insatisfatório nunca sobrescreve ou mistura material com a tentativa anterior. `plans/assets/` não é fonte canônica — a conclusão vai para o artefato do domínio correto, e o asset permanece como rastro auditável. Ver a skill [`workspace-projects`](../skills/workspace-projects/SKILL.md) para o detalhamento completo.

## Ownership entre workspaces

| Domínio | Fonte canônica | Os demais workspaces recebem |
|---|---|---|
| Valor, prioridade, outcome e requisitos | `pm/` | decisão aprovada e handoff de produto |
| Evidência de usuário, jornada e experiência | `ux/` | UX spec, critérios e handoff de experiência |
| Arquitetura, implementação e risco operacional | `tech-lead/` | viabilidade, contratos técnicos e evidence pack |

Uma informação autoritativa não deve ser mantida em dois workspaces. Quando uma IA precisar de contexto de outro domínio, deve seguir o link até a fonte ou usar um snapshot identificado como não autoritativo e confirmar sua validade antes de agir.
