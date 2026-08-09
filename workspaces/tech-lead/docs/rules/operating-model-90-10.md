---
title: Agent Team — modelo operacional 90/10
status: proposed
updated_at: 2026-08-08
---

# Agent Team — modelo operacional 90/10

> Desdobramento prático de [Agent Team — sistema operacional do trio humano](../rules/operating-model.md) · [Fluxo visual completo](end-to-end-journey.md) · [Fluxos por fase](journey-by-phase.md) · [workflows multiagente](../workflows/README.md).

As subseções do fluxo operacional indicam o que deve ser feito; os [workflows](../workflows/README.md) descrevem como os agentes colaboram, fazem handoff, criticam e consolidam cada saída.

## Objetivo do modelo

- Automatizar aproximadamente 90% do trabalho operacional
- Reservar o tempo humano para decisões de valor, risco e responsabilidade
- Fazer agentes produzirem, criticarem, corrigirem e comprovarem o trabalho
- Substituir reviews extensos por checkpoints curtos e orientados a evidências
- Permitir mais autonomia conforme o fluxo demonstra segurança

## O que significa 90% automatizado

- 90% das atividades executadas sem intervenção manual
- Não significa 90% das decisões delegadas aos agentes
- Não elimina responsabilidade humana sobre produto e produção
- Não autoriza agentes a ignorar gates ou ampliar o próprio acesso
- Não deve ser medido apenas por quantidade de tarefas
- Deve reduzir tempo humano sem aumentar falhas, risco ou retrabalho

## Divisão de responsabilidade

- **Agentes fazem:** pesquisa, síntese, especificação, código, testes e evidências
- **Automações fazem:** validações determinísticas, bloqueios e rastreabilidade
- **Humanos fazem:** prioridade, escolhas irreversíveis, exceções e aceite
- **Sistema faz:** roteamento, registro, observação e escalonamento

---

## Princípio central: review de decisão

- O humano não revisa todo o processo
- O humano responde a uma pergunta objetiva em cada checkpoint
- O sistema apresenta decisão recomendada, alternativas, riscos e evidências
- O review possui tempo esperado e critérios explícitos
- Falta de resposta não equivale a aprovação
- Mudança material invalida a aprovação relacionada

## Evidence pack apresentado ao humano

- Decisão solicitada em uma frase
- Recomendação dos agentes
- Alternativas consideradas
- Principais riscos e trade-offs
- Mudanças desde o último checkpoint
- Evidências dos gates executados
- Pendências, exceções e nível de confiança
- Links para artefatos completos, código e execução

---

## Classificação de risco

### R0 — mínimo

- Documentação, texto e formatação
- Sem mudança de comportamento
- Sem dados, secrets ou contratos
- Merge automático após gates
- Review humano por amostragem

### R1 — baixo

- Refatoração interna ou mudança localizada
- Comportamento coberto por testes existentes
- Sem migração, segurança ou integração crítica
- Uma aprovação humana curta no PR
- Deploy automático com observação

### R2 — médio

- Novo comportamento de produto
- Mudança de contrato interno ou integração
- Impacto reversível, mas relevante
- Aprovação de produto ou Code Owner
- Canary e rollback automatizados

### R3 — alto

- Dados persistidos, migrações ou contratos públicos
- Autenticação, autorização, secrets ou privacidade
- Pagamentos, disponibilidade ou operação crítica
- Aprovações humana de produto e técnica
- Aprovação explícita antes de produção

### R4 — crítico

- Impacto regulatório, financeiro ou destrutivo
- Ação irreversível ou de grande alcance
- Plano de mudança e rollback revisados manualmente
- Dupla aprovação e segregação de função
- Acompanhamento humano durante a liberação

## Regras da classificação

- Um agente propõe o risco e outro agente tenta elevá-lo
- O maior risco justificado prevalece
- Redução manual de risco exige justificativa registrada
- Mudança de escopo recalcula o risco
- Paths sensíveis elevam o risco automaticamente
- Dúvida não resolvida impede classificação como R0 ou R1

---

