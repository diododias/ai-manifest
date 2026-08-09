---
title: Repositório da aplicação (harness) — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Repositório da aplicação · TLDR

> A pista rápida da seção. Você vai entender o que é o repo harness, as cinco camadas que o compõem, como ele se estrutura em arquivos e os níveis de maturidade que definem o teto da autonomia. Os detalhes ficam nas páginas ao final.

## Um agente competente em um repo sem harness

Coloque um agente excelente em um repositório sem harness e ele produzirá **código plausível e errado**. Ele não sabe qual padrão o time abandonou no ano passado, qual módulo não pode importar qual, quais testes provam o que ele acabou de escrever, nem quando parar e perguntar. Esse conhecimento existe — mas vive na cabeça das pessoas, e a cada execução alguém precisa recitá-lo de novo.

O custo real disso não é o erro isolado. É que a revisão humana volta a ser o único gate de verdade, e a autonomia nunca sobe.

## Converter conhecimento tácito em arquivos e verificações

O repo harness resolve isso convertendo o conhecimento tácito do repositório em **arquivos versionados que o agente lê sozinho e verificações que rodam sem pedir licença**. Ele se organiza em cinco camadas cumulativas, e a ordem importa.

| Camada | Responde | Materializa em |
|---|---|---|
| **Contexto** | o que este repositório é e quais regras valem | `AGENTS.md`, `docs/rules/` |
| **Procedimento** | como executar uma tarefa recorrente do jeito certo | skills, comandos, scripts |
| **Verificação** | o que precisa ser verdade antes de avançar | hooks, CI, políticas de merge |
| **Permissão** | o que este agente pode tocar e o que exige gente | `CODEOWNERS`, settings, ambientes |
| **Evidência** | como provar depois que estava correto | evidence pack, logs, artefatos |

As camadas e a estrutura de arquivos são detalhadas em [As cinco camadas](as-cinco-camadas.md) e [Estrutura de arquivos](estrutura-de-arquivos.md).

## A maturidade é o teto da autonomia

A regra que amarra esta seção ao modelo inteiro: **a maturidade do harness é o teto da autonomia, nunca a consequência dela**. Os níveis HL0 a HL3 medem o que o repositório tem, e cada nível autoriza um teto de autonomia. Um repositório não fica seguro porque você decidiu confiar nele — ele fica seguro porque construiu as camadas que tornam a confiança verificável. Os níveis estão em [Níveis de maturidade](niveis-de-maturidade.md).

## Continue por aqui

Comece por [As cinco camadas](as-cinco-camadas.md) para a lógica. Depois veja a [Estrutura de arquivos](estrutura-de-arquivos.md) para montar um repo, e feche com os [Níveis de maturidade](niveis-de-maturidade.md).
