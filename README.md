# Agent Team

Framework operacional para um núcleo humano formado por **Product Manager, UX e Tech Lead** coordenar agentes especializados ao longo de todo o ciclo de desenvolvimento de software.

O repositório reúne o modelo operacional, o catálogo de agentes, os workspaces onde o trio pilota o workflow e as skills que transformam discovery, especificação, implementação, validação e publicação em trabalho repetível.

## Comece por aqui

1. Leia o [modelo operacional canônico](docs/operating-model.md) para entender papéis, direitos de decisão e limites de autonomia.
2. Percorra a [jornada de ponta a ponta](docs/operations/end-to-end-journey.md) para ver gates, artefatos e passagem de contexto entre fases.
3. Consulte o [catálogo de agentes](docs/agents/catalog.md) e importe os [workspaces dos agentes no OpenClaw](docs/agents/README.md) para materializar os papéis especializados.
4. Explore os [workspaces de exemplo de PM, UX e Tech Lead](workspaces/README.md) — é ali que o trio efetivamente pilota o workflow: seleciona Work Items, executa fases, registra decisões e evidências.
5. Escolha as skills aplicáveis em [`skills/`](skills/); cada `SKILL.md` define contexto, entradas, saída e critérios de qualidade.
6. Use o [índice de documentação](docs/README.md) para os demais materiais canônicos, propostos e históricos.

## O workspace é o ponto de trabalho

`workspaces/<pm|ux|tech-lead>/` não é material de referência: é onde cada papel humano e seus agentes efetivamente rodam o workflow. Cada workspace mantém `AGENTS.md` (como operar), `BOARD.md` (Work Items em andamento), `memory/` (retomada de contexto) e `projects/<project>/` (artefatos reais de cada iniciativa). Ao iniciar uma missão, um agente deve ler o `AGENTS.md` do workspace, identificar as skills aplicáveis e seguir a estrutura de `projects/` em vez de criar convenções próprias.

## Fluxo de trabalho

| Fase | Resultado esperado | Referência principal |
|---|---|---|
| Descoberta | problema, requisitos, regras, cenários, métricas e lacunas explícitas | [`business-discovery`](skills/business-discovery/SKILL.md) |
| Produto e UX | objetivo, escopo, jornada e critérios de aceite observáveis | [jornada operacional](docs/operations/end-to-end-journey.md) |
| Especificação técnica | opções, riscos, plano técnico e contratos verificáveis | [`technical-discovery`](skills/technical-discovery/SKILL.md), [`create-spec`](skills/create-spec/SKILL.md) e [`review-spec`](skills/review-spec/SKILL.md) |
| Planejamento | coerência entre produto e técnica e uma sequência de execução | [`review-cross-prd-spec`](skills/review-cross-prd-spec/SKILL.md) e [`refine-spec`](skills/refine-spec/SKILL.md) |
| Implementação e validação | código, testes, evidências de aceite e homologação | [`implement`](skills/implement/SKILL.md), [`test-integration-local`](skills/test-integration-local/SKILL.md) e [`code-review`](skills/code-review/SKILL.md) |
| Documentação e publicação | artefatos atualizados, commit e PR rastreáveis | [`update-docs`](skills/update-docs/SKILL.md), [`commit`](skills/commit/SKILL.md), [`update-pr`](skills/update-pr/SKILL.md) e [`check-pr`](skills/check-pr/SKILL.md) |

`dev-flow` é o orquestrador para uma entrega completa. As decisões de valor, experiência, risco e aprovação continuam com o trio humano; agentes preparam, executam dentro do escopo autorizado e produzem evidências.

## Skills para operar workspaces

Os agentes devem verificar as skills disponíveis no início de cada missão e usar as aplicáveis, declarando os nomes no resultado e no handoff. As skills de base são:

- [`workspace-memory`](skills/workspace-memory/SKILL.md): retomada e registro seguro de memória operacional;
- [`workspace-projects`](skills/workspace-projects/SKILL.md): localização da fonte canônica, atualização de artefatos em `projects/` e organização de assets de sessão em `plans/assets/`;
- [`workspace-board`](skills/workspace-board/SKILL.md): seleção, transição e reconciliação de Work Items com o `BOARD.md`.

As skills de domínio continuam obrigatórias quando se aplicarem à missão: discovery, especificação, implementação, revisão, documentação ou fluxo de desenvolvimento. O [catálogo de agentes](docs/agents/catalog.md) declara, por papel, quais skills são esperadas em cada etapa.

## Estrutura

```text
.
├── docs/         # modelo operacional canônico, catálogo de agentes, workflows e arquitetura
├── workspaces/   # ponto de trabalho do trio: pm/, ux/, tech-lead/
├── skills/       # skills de discovery, engenharia, revisão e publicação
└── scripts/      # automações de apoio
```

- `docs/operating-model.md`: visão canônica do sistema.
- `docs/agents/`: catálogo e contratos executáveis por agente.
- `docs/architecture/`: organização do workspace e fontes de verdade.
- `docs/operations/`: jornada, gates, checkpoints e autonomia.
- `docs/workflows/`: contratos de colaboração multiagente por etapa da jornada.
- `docs/archive/`: materiais históricos preservados para rastreabilidade.
- `workspaces/`: ambientes operacionais reais de PM, UX e Tech Lead.

## Estado do projeto

Este repositório contém um modelo operacional em evolução. Cada documento declara seu estado no front matter:

- `canonical`: referência principal vigente.
- `proposed`: proposta pronta para validação em piloto.
- `reference`: material de apoio à compreensão ou apresentação.
- `archived`: versão histórica, mantida apenas para rastreabilidade — não orienta decisões correntes.

## Princípios de operação

- Contexto, decisões e evidências passam entre fases por artefatos versionados.
- Cada fase tem owner humano, entrada, saída, gate e condição de escalonamento.
- Quem propõe uma mudança não é o único responsável por validá-la.
- Aprovação exige evidência explícita; silêncio não é aprovação.
- A autonomia cresce apenas quando os gates e métricas demonstram segurança.
- Mudanças conceituais são incorporadas primeiro ao modelo canônico e depois propagadas aos documentos especializados.

## Como contribuir

1. Faça um fork e crie uma branch para a mudança.
2. Atualize primeiro a fonte canônica relevante e depois os materiais especializados que ela afeta.
3. Preserve os contratos entre agentes, os gates e os links de navegação.
4. Valide os links e abra um Pull Request descrevendo as evidências da alteração.

## Licença

Este projeto está sob a licença MIT.
