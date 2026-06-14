# Fluxo de trabalho AI First — Spec Driven Development

---

## 0. Preparação da feature

**Responsáveis:** PM / PA

### Atividades

**Geração do roteiro de agenda**
O PM utiliza a **Skill: Business Discovery Preparation** para estruturar a demanda antes de qualquer reunião com o time técnico. A skill realiza uma entrevista interativa com o PM, cobrindo 10 seções obrigatórias e opcionais: contexto, recap, problema de negócio, fluxo principal, regras de negócio, exceções, fora de escopo, cenários de aceite, dúvidas em aberto e materiais de apoio.

**Preenchimento do roteiro**
O PM responde perguntas abertas para cada seção. A skill força a explicitação de contexto implícito — "aquele fluxo que a gente falou" vira definição concreta. Seções opcionais podem ser puladas, ficando marcadas como `[PENDENTE — confirmar na agenda]`. Métricas vagas ("rápido", "fácil") são flagradas como gaps imediatamente.

**Validação e geração**
A skill gera o arquivo `roteiro-preenchido.md` com as respostas estruturadas, incluindo lista de gaps detectados (métricas sem número, regras sem exemplo, cenários sem "Então"). O roteiro é compartilhado com o dev antes da reunião para que ele leia e leve dúvidas à agenda.

### Output

- `roteiro-preenchido.md` estruturado com 10 seções
- Lista de gaps detectados para confirmar na agenda
- Roteiro pronto para usar como pauta na reunião

---

## 1. Descoberta de requisitos

**Responsáveis:** PM / PA / Dev

### Atividades

**Processamento da transcrição**
Após a reunião com transcrição gravada, o time utiliza a **Skill: Business Discovery** para extrair requisitos de negócio estruturados a partir da transcrição. A skill recebe como entrada o `roteiro-preenchido.md` (baseline) e a transcrição da agenda, e realiza um diff entre os dois — identificando o que é novo, o que foi alterado e o que foi contradito.

**Extração de requisitos**
A skill extrai da transcrição:
- **User stories** — quem, quer o quê, pra quê, com prioridade (P1 = MVP, P2/P3 = incremento)
- **Cenários (Dado / Quando / Então)** — exemplos testáveis ditos na agenda, em Gherkin pt-BR
- **Regras de negócio (RN-XX)** — cada uma com pré-condição + gatilho + "o sistema deve" + resposta, e exemplo concreto/numérico
- **Critérios de sucesso (SC-XX)** — métrica de negócio com número (adjeto vago sem alvo = gap)
- **Fluxos** — happy path e exceções / edge cases
- **Decisões** tomadas na agenda
- **Termos de domínio** → glossário
- **Fora de escopo** dito explicitamente

**Gap detection**
A skill sinaliza lacunas residuais: referências não resolvidas ("aquele fluxo"), regras sem exemplo concreto, cenários sem "Então" claro, métricas sem número. Essas lacunas viram `DA-XX` (dúvidas em aberto) com dono e prazo, para serem resolvidas na próxima agenda.

**Status da feature**
A skill atualiza o status da feature: 🟡 em descoberta → 🟢 pronto pra especificar (quando gaps estão resolvidos). O `requisitos.md` é um documento vivo — cada agenda acumula contexto, nunca descarta.

### Output

- `requisitos.md` com RN-XX, US-X, cenários D/Q/E, SC-X, glossário e gaps
- Changelog com data da agenda e resumo do delta (novo/alterado/contradito)
- Lista de `DA-XX` para levar na próxima agenda

---

## 2. Refinamento da feature

**Responsáveis:** PM / PA

### Atividades

**Preparação prévia**
O PM prepara material com sua visão da feature e as histórias associadas antes da agenda de refinamento.

**Agenda gravada com transcrição**
Reunião realizada em conjunto com o time técnico para contextualização da demanda. A agenda é gravada e transcrita para servir como base dos artefatos gerados na sequência.

**Escrita da feature e do PRD**
PM ou PA utiliza o `requisitos.md` (gerado na etapa de Descoberta de requisitos) como base para escrever a feature e gerar o PRD Plan. Duas skills podem ser utilizadas nessa etapa: a **Skill: Geração de histórias** para extrair e estruturar as histórias a partir do `requisitos.md` e da transcrição, e a **Skill: Escrita de PRD** para gerar o PRD Plan a partir das histórias escritas e dos critérios de sucesso (SC-XX) e regras de negócio (RN-XX) já extraídos.

### Output

- Feature escrita
- Histórias escritas
- PRD Plan gerado

---

## 3. Refinamento das histórias

