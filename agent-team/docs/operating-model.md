---
title: Agent Team — sistema operacional do trio humano
status: canonical
updated_at: 2026-08-08
---

# Agent Team — sistema operacional do trio humano

> Documento proposto para substituir [Agent Team — visão macro](archive/original-vision.md) como visão canônica. Preserva o conteúdo, os tools e os gates do material original e os reorganiza para um time pilotado por **Product Manager, UX e Tech Lead**. Detalhamentos relacionados: [modelo operacional 90/10](operations/operating-model-90-10.md) · [fluxo visual completo](operations/end-to-end-journey.md) · [fluxos por fase](operations/journey-by-phase.md) · [workflows multiagente](workflows/README.md) · [workspace do Tech Lead](architecture/tech-lead-workspace.md).

> Agentes: [catálogo e contratos detalhados](agents/catalog.md) · [Meeting Context Agent para transcrições](agents/meeting-context-agent.md).

## 1. Propósito

Transformar uma necessidade de negócio em software validado por meio de um pequeno núcleo humano que dirige uma força de trabalho de agentes especializados.

O modelo deve:

- combinar agentes especializados, pessoas e automações
- manter decisões, código e documentação sincronizados
- produzir evidências em todas as etapas do ciclo
- escalar a entrega sem perder segurança e governança
- reservar atenção humana para intenção, julgamento, risco e responsabilidade
- tornar execução, validação e coleta de evidências progressivamente autônomas
- melhorar o próprio sistema de trabalho a cada ciclo

O trio humano não tenta executar manualmente todo o trabalho. Ele opera o sistema:

- **Product Manager:** dirige valor, prioridade e resultado de negócio
- **UX:** dirige entendimento do usuário, experiência e qualidade de uso
- **Tech Lead:** dirige viabilidade, arquitetura, qualidade técnica e risco operacional
- **Agentes:** pesquisam, propõem, implementam, criticam, validam e documentam
- **Automações:** executam verificações determinísticas, bloqueios e rastreabilidade

---

## 2. Princípios operacionais

- Pessoas definem prioridade, restrições, limites de autonomia e aprovação final.
- Agentes executam trabalho especializado e produzem evidências.
- Cada etapa possui entrada, saída, owner humano e critério de passagem.
- O responsável humano decide; o agente primário prepara e recomenda.
- Quem produz uma mudança não é o único responsável por validá-la.
- Divergências relevantes entre agentes são resolvidas pelo owner humano do domínio.
- A etapa termina com um artefato coerente, não com análises isoladas.
- O repositório concentra regras e contexto executável do produto.
- O harness transforma padrões em verificações repetíveis.
- Mudanças pequenas, reversíveis e rastreáveis reduzem risco e retrabalho.
- Comunicação assíncrona é o padrão; reunião existe para decidir, não para narrar status.
- Aprovação humana deve receber síntese, alternativas, riscos e evidências, não contexto bruto.
- Uma mudança material invalida a aprovação relacionada.
- Ausência de resposta nunca equivale a aprovação.
- Autonomia aumenta apenas quando métricas e gates demonstram segurança.

## 3. Modelo de atuação dos Agent Teams

- Cada fase pode acionar um time temporário de agentes especializados.
- O [catálogo de agentes](agents/catalog.md) define os contratos e limites de cada papel.
- Cada agente analisa o problema a partir de uma responsabilidade explícita.
- Um agente primário conduz e consolida o artefato da fase.
- Agentes adversariais procuram ambiguidades, gaps, riscos e suposições frágeis.
- As contribuições e divergências são registradas antes da consolidação.
- O owner humano intervém em decisão de valor, experiência, risco ou exceção — não em toda execução.
- O contexto passa entre fases por artefatos versionados e evidence packs.
- Agentes recebem acesso mínimo, escopo delimitado e condição objetiva de parada.

### Estrutura mínima de uma missão para agentes

- objetivo e resultado esperado
- contexto e fontes canônicas
- escopo e fora de escopo
- artefato de entrada
- artefato de saída
- critérios de aceite
- gates obrigatórios
- ferramentas e permissões autorizadas
- classe de risco
- condição de escalonamento
- owner humano da decisão

---

## 4. O trio humano

### 4.1 Product Manager — dono do valor e da prioridade

#### Responsabilidades

- manter visão, objetivos, outcomes e roadmap
- ordenar o backlog por valor, urgência, risco e aprendizado
- formular o problema antes de comprometer uma solução
- identificar stakeholders, restrições comerciais e resultados esperados
- definir escopo, fora de escopo e critérios de sucesso
- garantir rastreabilidade entre problema, investimento, entrega e resultado
- decidir avançar, ajustar, adiar ou encerrar um item
- homologar valor com stakeholders e registrar pendências
- priorizar melhorias originadas pela telemetria
- operar agentes de intake, discovery, pesquisa, planejamento e validação de produto

#### Inputs recorrentes

- estratégia e objetivos do negócio
- necessidades de clientes e stakeholders
- pesquisas e evidências de UX
- métricas de produto e operação
- restrições, riscos e estimativas do Tech Lead
- feedback de homologação e produção
- incidentes, custo do fluxo e oportunidades de melhoria

#### Outputs recorrentes

- backlog ordenado e com owner
- objetivo e outcome esperado
- `PB.md` aprovado
- `PRD.md` consolidado
- escopo e fora de escopo explícitos
- métricas e critérios de sucesso
- decisões H1, H2 e aceite de produto
- prioridade das demandas de melhoria
- comunicação de resultado aos stakeholders

#### Não é responsabilidade exclusiva do PM

