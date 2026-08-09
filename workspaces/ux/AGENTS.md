# Regras dos agentes de UX

1. Leia `README.md` e `WORKSPACE.md` antes de atuar.
2. Trabalhe com missão, hipótese, owner humano e condição de parada explícitos.
3. Proteja consentimento, privacidade e anonimização de participantes.
4. Registre método, fonte, amostra, limitações e confiança de cada achado.
5. Não invente pesquisa, citação, participante, comportamento ou preferência.
6. Cubra estados de sucesso, vazio, loading, erro, permissão e recuperação quando aplicáveis.
7. Avalie acessibilidade desde a especificação, não apenas ao final.
8. Não altere outcome, prioridade ou restrição técnica sem devolver a decisão ao owner.
9. Nunca valide sozinho a experiência que produziu.
10. Entregue handoff rastreável ao PM ou Tech Lead.

## Skills obrigatórias

- Antes de agir, verifique as skills disponíveis e use todas as que forem aplicáveis; uma skill disponível e aderente à missão não pode ser ignorada. O [catálogo de agentes](../../docs/agents/catalog.md) lista as skills recomendadas por papel.
- Use `/workspace-memory` ao iniciar ou retomar uma missão e antes de registrar memória; use `/workspace-projects` ao consultar ou alterar `projects/`; use `/workspace-board` ao escolher, assumir, bloquear, transicionar ou encerrar um Work Item.
- Use também a skill de domínio disponível que corresponda ao trabalho. Cite, no Work Item, handoff ou resultado, os nomes exatos das skills usadas; se nenhuma skill de domínio se aplicar, registre o motivo.
- Grave transcrições de pesquisa, printscreens e outros materiais brutos de uma sessão em `projects/<project>/plans/assets/<workflow>/<data>-<session-id>/`, protegendo consentimento e privacidade dos participantes. Ver [`workspace-projects`](../../skills/workspace-projects/SKILL.md).
