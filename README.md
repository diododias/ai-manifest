# Agent Team

> Framework operacional para um núcleo humano de **Product Manager, UX e Tech Lead** dirigir agentes especializados ao longo de todo o ciclo de desenvolvimento de software.

## Em 2 minutos

Times pequenos que adotam agentes de IA costumam esbarrar no mesmo limite: a geração de código deixa de ser o gargalo, e o gargalo passa a ser decidir o que construir, garantir que foi construído certo e manter decisões, código e documentação sincronizados. O Agent Team existe para resolver esse segundo problema.

A proposta é tratar o desenvolvimento como um sistema operado por três pessoas, e não executado por elas. O trio humano define intenção, prioridade, risco e aprovação; agentes especializados pesquisam, especificam, implementam, criticam, validam e documentam dentro de escopo autorizado. Entre uma fase e outra, o contexto não passa por conversa: passa por **artefatos versionados** com owner, gate e evidência.

| Peça | O que é | Onde vive |
|---|---|---|
| **Modelo operacional** | Papéis, direitos de decisão, gates e níveis de autonomia | [`docs/operating-model.md`](docs/operating-model.md) |
| **Workflows** | Contrato de colaboração multiagente em cada uma das 11 etapas da jornada | [`docs/workflows/`](docs/workflows/README.md) |
| **Agentes** | 23 papéis com identidade, contrato, permissões e skills esperadas | [`docs/agents/`](docs/agents/catalog.md) |
| **Skills** | Procedimentos repetíveis de discovery, especificação, implementação e publicação | [`skills/`](skills/README.md) |
| **Repo harness** | O que um repositório precisa ter para ser operado por agentes com segurança | [`docs/repo-harness.md`](docs/repo-harness.md) |
| **Workspaces** | Onde PM, UX e Tech Lead efetivamente pilotam o fluxo | [`workspaces/`](workspaces/README.md) |

Três ideias sustentam o resto: quem propõe uma mudança não é quem a aprova; aprovação exige evidência explícita, nunca silêncio; e autonomia só cresce quando gates e métricas demonstram que é seguro.

---

## Por onde começar

Escolha a trilha pelo tempo que você tem agora.

| Você quer… | Leia | Tempo |
|---|---|---|
| Entender a proposta e decidir se vale investigar | esta seção e o [índice da documentação](docs/README.md) | 5 min |
| Ver o fluxo de ponta a ponta em diagrama | [fluxo da jornada](docs/end-to-end-journey.md) | 10 min |
| Entender papéis, decisões e limites de autonomia | [modelo operacional](docs/operating-model.md) | 25 min |
| Executar uma etapa específica com agentes | o [workflow](docs/workflows/README.md) correspondente | 5 min por etapa |
| Montar seus próprios agentes | [catálogo](docs/agents/catalog.md) e [pacotes importáveis](docs/agents/README.md) | 30 min |
| Saber qual procedimento roda em cada etapa | [catálogo de skills](skills/README.md) | 15 min |
| Preparar um repositório para ser operado por agentes | [repo harness](docs/repo-harness.md) | 20 min |
| Copiar a estrutura de trabalho para o seu time | [workspaces de exemplo](workspaces/README.md) | 20 min |

---

## Como o sistema funciona

### O trio dirige, os agentes executam

Cada domínio tem um dono humano inequívoco, e essa separação é o que permite delegar sem perder controle.

| Papel | Dirige | Decide sozinho |
|---|---|---|
| **Product Manager** | Valor, prioridade, requisitos e outcome | prioridade, escopo e aceite de produto |
| **UX** | Evidência sobre o usuário, jornada e qualidade de uso | experiência, acessibilidade e aceite de UX |
| **Tech Lead** | Viabilidade, arquitetura, qualidade técnica e risco | arquitetura, exceções técnicas, merge e release |

Os agentes não decidem: eles preparam a decisão. Um agente primário conduz e consolida o artefato da fase, agentes adversariais procuram ambiguidade, risco e suposição frágil, e o owner humano resolve as divergências que sobram.

### A jornada tem gates, não etapas soltas

Cada fase declara entrada, saída, owner e critério de passagem. Um item só avança quando o gate anterior produziu evidência.