- desenhar sozinho a experiência
- definir arquitetura ou solução técnica
- aprovar exceção técnica sem o Tech Lead
- substituir evidência de usuário por opinião de stakeholder

### 4.2 UX — dono da experiência e da evidência sobre o usuário

#### Responsabilidades

- planejar e executar pesquisa proporcional ao risco
- representar necessidades, contexto e limitações dos usuários
- mapear jornadas, fluxos, tarefas e pontos de fricção
- definir princípios de experiência, conteúdo e interação
- especificar estados nominal, vazio, loading, erro, permissão e recuperação
- garantir acessibilidade, consistência e usabilidade
- produzir protótipos na fidelidade necessária para decidir
- validar hipóteses antes e depois da implementação
- acompanhar qualidade da experiência na homologação e em produção
- operar agentes de pesquisa, síntese, UX writing, prototipação e avaliação heurística

#### Inputs recorrentes

- problema, público e outcome definidos com o PM
- dados de comportamento, suporte e analytics
- restrições técnicas e oportunidades informadas pelo Tech Lead
- design system e padrões existentes
- feedback de stakeholders e usuários
- resultados de experimentos e homologação

#### Outputs recorrentes

- plano e evidências de pesquisa
- personas ou segmentos quando úteis à decisão
- jornada atual e jornada desejada
- fluxos, wireframes e protótipos
- especificação de UX, conteúdo, estados e acessibilidade
- hipóteses e riscos de experiência
- critérios de aceite de UX
- relatório de validação e recomendações pós-entrega

#### Não é responsabilidade exclusiva do UX

- decidir prioridade de negócio
- prometer escopo sem alinhamento com PM e Tech Lead
- produzir telas sem problema e hipótese explícitos
- validar experiência apenas por aderência visual

### 4.3 Tech Lead — dono da integridade técnica e do risco operacional

#### Responsabilidades

- avaliar viabilidade e risco desde o discovery
- definir arquitetura, contratos, integrações e estratégia de dados
- registrar alternativas, trade-offs e ADRs relevantes
- decompor a solução em unidades pequenas, independentes e verificáveis
- definir estratégia de testes, observabilidade, rollout e rollback
- manter fronteiras arquiteturais, padrões e débito técnico sob controle
- definir e evoluir rules, hooks, gates, skills e harness do repositório
- proteger segurança, privacidade, confiabilidade e manutenibilidade
- decidir exceções técnicas e escalonar riscos R3/R4
- operar agentes de especificação, engenharia, QA, segurança, arquitetura, review e release

#### Inputs recorrentes

- `PB.md`, `PRD.md` e especificação de UX
- arquitetura e contratos existentes
- SLOs, incidentes e telemetria técnica
- inventário de dependências e restrições de plataforma
- requisitos de segurança, privacidade e compliance
- capacidade do time e custo operacional

#### Outputs recorrentes

- avaliação de viabilidade e risco
- `PLAN.md`, `SPEC.md`, `ADR.md`, `TASKS.md` e `CHECKLIST.md`
- estratégia de implementação e testes
- plano de migração, rollout e rollback quando aplicável
- gates e evidence pack técnico
- decisão H3 e recomendação técnica em H4/H5
- backlog de saúde técnica e melhorias do harness

#### Não é responsabilidade exclusiva do Tech Lead

- redefinir objetivo de produto por conveniência técnica
- escolher experiência sem participação do UX
- aprovar o próprio desvio de arquitetura sem revisão independente
- transformar toda decisão técnica em reunião humana

### 4.4 Responsabilidade compartilhada

Os três são conjuntamente responsáveis por:

- qualidade do problema antes da solução
- coerência entre valor, experiência e viabilidade
- riscos explícitos e decisões rastreáveis
- critérios de aceite observáveis
- proteção dos dados e dos usuários
- saúde do fluxo agentico
- aprendizado após a entrega

Nenhuma pessoa é um “tradutor” passivo para outra. PM, UX e Tech Lead trazem decisões do próprio domínio e constroem juntos o contrato que os agentes executarão.

---

## 5. Direitos de decisão

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

### Regra de desempate

- valor, prioridade e outcome: decide o PM
- experiência, usabilidade e acessibilidade: decide o UX
- arquitetura, segurança e confiabilidade: decide o Tech Lead
- conflito entre domínios: registrar alternativas, impacto e decisão conjunta
- risco irreversível, regulatório ou de grande alcance: escalar ao sponsor ou responsável formal

---

## 6. Contrato de passagem entre os três profissionais

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

### Definition of Ready para execução agentica

- problema e usuário explícitos
- outcome e métrica definidos
- owner humano conhecido
- escopo e fora de escopo claros
- fluxo e estados de UX suficientes para a tarefa
- contratos e restrições técnicas suficientes
- critérios de aceite verificáveis
- classe de risco e gates definidos
- acessos e ferramentas autorizados
- dúvidas críticas resolvidas ou assumidas de forma explícita

### Definition of Done do ciclo

- critérios de produto, UX e engenharia cobertos
- testes e gates obrigatórios aprovados
- impacto arquitetural avaliado
- riscos e limitações conhecidos
- documentação e fontes canônicas atualizadas
- aprovações humanas e automatizadas identificadas
- backlog, artefatos, commits, PR, release e telemetria vinculados
- rollout observado sem regressão relevante ou com plano de correção
- aprendizados e melhorias encaminhados ao loop correto

---

## 7. Cerimônias humanas

As cerimônias são pontos de decisão do trio. Preparação, análise, atualização de status e geração de artefatos ficam preferencialmente com os agentes e automações.

