---
title: Repo harness — repositório de código
status: proposed
updated_at: 2026-08-09
---

# Repo harness

> O conjunto de arquivos, verificações e permissões que torna um **repositório de código (GitHub)** seguro de operar por agentes. Este documento é específico do repositório — não confundir com a coordenação entre múltiplos agentes, tratada separadamente na [seção 8, Harness do Agent Team](#8-harness-do-agent-team).

## Em 2 minutos

Um agente competente em um repositório sem harness produz código plausível e errado. Ele não sabe qual padrão o time abandonou no ano passado, qual módulo não pode importar qual, quais testes provam o que ele acabou de escrever, nem quando parar e perguntar. Esse conhecimento existe — mas vive na cabeça das pessoas, e a cada execução o agente precisa que alguém o recite de novo. O custo disso não é o erro isolado: é que a revisão humana volta a ser o único gate real, e a autonomia nunca sobe.

O harness resolve isso convertendo o conhecimento tácito do repositório em **arquivos versionados que o agente lê sozinho e verificações que rodam sem pedir licença**. É um artefato do repositório de código, não do workspace do agente — a organização do trabalho em disco é responsabilidade do [workspace do Tech Lead](diagrams/tech-lead-workspace.md); o harness é o que cada repositório carrega dentro de si e viaja junto com o clone.

| Camada | Responde | Materializa em |
|---|---|---|
| **Contexto** | o que este repositório é e quais regras valem | `AGENTS.md`, `docs/rules/` |
| **Procedimento** | como executar uma tarefa recorrente do jeito certo | `skills/`, comandos, scripts |
| **Verificação** | o que precisa ser verdade antes de avançar | hooks, CI, políticas de merge |
| **Permissão** | o que este agente pode tocar e o que exige gente | `CODEOWNERS`, settings, ambientes |
| **Evidência** | como provar depois que estava correto | evidence pack, logs, artefatos |

As camadas são cumulativas e a ordem importa. Verificação sem contexto produz agente que falha rápido sem saber por quê; contexto sem verificação produz agente que acerta às vezes e ninguém sabe quando. A maturidade do harness é o que autoriza subir a autonomia — nunca o contrário.

---

## Mapa do documento

| Seção | Responde | Leia se você… |
|---|---|---|
| [1. O que é](#1-o-que-é) | O que o harness cobre e o que fica de fora | está começando a ler o documento |
| [2. As cinco camadas](#2-as-cinco-camadas) | O que cada camada garante e o que a quebra custa | vai avaliar um harness existente |
| [3. Estrutura de arquivos](#3-estrutura-de-arquivos-do-repositório) | Onde cada peça fica no repositório | vai montar ou auditar um repo |
| [4. Contexto](#4-camada-de-contexto) | O que escrever em `AGENTS.md` e nas rules | vai escrever o contexto do repo |
| [5. Procedimento](#5-camada-de-procedimento) | Quando algo vira skill em vez de rule | vai criar uma skill ou script |
| [6. Verificação](#6-camada-de-verificação) | Onde cada check pertence na escada | vai configurar hooks e CI |
| [7. Permissão e evidência](#7-camadas-de-permissão-e-evidência) | Quem pode o quê e como se prova | vai definir política de merge e deploy |
| [8. Harness do Agent Team](#8-harness-do-agent-team) | O que quebra quando são vários agentes — distinto do repo harness | vai rodar agentes em paralelo |
| [9. Níveis HL0–HL3](#9-níveis-de-maturidade-hl0hl3) | Onde seu repo está e o que falta | vai propor elevar autonomia |
| [10. Stack de referência](#10-stack-de-referência) | Uma implementação concreta possível | quer um ponto de partida executável |
| [11. Checklist](#11-checklist-de-conformidade) | Como validar antes de operar | vai declarar um repo pronto |

**Vizinhos:** [sistema operacional do trio humano](operating-model.md) · [modelo operacional 90/10](operating-model-90-10.md) · [workspace do Tech Lead](diagrams/tech-lead-workspace.md) · [catálogo de skills](../skills/README.md) · [workflows multiagente](workflows/README.md).

---

## 1. O que é

Pense no harness como o manual de bordo do repositório: tudo que uma pessoa nova precisaria saber para trabalhar ali sem atrapalhar ninguém, só que escrito para ser lido e seguido por um agente. Ele mora dentro do repositório de código, viaja com o clone, e existe para responder quatro perguntas antes que o agente precise agir: o que é este repositório, como se faz as coisas aqui, o que preciso provar antes de dizer que terminei, e o que eu não posso tocar sem autorização.

A ideia central é simples: hoje, esse conhecimento existe, mas vive na cabeça de quem já trabalha no repositório. O harness pega esse conhecimento e coloca em arquivos versionados dentro do próprio repositório, para que o agente leia sozinho em vez de precisar perguntar.

Um jeito útil de entender os limites do harness é olhar para o que ele não é:

**Não é a esteira de CI.** A esteira é uma implementação possível da camada de verificação (seção 6), mas verificação é só uma das cinco camadas. Um repositório pode ter CI robusto e ainda assim não ter harness — se não existe `AGENTS.md` nem rules, o agente até é barrado quando erra, mas nunca aprende por quê, e volta a errar do mesmo jeito na próxima tarefa.

**Não é a documentação de arquitetura em si.** O harness aponta para essa documentação (rules, ADRs) — ele é o contrato que organiza onde cada coisa mora e garante que o agente saiba onde procurar, não o conteúdo técnico em si.

**Não é sobre como o trabalho é organizado fora do código** — quais projetos existem, quem está fazendo o quê esta semana, em qual branch. Isso é papel do workspace de quem coordena os agentes, descrito em [workspace do Tech Lead](diagrams/tech-lead-workspace.md), que também traz uma tabela com exemplos lado a lado de onde cada tipo de informação mora.

O restante deste documento detalha como construir esse manual de bordo, camada por camada.

---

## 2. As cinco camadas

Cada camada existe para eliminar uma classe específica de falha. A tabela abaixo mostra como: liga cada camada à falha que ela previne e ao sintoma que aparece quando ela está ausente — útil como referência para reconhecer, num repositório real, qual camada está faltando.

| Camada | Elimina | Sintoma quando falta |
|---|---|---|
| **Contexto** | agente reconstruindo premissas a cada execução | soluções plausíveis fora do padrão do repo; mesma correção pedida em PRs diferentes |
| **Procedimento** | variação entre execuções da mesma tarefa | dois agentes resolvem o mesmo tipo de tarefa de formas incompatíveis |
| **Verificação** | confiança substituindo prova | aprovação baseada em "o agente parece confiável"; defeito descoberto em produção |
| **Permissão** | mudança fora do escopo autorizado | agente altera migração, secret ou gate sem que ninguém tenha decidido isso |
| **Evidência** | conclusão sem rastro auditável | ninguém consegue reconstruir por que aquela mudança foi aprovada |

A ordem de construção segue a mesma sequência, e a razão é econômica. Contexto é o mais barato de escrever e o que mais reduz retrabalho imediato. Verificação é cara de configurar mas é a única camada que permite reduzir revisão humana. Evidência só tem valor quando existe algo verificado para registrar — construída antes, produz arquivos que ninguém lê.

Pular contexto para ir direto a gates é o erro de sequenciamento mais comum. Ele parece produtivo porque gates dão sinal imediato, mas produz um agente que passa a tratar o pipeline como oráculo: tenta, falha, ajusta, tenta de novo. Cada volta custa tempo de CI e tokens, e nenhuma delas ensina o padrão para a próxima execução.

---

## 3. Estrutura de arquivos do repositório

A estrutura abaixo é o alvo completo — um repositório em [HL3](#9-níveis-de-maturidade-hl0hl3). Repositórios em níveis anteriores contêm um subconjunto, e a seção de maturidade indica qual.

```text
<repositório>/
├── AGENTS.md                      # contrato de entrada do agente
├── README.md                      # uso humano: rodar, buildar, contribuir
├── CODEOWNERS                     # propriedade por path
│
├── docs/
│   ├── rules/
│   │   ├── architecture.md        # módulos, fronteiras, dependências permitidas
│   │   ├── coding.md              # convenções, padrões aceitos e proibidos
│   │   ├── testing.md             # níveis obrigatórios por tipo de mudança
│   │   ├── security.md            # dados, secrets, autenticação, privacidade
│   │   └── operations.md          # SLOs, observabilidade, rollout, rollback
│   ├── adr/
│   │   └── ADR-NNN-<slug>.md      # decisões e consequências
│   └── evidence/
│       └── <work-item>/           # evidence pack por unidade de trabalho
│
├── skills/
│   └── <skill>/SKILL.md           # procedimentos executáveis do repo
│
├── .agent/
│   ├── settings.json              # tools permitidas, limites, modelos
│   └── permissions.md             # o que exige humano neste repositório
│
├── scripts/
│   ├── verify.sh                  # entrada única das verificações locais
│   └── evidence.sh                # coleta e empacota evidência
│
├── .hooks/                        # pre-commit e pre-push versionados
└── .ci/                           # fast lane e deep lane
```

Três decisões nessa árvore merecem justificativa, porque a alternativa aparente é sempre mais simples e sempre pior no médio prazo.

**Rules em arquivos separados, não em um `AGENTS.md` gigante.** O `AGENTS.md` é lido inteiro em toda execução; as rules são lidas sob demanda. Fundir os dois faz cada tarefa trivial pagar o custo de contexto da regra de migração de banco. A separação é uma decisão de orçamento de contexto, não de organização estética.

**`scripts/verify.sh` como entrada única.** Hooks, CI e agente chamam o mesmo script. Sem isso, a verificação local e a de CI divergem, e a divergência aparece na forma mais cara possível — o agente entrega, o CI reprova, e ninguém consegue reproduzir localmente.

**`docs/evidence/` dentro do repositório.** A evidência acompanha o código que ela comprova. Guardada fora, ela sobrevive à mudança de ferramenta de CI mas perde a ligação com o commit; guardada dentro, a ligação é o próprio histórico do Git.

| Arquivo | Carrega | Não carrega |
|---|---|---|
| `AGENTS.md` | como operar o repo, comandos, quando parar | arquitetura detalhada, histórico de decisões |
| `docs/rules/*.md` | a regra e o motivo dela | instruções de execução passo a passo |
| `docs/adr/` | por que a decisão foi tomada e o que ela custa | a regra vigente resultante |
| `skills/<skill>/SKILL.md` | passo a passo verificável de uma tarefa recorrente | conhecimento geral sobre o domínio |
| `.agent/permissions.md` | o que exige autorização humana | política de risco global do time |
| `CODEOWNERS` | quem aprova mudança em cada path | por que aquele path é sensível |

---

## 4. Camada de contexto

### 4.1 `AGENTS.md` — o contrato de entrada

O `AGENTS.md` é lido antes de qualquer ação, o que torna cada linha dele um custo fixo por execução. Isso impõe uma disciplina que o `README.md` não tem: ele responde o que o agente precisa para **agir corretamente na primeira tentativa**, e delega o resto por ponteiro.

| Bloco | Conteúdo | Erro comum |
|---|---|---|
| Identidade | o que o serviço faz e para quem, em três frases | reescrever o pitch do produto |
| Comandos | instalar, buildar, testar, verificar, rodar local | listar comandos que ninguém usa mais |
| Fronteiras | o que não pode ser alterado sem autorização | descrever a arquitetura inteira |
| Verificação | o que precisa passar antes de considerar pronto | duplicar a configuração de CI |
| Escalonamento | as condições em que se para e devolve a decisão | omitir — é o bloco mais esquecido |
| Ponteiros | onde ficam rules, ADRs, skills e evidências | inlinar o conteúdo apontado |

O bloco de escalonamento é o que mais falta e o que mais importa. Sem ele, um agente diante de requisito contraditório escolhe uma interpretação e segue — e a escolha só aparece na revisão, quando o trabalho já foi feito. O [contrato de escalonamento](operating-model-90-10.md#62-contrato-de-escalonamento) do modelo operacional define as condições genéricas; o `AGENTS.md` acrescenta as específicas do repositório.

### 4.2 Rules — a regra e o motivo

Rules descrevem estado desejado, não procedimento. "Módulos de domínio não importam de infraestrutura" é rule; "para adicionar um adapter, crie a interface em X e a implementação em Y" é skill. A confusão entre os dois produz rules longas que ninguém lê e skills vagas que não se consegue executar.

Toda rule carrega o motivo junto. Isso não é cortesia editorial: um agente que conhece a razão de uma regra decide corretamente no caso de borda que a regra não previu, enquanto um agente que só conhece a regra ou a aplica cegamente ou a ignora.

As rules cobrem quatro frentes, e a divisão existe para que cada uma possa ser carregada isoladamente conforme a tarefa:

| Frente | Define | Arquivo |
|---|---|---|
| Estrutura de código | arquitetura e fronteiras entre módulos, convenções e nomes, padrões aceitos e proibidos, injeção de dependência e composição | `architecture.md`, `coding.md` |
| Fluxo | gitflow e estratégia de branches, critérios de validação e homologação, propriedade por paths | `coding.md`, `CODEOWNERS` |
| Risco e dados | classificação de risco e permissões por fase, segurança, privacidade e uso de dados | `security.md` |
| Operação | SLOs, observabilidade, rollout e rollback | `operations.md` |
| Estratégia de testes | quais níveis são obrigatórios por tipo de mudança | `testing.md` |

A estratégia de testes merece destaque porque é a rule que os gates traduzem diretamente em bloqueio:

```text
unitários → arquitetura → integração / TAAC → contrato → end-to-end → acessibilidade → mutação
```

A rule define quais níveis são **obrigatórios por tipo de mudança**. Sem esse mapeamento, o agente ou escreve testes de menos, e o gate reprova tarde, ou escreve testes de mais, e o custo por entrega sobe sem ganho de segurança.

---

## 5. Camada de procedimento

Uma tarefa vira skill quando três condições se acumulam: ela se repete, ela tem um jeito certo de ser feita, e errá-la custa caro o suficiente para justificar escrever o procedimento. Tarefa que se repete mas tolera variação não precisa de skill — precisa de rule. Tarefa cara mas única não precisa de skill — precisa de um humano.

O catálogo global em [`skills/`](../skills/README.md) cobre os procedimentos que valem para qualquer repositório: discovery, especificação, implementação, revisão, publicação e operação de workspace. O repositório acrescenta apenas o que é dele — o procedimento de migração daquele banco, o fluxo de rollout daquele serviço, a forma de gerar aquele client.

| Origem | Contém | Exemplo |
|---|---|---|
| Catálogo global | procedimento válido em qualquer repo | `code-review`, `commit`, `create-spec` |
| Skill do repositório | procedimento específico daquele código | migração de schema, geração de SDK, rollout do serviço |

Toda skill declara objetivo, inputs, outputs, tools permitidas, critérios de parada, exemplos e testes. O critério de parada é o campo que separa uma skill de um tutorial: sem ele, o agente não sabe se terminou, e a resposta padrão de um agente que não sabe se terminou é continuar.

Scripts são o degrau abaixo da skill. Quando o procedimento é determinístico o bastante para virar código, ele deve virar código — um script é mais barato de executar, mais fácil de testar e impossível de interpretar errado. A skill existe para o que exige julgamento; o script, para o que não exige.

---

## 6. Camada de verificação

A escada de gates completa — local, CI, merge, ambiente, pós-deploy — está definida em [`operating-model-90-10.md`](operating-model-90-10.md#6-arquitetura-de-gates) e não se repete aqui. O que o harness acrescenta é a decisão de **onde cada check pertence**, que é onde a maioria das configurações erra.

O critério é a razão entre custo de execução e frequência de falha. Um check barato que falha com frequência pertence ao degrau mais baixo possível; um check caro que quase nunca falha pertence ao mais alto. Colocar um check caro cedo trava o agente em cada commit; colocar um check barato tarde desperdiça uma volta inteira de CI para informar algo que se saberia em dois segundos.

| Se o check… | …ele pertence a | Porque |
|---|---|---|
| roda em segundos e falha com frequência | pre-commit | corrigir custa quase nada e o loop é imediato |
| precisa de container ou serviço externo | pre-push ou CI | inviável a cada commit |
| depende de ambiente limpo ou build completo | CI | resultado local não é confiável |
| exige julgamento sobre risco ou trade-off | merge | é decisão, não verificação |
| só é observável com tráfego real | pós-deploy | não existe forma de antecipar |

Duas travas se aplicam especificamente a repositórios operados por agentes. A primeira: **o resultado de um gate é input do agente, não apenas do humano** — uma falha de CI precisa produzir mensagem acionável o suficiente para o agente corrigir sozinho, o que na prática significa apontar arquivo, regra violada e correção esperada. Gate que só diz "falhou" transfere para a revisão humana o trabalho que ele existia para evitar.

A segunda: **mudança em rules, hooks ou CI eleva o risco automaticamente**, e nenhum agente altera gates dentro do mesmo fluxo que aqueles gates avaliam. Sem essa separação, o caminho de menor resistência para um agente bloqueado passa a ser afrouxar o bloqueio.

---

## 7. Camadas de permissão e evidência

Permissão e evidência são as duas camadas que só existem porque quem opera o repositório não é uma pessoa. Um humano diante de uma migração de banco hesita; um agente, não — a hesitação precisa estar escrita.

A permissão se expressa em três níveis que se sobrepõem, do mais granular ao mais amplo. `CODEOWNERS` define quem aprova mudança em cada path, e é a trava mais eficaz porque age no ponto exato do risco. As configurações do agente definem quais tools ele pode invocar e com que limites. As proteções de branch e ambiente definem o que exige autorização independentemente de quem pediu.

| Categoria de path | Tratamento típico |
|---|---|
| migrações, schema, dados persistidos | owner obrigatório; nunca auto-merge |
| autenticação, autorização, secrets | owner de segurança; risco elevado automaticamente |
| contratos públicos e integrações externas | owner técnico; verificação de compatibilidade |
| rules, hooks, CI, `AGENTS.md` | owner do harness; separado do fluxo avaliado |
| código de aplicação coberto por testes | fluxo normal conforme classe de risco |

A evidência fecha o ciclo. Ela existe para que a aprovação seja sobre fatos verificáveis, e não sobre a impressão que o resumo do agente causou. O evidence pack de uma unidade de trabalho registra o que foi feito, o que foi verificado, o que falhou e foi corrigido, e o que permanece em aberto — com ponteiros para os artefatos originais em vez de reproduzi-los.

Um jeito simples de testar se um evidence pack está bom: **outra pessoa consegue refazer a verificação sem perguntar nada a quem o produziu?** Se precisa de contexto adicional, o que existe ainda é um resumo, não evidência.

---

## 8. Harness do Agent Team

> Esta seção é conceitualmente distinta do restante do documento. As seções 1–7 e 9–11 descrevem o **repo harness**: o que um repositório de código carrega dentro de si, independente de quem o opera. Esta seção descreve o **harness do agent team**: as garantias adicionais que passam a valer quando *vários agentes* operam sobre o mesmo repositório ao mesmo tempo. O repo harness é pré-requisito do harness do agent team, não o contrário — um time de agentes não compensa a ausência de contexto, verificação, permissão e evidência no repositório; ele só adiciona coordenação em cima do que já existe.

Um harness dimensionado para um agente por vez falha de formas específicas quando vários agentes operam em paralelo, e as falhas não são de qualidade — são de coordenação. Cada uma tem uma contramedida no harness do agent team.

| Falha | O que acontece | Contramedida no harness |
|---|---|---|
| Sobrescrita silenciosa | dois agentes editam o mesmo arquivo; o último vence | worktree por Work Item; nunca clone compartilhado |
| Auto-aprovação | o agente que produziu também revisa | identidade distinta por agente; owner ≠ autor |
| Divergência de contexto | agentes leem versões diferentes da mesma rule | rules versionadas com o código; sem contexto injetado fora do repo |
| Contenção em arquivo comum | vários agentes atualizam o mesmo board ou log | um arquivo por unidade de trabalho; consolidação por um coordenador |
| Deriva de gate | um agente afrouxa a verificação que o bloqueia | mudança em gate sai do fluxo avaliado e exige owner |
| Perda de rastro | não se sabe qual agente produziu o quê | autoria, modelo e versão registrados em cada commit e evidência |

### 8.1 Isolamento de execução

O isolamento é a contramedida de maior impacto e a mais barata de adotar. Cada missão trabalha em um worktree próprio, derivado do clone canônico, com branch dedicada ao Work Item — o padrão de diretórios está definido no [workspace do Tech Lead](diagrams/tech-lead-workspace.md#worktrees-para-agentes-concorrentes).

O que o harness precisa garantir do seu lado é que **o repositório funcione a partir de um worktree limpo sem configuração manual**. Repositório que depende de um `.env` montado à mão, de um cache local aquecido ou de um passo não documentado quebra o isolamento na prática, mesmo que a estrutura de diretórios esteja correta. O teste é direto: um worktree recém-criado roda `scripts/verify.sh` com sucesso sem intervenção.

### 8.2 Separação entre produzir e aprovar

Nenhum agente aprova a própria mudança. Isso exige que agentes tenham **identidades distintas e verificáveis** no sistema de versionamento — não basta um prompt instruindo o agente revisor a ser rigoroso, porque a proteção precisa ser estrutural, aplicada pela política de merge e não pela boa-fé do modelo.

A separação vale também entre papéis: o agente que implementa não é o que revisa, e o que revisa não é o que decide o merge em mudanças de risco elevado. A [validação adversarial](workflows/05-adversarial-validation.md) é o workflow que materializa isso.

### 8.3 Orçamento de contexto por agente

Com um agente, contexto excedente custa tokens. Com um time, custa consistência: agentes com janelas diferentes de contexto tomam decisões diferentes sobre o mesmo repositório, e a divergência aparece como inconsistência arquitetural que ninguém autorizou.

A contramedida é estrutural — `AGENTS.md` enxuto, rules carregadas sob demanda por área, skills que declaram exatamente o que precisam ler. Um harness que exige ler tudo para fazer qualquer coisa não escala para time.

---

## 9. Níveis de maturidade HL0–HL3

Os níveis descrevem o que existe no repositório, e servem para responder uma pergunta só: **até onde a autonomia pode subir com segurança neste repo**. A nomenclatura `HL` evita colisão com os checkpoints humanos `H1–H6` do [modelo 90/10](operating-model-90-10.md#2-review-de-decisão).

| Nível | O repositório tem | Autonomia sustentada | O que ainda depende de gente |
|---|---|---|---|
| **HL0 — nu** | `README.md`, testes eventuais, CI de build | nenhuma — assistido | tudo; revisão humana é o único gate |
| **HL1 — legível** | `AGENTS.md`, rules mínimas, `scripts/verify.sh`, pre-commit | [A0–A1](operating-model-90-10.md#7-autonomia-progressiva) | integração e liberação; revisão de conteúdo ainda ampla |
| **HL2 — verificável** | CI por risco e paths, `CODEOWNERS`, proteção de branch, evidence pack | A2 | merge em R2+; decisões de trade-off |
| **HL3 — operável por time** | skills do repo, worktree limpo, identidades por agente, gates de ambiente e pós-deploy, rollback testado | A3–A4 | exceções, incidentes e auditoria por amostragem |

A progressão segue uma regra prática, e vale ter ela em mente ao ler a tabela: **o nível do harness é teto da autonomia, nunca consequência dela**. Se você encontrar um repositório em HL1 operando com autonomia A2, isso não é um repositório adiantado — é um repositório com um gate faltando que ninguém percebeu ainda. O [critério para elevar autonomia](operating-model-90-10.md#7-autonomia-progressiva) exige evidência acumulada além do nível do harness.

A ordem de construção entre níveis segue o retorno decrescente. Sair de HL0 para HL1 é o movimento de maior impacto por esforço — é onde o agente para de reconstruir premissas. De HL1 para HL2 é onde a revisão humana começa a encolher de fato, e é o movimento que mais exige disciplina, porque gates mal calibrados geram falso positivo e o time aprende a ignorá-los. De HL2 para HL3 só compensa quando há mais de um agente em paralelo; antes disso, o custo de isolamento e identidade não se paga.

---

## 10. Stack de referência

As opções abaixo são **uma** implementação possível, não uma decisão de adoção. O contrato do harness não deve depender de marca — o que a tabela oferece é um ponto de partida concreto para quem está montando o primeiro repositório e não quer decidir dez ferramentas antes de começar. A avaliação de qualquer alternativa passa pelo [contrato de avaliação de ferramenta](operating-model.md#126-contrato-de-avaliação-de-uma-ferramenta).

| Camada | Implementação de referência | Papel |
|---|---|---|
| Contexto | `AGENTS.md` + Markdown em `docs/rules/` | lido pelo agente e pela pessoa, versionado com o código |
| Procedimento | skills em Markdown + scripts POSIX | procedimento com julgamento e procedimento determinístico |
| Verificação local | pre-commit framework chamando `scripts/verify.sh` | mesmo comando local e em CI |
| Verificação em CI | GitHub Actions com fast lane e deep lane | seleção de checks por risco e paths |
| Segurança | CodeQL, secret scanning, dependency review | achados com regra reproduzível |
| Permissão | `CODEOWNERS`, branch protection, environments | trava estrutural, não instrução em prompt |
| Evidência | artefatos de workflow + `docs/evidence/<work-item>/` | rastro auditável ligado ao commit |
| Isolamento | `git worktree` por Work Item | execução paralela sem contenção |
| Observabilidade | OpenTelemetry + backend do time | sinal de pós-deploy que sustenta A3 |

Duas escolhas dessa lista costumam ser questionadas, e ambas têm resposta curta. **Markdown em vez de formato estruturado** para rules e skills: o consumidor primário é um modelo de linguagem, e prosa com estrutura leve é lida melhor que YAML aninhado — estrutura rígida só compensa quando há automação lendo o mesmo arquivo. **Duas lanes de CI em vez de uma**: a fast lane existe para devolver sinal ao agente em minutos; uma esteira única e completa transforma cada tentativa em uma espera longa, e o agente ocioso custa tanto quanto o agente errado.

O que falta hoje neste repositório é o esqueleto executável correspondente — um template copiável com `AGENTS.md`, rules mínimas, hooks e workflows prontos. Ele está registrado como pendência em [`operating-model-90-10.md §9.1`](operating-model-90-10.md#91-próximo-detalhamento-recomendado).

---

## 11. Checklist de conformidade

Antes de declarar um repositório pronto para ser operado por agentes, confirme o nível pretendido item a item. Um repositório que falha em qualquer linha do seu nível opera no nível anterior, independentemente do que o restante tenha.

**HL1 — legível**

- [ ] `AGENTS.md` responde identidade, comandos, fronteiras, verificação, escalonamento e ponteiros
- [ ] Rules cobrem arquitetura, código, testes e segurança, cada uma com o motivo declarado
- [ ] `scripts/verify.sh` roda a verificação completa e é o mesmo comando usado por hooks e CI
- [ ] Pre-commit bloqueia lint, formatação, typecheck e testes unitários afetados
- [ ] Falha de verificação produz mensagem com arquivo, regra violada e correção esperada

**HL2 — verificável**

- [ ] CI seleciona checks por classe de risco e paths alterados
- [ ] `CODEOWNERS` cobre migrações, segurança, contratos públicos e o próprio harness
- [ ] Proteção de branch impede bypass silencioso e force push, e invalida aprovação após mudança material
- [ ] Evidence pack é gerado automaticamente e permite refazer a verificação sem contexto adicional
- [ ] Mudança em rules, hooks ou CI eleva risco e exige owner do harness

**HL3 — operável por time**

- [ ] Worktree limpo roda `scripts/verify.sh` sem configuração manual
- [ ] Cada agente tem identidade distinta e verificável; autor nunca aprova
- [ ] Skills específicas do repositório existem para os procedimentos caros e recorrentes
- [ ] Gates de ambiente e pós-deploy estão configurados, com rollback testado em produção
- [ ] Autoria, modelo e versão ficam registrados em commits e evidências

O checklist não substitui o [critério de elevação de autonomia](operating-model-90-10.md#7-autonomia-progressiva): ele atesta que a capacidade existe, e não que o histórico já demonstrou que ela funciona.