## Fluxo operacional de ponta a ponta

### 0. Entrada e triagem

- **Agentes:** Intake Agent + Product Manager Agent
- **Automações:**
  - validar campos obrigatórios
  - identificar duplicidade e dependências
  - relacionar demanda, produto e repositório
  - classificar tipo e risco inicial
- **Saída:** Work Item com contexto, prioridade proposta e owner
- **Gate automático:** item completo, rastreável e sem duplicidade conhecida
- **Ação humana:** priorizar ou rejeitar o item
- **Tempo humano esperado:** 2–5 minutos

### 1. Discovery multiagente

- **Agent Team:**
  - Product Manager Agent
  - UX Specification Agent
  - Tech Lead Discovery Agent
- **Execução:**
  - agentes investigam em paralelo
  - cada agente registra hipóteses e evidências
  - Product Manager Agent consolida o `PB.md`
  - os demais agentes criticam a síntese
- **Automações:**
  - validar estrutura do `PB.md`
  - verificar links e fontes
  - detectar afirmações sem evidência
  - identificar perguntas e riscos sem owner
  - comparar descoberta com demandas similares
- **Gate automático:** problema, usuário, experiência e viabilidade cobertos

#### Checkpoint humano H1 — vale avançar?

- **Responsável:** Product Manager / sponsor
- **Pergunta:** este problema merece investimento agora?
- **Review:** problema, usuário, valor, restrições e riscos
- **Decisão:** avançar, ajustar, adiar ou encerrar
- **Tempo humano esperado:** 5–10 minutos

### 2. Planejamento de produto

- **Agent Team:**
  - Product Manager Agent
  - Adversarial Product Manager Agent
- **Execução:**
  - Product Manager propõe o `PRD.md`
  - agente adversarial procura ambiguidades e gaps
  - Product Manager responde e revisa o documento
  - gaps não resolvidos são escalados
- **Automações:**
  - validar template e campos obrigatórios
  - detectar termos vagos ou não mensuráveis
  - exigir critérios de aceite observáveis
  - verificar rastreabilidade `PB → PRD`
  - verificar escopo, fora de escopo e métricas
- **Gate automático:** PRD completo e crítica adversarial respondida

#### Checkpoint humano H2 — é isto que construiremos?

- **Responsável:** Product Manager / stakeholder
- **Pergunta:** escopo, experiência e critérios de sucesso estão corretos?
- **Review:** decisões e gaps; não o documento linha por linha
- **Decisão:** aprovar, reduzir, ampliar ou devolver
- **Tempo humano esperado:** 10–15 minutos

### 3. Especificação técnica

- **Agent Team:**
  - Specification Tech Lead Agent
  - Adversarial Tech Lead Agent
- **Execução:**
  - especificador propõe arquitetura e decomposição
  - agente adversarial avalia gaps, riscos e trade-offs
  - decisões são consolidadas em `ADR.md` e `SPEC.md`
  - trabalho é dividido em tarefas verificáveis
- **Automações:**
  - validar estrutura dos artefatos
  - verificar rastreabilidade `PRD → SPEC → TASKS`
  - detectar ciclos e violações arquiteturais conhecidas
  - identificar contratos e paths sensíveis
  - validar dependências e ordem das tarefas
  - gerar threat model quando aplicável
- **Gate automático:** especificação consistente e gaps críticos tratados

#### Checkpoint humano H3 — decisão técnica excepcional

- **Obrigatório:** R3, R4, nova ADR ou exceção arquitetural
- **Opcional:** R0, R1 e R2 sem decisão estrutural nova
- **Responsável:** Tech Lead / arquiteto / especialista do domínio
- **Pergunta:** aceitamos estes trade-offs e riscos residuais?
- **Review:** decisão, alternativas descartadas e impacto futuro
- **Tempo humano esperado:** 10–20 minutos

### 4. Implementação autônoma