### 7.1 Pulso assíncrono diário

- **Cadência:** diária; leitura em até 10 minutos por pessoa
- **Participantes:** PM, UX e Tech Lead
- **Preparação por agentes:** estado do fluxo, mudanças, bloqueios, risco e decisões requeridas
- **Inputs:** quadro atualizado, evidence packs parciais, alertas e divergências
- **Agenda:** somente bloqueios, novas informações e pedidos de decisão
- **Outputs:** owners, prazo da decisão e replanejamento registrado
- **Não deve virar:** reunião diária de relato individual

### 7.2 Triagem e prioridade

- **Cadência:** semanal, 30–45 minutos
- **Owner:** PM
- **Participantes:** PM, UX e Tech Lead
- **Inputs:** novos itens, métricas, feedback, incidentes, dependências e capacidade
- **Perguntas:** qual problema entra, qual sai e o que precisa de discovery?
- **Outputs:** backlog ordenado, owner, risco inicial e próximos discoveries
- **Gate:** contexto, prioridade e responsável minimamente claros

### 7.3 Kickoff de discovery — H1

- **Cadência:** por oportunidade; 30–45 minutos
- **Owner:** PM
- **Inputs:** intake consolidado, evidências existentes e perguntas abertas
- **Contribuição do PM:** problema, valor, stakeholders e outcome
- **Contribuição do UX:** lacunas sobre usuário e plano de pesquisa
- **Contribuição do Tech Lead:** restrições, dependências e risco de viabilidade
- **Outputs:** missão de discovery, `PB.md` inicial, agentes acionados e timebox
- **Decisão final:** avançar, ajustar, adiar ou encerrar

### 7.4 Refinamento de produto e experiência — H2

- **Cadência:** por item candidato; 45–60 minutos
- **Owner:** PM; UX co-owner da experiência
- **Inputs:** `PB.md`, pesquisa, jornada, protótipo, PRD proposto e crítica adversarial
- **Perguntas:** é isto que construiremos, para quem e com qual resultado?
- **Outputs:** `PRD.md`, especificação de UX, critérios de aceite e escopo aprovado
- **Gate:** gaps críticos tratados, ambiguidades reduzidas e sucesso mensurável

### 7.5 Revisão de solução e risco — H3

- **Cadência:** sob demanda; obrigatória para ADR, exceção ou risco elevado; 30–60 minutos
- **Owner:** Tech Lead
- **Inputs:** `PLAN.md`, `SPEC.md`, ADR, alternativas, threat model, plano de testes e crítica adversarial
- **Contribuição do PM:** impacto em outcome, prazo e escopo
- **Contribuição do UX:** impacto em jornada, conteúdo, acessibilidade e estados
- **Outputs:** decisão técnica, trade-offs aceitos, tarefas executáveis e riscos com owner
- **Gate:** rastreabilidade, gaps críticos tratados e validação viável

### 7.6 Review de entrega — H4

- **Cadência:** por incremento ou release candidate; 20–30 minutos
- **Owner:** PM para valor; Tech Lead para integridade técnica; UX para experiência
- **Inputs:** demo preparada por agentes, evidence pack, critérios de aceite e mudanças desde H2/H3
- **Perguntas:** entrega o outcome acordado, funciona bem e pode ser integrada?
- **Outputs:** aceite, ajustes, novos itens ou rejeição justificada
- **Gate:** revisão aprovada, CI verde e ausência de bloqueadores

### 7.7 Decisão de release — H5

- **Cadência:** por release; apenas síncrona quando risco exigir; 10–20 minutos
- **Owner:** Tech Lead; PM coaprova R3/R4
- **Inputs:** release candidate, risco, rollout, rollback, SLOs e sinais de saúde
- **Outputs:** liberar, pausar, reduzir exposição ou retornar à implementação
- **Gate:** ambiente, secrets, migração, observabilidade e rollback verificados

### 7.8 Telemetria e melhoria — H6

- **Cadência:** semanal, 45–60 minutos
- **Owner:** trio, com facilitação rotativa
- **Inputs:** relatório de telemetria, padrões, incidentes, custo, feedback e propostas do Auto Dream
- **Perguntas:** o sistema aprendeu corretamente e qual melhoria merece investimento?
- **Outputs:** memória validada, demandas P0–P3, owners, experimentos e alterações de processo propostas
- **Gate:** evidência rastreável, hipótese separada de aprendizado e mudança sensível revisada

### 7.9 Revisão mensal do sistema

- **Cadência:** mensal, 60–90 minutos
- **Participantes:** trio; sponsor ou enablement quando necessário
- **Inputs:** tendências de outcome, qualidade, fluxo, custo, autonomia e falsos positivos dos gates
- **Outputs:** ajustes de capacidade, políticas, ferramentas, gates e nível de autonomia
- **Regra:** não usar uma métrica isolada para elevar autonomia

### 7.10 Quarterly outcome review

- **Cadência:** trimestral, 60–90 minutos
- **Owner:** PM
- **Inputs:** outcomes, estratégia, pesquisas, saúde técnica, custo e aprendizados acumulados
- **Outputs:** prioridades do próximo ciclo, apostas encerradas e capacidades a desenvolver

---

## 8. Ciclo de desenvolvimento de ponta a ponta

### 0. Intake e triagem de backlog

