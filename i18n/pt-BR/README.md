# Agent-Team

**Agent-Team** é um manifesto: um conjunto de documentos que descreve, de forma completa e verificável, como um time de agentes de IA pode colaborar na construção de software — do intake de uma ideia até a operação em produção — com pontos de decisão humana bem definidos.

Este repositório não contém uma aplicação para instalar ou rodar. Ele contém **a especificação de um método de trabalho**: papéis, procedimentos, ordens de execução e regras de governança, todos versionados como texto para que tanto pessoas quanto agentes consigam lê-los e segui-los sem ambiguidade.

Se esta é a sua primeira visita, pense neste README como uma introdução guiada. Ele explica a ideia central do projeto, como o conteúdo está organizado e por onde começar a leitura — sem exigir que você já conheça o vocabulário do resto da documentação.

---

## Experiência interativa

Abra [`index.html`](index.html) para explorar a documentação em uma interface dark, com busca global, navegação por drilldown e uma pirâmide interativa das seis camadas. O arquivo funciona localmente, sem servidor.

O HTML é gerado a partir dos Markdown vigentes — nunca editado como uma fonte paralela:

```bash
uv run scripts/build-docs-site.py
```

---

## A ideia central: uma pirâmide de seis camadas

O método é organizado em seis camadas, do mais concreto ao mais abstrato. Cada camada responde a uma pergunta diferente e depende da camada anterior já existir — pular uma delas é, segundo o próprio manifesto, o que produz documentação que ninguém consegue executar de fato.

| # | Camada | Pergunta que responde | Documento principal |
|---|---|---|---|
| 1 | **Harness** | O que o repositório da aplicação precisa carregar para ser operado por agentes? | [`docs/REPO_HARNESS.md`](docs/REPO_HARNESS.md) |
| 2 | **Skills** | *Como* uma tarefa recorrente deve ser executada corretamente? | [`docs/SKILLS.md`](docs/SKILLS.md) |
| 3 | **Agentes** | *Quem* executa cada tarefa, sob qual autoridade e com qual limite? | [`docs/AGENTES.md`](docs/AGENTES.md) |
| 4 | **Loops** | *Em que ordem* os agentes colaboram, e quando parar? | [`docs/LOOPS.md`](docs/LOOPS.md) |
| 5 | **Metodologia** | *Quem opera* o sistema no dia a dia, e o que exige uma pessoa? | [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) |
| 6 | **Workspace** | *Onde* cada artefato de uma execução vive, fora do código? | [`docs/WORKSPACE.md`](docs/WORKSPACE.md) |

Uma forma simples de entender a relação entre as camadas: o **harness** é o que torna um repositório legível para um agente; as **skills** são as receitas que impedem que um procedimento recorrente seja reinventado a cada tarefa; os **agentes** são quem faz o trabalho dentro desse repositório, seguindo essas receitas; os **loops** definem a ordem de uma etapa da jornada, do intake ao deploy; a **metodologia** explica o que uma pessoa precisa decidir ao longo desse caminho; e o **workspace** é o lugar, fora do código, onde as decisões e artefatos de cada execução ficam guardados.

---

## Estrutura do repositório

