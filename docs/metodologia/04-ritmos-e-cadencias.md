# 04 — Ritmos e cadências

> O que acontece todo dia, toda semana e a cada marco — independentemente de qualquer entrega estar em curso.

A jornada descreve o caminho de **um** Work Item. O ritmo descreve o que acontece **todo dia**, tenha ou não havido entrega. São eixos diferentes, e confundi-los produz o erro mais comum na adoção do modelo: acreditar que, sem item em voo, não há nada a operar.

Há sempre algo a operar. Itens parados não geram evento próprio, aprendizados dispersos em sessões não se consolidam sozinhos, e o custo de um atrito recorrente só aparece quando alguém soma as ocorrências. É para isso que existem as cadências.

| Cadência | O que roda | Saída | Tempo humano |
|---|---|---|---:|
| **Diária** | [☀️ Daily Loop](../loops/11-daily-operations.md) | briefing, memória, itens no intake | ≤ 10 min de leitura |
| **Por entrega** | checkpoints H1–H5, por evento | decisão registrada | 30–45 min por entrega R1/R2 |
| **Semanal** | triagem de backlog e [🌙 Dream Loop](../loops/10-continuous-improvement.md) + H6 | backlog ordenado, aprendizado validado | 40–65 min |
| **Por marco** | revisão de risco e de autonomia | subida, manutenção ou rebaixamento | 30–60 min |

---

## Diária — o pulso

Todo início de dia, o [☀️ Daily Loop](../loops/11-daily-operations.md) lê as sessões encerradas desde a última execução e devolve ao owner um briefing curto. É a única cadência que roda mesmo em um dia sem nenhuma entrega.

### O que o loop faz

Ele separa quatro naturezas que não podem ser lidas juntas — o que foi concluído, o que ficou pendente, o que falhou e por qual causa, e o que só uma pessoa pode decidir — e converte cada uma em um destino diferente.

| Natureza | Destino |
|---|---|
| Padrão recorrente com evidência de sessão | proposta de atualização de `MEMORY.md` |
| Atrito reproduzível | Work Item no [🚦 Triage Loop](../loops/00-intake-and-triage.md) |
| Decisão pendente ou bloqueio | briefing ao owner |
| Ocorrência isolada | hipótese em observação, insumo do ciclo semanal |

### O que o owner faz

A leitura é de poucos minutos e tem uma ordem obrigatória, que é a mesma em que o briefing é montado.

1. **Bloqueado** — precisa de decisão hoje. Cada item traz a decisão pedida e a data-limite. Esta é a única parte que exige ação imediata.
2. **Em risco** — vai bloquear se ninguém agir. Decidir agora ou aceitar conscientemente que vire bloqueio.
3. **Em andamento** — informativo. Existe para que o owner saiba onde o trabalho está, não para que aprove nada.

A pauta cobre apenas bloqueios, informação nova e pedidos de decisão. **O que este ritmo não deve virar:** uma reunião diária de relato individual. Narrar status é função do artefato assíncrono; a pessoa entra para desbloquear.

### O que sai daqui e não volta

Duas saídas do ritmo diário atravessam a fronteira e passam a viver em outro lugar: a atualização de memória, que vai para `MEMORY.md`, e a melhoria, que vira Work Item no intake. **Nenhuma melhoria fica registrada apenas no briefing** — o briefing tem validade de um dia, e o que só existe nele desaparece.

---

## Por entrega — os checkpoints

Esta cadência não tem calendário: ela é disparada por evento, conforme o [mapa de gatilhos](03-gatilhos-e-disparos.md). Um item de baixo risco atravessa três decisões humanas; um item R3/R4 atravessa até seis.

A propriedade a preservar é que **checkpoint não espera reunião**. Ele chega ao owner com o evidence pack montado e é respondido de forma assíncrona. Agendar um checkpoint para a próxima cerimônia converte minutos de decisão em dias de espera — e é a causa mais comum de lead time alto em times que adotaram o modelo corretamente em todo o resto.

O detalhe de cada checkpoint está em [Checkpoints humanos](02-checkpoints-humanos.md).

---

## Semanal — triagem e aprendizado

A semana tem dois momentos distintos, com owners e objetos diferentes. Um olha para o produto; o outro, para o sistema que constrói o produto.

### Triagem de prioridade

Owner: PM. Recebe novos Work Items, métricas, feedback, incidentes, dependências e capacidade; devolve o backlog ordenado, com owner e risco inicial atribuídos, e a lista do que precisa de discovery.

O gate é simples: cada item que sai da triagem tem contexto, prioridade e responsável minimamente claros. Um item que não atinge isso volta à origem como pergunta — não entra no backlog como incógnita.

É aqui também que entram as melhorias que o ritmo diário e o semanal produziram. **O sistema de trabalho compete por prioridade com o produto, na mesma fila.** Manter duas filas separadas garante que a segunda nunca seja atendida.

### 🌙 Dream Loop e H6

Owner: trio. O [🌙 Dream Loop](../loops/10-continuous-improvement.md) observa como os outros loops se comportaram na semana — quantas voltas deram, onde escalaram, o que custaram — e separa padrão de ocorrência isolada, com crítica independente obrigatória.

A saída vai a **H6**, que decide se o sistema aprendeu corretamente. É obrigatório para mudança sensível de memória, item P0/P1 e qualquer alteração de gate; o restante segue por amostragem.

A relação entre as duas cadências de aprendizado é de alimentação: o diário registra hipóteses com evidência de sessão; o semanal as confirma ou descarta contra baseline. A comparação completa está no [contrato do ☀️ Daily Loop](../loops/11-daily-operations.md#diário-e-semanal--por-que-são-dois-loops).

---

## Por marco — risco e autonomia

A cadência mais longa não tem periodicidade fixa: ela acontece quando há material suficiente para decidir. Duas revisões acontecem aqui.

**Revisão de nível de autonomia.** Verifica se todos os critérios de subida estão presentes simultaneamente — volume observado, defeitos escapados, rollback confiável, falsos positivos baixos, risco classificado corretamente, evidência auditável e tempo humano de fato reduzido. Um único critério ausente mantém o nível.

**Revisão de classe de risco e de gates.** Verifica se as classes ainda descrevem a realidade do produto e se cada gate ainda paga o próprio custo. Um gate com alto índice de falso positivo não é rigor: é ruído que treina o time a ignorar sinal.

Ambas exigem revisor independente de quem opera o harness, pelo mesmo motivo que aparece em [Papéis](01-papeis.md): relaxar a verificação que avalia o próprio trabalho é o caminho mais curto para a ausência de verificação.

---

## A regra que atravessa os quatro ritmos

**Reunião existe para decidir, não para narrar status.** Preparação, análise, atualização de estado e geração de artefato ficam com agentes e automações; a pessoa entra no momento da decisão.

O teste prático de qualquer ritmo deste modelo: se a cerimônia pode ser substituída por um documento lido de forma assíncrona sem perda, ela deveria ter sido esse documento. Sobram poucas — e são exatamente aquelas em que duas ou três pessoas precisam decidir **juntas**, porque a decisão é compartilhada por construção.

---

*Anterior: [Gatilhos e disparos](03-gatilhos-e-disparos.md) · Próximo: [Manual do operador](05-manual-do-operador.md).*
