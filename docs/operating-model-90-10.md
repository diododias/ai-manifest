---
title: Agent Team — modelo operacional 90/10
status: proposed
updated_at: 2026-08-09
---

# Agent Team — modelo operacional 90/10

> Como chegar a ~90% do trabalho operacional executado sem intervenção humana, mantendo 100% das decisões de risco sob responsabilidade de uma pessoa.

## Em 2 minutos

O modelo 90/10 é o desdobramento operacional do [sistema operacional do trio humano](operating-model.md). Ele responde a uma pergunta específica: **onde exatamente o humano entra, por quanto tempo, e o que ele precisa ver para decidir?**

A resposta é substituir review de processo por review de decisão. Ninguém acompanha o diff inteiro nem lê o PRD linha por linha. Em cada checkpoint, o sistema entrega uma pergunta objetiva, a recomendação dos agentes, as alternativas descartadas, os riscos e as evidências dos gates — e a pessoa responde. São seis checkpoints em todo o ciclo, somando algo entre 30 e 45 minutos de tempo humano por entrega R1/R2.

| Checkpoint | Decisão | Quando | Tempo esperado |
|---|---|---|---:|
| **H1** | Vale investir? | após discovery | 5–10 min |
| **H2** | É isto que construiremos? | após PRD | 10–15 min |
| **H3** | Aceitamos o trade-off? | apenas ADR, exceção ou R3/R4 | 10–20 min |
| **H4** | Podemos integrar? | antes do merge, conforme risco | 5–15 min |
| **H5** | Podemos expor o risco? | produção R3/R4 | 3–10 min |
| **H6** | O sistema aprendeu corretamente? | ciclo semanal do Auto Dream | 10–20 min |

O que sustenta esses números não é confiança no agente: é a **arquitetura de gates**. Cinco camadas de verificação — local, CI, merge, ambiente e pós-deploy — filtram tudo que é determinístico antes de qualquer pessoa ser chamada. A autonomia sobe de A0 a A4 apenas quando essas camadas demonstram baixo índice de falsos positivos e rollback confiável.

---

## Mapa do documento

