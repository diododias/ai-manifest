---
title: Agent Team — sistema operacional do trio humano
status: canonical
updated_at: 2026-08-09
---

# Agent Team — sistema operacional do trio humano

> Visão canônica do Agent Team: como um núcleo de **Product Manager, UX e Tech Lead** dirige agentes especializados do backlog à produção sem perder controle, evidência ou rastreabilidade.

## Em 2 minutos

Quando agentes de IA assumem a produção de código, o gargalo se desloca. Escrever deixa de ser caro; o que fica caro é decidir o que construir, provar que foi construído certo e impedir que decisões, código e documentação se separem. Um time pequeno que não trata esse deslocamento acaba gerando volume sem confiança.

O Agent Team responde com uma inversão: as três pessoas **operam o sistema** em vez de executar o trabalho. O trio define intenção, prioridade, risco e aprovação; agentes especializados pesquisam, especificam, implementam, criticam, validam e documentam dentro de escopo autorizado. Nenhuma passagem entre fases acontece por conversa — cada uma tem entrada, saída, owner humano, gate e evidência, materializados em artefatos versionados.

| Elemento | O que é | Por que existe |
|---|---|---|
| **Trio humano** | PM, UX e Tech Lead, cada um dono de um domínio | evita decisão sem responsável |
| **Agent Team** | Time temporário de agentes montado por fase | especialização sem custo fixo de headcount |
| **Agente adversarial** | Instância independente que ataca a proposta | quem produz não valida a própria mudança |
| **Gate** | Critério objetivo de passagem entre fases | impede avanço sem evidência |
| **Evidence pack** | Pacote curto que sustenta uma decisão humana | decidir sem reler sessões inteiras |
| **Classe de risco (R0–R4)** | Peso da mudança | define quanto de autonomia é permitido |
| **Nível de autonomia (A0–A4)** | Quanto o sistema roda sem intervenção | cresce só com histórico e gates confiáveis |

Três regras sustentam o resto: quem propõe não é quem aprova; aprovação exige evidência explícita e silêncio nunca equivale a aprovação; autonomia só aumenta quando métricas e gates demonstram que é seguro.

---

## Mapa do documento

