# Agent Team

> Framework operacional para um núcleo humano de **Product Manager, UX e Tech Lead** dirigir agentes especializados ao longo de todo o ciclo de desenvolvimento de software.

## Em 2 minutos

Times pequenos que adotam agentes de IA costumam esbarrar no mesmo limite: a geração de código deixa de ser o gargalo, e o gargalo passa a ser decidir o que construir, garantir que foi construído certo e manter decisões, código e documentação sincronizados. O Agent Team existe para resolver esse segundo problema.

A proposta é tratar o desenvolvimento como um sistema operado por três pessoas, e não executado por elas. O trio humano define intenção, prioridade, risco e aprovação; agentes especializados pesquisam, especificam, implementam, criticam, validam e documentam dentro de escopo autorizado. Entre uma fase e outra, o contexto não passa por conversa: passa por **artefatos versionados** com owner, gate e evidência.

| Peça | O que é | Onde vive |
|---|---|---|
| **Harness do repositório** | O que um repositório precisa carregar para ser operado por agentes com segurança | [`docs/REPO_HARNESS.md`](docs/REPO_HARNESS.md) |
| **Agentes** | 23 papéis com identidade, contrato, permissões e skills esperadas — e os prompts prontos para uso | [`docs/AGENTES.md`](docs/AGENTES.md) e [`agents/`](agents/catalog.md) |
| **Skills** | Procedimentos repetíveis de discovery, especificação, implementação e publicação | [`skills/`](skills/README.md) |
| **Loops** | Contrato de colaboração multiagente em cada uma das 12 etapas da jornada | [`docs/LOOPS.md`](docs/LOOPS.md) e [`workflows/`](workflows/README.md) |
| **Metodologia** | Papéis, checkpoints humanos, gatilhos e ritmos de quem opera o sistema | [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) |
| **Workspaces** | Onde PM, UX e Tech Lead efetivamente pilotam o fluxo | [`workspaces/`](workspaces/README.md) e [`docs/WORKSPACE.md`](docs/WORKSPACE.md) |

Três ideias sustentam o resto: quem propõe uma mudança não é quem a aprova; aprovação exige evidência explícita, nunca silêncio; e autonomia só cresce quando gates e métricas demonstram que é seguro.

---

## Por onde começar

Escolha a trilha pelo tempo que você tem agora.

| Você quer… | Leia | Tempo |
|---|---|---|
| Entender a proposta e decidir se vale investigar | esta seção e o [índice da documentação](docs/README.md) | 5 min |
| Ver o fluxo de ponta a ponta em diagrama | [jornada comentada](docs/metodologia/06-jornada-comentada.md) | 10 min |
| Entender papéis, decisões e limites de autonomia | [metodologia](docs/METODOLOGIA.md) e [gates](docs/GATES.md) | 25 min |
| Executar uma etapa específica com agentes | o [workflow](workflows/README.md) correspondente | 5 min por etapa |
| Montar seus próprios agentes | [catálogo](docs/AGENTES.md) e [prompts prontos](agents/README.md) | 30 min |
| Saber qual procedimento roda em cada etapa | [catálogo de skills](skills/README.md) | 15 min |
| Preparar um repositório para ser operado por agentes | [repo harness](docs/REPO_HARNESS.md) | 20 min |
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
| Intake e triagem | necessidade registrada, deduplicada e priorizada | [`00`](workflows/00-intake-and-triage.md) |
| Descoberta | problema, requisitos, regras, cenários, métricas e lacunas explícitas | [`01`](workflows/01-discovery-and-research.md) · [`business-discovery`](skills/business-discovery/SKILL.md) |
| Produto e UX | objetivo, escopo, jornada e critérios de aceite observáveis | [`02`](workflows/02-product-and-ux-planning.md) |
| Especificação técnica | opções, riscos, plano técnico e contratos verificáveis | [`03`](workflows/03-technical-specification.md) · [`create-spec`](skills/create-spec/SKILL.md) |
| Implementação | código e testes dentro do escopo autorizado | [`04`](workflows/04-autonomous-implementation.md) · [`implement`](skills/implement/SKILL.md) |
| Validação adversarial | falhas encontradas por instância independente | [`05`](workflows/05-adversarial-validation.md) · [`code-review`](skills/code-review/SKILL.md) |
| PR e merge | mudança rastreável, revisada e integrada | [`06`](workflows/06-pr-and-merge.md) · [`update-pr`](skills/update-pr/SKILL.md) |
| Homologação | evidência de aceite antes da exposição | [`07`](workflows/07-release-candidate-validation.md) |
| Entrega e observação | rollout observado, com rollback pronto | [`08`](workflows/08-production-release-and-observation.md) |
| Conhecimento | base atualizada e aprendizado registrado | [`09`](workflows/09-knowledge-curation.md) · [`update-docs`](skills/update-docs/SKILL.md) |
| Melhoria contínua | telemetria convertida em demanda priorizada | [`10`](workflows/10-continuous-improvement.md) |
| Operação diária | briefing do dia anterior convertido em decisão, memória e melhoria | [`11`](workflows/11-daily-operations.md) |

