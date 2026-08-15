# Glossary

Terminology that must stay consistent across every locale. A translation that renders the same concept two different ways costs the reader more than a slightly awkward sentence.

## Do not translate

These are the vocabulary of the method, not prose. They stay in English in every language, keep their English plural where the sentence allows (`skills`, `loops`, `gates`), and take the article the sentence needs (`o harness`, `a skill`, `os loops`).

| Term | Why it stays | Portuguese usage |
|---|---|---|
| **harness** | names a specific construct of this method; "arreio"/"estrutura" loses it | *o harness*, *o repo harness* |
| **skill** | a defined artifact (`SKILL.md`), not a generic ability | *a skill*, *as skills* |
| **loop** | deliberately not "workflow" — the distinction disappears in translation | *o loop*, *os loops* |
| **gate** | paired with *sensor* on the verification ladder | *o gate*, *os gates* |
| **sensor** | same word in both languages | *o sensor*, *os sensores* |
| **workspace** | names the directory and the concept | *o workspace* |
| **work item** | a unit with an ID and a lifecycle | *o work item*, *os work items* |
| **handoff** | a contract between agents, not a generic delivery | *o handoff* |
| **intake** | names a specific journey stage | *o intake* |
| **discovery** | names a specific journey stage | *o discovery* |
| **evidence pack** | a named artifact | *o evidence pack* |
| **board** | names the file (`BOARD.md`) | *o board* |
| **backlog**, **checkpoint**, **rollout**, **rollback**, **trade-off** | established loanwords in Brazilian technical usage | as written |
| **PRD**, **ADR**, **MCP**, **LSP**, **CI**, **PR** | acronyms | as written |
| **lint**, **typecheck**, **commit**, **push**, **merge**, **deploy** | established loanwords | as written |

Tool, file, command and role names are never translated: `verify.sh`, `AGENTS.md`, `kb-store/`, `pre-commit`, Serena, RTK, Tech Lead, Product Manager, UX.

## Standard renderings

Where a term *is* translated, it is translated the same way every time.

| English | pt-BR |
|---|---|
| agent | agente |
| rule | rule (in `RULES.md` context) / regra (in prose) |
| journey | jornada |
| stage | etapa |
| verification | verificação |
| evidence | evidência |
| ownership | propriedade |
| trigger | gatilho |
| cadence | cadência |
| attempt | tentativa |
| statement | afirmação |
| scope | escopo |
| constraint | restrição |
| assumption | premissa |
| finding | achado |
| output contract | contrato de saída |
| source of truth | fonte da verdade |
| dead code | código morto |
| mutation testing | teste de mutação |
| circular dependency | dependência circular |
| unused dependency | dependência não usada |
| architecture boundary | fronteira de arquitetura |
| context window | janela de contexto |

## Register

Portuguese documentation uses the same register as the English: direct, second person avoided, no exclamation marks, no filler. Prefer the impersonal or the infinitive (*"a skill é verificada"*, *"antes de agir, um agente verifica"*) over addressing the reader.

Numbers, units and code stay as written. Em dashes (—) are used the same way in both languages.
