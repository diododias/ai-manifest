# 05 — Manual do operador

> Como operar na prática: o que abrir, em que ordem, como despachar, como ler uma saída e como intervir sem quebrar o fluxo.

As páginas anteriores descrevem o modelo. Esta descreve o **uso**. Ela responde à pergunta de quem senta para trabalhar e precisa saber o que fazer primeiro — e, principalmente, o que fazer quando algo não sai como o contrato previa.

O princípio que organiza tudo aqui: **você opera por exceção.** O fluxo saudável não precisa de você. O que chega até você é uma decisão, um bloqueio ou uma anomalia — e para cada um existe uma resposta válida, um registro obrigatório e um limite do que pode ser feito sem envolver outra pessoa.

---

## O dia, na ordem

A sequência abaixo vale para os três papéis. O que muda é o conteúdo, não a ordem.

1. **Briefing diário.** Abrir `.coordination/daily/<data>.md`, produzido pelo [☀️ Daily Loop](../loops/11-daily-operations.md). Ler a seção *bloqueado* primeiro e responder ao que tem data-limite hoje. As demais seções são leitura, não ação.
2. **Checkpoints pendentes.** Responder aos H acumulados. Cada um chega com evidence pack; se não chegou, ele não está pronto para ser respondido — devolver por essa razão é uma resposta válida.
3. **Escalonamentos abertos.** Verificar o que parou esperando decisão. Um escalonamento sem resposta por mais de um ciclo diário reaparece no briefing do dia seguinte, com destaque.
4. **Despacho.** Iniciar o que foi priorizado, com a identidade de missão completa.
5. **Nada mais.** Se depois disso não há nada aguardando você, o fluxo está saudável. Acompanhar execução em andamento não é operação — é ansiedade com aparência de rigor.

### O que cada papel abre

| Papel | Primeiro | Depois |
|---|---|---|
| **PM** | bloqueios de produto e H1/H2 pendentes | fila de triagem, melhorias aguardando ordenação |
| **UX** | H2 pendente e aceites de experiência | itens em discovery aguardando evidência |
| **Tech Lead** | escalonamentos técnicos, H3/H4/H5 | saúde dos gates, itens em rollout, harness |

---

## Despachar uma missão

Uma missão só deve ser executada com identidade completa. **Campo ausente é autorização em branco** — o agente preencherá a lacuna com a suposição mais plausível, e a suposição só aparecerá na crítica ou, pior, no gate de CI.

| Bloco | O que declarar |
|---|---|
| Identificação | missão, Work Item, etapa e papel do agente |
| Autoridade | sponsor humano e owner da decisão |
| Direção | objetivo, resultado esperado, escopo e **fora de escopo** |
| Fontes | fontes canônicas, artefatos de entrada e de saída |
| Verificação | critérios de aceite e gates aplicáveis |
| Limites | classe de risco, autonomia autorizada, tools, permissões e budget |
| Parada | condição de parada e para quem escalar |

Antes de despachar, o item precisa satisfazer a *Definition of Ready* descrita em [Papéis](01-papeis.md). Despachar sem ela não acelera nada: transfere a ambiguidade para dentro da execução, onde descobri-la custa uma volta externa.

O campo mais negligenciado é **fora de escopo**. Ele não é redundante com o escopo: é o que impede que o agente resolva um problema adjacente que ninguém pediu, e que agora precisa ser revisado.

---

## Ler uma saída sem reler a execução

Toda missão termina em um envelope padronizado. Ele existe para que ninguém precise reler a sessão inteira para saber o que aconteceu.

| Campo | O que observar |
|---|---|
| `status` | `completed`, `partial` ou `blocked` — `partial` exige leitura das pendências |
| `confidence` | `low` nunca deve ser aprovado sem verificação adicional |
| `skills_used` | skill aderente não utilizada é sinal de procedimento reinventado |
| `sources_used` | fonte não canônica é sinal de contexto reconstruído por suposição |

### Ler um evidence pack

O evidence pack sustenta a decisão. A leitura eficiente segue três movimentos, nesta ordem: **delta** (o que mudou desde a última vez que você olhou), **pendências** (o que permanece em aberto e por quê) e **evidências** (o resultado bruto dos gates, consultado apenas se algo nos dois anteriores não fechar).

O teste de qualidade do pacote é objetivo: **outra pessoa consegue refazer a verificação sem perguntar nada a quem a produziu?** Se precisa de contexto adicional, o que chegou é um resumo, não evidência — e devolver por essa razão é a resposta correta.