- **Workflow:** [intake e triagem](workflows/00-intake-and-triage.md)
- **Owner humano:** Product Manager
- **Agentes:** Intake Agent + Product Manager Agent
- **Objetivo:** registrar, deduplicar, contextualizar e priorizar necessidades
- **Inputs:** problema, oportunidade, solicitação, feedback, incidente ou melhoria
- **Atividades:** validar campos, relacionar produto/repositório, identificar duplicidade e propor risco
- **Outputs:** Work Item priorizável, contexto inicial, owner e risco preliminar
- **Gate:** problema, prioridade, rastreabilidade e responsável minimamente claros
- **Cerimônia:** triagem e prioridade

### 1. Discovery

- **Workflow:** [discovery e research](workflows/01-discovery-and-research.md)
- **Owner humano:** PM; UX e Tech Lead respondem por seus domínios
- **Agent Team:** Product Discovery Team
  - Product Manager Agent
  - UX Specification Agent
  - Tech Lead Discovery Agent
- **Objetivo:** compreender problema, usuário, contexto, valor e viabilidade inicial
- **Inputs:** Work Item priorizado, dados, pesquisas existentes, restrições e perguntas
- **Dinâmica:** investigação paralela, registro de hipóteses, síntese pelo Product Manager Agent e crítica dos demais
- **Outputs:** `PB.md`, evidências, jornada inicial, restrições, riscos e perguntas abertas
- **Conteúdo mínimo:** problema, usuários, jornada, valor, restrições e riscos
- **Gate:** problema validado, experiência desejada compreendida e viabilidade inicial avaliada
- **Cerimônia:** kickoff de discovery / H1

### 2. Planejamento de produto e experiência

- **Workflow:** [planejamento de produto e UX](workflows/02-product-and-ux-planning.md)
- **Owner humano:** PM para produto; UX para experiência
- **Agent Team:** Product Planning Team
  - Product Manager Agent
  - UX Specification Agent
  - Adversarial Product Manager Agent
  - agentes de pesquisa, conteúdo ou prototipação quando necessários
- **Objetivo:** transformar o problema em uma proposta clara, testável e utilizável
- **Inputs:** `PB.md`, evidências de usuário, restrições e decisão H1
- **Dinâmica:** proposta → protótipo/especificação de UX → crítica adversarial → revisão → consolidação
- **Outputs:**
  - `PRD.md`
  - jornada e fluxo desejados
  - wireframe ou protótipo na fidelidade necessária
  - estados, conteúdo e critérios de acessibilidade
  - critérios de sucesso e aceite
- **Conteúdo mínimo:** objetivos, usuários, jornadas, escopo, fora de escopo, requisitos e métricas
- **Gate:** gaps críticos tratados, ambiguidades reduzidas e critérios de sucesso aprovados
- **Cerimônia:** refinamento de produto e experiência / H2

### 3. Especificação técnica

- **Workflow:** [especificação técnica](workflows/03-technical-specification.md)
- **Owner humano:** Tech Lead
- **Agent Team:** Technical Specification Team
  - Specification Tech Lead Agent
  - Adversarial Tech Lead Agent
  - Security, Data ou Platform Agent quando o risco exigir
- **Objetivo:** definir como construir, validar, liberar e operar a solução
- **Inputs:** `PB.md`, `PRD.md`, especificação de UX, arquitetura, contratos e SLOs
- **Dinâmica:** especificação → revisão crítica → resposta aos gaps → decisão
- **Outputs:**
  - `PLAN.md` — estratégia de implementação
  - `ADR.md` — decisões arquiteturais relevantes
  - `SPEC.md` — comportamento e contratos técnicos
  - `TASKS.md` — unidades pequenas de execução
  - `CHECKLIST.md` — critérios verificáveis de aceite
  - plano de testes, rollout, rollback e observabilidade conforme risco
- **Conteúdo mínimo:** arquitetura, alternativas, trade-offs, riscos e validação
- **Gate:** gaps críticos tratados, trade-offs registrados e tarefas executáveis
- **Cerimônia:** revisão de solução e risco / H3 quando necessária

### 4. Implementação

- **Workflow:** [implementação autônoma](workflows/04-autonomous-implementation.md)
- **Owner humano:** Tech Lead por política e exceção
- **Agentes:** Orchestrator Agent + Software Engineer Agents
- **Suporte:** repo harness, skills e ferramentas de código
- **Objetivo:** implementar uma tarefa pequena por vez
- **Inputs:** tarefa, SPEC, critérios, contexto, permissões e gates
- **Atividades:** código, testes, documentação, commits e evidências
- **Outputs:** mudança funcional pronta para validação e diff rastreável
- **Gate:** verificações locais rápidas aprovadas
- **Ação humana:** apenas diante de decisão, exceção ou escalonamento

### 5. Validação adversarial

- **Workflow:** [validação adversarial](workflows/05-adversarial-validation.md)
- **Owner humano:** Tech Lead; PM e UX validam seus critérios
- **Agentes:** Validation / QA, Security, Architecture e Reviewer Agents
- **Suporte:** repo harness e ambientes reproduzíveis
- **Objetivo:** provar aderência à especificação e procurar falhas que o autor não encontrou
- **Inputs:** mudança, PRD, UX spec, SPEC, CHECKLIST e classe de risco
- **Atividades:** testes, segurança, arquitetura, acessibilidade, regressão e mutation testing quando aplicável
- **Outputs:** evidências vinculadas aos critérios e achados classificados
- **Gate:** checklist completo e ausência de bloqueadores

### 6. Code review, PR e decisão de merge

