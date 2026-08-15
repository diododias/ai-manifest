# 01 — Papéis

> Quem é dono de qual decisão, quem precisa ser consultado, e o que se faz quando dois donos discordam.

Um modelo com agentes multiplica a quantidade de decisões tomadas por unidade de tempo. Se a titularidade dessas decisões não for explícita, o efeito não é paralisia — é algo pior: **decisões passam a ser tomadas por omissão**, dentro de artefatos, por quem estava ali no momento. Esta página existe para que nenhuma decisão fique parada esperando consenso e nenhuma seja tomada sem responsável nominal.

A distinção de partida é entre executar e dirigir. O trio humano não tenta fazer manualmente o trabalho dos agentes; ele opera o sistema que o faz.

---

## Os quatro atores

| Ator | Dirige | Não responde por |
|---|---|---|
| **Product Manager** | valor, prioridade e resultado de negócio | arquitetura, desenho da experiência |
| **UX** | entendimento do usuário, experiência e qualidade de uso | prioridade de negócio, escolha de arquitetura |
| **Tech Lead** | viabilidade, arquitetura, qualidade técnica e risco operacional | valor de negócio, decisão de experiência |
| **Agentes** | pesquisa, proposta, implementação, crítica, validação e documentação | qualquer decisão de valor, escopo ou exceção |
| **Automações** | verificações determinísticas, bloqueios e rastreabilidade | julgamento sobre o que fazer com uma falha |

As três primeiras linhas descrevem pessoas; as duas últimas, capacidade. A separação importa porque **agentes e automações não têm titularidade** — eles preparam, executam e comprovam. Quando um agente parece ter decidido algo relevante, ou a decisão era de fato mecânica, ou o contrato dele está mal desenhado.

### Product Manager — dono do valor e da prioridade

Responde por "vale a pena construir isto, agora, para este resultado?". Mantém objetivos e roadmap, ordena o backlog por valor, urgência, risco e aprendizado, e **formula o problema antes de comprometer uma solução**. Na operação diária, decide avançar, ajustar, adiar ou encerrar um item, homologa valor com stakeholders e ordena as melhorias que a telemetria produz.

Opera os agentes de intake, discovery, planejamento e validação de produto — [📥 Intake](../agentes/intake-agent.md), [📋 Product Manager](../agentes/product-manager-agent.md), [🥊 Adversarial PM](../agentes/adversarial-product-manager-agent.md) e [✅ Product Validation](../agentes/product-validation-agent.md).

**O que não é exclusividade do PM:** desenhar sozinho a experiência, definir solução técnica, aprovar exceção técnica sem o Tech Lead, ou substituir evidência de usuário por opinião de stakeholder.

### UX — dono da experiência e da evidência sobre o usuário

Responde por "isto resolve o problema de quem vai usar, e resolve bem?". Planeja pesquisa proporcional ao risco, mapeia jornadas e pontos de fricção, e especifica os estados nominal, vazio, carregando, erro, permissão e recuperação — o conjunto que costuma ser esquecido e reaparece como retrabalho três etapas depois.

Opera a [🧭 UX Specification](../agentes/ux-specification-agent.md) e participa da crítica de produto.

**O que não é exclusividade do UX:** definir prioridade de negócio, escolher arquitetura, ou aprovar escopo sozinho.

### Tech Lead — dono da integridade técnica e do risco operacional

Responde por "isto é viável, sustentável e seguro de operar?". Define arquitetura, contratos e fronteiras, estabelece padrões de qualidade e observabilidade, e classifica risco. Também **mantém o harness** — as rules, skills, sensors e gates que tornam o repositório compreensível e seguro para agentes. É a única titularidade que recai sobre o próprio sistema de trabalho, e não sobre o produto.

Opera os agentes de especificação, implementação, revisão, segurança e operação — de [📐 Specification Tech Lead](../agentes/specification-tech-lead-agent.md) a [🚀 Release](../agentes/release-agent.md).

**O que não é exclusividade do Tech Lead:** definir valor de negócio, decidir experiência, ou absorver sozinho decisão de escopo.

### Responsabilidade compartilhada

Os três respondem conjuntamente pela qualidade do problema antes da solução, pela coerência entre valor, experiência e viabilidade, por riscos explícitos e decisões rastreáveis, pela proteção dos dados e dos usuários, e pelo aprendizado após a entrega. Compartilhado aqui significa que **nenhum dos três pode aprovar sozinho** — não que a responsabilidade se dilua.

---

## Direitos de decisão

Referência para resolver "quem decide isto?". A coluna de evidência mínima é a parte operacional da tabela: uma decisão tomada sem ela é reversível por qualquer consultado.

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
| Merge e release | Tech Lead, por política | PM + UX conforme risco | CI, evidence pack, plano de rollout e rollback |
| Exposição de risco R3/R4 | PM + Tech Lead | UX quando houver impacto ao usuário | impacto, mitigação, observabilidade e rollback |
| Prioridade de melhoria do sistema | owner do domínio; PM ordena o backlog | trio | telemetria, frequência, impacto e esforço |
| Mudança de gate | Tech Lead + revisor independente | PM e UX se afetados | falsos positivos, risco coberto e plano de adoção |

Duas leituras dessa tabela merecem destaque. **Mudança de gate exige revisor independente** — é a única linha em que o owner não decide sozinho dentro do próprio domínio, porque relaxar a verificação que avalia o próprio trabalho é o caminho mais curto para a ausência de verificação. E **exposição de risco alto tem dois owners**, deliberadamente: nem o produto nem a técnica podem expor o usuário sozinhos.

---

## Regra de desempate

