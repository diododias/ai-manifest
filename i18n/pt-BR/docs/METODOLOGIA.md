# 5. Metodologia

---

## Overview — How Humans Operate It

As quatro seções anteriores descrevem **o sistema**: o que o repositório precisa carregar para ser operável por agentes, quem são os agentes e sob qual autoridade agem, quais procedimentos eles executam e em que ordem colaboram em cada etapa da jornada. Nenhuma delas responde à pergunta que uma pessoa faz na segunda-feira de manhã: **e eu, o que faço?**

Essa é a lacuna que a metodologia preenche. Ela não introduz nenhum conceito novo, não amplia a autonomia de ninguém e não redefine contrato algum. Ela é a **cola**: mostra como as camadas já documentadas se comportam quando alguém as opera de verdade — o que dispara o quê, quando uma pessoa é chamada, o que ela precisa ver para responder, e o que acontece se ela não responder.

O deslocamento que justifica a seção é conhecido. Quando agentes assumem a produção de código, escrever deixa de ser caro; o que fica caro é decidir o que construir, provar que foi construído certo e impedir que decisões, código e documentação se separem. Um time que não trata esse deslocamento gera volume sem confiança. A resposta do modelo é uma inversão: **o núcleo humano opera o sistema em vez de executar o trabalho.**

### Onde está cada coisa

A regra de leitura da documentação inteira cabe em uma tabela. Confundir estas camadas é o que produz documentação que ninguém consegue executar — e é o que esta seção evita ao linkar em vez de reescrever.

| Camada | Responde | Onde vive |
|---|---|---|
| **Harness** | o que o repositório precisa carregar para sustentar tudo isso | [`REPO_HARNESS.md`](REPO_HARNESS.md) e vizinhos |
| **Skill** | *como* uma tarefa recorrente é executada corretamente | [`SKILLS.md`](SKILLS.md) |
| **Agente** | *quem* executa, sob qual autoridade e com qual limite | [`AGENTES.md`](AGENTES.md), [`agentes/`](agentes/README.md) |
| **Loop** | *em que ordem*, o que atravessa a fronteira e quando parar | [`LOOPS.md`](LOOPS.md), [`loops/`](loops/README.md) |
| **Metodologia** | *quem opera*, o que dispara o quê e o que exige gente | esta seção |

Uma consequência prática: quando um documento desta seção descreve a sequência interna de uma etapa, ele está errado por construção. Sequência é assunto de [`loops/`](loops/README.md). Aqui se documenta o gatilho, o ponto de decisão humana e a responsabilidade — nunca a mecânica.

### Os cinco compromissos

Tudo nesta seção deriva de cinco compromissos. Eles resolvem antecipadamente as disputas mais comuns em um fluxo com agentes, e cada página adiante é o desdobramento operacional de um ou mais deles.

| Compromisso | O que ele impede |
|---|---|
| **Quem propõe não aprova** | que o incentivo de declarar o próprio trabalho pronto se converta em aprovação |
| **Aprovação exige evidência, e silêncio nunca aprova** | que um item avance por cansaço, prazo ou ausência de resposta |
| **Mudança material invalida a aprovação anterior** | que uma decisão tomada sobre um artefato cubra outro |
| **Autonomia sobe por métrica, não por confiança** | que a percepção de que "está funcionando bem" substitua a evidência de que está |
| **Artefato só existe na fonte canônica** | que uma decisão viva em um handoff temporário e se perca na volta seguinte |

### O que uma pessoa faz, afinal

A resposta curta, antes do detalhe: uma pessoa **decide**, **desbloqueia** e **corrige o sistema**. Não acompanha execução, não revisa diff inteiro, não narra status.

| Atividade | Frequência | Onde está documentada |
|---|---|---|
| Responder a um checkpoint de decisão | por entrega, 3 a 6 vezes | [Checkpoints humanos](metodologia/02-checkpoints-humanos.md) |
| Ler o briefing diário e desbloquear | diária, poucos minutos | [Ritmos e cadências](metodologia/04-ritmos-e-cadencias.md) |
| Responder a um escalonamento | por exceção | [Manual do operador](metodologia/05-manual-do-operador.md) |
| Ordenar melhorias do próprio sistema | semanal | [Ritmos e cadências](metodologia/04-ritmos-e-cadencias.md) |
| Ajustar gate, risco ou autonomia | por marco | [Checkpoints humanos](metodologia/02-checkpoints-humanos.md) |

---

## Índice da seção

| Página | Responde |
|---|---|
| [Papéis](metodologia/01-papeis.md) | quem é dono de qual decisão, e como se resolve um empate |
| [Checkpoints humanos](metodologia/02-checkpoints-humanos.md) | onde uma pessoa entra, com qual pergunta e por quanto tempo |
| [Gatilhos e disparos](metodologia/03-gatilhos-e-disparos.md) | o que dispara o quê, quando, e o que nunca dispara sozinho |
| [Ritmos e cadências](metodologia/04-ritmos-e-cadencias.md) | o que acontece todo dia, toda semana e a cada marco |
| [Manual do operador](metodologia/05-manual-do-operador.md) | como operar na prática: despachar, ler saída, intervir |
| [Jornada comentada](metodologia/06-jornada-comentada.md) | o ciclo inteiro visto pelos pontos humanos |
| [Workflows de documentação](metodologia/07-workflows-de-documentacao.md) | como a documentação se mantém viva sozinha |

O índice completo, com trilhas de leitura por perfil, está em [`metodologia/README.md`](metodologia/README.md).

---

*Anterior: [Loops](LOOPS.md) · Detalhe: [as sete páginas da metodologia](metodologia/README.md) · Próximo: [Workspace](WORKSPACE.md) — onde esse trabalho vive fora do código.*