```text
ai-manifest/
├── README.md # este arquivo
├── docs/ # a documentação do método — comece por aqui
│ ├── README.md # índice completo da pirâmide, com trilhas de leitura
│ ├── REPO_HARNESS.md # camada 1 — harness do repositório
│ ├── PERMISSIONS.md # o que o agente pode invocar e o que exige uma pessoa
│ ├── TOOLS.md # índice de ferramentas e onde cada check roda
│ ├── MCPS.md # servidores MCP e escopos autorizados
│ ├── SKILLS.md # camada 2 — catálogo de procedimentos
│ ├── RULES.md # estado desejado do repositório e AGENTS.md
│ ├── SENSORS.md # verificações locais (pre-commit, pre-push)
│ ├── GATES.md # verificação do commit ao deploy, níveis de autonomia
│ ├── DOCUMENTATION.md # ADRs, evidence pack, identidade e proveniência
│ ├── TRUST.md # conteúdo não confiável, injeção, exfiltração
│ ├── FAILURE.md # o gate que não rodou e como detectá-lo
│ ├── CONCURRENCY.md # vários agentes simultâneos, frescor de evidência
│ ├── BUDGET.md # custo, turnos, contexto e o que degrada
│ ├── VERSIONING.md # o harness tem versões, e elas invalidam
│ ├── METRICS.md # métricas equilibradas da squad para a era da IA
│ ├── MATURITY.md # maturidade do oportunista ao adaptativo
│ ├── AGENTES.md # camada 3 — como um agente funciona
│ ├── agentes/ # os 23 contratos individuais de agentes
│ ├── LOOPS.md # camada 4 — como as etapas da jornada se coordenam
│ ├── loops/ # os 12 contratos de etapa, do intake à operação diária
│ ├── METODOLOGIA.md # camada 5 — como uma pessoa opera o sistema
│ ├── metodologia/ # as sete páginas operacionais
│ ├── WORKSPACE.md # camada 6 — onde o trabalho vive fora do código
│ └── workspace/ # as quatro páginas operacionais
├── agents/ # os prompts executáveis de cada agente (AGENT.md)
├── skills/ # os procedimentos executáveis (SKILL.md)
├── workflows/ # a versão executável dos loops
├── templates/ # modelos usados por PM, UX e Tech Lead
├── workspaces/ # exemplos de workspace para os três papéis
├── i18n/ # traduções: espelho pt-BR, strings de interface e glossário
└── scripts/ # utilitários de apoio à documentação
```

A documentação é publicada em inglês e português brasileiro a partir deste mesmo branch. O texto canônico é a árvore acima; o `i18n/pt-BR/` espelha os mesmos caminhos, e o [`i18n/README.md`](i18n/README.md) é o contrato para manter os dois em sincronia.

A regra prática para se orientar: **`docs/` explica o conceito e o porquê; as pastas irmãs (`agents/`, `skills/`, `workflows/`, `templates/`, `workspaces/`) contêm a versão executável daquilo que `docs/` descreve.** Ler um documento de conceito antes do artefato correspondente evita aplicar um procedimento sem entender a razão por trás dele.

---

## Por onde começar

A documentação completa, com o índice detalhado de cada camada e trilhas de leitura por perfil, está em **[`docs/README.md`](docs/README.md)**. A tabela abaixo é um atalho para os objetivos mais comuns.

| Se você quer… | Comece por… |
|---|---|
| Entender a ideia do projeto em conjunto | [`docs/README.md`](docs/README.md) |
| Preparar um repositório de aplicação para ser operado por agentes | [Harness](docs/REPO_HARNESS.md) → [Permissões](docs/PERMISSIONS.md) → [Tools](docs/TOOLS.md) → [Skills](docs/SKILLS.md) → [Rules](docs/RULES.md) → [Sensors](docs/SENSORS.md) → [Gates](docs/GATES.md) |
| Avaliar o perfil de maturidade da squad e escolher a próxima melhoria | [Maturidade](docs/MATURITY.md) → [Métricas](docs/METRICS.md) |
| Operar agentes em produção, em volume | [Confiança](docs/TRUST.md) → [Falha](docs/FAILURE.md) → [Concorrência](docs/CONCURRENCY.md) → [Orçamento](docs/BUDGET.md) |
| Conhecer o catálogo de agentes e o que cada um faz | [`docs/AGENTES.md`](docs/AGENTES.md) → [contratos individuais](docs/agentes/README.md) |
| Ver a jornada completa, do intake ao deploy | [`docs/LOOPS.md`](docs/LOOPS.md) → [as 12 etapas](docs/loops/README.md) |
| Saber o que cabe a uma pessoa decidir, na prática | [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) → [manual do operador](docs/metodologia/05-manual-do-operador.md) |
| Saber onde cada artefato de uma execução deve ser salvo | [`docs/WORKSPACE.md`](docs/WORKSPACE.md) → [estrutura do workspace](docs/workspace/01-estrutura-do-workspace.md) |