| Parte | Seções | Responde | Leia se você… |
|---|---|---|---|
| [I — Fundamentos](#parte-i--fundamentos) | 1–3 | Para que o modelo existe e como agentes atuam | quer entender a lógica antes dos detalhes |
| [II — Quem decide](#parte-ii--quem-decide) | 4–7 | Papéis, direitos de decisão, handoffs e cerimônias | vai assumir um dos três papéis |
| [III — Como o trabalho anda](#parte-iii--como-o-trabalho-anda) | 8–11 | O ciclo de ponta a ponta e o loop de melhoria | vai executar ou instrumentar o fluxo |
| [IV — O que sustenta](#parte-iv--o-que-sustenta) | 12–14 | Harness, governança, risco e autonomia | vai configurar o repositório e os gates |

Para montar ou auditar um repositório operado por agentes, o detalhamento está em [repo harness](repo-harness.md).
| [V — Evolução](#parte-v--evolução) | 15–18 | Fases de adoção, métricas e pendências | vai implantar o modelo em um time |

**Documentos vizinhos:** [modelo operacional 90/10](operating-model-90-10.md) · [repo harness](repo-harness.md) · [fluxo visual completo](end-to-end-journey.md) · [fluxos por fase](journey-by-phase.md) · [workflows multiagente](workflows/README.md) · [catálogo de agentes](agents/catalog.md) · [workspace do Tech Lead](diagrams/tech-lead-workspace.md).

---

# Parte I — Fundamentos

## 1. Propósito

O objetivo do modelo é transformar uma necessidade de negócio em software validado por meio de um núcleo humano pequeno que dirige uma força de trabalho de agentes especializados. Isso exige combinar agentes, pessoas e automações mantendo decisões, código e documentação sincronizados, produzir evidência em todas as etapas e escalar a entrega sem abrir mão de segurança e governança.

Duas consequências disso são intencionais. A primeira é que a atenção humana fica reservada para intenção, julgamento, risco e responsabilidade — não para execução repetitiva. A segunda é que execução, validação e coleta de evidências se tornam progressivamente autônomas, e o próprio sistema de trabalho melhora a cada ciclo.

A divisão de trabalho que torna isso possível é a seguinte:

| Ator | Dirige |
|---|---|
| **Product Manager** | valor, prioridade e resultado de negócio |
| **UX** | entendimento do usuário, experiência e qualidade de uso |
| **Tech Lead** | viabilidade, arquitetura, qualidade técnica e risco operacional |
| **Agentes** | pesquisa, proposta, implementação, crítica, validação e documentação |
| **Automações** | verificações determinísticas, bloqueios e rastreabilidade |

O trio não tenta executar manualmente todo o trabalho. Ele opera o sistema que executa.

---

## 2. Princípios operacionais

Os princípios abaixo resolvem, antecipadamente, as disputas mais comuns em um fluxo com agentes. Estão agrupados por aquilo que protegem.

**Autoridade e responsabilidade.** Pessoas definem prioridade, restrições, limites de autonomia e aprovação final; agentes executam trabalho especializado e produzem evidências. Cada etapa tem entrada, saída, owner humano e critério de passagem. O responsável humano decide, o agente primário prepara e recomenda, e divergências relevantes entre agentes são resolvidas pelo owner humano do domínio.

**Integridade da validação.** Quem produz uma mudança não é o único responsável por validá-la. A etapa termina com um artefato coerente, não com análises isoladas. Uma mudança material invalida a aprovação relacionada, e ausência de resposta nunca equivale a aprovação.

**Qualidade da decisão.** Aprovação humana deve receber síntese, alternativas, riscos e evidências — nunca contexto bruto. Comunicação assíncrona é o padrão; reunião existe para decidir, não para narrar status.

**Segurança da evolução.** Mudanças pequenas, reversíveis e rastreáveis reduzem risco e retrabalho. O repositório concentra regras e contexto executável do produto, o harness transforma padrões em verificações repetíveis, e a autonomia aumenta apenas quando métricas e gates demonstram segurança.

---

## 3. Modelo de atuação dos Agent Teams

Cada fase pode acionar um time temporário de agentes especializados, dissolvido ao final. Isso permite ter dezenas de especializações sem manter nenhuma delas ociosa. O [catálogo de agentes](agents/catalog.md) define os contratos e limites de cada papel.

A dinâmica interna do time é sempre a mesma. Um **agente primário** conduz e consolida o artefato da fase, enquanto cada agente analisa o problema a partir de uma responsabilidade explícita. **Agentes adversariais** procuram ambiguidades, gaps, riscos e suposições frágeis. As contribuições e divergências são registradas antes da consolidação, e o owner humano intervém apenas em decisão de valor, experiência, risco ou exceção — não em toda execução.

O contexto passa entre fases por artefatos versionados e evidence packs. Nenhum agente recebe acesso amplo: cada um opera com acesso mínimo, escopo delimitado e condição objetiva de parada.

### 3.1 Estrutura mínima de uma missão

Toda missão entregue a um agente declara, no mínimo, os campos abaixo. Missão sem esses campos não deve ser executada.

| Campo | Define |
|---|---|
| Objetivo e resultado esperado | o que a missão precisa produzir |
| Contexto e fontes canônicas | onde está a verdade sobre o tema |
| Escopo e fora de escopo | o limite da autonomia concedida |
| Artefato de entrada e de saída | o que se lê e o que se escreve |
| Critérios de aceite | como saber que terminou |
| Gates obrigatórios | o que precisa passar antes de avançar |
| Ferramentas e permissões | o que o agente pode acionar |
| Classe de risco | quanto de verificação a mudança exige |
| Condição de escalonamento | quando parar e chamar uma pessoa |
| Owner humano da decisão | quem responde pelo resultado |

---

# Parte II — Quem decide

## 4. O trio humano

Cada papel é dono de um domínio e traz decisões próprias para a mesa. Nenhum dos três é um "tradutor" passivo dos outros: eles constroem juntos o contrato que os agentes executarão.

### 4.1 Product Manager — dono do valor e da prioridade

O PM responde pela pergunta "vale a pena construir isto, agora, para este resultado?". Ele mantém visão, objetivos, outcomes e roadmap, ordena o backlog por valor, urgência, risco e aprendizado, e formula o problema antes de comprometer uma solução. Também identifica stakeholders e restrições comerciais, define escopo, fora de escopo e critérios de sucesso, e garante rastreabilidade entre problema, investimento, entrega e resultado.

Na operação diária, cabe ao PM decidir avançar, ajustar, adiar ou encerrar um item; homologar valor com stakeholders e registrar pendências; priorizar melhorias originadas pela telemetria; e operar os agentes de intake, discovery, pesquisa, planejamento e validação de produto.

| Recebe | Entrega |
|---|---|
| estratégia e objetivos do negócio | backlog ordenado e com owner |
| necessidades de clientes e stakeholders | objetivo e outcome esperado |
| pesquisas e evidências de UX | `PB.md` aprovado e `PRD.md` consolidado |
| métricas de produto e operação | escopo e fora de escopo explícitos |
| restrições, riscos e estimativas do Tech Lead | métricas e critérios de sucesso |
| feedback de homologação e produção | decisões H1, H2 e aceite de produto |
| incidentes, custo do fluxo e oportunidades | prioridade das melhorias e comunicação de resultado |

**Não é responsabilidade exclusiva do PM:** desenhar sozinho a experiência, definir arquitetura ou solução técnica, aprovar exceção técnica sem o Tech Lead, ou substituir evidência de usuário por opinião de stakeholder.

### 4.2 UX — dono da experiência e da evidência sobre o usuário

O UX responde por "isto resolve o problema de quem vai usar, e resolve bem?". Planeja e executa pesquisa proporcional ao risco, representa necessidades, contexto e limitações dos usuários, e mapeia jornadas, fluxos, tarefas e pontos de fricção. Define princípios de experiência, conteúdo e interação, e especifica os estados nominal, vazio, loading, erro, permissão e recuperação — o conjunto que costuma ser esquecido e vira retrabalho.

Também garante acessibilidade, consistência e usabilidade, produz protótipos na fidelidade necessária para decidir, e valida hipóteses antes e depois da implementação.

| Recebe | Entrega |
|---|---|
| problema, segmento e outcome do PM | evidência e síntese de pesquisa |
| restrições técnicas e de plataforma | jornada, fluxo e mapa de estados |
| feedback de uso, suporte e telemetria | protótipo na fidelidade adequada |
| critérios de negócio e métricas | especificação de UX e critérios de aceite de experiência |
| resultados de homologação | decisão de aceite de experiência e backlog de melhorias de uso |

**Não é responsabilidade exclusiva do UX:** definir prioridade de negócio, escolher arquitetura, ou aprovar escopo sozinho.

### 4.3 Tech Lead — dono da integridade técnica e do risco operacional

O Tech Lead responde por "isto é viável, sustentável e seguro de operar?". Avalia viabilidade e alternativas, define arquitetura, contratos e fronteiras, estabelece padrões de qualidade, testes e observabilidade, e classifica risco. Também mantém o repo harness — o conjunto de rules, skills, hooks e gates que torna o repositório compreensível e seguro para agentes.

Na operação, decide sobre exceções arquiteturais, merge e release conforme política, e opera os agentes de especificação, implementação, revisão, segurança e operação.

| Recebe | Entrega |
|---|---|
| problema, escopo candidato e métricas | viabilidade, alternativas e trade-offs |
| especificação de UX e estados | `PLAN.md`, `SPEC.md`, `TASKS.md` e ADRs |
| restrições de plataforma e dependências | classificação de risco e gates aplicáveis |
| resultados de CI, validação e incidentes | evidence pack técnico |
| sinais de produção e custo | decisão de merge, release e rollback |

**Não é responsabilidade exclusiva do Tech Lead:** definir valor de negócio, decidir experiência do usuário, ou absorver sozinho decisão de escopo.

### 4.4 Responsabilidade compartilhada

Os três respondem conjuntamente pela qualidade do problema antes da solução, pela coerência entre valor, experiência e viabilidade, por riscos explícitos e decisões rastreáveis, por critérios de aceite observáveis, pela proteção dos dados e dos usuários, pela saúde do fluxo agentico e pelo aprendizado após a entrega.

---

## 5. Direitos de decisão

A tabela abaixo é a referência para resolver "quem decide isto?". Ela existe para que nenhuma decisão fique parada aguardando consenso, e para que nenhuma seja tomada sem a evidência que a sustenta.

| Decisão | Owner | Consultados | Evidência mínima |
|---|---|---|---|
| Prioridade e investimento | PM | UX + Tech Lead | valor, urgência, risco e custo de oportunidade |
| Problema e outcome | PM | UX + Tech Lead | evidência do problema e métrica de resultado |
| Jornada e experiência | UX | PM + Tech Lead | pesquisa, fluxo, protótipo e critérios de UX |
| Escopo da entrega | PM | UX + Tech Lead | outcome, capacidade, dependências e riscos |
| Arquitetura e implementação | Tech Lead | PM + UX | alternativas, trade-offs, risco e validação |
| Exceção arquitetural | Tech Lead | owner afetado | ADR, prazo, consequência e plano de reversão |
| Aceite de produto | PM | UX + stakeholder | critérios de produto e evidências de homologação |
| Aceite de experiência | UX | PM + Tech Lead | critérios de UX, acessibilidade e validação |
| Merge e release | Tech Lead por política | PM + UX conforme risco | CI, evidence pack, rollout e rollback |
| Exposição de risco R3/R4 | PM + Tech Lead | UX quando houver impacto ao usuário | impacto, mitigação, observabilidade e rollback |
| Prioridade de melhoria | owner do domínio; PM ordena o backlog | trio | telemetria, frequência, impacto e esforço |
| Mudança de gate | Tech Lead + revisor independente | PM/UX se afetados | falsos positivos, risco coberto e plano de adoção |

### 5.1 Regra de desempate

Quando a discussão trava, o domínio decide: valor, prioridade e outcome com o PM; experiência, usabilidade e acessibilidade com o UX; arquitetura, segurança e confiabilidade com o Tech Lead. Conflitos entre domínios exigem registrar alternativas, impacto e decisão conjunta. Risco irreversível, regulatório ou de grande alcance escala ao sponsor ou responsável formal — não se resolve dentro do trio.

---

## 6. Contrato de passagem entre os três profissionais

Cada seta entre papéis é um contrato, não uma conversa. O emissor entrega insumos definidos e o receptor devolve um resultado definido.

| De | Para | Inputs entregues | Output esperado do receptor |
|---|---|---|---|
| PM | UX | problema, segmento, outcome, restrições e perguntas | evidência do usuário, jornada, fluxo e critérios de experiência |
| PM | Tech Lead | problema, escopo candidato, métricas e restrições | viabilidade, riscos, dependências e opções técnicas |
| UX | PM | evidências, necessidades, hipóteses e riscos de experiência | decisão de escopo/prioridade e atualização do PRD |
| UX | Tech Lead | fluxo, estados, conteúdo, acessibilidade e protótipo | contratos, tarefas e estratégia de implementação compatíveis |
| Tech Lead | PM | custo, riscos, dependências, alternativas e impacto operacional | decisão de investimento, corte ou sequenciamento |
| Tech Lead | UX | restrições, latência, dados, plataforma e componentes existentes | adaptação consciente da experiência sem perder o outcome |
| Trio | Agent Team | artefato aprovado, critérios, gates, risco e permissões | mudança executada, validada, documentada e evidenciada |
| Agent Team | Trio | evidence pack, divergências e decisões pendentes | aprovação, correção, adiamento ou escalonamento |

### 6.1 Definition of Ready para execução agentica

Um item só entra em execução por agentes quando problema e usuário estão explícitos, outcome e métrica definidos, owner humano conhecido, e escopo e fora de escopo claros. Do lado do detalhe, exige fluxo e estados de UX suficientes para a tarefa, contratos e restrições técnicas suficientes, critérios de aceite verificáveis, classe de risco e gates definidos, acessos e ferramentas autorizados, e dúvidas críticas resolvidas ou assumidas de forma explícita.

### 6.2 Definition of Done do ciclo

O ciclo fecha quando os critérios de produto, UX e engenharia estão cobertos; testes e gates obrigatórios aprovados; impacto arquitetural avaliado; riscos e limitações conhecidos; documentação e fontes canônicas atualizadas; aprovações humanas e automatizadas identificadas; backlog, artefatos, commits, PR, release e telemetria vinculados; rollout observado sem regressão relevante ou com plano de correção; e aprendizados encaminhados ao loop correto.

---

## 7. Cerimônias humanas

As cerimônias são **pontos de decisão**, não pontos de relato. Preparação, análise, atualização de status e geração de artefatos ficam com os agentes e automações; a pessoa entra para decidir. Os marcos H1 a H6 aparecem no ciclo da [Parte III](#8-ciclo-de-desenvolvimento-de-ponta-a-ponta) como gates com nome.

### 7.1 Ritmo contínuo

| Cerimônia | Cadência | Owner | Decide |
|---|---|---|---|
| Pulso assíncrono diário | diária, ≤10 min de leitura | trio | o que está bloqueado e quem desbloqueia |
| Triagem e prioridade | semanal, 30–45 min | PM | o que entra, o que sai e o que precisa de discovery |

O pulso diário é alimentado por agentes com estado do fluxo, mudanças, bloqueios, risco e decisões requeridas. A pauta cobre apenas bloqueios, novas informações e pedidos de decisão, e o resultado registra owners, prazo da decisão e replanejamento. **Não deve virar** reunião diária de relato individual.

A triagem recebe novos itens, métricas, feedback, incidentes, dependências e capacidade, e devolve backlog ordenado com owner, risco inicial e próximos discoveries. O gate é ter contexto, prioridade e responsável minimamente claros.

### 7.2 Marcos de decisão H1–H6

| Marco | Cerimônia | Owner | Cadência | Gate |
|---|---|---|---|---|
| **H1** | Kickoff de discovery | PM | por oportunidade, 30–45 min | missão, timebox e agentes definidos |
| **H2** | Refinamento de produto e experiência | PM (UX co-owner) | por item candidato, 45–60 min | gaps críticos tratados e sucesso mensurável |
| **H3** | Revisão de solução e risco | Tech Lead | sob demanda, 30–60 min | rastreabilidade e validação viável |
| **H4** | Review de entrega | PM/UX/Tech Lead por critério | por incremento, 20–30 min | revisão aprovada, CI verde, sem bloqueadores |
| **H5** | Decisão de release | Tech Lead (PM coaprova R3/R4) | por release, 10–20 min | ambiente, migração, observabilidade e rollback verificados |
| **H6** | Telemetria e melhoria | trio, facilitação rotativa | semanal, 45–60 min | evidência rastreável e hipótese separada de aprendizado |

**H1 — Kickoff de discovery.** Parte do intake consolidado, evidências existentes e perguntas abertas. O PM traz problema, valor, stakeholders e outcome; o UX traz as lacunas sobre o usuário e o plano de pesquisa; o Tech Lead traz restrições, dependências e risco de viabilidade. Sai com missão de discovery, `PB.md` inicial, agentes acionados e timebox. A decisão final é avançar, ajustar, adiar ou encerrar.

**H2 — Refinamento de produto e experiência.** A pergunta é "é isto que construiremos, para quem e com qual resultado?". Entram `PB.md`, pesquisa, jornada, protótipo, PRD proposto e crítica adversarial. Saem `PRD.md`, especificação de UX, critérios de aceite e escopo aprovado.

**H3 — Revisão de solução e risco.** Obrigatória para ADR, exceção ou risco elevado. Entram `PLAN.md`, `SPEC.md`, ADR, alternativas, threat model, plano de testes e crítica adversarial. O PM avalia impacto em outcome, prazo e escopo; o UX avalia impacto em jornada, conteúdo, acessibilidade e estados. Saem decisão técnica, trade-offs aceitos, tarefas executáveis e riscos com owner.

**H4 — Review de entrega.** A pergunta é "entrega o outcome acordado, funciona bem e pode ser integrada?". Entram demo preparada por agentes, evidence pack, critérios de aceite e mudanças desde H2/H3. Saem aceite, ajustes, novos itens ou rejeição justificada.

**H5 — Decisão de release.** Síncrona apenas quando o risco exigir. Entram release candidate, risco, rollout, rollback, SLOs e sinais de saúde. Saem liberar, pausar, reduzir exposição ou retornar à implementação.

**H6 — Telemetria e melhoria.** A pergunta é "o sistema aprendeu corretamente e qual melhoria merece investimento?". Entram relatório de telemetria, padrões, incidentes, custo, feedback e propostas do Auto Dream. Saem memória validada, demandas P0–P3, owners, experimentos e alterações de processo.

### 7.3 Revisões periódicas

A **revisão mensal do sistema** (60–90 min, trio mais sponsor ou enablement quando necessário) olha tendências de outcome, qualidade, fluxo, custo, autonomia e falsos positivos dos gates, e ajusta capacidade, políticas, ferramentas, gates e nível de autonomia. A regra que protege essa reunião: nunca usar uma métrica isolada para elevar autonomia.

A **quarterly outcome review** (60–90 min, owner PM) revisa outcomes, estratégia, pesquisas, saúde técnica, custo e aprendizados acumulados, e define prioridades do próximo ciclo, apostas encerradas e capacidades a desenvolver.

---

# Parte III — Como o trabalho anda

## 8. Ciclo de desenvolvimento de ponta a ponta

O ciclo tem dez etapas, cada uma com workflow próprio, owner humano, time de agentes e gate. A visão em diagrama está em [fluxo da jornada](end-to-end-journey.md); o detalhamento por fase, em [jornada por fases](journey-by-phase.md).

| # | Etapa | Owner humano | Agentes | Gate | Cerimônia |
|---:|---|---|---|---|---|
| 0 | [Intake e triagem](workflows/00-intake-and-triage.md) | PM | Intake + Product Manager | problema, prioridade e responsável claros | Triagem |
| 1 | [Discovery](workflows/01-discovery-and-research.md) | PM (UX e TL por domínio) | Product Discovery Team | problema validado e viabilidade avaliada | H1 |
| 2 | [Produto e experiência](workflows/02-product-and-ux-planning.md) | PM / UX | Product Planning Team | gaps tratados e critérios aprovados | H2 |
| 3 | [Especificação técnica](workflows/03-technical-specification.md) | Tech Lead | Technical Specification Team | trade-offs registrados e tarefas executáveis | H3 |
| 4 | [Implementação](workflows/04-autonomous-implementation.md) | Tech Lead por exceção | Orchestrator + Software Engineer | verificações locais aprovadas | — |
| 5 | [Validação adversarial](workflows/05-adversarial-validation.md) | Tech Lead (PM/UX por critério) | QA, Security, Architecture, Reviewer | checklist completo, sem bloqueadores | — |
| 6 | [PR e merge](workflows/06-pr-and-merge.md) | Tech Lead ou Code Owner | PR + Reviewer | CI verde e aprovações válidas | H4 |
| 7 | [Homologação](workflows/07-release-candidate-validation.md) | PM / UX | Release + Product Validation | critérios validados ou plano de correção | — |
| 8 | [Entrega e observação](workflows/08-production-release-and-observation.md) | Tech Lead (PM em R3/R4) | Release + Observability | janela pós-deploy sem regressão | H5 |
| 9 | [Curadoria de conhecimento](workflows/09-knowledge-curation.md) | owner do domínio alterado | Knowledge | documentação atual e sem contradições | — |

### 8.0 Intake e triagem de backlog

Registra, deduplica, contextualiza e prioriza necessidades. Recebe problema, oportunidade, solicitação, feedback, incidente ou melhoria; valida campos, relaciona produto e repositório, identifica duplicidade e propõe risco. Entrega Work Item priorizável com contexto inicial, owner e risco preliminar.

### 8.1 Discovery

Compreende problema, usuário, contexto, valor e viabilidade inicial. O **Product Discovery Team** reúne Product Manager Agent, UX Specification Agent e Tech Lead Discovery Agent em investigação paralela: cada um registra hipóteses no seu domínio, o Product Manager Agent sintetiza e os demais criticam a síntese.

Entrega `PB.md` com problema, usuários, jornada, valor, restrições e riscos, acompanhado de evidências e perguntas abertas. O gate exige problema validado, experiência desejada compreendida e viabilidade inicial avaliada.

### 8.2 Planejamento de produto e experiência

Transforma o problema em proposta clara, testável e utilizável. O **Product Planning Team** reúne Product Manager Agent, UX Specification Agent e Adversarial Product Manager Agent, mais agentes de pesquisa, conteúdo ou prototipação quando necessários. A dinâmica é proposta → protótipo e especificação de UX → crítica adversarial → revisão → consolidação.

Entrega `PRD.md`, jornada e fluxo desejados, wireframe ou protótipo na fidelidade necessária, estados, conteúdo e critérios de acessibilidade, e critérios de sucesso e aceite. O conteúdo mínimo do PRD cobre objetivos, usuários, jornadas, escopo, fora de escopo, requisitos e métricas.

### 8.3 Especificação técnica

Define como construir, validar, liberar e operar a solução. O **Technical Specification Team** reúne Specification Tech Lead Agent e Adversarial Tech Lead Agent, com Security, Data ou Platform Agent quando o risco exigir. A dinâmica é especificação → revisão crítica → resposta aos gaps → decisão.

| Artefato | Conteúdo |
|---|---|
| `PLAN.md` | estratégia de implementação |
| `ADR.md` | decisões arquiteturais relevantes e consequências |
| `SPEC.md` | comportamento e contratos técnicos |
| `TASKS.md` | unidades pequenas de execução |
| `CHECKLIST.md` | critérios verificáveis de aceite |
| Planos complementares | testes, rollout, rollback e observabilidade conforme risco |

O gate exige gaps críticos tratados, trade-offs registrados e tarefas executáveis.

### 8.4 Implementação

Implementa **uma tarefa pequena por vez**. O Orchestrator Agent distribui e os Software Engineer Agents executam, apoiados pelo repo harness, pelas skills e pelas ferramentas de código. Recebe tarefa, SPEC, critérios, contexto, permissões e gates; entrega código, testes, documentação, commits e evidências em um diff rastreável. A ação humana só ocorre diante de decisão, exceção ou escalonamento.

### 8.5 Validação adversarial

Prova aderência à especificação e procura falhas que o autor não encontrou. Agentes de Validation/QA, Security, Architecture e Reviewer executam testes, verificação de segurança, análise arquitetural, acessibilidade, regressão e mutation testing quando aplicável. Entrega evidências vinculadas a cada critério e achados classificados. O gate exige checklist completo e ausência de bloqueadores.

### 8.6 Code review, PR e decisão de merge

Avalia qualidade, risco, manutenibilidade e prontidão para integração. PR Agent e Reviewer Agent analisam diff, commits, resultados de validação e evidence pack, cobrindo código, testes, impacto arquitetural, contratos e documentação. O gate exige revisão aprovada, CI verde, branch atualizada e aprovações válidas.

### 8.7 Homologação

Confirma valor e comportamento em cenário representativo. Release Agent e Product Validation Agent preparam preview, smoke, E2E, acessibilidade e demonstração, e coletam evidências. O PM responde por valor, o UX por experiência e o stakeholder participa quando necessário. O gate exige critérios de aceite validados ou plano de correção explícito.

### 8.8 Entrega e observação

Libera com exposição controlada e prova saúde no uso real. Release Agent e Observability Agent conduzem deploy progressivo, feature flag quando aplicável, monitoramento e comparação com baseline. Entrega versão liberada, sinais de saúde, changelog e — quando necessário — rollback ou pausa. O gate exige ambiente autorizado, migração compatível e janela pós-deploy sem regressão relevante.

### 8.9 Atualização da base de conhecimento

Mantém a documentação alinhada ao produto real, de forma contínua e com revisão automatizada semanal. O Knowledge Agent consolida decisões, aprendizados e mudanças a partir de decisões, código, PR, homologação, release e incidentes, e procura contradições e obsolescência. O gate exige documentação atual, rastreável e sem contradições não resolvidas.

---

## 10. Telemetria e melhoria contínua — Auto Dream

Esta é a etapa que fecha o ciclo sobre o próprio sistema de trabalho. O [workflow de telemetria e melhoria contínua](workflows/10-continuous-improvement.md) roda com coleta contínua, síntese semanal e execução extraordinária após incidente relevante. Os agentes envolvidos são Telemetry/Observability Agent, Auto Dream Agent e um Critic Agent independente; o owner é o trio, e cada demanda retorna ao owner do domínio. A cerimônia associada é H6.

O escopo é deliberadamente amplo: produto, UX, engenharia, agentes, prompts, processo, harness, skills, scripts, ferramentas, hooks, gates, documentação e arquitetura do workflow.

### 10.1 Por que "Telemetria e melhoria"

"Auto Dream" descreve um mecanismo; "Telemetria e melhoria" descreve o resultado operacional: enxergar como o sistema se comporta, distinguir sinal de ruído e converter evidência em aprendizado ou ação. Sem telemetria, melhoria contínua vira opinião. Sem retorno ao backlog e à memória, telemetria vira dashboard decorativo.

### 10.2 Eventos e correlação mínima

Cada evento relevante carrega, quando aplicável, os campos abaixo. O padrão recomendado é instrumentar logs, métricas e traces correlacionáveis, com taxonomia versionada e política de retenção.

| Dimensão | Campos |
|---|---|
| Identidade | `work_item_id`, produto, repositório, session/run ID, timestamp |
| Execução | fase, agente, modelo, versão de prompt/skill, tool usada |
| Resultado | input, output, status, retry, fallback, bloqueio, escalonamento |
| Custo | duração, tokens, custo, tamanho de contexto |
| Verificação | gate, resultado, evidência e duração |
| Decisão | decisão humana, owner e motivo |
| Rastreio | commit, PR, release, ambiente, classe de risco, nível de autonomia |
| Proteção | anonimização e tratamento de dados sensíveis |

### 10.3 Entradas do ciclo

O ciclo consome sessões e decisões dos agentes, evidence packs e feedbacks humanos, falhas, retries, bloqueios e escalonamentos, resultados de hooks, CI, homologação e deploy, incidentes, rollbacks e defeitos escapados, métricas de tempo, custo, qualidade, UX e autonomia, feedback de usuário e sinais de produto, e as demandas de melhoria geradas anteriormente.

### 10.4 Pipeline automatizado

1. Coletar sessões e eventos continuamente.
2. Remover secrets e dados pessoais antes da análise.
3. Validar completude, correlação e qualidade dos dados.
4. Agrupar eventos por etapa, causa e tipo de impacto.
5. Identificar padrões recorrentes e ocorrências isoladas.
6. Comparar resultados com baseline e períodos anteriores.
7. Distinguir aprendizado reutilizável de problema operacional.
8. Procurar duplicidade, contradição e obsolescência na memória.
9. Produzir evidências e nível de confiança para cada conclusão.
10. Submeter conclusões a um Critic Agent independente.
11. Consolidar itens confirmados e manter hipóteses inconclusivas em observação.

### 10.5 Loop A — aprendizado validado

Identifica o que funcionou, para quem e em qual contexto, e registra evidências, origem, data e condições de reutilização. Antes de propor inclusão, atualização ou remoção no `MEMORY.md`, verifica duplicidade, contradição e validade temporal. Duas travas protegem esse loop: preferência isolada não vira regra global, e memória sensível exige aprovação humana.

**Gate de memória:** evidência vinculada à conclusão, escopo e contexto de aplicação explícitos, ausência de secrets ou dados pessoais, nenhuma contradição não resolvida, conhecimento acionável e reutilizável, e mudança sensível revisada por pessoa responsável.

### 10.6 Loop B — falha ou oportunidade de melhoria

Descreve sintoma, impacto e etapa afetada; identifica causa provável e evidências; registra frequência e alcance; propõe ação corretiva e resultado esperado; gera demanda rastreável no backlog; relaciona sessões, execuções e incidentes de origem; e detecta e vincula duplicidades.

Os tipos de melhoria previstos cobrem produto ou experiência, processo ou cerimônia, harness, skill ou prompt, script, ferramenta ou integração, hook ou gate, arquitetura do workflow, documentação, contexto ou memória, e observabilidade, segurança ou custo.

| Campo da demanda | Conteúdo |
|---|---|
| Título | orientado ao problema |
| Sintoma e impacto | o que se observa e o que custa |
| Evidências e frequência | origem e recorrência |
| Hipótese de causa-raiz | explicação candidata |
| Melhoria proposta | ação corretiva |
| Critério de aceite | mensurável |
| Prioridade e risco sugeridos | P0–P3 e classe R |
| Owner recomendado | quem deveria assumir |
| Links | sessões e artefatos relacionados |

**Priorização.** P0 é risco crítico, segurança ou perda de dados; P1, falha recorrente que bloqueia o fluxo; P2, retrabalho, custo ou baixa confiabilidade; P3, otimização incremental. Frequência não substitui impacto. O Auto Dream recomenda, o owner humano decide e o PM ordena o backlog.

### 10.7 Painel mínimo do trio

| Dimensão | Owner | Indicadores |
|---|---|---|
| **Produto e UX** | PM + UX | outcome e adoção; conversão ou conclusão da tarefa principal; erros de usuário, abandono e tempo na tarefa; feedback qualitativo e defeitos de experiência; acessibilidade e critérios de UX não atendidos |
| **Fluxo** | trio | lead time (backlog→homologação); cycle time (implementação→merge); tempo por fase e tempo esperando decisão humana; aprovação na primeira passagem por gate; retrabalho após validação; bloqueios, retries e escalonamentos; % de gates automatizados; % de execução autônoma por classe de risco |
| **Engenharia** | Tech Lead | falhas de build, testes e CI; defeitos e regressões pós-entrega; cobertura dos critérios de aceite; change failure rate e tempo de recuperação; violações arquiteturais, segurança e dependências; falsos positivos e tempo gasto por gate |
| **Agentes e custo** | trio | tokens, custo e duração por fase, agente e entrega; taxa de sucesso sem intervenção; tentativas até conclusão; falhas por tool, skill, prompt e modelo; qualidade do evidence pack; tempo humano em exceções; atualidade e uso da base de conhecimento |

### 10.8 Saídas e encerramento

O ciclo entrega `MEMORY.md` atualizado com aprendizados validados, demandas de melhoria criadas ou enriquecidas no backlog, relatório semanal curto com padrões, tendências e qualidade dos dados, métricas do sistema atualizadas, hipóteses inconclusivas mantidas em observação, e experimentos com owner, baseline, prazo e critério de sucesso.

**Gate de conclusão:** fontes processadas e rastreáveis; qualidade e lacunas dos dados explícitas; aprendizados separados de hipóteses; falhas relevantes convertidas em demandas; duplicidades e contradições tratadas; mudanças sensíveis revisadas; nenhum dado confidencial persistido indevidamente.

### 10.9 Falhas do próprio ciclo

O ciclo precisa falhar de forma visível. Falha de coleta abre alerta e impede conclusão silenciosamente parcial. Baixa confiança mantém o item como hipótese. Contradição bloqueia atualização automática da memória. Demanda sem evidência permanece como rascunho. Um agente não pode aprovar alteração nos próprios gates. E incidentes do Auto Dream entram no próximo ciclo de análise.

---

## 11. Evidence pack apresentado às pessoas

Toda decisão humana recebe um pacote curto, desenhado para permitir decidir sem reler todas as sessões — mas preservando os links para auditoria.

| Item | Conteúdo |
|---|---|
| Pergunta de decisão | uma frase |
| Recomendação | posição dos agentes |
| Alternativas | opções consideradas e descartadas |
| Riscos e trade-offs | o que se ganha e o que se aceita |
| Delta | mudanças desde a última aprovação |
| Evidências | resultado dos gates executados |
| Pendências | exceções e nível de confiança |
| Impacto | em produto, experiência e engenharia |
| Links | artefatos completos, código e execução |

---

# Parte IV — O que sustenta

## 12. Repo harness

### 12.1 Papel

O harness é o que torna o repositório compreensível para pessoas e agentes ao mesmo tempo. Ele converte padrões de engenharia em regras executáveis, oferece caminhos seguros e repetíveis para mudanças, reduz a dependência de contexto informal ou individual, e produz feedback acionável e evidência auditável.

Distinguem-se dois harnesses, e confundi-los produz duplicidade silenciosa. O **repo harness** vive dentro de cada repositório de código e viaja junto com o clone; o **workspace** organiza o trabalho do agente fora do código. A regra de decisão é simples: se a informação continua verdadeira quando outro time clona o repositório, ela é harness.

### 12.2 As cinco camadas

O repo harness se organiza em cinco camadas cumulativas. Cada uma elimina uma classe de falha, e a ordem de construção segue o retorno decrescente — contexto é o mais barato e o que mais reduz retrabalho; evidência só tem valor quando existe algo verificado para registrar.

| Camada | Responde | Materializa em |
|---|---|---|
| **Contexto** | o que este repositório é e quais regras valem | `AGENTS.md`, `docs/rules/` |
| **Procedimento** | como executar uma tarefa recorrente do jeito certo | skills, comandos, scripts |
| **Verificação** | o que precisa ser verdade antes de avançar | hooks, CI, políticas de merge |
| **Permissão** | o que este agente pode tocar e o que exige gente | `CODEOWNERS`, settings, ambientes |
| **Evidência** | como provar depois que estava correto | evidence pack, logs, artefatos |

A maturidade do harness é teto da autonomia, nunca consequência dela. O detalhamento — estrutura de arquivos, conteúdo de cada camada, o que muda com Agent Teams, níveis `HL0–HL3` e checklist de conformidade — está em [repo harness](repo-harness.md). A escada de gates está em [modelo operacional 90/10](operating-model-90-10.md#6-arquitetura-de-gates).

### 12.3 Skills

Skills nativas do Agent Team, em [`skills/`](../skills/):

| Grupo | Skills |
|---|---|
| Discovery, especificação e planejamento | `business-discovery`, `technical-discovery`, `write-feature`, `review-prd`, `create-spec`, `review-spec`, `review-cross-prd-spec`, `refine-spec` |
| Implementação e validação | `implement`, `dev-flow`, `fix-bug`, `analyse-bug`, `test-integration-local` |
| Revisão, publicação e documentação | `code-review`, `commit`, `update-pr`, `check-pr`, `update-docs` |
| Operação do workspace | `workspace-memory`, `workspace-projects`, `workspace-board` |

Extensões recomendadas, ainda não implementadas: intake e deduplicação; pesquisa e síntese de UX; threat modeling e privacidade; migração, rollout e rollback; incident response e post-mortem; telemetria e avaliação de agentes; atualização e verificação de documentação.

Toda skill declara objetivo, inputs, outputs, tools permitidas, critérios de parada, exemplos e testes.

### 12.4 Regras para gates baseados em IA

IA pode recomendar, explicar e priorizar achados — mas bloqueio automático exige regra reproduzível e evidência verificável, e achado probabilístico exige confirmação independente. O mesmo agente não produz e aprova sozinho a própria mudança, e agentes não alteram gates dentro do mesmo fluxo avaliado.

Mudança em rules, hooks ou CI eleva o risco automaticamente. Qualquer bypass exige pessoa autorizada, motivo, validade e plano de correção.

### 12.5 Tools por capacidade

As ferramentas são opções de implementação; o contrato do fluxo não deve depender de uma marca específica.

| Capacidade | Opções de implementação |
|---|---|
| Gestão, decisão e colaboração | backlog e roadmap (Linear, Jira, GitHub Projects); documentos e decisões (Markdown no repositório, Obsidian, Notion); comunicação (Slack, Teams); ADRs versionados e decision log |
| Pesquisa, experiência e design | repositório de research ou Dovetail; Figma, FigJam ou Penpot; Storybook e tokens versionados; testes de usabilidade, axe/Lighthouse e regressão visual |
| Código e compreensão da codebase | LSP, lint e formatação; typecheck e análise estática; Serena; Dora; busca estrutural, grafo de dependências e análise arquitetural; ambientes reproduzíveis e containers |
| Redução e gestão de contexto | RTK; índices de codebase e recuperação semântica autorizada; compactação de logs e evidence packs; budgets de contexto, tokens e custo por fase |
| Qualidade e segurança | frameworks de teste e mutation testing; SAST/code scanning (CodeQL); secret scanning; dependency review, SBOM e licenças; DAST e testes de contrato; policy as code |
| CI/CD e operação | GitHub Actions, GitLab CI ou Buildkite; preview environments e IaC; feature flags e rollout gradual; artifact registry e attestation; canary e rollback automatizado |
| Observabilidade e telemetria | OpenTelemetry; backend de observabilidade (Grafana stack, Datadog, New Relic); error tracking (Sentry); product analytics (PostHog, Amplitude); avaliação de prompts/agentes; dashboards de custo, qualidade, autonomia e fluxo |
| Portal e conhecimento | Backstage Software Catalog/TechDocs ou equivalente para ownership, catálogo e descoberta em escala |

Os artefatos que constituem o conhecimento do produto são fixos, independentemente da ferramenta escolhida:

| Artefato | Responde |
|---|---|
| `PRD.md` | por que e o que será entregue |
| Especificação de UX | jornada, fluxo, estados, conteúdo e acessibilidade |
| `SPEC.md` | comportamento e contratos esperados |
| `ADR.md` | decisões e consequências arquiteturais |
| `AGENTS.md` | instruções operacionais para agentes |
| `README.md` | uso, execução e visão geral do repositório |
| Histórico de PRs | mudanças, evidências e decisões locais |

### 12.6 Contrato de avaliação de uma ferramenta

Antes de adotar qualquer ferramenta, registre: problema que resolve e owner; etapa, input e output atendidos; integração com fontes canônicas; permissões, dados enviados e retenção; custo financeiro e cognitivo; API, automação e exportabilidade; evidência produzida e capacidade de auditoria; lock-in e plano de saída; métrica de sucesso e data de revisão.

### 12.7 Referências oficiais

- [GitHub Actions — workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows)
- [GitHub CodeQL — code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning)
- [GitHub — segurança da cadeia de suprimentos](https://docs.github.com/en/code-security/concepts/supply-chain-security/supply-chain-security)
- [OpenTelemetry — métricas e correlação entre sinais](https://opentelemetry.io/docs/specs/otel/metrics/)
- [Backstage — Software Catalog](https://backstage.io/docs/features/software-catalog/)
- [Backstage — TechDocs](https://backstage.io/docs/features/techdocs/)

Essas referências sustentam as capacidades sugeridas; não constituem decisão de adoção. A escolha passa pelo contrato de avaliação acima.

---

## 13. Governança e segurança

A governança do modelo se apoia em três camadas. A camada de **acesso** define permissões mínimas por agente e por etapa, exige aprovação humana para ações irreversíveis ou externas, mantém segredos fora de prompts, logs e artefatos, e minimiza, protege e retém dados pessoais por política.

A camada de **rastreabilidade** liga demanda, decisão, código e evidência, e registra autoria, ferramentas, modelos e versões utilizadas. A camada de **contenção** define critérios claros para interromper, escalar ou pedir decisão, documenta exceções com prazo e responsável, segrega produção, validação e aprovação, mantém kill switch e revogação de credenciais, e audita periodicamente as permissões de agentes e integrações.

### 13.1 Contrato de escalonamento

Um agente para e escala quando encontra requisito contraditório ou sem owner, confiança abaixo do limite definido, duas ou mais tentativas de correção sem progresso, mudança fora do escopo aprovado, necessidade de nova permissão ou acesso externo, falha não reproduzível ou evidência inconsistente, decisão irreversível ou impacto não calculável, ou divergência entre agentes sem critério objetivo de desempate.

---

## 14. Classificação de risco e autonomia

### 14.1 Classes de risco

| Classe | Caracteriza | Exige |
|---|---|---|
| **R0 — mínimo** | documentação, texto e formatação; sem mudança de comportamento, dados, secrets ou contratos | merge automático após gates; review humano por amostragem |
| **R1 — baixo** | refatoração interna ou mudança localizada, coberta por testes existentes, sem migração, segurança ou integração crítica | aprovação curta; deploy automático com observação |
| **R2 — médio** | novo comportamento ou mudança de contrato interno/integração; impacto reversível mas relevante | aprovação de produto ou Code Owner; canary e rollback |
| **R3 — alto** | dados persistidos, migrações, contratos públicos, autenticação, privacidade, pagamentos ou operação crítica | aprovações humana de produto e técnica antes de produção |
| **R4 — crítico** | impacto regulatório, financeiro, destrutivo ou de grande alcance | plano de mudança e rollback revisados manualmente; dupla aprovação, segregação de função e acompanhamento humano |

**Regras de classificação.** Um agente propõe o risco e outro tenta elevá-lo; o maior risco justificado prevalece. Redução manual exige justificativa registrada, mudança de escopo recalcula o risco, paths sensíveis elevam risco automaticamente, e dúvida não resolvida impede R0/R1.

### 14.2 Autonomia progressiva

| Nível | Significa |
|---|---|
| **A0 — assistido** | pessoas aprovam todas as transições |
| **A1 — execução autônoma** | agentes executam; pessoas aprovam decisões e merge |
| **A2 — merge por risco** | R0/R1 podem integrar por política |
| **A3 — entrega autônoma controlada** | baixo risco chega à produção com rollback comprovado |
| **A4 — orientado a exceções** | fluxo saudável ocorre sem intervenção; pessoas tratam decisões e anomalias |

Elevar autonomia exige, simultaneamente: histórico suficiente, baixa taxa de falha, gates confiáveis, poucos falsos positivos, rollback testado e telemetria íntegra. Nenhum desses critérios sozinho autoriza a subida.

---

# Parte V — Evolução

## 15. Fases de adoção

| Fase | Objetivo | Movimentos principais |
|---|---|---|
| **1 — Piloto assistido** | provar o contrato | um repositório e fluxo de baixo risco; papéis, artefatos e gates mínimos; aprovação humana em todas as transições; medir tempo, retrabalho, custo e falhas |
| **2 — Padronização** | tornar repetível | templates reutilizáveis; consolidar rules, skills, hooks e PR template; critérios comuns de entrada e saída; exceções documentadas por tipo de repositório; instituir as cerimônias do trio |
| **3 — Automação** | reduzir intervenção | roteamento automático entre agentes; gates por risco e paths; atualização automática de status, artefatos e evidências; telemetria ponta a ponta; escalar para pessoas somente decisões e exceções |
| **4 — Escala e melhoria contínua** | ampliar com segurança | expandir para outros times e repositórios; comparar fluxos sem ranking simplista; evoluir skills a partir de falhas recorrentes; revisar semanalmente regras, métricas e conhecimento; elevar autonomia por evidência |

---

## 16. Métricas iniciais do modelo

As métricas orientam investigação. **Nenhuma delas, isoladamente, representa produtividade ou qualidade do trio** — e usar uma delas como meta individual corrompe o sinal.

| Dimensão | Métricas |
|---|---|
| Fluxo | lead time (backlog→homologação); cycle time (implementação→merge); aprovação na primeira revisão e por gate; retrabalho após validação ou homologação |
| Qualidade | defeitos e regressões após entrega; cobertura dos critérios de aceite; falsos positivos por gate |
| Automação | % de gates automatizados; % de trabalho autônomo por classe de risco; falhas, retries e escalonamentos por fase |
| Custo humano | tempo humano em exceções e aprovações; custo por etapa, agente, modelo e entrega |
| Conhecimento | atualidade e uso da base de conhecimento; qualidade e completude do evidence pack |
| Resultado | outcome e adoção por entrega |

---

## 17. Decisões ainda em aberto

Estas pendências são reconhecidas e não bloqueiam o piloto, mas devem ser fechadas antes de escalar:

| Tema | Pendência |
|---|---|
| Orquestração | ferramenta que orquestrará o Agent Team |
| Autonomia | limites de autonomia de cada papel |
| Artefatos | formato canônico e ciclo de vida |
| Risco | critério de risco por tipo de mudança; gates obrigatórios por linguagem e repositório |
| Exceções | responsável por aprovar exceção fora do trio |
| Ambientes | estratégia para integração e homologação |
| Medição | como medir custo, qualidade e ganho de produtividade |
| Distribuição | como versionar e distribuir rules e skills compartilhadas |
| Telemetria | onde ficará a fonte canônica |
| Registro | qual ferramenta será sistema de registro para backlog e decisões |
| Dados | política de retenção das sessões e dados dos agentes |
| Processo | quais cerimônias podem ser eliminadas após maturidade comprovada |

---

## 18. Próximos passos para o piloto de três pessoas

1. Escolher o repositório e um caso R1 real.
2. Nomear PM, UX e Tech Lead e registrar seus direitos de decisão.
3. Mapear o fluxo atual e os principais gargalos.
4. Definir o conjunto mínimo de agentes e permissões.
5. Criar templates mínimos de `PB`, `PRD`, UX spec, `SPEC` e evidence pack.
6. Implementar gates essenciais no repo harness.
7. Instrumentar IDs, eventos, custo, duração e resultados dos gates.
8. Executar um ciclo completo de ponta a ponta.
9. Realizar H6 com dados do ciclo e criar no máximo três melhorias prioritárias.
10. Repetir por três ciclos antes de elevar autonomia ou adicionar cerimônias.

---

## Resultado esperado

O trio mantém autoridade clara sobre produto, experiência e tecnologia, enquanto os agentes absorvem a maior parte da pesquisa operacional, produção, crítica, execução, validação e documentação.

O sistema não depende de heroísmo nem de contexto oral: cada passagem possui contrato, cada decisão possui owner, cada entrega possui evidência e cada ciclo deixa o próximo mais seguro, rápido e autônomo.
