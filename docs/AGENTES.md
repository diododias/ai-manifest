# 2. Agentes

---

## Overview — How Agents Work

Um agente é um processo que recebe uma missão delimitada, lê um contexto versionado, executa trabalho autorizado com ferramentas declaradas, submete o resultado a verificações objetivas e devolve um envelope padronizado ao owner humano. Nenhuma dessas cinco etapas é opcional, e é a combinação delas — não a capacidade do modelo — que determina se o agente é confiável.

O ponto de partida é uma observação simples: **um nome em um diagrama não é um papel**. "Security Review Agent" é apenas um rótulo até que se defina o que ele lê, o que entrega, qual gate precisa satisfazer e em que condição para e escala. O catálogo de agentes existe para converter rótulos em papéis operacionais inequívocos, de modo que uma missão possa ser despachada sem negociação prévia sobre responsabilidade, escopo ou critério de conclusão.

### Anatomia de um agente — o que ele consome

Um agente não carrega conhecimento próprio sobre o repositório. Tudo o que ele sabe vem de camadas versionadas que o [repo harness](REPO_HARNESS.md) disponibiliza. Cada camada responde a uma pergunta distinta, e a ausência de qualquer uma delas produz uma classe específica de falha.

| Insumo | Responde | Onde vive | Se faltar |
|---|---|---|---|
| **Rules** | qual é o estado desejado e por quê | [`docs/rules/`](RULES.md), `AGENTS.md` | o agente escolhe uma convenção plausível e diverge do repositório |
| **Skills** | como executar uma tarefa recorrente do jeito certo | [`skills/<skill>/SKILL.md`](SKILLS.md) | o procedimento é reinventado a cada execução, com resultado instável |
| **Tools** | o que pode invocar e com que limite | [`.agent/settings.json`](TOOLS.md) | qualquer ação parece autorizada |
| **MCPs** | como alcançar sistemas externos e sob qual escopo | [`.agent/mcps.json`](MCPS.md) | efeitos externos ocorrem antes que o gate local detecte |
| **Sensors** | o que precisa passar antes de o código sair da máquina | [`.hooks/`](SENSORS.md) | o erro barato só aparece no CI, uma volta inteira depois |
| **Gates** | o que precisa ser verdade para avançar de etapa | [CI, merge, ambiente, pós-deploy](GATES.md) | o julgamento de "pronto" fica com quem produziu |
| **Evidência** | como provar depois que estava correto | [`docs/evidence/<work-item>/`](DOCUMENTATION.md) | a aprovação se baseia no resumo do agente, não em fatos |
| **Memória** | o que já foi decidido em sessões anteriores | `workspace-memory`, `MEMORY.md` | o contexto é reconstruído por suposição a cada sessão |

Vale explicitar a distinção mais confundida do conjunto. **Rule descreve estado desejado; skill descreve procedimento.** "Módulos de domínio não importam de infraestrutura" é rule. "Para adicionar um adapter, crie a interface em X e a implementação em Y" é skill. Tratar uma como a outra produz rules longas que ninguém lê e skills vagas que não se consegue executar.

### O ciclo de execução de uma missão

Toda execução — de qualquer papel, em qualquer fase — percorre a mesma sequência.

**1. Identidade da missão.** O agente recebe um bloco de identidade completo. A ausência de qualquer campo é, na prática, uma autorização em branco, e por isso uma missão incompleta não deve ser executada.

| Bloco | Campos |
|---|---|
| Identificação | `mission_id`, `work_item_id` (quando houver), fase do workflow, papel do agente |
| Autoridade | sponsor humano (PM, UX ou Tech Lead), owner da decisão |
| Direção | objetivo e resultado esperado, escopo e fora de escopo |
| Fontes | fontes canônicas, artefatos de entrada e de saída |
| Verificação | critérios de aceite e gates |
| Limites | risco e autonomia autorizada, tools, permissões e budget |
| Parada | condição de parada e escalonamento |

