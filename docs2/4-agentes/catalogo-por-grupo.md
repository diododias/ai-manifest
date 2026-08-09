---
title: Catálogo de agentes por grupo
status: canonical
updated_at: 2026-08-09
---

# Catálogo de agentes por grupo

> Os 23 papéis organizados por função na jornada, com a saída central de cada um e o que ele deliberadamente não faz.

## Como ler este catálogo

Cada agente aqui é o [contrato comum](contrato-comum.md) mais um conjunto de particularidades: uma missão, um sponsor, uma saída central e um limite explícito. Neste guia educativo, apresentamos os papéis agrupados por função, com foco no que você precisa para escolher e acionar cada um. O que um agente **não** faz é tão vinculante quanto o que ele faz — por isso essa coluna aparece em cada grupo.

## Entrada e coordenação

Estes três agentes ficam nas bordas do fluxo: recebem o que chega de fora e organizam o trabalho dos demais. Nenhum deles decide ou aprova nada — eles preparam e roteiam.

| Agente | Sponsor | Saída central | Não faz |
|---|---|---|---|
| **Intake Agent** | PM | Work Item triado e priorizável | priorizar definitivamente ou prometer solução |
| **Meeting Context Agent** | owner da reunião | resumo e context pack de uma transcrição | atribuir compromisso não falado; publicar sozinho |
| **Orchestrator Agent** | owner da fase | missões roteadas e estado consolidado | aprovar produto, UX, arquitetura, merge ou release |

O Meeting Context Agent carrega a regra mais estrita do catálogo, e vale entender por quê: ele é o único que lida com material bruto de origem humana. Por isso, nada que não foi dito pode aparecer no output — a disciplina protege contra a "decisão" que ninguém tomou virar fato registrado.

## Produto, UX e discovery

Este grupo estrutura o problema antes de qualquer solução. Repare no par produção/crítica: o Product Manager Agent propõe, e o Adversarial PM tenta invalidar — sempre como instância independente.

| Agente | Sponsor | Saída central | Não faz |
|---|---|---|---|
| **Product Manager Agent** | PM | `PB.md` ou `PRD.md` | aprovar o próprio PRD ou escolher arquitetura |
| **UX Specification Agent** | UX | jornada, fluxo e UX spec | definir prioridade ou substituir teste com usuários por heurística |
| **Tech Lead Discovery Agent** | Tech Lead | viabilidade e riscos iniciais | produzir a arquitetura final durante o discovery |
| **Adversarial Product Manager Agent** | PM | crítica de produto classificada | reescrever silenciosamente o PRD ou aprová-lo |

Uma disciplina se destaca aqui: o Tech Lead Discovery Agent **para antes de arquitetar**. Discovery é para avaliar viabilidade e risco, não para desenhar a solução — antecipar isso compromete a fase seguinte.

## Especificação técnica

Aqui o produto aprovado vira estratégia técnica executável. O mesmo padrão de produção e crítica independente se repete.

| Agente | Sponsor | Saída central | Não faz |
|---|---|---|---|
| **Specification Tech Lead Agent** | Tech Lead | `PLAN`, `SPEC`, `ADR`, `TASKS`, `CHECKLIST` | alterar outcome sem devolver a decisão ao owner |
| **Adversarial Tech Lead Agent** | Tech Lead | crítica técnica e trade-offs | bloquear por preferência estética sem evidência |
| **Security / Data / Platform Agent** | Tech Lead | análise especializada | ampliar o parecer para domínios que não avaliou |

O agente especialista tem uma regra de timing importante: é consultado **antes** da crítica adversarial, não depois. Trazer segurança ou dados ao final, quando a especificação já está fechada, transforma achado em retrabalho.

## Construção e validação

O maior grupo, e onde a separação entre produzir e aprovar fica mais visível: quem implementa não é quem valida.

| Agente | Sponsor | Saída central | Não faz |
|---|---|---|---|
| **Software Engineer Agent** | Tech Lead | código, testes e documentação | mudar gates para aprovar o próprio código |
| **QA / Validation Agent** | Tech Lead | matriz critério-evidência | corrigir silenciosamente o código que avalia |
| **Security Review Agent** | Tech Lead | achados de segurança e privacidade | explorar produção ou exfiltrar dados |
| **Architecture Review Agent** | Tech Lead | conformidade arquitetural | introduzir nova arquitetura sem ADR |
| **Adversarial Code Reviewer Agent** | Tech Lead | achados de corretude e manutenção | exigir refatoração fora do escopo sem risco comprovado |

O Software Engineer Agent trabalha sob uma restrição que parece limitante, mas é o que torna a revisão barata: **mudança mínima e comprovável, uma tarefa por vez**. Diffs pequenos são revisáveis; diffs grandes escondem defeitos.

## Integração, homologação e operação

Este grupo leva a mudança validada até a produção e observa sua saúde.

| Agente | Sponsor | Saída central | Não faz |
|---|---|---|---|
| **PR Agent** | Tech Lead | PR e evidence pack | fazer merge sem política ou declarar CI verde sem checar |
| **Product Validation Agent** | PM e UX | aceite de produto e experiência | dar o aceite humano final |
| **Release Agent** | Tech Lead | release rastreável | ampliar exposição além da política |
| **Observability Agent** | Tech Lead | sinais de saúde e alertas | silenciar alerta ou redefinir baseline para mascarar regressão |

O Product Validation Agent ilustra bem a fronteira agente/humano: ele valida, produz evidências e recomenda o aceite — mas o **aceite final é humano**. O agente prepara a decisão; não a toma.

## Conhecimento e melhoria

O grupo que fecha o ciclo sobre o próprio sistema, mantendo a documentação viva e convertendo telemetria em aprendizado.

| Agente | Sponsor | Saída central | Não faz |
|---|---|---|---|
| **Knowledge Agent** | owner do domínio | fontes canônicas atualizadas | converter hipótese em regra |
| **Telemetry Agent** | trio | dataset e relatório do fluxo | concluir causalidade ou priorizar melhoria |
| **Auto Dream Agent** | trio | aprendizados e demandas P0–P3 | aprovar prioridade ou editar memória sensível sozinho |
| **Critic Agent** | owner da decisão | crítica independente | reavaliar com o mesmo raciocínio do autor |

O Critic Agent é o mecanismo que **impede o sistema de concordar consigo mesmo**. Ele tenta refutar conclusões produzidas por outro agente, e sua regra fundamental é a independência real: reavaliar com o mesmo raciocínio e contexto do autor não é crítica, é eco.

## Continue por aqui

Você conhece os papéis. Falta ver como eles se combinam em times temporários a cada fase — a [Composição por fase](composicao-por-fase.md).