| Seção | Responde | Leia se você… |
|---|---|---|
| [1. O que 90% significa](#1-o-que-90-significa) | O que o número mede e o que não mede | quer evitar a leitura errada da meta |
| [2. Review de decisão](#2-review-de-decisão) | Como o humano decide sem ler tudo | vai desenhar o evidence pack |
| [3. Classificação de risco](#3-classificação-de-risco) | R0 a R4 e o que cada classe exige | vai definir política de aprovação |
| [4. Fluxo operacional](#4-fluxo-operacional-de-ponta-a-ponta) | O que acontece em cada uma das 11 etapas | vai operar o fluxo |
| [5. Reduzindo reviews](#5-como-reduzir-ainda-mais-os-reviews) | Onde cortar intervenção com segurança | já rodou alguns ciclos |
| [6. Arquitetura de gates](#6-arquitetura-de-gates) | As cinco camadas de verificação | vai configurar o harness |
| [7. Autonomia progressiva](#7-autonomia-progressiva) | A0 a A4 e critérios de subida | vai propor elevar autonomia |
| [8. Métricas e metas](#8-métricas-e-metas) | Como saber se está funcionando | vai instrumentar o fluxo |
| [9. Implementação](#9-implementação-do-modelo) | Em que ordem construir | está começando do zero |

**Vizinhos:** [sistema operacional do trio humano](operating-model.md) · [fluxo visual completo](end-to-end-journey.md) · [fluxos por fase](journey-by-phase.md) · [workflows multiagente](workflows/README.md).

As subseções do fluxo operacional indicam **o que** deve ser feito; os [workflows](workflows/README.md) descrevem **como** os agentes colaboram, fazem handoff, criticam e consolidam cada saída.

---

## 1. O que 90% significa

O objetivo é automatizar aproximadamente 90% do trabalho operacional, reservando o tempo humano para decisões de valor, risco e responsabilidade. Agentes produzem, criticam, corrigem e comprovam o próprio trabalho; reviews extensos dão lugar a checkpoints curtos orientados a evidência; e a autonomia cresce à medida que o fluxo demonstra segurança.

A leitura correta do número importa, porque a leitura errada destrói o modelo:

| 90% **significa** | 90% **não significa** |
|---|---|
| 90% das atividades executadas sem intervenção manual | 90% das decisões delegadas aos agentes |
| Redução de tempo humano sem aumento de falhas, risco ou retrabalho | Eliminação da responsabilidade humana sobre produto e produção |
| Gates aplicados a todo trabalho autônomo | Autorização para agentes ignorarem gates ou ampliarem o próprio acesso |
| Medição por tempo e por resultado | Medição apenas por quantidade de tarefas |

A divisão de responsabilidade que produz esse número: **agentes** fazem pesquisa, síntese, especificação, código, testes e evidências; **automações** fazem validações determinísticas, bloqueios e rastreabilidade; **humanos** definem prioridade, escolhas irreversíveis, exceções e aceite; e o **sistema** cuida de roteamento, registro, observação e escalonamento.

---

## 2. Review de decisão

O princípio central é que o humano não revisa o processo — ele responde a uma pergunta objetiva. Para cada checkpoint, o sistema apresenta decisão recomendada, alternativas, riscos e evidências, com tempo esperado e critérios explícitos. Duas travas protegem o mecanismo: falta de resposta não equivale a aprovação, e mudança material invalida a aprovação relacionada.

O evidence pack é o que torna isso viável. Ele contém:

| Item | Conteúdo |
|---|---|
| Decisão solicitada | uma frase |
| Recomendação | posição dos agentes |
| Alternativas | opções consideradas e descartadas |
| Riscos e trade-offs | o que se aceita ao aprovar |
| Delta | mudanças desde o último checkpoint |
| Evidências | resultado dos gates executados |
| Pendências | exceções e nível de confiança |
| Links | artefatos completos, código e execução |

---

## 3. Classificação de risco

A classe de risco é o que determina quantas aprovações a mudança exige e quanto de automação ela pode usar.

| Classe | Caracteriza | Aprovação e entrega |
|---|---|---|
| **R0 — mínimo** | documentação, texto e formatação; sem mudança de comportamento, dados, secrets ou contratos | merge automático após gates; review humano por amostragem |
| **R1 — baixo** | refatoração interna ou mudança localizada, coberta por testes existentes; sem migração, segurança ou integração crítica | uma aprovação humana curta no PR; deploy automático com observação |
| **R2 — médio** | novo comportamento de produto ou mudança de contrato interno/integração; impacto reversível mas relevante | aprovação de produto ou Code Owner; canary e rollback automatizados |
| **R3 — alto** | dados persistidos, migrações, contratos públicos, autenticação, autorização, secrets, privacidade, pagamentos, disponibilidade ou operação crítica | aprovações humana de produto e técnica; aprovação explícita antes de produção |
| **R4 — crítico** | impacto regulatório, financeiro ou destrutivo; ação irreversível ou de grande alcance | plano de mudança e rollback revisados manualmente; dupla aprovação, segregação de função e acompanhamento humano durante a liberação |

**Regras da classificação.** Um agente propõe o risco e outro tenta elevá-lo; o maior risco justificado prevalece. Redução manual exige justificativa registrada, mudança de escopo recalcula o risco, paths sensíveis elevam risco automaticamente, e dúvida não resolvida impede classificação como R0 ou R1.

---

## 4. Fluxo operacional de ponta a ponta

### 4.0 Entrada e triagem

Intake Agent e Product Manager Agent recebem a solicitação. As automações validam campos obrigatórios, identificam duplicidade e dependências, relacionam demanda, produto e repositório, e classificam tipo e risco inicial. A saída é um Work Item com contexto, prioridade proposta e owner.

**Gate automático:** item completo, rastreável e sem duplicidade conhecida. **Ação humana:** priorizar ou rejeitar — 2 a 5 minutos.

### 4.1 Discovery multiagente

O Agent Team reúne Product Manager Agent, UX Specification Agent e Tech Lead Discovery Agent. Os três investigam em paralelo e registram hipóteses e evidências; o Product Manager Agent consolida o `PB.md` e os demais criticam a síntese.

As automações validam a estrutura do `PB.md`, verificam links e fontes, detectam afirmações sem evidência, identificam perguntas e riscos sem owner, e comparam a descoberta com demandas similares.

**Gate automático:** problema, usuário, experiência e viabilidade cobertos.

> **H1 — vale avançar?** Responsável: PM ou sponsor. Revisa problema, usuário, valor, restrições e riscos. Decide avançar, ajustar, adiar ou encerrar. **5–10 minutos.**

### 4.2 Planejamento de produto

Product Manager Agent propõe o `PRD.md`; o Adversarial Product Manager Agent procura ambiguidades e gaps; o primeiro responde e revisa o documento. Gaps não resolvidos são escalados.

As automações validam template e campos obrigatórios, detectam termos vagos ou não mensuráveis, exigem critérios de aceite observáveis, e verificam rastreabilidade `PB → PRD`, escopo, fora de escopo e métricas.

**Gate automático:** PRD completo e crítica adversarial respondida.

> **H2 — é isto que construiremos?** Responsável: PM ou stakeholder. Revisa **decisões e gaps**, não o documento linha por linha. Decide aprovar, reduzir, ampliar ou devolver. **10–15 minutos.**

### 4.3 Especificação técnica

O Specification Tech Lead Agent propõe arquitetura e decomposição; o Adversarial Tech Lead Agent avalia gaps, riscos e trade-offs. As decisões são consolidadas em `ADR.md` e `SPEC.md`, e o trabalho é dividido em tarefas verificáveis.

As automações validam a estrutura dos artefatos, verificam rastreabilidade `PRD → SPEC → TASKS`, detectam ciclos e violações arquiteturais conhecidas, identificam contratos e paths sensíveis, validam dependências e ordem das tarefas, e geram threat model quando aplicável.

**Gate automático:** especificação consistente e gaps críticos tratados.

> **H3 — decisão técnica excepcional.** Obrigatório em R3, R4, nova ADR ou exceção arquitetural; dispensável em R0–R2 sem decisão estrutural nova. Responsável: Tech Lead, arquiteto ou especialista do domínio. Revisa decisão, alternativas descartadas e impacto futuro. **10–20 minutos.**

### 4.4 Implementação autônoma

Orchestrator Agent e Software Engineer Agents selecionam a próxima tarefa elegível, criam branch ou worktree isolado, implementam a mudança mínima, criam ou atualizam testes, executam validações locais, corrigem falhas automaticamente, registram commits pequenos e rastreáveis, e atualizam a documentação afetada.

| Gate | Verifica |
|---|---|
| **Pre-commit** | formatação, lint e typecheck; unit tests afetados; testes de arquitetura rápidos; secrets e arquivos proibidos; consistência básica dos artefatos |
| **Pre-push** | build reproduzível; suíte ampliada de testes; cobertura mínima e mutation delta; análise estática e dependências; código morto e contratos quebrados |

A correção automática opera até um limite de tentativas e tempo. Falha repetida, conflito de requisito ou risco elevado disparam escalonamento. **Nenhuma ação humana durante o fluxo saudável.**

### 4.5 Validação adversarial

QA/Validation, Security Review, Architecture Review e Adversarial Code Reviewer validam cada critério de aceite, testam caminhos felizes, erros e casos-limite, comparam a implementação com `PRD` e `SPEC`, procuram regressões, vulnerabilidades e violações, e produzem evidências reproduzíveis.

A CI opera em duas faixas: a **fast lane** (lint, typecheck, unit tests e arquitetura) roda em todo push; a **deep lane** (integração, TAAC, mutação e segurança) roda conforme risco, paths e impacto.

**Gate automático:** todos os checks obrigatórios aprovados. **Ação humana:** somente para falso positivo, exceção ou gap de requisito.

### 4.6 PR e decisão de merge

PR Agent e Reviewer Agents geram descrição e evidence pack, resumem o comportamento alterado, destacam arquivos e trechos de maior risco, solicitam Code Owners conforme paths, exigem status checks da fonte autorizada, e invalidam aprovação após mudança material. A revisão dos agentes cobre corretude e completude, segurança e privacidade, arquitetura e contratos, testes e manutenibilidade, documentação e observabilidade.

> **H4 — podemos integrar?** O peso da aprovação varia por classe de risco:

| Risco | Aprovação exigida |
|---|---|
| R0 | merge automático; revisão humana por amostragem |
| R1 | uma revisão rápida do owner |
| R2 | uma aprovação do responsável afetado |
| R3 | aprovação técnica + aprovação do owner |
| R4 | dupla aprovação com segregação de função |

O humano revisa evidence pack, hotspots e exceções — **5 a 15 minutos**. O gate de merge exige aprovações, CI verde e branch atualizada.

### 4.7 Homologação automatizada

Release Agent e Product Validation Agent operam em preview ou staging isolado. As automações fazem deploy do artefato imutável, seed de dados seguros, smoke, E2E e testes sintéticos, comparação visual quando aplicável, validação automática dos critérios de aceite, e geração de demonstração e evidências.

A ação humana se limita a revisar experiência nova ou mudança R2+. A saída é um release candidate aprovado ou devolvido.

### 4.8 Liberação em produção

Release Agent e Observability Agent aplicam feature flag, canary, blue/green ou rollout progressivo. Os gates automáticos exigem artefato assinado e rastreável, ambiente e secrets autorizados, migração validada e compatível, backup e rollback verificados, e SLOs e alertas configurados.

> **H5 — podemos expor o risco?** R0/R1 fazem deploy automático; R2 tem aprovação opcional conforme criticidade do produto; R3/R4 exigem aprovação explícita antes de produção. Responsável: Product Owner mais responsável técnico quando necessário. Revisa impacto, plano de rollout, rollback e sinais de saúde. **3–10 minutos.**

### 4.9 Observação e aprendizado

Observability Agent e Knowledge Agent monitoram erros, latência, SLOs e métricas de produto, comparam baseline e comportamento após deploy, pausam rollout ou revertem automaticamente, atualizam changelog e documentação, e registram falhas e novos itens no backlog.

**Gate pós-deploy:** janela de observação sem regressão relevante. **Ação humana:** apenas quando o rollback não for seguro ou automático.

### 4.10 Melhoria contínua — Auto Dream

O Auto Dream Agent roda em agenda semanal, com execução extraordinária após incidente relevante. O objetivo é transformar o histórico operacional em memória e melhorias concretas, com escopo sobre produto, agentes, prompts, processo, harness, skills, scripts, gates e fluxo.

**Entradas:** sessões e decisões dos agentes; evidence packs e feedbacks humanos; falhas, retries, bloqueios e escalonamentos; resultados de hooks, CI, homologação e deploy; incidentes, rollbacks e defeitos escapados; métricas de tempo, custo, qualidade e autonomia; demandas de melhoria geradas anteriormente.

**Pipeline.** Coletar sessões e eventos da semana → remover secrets e dados pessoais → agrupar por etapa, causa e tipo de impacto → identificar padrões recorrentes e ocorrências isoladas → comparar com semanas anteriores → distinguir aprendizado reutilizável de problema operacional → procurar contradições com a memória existente → produzir evidências e nível de confiança → submeter a um Critic Agent independente → consolidar somente itens confirmados ou explicitamente sinalizados como hipótese.

**Caminho A — aprendizado validado.** Identifica o que funcionou e em qual contexto, registra evidências e condições de reutilização, verifica duplicidade, contradição e validade temporal, e propõe inclusão, atualização ou remoção no `MEMORY.md` preservando origem e data. Preferência isolada não vira regra global.

O **gate de memória** exige evidência vinculada à conclusão, escopo e contexto explícitos, ausência de secrets ou dados pessoais, nenhuma contradição não resolvida, conhecimento acionável e reutilizável, e aprovação humana para mudança sensível.

**Caminho B — falha ou oportunidade.** Descreve o sintoma, identifica causa provável e evidências, registra frequência, impacto e etapa afetada, propõe ação corretiva e resultado esperado, classifica o tipo de melhoria (processo, harness, skill ou prompt, script ou ferramenta, hook ou gate, arquitetura do workflow, documentação ou contexto), gera demanda rastreável no backlog, relaciona sessões e incidentes de origem, e vincula duplicadas.

| Campo da demanda | Conteúdo |
|---|---|
| Título | orientado ao problema |
| Sintoma e impacto | o que se observa e o que custa |
| Evidências e frequência | origem e recorrência |
| Hipótese de causa-raiz | explicação candidata |
| Melhoria proposta | ação corretiva |
| Critério de aceite | mensurável |
| Prioridade e risco | P0–P3 e classe R |
| Owner recomendado | quem deveria assumir |
| Links | sessões e artefatos relacionados |

**Priorização.** P0 é risco crítico, segurança ou perda de dados; P1, falha recorrente que bloqueia o fluxo; P2, retrabalho, custo ou baixa confiabilidade; P3, otimização incremental. Frequência não substitui impacto, e o Auto Dream recomenda enquanto o responsável humano controla a prioridade final.

> **H6 — o sistema aprendeu corretamente?** Obrigatório para mudanças sensíveis no `MEMORY.md`, P0/P1 e alteração de gates; por amostragem para aprendizados de baixo risco e demandas P2/P3. Responsável: owner do Agent Team ou Engineering Enablement. Decide aprovar, ajustar, descartar ou solicitar mais evidências. **10–20 minutos por ciclo semanal.**

**Saídas:** `MEMORY.md` atualizado, demandas criadas ou enriquecidas no backlog, relatório semanal curto com padrões e tendências, métricas do sistema atualizadas, e hipóteses inconclusivas mantidas em observação.

**Gate de conclusão:** fontes processadas e rastreáveis; aprendizados separados de hipóteses; falhas relevantes convertidas em demandas; duplicidades e contradições tratadas; mudanças sensíveis revisadas; nenhum dado confidencial persistido indevidamente.

**Falhas do próprio ciclo.** Falha de coleta abre alerta em vez de produzir conclusão parcial silenciosa. Baixa confiança mantém o item como hipótese. Contradição bloqueia atualização automática da memória. Demanda sem evidência permanece como rascunho. O agente não aprova alterações nos próprios gates. E incidentes do Auto Dream entram no próximo ciclo de análise.

---

## 5. Como reduzir ainda mais os reviews

Cada corte abaixo só é seguro depois que o histórico demonstrar que o gate correspondente é confiável. Reduzir review antes disso não aumenta autonomia — aumenta risco não observado.

| Movimento | Pré-requisito |
|---|---|
| Combinar H2 e H3 em mudanças pequenas e conhecidas | padrão já validado em ciclos anteriores |
| Eliminar H3 quando não houver ADR, exceção ou risco relevante | classificação de risco confiável |
| Aplicar H4 por amostragem em R0 | histórico de defeitos escapados baixo |
| Tornar H5 automático em R0/R1 | rollback comprovado em produção |
| Mostrar somente diferenças desde a última aprovação | evidence pack com delta |
| Direcionar o humano aos hotspots, não ao diff completo | análise de risco por trecho |
| Usar Code Owners apenas para paths realmente sensíveis | mapeamento de paths revisado |
| Criar políticas diferentes por risco e tipo de repositório | política parametrizável |
| Remover gates sem valor | medição de falsos positivos |

---

## 6. Arquitetura de gates

As cinco camadas formam uma escada de custo crescente. O objetivo é que o feedback barato chegue primeiro e que nada que possa ser verificado por máquina chegue a uma pessoa.

| Camada | Latência | Verifica | Falha bloqueia |
|---|---|---|---|
| **Local** | segundos a poucos minutos | checks determinísticos e de baixo custo, com instrução clara de correção | commit ou push |
| **CI** | minutos | build, testes, segurança e arquitetura em ambiente limpo; seleciona checks por risco e paths | merge |
| **Merge** | decisão consolidada | aprovações e status checks; proveniência da automação; bypass silencioso e force push; invalidação após mudança material | integração |
| **Ambiente** | antes da exposição | liberação de secrets após autorização; branches e artefatos permitidos; aprovação conforme risco; observabilidade e change management | deploy |
| **Pós-deploy** | janela de observação | comparação com baseline; interrupção diante de regressão; reversão automática quando seguro; incidente quando exigir ação humana | rollout |

### 6.1 Regras para gates baseados em IA

IA pode recomendar, explicar e priorizar achados. **Bloqueio automático, não** — ele exige regra reproduzível e evidência verificável, e achado probabilístico exige confirmação independente.

Três separações são inegociáveis: o mesmo agente não produz e aprova a própria mudança; agentes não alteram gates dentro do mesmo fluxo avaliado; e mudança em rules, hooks ou CI eleva o risco automaticamente. Qualquer bypass exige pessoa autorizada, motivo e prazo de correção.

### 6.2 Contrato de escalonamento

O agente para e devolve a decisão diante de requisito contraditório ou sem owner, confiança abaixo do limite definido, duas ou mais tentativas de correção sem progresso, mudança fora do escopo aprovado, necessidade de nova permissão ou acesso externo, falha não reproduzível ou evidência inconsistente, decisão irreversível ou impacto não calculável, ou divergência entre agentes sem critério objetivo de desempate.

---

## 7. Autonomia progressiva

| Nível | O sistema faz | O humano faz |
|---|---|---|
| **A0 — assistido** | executa sob supervisão | aprova todas as transições — indicado para início do piloto |
| **A1 — execução autônoma** | implementação e validação | mantém H1, H2, H4 e H5 |
| **A2 — merge por risco** | auto-merge em R0 | review curto em R1; owners específicos em R2+ |
| **A3 — entrega autônoma controlada** | deploy automático em R0/R1, com rollback e observabilidade obrigatórios | atua em exceções e riscos altos |
| **A4 — orientado a exceções** | opera o fluxo saudável sem intervenção | recebe apenas decisões e incidentes relevantes; audita por amostragem |

**Critério para elevar autonomia.** Todos os itens abaixo, simultaneamente: volume mínimo de entregas observado; baixa taxa de defeitos escapados; rollback testado e confiável; gates com poucos falsos positivos; risco classificado corretamente; evidências completas e auditáveis; e tempo humano realmente reduzido.

---

## 8. Métricas e metas

### 8.1 Métricas do modelo

| Dimensão | Métricas |
|---|---|
| Autonomia | % de etapas concluídas sem intervenção; % de mudanças por classe de risco |
| Tempo humano | minutos humanos por entrega; tempo aguardando aprovação; decisões devolvidas por falta de contexto |
| Qualidade dos gates | aprovação na primeira passagem; falsos positivos por gate; retrabalho após H2, H3 e H4 |
| Resultado | defeitos escapados para produção; rollbacks automáticos e manuais |
| Custo e fluxo | custo de agentes por entrega; lead time e cycle time |
| Rastreabilidade | cobertura entre artefatos |

### 8.2 Meta inicial sugerida

| Meta | Valor |
|---|---|
| Atividades executadas por agentes | 80–90% |
| Tempo humano por entrega R1/R2 | até 30–45 minutos |
| Aprovações baseadas apenas em confiança no agente | zero |
| Merges protegidos por gates verificáveis | 100% |
| Mudanças R3/R4 com owner e rollback definidos | 100% |
| Auto-merge | somente após evidência do piloto |

---

## 9. Implementação do modelo

| Etapa | Entrega |
|---|---|
| **1 — Contrato mínimo** | classes de risco; responsáveis humanos; templates dos artefatos; formato do evidence pack; condições de escalonamento |
| **2 — Harness mínimo** | `AGENTS.md`, rules e skills; pre-commit e pre-push; CI fast lane e deep lane; proteção de branch e status checks; `CODEOWNERS` para paths sensíveis — detalhado em [repo harness](repo-harness.md) |
| **3 — Piloto controlado** | um fluxo R1 real em autonomia A0/A1; medição de tempo humano e falhas; ajuste de gates e templates; validação de rollback e rastreabilidade |
| **4 — Automação do roteamento** | classificação automática de risco; acionamento de Agent Teams por etapa; evidence packs automáticos; solicitação apenas dos reviewers necessários; escalonamento com contexto completo |
| **5 — Autonomia progressiva** | auto-merge em R0; deploy automático em R0/R1; ampliação por evidência, não por expectativa; auditoria humana por amostragem |

### 9.1 Próximo detalhamento recomendado

Definir o schema do Work Item; criar o template do evidence pack; desenhar a matriz `risco × gates × aprovações`; especificar os prompts e contratos de cada agente; definir os eventos que movimentam o workflow; criar o primeiro repo harness de referência; e simular uma entrega R1 de ponta a ponta.

---

## Referências operacionais

- [GitHub Rulesets e regras disponíveis](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [NIST Secure Software Development Framework](https://www.nist.gov/publications/secure-software-development-framework-ssdf-version-11-recommendations-mitigating-risk)