**2. Leitura de contexto.** O agente lê `AGENTS.md`, as rules aplicáveis à tarefa, os ADRs relevantes e a memória do workspace. A leitura é sob demanda: rules não são carregadas inteiras a cada execução, porque contexto é o recurso mais escasso de uma sessão.

**3. Verificação de skills.** Antes de agir, o agente inventaria as skills disponíveis e usa todas as que se aplicam. Uma skill aderente à missão não pode ser ignorada, e a skill utilizada — ou a razão da não aplicação — é registrada no envelope de saída. É isso que torna auditável se o procedimento correto foi seguido.

**4. Execução autorizada.** O agente age dentro do escopo declarado, preferindo verificações locais e reversíveis. Não amplia acesso, escopo ou impacto por conta própria, e não executa ação externa ou irreversível sem autorização explícita.

**5. Gates.** Sensors locais e gates de CI avaliam o resultado por critérios objetivos. O agente não declara sucesso: ele executa a verificação e registra o que ela devolveu.

**6. Envelope de saída.** A missão termina em um formato padronizado, que permite ao orquestrador e ao owner humano entender o resultado sem reler a execução inteira.

```yaml
mission_id: "..."
agent_role: "..."
status: completed | partial | blocked
confidence: high | medium | low
sources_used: []
skills_used: []
outputs_created: []
decisions_requested: []
assumptions: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

Dois campos merecem atenção especial. O campo `confidence` obriga o agente a declarar quão seguro está — e confiança abaixo do limite da missão é, por si só, uma condição de escalonamento. O campo `skills_used` converte a disciplina de procedimento em algo verificável por terceiros.

### As regras universais

Quatro conjuntos de regras valem para qualquer agente, sempre. Elas resolvem antecipadamente os comportamentos que mais comprometem confiança.

**Sobre a verdade.** Separar fato, evidência, inferência, hipótese e recomendação. Não inventar requisitos, decisões, participantes ou resultados. Citar a origem de afirmações relevantes e preservar incerteza e contradições não resolvidas. Quando uma fonte estiver ausente, produzir output parcial identificado como tal em vez de preencher a lacuna com suposição.

**Sobre o limite.** Não ampliar escopo, acesso ou impacto por conta própria. Não executar ação externa ou irreversível sem autorização explícita. Atualizar somente a fonte canônica autorizada. Nunca aprovar sozinho o artefato que produziu.

**Sobre as skills.** Verificar as disponíveis antes de agir e usar cada uma que se aplique. As três skills de base são obrigatórias na operação de workspace: [`workspace-memory`](../skills/workspace-memory/SKILL.md) para retomada e escrita segura de memória, [`workspace-projects`](../skills/workspace-projects/SKILL.md) para localizar a fonte canônica de `projects/`, e [`workspace-board`](../skills/workspace-board/SKILL.md) para assumir ou reconciliar Work Items.

**Sobre a entrega.** Entregar sempre evidence pack e resumo das mudanças, não apenas o artefato cru.

### Orquestração e times por fase

Cada fase do workflow aciona um **time temporário de agentes, dissolvido ao final**. Isso permite manter dezenas de especializações disponíveis sem que nenhuma delas fique ociosa: não se paga por um Security Review Agent parado — ele só existe quando a validação de uma mudança sensível o exige.

Dentro de cada time, a dinâmica se repete. Um **agente primário** conduz e consolida o artefato da fase. Um ou mais agentes **colaboram ou desafiam** a partir de uma responsabilidade explícita. Os agentes **adversariais** procuram ambiguidade, lacuna, risco e suposição frágil — sempre como instâncias independentes de quem produziu.

| Fase | Agente primário | Agentes críticos ou especialistas | Handoff |
|---|---|---|---|
| Intake | Intake Agent | Meeting Context quando houver reunião | PM prioriza |
| Discovery | Product Manager Agent | UX Specification + Tech Lead Discovery | `PB.md` para H1 |
| Produto e UX | Product Manager + UX Specification | Adversarial Product Manager | PRD + UX spec para H2 |
| Especificação | Specification Tech Lead | Adversarial TL + especialistas | PLAN/SPEC/TASKS para H3 |
| Implementação | Orchestrator + Software Engineer | — | diff e gates locais |
| Validação | QA / Validation | Security + Architecture + Code Reviewer | evidence pack |
| Integração | PR Agent | Reviewer Agents | H4 / merge |
| Homologação | Product Validation | Release Agent | release candidate |
| Produção | Release Agent | Observability Agent | H5 / health report |
| Conhecimento | Knowledge Agent | Critic quando sensível | fontes canônicas |
| Melhoria | Telemetry + Auto Dream | Critic Agent | H6, memória ou backlog |

Observe o padrão deliberado: em quase toda fase, quem consolida não é quem critica. Isso não é redundância — é a regra de que **quem propõe não aprova**, aplicada ao nível do time. Um agente que revisasse o próprio trabalho tenderia a confirmar as próprias suposições; a independência estrutural, e não a boa-fé do modelo, é o que faz a crítica valer.

O Orchestrator Agent distribui contexto mínimo e controla dependências nas fases com paralelismo, mas há um limite que convém gravar: ele **não substitui** o consolidado do agente primário nem a decisão do owner humano. O orquestrador organiza o trânsito; não decide o destino.

Por fim, o catálogo descreve **papéis lógicos, não instâncias**. Uma execução pode usar uma instância por papel, várias instâncias paralelas do mesmo papel, ou uma instância assumindo mais de um papel compatível. A restrição que nunca se quebra: papéis de produção e de aprovação não se combinam na mesma instância quando houver risco de autoavaliação.

### Autonomia e escalonamento

O nível de autonomia concedido a um agente não é uma escolha de configuração — é uma consequência do que o repositório consegue verificar. A regra central é que **o nível do harness é o teto da autonomia, nunca a consequência dela**. Um repositório em HL1 operando com autonomia A2 não é um repositório adiantado; é um repositório com um gate faltando que ninguém percebeu ainda. Os níveis estão detalhados em [Gates](GATES.md).

Dentro do teto autorizado, o agente age com iniciativa. Fora dele, para. As condições universais de escalonamento são:

- Requisito contraditório ou sem owner definido
- Fonte canônica ausente, inconsistente ou reivindicada por dois donos
- Confiança abaixo do limite declarado para a missão
- Duas ou mais tentativas de correção sem progresso
- Mudança fora do escopo aprovado
- Necessidade de nova permissão ou acesso externo
- Risco maior que o autorizado para a missão
- Decisão irreversível ou impacto não calculável
- Divergência entre agentes sem critério objetivo de desempate

Essas condições não são falhas: são o sistema funcionando como projetado. A lógica por trás de todas elas é a mesma — **quando o custo de errar sozinho supera o custo de perguntar, o agente pergunta**.

### Permissões por categoria

O princípio é privilégio mínimo: um agente recebe apenas o acesso que sua missão exige, e escrita externa é sempre exceção autorizada.

| Categoria | Leitura | Escrita local | PR / backlog | Deploy / externo |
|---|---|---|---|---|
| Intake e Meeting Context | fontes autorizadas | artefatos de proposta | somente se a missão autorizar | não |
| Produto, UX e Discovery | produto, pesquisa e código | artefatos da fase | comentário ou proposta | não |
| Especificação | código e docs | artefatos técnicos | comentário ou proposta | não |
| Software Engineer | escopo do repositório | código, testes e docs | branch ou PR autorizado | não por padrão |
| Reviewers | código e evidências | relatório e comentários | review autorizado | não |
| PR Agent | Git e checks | descrição e evidence pack | PR autorizado | merge só por política |
| Release | artefato e ambientes | registro de release | status | ambiente explicitamente autorizado |
| Observability | telemetria | alertas e relatórios | incidente autorizado | pausa ou rollback por política |
| Knowledge e melhoria | docs, memória e métricas | proposta ou fonte autorizada | backlog autorizado | não |

### Do papel lógico ao agente executável

Cada papel deste catálogo está materializado em [`agents/<agent-id>/`](../agents/README.md) por um prompt único, independente de runtime:

```text
<agent-id>/
└── AGENT.md     # missão, limites, presença e diretivas estáveis do sponsor
```

`AGENT.md` é a única fonte de instruções executáveis do papel e inclui regras universais, output e persistência. Fontes, regras locais e skills são consultadas apenas quando forem específicas da missão; não existe prompt consolidado gerado nem artefato de sincronização de runtime.

---

## Agentes disponíveis

Os 23 papéis estão documentados individualmente em **[`agentes/`](agentes/README.md)** — um arquivo por agente, com o contrato operacional completo, os limites explícitos do papel, a personalidade e as notas de operação.

O índice oficial, agrupado por função na jornada, vive nesse mesmo diretório: **[índice de contratos dos agentes](agentes/README.md)**. Ele é a fonte canônica da lista; esta página descreve o funcionamento comum a todos.

| Grupo | Papéis | Sponsor típico |
|---|---|---|
| [Entrada e coordenação](agentes/README.md#entrada-e-coordenação) | Intake, Meeting Context, Orchestrator | PM e owner da fase |
| [Produto, UX e discovery](agentes/README.md#produto-ux-e-discovery) | Product Manager, UX Specification, Tech Lead Discovery, Adversarial PM | PM e UX |
| [Especificação técnica](agentes/README.md#especificação-técnica) | Specification TL, Adversarial TL, Security/Data/Platform | Tech Lead |
| [Construção e validação](agentes/README.md#construção-e-validação) | Software Engineer, QA, Security Review, Architecture Review, Adversarial Code Reviewer | Tech Lead |
| [Integração, homologação e operação](agentes/README.md#integração-homologação-e-operação) | PR, Product Validation, Release, Observability | Tech Lead, PM e UX |
| [Conhecimento e melhoria](agentes/README.md#conhecimento-e-melhoria) | Knowledge, Telemetry, Auto Dream, Critic | owner do domínio e trio |

---

## Versionamento e avaliação

Cada definição de agente registra versão do contrato e data, versão do prompt, modelo, effort e tools, responsável humano, casos de teste e golden outputs, métricas de qualidade, custo e duração, falhas conhecidas e contextos proibidos, além de changelog com plano de rollback.

As métricas por agente cobrem taxa de conclusão sem escalonamento, aprovação na primeira passagem do gate, precisão dos fatos e rastreabilidade, findings confirmados e falsos positivos, retrabalho causado no próximo handoff, tokens, custo e tempo, cobertura do output obrigatório, e violações de escopo ou permissão.

**Essas métricas não formam ranking individual.** Elas servem para melhorar contrato, contexto, tools, modelo e gates — usá-las como avaliação de desempenho corrompe o sinal que produzem.

---

## Checklist para adicionar um novo agente

- [ ] O problema exige um papel novo ou cabe em um agente existente?
- [ ] Sponsor e direito de decisão estão claros?
- [ ] Inputs e fontes canônicas estão definidos?
- [ ] O output possui schema verificável?
- [ ] As permissões seguem privilégio mínimo?
- [ ] Existe condição de parada e escalonamento?
- [ ] Produção e crítica estão segregadas?
- [ ] Há testes com casos nominal, ambíguo, incompleto e sensível?
- [ ] Telemetria e custo serão registrados?
- [ ] O catálogo, o orquestrador e os handoffs foram atualizados?

---

*Anterior: [Harness do Repositório](REPO_HARNESS.md) · Próximo: os [contratos individuais dos agentes](agentes/README.md).*
