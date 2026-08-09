---
title: Modelo operacional — pista rápida
status: canonical
updated_at: 2026-08-09
---

# Modelo operacional · TLDR

> A pista rápida da seção. Você vai entender quem decide o quê, como a jornada é dividida em gates com owner e como a autonomia do sistema cresce sem virar aposta. Os detalhes ficam nas páginas ao final.

## O que o modelo operacional resolve

Delegar trabalho a agentes é fácil; delegar **sem perder controle** é o problema. O modelo operacional é o conjunto de regras que responde a uma pergunta recorrente — "quem decide isto, com base em qual evidência?" — antes que ela trave o fluxo. Ele existe para que nenhuma decisão fique parada esperando consenso e nenhuma seja tomada sem a prova que a sustenta.

## As três engrenagens

O modelo se apoia em três engrenagens que trabalham juntas. A primeira é **quem decide**: cada domínio tem um dono humano inequívoco, e uma tabela de direitos de decisão resolve os casos de fronteira. A segunda é **como o trabalho anda**: a jornada é uma sequência de gates com owner e critério de passagem, marcada por cerimônias de decisão (H1 a H6) onde a pessoa entra para decidir, não para ouvir relato. A terceira é **quanto o sistema pode fazer sozinho**: uma escala de risco (R0 a R4) define quanta verificação cada mudança exige, e uma escala de autonomia (A0 a A4) define quanto o fluxo roda sem intervenção.

| Engrenagem | Pergunta que responde | Você aprende em |
|---|---|---|
| **Trio humano** | quem é dono de cada decisão | [Trio humano](trio-humano.md) |
| **Gates e cerimônias** | como o trabalho avança e onde a pessoa decide | [Gates e cerimônias](gates-e-cerimonias.md) |
| **Risco e autonomia** | quanto verificar e quanto delegar | [Risco e autonomia](risco-e-autonomia.md) |

## A regra que protege o modelo

Acima de qualquer tabela, vale uma trava de segurança: **nenhuma métrica isolada eleva a autonomia**. Subir o quanto o sistema roda sozinho exige, ao mesmo tempo, histórico suficiente, baixa taxa de falha, gates confiáveis, poucos falsos positivos, rollback testado e telemetria íntegra. É essa exigência combinada que impede o modelo de confundir sorte com maturidade.

## Continue por aqui

Comece por [Trio humano](trio-humano.md) para entender os papéis e os direitos de decisão. Depois veja [Gates e cerimônias](gates-e-cerimonias.md) para o ciclo de ponta a ponta, e feche com [Risco e autonomia](risco-e-autonomia.md).
