# 07 — Workflows de documentação

> Como a documentação se mantém viva: quem produz cada artefato, o que dispara uma atualização e o que impede que ela seja esquecida.

[Documentation](../DOCUMENTATION.md) descreve **onde** a documentação vive dentro do repositório — rules, ADRs, evidence pack, estrutura de arquivos. Esta página descreve **como ela se mantém correta ao longo do tempo**, que é um problema diferente e mais difícil.

O antipadrão que ela combate tem nome: **documentação atualizada por lembrança**. Ela funciona por algumas semanas, degrada em silêncio e é descoberta no pior momento possível — quando um agente lê uma rule desatualizada, segue-a corretamente e produz algo errado. Num fluxo com agentes, documentação obsoleta não é dívida cosmética: é instrução ativa e equivocada.

A resposta do modelo é a mesma que ele dá em todo lugar: **transformar lembrança em gatilho.** Cada artefato tem um evento observável que exige sua atualização, e a verificação disso mora no gate, não na memória de quem revisa.

---

## Quem produz o quê

Todo artefato documental tem exatamente um consolidador e um destino canônico — o mesmo princípio dos loops, aplicado à documentação.

| Artefato | Nasce em | Consolida | Owner humano | Fonte canônica |
|---|---|---|---|---|
| Work Item | [🚦 Triage](../loops/00-intake-and-triage.md) | Intake Agent | PM | `projects/<project>/work-items/` |
| `PB.md` | [🔦 Scout](../loops/01-discovery-and-research.md) | Product Manager Agent | PM | workspace de produto |
| `PRD.md` | [🎨 Studio](../loops/02-product-and-ux-planning.md) | Product Manager + UX Specification | PM, com UX | workspace de produto |
| `SPEC`, `PLAN`, `TASKS` | [🗺️ Drafting](../loops/03-technical-specification.md) | Specification Tech Lead | Tech Lead | workspace técnico |
| ADR | [🗺️ Drafting](../loops/03-technical-specification.md) | Specification Tech Lead | Tech Lead | `docs/adr/` no repositório |
| `docs/rules/*.md` | qualquer loop que adote uma convenção | o agente que a introduziu | Tech Lead | repositório |
| `AGENTS.md` | [🔁 Ralph](../loops/04-autonomous-implementation.md) | Software Engineer Agent | Tech Lead | repositório |
| `skills/<skill>/SKILL.md` | [🗄️ Archivist](../loops/09-knowledge-curation.md) | Knowledge Agent | owner do domínio | repositório |
| Evidence pack | [⚔️ Red Team](../loops/05-adversarial-validation.md) e [🚪 Gatekeeper](../loops/06-pr-and-merge.md) | gerado por `scripts/evidence.sh` | Tech Lead | `docs/evidence/<work-item>/` |
| `MEMORY.md` | [☀️ Daily](../loops/11-daily-operations.md) e [🌙 Dream](../loops/10-continuous-improvement.md) | Knowledge Agent | trio | workspace correspondente |

Duas linhas merecem comentário. O **evidence pack é gerado por script**, nunca montado à mão ao final da tarefa — evidência manual é seletiva por natureza, e a seleção é feita justamente por quem tem interesse no resultado. E o **`MEMORY.md` tem dois produtores com janelas diferentes**: o diário propõe com evidência de sessão, o semanal valida contra baseline.

---

## O que dispara uma atualização

Cada gatilho abaixo é um evento observável, não uma boa intenção. É a diferença entre "lembrar de atualizar a documentação" e "a documentação ser atualizada".

| Gatilho | Atualiza | Quem |
|---|---|---|
| Decisão de arquitetura tomada ou revertida | **novo** ADR, nunca edição do anterior | Specification Tech Lead |
| Convenção nova adotada de fato no código | a rule correspondente em `docs/rules/` | o agente que a introduziu, via `update-docs` |
| Procedimento repetido pela terceira vez | nova skill em `skills/` | Knowledge Agent |
| Comando de build, teste ou execução alterado | `AGENTS.md` | Software Engineer Agent, no mesmo PR |
| Contrato público ou schema alterado | rule, ADR e documentação de contrato | Specification Tech Lead |
| Incidente com causa raiz identificada | rule, ADR ou skill, conforme a natureza | owner do domínio |
| Aprendizado validado no ☀️ ou 🌙 | `MEMORY.md` | Knowledge Agent |
| Exceção arquitetural aberta | ADR com prazo e plano de reversão | Tech Lead |
| Gate, sensor ou nível de autonomia alterado | a documentação do harness e o registro da mudança | Tech Lead + revisor independente |

