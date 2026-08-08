# AI Manifest

Repositório para operar squads AI-first com um processo orientado a evidências. Ele reúne dois componentes complementares:

- [**Agent Team**](agent-team/README.md): sistema operacional para um trio humano — Product Manager, UX e Tech Lead — coordenar agentes especializados, automações, decisões e gates;
- [**Skills**](skills/): instruções executáveis que transformam discovery, especificação, implementação, validação e publicação em trabalho repetível.

## Comece por aqui

1. Leia o [modelo operacional canônico](agent-team/docs/operating-model.md) para entender papéis, direitos de decisão e limites de autonomia.
2. Consulte a [jornada de ponta a ponta](agent-team/docs/operations/end-to-end-journey.md) para ver os gates, os artefatos e a passagem de contexto entre as fases.
3. Use o [catálogo de agentes](agent-team/docs/agents/catalog.md) e os [workspaces importáveis](agent-team/docs/agents/README.md) para materializar os papéis especializados.
4. Escolha as skills aplicáveis em [`skills/`](skills/); cada `SKILL.md` define contexto, entradas, saída e critérios de qualidade.

O [índice completo do Agent Team](agent-team/docs/README.md) organiza os documentos canônicos, propostos e históricos. Os exemplos de ambiente de trabalho para PM, UX e Tech Lead ficam em [workspaces](agent-team/workspaces/README.md).

## Fluxo de trabalho

O fluxo Spec Driven Development é agora mantido pelos documentos e skills canônicos, em vez de um guia monolítico:

| Fase | Resultado esperado | Referência principal |
|---|---|---|
| Descoberta | problema, requisitos, regras, cenários, métricas e lacunas explícitas | [`business-discovery`](skills/business-discovery/SKILL.md) |
| Produto e UX | objetivo, escopo, jornada e critérios de aceite observáveis | [jornada operacional](agent-team/docs/operations/end-to-end-journey.md) |
| Especificação técnica | opções, riscos, plano técnico e contratos verificáveis | [`technical-discovery`](skills/technical-discovery/SKILL.md), [`create-spec`](skills/create-spec/SKILL.md) e [`review-spec`](skills/review-spec/SKILL.md) |
| Planejamento | coerência entre produto e técnica e uma sequência de execução | [`review-cross-prd-spec`](skills/review-cross-prd-spec/SKILL.md) e [`refine-spec`](skills/refine-spec/SKILL.md) |
| Implementação e validação | código, testes, evidências de aceite e homologação | [`implement`](skills/implement/SKILL.md), [`test-integration-local`](skills/test-integration-local/SKILL.md) e [`code-review`](skills/code-review/SKILL.md) |
| Documentação e publicação | artefatos atualizados, commit e PR rastreáveis | [`update-docs`](skills/update-docs/SKILL.md), [`commit`](skills/commit/SKILL.md), [`update-pr`](skills/update-pr/SKILL.md) e [`check-pr`](skills/check-pr/SKILL.md) |

`dev-flow` é o orquestrador para uma entrega completa. As decisões de valor, experiência, risco e aprovação continuam com o trio humano; agentes preparam, executam dentro do escopo autorizado e produzem evidências.

## Estrutura

```text
.
├── agent-team/  # modelo operacional, catálogo de agentes e workspaces
├── skills/      # skills de discovery, engenharia, revisão e publicação
└── scripts/     # automações de apoio
```

## Princípios de operação

- Contexto, decisões e evidências passam entre fases por artefatos versionados.
- Cada fase tem owner humano, entrada, saída, gate e condição de escalonamento.
- Quem propõe uma mudança não é o único responsável por validá-la.
- Aprovação exige evidência explícita; silêncio não é aprovação.
- A autonomia cresce apenas quando os gates e métricas demonstram segurança.

## Como contribuir

1. Faça um fork e crie uma branch para a mudança.
2. Atualize primeiro a fonte canônica relevante e depois os materiais especializados que ela afeta.
3. Preserve os contratos entre agentes, os gates e os links de navegação.
4. Valide os links e abra um Pull Request descrevendo as evidências da alteração.

## Licença

Este projeto está sob a licença MIT.