---

## Responder a um escalonamento

Um agente escala quando encontra requisito contraditório ou sem owner, confiança abaixo do limite, duas ou mais tentativas de correção sem progresso, mudança fora do escopo aprovado, necessidade de novo acesso, falha não reproduzível, decisão irreversível, ou divergência entre agentes sem critério objetivo de desempate.

As respostas válidas são cinco. Escolher entre elas é a operação mais frequente do modelo.

| Resposta | Quando | O que registrar |
|---|---|---|
| **Decidir** | a informação existe e a decisão é sua | a decisão e a razão |
| **Esclarecer** | falta contexto, e o agente pode seguir com ele | o esclarecimento como parte do artefato, não como mensagem |
| **Reduzir escopo** | parte do trabalho é executável e parte não | novo fora de escopo, explicitamente |
| **Devolver a um loop anterior** | o problema nasceu antes desta etapa | a pergunta que motivou a devolução |
| **Encerrar** | o item não deve prosseguir | a razão, e o vínculo se foi absorvido por outro item |

O que **não** é resposta válida: mandar tentar de novo sem mudar nada. Se nada mudou na entrada, a saída será a mesma, e o custo da volta é real.

---

## Intervir sem quebrar o fluxo

Intervenções são normais e previstas. O que as torna seguras é o registro — uma intervenção não registrada some do histórico e distorce a telemetria que o [🌙 Dream Loop](../loops/10-continuous-improvement.md) usa para melhorar o desenho dos loops.

| Intervenção | Efeito | Quem pode | Registro |
|---|---|---|---|
| **Parar** um loop em curso | interrompe antes do próximo handoff | owner do loop | razão e estado em que parou |
| **Reverter** um rollout | remove a exposição | Tech Lead | sinal observado e decisão |
| **Reduzir escopo** | preserva o avanço parcial | PM | novo fora de escopo |
| **Elevar risco** | acrescenta gates e aprovações | qualquer um do trio | o que motivou a elevação |
| **Abrir exceção** | libera o avanço com dívida declarada | Tech Lead | ADR com prazo e plano de reversão |
| **Rebaixar autonomia** | reintroduz checkpoints | Tech Lead | a métrica que motivou |

Sobre a linha mais delicada: **abrir exceção é diferente de ignorar o gate.** A exceção declara a dívida, nomeia o prazo e descreve como se sai dela. Um bypass sem esses três elementos não é exceção — é o gate deixando de existir para aquele caso, e nada no sistema registrará isso.

E sobre a última: **rebaixar autonomia é operação normal**, não fracasso. A autonomia sobe por evidência e desce pela mesma via. Um sistema em que ela só sobe está medindo mal.

---

## O que fazer quando o modelo parece atrapalhar

Três situações recorrentes, com a leitura correta de cada uma.

**"O checkpoint chegou sem o que eu preciso para decidir."** O evidence pack está incompleto. Devolver é a resposta correta, e a devolução é um dado: se acontece com frequência, o problema está no template do pacote, não na etapa. Encaminhar como melhoria.

**"O gate reprovou algo que está certo."** É um falso positivo, e falsos positivos são medidos. Um gate com índice alto não é rigor — é ruído que treina o time a ignorar sinal. Registrar a ocorrência e levar a mudança do gate ao caminho próprio, que exige revisor independente.

**"Eu resolveria isso mais rápido na mão."** Provavelmente sim, uma vez. A pergunta relevante é se o caso se repete. Se sim, ele é uma skill ou uma automação faltando, e resolver na mão é o que impede que isso apareça. Se não, resolver na mão é legítimo — desde que o resultado chegue à fonte canônica como qualquer outro artefato.

---

## O que nunca fazer

| Nunca | Por quê |
|---|---|
| Aprovar sem evidence pack | a aprovação passa a se basear no resumo de quem produziu |
| Deixar um checkpoint sem resposta como forma de recusa | silêncio não é aprovação, mas também não é decisão — o item apenas para |
| Ampliar o escopo de uma missão em curso | o risco foi classificado sobre o escopo original |
| Editar um artefato aprovado sem reabrir a decisão | mudança material invalida a aprovação relacionada |
| Resolver um conflito de domínio por consenso sem owner | reaparece como retrabalho na primeira contestação |
| Alterar um gate dentro do fluxo que ele está avaliando | é a definição de juiz em causa própria |

---

*Anterior: [Ritmos e cadências](04-ritmos-e-cadencias.md) · Próximo: [Jornada comentada](06-jornada-comentada.md).*