| Fase | Resultado esperado | Referência |
|---|---|---|
| Intake e triagem | necessidade registrada, deduplicada e priorizada | [`00`](docs/workflows/00-intake-and-triage.md) |
| Descoberta | problema, requisitos, regras, cenários, métricas e lacunas explícitas | [`01`](docs/workflows/01-discovery-and-research.md) · [`business-discovery`](skills/business-discovery/SKILL.md) |
| Produto e UX | objetivo, escopo, jornada e critérios de aceite observáveis | [`02`](docs/workflows/02-product-and-ux-planning.md) |
| Especificação técnica | opções, riscos, plano técnico e contratos verificáveis | [`03`](docs/workflows/03-technical-specification.md) · [`create-spec`](skills/create-spec/SKILL.md) |
| Implementação | código e testes dentro do escopo autorizado | [`04`](docs/workflows/04-autonomous-implementation.md) · [`implement`](skills/implement/SKILL.md) |
| Validação adversarial | falhas encontradas por instância independente | [`05`](docs/workflows/05-adversarial-validation.md) · [`code-review`](skills/code-review/SKILL.md) |
| PR e merge | mudança rastreável, revisada e integrada | [`06`](docs/workflows/06-pr-and-merge.md) · [`update-pr`](skills/update-pr/SKILL.md) |
| Homologação | evidência de aceite antes da exposição | [`07`](docs/workflows/07-release-candidate-validation.md) |
| Entrega e observação | rollout observado, com rollback pronto | [`08`](docs/workflows/08-production-release-and-observation.md) |
| Conhecimento | base atualizada e aprendizado registrado | [`09`](docs/workflows/09-knowledge-curation.md) · [`update-docs`](skills/update-docs/SKILL.md) |
| Melhoria contínua | telemetria convertida em demanda priorizada | [`10`](docs/workflows/10-continuous-improvement.md) |

A skill [`dev-flow`](skills/dev-flow/SKILL.md) orquestra uma entrega completa quando o item não exige condução manual fase a fase.

### O workspace é o ponto de trabalho

`workspaces/<pm|ux|tech-lead>/` não é material de referência: é onde cada papel humano e seus agentes rodam o fluxo de verdade. Cada workspace mantém `AGENTS.md` (como operar), `BOARD.md` (Work Items em andamento), `memory.md` (retomada de contexto) e `projects/<project>/` (artefatos reais de cada iniciativa).

Ao iniciar uma missão, o agente lê o `AGENTS.md` do workspace, identifica as skills aplicáveis e segue a estrutura de `projects/` em vez de inventar convenções próprias. Três skills sustentam essa operação:

| Skill | Garante |
|---|---|
| [`workspace-memory`](skills/workspace-memory/SKILL.md) | retomada e registro seguro de memória operacional |
| [`workspace-projects`](skills/workspace-projects/SKILL.md) | fonte canônica correta e assets de sessão isolados em `plans/assets/` |
| [`workspace-board`](skills/workspace-board/SKILL.md) | seleção, transição e reconciliação de Work Items |

As skills de domínio continuam obrigatórias quando se aplicam à missão. O agente declara no resultado e no handoff quais skills usou — o [catálogo](docs/agents/catalog.md) define, por papel, quais são esperadas em cada etapa.

---

## Estrutura do repositório

```text
.
├── docs/
│   ├── operating-model.md         # fonte canônica: papéis, decisões e ciclo
│   ├── operating-model-90-10.md   # gates, risco e autonomia progressiva
│   ├── repo-harness.md            # o contrato executável de um repositório
│   ├── end-to-end-journey.md      # a jornada completa em um diagrama
│   ├── journey-by-phase.md        # a mesma jornada, um bloco por vez
│   ├── documentation-standard.md  # como escrever documentação aqui
│   ├── site.html                  # documentação navegável em página única
│   ├── agents/                    # catálogo e pacotes executáveis por agente
│   ├── workflows/                 # contratos de colaboração multiagente por etapa
│   └── diagrams/                  # organização do workspace e fontes de verdade
├── workspaces/        # ponto de trabalho do trio: pm/, ux/, tech-lead/
├── skills/            # 22 procedimentos: discovery, engenharia, revisão e publicação
│   ├── README.md      # catálogo por etapa da jornada
│   └── <skill>/       # SKILL.md com entrada, passos, saída e critério de conclusão
└── scripts/           # automações de apoio, incluindo o gerador de docs/site.html
```

---

## Estado do projeto

Este é um modelo operacional em evolução. Cada documento declara seu estado no front matter, e o estado define o peso que ele tem em uma decisão.

| Estado | Significado |
|---|---|
| `canonical` | referência principal vigente |
| `proposed` | proposta pronta para validação em piloto |
| `reference` | material de apoio à compreensão ou apresentação |

O repositório documenta apenas o fluxo vigente. Não há estado `archived` nem pasta de material histórico: o que deixa de valer é removido no mesmo PR que o substitui, e o histórico fica no Git.

---

## Como contribuir

1. Faça um fork e crie uma branch para a mudança.
2. Atualize primeiro a fonte canônica relevante e depois os materiais especializados que ela afeta.
3. Preserve os contratos entre agentes, os gates e os links de navegação.
4. Siga o [padrão de documentação](docs/documentation-standard.md) — em especial as duas camadas e os limites de formatação.
5. Valide os links e abra um Pull Request descrevendo as evidências da alteração.

## Licença

Este projeto está sob a licença MIT.
