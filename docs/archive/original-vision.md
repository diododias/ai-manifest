---
title: Agent Team — visão macro original
status: archived
updated_at: 2026-08-08
---

# Agent Team — visão macro

> Nova proposta canônica: [Agent Team — sistema operacional do trio humano](../operating-model.md). Este documento foi preservado como referência da versão original.
>
> Próximo nível: [Agent Team — modelo operacional 90/10](../operations/operating-model-90-10.md) · [Fluxo visual completo](../operations/end-to-end-journey.md) · [Fluxos por fase](../operations/journey-by-phase.md).

## Objetivo

- Transformar uma necessidade de negócio em software validado
- Combinar agentes especializados, pessoas e automações
- Manter decisões, código e documentação sincronizados
- Produzir evidências em todas as etapas do ciclo
- Escalar a entrega sem perder segurança e governança

## Princípios do modelo

- Pessoas definem prioridade, restrições e aprovação final
- Agentes executam trabalho especializado e produzem evidências
- Cada etapa possui entrada, saída e critério de passagem
- O repositório concentra regras e contexto do produto
- O harness transforma padrões em verificações executáveis
- Mudanças pequenas e rastreáveis reduzem risco e retrabalho

## Modelo de atuação dos Agent Teams

- Algumas etapas são executadas por times de agentes especializados
- Cada agente analisa o problema a partir de uma responsabilidade clara
- Um agente primário conduz e consolida o artefato da etapa
- Agentes críticos procuram ambiguidades, gaps, riscos e suposições frágeis
- As contribuições são registradas antes da consolidação final
- Divergências relevantes são resolvidas pelo responsável humano
- A etapa termina com um único artefato coerente, não com análises isoladas

---

## Ciclo de desenvolvimento

### 1. Backlog

- **Objetivo:** registrar e priorizar necessidades
- **Responsável:** Product Manager, em ferramenta externa
- **Entrada:** problema, oportunidade ou solicitação
- **Saída:** item priorizado, contexto inicial e responsável
- **Gate:** problema e prioridade minimamente claros

### 2. Discovery

- **Agent Team:** Product Discovery Team
- **Objetivo:** compreender problema, usuário e contexto
- **Composição:**
  - **Product Manager Agent:**
    - conduz entendimento do problema e do negócio
    - identifica objetivos, stakeholders e resultados esperados
    - organiza hipóteses, restrições e perguntas em aberto
  - **UX Specification Agent:**
    - representa necessidades e contexto dos usuários
    - propõe jornadas, fluxos e princípios de experiência
    - identifica fricções, estados, acessibilidade e necessidades de design
  - **Tech Lead Discovery Agent:**
    - avalia viabilidade técnica inicial
    - identifica dependências, restrições, riscos e integrações
    - oferece direcionamento técnico sem antecipar a solução completa
- **Dinâmica:** investigação paralela + síntese conduzida pelo Product Manager Agent
- **Saída:** `PB.md` — Problem Brief
- **Conteúdo mínimo:** problema, usuários, jornada, valor, restrições e riscos
- **Gate:** problema validado, experiência desejada compreendida e viabilidade inicial avaliada

### 3. Planejamento de produto

- **Agent Team:** Product Planning Team
- **Objetivo:** transformar o problema em proposta de produto
- **Composição:**
  - **Product Manager Agent:**
    - propõe visão, escopo e requisitos do produto
    - define jornadas, prioridades e critérios de sucesso
    - consolida a versão final do planejamento
  - **Adversarial Product Manager Agent:**
    - desafia clareza, coerência e completude da proposta
    - procura ambiguidades, gaps e requisitos conflitantes
    - questiona premissas, casos-limite e itens fora de escopo
- **Dinâmica:** proposta → crítica adversarial → revisão → consolidação
- **Saída:** `PRD.md`
- **Conteúdo mínimo:** objetivos, usuários, jornadas, escopo, requisitos e métricas
- **Gate:** gaps críticos tratados, ambiguidades reduzidas e critérios de sucesso aprovados

### 4. Especificação técnica

- **Agent Team:** Technical Specification Team
- **Objetivo:** definir como a solução será construída
- **Composição:**
  - **Specification Tech Lead Agent:**
    - propõe arquitetura, contratos e plano de implementação
    - decompõe a solução em tarefas pequenas e verificáveis
    - consolida os artefatos técnicos da etapa
  - **Adversarial Tech Lead Agent:**
    - procura gaps técnicos, riscos e acoplamentos ocultos
    - avalia trade-offs, alternativas e impactos arquiteturais
    - critica complexidade, testabilidade e capacidade de evolução