**Responsáveis:** Tech Lead / responsável pelo refinamento técnico

### Atividades

**Preparação prévia**
O Tech Lead prepara material com sua visão técnica da solução antes da agenda de refinamento técnico.

**Agenda gravada com transcrição**
Reunião realizada em conjunto com o time técnico para apresentação e discussão da solução. Essa etapa pode se repetir quantas vezes forem necessárias até que o time chegue a um consenso sobre a solução técnica. A SPEC é considerada pronta quando aprovada pelo Tech Lead e por pelo menos um engenheiro que irá implementar a história.

**Escrita do refinamento técnico e da SPEC**
Com base na transcrição da agenda, o Tech Lead escreve a visão técnica das histórias e gera o SPEC Plan. A **Skill: Geração de SPEC** pode ser utilizada para estruturar a SPEC a partir do PRD e da transcrição. Em seguida, a **Skill: Revisão de SPEC** identifica gaps, ambiguidades e critérios de aceite faltando antes da SPEC ser considerada pronta.

### Output

- Visão técnica das histórias escrita
- SPEC Plan gerado

---

## 4. Planejamento

**Responsáveis:** Time completo

### Atividades

**Revisão da SPEC com IA**
Antes do sprint planning, a **Skill: Revisão cruzada PRD vs SPEC** é executada para identificar inconsistências entre os dois artefatos. Pontos levantados são resolvidos antes da pontuação.

**Sprint planning**
O time realiza a pontuação das histórias em complexity points e define quais histórias entrarão na sprint, respeitando a capacidade do time e a granularidade já estabelecida no refinamento.

---

## 5. Execução

**Responsáveis:** Engenheiro / ferramentas de IA

O time opera em dois modos dependendo das ferramentas disponíveis para cada engenheiro:

- **Modo assistido:** engenheiro com Copilot, onde a IA auxilia a geração mas o engenheiro conduz ativamente cada passo
- **Modo delegado:** engenheiro com Devin ou Claude, onde é possível delegar blocos maiores de implementação e validar o resultado ao final

---

### Ciclo 0 — Planejamento da execução

Antes de qualquer geração de código, o engenheiro utiliza a **Skill: Planejamento da execução** para transformar a SPEC em um plano de implementação passo a passo. Esse plano define a sequência de trabalho, identifica dependências internas e serve como guia para os ciclos seguintes — independente do modo de trabalho.

---

### Ciclo 1 — Geração

**Leitura e validação da SPEC**
Antes de qualquer implementação, o engenheiro lê a SPEC da história e valida que entendeu o escopo completo. Dúvidas são resolvidas com o Tech Lead. 

**Geração de código**

*Modo assistido — Copilot:*
O engenheiro usa a SPEC e o plano de execução como base para os prompts enviados ao Copilot, alimentando o contexto por seção. A SPEC não é enviada inteira de uma vez; cada bloco lógico do plano vira um prompt direcionado. O engenheiro conduz ativamente cada iteração.

*Modo delegado — Devin ou Claude:*
O engenheiro delega blocos maiores de implementação utilizando a SPEC e o plano de execução como contexto. A validação acontece ao final de cada bloco delegado, não a cada iteração.

**Revisão e ajuste do output da IA**
O engenheiro revisa o código gerado, ajusta inconsistências e valida que o output está alinhado com a SPEC antes de avançar para o ciclo de validação.

---

### Ciclo 2 — Validação

**Testes automatizados**
O engenheiro executa testes unitários, testes de mutação e validação local. A **Skill: Geração de testes** é utilizada para gerar os casos de teste a partir dos critérios de aceite da SPEC — junto com o código, não após a implementação.

**Self-check dos critérios de aceite**
Antes de abrir o PR, o engenheiro percorre cada critério de aceite da SPEC e confirma que está coberto. Esse check é explícito, não implícito.

**Geração do material de homologação**
O engenheiro utiliza a **Skill: Escrita de material de homologação** para gerar o material de homologação seguindo o template do time. Esse material é submetido para aprovação do Tech Lead e do PM antes de o PR seguir para code review — a aprovação da homologação é o gatilho para a etapa de revisão.

### Output
- Código implementado
- Testes passando
- Material com evidências da homologação aprovado
---

## 6. Documentação

**Responsáveis:** Engenheiro, PM, Tech Lead, IA

### Atividades

**Homologação**
Tech Lead e PM revisam e aprovam a entrega. A aprovação é o gatilho para a etapa de documentação.

**Atualização dos artefatos**
PRD e SPEC são incrementados para refletir o código efetivamente entregue, utilizando o PRD Plan e o SPEC Plan como base. A **Skill: Diff SPEC vs entregue** auxilia na identificação das diferenças entre o planejado e o implementado.