---

## Conceitos essenciais, em linguagem simples

Estes cinco conceitos aparecem em quase todos os documentos do repositório. Vale fixá-los antes de seguir para o material completo.

**Skill.** O procedimento verificável para uma tarefa recorrente que exige julgamento — por exemplo, como investigar um bug ou como escrever uma especificação técnica. Uma skill é diferente de um script porque cobre o que exige critério, não apenas o determinístico.

**Agente.** Um processo com missão delimitada: recebe um objetivo, lê o contexto necessário, age dentro de ferramentas autorizadas, submete o resultado a uma verificação objetiva e devolve um relatório padronizado. Um nome bonito em um diagrama não é um agente — só vira um quando essas cinco partes estão definidas.

**Loop.** O contrato de colaboração de uma etapa da jornada: quem participa, em que ordem, o que passa de um agente para o outro e o que precisa ser verdade para seguir adiante. O nome "loop", em vez de "workflow", é proposital — o trabalho gira (tenta, é corrigido, é contestado, converge) em vez de andar em linha reta.

**Metodologia.** A camada que explica o que uma pessoa faz de fato: quando ela é chamada para decidir, o que precisa ver para responder, e o que acontece se ela não responder. Cinco compromissos sustentam essa camada — entre eles, o mais estrutural: **quem propõe não aprova**.

**Workspace.** O lugar físico, fora do código da aplicação, onde um Work Item é aberto, uma decisão vira artefato e um agente retoma o contexto de uma sessão anterior. Existe um workspace por papel — PM, UX e Tech Lead — cada um com sua própria fonte canônica de verdade.

---

## Maturidade no desenvolvimento de software na era da IA

Maturidade é a capacidade da squad transformar um problema real em um outcome de produto mensurável de forma repetível, segura e sustentável. Adoção de IA isolada não é maturidade: sem outcomes claros, lotes pequenos, engenharia confiável, contexto acessível e governança, ela apenas amplifica o sistema ao redor.

| Nível | A squad opera como |
|---|---|
| **M0 — Oportunista** | uso individual de IA, conhecimento implícito e nenhuma baseline comparável |
| **M1 — Assistido** | IA supervisionada sobre trabalho visível, versionado e verificado no nível básico |
| **M2 — Padronizado** | procedimentos compartilhados, contexto reutilizável, lotes pequenos e dados comparáveis |
| **M3 — Integrado** | um fluxo rastreável da decisão de produto ao outcome em produção |
| **M4 — Autonomia governada** | trabalho delegado e reversível dentro de políticas explícitas e com evidências |
| **M5 — Adaptativo** | melhoria contínua do sistema humano-IA por experimentos controlados |

A avaliação multidimensional completa está em [`docs/MATURITY.md`](docs/MATURITY.md), e o dashboard equilibrado da squad — incluindo implantações, implantações com falha, fluxo, qualidade, produto, colaboração com IA, economia e saúde da equipe — está em [`docs/METRICS.md`](docs/METRICS.md). A verificação do repositório ainda impõe um teto separado à autonomia dos agentes; esse controle especializado está descrito em [`docs/GATES.md`](docs/GATES.md).

---

## Como este repositório evolui

Cada camada tem seu próprio checklist de mudança, versionamento explícito e critério de avaliação — nunca usados como ranking de desempenho individual, apenas para melhorar o contrato, o contexto e as ferramentas de cada papel. Antes de propor uma alteração relevante em uma camada, vale ler o documento correspondente até o fim: cada um termina com o checklist e as regras de versionamento que se aplicam a mudanças naquela camada específica.

Para o mapa completo, com todos os documentos e as trilhas de leitura por perfil, veja **[`docs/README.md`](docs/README.md)**.
