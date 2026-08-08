# Agent Team

Framework operacional para um núcleo humano formado por **Product Manager, UX e Tech Lead** coordenar agentes especializados ao longo de todo o ciclo de desenvolvimento de software.

O projeto reúne princípios, papéis, contratos, gates, fluxos e estruturas de workspace para aumentar a autonomia operacional sem transferir decisões humanas de valor, risco e responsabilidade.

## Comece por aqui

1. Leia o [modelo operacional canônico](docs/operating-model.md).
2. Percorra a [jornada de ponta a ponta](docs/operations/end-to-end-journey.md).
3. Consulte o [catálogo de agentes](docs/agents/catalog.md).
4. Importe os [workspaces dos agentes no OpenClaw](docs/agents/README.md).
5. Aprofunde o [modelo 90/10](docs/operations/operating-model-90-10.md).
6. Use o [índice de documentação](docs/README.md) para os demais materiais.
7. Explore os [workspaces de exemplo de PM, UX e Tech Lead](workspaces/README.md).

## Skills para operar workspaces

Os agentes devem verificar as skills disponíveis no início de cada missão e usar as aplicáveis, declarando os nomes no resultado e no handoff. As skills de base são:

- [`workspace-memory`](../skills/workspace-memory/SKILL.md): retomada e registro seguro de memória operacional;
- [`workspace-projects`](../skills/workspace-projects/SKILL.md): localização da fonte canônica e atualização de artefatos em `projects/`;
- [`workspace-board`](../skills/workspace-board/SKILL.md): seleção, transição e reconciliação de Work Items com o `BOARD.md`.

As skills de domínio continuam obrigatórias quando se aplicarem à missão, como implementação, revisão, documentação ou fluxo de desenvolvimento.

## Estrutura

```text
agent-team/
├── README.md
├── workspaces/
│   ├── pm/
│   ├── ux/
│   └── tech-lead/
└── docs/
    ├── README.md
    ├── operating-model.md
    ├── agents/
    ├── architecture/
    ├── operations/
    ├── workflows/
    └── archive/
```

- `operating-model.md`: visão canônica do sistema.
- `agents/`: catálogo e contratos executáveis.
- `architecture/`: organização do workspace e fontes de verdade.
- `operations/`: jornada, gates, checkpoints e autonomia.
- `workflows/`: contratos de colaboração multiagente por etapa da jornada.
- `archive/`: materiais históricos preservados para rastreabilidade.
- `workspaces/`: exemplos concretos dos ambientes operacionais de cada papel.

## Estado do projeto

Este repositório contém uma proposta operacional em evolução. Cada documento declara seu estado no front matter:

- `canonical`: referência principal vigente.
- `proposed`: proposta pronta para validação em piloto.
- `reference`: material de apoio à compreensão ou apresentação.
- `archived`: versão histórica, mantida apenas para rastreabilidade.

## Princípio de manutenção

Mudanças conceituais devem ser incorporadas primeiro ao modelo canônico e depois propagadas aos documentos especializados. Conteúdo histórico não deve voltar a orientar decisões sem ser promovido explicitamente.
