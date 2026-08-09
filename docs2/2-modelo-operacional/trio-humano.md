---
title: O trio humano e os direitos de decisão
status: canonical
updated_at: 2026-08-09
---

# O trio humano e os direitos de decisão

> Como três papéis — PM, UX e Tech Lead — dividem a autoridade sem sobreposição, e como a tabela de direitos de decisão resolve os casos de fronteira.

## Por que exatamente três donos

A escolha de ter três papéis não é arbitrária. Todo produto de software vive de responder bem a três perguntas independentes: **vale a pena construir isto?**, **isto resolve bem o problema de quem usa?** e **isto é viável e seguro de operar?**. Quando uma única pessoa responde às três, ela inevitavelmente favorece a que domina e negligencia as outras. Quando ninguém é claramente dono de uma delas, a pergunta fica sem resposta até virar problema.

O trio dá a cada pergunta um dono inequívoco. E o mais importante: nenhum dos três é um "tradutor" passivo dos outros. Eles constroem **juntos** o contrato que os agentes vão executar.

## O que cada papel dirige

Cada papel traz decisões próprias para a mesa e responde por uma pergunta central.

O **Product Manager** responde por "vale a pena construir isto, agora, para este resultado?". Mantém visão, objetivos e roadmap, ordena o backlog por valor, urgência, risco e aprendizado, e formula o problema antes de comprometer uma solução. Decide avançar, ajustar, adiar ou encerrar um item, e homologa valor com stakeholders.

O **UX** responde por "isto resolve o problema de quem vai usar, e resolve bem?". Planeja pesquisa proporcional ao risco, mapeia jornadas e fluxos, e especifica os estados que costumam ser esquecidos — nominal, vazio, loading, erro, permissão e recuperação — justamente o conjunto que vira retrabalho quando ninguém cuida dele. Garante acessibilidade, consistência e usabilidade.

O **Tech Lead** responde por "isto é viável, sustentável e seguro de operar?". Avalia alternativas, define arquitetura, contratos e fronteiras, estabelece padrões de qualidade e testes, e classifica risco. Também mantém o repo harness — o conjunto de rules, skills, hooks e gates que torna o repositório compreensível e seguro para agentes.

| Papel | Dirige | Decide sozinho |
|---|---|---|
| **Product Manager** | valor, prioridade, requisitos e outcome | prioridade, escopo e aceite de produto |
| **UX** | evidência sobre o usuário, jornada e qualidade de uso | experiência, acessibilidade e aceite de UX |
| **Tech Lead** | viabilidade, arquitetura, qualidade técnica e risco | arquitetura, exceção técnica, merge e release |

## O que cada papel deliberadamente não faz

Tão importante quanto saber o que um papel decide é saber o que ele **não** decide sozinho — é aí que a separação protege o time. O PM não desenha a experiência nem escolhe a arquitetura, e não substitui evidência de usuário por opinião de stakeholder. O UX não define prioridade de negócio nem aprova escopo sozinho. O Tech Lead não define valor de negócio nem decide a experiência do usuário. Cada limite empurra a decisão para quem tem o contexto certo.

## A tabela de direitos de decisão

Esta é a referência que você consulta quando surge a pergunta "quem decide isto?". Ela existe para que nenhuma decisão fique parada aguardando consenso, e para que nenhuma seja tomada sem a evidência que a sustenta. Cada linha nomeia o owner, quem deve ser consultado e a evidência mínima que a decisão exige.

| Decisão | Owner | Consultados | Evidência mínima |
|---|---|---|---|
| Prioridade e investimento | PM | UX + Tech Lead | valor, urgência, risco e custo de oportunidade |
| Problema e outcome | PM | UX + Tech Lead | evidência do problema e métrica de resultado |
| Jornada e experiência | UX | PM + Tech Lead | pesquisa, fluxo, protótipo e critérios de UX |
| Escopo da entrega | PM | UX + Tech Lead | outcome, capacidade, dependências e riscos |
| Arquitetura e implementação | Tech Lead | PM + UX | alternativas, trade-offs, risco e validação |
| Exceção arquitetural | Tech Lead | owner afetado | ADR, prazo, consequência e plano de reversão |
| Aceite de produto | PM | UX + stakeholder | critérios de produto e evidências de homologação |
| Aceite de experiência | UX | PM + Tech Lead | critérios de UX, acessibilidade e validação |
| Merge e release | Tech Lead por política | PM + UX conforme risco | CI, evidence pack, rollout e rollback |
| Exposição de risco R3/R4 | PM + Tech Lead | UX quando houver impacto ao usuário | impacto, mitigação, observabilidade e rollback |

## Quando a discussão trava: a regra de desempate

Nenhum time escapa de impasses, então o modelo define de antemão como sair deles. A regra é: **o domínio decide**. Valor, prioridade e outcome ficam com o PM; experiência, usabilidade e acessibilidade com o UX; arquitetura, segurança e confiabilidade com o Tech Lead. Conflitos entre domínios exigem registrar alternativas, impacto e decisão conjunta — nunca resolver no boca a boca. E há um limite: risco irreversível, regulatório ou de grande alcance **escala ao sponsor ou responsável formal**; não se resolve dentro do trio.

## Como isso se conecta aos agentes

Entender os papéis humanos é o pré-requisito para entender os agentes. Cada agente tem um **sponsor humano** — um dos três — que responde por seu resultado. O agente prepara e recomenda; o sponsor decide. Quando você chegar em [Agentes](../4-agentes/TLDR.md), verá que a coluna "sponsor" de cada contrato é simplesmente a aplicação da tabela acima ao nível de cada missão.

Para ver como essas decisões se distribuem ao longo da jornada, siga para [Gates e cerimônias](gates-e-cerimonias.md).
