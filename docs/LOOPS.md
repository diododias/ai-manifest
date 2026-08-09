# 4. Loops

---

## Overview — How Loops Work

Um **loop** é o contrato de colaboração de uma etapa da jornada: quem executa, em que ordem, o que atravessa a fronteira entre agentes e qual condição precisa ser verdadeira para avançar. É o que a literatura chama de *workflow multiagente* — e este manifesto chama de loop porque a palavra descreve melhor o que de fato acontece.

Um workflow, no uso comum, sugere uma esteira: entra de um lado, sai do outro. Um loop com agentes não se comporta assim. Ele gira. O agente tenta, o sensor reprova, o agente corrige, o crítico contesta, o consolidador responde, o gate devolve. **A execução bem-sucedida é o caso em que o giro converge rápido, não o caso em que não houve giro.** Um processo desenhado para a esteira trata cada volta como exceção e não instrumenta nenhuma delas; um processo desenhado como loop declara onde a correção acontece e quanto ela custa.

### O que um loop é — e o que ele não é

Três camadas do harness respondem a perguntas diferentes, e confundi-las produz documentação que ninguém consegue executar.

| Camada | Responde | Onde vive |
|---|---|---|
| **Agente** | *quem* executa, sob qual autoridade e com qual limite | [`AGENTES.md`](AGENTES.md), [`agentes/`](agentes/README.md) |
| **Skill** | *como* uma tarefa recorrente é executada corretamente | [`SKILLS.md`](SKILLS.md), `skills/<skill>/SKILL.md` |
| **Loop** | *em que ordem*, o que atravessa a fronteira e quando parar | esta página, [`loops/`](loops/README.md) |

Um loop não redefine o contrato de nenhum agente, não amplia a autonomia de ninguém e não cria gates próprios. Ele compõe peças que já existem. Quando um loop precisa de uma permissão que o agente não tem, o problema está no contrato do agente — não no loop.

### As três voltas

Todo loop contém três circuitos aninhados, com custos de ordem de grandeza diferentes. Reconhecê-los é o que permite decidir onde uma verificação deve morar.

| Volta | Circuito | Frequência típica | Custo | Quem fecha |
|---|---|---|---|---|
| **Interna** | agente ↔ sensors locais | dezenas por missão | segundos | o próprio agente |
| **Média** | consolidação ↔ crítica independente | uma a três por etapa | minutos a horas | o agente consolidador |
| **Externa** | gate ↔ etapa anterior ou owner humano | zero a duas por etapa | horas a dias | o gate de CI ou o owner |

O princípio que decorre disso vale para o desenho de qualquer loop: **uma falha detectável na volta interna que só aparece na volta externa custa três ordens de grandeza a mais e consome julgamento humano que deveria estar em outro lugar.** Todo check tem uma volta natural. Colocá-lo mais para fora do que o necessário é o defeito mais comum — e o mais caro — no desenho de um loop.

Existe ainda uma quarta volta, de período muito mais longo, em que **o sistema de trabalho é o objeto do trabalho**. Ela gira por calendário, e não por Work Item, em duas janelas: o [☀️ Daily Loop](loops/11-daily-operations.md) lê as sessões do dia anterior e converte o que aconteceu em memória, melhoria e sinalização ao owner; o [🌙 Dream Loop](loops/10-continuous-improvement.md) lê o período com telemetria agregada e crítica independente, e realimenta o desenho dos próprios loops.

### Anatomia de um loop

Um loop não carrega conhecimento próprio. Ele coordena camadas versionadas que o [repo harness](REPO_HARNESS.md) disponibiliza — as mesmas que um agente consome, agora vistas na dimensão da etapa.

| Elemento | Define | Se faltar |
|---|---|---|
| **Entrada** | artefatos exigidos e critério para iniciar | o loop começa sobre material incompleto e descobre isso na crítica |
| **Missões** | o que roda em sequência e o que roda em paralelo | trabalho concorrente colide ou serializa sem necessidade |
| **Consolidação** | o único agente responsável pela saída | a saída vira um amontoado de respostas isoladas |
| **Handoffs** | o que atravessa a fronteira entre agentes | o próximo agente reconstrói o contexto por suposição |
| **Gate de saída** | o que precisa ser verdade para avançar | o julgamento de "pronto" fica com quem produziu |
| **Escalonamento** | condição de parada e owner humano da decisão | o agente decide por conta própria o que não lhe cabe |

A ausência de qualquer um desses seis itens torna o loop inexecutável por um agente sem negociação humana prévia. É por isso que eles são obrigatórios em todo arquivo de [`loops/`](loops/README.md).

### O ciclo de iteração — do despacho ao handoff

A pergunta prática é como agentes, skills, tools, MCPs, sensors e gates se encaixam durante uma única volta. A sequência abaixo é a mesma em qualquer loop; o que muda é quem a executa e contra qual gate.