- **Workflow:** [PR e merge](workflows/06-pr-and-merge.md)
- **Owner humano:** Tech Lead ou Code Owner conforme risco
- **Agentes:** PR Agent + Reviewer Agent
- **Objetivo:** avaliar qualidade, risco, manutenibilidade e prontidão para integração
- **Inputs:** diff, commits, resultados de validação e evidence pack
- **Atividades:** revisão de código, testes, impacto arquitetural, contratos e documentação
- **Outputs:** PR rastreável, aprovação ou solicitações de ajuste
- **Gate:** revisão aprovada, CI verde, branch atualizada e aprovações válidas
- **Cerimônia:** review de entrega / H4 quando exigido pela política

### 7. Homologação

- **Workflow:** [homologação](workflows/07-release-candidate-validation.md)
- **Owners humanos:** PM para valor; UX para experiência; stakeholder quando necessário
- **Agentes:** Release Agent + Product Validation Agent
- **Objetivo:** confirmar valor e comportamento no cenário representativo
- **Inputs:** release candidate, critérios de aceite, ambiente e dados de teste
- **Atividades:** preview, smoke, E2E, acessibilidade, demonstração e coleta de evidências
- **Outputs:** aceite, evidências e pendências registradas
- **Gate:** critérios de aceite validados ou plano de correção explícito

### 8. Entrega e observação

- **Workflow:** [produção e observação](workflows/08-production-release-and-observation.md)
- **Owner humano:** Tech Lead; PM coaprova exposição R3/R4
- **Agentes:** Release Agent + Observability Agent
- **Objetivo:** liberar com exposição controlada e provar saúde no uso real
- **Inputs:** release candidate aprovado, plano de rollout, rollback, SLOs e alertas
- **Atividades:** deploy progressivo, feature flag quando aplicável, monitoramento e comparação com baseline
- **Outputs:** versão liberada, sinais de saúde, rollback/pausa quando necessário e changelog
- **Gate:** ambiente autorizado, migração compatível e janela pós-deploy sem regressão relevante
- **Cerimônia:** decisão de release / H5 conforme risco

### 9. Atualização da base de conhecimento

- **Workflow:** [curadoria de conhecimento](workflows/09-knowledge-curation.md)
- **Owner humano:** owner do domínio alterado
- **Agente:** Knowledge Agent
- **Cadência:** contínua + revisão automatizada semanal
- **Objetivo:** manter documentação alinhada ao produto real
- **Inputs:** decisões, código, PR, homologação, release e incidentes
- **Atividades:** consolidar decisões, aprendizados e mudanças; procurar contradições e obsolescência
- **Outputs:** fontes canônicas e conhecimento reutilizável atualizados
- **Gate:** documentação atual, rastreável e sem contradições não resolvidas

## 10. Telemetria e melhoria contínua — Auto Dream

- **Workflow:** [telemetria e melhoria contínua](workflows/10-continuous-improvement.md)
- **Owner humano:** trio; cada demanda retorna ao owner do domínio
- **Agentes:** Telemetry/Observability Agent + Auto Dream Agent + Critic Agent independente
- **Trigger:** coleta contínua, síntese semanal e execução extraordinária após incidente relevante
- **Objetivo:** observar o sistema de trabalho, aprender com evidência e melhorar produto, agentes e fluxo
- **Escopo:** produto, UX, engenharia, agentes, prompts, processo, harness, skills, scripts, ferramentas, hooks, gates, documentação e arquitetura do workflow
- **Cerimônia:** telemetria e melhoria / H6

### 10.1 Por que “Telemetria e melhoria”

“Auto Dream” descreve um mecanismo. “Telemetria e melhoria” descreve o resultado operacional: enxergar como o sistema se comporta, distinguir sinal de ruído e converter evidência em aprendizado ou ação.

Sem telemetria, melhoria contínua vira opinião. Sem retorno ao backlog e à memória, telemetria vira dashboard decorativo.

### 10.2 Eventos e correlação mínima

Cada evento relevante deve carregar, quando aplicável:

- `work_item_id`, produto e repositório
- fase, agente, modelo, versão de prompt/skill e tool usada
- session/run ID e timestamp
- input, output e status da execução
- duração, tokens, custo e tamanho de contexto
- retry, fallback, bloqueio e escalonamento
- gate, resultado, evidência e duração
- decisão humana, owner e motivo
- commit, PR, release e ambiente
- classe de risco e nível de autonomia
- proteção ou anonimização de dados sensíveis

O padrão recomendado é instrumentar logs, métricas e traces correlacionáveis, com taxonomia versionada e política de retenção.

### 10.3 Entradas do ciclo

- sessões e decisões dos agentes
- evidence packs e feedbacks humanos
- falhas, retries, bloqueios e escalonamentos
- resultados de hooks, CI, homologação e deploy
- incidentes, rollbacks e defeitos escapados
- métricas de tempo, custo, qualidade, UX e autonomia
- feedback de usuário e sinais de produto
- demandas de melhoria geradas anteriormente

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

- identificar o que funcionou, para quem e em qual contexto
- registrar evidências, origem, data e condições de reutilização
- verificar duplicidade, contradição e validade temporal
- propor inclusão, atualização ou remoção no `MEMORY.md`
- evitar transformar preferência isolada em regra global
- exigir aprovação humana para memória sensível

#### Gate de memória

- evidência vinculada à conclusão
- escopo e contexto de aplicação explícitos
- ausência de secrets ou dados pessoais
- nenhuma contradição não resolvida
- conhecimento acionável e reutilizável
- mudança sensível revisada por pessoa responsável

### 10.6 Loop B — falha ou oportunidade de melhoria

- descrever sintoma, impacto e etapa afetada
- identificar causa provável e evidências
- registrar frequência e alcance
- propor ação corretiva e resultado esperado
- gerar demanda rastreável no backlog
- relacionar sessões, execuções e incidentes de origem
- detectar e vincular duplicidades