**Documentação oficial**
Atualização do README e dos canais de documentação oficiais do time. A **Skill: Atualização de README** auxilia na escrita a partir do conteúdo do PRD e da SPEC atualizados.

**Commit e PR final**
O engenheiro commita a documentação com auxílio da IA e gera o PR utilizando a **Skill: Escrita de PR**, que estrutura a descrição seguindo o template do time.

### Output

- PRD e SPEC atualizados refletindo o código entregue
- README atualizado
- Documentação publicada nos canais oficiais do time
- PR aberto seguindo o template do time

---

## 7. Revisão

**Responsáveis:** Tech Lead, ferramentas de IA

### Atividades

**Revisão assistida por IA**
A **Skill: Revisão de PR** verifica a conformidade do PR com a SPEC, a qualidade do código e a cobertura de testes. A IA atua como filtro inicial antes de o PR chegar aos revisores humanos. O PR continua exigindo duas aprovações manuais.

**Aprovação do Tech Lead**
O critério principal de aprovação é a conformidade com a SPEC, não apenas qualidade de código. Desvios sem justificativa retornam ao engenheiro. Desvios justificados podem gerar atualização da SPEC antes do merge.

**Confirmação dos artefatos**
Após o merge, confirma-se que PRD e SPEC estão atualizados e consistentes com o que foi entregue. Esse passo fecha o ciclo e garante que os artefatos permanecem confiáveis para as próximas histórias.

### Output

- PR aprovado e merged

---

## 8. Catálogo de skills

As skills são instruções estruturadas que orientam a IA a executar tarefas específicas do fluxo de forma padronizada. Cada skill define o contexto necessário, o que a IA deve fazer e qual o formato esperado do output.

---

### Skill: Business Discovery Preparation

**Quando usar:** antes de qualquer reunião de refinamento com o time técnico.

**Input necessário:** nenhum obrigatório — começa do zero ou com material já trazido (PRD, mockup, docs).

**O que faz:** realiza entrevista interativa com o PM para preencher um roteiro de agenda estruturado com 10 seções (contexto, recap, problema de negócio, fluxo principal, regras, exceções, fora de escopo, cenários, dúvidas, materiais). Força a explicitação de contexto implícito, oferece skip para seções opcionais e flagra gaps (métricas sem número, regras sem exemplo, cenários sem "Então").

**Output esperado:** `roteiro-preenchido.md` com seções preenchidas e lista de gaps detectados, pronto para usar como pauta na reunião.

---

### Skill: Business Discovery

**Quando usar:** após a reunião com transcrição gravada, para extrair requisitos de negócio.

**Input necessário:** `roteiro-preenchido.md` (baseline da preparação) e transcrição da agenda.

**O que faz:** extrai da transcrição user stories (com prioridade P1/P2/P3), cenários em Gherkin pt-BR (Dado/Quando/Então), regras de negócio estruturadas (RN-XX), critérios de sucesso mensuráveis (SC-XX), fluxos, decisões, glossário e fora de escopo. Realiza diff contra o baseline — classificando itens como novos, alterados ou contraditos. Detecta lacunas residuais (referências não resolvidas, regras sem exemplo, métricas vagas) e gera dúvidas em aberto (DA-XX) com dono e prazo.

**Output esperado:** `requisitos.md` documento vivo com changelog por agenda, status da feature (🟡 descoberta / 🟢 pronto pra especificar) e lista de gaps para próxima agenda.

---

### Skill: Geração de histórias

**Quando usar:** etapa de refinamento da feature, após a descoberta de requisitos.

**Input necessário:** `requisitos.md` (com US-X, cenários e SC-X) e transcrição da agenda de refinamento.

**O que faz:** extrai as histórias discutidas na agenda, estrutura cada uma no formato padrão do time (contexto, critérios de aceite, dependências) e identifica histórias que precisam ser fatiadas. Utiliza os US-X e cenários já extraídos pelo Business Discovery como ponto de partida.

**Output esperado:** lista de histórias escritas no formato padrão, prontas para revisão do PM.

---

### Skill: Escrita de PRD

**Quando usar:** etapa de refinamento da feature, após as histórias escritas.

**Input necessário:** histórias escritas, `requisitos.md` e transcrição da agenda de refinamento.

**O que faz:** estrutura o PRD Plan consolidando o objetivo da feature, as histórias associadas, os critérios de sucesso (SC-XX) e as regras de negócio (RN-XX) extraídas pelo Business Discovery, além das restrições identificadas na agenda.

