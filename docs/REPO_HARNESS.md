# 1. Harness do Repositório da Aplicação

---

## Overview

O **repo harness** converte o conhecimento tácito do repositório em arquivos versionados que o agente lê sozinho e em verificações que rodam sem pedir licença. Ele mora dentro do repositório de código, viaja com o clone, e existe para responder quatro perguntas antes que o agente precise agir:

1. O que é este repositório?
2. Como se faz as coisas aqui?
3. O que preciso provar antes de dizer que terminei?
4. O que não posso tocar sem autorização?

O harness se organiza em cinco camadas cumulativas. A ordem importa: cada camada elimina uma classe específica de falha, e construir fora de sequência produz falhas caras.

| Camada | Responde | Materializa em |
|---|---|---|
| **Contexto** | o que este repositório é e quais regras valem | `AGENTS.md`, `docs/rules/` |
| **Procedimento** | como executar uma tarefa recorrente do jeito certo | `skills/`, scripts |
| **Verificação** | o que precisa ser verdade antes de avançar | sensors, CI, políticas de merge |
| **Permissão** | o que este agente pode tocar e o que exige gente | `.agent/`, ambientes |
| **Evidência** | como provar depois que estava correto | evidence pack, logs, artefatos |

Vale entender também o que o harness **não é**. Ele não é a esteira de CI — a esteira é apenas uma implementação possível da camada de verificação. Ele não é a documentação de arquitetura em si — ele aponta para ela. E ele não é sobre como o trabalho é organizado fora do código: isso é responsabilidade do workspace de quem coordena os agentes.

---

## Índice

- [Tools](TOOLS.md) — ferramentas autorizadas, LSP, navegação de codebase, gestão de contexto
- [MCPs](MCPS.md) — servidores Model Context Protocol, escopos e autorização
- [Skills](SKILLS.md) — catálogo de procedimentos verificáveis do repositório
- [Rules](RULES.md) — estado desejado, contrato de entrada (`AGENTS.md`) e condições de escalonamento
- [Sensors](SENSORS.md) — verificações locais versionadas (pre-commit, pre-push)
- [Gates](GATES.md) — arquitetura de verificação do commit ao deploy e níveis de autonomia
- [Documentation](DOCUMENTATION.md) — ADRs, evidence pack e estrutura completa de arquivos

---

*Próximo: [Agentes](AGENTES.md) — como um agente funciona e o catálogo dos 23 papéis.*