- **Agentes:** Orchestrator Agent + Software Engineer Agents
- **Execução:**
  - selecionar próxima tarefa elegível
  - criar branch ou worktree isolado
  - implementar mudança mínima
  - criar ou atualizar testes
  - executar validações locais
  - corrigir falhas automaticamente
  - registrar commits pequenos e rastreáveis
  - atualizar documentação afetada
- **Pre-commit gate:**
  - formatação, lint e typecheck
  - unit tests afetados
  - testes de arquitetura rápidos
  - secrets e arquivos proibidos
  - consistência básica dos artefatos
- **Pre-push gate:**
  - build reproduzível
  - suíte ampliada de testes
  - cobertura mínima e mutation delta
  - análise estática e dependências
  - código morto e contratos quebrados
- **Correção automática:** até um limite de tentativas e tempo
- **Escalonamento:** falha repetida, conflito de requisito ou risco elevado
- **Ação humana:** nenhuma durante o fluxo saudável

### 5. Validação adversarial

- **Agent Team:**
  - QA / Validation Agent
  - Security Review Agent
  - Architecture Review Agent
  - Adversarial Code Reviewer Agent
- **Execução:**
  - validar cada critério de aceite
  - testar caminhos felizes, erros e casos-limite
  - comparar implementação com `PRD` e `SPEC`
  - procurar regressões, vulnerabilidades e violações
  - produzir evidências reproduzíveis
- **CI fast lane:**
  - lint, typecheck, unit tests e arquitetura
  - executada em todo push
- **CI deep lane:**
  - integração, TAAC, mutação e segurança
  - executada conforme risco, paths e impacto
- **Gate automático:** todos os checks obrigatórios aprovados
- **Ação humana:** somente para falso positivo, exceção ou gap de requisito

### 6. PR e decisão de merge

- **Agentes:** PR Agent + Reviewer Agents
- **Automações:**
  - gerar descrição e evidence pack
  - resumir comportamento alterado
  - destacar arquivos e trechos de maior risco
  - solicitar Code Owners conforme paths
  - exigir status checks da fonte autorizada
  - invalidar aprovação após mudança material
- **Review dos agentes:**
  - corretude e completude
  - segurança e privacidade
  - arquitetura e contratos
  - testes e manutenibilidade
  - documentação e observabilidade

#### Checkpoint humano H4 — podemos integrar?

- **R0:** merge automático; revisão humana por amostragem
- **R1:** uma revisão rápida do owner
- **R2:** uma aprovação do responsável afetado
- **R3:** aprovação técnica + aprovação do owner
- **R4:** dupla aprovação com segregação de função
- **Review humano:** evidence pack, hotspots e exceções
- **Tempo humano esperado:** 5–15 minutos
- **Gate de merge:** aprovações exigidas + CI verde + branch atualizada

### 7. Homologação automatizada

- **Agentes:** Release Agent + Product Validation Agent
- **Ambiente:** preview ou staging isolado
- **Automações:**
  - deploy do artefato imutável
  - seed de dados seguros
  - smoke, E2E e testes sintéticos
  - comparação visual quando aplicável
  - validação automática dos critérios de aceite
  - geração de demonstração e evidências
- **Ação humana:** revisar apenas experiência nova ou mudança R2+
- **Saída:** release candidate aprovado ou devolvido

### 8. Liberação em produção

- **Agentes:** Release Agent + Observability Agent
- **Estratégias:** feature flag, canary, blue/green ou rollout progressivo
- **Gates automáticos:**
  - artefato assinado e rastreável
  - ambiente e secrets autorizados
  - migração validada e compatível
  - backup e rollback verificados
  - SLOs e alertas configurados

#### Checkpoint humano H5 — podemos expor o risco?

- **R0/R1:** deploy automático
- **R2:** aprovação opcional conforme criticidade do produto
- **R3/R4:** aprovação explícita antes do ambiente de produção
- **Responsável:** Product Owner + responsável técnico quando necessário
- **Review:** impacto, plano de rollout, rollback e sinais de saúde
- **Tempo humano esperado:** 3–10 minutos

### 9. Observação e aprendizado

