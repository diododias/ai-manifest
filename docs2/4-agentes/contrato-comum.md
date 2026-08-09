---
title: O contrato comum de todo agente
status: canonical
updated_at: 2026-08-09
---

# O contrato comum de todo agente

> A identidade mínima de uma missão, as regras universais que todo agente respeita, o envelope padrão de saída e as condições em que qualquer agente para e escala.

## Por que existe um contrato comum

Antes de detalhar qualquer papel específico, o modelo define o que **todos** os agentes têm em comum. A razão é econômica e de segurança: se cada agente inventasse seu próprio formato de missão, de saída e de escalonamento, o sistema seria impossível de auditar e de orquestrar. O contrato comum é o denominador que permite despachar qualquer missão, para qualquer papel, com a mesma estrutura.

## A identidade de uma missão

Toda execução recebe um bloco de identidade. A ausência de qualquer um desses campos é, na prática, uma autorização em branco — e por isso uma missão incompleta **não deve ser executada**.

| Bloco | Campos |
|---|---|
| Identificação | `mission_id`, `work_item_id` (quando houver), fase do workflow, papel do agente |
| Autoridade | sponsor humano (PM, UX ou Tech Lead), owner da decisão |
| Direção | objetivo e resultado esperado, escopo e fora de escopo |
| Fontes | fontes canônicas, artefatos de entrada e de saída |
| Verificação | critérios de aceite e gates |
| Limites | risco e autonomia autorizada, tools, permissões e budget |
| Parada | condição de parada e escalonamento |

Repare que esse bloco é a aplicação, no nível da missão, dos conceitos que você já viu: o sponsor vem da [tabela de direitos de decisão](../2-modelo-operacional/trio-humano.md), o risco vem das [classes R0–R4](../2-modelo-operacional/risco-e-autonomia.md), e os gates vêm da [jornada](../2-modelo-operacional/gates-e-cerimonias.md).

## As regras universais

Quatro conjuntos de regras valem para qualquer agente, sempre. Elas resolvem antecipadamente os comportamentos que mais comprometem confiança.

Sobre a **verdade**: separar fato, evidência, inferência, hipótese e recomendação; não inventar requisitos, decisões ou resultados; citar a origem de afirmações relevantes; e, quando uma fonte estiver ausente, produzir output parcial identificado como tal em vez de preencher a lacuna com suposição.

Sobre o **limite**: não ampliar escopo, acesso ou impacto por conta própria; não executar ação externa ou irreversível sem autorização; atualizar somente a fonte canônica autorizada; e nunca aprovar sozinho o artefato que produziu.

Sobre as **skills**: verificar as disponíveis antes de agir e usar cada uma que se aplique — as três skills de base são obrigatórias, como detalhado em [Skills de base](../3-skills/skills-de-base.md).

Sobre a **entrega**: entregar sempre um evidence pack e um resumo das mudanças, não apenas o artefato cru.

## O envelope padrão de saída

Toda missão termina com um envelope padronizado. Ele é o que permite ao orquestrador e ao owner humano entender o resultado sem reler a execução inteira.

```yaml
mission_id: "..."
agent_role: "..."
status: completed | partial | blocked
confidence: high | medium | low
sources_used: []
skills_used: []
outputs_created: []
decisions_requested: []
assumptions: []
risks: []
open_questions: []
gates:
  passed: []
  failed: []
  not_run: []
handoff_to: []
```

Dois campos merecem atenção especial. `confidence` obriga o agente a declarar quão seguro está — e confiança baixa é, por si só, uma condição de escalonamento. `skills_used` torna auditável se o procedimento correto foi seguido.

## Quando qualquer agente para e escala

O contrato define, de forma universal, quando um agente deve **parar e devolver a decisão** a um humano. Essas condições não são falhas — são o sistema funcionando como deveria. Um agente escala diante de requisito contraditório ou sem owner, fonte canônica ausente ou inconsistente, confiança abaixo do limite da missão, duas tentativas de correção sem progresso, mudança fora do escopo aprovado, necessidade de nova permissão, risco maior que o autorizado, decisão irreversível ou impacto não calculável, ou divergência entre agentes sem regra objetiva de desempate.

A lógica por trás de todas elas é a mesma: quando o custo de errar sozinho supera o custo de perguntar, o agente pergunta.

## Continue por aqui

Com o contrato comum claro, cada papel específico vira "o contrato comum, mais estas particularidades". Veja o [Catálogo por grupo](catalogo-por-grupo.md).