```text
Orchestrator despacha a missão            identidade completa, contexto mínimo, budget
  │
  ├─▶ Agente lê o contexto versionado      AGENTS.md, rules aplicáveis, ADRs, memória
  │
  ├─▶ inventaria skills e aplica as aderentes    skills/<skill>/SKILL.md
  │
  ├─▶ invoca tools e MCPs no escopo autorizado   .agent/settings.json, .agent/mcps.json
  │
  ├─▶ sensors locais avaliam                     .hooks/   ◀── volta interna: corrige e repete
  │
  ├─▶ crítica independente contesta              agente adversarial  ◀── volta média
  │
  ├─▶ gate de CI decide por critério objetivo    fast lane, deep lane
  │
  ├─▶ evidence.sh empacota a prova               docs/evidence/<work-item>/
  │
  ├─▶ envelope de saída volta ao orquestrador    status, confidence, skills_used
  │
  └─▶ handoff atravessa a fronteira              artefato na fonte canônica  ◀── volta externa
```

Cada elo responde por uma classe de falha, e a remoção de qualquer um deles não deixa o loop mais rápido — desloca a falha para uma volta mais cara.

| Elo | Impede que | Se removido, a falha aparece |
|---|---|---|
| Contexto versionado | o agente invente uma convenção plausível | na crítica, como divergência de padrão |
| Skill | o procedimento seja reinventado a cada execução | no handoff, como resultado instável |
| Escopo de tools e MCPs | efeitos externos ocorram antes da verificação | em produção, como incidente |
| Sensors | erro barato viaje até o CI | uma volta inteira depois, no gate de CI |
| Crítica independente | quem produziu declare o próprio trabalho pronto | na homologação ou no cliente |
| Gate | "pronto" seja uma impressão | após o merge, como retrabalho |
| Evidência | a aprovação se baseie no resumo do agente | na auditoria, quando ninguém consegue refazer |
| Envelope | o orquestrador releia a execução inteira | como perda de contexto entre etapas |

### Consolidação e crítica

Dois princípios estruturais atravessam todos os loops.

**Cada loop tem exatamente um agente que consolida.** Contribuições paralelas convergem para um único artefato sob responsabilidade nominal. Uma contribuição não vira decisão pelo fato de estar no consolidado: divergências e riscos residuais permanecem explícitos no artefato final, não são resolvidos por omissão.

**A crítica vem sempre de uma instância independente de quem produziu.** Não é uma formalidade de processo — é a única defesa contra o incentivo estrutural que um agente tem de aprovar o próprio trabalho. Um agente adversarial produz findings rastreáveis com evidência, severidade e ação sugerida; ele não reescreve o artefato criticado.

### Handoff — o que atravessa a fronteira

Um handoff carrega cinco coisas, sempre separadas entre si: **fatos** verificáveis, **evidências** referenciadas, **hipóteses** ainda não confirmadas, **riscos** conhecidos e **perguntas em aberto**. A separação existe porque a fusão dessas categorias é como uma hipótese vira requisito sem que ninguém tenha decidido isso.

Um handoff referencia artefatos versionados em vez de copiar contexto. E um handoff só está concluído quando o artefato final chegou à **fonte canônica** do domínio — `.coordination/` e `memory.md` são trânsito, nunca destino.

### Onde o loop vive e onde a execução acontece

`docs/loops/` é o **catálogo canônico e versionado**. Ele não recebe artefatos de execução — nenhum `PB`, `PRD`, plano, evidência ou handoff de uma rodada concreta é gravado aqui.

Cada owner executa o loop dentro do próprio workspace:

```text
<workspace-do-owner>/
├── docs/loops/          # bindings locais: versão habilitada, permissões, adaptações
├── projects/<project>/  # artefatos persistentes de uma execução
├── .coordination/       # handoffs e bloqueios temporários
├── memory.md            # contexto retomável, nunca fonte canônica
└── repos/               # somente no workspace técnico, quando aplicável
```

Antes de iniciar uma missão, o agente resolve `workspace do owner → projects/<project> → Work Item → fontes canônicas`.

O binding local declara a versão do loop canônico e pode **restringir** tools, permissões e integrações. Ele não pode ampliar autonomia nem alterar gates sem a decisão prevista no modelo operacional. Essa assimetria é intencional: adaptação local deve ser capaz de apertar, nunca de afrouxar.

### Modo dry-run

Um loop pode ser executado sem gerar artefatos persistentes. Ative com `mode: dry-run` no início da missão ou prefixe o comando com `--dry-run`.

