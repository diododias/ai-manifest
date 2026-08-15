# Skills

O repositório carrega um catálogo de skills em `skills/`. Cada skill é um procedimento verificável para uma tarefa recorrente que exige julgamento — o que a distingue de um script, que cobre o determinístico.

As skills de maior impacto operacional neste repositório são:

| Skill | O que faz |
|---|---|
| `analyse-bug` | investiga um bug com rastreamento estruturado de hipóteses até isolamento da causa raiz |
| `fix-bug` | executa a correção a partir do diagnóstico, com critério de parada e evidence pack |
| `implement` | implementa uma feature a partir de uma spec aprovada, respeitando rules e estratégia de testes |
| `write-feature` | fluxo completo de spec → implementação → PR para features novas |
| `code-review` | revisão estruturada com checagem de rules, testes e evidência antes de aprovar |
| `check-pr` | valida um PR aberto antes do merge: status checks, scope, evidence pack |
| `create-spec` | produz uma especificação técnica a partir de um requisito, pronta para revisão humana |
| `refine-spec` | itera sobre uma spec existente incorporando feedback |
| `technical-discovery` | mapeia o repositório para orientar uma tarefa nova — lido antes de qualquer implementação |
| `test-integration-local` | roda a bateria de integração localmente com ambiente isolado |
| `commit` | monta mensagem de commit estruturada com rastreabilidade para o Work Item |
| `update-docs` | atualiza a documentação afetada por uma mudança, incluindo ADRs quando necessário |
| `workspace-memory` | retoma contexto de sessões anteriores antes de qualquer ação |
| `workspace-board` | assume e reconcilia Work Items com evidência no board |

Skills específicas do repositório — migração de schema, geração de SDK, rollout do serviço — ficam em `skills/<nome>/SKILL.md` e seguem a mesma estrutura do catálogo global.
