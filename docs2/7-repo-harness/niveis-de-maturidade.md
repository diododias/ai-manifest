---
title: Níveis de maturidade HL0–HL3
status: canonical
updated_at: 2026-08-09
---

# Níveis de maturidade HL0–HL3

> Como medir onde um repositório está, quanto de autonomia cada nível sustenta e por que a progressão segue o retorno decrescente.

## Para que servem os níveis

Os níveis de maturidade descrevem o que existe em um repositório, e servem para responder **uma única pergunta**: até onde a autonomia pode subir com segurança neste repo? Eles não são um selo de qualidade — são uma medida de teto. Um repositório em um dado nível pode operar até um certo nível de autonomia, e não além.

A nomenclatura usa `HL` (harness level) de propósito, para não colidir com os checkpoints humanos `H1–H6` que você viu em [Gates e cerimônias](../2-modelo-operacional/gates-e-cerimonias.md). São coisas diferentes: `H` é um marco de decisão humana; `HL` é um nível de maturidade de repositório.

## Os quatro níveis

Cada nível acrescenta camadas do harness e, com elas, autoriza um teto maior de autonomia. A última coluna — o que ainda depende de gente — é a mais útil no dia a dia: ela diz o que você ainda não pode delegar.

| Nível | O repositório tem | Autonomia sustentada | O que ainda depende de gente |
|---|---|---|---|
| **HL0 — nu** | `README.md`, testes eventuais, CI de build | nenhuma — assistido | tudo; revisão humana é o único gate |
| **HL1 — legível** | `AGENTS.md`, rules mínimas, `verify.sh`, pre-commit | A0–A1 | integração e liberação; revisão ainda ampla |
| **HL2 — verificável** | CI por risco e paths, `CODEOWNERS`, proteção de branch, evidence pack | A2 | merge em R2+; decisões de trade-off |
| **HL3 — operável por time** | skills do repo, worktree limpo, identidades por agente, gates de ambiente e pós-deploy, rollback testado | A3–A4 | exceções, incidentes e auditoria por amostragem |

## A regra que evita o autoengano

Existe uma regra que vale gravar, porque ela contradiz a tentação natural de todo time: **o nível do harness é o teto da autonomia, nunca a consequência dela**.

O que isso quer dizer na prática? Se você encontrar um repositório em HL1 operando com autonomia A2, isso **não** é um repositório adiantado — é um repositório com um gate faltando que ninguém percebeu ainda. A autonomia não pode ultrapassar o que o harness sustenta, por melhor que o histórico pareça, porque falta a estrutura que tornaria esse histórico confiável. E mesmo dentro do teto, elevar autonomia exige a evidência acumulada descrita em [Risco e autonomia](../2-modelo-operacional/risco-e-autonomia.md) — o nível do harness autoriza, mas não basta sozinho.

## Por que a progressão segue o retorno decrescente

A ordem de construção entre níveis não é linear em esforço nem em ganho — e saber disso ajuda a priorizar.

Sair de **HL0 para HL1** é o movimento de maior impacto por esforço: é onde o agente para de reconstruir premissas a cada execução. Se você só puder fazer um movimento, faça este. De **HL1 para HL2** é onde a revisão humana começa a encolher de verdade, e é o que mais exige disciplina — gates mal calibrados geram falso positivo, e um time que aprende a ignorar gates perdeu a proteção que eles davam. De **HL2 para HL3** só compensa quando há mais de um agente em paralelo; antes disso, o custo de isolamento e identidade não se paga.

## O checklist como atestado de capacidade

Cada nível tem um checklist de conformidade — itens verificáveis como "`AGENTS.md` responde identidade, comandos, fronteiras, verificação, escalonamento e ponteiros" ou "worktree limpo roda `scripts/verify.sh` sem configuração manual". Um repositório que falha em qualquer linha do seu nível opera, na prática, no nível anterior.

Mas cuidado com o que o checklist prova. Ele atesta que a **capacidade existe** — não que o histórico já demonstrou que ela funciona. Capacidade é pré-requisito da autonomia; evidência acumulada é o que a autoriza. Os dois são necessários, e o checklist cobre só o primeiro.

## Você chegou ao fim da trilha

Esta é a última seção da wiki. Se você leu na ordem, agora tem o quadro completo: por que o Agent Team existe, quem decide o quê, quais procedimentos e agentes executam o trabalho, como eles colaboram nos workflows, onde tudo roda no workspace e o que um repositório carrega para ser operado com segurança. Para revisar qualquer peça, volte ao [índice da wiki](../README.md).
