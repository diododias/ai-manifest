---
title: As cinco camadas do repo harness
status: canonical
updated_at: 2026-08-09
---

# As cinco camadas do repo harness

> O que cada camada elimina, por que a ordem de construção importa e qual é o erro de sequenciamento mais comum.

## O manual de bordo do repositório

Uma boa metáfora para o repo harness é o **manual de bordo**: tudo que uma pessoa nova precisaria saber para trabalhar no repositório sem atrapalhar ninguém, só que escrito para ser lido e seguido por um agente. Ele mora dentro do repositório de código, viaja com o clone, e existe para responder quatro perguntas antes que o agente precise agir — o que é este repositório, como se faz as coisas aqui, o que preciso provar antes de dizer que terminei, e o que não posso tocar sem autorização.

Vale saber também o que o harness **não** é. Ele não é a esteira de CI — a esteira é apenas uma implementação de uma das cinco camadas. Ele não é a documentação de arquitetura em si — ele aponta para ela. E ele não é sobre como o trabalho é organizado fora do código — isso é o [workspace](../6-workspace/harness-do-workspace.md).

## Cada camada elimina uma classe de falha

O harness tem cinco camadas, e cada uma existe para eliminar um tipo específico de falha. A melhor forma de entendê-las é olhar o sintoma que aparece quando a camada está ausente — é assim que você reconhece, num repositório real, qual camada está faltando.

| Camada | Elimina | Sintoma quando falta |
|---|---|---|
| **Contexto** | agente reconstruindo premissas a cada execução | soluções fora do padrão do repo; mesma correção pedida em PRs diferentes |
| **Procedimento** | variação entre execuções da mesma tarefa | dois agentes resolvem a mesma tarefa de formas incompatíveis |
| **Verificação** | confiança substituindo prova | aprovação baseada em "o agente parece confiável"; defeito em produção |
| **Permissão** | mudança fora do escopo autorizado | agente altera migração ou secret sem que ninguém tenha decidido |
| **Evidência** | conclusão sem rastro auditável | ninguém reconstrói por que a mudança foi aprovada |

## A ordem de construção segue o retorno decrescente

As camadas são cumulativas, e a ordem de construção não é estética — é econômica. Você constrói na sequência contexto → procedimento → verificação → permissão → evidência, e há uma razão para cada posição.

**Contexto é o mais barato de escrever e o que mais reduz retrabalho imediato.** Um `AGENTS.md` e algumas rules custam pouco e já fazem o agente parar de reconstruir premissas. **Verificação é cara de configurar, mas é a única camada que permite reduzir a revisão humana** — sem gates, a pessoa continua sendo o único filtro. **Evidência só tem valor quando existe algo verificado para registrar** — construída antes das outras, ela produz arquivos que ninguém lê.

## O erro de sequenciamento mais comum

Vale um alerta explícito, porque quase todo time novo comete o mesmo erro: **pular contexto para ir direto aos gates**. Parece produtivo, porque gates dão sinal imediato — o agente tenta, falha, ajusta, tenta de novo. Mas cada volta custa tempo de CI e tokens, e nenhuma delas ensina o padrão para a próxima execução.

O resultado é um agente que trata o pipeline como oráculo: nunca aprende por que algo está errado, só descobre *que* está. Verificação sem contexto produz um agente que falha rápido sem saber por quê; contexto sem verificação produz um agente que acerta às vezes e ninguém sabe quando. As duas camadas se sustentam mutuamente, e contexto vem primeiro.

## As duas camadas que só existem por causa dos agentes

Duas das cinco camadas — permissão e evidência — merecem uma observação final. Elas existem precisamente porque quem opera o repositório **não é uma pessoa**. Um humano diante de uma migração de banco hesita naturalmente; um agente, não — então a hesitação precisa estar escrita, na forma de permissão. E a aprovação humana precisa ser sobre fatos verificáveis, não sobre a impressão que o resumo do agente causou — daí a evidência.

## Continue por aqui

Você entende a lógica das camadas. Para vê-las materializadas em arquivos concretos, vá para [Estrutura de arquivos](estrutura-de-arquivos.md).