- **Agentes:** Observability Agent + Knowledge Agent
- **Automações:**
  - monitorar erros, latência, SLOs e métricas de produto
  - comparar baseline e comportamento após deploy
  - pausar rollout ou reverter automaticamente
  - atualizar changelog e documentação
  - registrar falhas e novos itens no backlog
- **Gate pós-deploy:** janela de observação sem regressão relevante
- **Ação humana:** decisão apenas quando rollback não for seguro ou automático

### 10. Melhoria contínua — Auto Dream

- **Agente:** Auto Dream Agent
- **Trigger:** agenda semanal + execução extraordinária após incidente relevante
- **Objetivo:** transformar o histórico operacional em memória e melhorias concretas
- **Escopo:** produto, agentes, prompts, processo, harness, skills, scripts, gates e fluxo

#### Entradas do ciclo

- Sessões e decisões dos agentes
- Evidence packs e feedbacks humanos
- Falhas, retries, bloqueios e escalonamentos
- Resultados de hooks, CI, homologação e deploy
- Incidentes, rollbacks e defeitos escapados
- Métricas de tempo, custo, qualidade e autonomia
- Demandas de melhoria geradas anteriormente

#### Pipeline automatizado

- Coletar sessões e eventos da semana
- Remover secrets e dados pessoais antes da análise
- Agrupar eventos por etapa, causa e tipo de impacto
- Identificar padrões recorrentes e ocorrências isoladas
- Comparar resultados com semanas anteriores
- Distinguir aprendizado reutilizável de problema operacional
- Procurar contradições com a memória existente
- Produzir evidências e nível de confiança para cada conclusão
- Submeter conclusões a um Critic Agent independente
- Consolidar somente itens confirmados ou explicitamente sinalizados como hipótese

#### Caminho A — aprendizado validado

- Identificar o que funcionou e em qual contexto
- Registrar evidências e condições de reutilização
- Verificar duplicidade, contradição e validade temporal
- Propor inclusão, atualização ou remoção no `MEMORY.md`
- Preservar a origem e a data do aprendizado
- Não transformar preferência isolada em regra global

#### Gate de memória

- Evidência vinculada à conclusão
- Escopo e contexto de aplicação explícitos
- Ausência de secrets ou dados pessoais
- Sem contradição não resolvida
- Conhecimento acionável e reutilizável
- Mudança sensível exige aprovação humana

#### Caminho B — falha ou oportunidade de melhoria

- Descrever o sintoma observado
- Identificar causa provável e evidências
- Registrar frequência, impacto e etapa afetada
- Propor ação corretiva e resultado esperado
- Classificar o tipo de melhoria:
  - processo
  - harness
  - skill ou prompt
  - script ou ferramenta
  - hook ou gate
  - arquitetura do workflow
  - documentação ou contexto
- Gerar demanda rastreável no backlog
- Relacionar sessões, execuções e incidentes de origem
- Detectar e vincular demandas duplicadas

#### Estrutura mínima da demanda

- Título orientado ao problema
- Sintoma e impacto
- Evidências e frequência
- Hipótese de causa-raiz
- Melhoria proposta
- Critério de aceite mensurável
- Prioridade e classe de risco sugeridas
- Owner recomendado
- Links para sessões e artefatos relacionados

#### Priorização sugerida

- **P0:** risco crítico, segurança ou perda de dados
- **P1:** falha recorrente que bloqueia o fluxo
- **P2:** retrabalho, custo ou baixa confiabilidade
- **P3:** otimização e melhoria incremental
- Frequência não substitui impacto na definição da prioridade
- O Auto Dream recomenda; o responsável humano controla a prioridade final

#### Checkpoint humano H6 — o sistema aprendeu corretamente?

- **Obrigatório:** mudanças sensíveis no `MEMORY.md`, P0/P1 e alteração de gates
- **Por amostragem:** aprendizados de baixo risco e demandas P2/P3
- **Responsável:** owner do Agent Team / Engineering Enablement
- **Pergunta:** evidências, aprendizado e ação proposta são confiáveis?
- **Decisão:** aprovar, ajustar, descartar ou solicitar mais evidências
- **Tempo humano esperado:** 10–20 minutos por ciclo semanal

