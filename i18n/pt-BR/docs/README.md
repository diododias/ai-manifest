# Agent-Team — Documentação

> Os pilares de um time agêntico, do mais baixo para o mais alto, como uma pirâmide: **harness → skills → agentes → loops → metodologia → workspace**. Cada camada responde a uma pergunta distinta e se apoia na anterior; pular uma camada é o que produz documentação que ninguém consegue executar.

## A pirâmide

| # | Camada | Responde | Onde vive |
|---|---|---|---|
| 1 | **Harness** | o que o repositório precisa carregar para ser operável por agentes | [`REPO_HARNESS.md`](REPO_HARNESS.md) e vizinhos |
| 2 | **Skills** | *como* uma tarefa recorrente é executada corretamente | [`SKILLS.md`](SKILLS.md) |
| 3 | **Agentes** | *quem* executa, sob qual autoridade e com qual limite | [`AGENTES.md`](AGENTES.md), [`agentes/`](agentes/README.md) |
| 4 | **Loops** | *em que ordem* os agentes colaboram e quando parar | [`LOOPS.md`](LOOPS.md), [`loops/`](loops/README.md) |
| 5 | **Metodologia** | *quem opera*, o que dispara o quê e o que exige gente | [`METODOLOGIA.md`](METODOLOGIA.md), [`metodologia/`](metodologia/README.md) |
| 6 | **Workspace** | *onde* cada artefato de uma execução vive, fora do código | [`WORKSPACE.md`](WORKSPACE.md), [`workspace/`](workspace/README.md) |

A base sustenta o topo, não o contrário: uma skill (2) só é verificável se o harness (1) existir; um agente (3) só é confiável quando executa as skills que já existem sobre esse harness; um loop (4) só coordena agentes e skills que já existem; a metodologia (5) não introduz conceito novo, apenas explica como uma pessoa opera as quatro camadas de baixo; e o workspace (6) é o lugar físico onde tudo isso deixa rastro fora do código.

---

## 1. Harness do repositório da aplicação

O **repo harness** converte o conhecimento tácito do repositório em arquivos versionados que o agente lê sozinho e em verificações que rodam sem pedir licença. Visão geral e as cinco camadas cumulativas (Contexto, Procedimento, Verificação, Permissão, Evidência) estão em [`REPO_HARNESS.md`](REPO_HARNESS.md).

| Seção | Responde | Arquivo |
|---|---|---|
| **Overview** | o que é o repo harness, as quatro perguntas que ele resolve e as cinco camadas cumulativas | [`REPO_HARNESS.md`](REPO_HARNESS.md) |
| **Tools** | quais ferramentas o agente pode invocar, com que limites, e o que exige autorização humana | [`TOOLS.md`](TOOLS.md) |
| **Skills** | o catálogo de procedimentos verificáveis para tarefas recorrentes que exigem julgamento | [`SKILLS.md`](SKILLS.md) |
| **Rules** | o estado desejado do repositório — arquitetura, coding e testing — e o motivo de cada regra | [`RULES.md`](RULES.md) |
| **Hooks** | as verificações locais versionadas (`.hooks/`) que rodam antes do código sair da máquina do agente | [`SENSORS.md`](SENSORS.md) |
| **Gates** | a arquitetura de verificação do commit ao deploy — local, CI, merge, ambiente, pós-deploy | [`GATES.md`](GATES.md) |
| **Documentation** | `AGENTS.md`, ADRs em `docs/adr/` e o evidence pack em `docs/evidence/` | [`DOCUMENTATION.md`](DOCUMENTATION.md) |
| **MCPs** | servidores Model Context Protocol, escopos autorizados e a diferença para uma tool local | [`MCPS.md`](MCPS.md) |

## 2. Skills

Uma skill é o procedimento verificável para uma tarefa recorrente que exige julgamento — o que a distingue de um script, que cobre o determinístico. Antes de agir, um agente verifica as skills disponíveis e usa todas as que se aplicam à missão. O catálogo — skills de base do workspace, skills por etapa da jornada e os limites de autonomia que nenhuma skill amplia — está em [`SKILLS.md`](SKILLS.md); os procedimentos executáveis, um `SKILL.md` por skill, estão em [`skills/`](../skills/README.md).