Tipos de melhoria preservados e ampliados:

- produto ou experiência
- processo ou cerimônia
- harness
- skill ou prompt
- script, ferramenta ou integração
- hook ou gate
- arquitetura do workflow
- documentação, contexto ou memória
- observabilidade, segurança ou custo

#### Estrutura mínima da demanda

- título orientado ao problema
- sintoma e impacto
- evidências e frequência
- hipótese de causa-raiz
- melhoria proposta
- critério de aceite mensurável
- prioridade e classe de risco sugeridas
- owner recomendado
- links para sessões e artefatos relacionados

#### Priorização

- **P0:** risco crítico, segurança ou perda de dados
- **P1:** falha recorrente que bloqueia o fluxo
- **P2:** retrabalho, custo ou baixa confiabilidade
- **P3:** otimização e melhoria incremental
- frequência não substitui impacto
- o Auto Dream recomenda; o owner humano decide e o PM ordena o backlog

### 10.7 Painel mínimo do trio

#### Produto e UX — PM + UX

- outcome e adoção da entrega
- conversão ou conclusão da tarefa principal
- erros de usuário, abandono e tempo na tarefa
- feedback qualitativo e defeitos de experiência
- acessibilidade e critérios de UX não atendidos

#### Fluxo — trio

- lead time: backlog até homologação
- cycle time: implementação até merge
- tempo por fase e tempo esperando decisão humana
- taxa de aprovação na primeira passagem por gate
- retrabalho após validação ou homologação
- bloqueios, retries e escalonamentos
- percentual de gates automatizados
- percentual de execução autônoma por classe de risco

#### Engenharia — Tech Lead

- falhas de build, testes e CI
- defeitos e regressões pós-entrega
- cobertura dos critérios de aceite
- change failure rate e tempo de recuperação
- violações arquiteturais, segurança e dependências
- falsos positivos e tempo gasto por gate

#### Agentes e custo — trio

- tokens, custo e duração por fase, agente e entrega
- taxa de sucesso sem intervenção
- número de tentativas até conclusão
- falhas por tool, skill, prompt e modelo
- qualidade do evidence pack
- tempo humano em exceções e aprovações
- atualidade e uso da base de conhecimento

### 10.8 Saídas do ciclo

- `MEMORY.md` atualizado com aprendizados validados
- demandas de melhoria criadas ou enriquecidas no backlog
- relatório semanal curto com padrões, tendências e qualidade dos dados
- métricas do sistema de trabalho atualizadas
- hipóteses inconclusivas mantidas para observação futura
- experimento com owner, baseline, prazo e critério de sucesso

### 10.9 Gate de conclusão

- fontes processadas e rastreáveis
- qualidade e lacunas dos dados explícitas
- aprendizados separados de hipóteses
- falhas relevantes convertidas em demandas
- duplicidades e contradições tratadas
- mudanças sensíveis revisadas
- nenhum dado confidencial persistido indevidamente

### 10.10 Falhas do próprio ciclo

- falha de coleta abre alerta e impede conclusão silenciosamente parcial
- baixa confiança mantém o item como hipótese
- contradição bloqueia atualização automática da memória
- demanda sem evidência permanece como rascunho
- agente não pode aprovar alteração nos próprios gates
- incidentes do Auto Dream entram no próximo ciclo de análise

---

## 11. Evidence pack apresentado às pessoas

Toda decisão humana recebe um pacote curto:

- pergunta de decisão em uma frase
- recomendação dos agentes
- alternativas consideradas
- principais riscos e trade-offs
- mudanças desde a última aprovação
- evidências dos gates executados
- pendências, exceções e nível de confiança
- impacto em produto, experiência e engenharia
- links para artefatos completos, código e execução

O evidence pack deve permitir decidir sem reler todas as sessões, mas preservar links para auditoria.

---

## 12. Repo harness

### 12.1 Papel

- tornar o repositório compreensível para pessoas e agentes
- converter padrões de engenharia em regras executáveis
- oferecer caminhos seguros e repetíveis para mudanças
- reduzir dependência de contexto informal ou individual
- produzir feedback acionável e evidência auditável

### 12.2 Skills

Conteúdo original preservado:

- `speckit-*` — especificação, plano, tarefas e implementação
- `my-tcl` — aplicação do ciclo de desenvolvimento
- `pr-template` — contexto, riscos, evidências e checklist do PR
- skills de domínio — procedimentos específicos do produto

Extensões recomendadas:

- skill de intake e deduplicação
- skill de pesquisa e síntese de UX
- skill de threat modeling e privacidade
- skill de migração, rollout e rollback
- skill de incident response e post-mortem
- skill de telemetria e avaliação de agentes
- skill de atualização e verificação de documentação

Toda skill deve declarar objetivo, inputs, outputs, tools permitidas, critérios de parada, exemplos e testes.

### 12.3 Rules

- arquitetura e fronteiras entre módulos
- convenções e nomes de objetos
- padrões aceitos e padrões proibidos
- injeção de dependência e composição
- gitflow e estratégia de branches
- critérios de validação e homologação
- propriedade por paths e Code Owners
- classificação de risco e permissões por fase
- segurança, privacidade e uso de dados
- SLOs, observabilidade, rollout e rollback
- estratégia de testes:
  - unitários
  - arquitetura
  - integração / TAAC
  - contrato
  - end-to-end
  - acessibilidade
  - mutação

### 12.4 Hooks e gates locais

#### Pre-commit — feedback rápido

- lint e formatação
- typecheck
- testes unitários afetados
- testes de arquitetura
- consistência entre código, PRD e SPEC

