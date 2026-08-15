# 03 — Gatilhos e disparos

> O que dispara o quê, quando, e o que nunca dispara sozinho.

Um catálogo de loops descreve o que acontece **dentro** de cada etapa. Ele não responde à pergunta que aparece na primeira semana de operação: *o que faz a próxima etapa começar?* Se a resposta for "alguém lembra", o modelo não é agentico — é um processo manual com agentes dentro.

Esta página documenta o sistema nervoso do fluxo. Todo movimento tem um gatilho declarado, e todo gatilho pertence a uma de três naturezas, com propriedades diferentes.

| Natureza | Origem | Propriedade que a define |
|---|---|---|
| **Por evento** | algo mudou de estado no sistema | reage imediatamente e não depende de ninguém lembrar |
| **Por calendário** | passou o tempo | acontece mesmo quando não houve entrega |
| **Manual** | uma pessoa acionou | é sempre registrado, nunca implícito |

A regra que atravessa as três: **um gatilho que não deixa rastro não existe.** Toda ativação registra origem, momento, missão despachada e owner notificado — é isso que permite ao [🌙 Dream Loop](../loops/10-continuous-improvement.md) medir o desenho do fluxo em vez de opinar sobre ele.

---

## Disparos por evento

A coluna mais importante é a última: **quem fica sabendo**. Um disparo que aciona um agente sem notificar ninguém produz trabalho invisível, e trabalho invisível é o que aparece semanas depois como surpresa.

| Evento | Aciona | Consolida | Notifica |
|---|---|---|---|
| Solicitação, incidente ou feedback chega | [🚦 Triage Loop](../loops/00-intake-and-triage.md) | Intake Agent | PM |
| Transcrição de reunião registrada | Meeting Context → [🚦 Triage](../loops/00-intake-and-triage.md) | Intake Agent | PM |
| Work Item priorizado pelo PM | [🔦 Scout Loop](../loops/01-discovery-and-research.md) | Product Manager Agent | PM e UX |
| Gate de discovery aprovado | **H1** | — | PM ou sponsor |
| H1 respondido com "avançar" | [🎨 Studio Loop](../loops/02-product-and-ux-planning.md) | PM + UX Specification | PM e UX |
| Gate de produto aprovado | **H2** | — | PM, com UX |
| H2 aprovado | [🗺️ Drafting Loop](../loops/03-technical-specification.md) | Specification Tech Lead | Tech Lead |
| ADR nova, exceção ou risco R3/R4 detectados | **H3** | — | Tech Lead |
| Especificação aprovada, tarefas elegíveis | [🔁 Ralph Loop](../loops/04-autonomous-implementation.md) | Orchestrator Agent | ninguém, no fluxo saudável |
| Sensor local reprova | volta interna do próprio agente | o agente | ninguém, dentro do limite de tentativas |
| Limite de tentativas atingido | escalonamento | Orchestrator | Tech Lead |
| Push com mudança pronta | [⚔️ Red Team Loop](../loops/05-adversarial-validation.md) e CI | QA / Validation | ninguém, se verde |
| CI reprova | volta para [🔁 Ralph](../loops/04-autonomous-implementation.md) | Orchestrator | Tech Lead, se recorrente |
| Validação adversarial aprovada | [🚪 Gatekeeper Loop](../loops/06-pr-and-merge.md) | PR Agent | Code Owners dos paths tocados |
| PR aberto com CI verde | **H4**, conforme risco | — | Code Owner |
| Merge concluído | [🎭 Rehearsal Loop](../loops/07-release-candidate-validation.md) | Product Validation | PM e UX, se houver experiência nova |
| Release candidate aprovado | [🐤 Canary Loop](../loops/08-production-release-and-observation.md) | Release Agent | Tech Lead |
| Risco R3/R4 ou exposição crítica | **H5** | — | Tech Lead e PM |
| Janela de observação sem regressão | [🗄️ Archivist Loop](../loops/09-knowledge-curation.md) | Knowledge Agent | owner do domínio |
| Regressão detectada após deploy | rollback automático e volta para [🔁 Ralph](../loops/04-autonomous-implementation.md) | Release + Observability | Tech Lead, imediatamente |
| Incidente em produção | [🚦 Triage](../loops/00-intake-and-triage.md) com prioridade elevada | Intake Agent | PM e Tech Lead |

### Eventos que mudam a classe de risco

Alguns eventos não acionam um loop: eles alteram quantas aprovações o item passará a exigir. Reconhecê-los é o que impede que uma mudança se torne perigosa sem que nada no fluxo registre isso.

| Evento | Efeito |
|---|---|
| Mudança toca path sensível declarado | eleva risco automaticamente |
| Mudança altera rules, sensors ou CI | eleva risco automaticamente e exige revisor independente |
| Escopo alterado após aprovação | recalcula risco e invalida a aprovação relacionada |
| Dúvida relevante permanece aberta | impede classificação como R0 ou R1 |

---

## Disparos por calendário

Dois circuitos giram por tempo. Eles existem porque o que observam — o estado do sistema de trabalho — não gera evento próprio: um item parado há três dias não dispara nada por si mesmo.