### A regra do ADR

ADR registra **a decisão tomada**, não a regra vigente. A rule em `architecture.md` diz *"módulos de domínio não importam de infraestrutura"*; o ADR correspondente diz por que essa decisão foi tomada, o que foi considerado e o que ela custa.

A consequência prática é a linha mais importante da tabela acima: **reverter uma decisão cria um ADR novo que supersede o anterior — nunca edita o antigo.** Um agente que lê apenas rules sabe o que fazer; um agente que também lê ADRs sabe por quê, e decide corretamente no caso de borda que a rule não previu. Apagar o histórico destrói exatamente essa capacidade.

### A trava

**Um PR que altera comportamento sem atualizar o artefato correspondente é reprovado no gate — não no review humano.**

Deixar isso para o julgamento de quem revisa transfere para uma pessoa um trabalho que uma máquina faz melhor, e o resultado é conhecido: a verificação acontece nas primeiras semanas e desaparece depois. O detalhe de como o gate implementa isso está em [Gates](../GATES.md).

---

## Estados e ciclo de vida

Todo documento canônico carrega um estado, e o estado tem significado operacional para o agente que o lê.

| Estado | Significa | O agente pode |
|---|---|---|
| `proposed` | escrito, ainda não aceito como referência | ler como contexto, nunca como regra |
| `canonical` | é a referência vigente para o tema | seguir sem confirmação |
| `superseded` | substituído por outro documento | ler para entender o histórico; nunca seguir |
| `archived` | não se aplica mais e não foi substituído | ignorar, salvo investigação histórica |

Um documento `superseded` **nunca é apagado**: ele aponta para quem o substituiu. É o que permite reconstruir por que algo é como é — a mesma razão que sustenta a regra do ADR.

O front matter mínimo é `title`, `status` e `updated_at`; documentos com titularidade não óbvia acrescentam `owner`. A ausência de `status` faz o agente tratar o documento como `proposed`, que é o comportamento seguro.

---

## O padrão de escrita

As regras abaixo existem para que o documento sirva a dois leitores no mesmo arquivo: quem chega sem contexto e tem poucos minutos, e quem já decidiu que vale e precisa do detalhe operacional.

| Regra | Aplicação |
|---|---|
| **Nenhuma seção começa com lista** | listas descrevem itens; prosa e tabelas descrevem relações |
| **Prosa antes de estrutura** | cada bloco abre explicando por que existe e como se liga ao anterior |
| **Consequência explícita** | todo bloco com decisão fecha com o que acontece se a regra não for seguida |
| **Um conceito, um lugar** | conteúdo que já existe em outra camada é linkado, nunca reescrito |
| **Duas camadas acima de 150 linhas** | abertura curta em prosa, depois o corpo navegável |
| **Front matter obrigatório** | `title`, `status`, `updated_at` |

**Exceção explícita:** documentos curtos de contrato — os arquivos de [`loops/`](../loops/README.md) e de [`agentes/`](../agentes/README.md) — dispensam a camada rápida. Eles já cabem em uma tela, abrem com um parágrafo de propósito seguido da tabela de contrato, e a regra prática é direta: se o documento inteiro é lido em menos tempo do que o resumo economizaria, não há resumo a escrever.

---

## Como auditar

Três perguntas respondem se a documentação está viva. Elas podem ser feitas a qualquer momento, sobre qualquer repositório.

1. **Existe alguma rule que o código já não segue?** Se sim, ou a rule morreu e ninguém a marcou como `superseded`, ou o código divergiu e nenhum gate percebeu. As duas causas são defeitos.
2. **Existe alguma decisão relevante sem ADR?** O sintoma é reconhecível: uma escolha estrutural que ninguém consegue explicar. Ver o antipadrão em [Papéis](01-papeis.md).
3. **O último evidence pack permite refazer a verificação sem perguntar nada?** Se não, o que existe é um resumo, e as aprovações recentes se basearam na impressão que ele causou.

---

*Anterior: [Jornada comentada](06-jornada-comentada.md) · Volta ao [índice da metodologia](README.md).*