Quando a discussão trava, o domínio decide.

| Assunto em disputa | Decide | Registro obrigatório |
|---|---|---|
| Valor, prioridade e outcome | PM | alternativa descartada e razão |
| Experiência, usabilidade e acessibilidade | UX | evidência de usuário considerada |
| Arquitetura, segurança e confiabilidade | Tech Lead | trade-off aceito e ADR quando estrutural |

Os três conflitos recorrentes seguem essa regra sem exceção:

- **Escopo contra prazo** é do PM, que decide o que sai — não o que é feito pela metade.
- **Experiência contra viabilidade** é resolvido pela adaptação consciente: o Tech Lead informa a restrição, o UX redesenha preservando o outcome, e o PM decide se o outcome reduzido ainda vale.
- **Risco contra velocidade** é do Tech Lead quando o risco é técnico, e escala ao sponsor quando é irreversível, regulatório ou de grande alcance. **Risco dessa natureza não se resolve dentro do trio.**

O que não vale em nenhum dos casos: decidir por consenso silencioso. Um empate registrado como "seguimos assim" sem owner nominal reaparece como retrabalho na primeira contestação.

---

## Contratos de passagem

Cada seta entre papéis é um contrato, não uma conversa. O emissor entrega insumos definidos; o receptor devolve um resultado definido.

| De | Para | Entrega | Espera de volta |
|---|---|---|---|
| PM | UX | problema, segmento, outcome, restrições e perguntas | evidência do usuário, jornada, fluxo e critérios de experiência |
| PM | Tech Lead | problema, escopo candidato, métricas e restrições | viabilidade, riscos, dependências e opções técnicas |
| UX | PM | evidências, necessidades, hipóteses e riscos de experiência | decisão de escopo e atualização do PRD |
| UX | Tech Lead | fluxo, estados, conteúdo, acessibilidade e protótipo | contratos e estratégia de implementação compatíveis |
| Tech Lead | PM | custo, riscos, dependências, alternativas e impacto operacional | decisão de investimento, corte ou sequenciamento |
| Tech Lead | UX | restrições de plataforma, latência, dados e componentes existentes | adaptação consciente da experiência sem perder o outcome |
| Trio | agentes | artefato aprovado, critérios, gates, risco e permissões | mudança executada, validada, documentada e evidenciada |
| Agentes | trio | evidence pack, divergências e decisões pendentes | aprovação, correção, adiamento ou escalonamento |

### Definition of Ready para execução agentica

Um item só entra em execução por agentes quando **problema e usuário estão explícitos, outcome e métrica definidos, owner humano conhecido, escopo e fora de escopo claros**, fluxo e estados de UX suficientes para a tarefa, contratos e restrições técnicas suficientes, critérios de aceite verificáveis, classe de risco e gates definidos, acessos autorizados e dúvidas críticas resolvidas ou assumidas de forma explícita.

Despachar sem isso não acelera a entrega: transfere a ambiguidade para dentro da execução, onde ela custa uma volta externa para ser descoberta.

### Definition of Done do ciclo

O ciclo fecha quando critérios de produto, UX e engenharia estão cobertos; testes e gates obrigatórios aprovados; impacto arquitetural avaliado; riscos e limitações conhecidos; documentação e fontes canônicas atualizadas; aprovações identificadas; backlog, commits, PR, release e telemetria vinculados; rollout observado sem regressão relevante ou com plano de correção; e aprendizados encaminhados ao loop correto.

---

## Agentes e seus patrocinadores

Todo agente tem um humano que responde pelo que ele produz. A tabela serve para a pergunta inversa da mais comum: não "o que este agente faz", que está em [`agentes/`](../agentes/README.md), mas **"quando isto der errado, quem é chamado?"**.

| Humano | Patrocina | Loops correspondentes |
|---|---|---|
| **PM** | Intake, Product Manager, Adversarial PM, Meeting Context, Product Validation | [🚦 Triage](../loops/00-intake-and-triage.md), [🔦 Scout](../loops/01-discovery-and-research.md), [🎨 Studio](../loops/02-product-and-ux-planning.md), [🎭 Rehearsal](../loops/07-release-candidate-validation.md) |
| **UX** | UX Specification | [🔦 Scout](../loops/01-discovery-and-research.md), [🎨 Studio](../loops/02-product-and-ux-planning.md) |
| **Tech Lead** | Tech Lead Discovery, Specification TL, Adversarial TL, Orchestrator, Software Engineer, QA, Security Review, Architecture Review, Adversarial Code Reviewer, PR, Release, Observability | [🗺️ Drafting](../loops/03-technical-specification.md) a [🐤 Canary](../loops/08-production-release-and-observation.md) |
| **Trio** | Knowledge, Telemetry, Auto Dream, Critic | [🗄️ Archivist](../loops/09-knowledge-curation.md), [🌙 Dream](../loops/10-continuous-improvement.md), [☀️ Daily](../loops/11-daily-operations.md) |

---

## O antipadrão

**Decisão sem responsável nominal.** O sintoma é reconhecível: existe um artefato aprovado que ninguém consegue explicar — a razão de uma escolha não está no ADR, não está no PRD e não está na cabeça de nenhuma das três pessoas. Isso quase sempre nasce de um consenso implícito em uma etapa anterior, onde o owner correto não foi chamado.

A correção não é retroativa. Uma decisão sem dono é reaberta com o owner correto, e o custo dessa reabertura é a métrica que mostra se a matriz de direitos de decisão está sendo usada.

---

*Anterior: [Índice da metodologia](README.md) · Próximo: [Checkpoints humanos](02-checkpoints-humanos.md).*