## 3. Agentes

Um agente é um processo com missão delimitada, contexto versionado, ferramentas declaradas, verificação objetiva e um envelope padronizado de saída. O conceito — anatomia, o que consome, quando escala — está em [`AGENTES.md`](AGENTES.md); os 23 contratos individuais, agrupados por fase (entrada e coordenação, produto/UX/discovery, especificação técnica, construção e validação, integração/homologação/operação, conhecimento e melhoria), estão em [`agentes/`](agentes/README.md).

## 4. Loops

Um loop é o contrato de colaboração de uma etapa da jornada: quem executa, em que ordem, o que atravessa a fronteira entre agentes e qual condição precisa ser verdadeira para avançar. O conceito — as três voltas e como agentes, skills, tools, MCPs, sensors e gates se encaixam em cada giro — está em [`LOOPS.md`](LOOPS.md); os 12 contratos das etapas da jornada, do intake à operação diária, estão em [`loops/`](loops/README.md).

## 5. Metodologia — Ciclo de Desenvolvimento de Software

A metodologia é a cola entre as camadas anteriores e a pessoa que opera o sistema na segunda-feira de manhã: não introduz conceito novo, mostra o que dispara o quê, quando uma pessoa é chamada, e o que acontece se ela não responder. Os cinco compromissos que governam o ciclo (quem propõe não aprova; aprovação exige evidência; mudança material invalida aprovação anterior; autonomia sobe por métrica; artefato só existe na fonte canônica) estão em [`METODOLOGIA.md`](METODOLOGIA.md); as sete páginas operacionais — papéis, checkpoints humanos, gatilhos, ritmos, manual do operador, jornada comentada e workflows de documentação — estão em [`metodologia/`](metodologia/README.md).

## 6. Workspace

O workspace é o lugar físico onde o trabalho de fato acontece: onde um Work Item é aberto, uma decisão vira artefato, um agente retoma contexto de uma sessão anterior. A fronteira com o repo harness e as quatro peças que todo workspace mantém (`AGENTS.md`, `BOARD.md`, `memory.md`, `projects/`) estão em [`WORKSPACE.md`](WORKSPACE.md); as quatro páginas operacionais — estrutura, ownership entre workspaces, harness do workspace e board/Work Items — estão em [`workspace/`](workspace/README.md).

---

## Idiomas

Toda página deste índice é publicada em inglês e português brasileiro a partir do mesmo branch: o texto canônico vive nestes caminhos e o `i18n/pt-BR/` os espelha um a um. Uma página ainda sem tradução cai para o inglês e avisa isso no topo, e a defasagem entre os dois é medida por `uv run scripts/i18n.py status`. Como traduzir, carimbar e adicionar um idioma está em [`i18n/README.md`](../i18n/README.md); a terminologia que precisa permanecer consistente está em [`i18n/GLOSSARY.md`](../i18n/GLOSSARY.md).

---

## Por onde começar

| Você quer… | Leia |
|---|---|
| Preparar um repositório para ser operado por agentes | [Harness](REPO_HARNESS.md) → [Tools](TOOLS.md) → [Skills](SKILLS.md) → [Rules](RULES.md) → [Hooks](SENSORS.md) → [Gates](GATES.md) → [Documentation](DOCUMENTATION.md) → [MCPs](MCPS.md) |
| Entender o catálogo de agentes | [Agentes](AGENTES.md) → [contratos individuais](agentes/README.md) |
| Ver a jornada de ponta a ponta | [Loops](LOOPS.md) → [as 12 etapas](loops/README.md) |
| Saber o que uma pessoa faz, na prática | [Metodologia](METODOLOGIA.md) → [manual do operador](metodologia/05-manual-do-operador.md) |
| Saber onde salvar o que produz | [Workspace](WORKSPACE.md) → [estrutura do workspace](workspace/01-estrutura-do-workspace.md) |