#### Saídas do ciclo

- `MEMORY.md` atualizado com aprendizados validados
- Demandas de melhoria criadas ou enriquecidas no backlog
- Relatório semanal curto com padrões e tendências
- Métricas do sistema de trabalho atualizadas
- Hipóteses inconclusivas mantidas para observação futura

#### Gate de conclusão

- Todas as fontes processadas e rastreáveis
- Aprendizados separados de hipóteses
- Falhas relevantes convertidas em demandas
- Duplicidades e contradições tratadas
- Mudanças sensíveis revisadas
- Nenhum dado confidencial persistido indevidamente

#### Falhas do próprio Auto Dream

- Falha de coleta abre alerta, não produz conclusão parcial silenciosa
- Baixa confiança mantém item como hipótese
- Contradição bloqueia atualização automática da memória
- Demanda sem evidência permanece como rascunho
- O agente não pode aprovar alterações nos próprios gates
- Incidentes do Auto Dream entram no próximo ciclo de análise

---

## Resumo dos checkpoints humanos

| Checkpoint | Decisão humana | Quando | Tempo esperado |
|---|---|---|---:|
| H1 | Vale investir? | Após discovery | 5–10 min |
| H2 | É isto que construiremos? | Após PRD | 10–15 min |
| H3 | Aceitamos o trade-off? | Apenas risco ou decisão estrutural | 10–20 min |
| H4 | Podemos integrar? | Antes do merge, conforme risco | 5–15 min |
| H5 | Podemos expor o risco? | Produção R3/R4 | 3–10 min |
| H6 | O sistema aprendeu corretamente? | Ciclo semanal do Auto Dream | 10–20 min |

## Como reduzir ainda mais os reviews

- Combinar H2 e H3 para mudanças pequenas e bem conhecidas
- Eliminar H3 quando não houver ADR, exceção ou risco relevante
- Aplicar H4 por amostragem em R0 após histórico confiável
- Tornar H5 automático em R0/R1 com rollback comprovado
- Mostrar somente diferenças desde a última aprovação
- Direcionar o humano aos hotspots, não ao diff completo
- Usar Code Owners apenas para paths realmente sensíveis
- Criar políticas diferentes por risco e tipo de repositório
- Medir falsos positivos e remover gates sem valor

---

## Arquitetura de gates

### Gate local — segundos ou poucos minutos

- Feedback imediato ao agente
- Checks determinísticos e de baixo custo
- Deve oferecer instrução clara de correção
- Falha bloqueia commit ou push

### Gate de CI — minutos

- Executado em ambiente limpo
- Confirma build, testes, segurança e arquitetura
- Seleciona checks conforme risco e paths alterados
- Falha bloqueia merge

### Gate de merge — decisão consolidada

- Confirma aprovações e status checks
- Confirma proveniência da automação
- Impede bypass silencioso e force push
- Invalida aprovação quando o diff muda materialmente

### Gate de ambiente — exposição controlada

- Libera secrets somente após autorização
- Restringe branches e artefatos permitidos
- Exige aprovação quando o risco determinar
- Integra sinais de observabilidade e change management

### Gate pós-deploy — comportamento real

- Compara métricas com o baseline
- Interrompe rollout diante de regressão
- Reverte automaticamente quando seguro
- Abre incidente quando ação humana for necessária

## Regras para gates baseados em IA

- IA pode recomendar, explicar e priorizar achados
- Bloqueio automático exige regra reproduzível e evidência verificável
- Achado probabilístico deve passar por confirmação independente
- O mesmo agente não deve produzir e aprovar a própria mudança
- Agents não podem alterar gates dentro do mesmo fluxo avaliado
- Mudança em rules, hooks ou CI eleva risco automaticamente
- Bypass exige pessoa autorizada, motivo e prazo de correção

---

## Contrato de escalonamento