#### Pre-push — validação ampliada

- cobertura mínima definida pelo projeto
- código morto e débito técnico bloqueante
- vazamento de secrets
- integração / TAAC em container
- impacto em contratos e compatibilidade
- dependency review e licenças quando aplicável

#### CI — validação independente

- repetir gates críticos em ambiente limpo
- executar build, testes, segurança e arquitetura
- selecionar checks conforme risco e paths alterados
- gerar evidências auditáveis
- impedir merge quando houver bloqueadores

#### Gate de merge

- confirmar aprovações e status checks
- confirmar proveniência da automação
- impedir bypass silencioso e force push
- invalidar aprovação quando o diff mudar materialmente

#### Gate de ambiente

- liberar secrets somente após autorização
- restringir branches e artefatos permitidos
- validar migração, backup e compatibilidade
- exigir aprovação conforme risco
- integrar sinais de observabilidade e change management

#### Gate pós-deploy

- comparar métricas com baseline
- interromper rollout diante de regressão
- reverter automaticamente quando seguro
- abrir incidente quando ação humana for necessária

### 12.5 Regras para gates baseados em IA

- IA pode recomendar, explicar e priorizar achados.
- Bloqueio automático exige regra reproduzível e evidência verificável.
- Achado probabilístico exige confirmação independente.
- O mesmo agente não produz e aprova sozinho a própria mudança.
- Agentes não alteram gates dentro do mesmo fluxo avaliado.
- Mudança em rules, hooks ou CI eleva o risco automaticamente.
- Bypass exige pessoa autorizada, motivo, validade e plano de correção.

### 12.6 Tools por capacidade

As ferramentas são opções de implementação; o contrato do fluxo não deve depender de uma marca específica.

#### Gestão, decisão e colaboração

- gerenciador de backlog e roadmap: Linear, Jira, GitHub Projects ou equivalente
- documentos e decisões: Markdown no repositório, Obsidian, Notion ou equivalente
- comunicação: Slack, Teams ou equivalente
- registro de decisão: ADRs versionados e decision log

#### Pesquisa, experiência e design

- pesquisa e síntese: repositório de research, Dovetail ou equivalente
- fluxos e protótipos: Figma, FigJam, Penpot ou equivalente
- design system: Storybook e tokens versionados
- avaliação: testes de usabilidade, axe/Lighthouse e regressão visual

#### Código e compreensão da codebase

- LSP, lint e formatação
- typecheck e análise estática
- Serena
- Dora
- busca estrutural, grafo de dependências e análise arquitetural
- ambientes de desenvolvimento reproduzíveis e containers

#### Redução e gestão de contexto

- RTK
- índices de codebase e recuperação semântica autorizada
- compactação de logs e evidence packs
- budgets de contexto, tokens e custo por fase

#### Qualidade e segurança

- frameworks de teste e mutation testing adequados à stack
- SAST/code scanning, como CodeQL ou equivalente
- secret scanning
- dependency review, SBOM, vulnerabilidades e licenças
- DAST e testes de contrato quando aplicáveis
- policy as code para regras determinísticas

#### CI/CD e operação

- GitHub Actions, GitLab CI, Buildkite ou equivalente
- preview environments e infraestrutura como código
- feature flags e rollout gradual
- artifact registry e proveniência/attestation
- deploy progressivo, canary e rollback automatizado

#### Observabilidade e telemetria do Agent Team

- OpenTelemetry para correlacionar logs, métricas e traces
- backend de observabilidade como Grafana stack, Datadog, New Relic ou equivalente
- error tracking como Sentry ou equivalente
- product analytics como PostHog, Amplitude ou equivalente
- experimentação e avaliação de prompts/agentes
- dashboards de custo, qualidade, autonomia e fluxo

#### Portal e conhecimento

- `PRD.md` — por que e o que será entregue
- especificação de UX — jornada, fluxo, estados, conteúdo e acessibilidade
- `SPEC.md` — comportamento e contratos esperados
- `ADR.md` — decisões e consequências arquiteturais
- `AGENTS.md` — instruções operacionais para agentes
- `README.md` — uso, execução e visão geral do repositório
- histórico de PRs — mudanças, evidências e decisões locais
- Backstage Software Catalog/TechDocs ou equivalente para ownership, catálogo e descoberta em escala

### 12.7 Contrato de avaliação de uma ferramenta

Antes de adotar uma ferramenta, registrar:

- problema que resolve e owner
- etapa, input e output atendidos
- integração com fontes canônicas
- permissões, dados enviados e retenção
- custo financeiro e cognitivo
- API, automação e exportabilidade
- evidência produzida e capacidade de auditoria
- lock-in e plano de saída
- métrica de sucesso e data de revisão

### 12.8 Referências oficiais para as extensões propostas