A skill [`dev-flow`](skills/dev-flow/SKILL.md) orquestra uma entrega completa quando o item não exige condução manual fase a fase.

### O workspace é o ponto de trabalho

`workspaces/<pm|ux|tech-lead>/` não é material de referência: é onde cada papel humano e seus agentes rodam o fluxo de verdade. Cada workspace mantém `AGENTS.md` (como operar), `BOARD.md` (Work Items em andamento), `memory.md` (retomada de contexto) e `projects/<project>/` (artefatos reais de cada iniciativa).

Ao iniciar uma missão, o agente lê o `AGENTS.md` do workspace, identifica as skills aplicáveis e segue a estrutura de `projects/` em vez de inventar convenções próprias. Três skills sustentam essa operação:

| Skill | Garante |
|---|---|
| [`workspace-memory`](skills/workspace-memory/SKILL.md) | retomada e registro seguro de memória operacional |
| [`workspace-projects`](skills/workspace-projects/SKILL.md) | fonte canônica correta e assets de sessão isolados em `plans/assets/` |
| [`workspace-board`](skills/workspace-board/SKILL.md) | seleção, transição e reconciliação de Work Items |

As skills de domínio continuam obrigatórias quando se aplicam à missão. O agente declara no resultado e no handoff quais skills usou — o [catálogo](docs/AGENTES.md) define, por papel, quais são esperadas em cada etapa.

---

## Estrutura do repositório

```text
.
├── docs/
│   ├── REPO_HARNESS.md    # o que um repositório precisa carregar para ser operável por agentes
│   ├── AGENTES.md         # quem executa, sob qual autoridade e com qual limite
│   ├── SKILLS.md          # como uma tarefa recorrente é executada corretamente
│   ├── LOOPS.md           # em que ordem os agentes colaboram e quando parar
│   ├── METODOLOGIA.md     # quem opera, o que dispara o quê e o que exige gente
│   ├── WORKSPACE.md       # onde cada artefato de uma execução vive, fora do código
│   ├── GATES.md · RULES.md · TOOLS.md · SENSORS.md · MCPS.md · DOCUMENTATION.md
│   ├── agentes/ · loops/ · metodologia/ · workspace/   # páginas operacionais de cada camada
│   └── README.md          # a pirâmide completa e por onde começar
├── agents/            # 23 prompts executáveis (AGENT.md por papel), catálogo e registro
├── workflows/         # 12 blocos executáveis: contrato de colaboração multiagente por etapa
├── workspaces/        # ponto de trabalho do trio: pm/, ux/, tech-lead/
├── skills/            # 22 procedimentos: discovery, engenharia, revisão e publicação
│   ├── README.md      # catálogo por etapa da jornada
│   └── <skill>/       # SKILL.md com entrada, passos, saída e critério de conclusão
├── templates/         # templates de artefato por papel: pm/, tech-lead/, ux/
└── scripts/           # automações de apoio, incluindo geradores de documentação
```

---

## Estado do projeto

Este é um modelo operacional em evolução. Todo documento canônico declara `title`, `status` e `updated_at` no front matter — a ausência de `status` faz o agente tratar o documento como `proposed`, o comportamento seguro.

| Estado | Significado | O agente pode |
|---|---|---|
| `proposed` | escrito, ainda não aceito como referência | ler como contexto, nunca como regra |
| `canonical` | é a referência vigente para o tema | seguir sem confirmação |
| `superseded` | substituído por outro documento | ler para entender o histórico; nunca seguir |
| `archived` | não se aplica mais e não foi substituído | ignorar, salvo investigação histórica |

Um documento `superseded` nunca é apagado: ele aponta para quem o substituiu, o que preserva o porquê de uma decisão. Detalhe completo em [Workflows de documentação](docs/metodologia/07-workflows-de-documentacao.md).

---

## Como contribuir

1. Faça um fork e crie uma branch para a mudança.
2. Atualize primeiro a fonte canônica relevante e depois os materiais especializados que ela afeta.
3. Preserve os contratos entre agentes, os gates e os links de navegação.
4. Siga o [padrão de escrita](docs/metodologia/07-workflows-de-documentacao.md#o-padrão-de-escrita) — em especial as duas camadas e os limites de formatação.
5. Valide os links e abra um Pull Request descrevendo as evidências da alteração.

## Licença

Este projeto está sob a licença MIT.