- Requisito contraditório ou sem owner
- Confiança abaixo do limite definido
- Duas ou mais tentativas de correção sem progresso
- Mudança fora do escopo aprovado
- Necessidade de nova permissão ou acesso externo
- Falha não reproduzível ou evidência inconsistente
- Decisão irreversível ou impacto não calculável
- Divergência entre agentes sem critério objetivo de desempate

## Autonomia progressiva

### Nível A0 — assistido

- Humanos aprovam todas as transições
- Indicado para início do piloto

### Nível A1 — execução autônoma

- Agentes executam implementação e validação
- Humanos mantêm H1, H2, H4 e H5

### Nível A2 — merge por risco

- R0 pode fazer auto-merge
- R1 recebe review humano curto
- R2+ mantém owners específicos

### Nível A3 — entrega autônoma controlada

- R0/R1 fazem deploy automático
- Rollback e observabilidade são obrigatórios
- Humanos atuam em exceções e riscos altos

### Nível A4 — operação orientada a exceções

- Fluxo saudável ocorre sem intervenção
- Humanos recebem apenas decisões e incidentes relevantes
- Auditorias por amostragem verificam a qualidade do sistema

## Critério para elevar autonomia

- Volume mínimo de entregas observado
- Baixa taxa de defeitos escapados
- Rollback testado e confiável
- Gates com poucos falsos positivos
- Risco classificado corretamente
- Evidências completas e auditáveis
- Tempo humano realmente reduzido

---

## Métricas do modelo 90/10

- Percentual de etapas concluídas sem intervenção
- Minutos humanos por entrega
- Tempo aguardando aprovação humana
- Taxa de decisões devolvidas por falta de contexto
- Aprovação na primeira passagem de cada gate
- Retrabalho após H2, H3 e H4
- Defeitos escapados para produção
- Rollbacks automáticos e manuais
- Falsos positivos por gate
- Custo de agentes por entrega
- Lead time e cycle time
- Percentual de mudanças por classe de risco
- Cobertura de rastreabilidade entre artefatos

## Meta inicial sugerida

- 80–90% das atividades executadas por agentes
- Até 30–45 minutos humanos por entrega R1/R2
- Nenhuma aprovação humana baseada apenas em confiança no agente
- 100% dos merges protegidos por gates verificáveis
- 100% das mudanças R3/R4 com owner e rollback definidos
- Evoluir para auto-merge somente após evidência do piloto

---

## Implementação do modelo

### Etapa 1 — contrato mínimo

- Definir classes de risco
- Definir responsáveis humanos
- Criar templates dos artefatos
- Criar formato do evidence pack
- Definir condições de escalonamento

### Etapa 2 — harness mínimo

- Configurar `AGENTS.md`, rules e skills
- Implementar pre-commit e pre-push
- Criar CI fast lane e deep lane
- Proteger branch e status checks
- Configurar `CODEOWNERS` para paths sensíveis

### Etapa 3 — piloto controlado

- Escolher um fluxo R1 real
- Operar inicialmente em autonomia A0/A1
- Medir tempo humano e falhas
- Ajustar gates e templates
- Validar rollback e rastreabilidade

### Etapa 4 — automação do roteamento

- Classificar risco automaticamente
- Acionar Agent Teams por etapa
- Produzir evidence packs automaticamente
- Solicitar apenas os reviewers necessários
- Escalar exceções com contexto completo

### Etapa 5 — autonomia progressiva

- Liberar auto-merge para R0
- Liberar deploy automático para R0/R1
- Ampliar por evidência, não por expectativa
- Manter auditoria humana por amostragem

---

## Referências operacionais

- [GitHub Rulesets e regras disponíveis](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [NIST Secure Software Development Framework](https://www.nist.gov/publications/secure-software-development-framework-ssdf-version-11-recommendations-mitigating-risk)

## Próximo detalhamento recomendado

- Definir o schema do Work Item
- Criar o template do evidence pack
- Desenhar a matriz `risco × gates × aprovações`
- Especificar os prompts e contratos de cada agente
- Definir os eventos que movimentam o workflow
- Criar o primeiro repo harness de referência
- Simular uma entrega R1 de ponta a ponta
