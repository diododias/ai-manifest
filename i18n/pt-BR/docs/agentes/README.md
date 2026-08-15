# Contratos individuais dos agentes

Este diretório contém a documentação de cada um dos 23 papéis do Agent Team, um arquivo por agente. O conceito geral — o que um agente é, o que consome, como executa uma missão e quando escala — está em [Agentes — How Agents Work](../AGENTES.md); aqui ficam os contratos específicos.

## Como ler um contrato

Cada arquivo segue a mesma estrutura, e a leitura na ordem abaixo responde às perguntas na sequência em que normalmente surgem:

| Seção | Responde |
|---|---|
| **Contrato operacional** | quem patrocina, o que o agente recebe, o que entrega, quais tools e skills usa, qual gate satisfaz e quando escala |
| **O que este agente não faz** | os limites explícitos do papel e a razão de cada um |
| **Presença e instintos** | a personalidade operacional que orienta o julgamento em casos não previstos |
| **Notas de operação** | as decisões e armadilhas específicas do papel na prática |
| **Prompt operacional** | onde está a única instrução executável do papel em `agents/` |

Todo agente cumpre, além dessas particularidades, o **contrato comum**: identidade de missão completa, regras universais de verdade, limite, skills e entrega, envelope padronizado de saída e as condições universais de escalonamento. Um contrato individual deve ser lido como "o contrato comum, mais estas particularidades".

## Entrada e coordenação

Recebem o que chega de fora e organizam o trabalho dos demais. Nenhum deles decide ou aprova: preparam e roteiam.

| Agente | Sponsor | Saída central |
|---|---|---|
| [📥 Intake Agent](intake-agent.md) | Product Manager | Work Item triado e priorizável |
| [📝 Meeting Context Agent](meeting-context-agent.md) | owner da reunião | resumo e context pack da transcrição |
| [🎛️ Orchestrator Agent](orchestrator-agent.md) | owner humano da fase | missões roteadas e estado consolidado |

## Produto, UX e discovery

Estruturam o problema antes de qualquer solução, com o par produção/crítica já presente.

| Agente | Sponsor | Saída central |
|---|---|---|
| [📋 Product Manager Agent](product-manager-agent.md) | Product Manager | `PB.md` ou `PRD.md` |
| [🧭 UX Specification Agent](ux-specification-agent.md) | UX | jornada, fluxos e UX spec |
| [🔭 Tech Lead Discovery Agent](tech-lead-discovery-agent.md) | Tech Lead | viabilidade e riscos iniciais |
| [🥊 Adversarial Product Manager Agent](adversarial-product-manager-agent.md) | Product Manager | crítica de produto classificada |

## Especificação técnica

Convertem o produto aprovado em estratégia técnica executável.

| Agente | Sponsor | Saída central |
|---|---|---|
| [📐 Specification Tech Lead Agent](specification-tech-lead-agent.md) | Tech Lead | `PLAN`, `SPEC`, `ADR`, `TASKS`, `CHECKLIST` |
| [♟️ Adversarial Tech Lead Agent](adversarial-tech-lead-agent.md) | Tech Lead | crítica técnica e trade-offs |
| [🧩 Security, Data & Platform Specialist Agent](specialist-security-data-platform-agent.md) | Tech Lead ou especialista | análise especializada de domínio |

## Construção e validação

O maior grupo, e onde a separação entre produzir e aprovar fica mais visível.

| Agente | Sponsor | Saída central |
|---|---|---|
| [🛠️ Software Engineer Agent](software-engineer-agent.md) | Tech Lead | código, testes, documentação e commits |
| [🧪 QA & Validation Agent](qa-validation-agent.md) | Tech Lead | matriz critério-evidência |
| [🛡️ Security Review Agent](security-review-agent.md) | Tech Lead ou Security Owner | achados de segurança e privacidade |
| [🏛️ Architecture Review Agent](architecture-review-agent.md) | Tech Lead | conformidade arquitetural |
| [🔎 Adversarial Code Reviewer Agent](adversarial-code-reviewer-agent.md) | Tech Lead | achados de corretude e manutenção |

## Integração, homologação e operação

Levam a mudança validada até a produção e observam sua saúde.

| Agente | Sponsor | Saída central |
|---|---|---|
| [🔀 PR Agent](pr-agent.md) | Tech Lead | PR e evidence pack |
| [✅ Product Validation Agent](product-validation-agent.md) | Product Manager e UX | relatório de homologação |
| [🚀 Release Agent](release-agent.md) | Tech Lead | release rastreável e reversível |
| [📡 Observability Agent](observability-agent.md) | Tech Lead | health report e alertas |

## Conhecimento e melhoria

Fecham o ciclo sobre o próprio sistema.

| Agente | Sponsor | Saída central |
|---|---|---|
| [📚 Knowledge Agent](knowledge-agent.md) | owner do domínio | fontes canônicas atualizadas |
| [📊 Telemetry Agent](telemetry-agent.md) | trio | dataset governado e painel do fluxo |
| [💭 Auto Dream Agent](auto-dream-agent.md) | trio | aprendizados e demandas P0–P3 |
| [⚖️ Critic Agent](critic-agent.md) | owner da decisão | crítica independente |

---

*Voltar para [Agentes — How Agents Work](../AGENTES.md) · [Harness do Repositório](../REPO_HARNESS.md)*
