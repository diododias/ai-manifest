# Contratos individuais dos loops

Este diretório contém a documentação das 12 etapas da jornada, um arquivo por loop. O conceito geral — o que é um loop, as três voltas, como agentes, skills, tools, MCPs, sensors e gates se encaixam em cada giro — está em [Loops — How Loops Work](../LOOPS.md); aqui ficam os contratos específicos.

## Como ler um contrato

Cada arquivo segue a mesma estrutura, e a leitura na ordem abaixo responde às perguntas na sequência em que normalmente surgem:

| Seção | Responde |
|---|---|
| **Contrato operacional** | o que entra, quem consolida, quem desafia, o que sai, qual gate e qual owner humano |
| **Sequência** | a ordem das missões, o que roda em paralelo e onde cada volta fecha |
| **Handoffs** | o que atravessa a fronteira na entrada e na saída |
| **O que este loop não faz** | os limites explícitos da etapa e a razão de cada um |
| **Falhas típicas** | o modo de falha recorrente e o sintoma pelo qual ele é reconhecido |
| **Artefatos e onde vivem** | o destino canônico de cada saída e o que é apenas trânsito |
| **Escalonamento** | a condição de parada e o owner humano da decisão |

Todo loop cumpre, além dessas particularidades, o **contrato comum**: seis itens obrigatórios, um único agente consolidador, crítica por instância independente, handoff que separa fato de hipótese, e artefato que só se considera entregue quando chega à fonte canônica. Um contrato individual deve ser lido como "o contrato comum, mais estas particularidades".

## Entrada

Recebe o que chega de fora e organiza o trabalho dos demais.

| # | Loop | Codinome | Consolida |
|---:|---|---|---|
| 0 | [Intake e triagem](00-intake-and-triage.md) | 🚦 Triage Loop | Intake Agent |

## Produto e discovery

Estruturam o problema antes de qualquer solução, com o par produção/crítica já presente.

| # | Loop | Codinome | Consolida |
|---:|---|---|---|
| 1 | [Discovery e research](01-discovery-and-research.md) | 🔦 Scout Loop | Product Manager Agent |
| 2 | [Planejamento de produto e UX](02-product-and-ux-planning.md) | 🎨 Studio Loop | Product Manager + UX Specification |

## Especificação

Converte o produto aprovado em estratégia técnica executável.

| # | Loop | Codinome | Consolida |
|---:|---|---|---|
| 3 | [Especificação técnica](03-technical-specification.md) | 🗺️ Drafting Loop | Specification Tech Lead Agent |

## Construção e validação

Onde a separação entre produzir e aprovar fica mais visível — e onde as três voltas giram mais rápido.

| # | Loop | Codinome | Consolida |
|---:|---|---|---|
| 4 | [Implementação autônoma](04-autonomous-implementation.md) | 🔁 Ralph Loop | Orchestrator Agent |
| 5 | [Validação adversarial](05-adversarial-validation.md) | ⚔️ Red Team Loop | QA / Validation Agent |
| 6 | [PR e merge](06-pr-and-merge.md) | 🚪 Gatekeeper Loop | PR Agent |

## Release e operação

Confirmam valor em ambiente representativo e expõem a mudança de forma controlada.

| # | Loop | Codinome | Consolida |
|---:|---|---|---|
| 7 | [Homologação](07-release-candidate-validation.md) | 🎭 Rehearsal Loop | Product Validation Agent |
| 8 | [Produção e observação](08-production-release-and-observation.md) | 🐤 Canary Loop | Release Agent |

## Conhecimento e melhoria

Fecham a volta mais longa: a que tem o próprio sistema de trabalho como objeto.

| # | Loop | Codinome | Consolida |
|---:|---|---|---|
| 9 | [Curadoria de conhecimento](09-knowledge-curation.md) | 🗄️ Archivist Loop | Knowledge Agent |
| 10 | [Telemetria e melhoria contínua](10-continuous-improvement.md) | 🌙 Dream Loop | Auto Dream Agent |
| 11 | [Operação diária](11-daily-operations.md) | ☀️ Daily Loop | Auto Dream Agent |

Os loops 10 e 11 são os únicos que giram por calendário, e não por Work Item. A [comparação entre as duas janelas](11-daily-operations.md#diário-e-semanal--por-que-são-dois-loops) explica por que são dois circuitos e não um.

---

## Caminhos de falha

Um gate reprovado não interrompe a jornada: devolve o trabalho a um loop específico. Este mapa é a resposta para "e se não passar?".

| Loop | Falha corrigível volta para | Decisão volta para |
|---|---|---|
| 🚦 Triage | origem da solicitação | PM |
| 🔦 Scout | o próprio loop, com nova pergunta | H1 — investir, ajustar, adiar ou encerrar |
| 🎨 Studio | 🔦 Scout, se faltar evidência | H2 — PM e UX |
| 🗺️ Drafting | 🎨 Studio, se o requisito for ambíguo | H3 — Tech Lead |
| 🔁 Ralph | o próprio agente, dentro do limite de tentativas | Tech Lead |
| ⚔️ Red Team | 🔁 Ralph | Tech Lead, para exceção |
| 🚪 Gatekeeper | 🔁 Ralph + revalidação em 🥊 | H4 — Code Owner |
| 🎭 Rehearsal | 🔁 Ralph, se for defeito; 🎨 Studio, se for escopo | PM ou UX |
| 🐤 Canary | rollback e 🔁 Ralph | H5 — Tech Lead; PM coaprova R3/R4 |
| 🗄️ Archivist | hipótese permanece identificada como tal | owner do domínio |
| 🌙 Dream | hipótese em observação | H6 — trio |
| ☀️ Daily | hipótese em observação até nova evidência | owner do workspace; melhoria segue ao PM via 🚦 Triage |