O agente executa raciocínio, análises e rascunhos normalmente, e pode imprimir o que *teria* gerado. Não cria nem modifica arquivos em `projects/`, `engineering/` ou `execution/`, e não atualiza `BOARD.md`, `STATUS.md`, Work Items ou handoffs. Serve para explorar um loop desconhecido, testar uma abordagem antes de comprometê-la ou validar o comportamento do agente sem efeito colateral.

---

## Loops disponíveis

Os 12 loops estão documentados individualmente em **[`loops/`](loops/README.md)** — um arquivo por etapa, com contrato operacional, sequência, handoffs, limites explícitos, falhas típicas e destino dos artefatos.

Cada loop tem um codinome. Não é decoração: um nome curto é o que permite dizer "isso é problema do Red Team Loop" sem ambiguidade em uma conversa. Quatro deles — Ralph, Red Team, Canary e Dream — vêm de termos já consagrados na prática de engenharia e de agentes; os demais seguem o mesmo registro.

| # | Loop | Codinome | Consolida | Colaboram ou desafiam |
|---:|---|---|---|---|
| 0 | [Intake e triagem](loops/00-intake-and-triage.md) | 🚦 **Triage Loop** | Intake Agent | Meeting Context; Product Manager |
| 1 | [Discovery e research](loops/01-discovery-and-research.md) | 🔦 **Scout Loop** | Product Manager Agent | UX Specification; Tech Lead Discovery; Adversarial PM |
| 2 | [Produto e UX](loops/02-product-and-ux-planning.md) | 🎨 **Studio Loop** | Product Manager + UX Specification | Adversarial PM; research, conteúdo e prototipação |
| 3 | [Especificação técnica](loops/03-technical-specification.md) | 🗺️ **Drafting Loop** | Specification Tech Lead | Adversarial TL; Security/Data/Platform |
| 4 | [Implementação autônoma](loops/04-autonomous-implementation.md) | 🔁 **Ralph Loop** | Orchestrator Agent | Software Engineer Agents |
| 5 | [Validação adversarial](loops/05-adversarial-validation.md) | ⚔️ **Red Team Loop** | QA / Validation Agent | Security Review; Architecture Review; Adversarial Code Reviewer |
| 6 | [PR e merge](loops/06-pr-and-merge.md) | 🚪 **Gatekeeper Loop** | PR Agent | Reviewer Agents; Code Owners |
| 7 | [Homologação](loops/07-release-candidate-validation.md) | 🎭 **Rehearsal Loop** | Product Validation Agent | Release Agent |
| 8 | [Produção e observação](loops/08-production-release-and-observation.md) | 🐤 **Canary Loop** | Release Agent | Observability Agent |
| 9 | [Curadoria de conhecimento](loops/09-knowledge-curation.md) | 🗄️ **Archivist Loop** | Knowledge Agent | Critic Agent |
| 10 | [Telemetria e melhoria contínua](loops/10-continuous-improvement.md) | 🌙 **Dream Loop** | Auto Dream Agent | Telemetry; Observability; Critic |
| 11 | [Operação diária](loops/11-daily-operations.md) | ☀️ **Daily Loop** | Auto Dream Agent | Telemetry; Knowledge; Orchestrator; Intake |

---

## Versionamento e avaliação

Cada loop registra versão do contrato e data, agentes e gates envolvidos, responsável humano, e changelog com plano de rollback. Alterar a sequência de um loop sem alterar sua versão quebra os bindings locais que declaram compatibilidade.

As métricas por loop cobrem: aprovação na primeira passagem do gate de saída, número de voltas por circuito (interna, média, externa), retrabalho gerado no loop seguinte, taxa de escalonamento e sua causa, tempo de ciclo e custo por rodada, e findings confirmados versus falsos positivos na volta média.

**Essas métricas medem o desenho do loop, não o desempenho dos agentes.** Uma volta externa frequente indica gate mal posicionado ou entrada mal definida — quase nunca indica um agente ruim. Usá-las como avaliação individual corrompe o sinal que produzem.

---

## Checklist para adicionar um novo loop

- [ ] A etapa exige um loop novo ou cabe como variação de um existente?
- [ ] Os seis itens do contrato comum estão explícitos?
- [ ] Existe exatamente um agente consolidador nomeado?
- [ ] A crítica vem de instância independente de quem produz?
- [ ] Cada verificação está na volta mais interna em que é possível executá-la?
- [ ] O gate de saída é verificável sem julgamento humano — e, quando não for, o owner está nomeado?
- [ ] Os handoffs separam fato, evidência, hipótese, risco e pergunta?
- [ ] O destino canônico de cada artefato está declarado?
- [ ] O caminho de falha do gate aponta para um loop específico?
- [ ] O loop funciona em `dry-run` sem efeito colateral?

---

*Anterior: [Agentes](AGENTES.md) · Detalhe: [contratos individuais dos loops](loops/README.md) · Próximo: [Metodologia](METODOLOGIA.md) — como os humanos operam tudo isso.*