- **Dinâmica:** especificação → revisão crítica → resposta aos gaps → decisão
- **Saídas:**
  - `PLAN.md` — estratégia de implementação
  - `ADR.md` — decisões arquiteturais relevantes
  - `SPEC.md` — comportamento e contratos técnicos
  - `TASKS.md` — execução em unidades pequenas
  - `CHECKLIST.md` — critérios verificáveis de aceite
- **Conteúdo mínimo:** arquitetura, alternativas, trade-offs, riscos e validação
- **Gate:** gaps críticos tratados, trade-offs registrados e tarefas executáveis

### 5. Implementação

- **Agente:** Software Engineer Agent
- **Suporte:** repo harness, skills e ferramentas de código
- **Objetivo:** implementar uma tarefa por vez
- **Atividades:** código, testes, documentação e commits
- **Saída:** mudança funcional pronta para validação
- **Gate:** verificações locais rápidas aprovadas

### 6. Validação

- **Agente:** Validation / QA Agent
- **Suporte:** repo harness e ambientes reproduzíveis
- **Objetivo:** provar aderência à especificação
- **Atividades:** testes, segurança, arquitetura e regressão
- **Saída:** evidências vinculadas aos critérios de aceite
- **Gate:** checklist completo e ausência de bloqueadores

### 7. Code review

- **Agentes:** Reviewer Agent + responsável humano
- **Objetivo:** avaliar qualidade, risco e manutenibilidade
- **Atividades:** revisão de código, testes e impacto arquitetural
- **Saída:** aprovação ou solicitações de ajuste
- **Gate:** revisão aprovada e CI verde

### 8. Homologação e entrega

- **Responsável:** Product Manager / stakeholder
- **Objetivo:** confirmar valor e comportamento no cenário real
- **Atividades:** demonstração, aceite e decisão de liberação
- **Saídas:** evidências, aprovação e registro de pendências
- **Gate:** aceite explícito ou plano de correção

### 9. Atualização da base de conhecimento

- **Agente:** Knowledge Agent
- **Cadência:** atualização contínua + revisão semanal automatizada
- **Objetivo:** manter documentação alinhada ao produto real
- **Atividades:** consolidar decisões, aprendizados e mudanças
- **Saída:** conhecimento reutilizável para os próximos ciclos
- **Gate:** fontes canônicas atualizadas e sem contradições

### 10. Melhoria contínua — Auto Dream

- **Agente:** Auto Dream Agent
- **Cadência:** execução semanal automatizada
- **Objetivo:** aprender com as sessões e melhorar o sistema de trabalho
- **Entradas:**
  - sessões e interações dos agentes
  - falhas, retries, bloqueios e escalonamentos
  - resultados dos gates, CI e homologação
  - feedback humano e métricas do fluxo
- **Atividades:**
  - identificar padrões, aprendizados e práticas eficazes
  - encontrar erros recorrentes, atritos e desperdícios
  - avaliar causas e impacto dos problemas
  - separar conhecimento reutilizável de oportunidades de melhoria
- **Saídas de aprendizado:**
  - atualizar `MEMORY.md` com aprendizados validados
  - registrar contexto, evidência e condição de reutilização
  - evitar duplicidade, contradição e conhecimento obsoleto
- **Saídas de melhoria:**
  - gerar demandas priorizáveis no backlog
  - classificar cada demanda por causa, impacto e urgência
  - sugerir melhoria de processo, harness, skill, script, gate ou fluxo
  - relacionar a demanda às sessões e evidências de origem
- **Supervisão humana:** revisar apenas mudanças sensíveis de memória e prioridades
- **Gate:** aprendizados consolidados e falhas relevantes convertidas em ações rastreáveis
- **Resultado esperado:** cada ciclo torna o próximo mais seguro, rápido e autônomo

---

## Fluxo de responsabilidade

- **PM / stakeholder:** prioridade, valor, escopo e aceite
- **Agent Team:** pesquisa, planejamento, execução e evidências
- **Tech Lead:** decisões técnicas e exceções arquiteturais
- **Repo harness:** políticas automatizadas e bloqueio de desvios
- **CI/CD:** validação independente e entrega reproduzível
- **Base de conhecimento:** memória compartilhada do produto

---

## Repo harness

### Papel

- Tornar o repositório compreensível para pessoas e agentes
- Converter padrões de engenharia em regras executáveis
- Oferecer caminhos seguros e repetíveis para mudanças
- Reduzir dependência de contexto informal ou individual

### Estrutura do repositório

#### Skills

- `speckit-*` — especificação, plano, tarefas e implementação
- `my-tcl` — aplicação do ciclo de desenvolvimento
- `pr-template` — contexto, riscos, evidências e checklist do PR
- Skills de domínio — procedimentos específicos do produto