- [GitHub Actions — workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows)
- [GitHub CodeQL — code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning)
- [GitHub — segurança da cadeia de suprimentos](https://docs.github.com/en/code-security/concepts/supply-chain-security/supply-chain-security)
- [OpenTelemetry — métricas e correlação entre sinais](https://opentelemetry.io/docs/specs/otel/metrics/)
- [Backstage — Software Catalog](https://backstage.io/docs/features/software-catalog/)
- [Backstage — TechDocs](https://backstage.io/docs/features/techdocs/)

Essas referências sustentam as capacidades sugeridas; não constituem decisão de adoção. A escolha deve passar pelo contrato de avaliação acima.

---

## 13. Governança e segurança

- permissões mínimas por agente e por etapa
- aprovação humana para ações irreversíveis ou externas
- segredos fora de prompts, logs e artefatos
- dados pessoais minimizados, protegidos e retidos por política
- rastreabilidade entre demanda, decisão, código e evidência
- registro de autoria, ferramentas, modelos e versões utilizadas
- critérios claros para interromper, escalar ou pedir decisão
- exceções documentadas com prazo e responsável
- segregação entre produção, validação e aprovação
- kill switch e revogação de credenciais
- auditoria periódica das permissões de agentes e integrações

### Contrato de escalonamento

Escalar quando houver:

- requisito contraditório ou sem owner
- confiança abaixo do limite definido
- duas ou mais tentativas de correção sem progresso
- mudança fora do escopo aprovado
- necessidade de nova permissão ou acesso externo
- falha não reproduzível ou evidência inconsistente
- decisão irreversível ou impacto não calculável
- divergência entre agentes sem critério objetivo de desempate

---

## 14. Classificação de risco e autonomia

### R0 — mínimo

- documentação, texto e formatação
- sem mudança de comportamento, dados, secrets ou contratos
- merge automático após gates; review humano por amostragem

### R1 — baixo

- refatoração interna ou mudança localizada
- comportamento coberto por testes existentes
- sem migração, segurança ou integração crítica
- aprovação curta e deploy automático com observação

### R2 — médio

- novo comportamento ou mudança de contrato interno/integração
- impacto reversível, mas relevante
- aprovação de produto ou Code Owner; canary e rollback

### R3 — alto

- dados persistidos, migrações, contratos públicos, autenticação, privacidade, pagamentos ou operação crítica
- aprovações humana de produto e técnica
- aprovação explícita antes de produção

### R4 — crítico

- impacto regulatório, financeiro, destrutivo ou de grande alcance
- plano de mudança e rollback revisados manualmente
- dupla aprovação, segregação de função e acompanhamento humano

### Regras

- um agente propõe o risco e outro tenta elevá-lo
- o maior risco justificado prevalece
- redução manual exige justificativa registrada
- mudança de escopo recalcula o risco
- paths sensíveis elevam risco automaticamente
- dúvida não resolvida impede R0/R1

### Autonomia progressiva

- **A0 — assistido:** pessoas aprovam todas as transições
- **A1 — execução autônoma:** agentes executam; pessoas aprovam decisões e merge
- **A2 — merge por risco:** R0/R1 podem integrar por política
- **A3 — entrega autônoma controlada:** baixo risco chega à produção com rollback comprovado
- **A4 — orientado a exceções:** fluxo saudável ocorre sem intervenção; pessoas tratam decisões e anomalias

Elevar autonomia somente com histórico suficiente, baixa taxa de falha, gates confiáveis, poucos falsos positivos, rollback testado e telemetria íntegra.

---

## 15. Evolução do modelo

### Fase 1 — piloto assistido

- selecionar um repositório e fluxo de baixo risco
- definir papéis, artefatos e gates mínimos
- manter aprovação humana em todas as transições
- medir tempo, retrabalho, custo e falhas

### Fase 2 — padronização

- criar templates reutilizáveis
- consolidar rules, skills, hooks e PR template
- definir critérios comuns de entrada e saída
- documentar exceções por tipo de repositório
- instituir as cerimônias do trio

### Fase 3 — automação

- automatizar roteamento entre agentes
- executar gates conforme risco e tipo de mudança
- atualizar status, artefatos e evidências automaticamente
- instrumentar telemetria ponta a ponta
- escalar para pessoas somente decisões e exceções

### Fase 4 — escala e melhoria contínua

- expandir para outros times e repositórios
- comparar desempenho entre fluxos sem criar ranking simplista
- evoluir skills a partir de falhas recorrentes
- revisar semanalmente regras, métricas e conhecimento
- elevar autonomia por evidência

---

## 16. Métricas iniciais do modelo

- lead time: backlog até homologação
- cycle time: implementação até merge
- taxa de aprovação na primeira revisão e por gate
- retrabalho após validação ou homologação
- defeitos e regressões após entrega
- cobertura dos critérios de aceite
- percentual de gates automatizados
- tempo humano gasto em exceções e aprovações
- custo por etapa, agente, modelo e entrega
- atualidade e uso da base de conhecimento
- outcome e adoção por entrega
- falhas, retries e escalonamentos por fase
- qualidade e completude do evidence pack
- falsos positivos por gate
- percentual de trabalho autônomo por classe de risco

As métricas devem orientar investigação. Nenhuma delas, isoladamente, representa produtividade ou qualidade do trio.

---

## 17. Decisões ainda em aberto

- ferramenta que orquestrará o Agent Team
- limites de autonomia de cada papel
- formato canônico e ciclo de vida dos artefatos
- critério de risco por tipo de mudança
- gates obrigatórios por linguagem e repositório
- responsável por aprovar exceções fora do trio
- estratégia de ambientes para integração e homologação
- como medir custo, qualidade e ganho de produtividade
- como versionar e distribuir rules e skills compartilhadas
- onde ficará a fonte canônica da telemetria do fluxo
- qual ferramenta será sistema de registro para backlog e decisões
- política de retenção das sessões e dados dos agentes
- quais cerimônias podem ser eliminadas após maturidade comprovada

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

## Resultado esperado

O trio mantém autoridade clara sobre produto, experiência e tecnologia, enquanto os agentes absorvem a maior parte da pesquisa operacional, produção, crítica, execução, validação e documentação. O sistema não depende de heroísmo nem de contexto oral: cada passagem possui contrato, cada decisão possui owner, cada entrega possui evidência e cada ciclo deixa o próximo mais seguro, rápido e autônomo.