| Cadência | Aciona | Consolida | Entrega a |
|---|---|---|---|
| **Diária, início do dia** | [☀️ Daily Loop](../loops/11-daily-operations.md) | Auto Dream Agent | briefing ao owner do workspace |
| **Semanal** | [🌙 Dream Loop](../loops/10-continuous-improvement.md) | Auto Dream Agent | H6, ao trio |
| **Extraordinária, após incidente relevante** | [🌙 Dream Loop](../loops/10-continuous-improvement.md) | Auto Dream Agent | H6, ao trio |

O detalhe do que cada cadência faz está em [Ritmos e cadências](04-ritmos-e-cadencias.md). O que importa aqui é a propriedade: **um disparo por calendário não pode ser silenciosamente pulado.** Falha de coleta abre alerta; um dia sem dados é um sinal, não a ausência de um.

---

## Disparos manuais

Existe um conjunto pequeno de acionamentos que uma pessoa faz diretamente. Todos são registrados, e a maioria é uma forma de **intervir no fluxo**, não de iniciá-lo.

| Ação | Quem pode | Efeito | Registro obrigatório |
|---|---|---|---|
| Priorizar ou despriorizar um Work Item | PM | move o item para a fila de discovery, ou o retira | razão da mudança |
| Devolver um artefato a um loop anterior | owner do checkpoint | reabre a etapa com pergunta nova | a pergunta que motivou a devolução |
| Solicitar discovery adicional | PM ou UX | nova rodada do [🔦 Scout](../loops/01-discovery-and-research.md) com escopo declarado | a lacuna a ser fechada |
| Abrir exceção arquitetural | Tech Lead | libera o avanço com dívida declarada | ADR com prazo e plano de reversão |
| Pausar ou reverter um rollout | Tech Lead | interrompe a exposição | sinal observado e decisão |
| Rebaixar nível de autonomia | Tech Lead | reintroduz checkpoints | métrica que motivou |
| Executar um loop em `dry-run` | qualquer owner | valida o contrato sem efeito colateral | nenhum, por não haver efeito |

Um comentário sobre o penúltimo item. **Rebaixar autonomia é uma ação normal do modelo**, não uma admissão de fracasso. A autonomia sobe por evidência e desce pela mesma via; um sistema em que ela só sobe está medindo mal.

---

## O que nunca dispara sozinho

Esta é a lista que define o limite do modelo. Cada linha tem uma razão estrutural, não uma preferência de estilo.

| Nunca automático | Por quê |
|---|---|
| Prioridade de um Work Item | prioridade é comparação entre itens, e a comparação exige a intenção do negócio |
| Aprovação de escopo | quem propôs o escopo tem incentivo estrutural para aprová-lo |
| Exceção arquitetural | uma exceção que se concede sozinha deixa de ser exceção |
| Exposição de risco R3/R4 | o custo de errar é irreversível ou de grande alcance |
| Alteração de gate, rule ou nível de autonomia | um sistema que relaxa a própria verificação converge para a ausência de verificação |
| Encerramento de um item por duplicidade | encerrar sem vínculo explícito faz o item sumir do rastro |
| Escrita em `MEMORY.md` de aprendizado de baixa confiança | memória inflacionada deixa de ser lida, e memória não lida é pior que ausente |

A regra geral por trás das sete linhas: **automação decide o verificável; pessoa decide o comparável e o irreversível.**

---

## Como um disparo é executado

Todo acionamento — por evento, calendário ou mão humana — atravessa a mesma sequência antes de virar trabalho. Ela existe para que nenhuma missão comece sem autoridade declarada.

1. O gatilho é registrado com origem, momento e item afetado.
2. O Orchestrator monta a **identidade da missão**: objetivo, escopo e fora de escopo, fontes canônicas, critérios de aceite, gates, risco, tools autorizadas, budget, condição de parada e owner humano.
3. A missão é despachada ao agente consolidador do loop correspondente.
4. O loop gira conforme seu contrato em [`loops/`](../loops/README.md).
5. O envelope de saída volta ao Orchestrator com status, confiança e skills usadas.
6. O handoff atravessa a fronteira: o artefato chega à fonte canônica e o owner é notificado se houver decisão pendente.

**Uma missão com qualquer campo de identidade ausente não deve ser executada** — a ausência é, na prática, uma autorização em branco. O detalhe dos campos está em [Agentes](../AGENTES.md).

---

## Falhas típicas do sistema de disparos

| Falha | Sintoma | Correção |
|---|---|---|
| Gatilho implícito | uma etapa só começa quando alguém pergunta por ela | declarar o evento que a inicia, ou aceitá-la como cadência |
| Disparo sem notificação | trabalho concluído que ninguém sabia estar em curso | todo disparo declara quem é notificado, mesmo que seja "ninguém" |
| Escalonamento sem prazo | o item fica em aberto indefinidamente | escalonamento carrega decisão pedida e data-limite |
| Cadência pulada em silêncio | um dia ou uma semana somem do histórico | falha de coleta abre alerta, nunca resultado vazio |
| Reentrada não declarada | o trabalho volta a um loop anterior sem registro | toda devolução carrega a pergunta que a motivou |

---

*Anterior: [Checkpoints humanos](02-checkpoints-humanos.md) · Próximo: [Ritmos e cadências](04-ritmos-e-cadencias.md).*