**Output esperado:** PRD Plan no formato padrão do time.

---

### Skill: Geração de SPEC

**Quando usar:** etapa de refinamento das histórias, após a agenda técnica gravada e transcrita.

**Input necessário:** PRD Plan, histórias escritas e transcrição da agenda de refinamento técnico.

**O que faz:** gera o SPEC Plan estruturando a solução técnica, os componentes envolvidos, o fluxo de implementação e os critérios de aceite técnicos para cada história.

**Output esperado:** SPEC Plan no formato padrão do time, pronto para revisão do Tech Lead.

---

### Skill: Revisão de SPEC

**Quando usar:** etapa de refinamento das histórias, antes de a SPEC ser considerada pronta.

**Input necessário:** SPEC Plan gerado e PRD Plan correspondente.

**O que faz:** analisa a SPEC em busca de gaps (requisitos do PRD não cobertos), ambiguidades (critérios de aceite vagos ou subjetivos) e inconsistências internas. Gera uma lista de pontos a resolver antes da aprovação.

**Output esperado:** relatório de pontos a resolver, classificados por severidade.

---

### Skill: Revisão cruzada PRD vs SPEC

**Quando usar:** etapa de planejamento, antes do sprint planning.

**Input necessário:** PRD Plan e SPEC Plan da sprint.

**O que faz:** verifica se todos os requisitos do PRD estão cobertos pela SPEC, se há itens na SPEC sem correspondência no PRD e se os critérios de aceite estão alinhados entre os dois artefatos.

**Output esperado:** lista de inconsistências e gaps, com sugestão de resolução para cada item.

---

### Skill: Planejamento da execução

**Quando usar:** Ciclo 0 da execução, antes de qualquer geração de código.

**Input necessário:** SPEC Plan da história.

**O que faz:** transforma a SPEC em um plano de implementação sequencial, definindo a ordem dos blocos de trabalho, identificando dependências internas entre os blocos e sugerindo o ponto de início mais seguro. Serve como guia tanto para o modo assistido (Copilot) quanto para o modo delegado (Devin ou Claude).

**Output esperado:** plano de implementação passo a passo, com blocos ordenados e dependências mapeadas.

---

### Skill: Geração de testes

**Quando usar:** Ciclo 2 da execução, junto com a implementação — não após.

**Input necessário:** critérios de aceite da SPEC e código implementado do bloco correspondente.

**O que faz:** gera casos de teste unitários e de mutação a partir dos critérios de aceite, cobrindo os cenários de sucesso, falha e edge cases descritos na SPEC.

**Output esperado:** casos de teste prontos para execução, organizados por critério de aceite.

---

### Skill: Diff SPEC vs entregue

**Quando usar:** etapa de documentação, após a homologação.

**Input necessário:** SPEC Plan original e código entregue (ou descrição da implementação real).

**O que faz:** identifica as diferenças entre o que foi planejado na SPEC e o que foi efetivamente implementado, classificando cada diferença como desvio intencional documentado, ajuste de escopo ou gap a ser endereçado.

**Output esperado:** relatório de diferenças, com indicação do que deve atualizar o PRD e a SPEC.

---

### Skill: Atualização de README

**Quando usar:** etapa de documentação, após a atualização dos artefatos.

**Input necessário:** PRD e SPEC atualizados, README atual.

**O que faz:** identifica as seções do README que precisam ser atualizadas com base nas mudanças entregues e gera o conteúdo atualizado no mesmo estilo e formato do documento existente.

**Output esperado:** README atualizado, pronto para revisão e commit.

---

### Skill: Escrita de PR

**Quando usar:** etapa de documentação, no momento do commit final.

**Input necessário:** SPEC Plan, código implementado e template de PR do time.

**O que faz:** estrutura a descrição do PR seguindo o template do time, preenchendo contexto da mudança, o que foi implementado, o que foi testado e desvios da SPEC documentados com justificativa.

**Output esperado:** descrição do PR preenchida, pronta para abertura.

---

### Skill: Revisão de PR

**Quando usar:** etapa de revisão, antes de o PR chegar aos revisores humanos.

**Input necessário:** SPEC Plan da história e conteúdo do PR (código, testes, descrição).

**O que faz:** verifica a conformidade do PR com a SPEC, analisa a cobertura de testes em relação aos critérios de aceite e sinaliza desvios sem justificativa. Gera um resumo estruturado para o Tech Lead antes da aprovação manual.

**Output esperado:** relatório de conformidade com a SPEC, lista de pontos de atenção e recomendação de aprovação ou revisão.

---

*Versão 1.2 — fluxo AI First com Spec Driven Development*