#### Rules

- Arquitetura e fronteiras entre módulos
- Convenções e nomes de objetos
- Padrões aceitos e padrões proibidos
- Injeção de dependência e composição
- Gitflow e estratégia de branches
- Critérios de validação e homologação
- Estratégia de testes:
  - unitários
  - arquitetura
  - integração / TAAC
  - mutação

#### Hooks e gates locais

- **Pre-commit — feedback rápido:**
  - lint e formatação
  - typecheck
  - testes unitários afetados
  - testes de arquitetura
  - consistência entre código, PRD e SPEC
- **Pre-push — validação ampliada:**
  - cobertura mínima definida pelo projeto
  - código morto e débito técnico bloqueante
  - vazamento de secrets
  - integração / TAAC em container
  - impacto em contratos e compatibilidade
- **CI — validação independente:**
  - repetir gates críticos em ambiente limpo
  - gerar evidências auditáveis
  - impedir merge quando houver bloqueadores

#### Tools

- LSP, lint e formatação
- Typecheck e análise estática
- Navegação e compreensão da codebase:
  - Serena
  - Dora
- Redução e gestão de contexto:
  - RTK
- Testes, containers e observabilidade

#### Documentação e contexto

- `PRD.md` — por que e o que será entregue
- `SPEC.md` — comportamento e contratos esperados
- `ADR.md` — decisões e consequências arquiteturais
- `AGENTS.md` — instruções operacionais para agentes
- `README.md` — uso, execução e visão geral do repositório
- Histórico de PRs — mudanças, evidências e decisões locais

---

## Governança e segurança

- Permissões mínimas por agente e por etapa
- Aprovação humana para ações irreversíveis ou externas
- Segredos fora de prompts, logs e artefatos
- Rastreabilidade entre demanda, decisão, código e evidência
- Registro de autoria, ferramentas e versões utilizadas
- Critérios claros para interromper, escalar ou pedir decisão
- Exceções documentadas com prazo e responsável

## Evidências mínimas por entrega

- Critérios de aceite cobertos
- Testes executados e respectivos resultados
- Impacto arquitetural avaliado
- Riscos e limitações conhecidos
- Alterações de documentação registradas
- Aprovações humana e automatizada identificadas
- Link entre backlog, artefatos, commits e PR

---

## Evolução para um modelo prático

### Fase 1 — Piloto assistido

- Selecionar um repositório e um fluxo de baixo risco
- Definir papéis, artefatos e gates mínimos
- Manter aprovação humana em todas as transições
- Medir tempo, retrabalho e falhas do processo

### Fase 2 — Padronização

- Criar templates reutilizáveis para os artefatos
- Consolidar rules, skills, hooks e PR template
- Definir critérios comuns de entrada e saída
- Documentar exceções por tipo de repositório

### Fase 3 — Automação

- Automatizar roteamento entre agentes
- Executar gates conforme risco e tipo de mudança
- Atualizar status e evidências automaticamente
- Escalar para humanos somente decisões e exceções

### Fase 4 — Escala e melhoria contínua

- Expandir para outros times e repositórios
- Comparar desempenho entre fluxos
- Evoluir skills a partir de falhas recorrentes
- Revisar semanalmente regras, métricas e conhecimento

## Métricas iniciais

- Lead time: backlog até homologação
- Cycle time: implementação até merge
- Taxa de aprovação na primeira revisão
- Retrabalho após validação ou homologação
- Defeitos e regressões após entrega
- Cobertura dos critérios de aceite
- Percentual de gates automatizados
- Tempo humano gasto em exceções e aprovações
- Custo de execução por etapa e por entrega
- Atualidade e uso da base de conhecimento

## Decisões em aberto

- Ferramenta que orquestrará o Agent Team
- Limites de autonomia de cada papel
- Formato canônico e ciclo de vida dos artefatos
- Critério de risco para cada tipo de mudança
- Gates obrigatórios por linguagem e repositório
- Responsável por aprovar exceções
- Estratégia de ambientes para integração e homologação
- Como medir custo, qualidade e ganho de produtividade
- Como versionar e distribuir rules e skills compartilhadas

## Próximos passos

- Escolher o repositório piloto
- Mapear o fluxo atual e seus principais gargalos
- Definir o conjunto mínimo de agentes
- Escolher um caso real de baixo risco
- Criar templates mínimos de `PB`, `PRD`, `SPEC` e evidências
- Implementar os gates essenciais no repo harness
- Executar um ciclo completo de ponta a ponta
- Registrar resultados, gaps e ajustes para a próxima versão
