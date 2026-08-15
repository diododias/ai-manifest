# Páginas da metodologia

Este diretório contém as sete páginas da seção. O conceito geral — por que existe uma camada de metodologia acima do harness e quais são os cinco compromissos — está em [Metodologia — How Humans Operate It](../METODOLOGIA.md); aqui ficam os detalhes operacionais.

## A regra que governa todas as páginas

Nenhuma página desta seção descreve a mecânica de uma etapa. Sequência de missões, handoffs entre agentes e gates de saída vivem em [`loops/`](../loops/README.md); autoridade e limite de cada papel vivem em [`agentes/`](../agentes/README.md); ferramentas, sensors e CI vivem no [harness](../REPO_HARNESS.md). O que se documenta aqui é o **gatilho**, o **ponto de decisão humana** e a **responsabilidade** — sempre com link para o contrato correspondente.

O teste prático: se um parágrafo desta seção continuaria correto caso um loop mudasse sua sequência interna, ele está no lugar certo. Se não, ele é duplicata e precisa virar link.

## Como ler

| Página | Responde | Leia se você… |
|---|---|---|
| [01 — Papéis](01-papeis.md) | quem é dono de qual decisão | vai assumir um dos três papéis ou não sabe a quem perguntar |
| [02 — Checkpoints humanos](02-checkpoints-humanos.md) | onde uma pessoa entra e com qual pergunta | vai responder a um H, ou desenhar o evidence pack |
| [03 — Gatilhos e disparos](03-gatilhos-e-disparos.md) | o que dispara o quê e quando | quer entender como o sistema se move sem alguém empurrando |
| [04 — Ritmos e cadências](04-ritmos-e-cadencias.md) | o que acontece todo dia e toda semana | vai operar a rotina, não uma entrega específica |
| [05 — Manual do operador](05-manual-do-operador.md) | como fazer, na prática | está operando pela primeira vez |
| [06 — Jornada comentada](06-jornada-comentada.md) | o ciclo inteiro pelos pontos humanos | quer a visão de conjunto antes do detalhe |
| [07 — Workflows de documentação](07-workflows-de-documentacao.md) | como a documentação se mantém viva | vai escrever, revisar ou auditar documentação |

## Trilhas por perfil

**Operador novo — 20 minutos.** [Papéis](01-papeis.md) → [Jornada comentada](06-jornada-comentada.md) → [Manual do operador](05-manual-do-operador.md). Ao final, você sabe quem decide o quê, onde entra e o que fazer quando algo chega até você.

**Product Manager.** [Papéis](01-papeis.md) → [Checkpoints humanos](02-checkpoints-humanos.md), com atenção a H1, H2 e ao aceite de produto → [Ritmos](04-ritmos-e-cadencias.md), para a triagem semanal e a ordenação das melhorias.

**UX.** [Papéis](01-papeis.md) → [Checkpoints humanos](02-checkpoints-humanos.md), com atenção a H2 e ao aceite de experiência → [Jornada comentada](06-jornada-comentada.md), bloco 1.

**Tech Lead.** [Checkpoints humanos](02-checkpoints-humanos.md), com atenção a H3, H4 e H5 → [Gatilhos e disparos](03-gatilhos-e-disparos.md) → [Manual do operador](05-manual-do-operador.md) → [Workflows de documentação](07-workflows-de-documentacao.md). É o papel que também responde pelo harness, e portanto pelos gatilhos que ele configura.

**Quem vai auditar o modelo.** [Checkpoints humanos](02-checkpoints-humanos.md) → [Gatilhos e disparos](03-gatilhos-e-disparos.md) → [Workflows de documentação](07-workflows-de-documentacao.md). As três páginas juntas respondem se uma decisão qualquer tem owner, evidência e rastro.
