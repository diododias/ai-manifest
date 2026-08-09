---
title: O contrato de um workflow
status: canonical
updated_at: 2026-08-09
---

# O contrato de um workflow

> As seis coisas que todo workflow explicita, as convenções de execução que valem para todos e o modo dry-run para experimentar sem gerar artefatos.

## O que um workflow adiciona ao catálogo

Vale reforçar a fronteira antes de entrar no detalhe. Os workflows **não substituem** nada do que você já viu: não substituem os contratos individuais do [catálogo de agentes](../4-agentes/catalogo-por-grupo.md), nem a autoridade do [modelo operacional](../2-modelo-operacional/TLDR.md), nem os gates da jornada. O que eles adicionam é a **coreografia**: a ordem das missões, o que atravessa cada fronteira e como as contribuições convergem.

## As seis cláusulas do contrato

Todo workflow explicita seis coisas. Pense nelas como as perguntas que precisam estar respondidas para que um agente execute a etapa sem ter que negociar com um humano no meio do caminho.

| Item | Define |
|---|---|
| Entrada | artefatos de entrada e critérios para iniciar |
| Missões | dependências e o que pode rodar em paralelo |
| Consolidação | o único agente responsável pela saída |
| Handoffs | fatos, evidências, hipóteses, riscos e perguntas em aberto |
| Saída | gate de saída e destino em caso de falha |
| Escalonamento | condição de parada e owner humano da decisão |

Duas cláusulas costumam ser subestimadas. **Consolidação** exige um único agente responsável pela saída — não um comitê — para que sempre exista alguém que responde pelo artefato final. E **saída** precisa declarar o destino *em caso de falha*, não só de sucesso: um workflow que só sabe o que fazer quando tudo dá certo trava no primeiro imprevisto.

## As convenções que valem para todo workflow

Além das seis cláusulas, três convenções de execução se aplicam a todos os workflows e merecem ser compreendidas de uma vez.

A convenção de **formato** determina que toda missão usa o envelope de saída padrão (o mesmo que você viu no [contrato comum dos agentes](../4-agentes/contrato-comum.md)) e que um handoff **referencia** artefatos versionados em vez de copiar o contexto inteiro. Copiar contexto gera divergência silenciosa quando o original muda; referenciar mantém uma única fonte de verdade.

A convenção de **convergência** estabelece que uma contribuição não vira decisão só por estar no consolidado. Divergências e riscos residuais permanecem explícitos, e o workflow termina com um artefato coerente e um evidence pack — nunca com respostas isoladas dos agentes empilhadas.

A convenção de **revisão** determina que nova informação material devolve o workflow ao agente responsável pela revisão e invalida a aprovação relacionada quando a política assim determinar. É a aplicação, no fluxo, da regra de que silêncio não aprova e que uma mudança relevante reabre a decisão.

## O modo dry-run: experimentar sem consequências

Há uma capacidade que ajuda muito no aprendizado: workflows podem rodar em **modo dry-run**, um modo de experimentação que não gera artefatos persistentes. Nele, o agente executa todo o raciocínio, análises e rascunhos normalmente, mas não cria nem modifica arquivos em `projects/` ou em qualquer pasta de artefatos, e não atualiza board, status ou handoffs. Ele pode imprimir na conversa o que *teria* gerado.

O dry-run é ideal para três situações: explorar um workflow que você não conhece, testar uma abordagem antes de comprometê-la, ou validar o comportamento de um agente sem efeitos colaterais. Para ativar, passa-se `mode: dry-run` no início da missão ou prefixa-se o comando com `--dry-run`.

## Continue por aqui

Com o contrato claro, veja como ele se aplica às onze etapas concretas em [A jornada completa](a-jornada-completa.md).
