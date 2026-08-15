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

Vale entender também o que o harness **não é**. Ele não é o pipeline de CI — o pipeline é apenas uma implementação possível da camada de verificação. Ele não é a documentação de arquitetura em si — ele aponta para ela. E ele não é sobre como o trabalho é organizado fora do código: isso é responsabilidade do workspace de quem coordena os agentes.

## As cinco camadas sob carga

As cinco camadas descrevem um harness que está sendo construído. Um harness que está sendo *operado* — vários agentes, tráfego real, um repositório que continua mudando — precisa de quatro propriedades que nenhuma camada isolada possui, porque cada uma delas representa uma forma de as camadas estarem presentes e ainda assim não se sustentarem:

| Propriedade | A falha a que responde |
|---|---|
| **Confiança** | o agente leu algo hostil e tratou como instrução |
| **Resiliência** | a verificação não rodou, e seu silêncio foi lido como aprovação |
| **Coordenação** | a evidência era válida contra uma base que mudou desde então |
| **Economia** | nada quebrou, e o trabalho custou mais do que valia |

Elas são propriedades, e não camadas, porque não podem ser construídas em sequência depois das outras: cada uma é uma pergunta feita *sobre* as cinco camadas, e um harness que nunca as faz não é um harness em estágio anterior — é um harness cujas lacunas ainda não apareceram.

---

## Índice

**Fundamentos**

- [Permissões](PERMISSIONS.md) — o que o agente pode invocar, o que exige uma pessoa e por que isso não pode viver no prompt
- [Tools](TOOLS.md) — índice de ferramentas: LSP, verificação, navegação, gestão de contexto
- [Rules](RULES.md) — estado desejado, contrato de entrada (`AGENTS.md`), escalação e reversibilidade
- [Sensors](SENSORS.md) — verificações locais versionadas (pre-commit, pre-push)
- [Gates](GATES.md) — arquitetura de verificação do commit ao deploy e níveis de autonomia
- [Documentation](DOCUMENTATION.md) — ADRs, evidence pack, identidade e proveniência
- [MCPs](MCPS.md) — servidores Model Context Protocol, escopos e autorização
- [Skills](SKILLS.md) — catálogo de procedimentos verificáveis do repositório

**Operação sob carga**

- [Confiança](TRUST.md) — conteúdo não confiável, injeção, exfiltração e o harness como supply chain
- [Falha](FAILURE.md) — fail-closed, o gate que não rodou, checks instáveis, verificação do verificador
- [Concorrência](CONCURRENCY.md) — vários agentes ao mesmo tempo, frescor de evidência e ordem de integração
- [Orçamento](BUDGET.md) — custo, turnos, contexto e o que degrada quando acabam
- [Versionamento](VERSIONING.md) — o harness tem versões, e uma mudança invalida aprovações anteriores
- [Métricas](METRICS.md) — taxa de escape dos gates e o painel que promove ou rebaixa autonomia

**Adoção**

- [Maturidade](MATURITY.md) — o checklist por nível, `harness-doctor` e a ordem de construção

---

*Próximo: [Permissões](PERMISSIONS.md) — a camada que não pode ser imposta por um pedido.*
