---
title: Agent Team — prompts operacionais por papel
status: proposed
updated_at: 2026-08-08
---

# Prompts operacionais dos agentes

> Os 23 papéis do catálogo, materializados como prompts autocontidos e independentes de runtime.

## Em 2 minutos

O [catálogo](catalog.md) define o que cada agente deve fazer. Este diretório entrega os agentes **prontos para usar**: uma pasta por papel, com um único prompt que reúne o contrato operacional, a presença e as diretivas estáveis do sponsor.

`AGENT.md` é a única fonte de instruções executáveis do papel. Cada `AGENT.md` contém todas as regras de execução, output e persistência do papel. Fontes, regras locais e skills só são lidas quando forem específicas da missão.

```text
<agent-id>/
└── AGENT.md     # prompt único: missão, limites, presença e diretivas estáveis
```

Não precrie memória operacional: ela nasce de fatos e decisões reais. Segredos, credenciais e arquivos `.env` não pertencem a estas pastas versionadas.

Um runtime pode carregar o arquivo diretamente, ou um orquestrador pode fornecer o seu conteúdo como instrução de papel. A pasta não pressupõe comandos, identidade sincronizável ou configuração de uma ferramenta específica.

---

## Catálogo materializado

| Agente | Identidade | Sponsor |
|---|---|---|
| [`intake-agent`](intake-agent/AGENT.md) | Intake Agent | Product Manager |
| [`meeting-context-agent`](meeting-context-agent/AGENT.md) | Meeting Context Agent | owner da reunião |
| [`orchestrator-agent`](orchestrator-agent/AGENT.md) | Orchestrator Agent | owner humano da fase |
| [`product-manager-agent`](product-manager-agent/AGENT.md) | Product Manager Agent | Product Manager |
| [`ux-specification-agent`](ux-specification-agent/AGENT.md) | UX Specification Agent | UX |
| [`tech-lead-discovery-agent`](tech-lead-discovery-agent/AGENT.md) | Tech Lead Discovery Agent | Tech Lead |
| [`adversarial-product-manager-agent`](adversarial-product-manager-agent/AGENT.md) | Adversarial Product Manager Agent | Product Manager |
| [`specification-tech-lead-agent`](specification-tech-lead-agent/AGENT.md) | Specification Tech Lead Agent | Tech Lead |
| [`adversarial-tech-lead-agent`](adversarial-tech-lead-agent/AGENT.md) | Adversarial Tech Lead Agent | Tech Lead |
| [`specialist-security-data-platform-agent`](specialist-security-data-platform-agent/AGENT.md) | Security, Data & Platform Specialist Agent | Tech Lead ou especialista |
| [`software-engineer-agent`](software-engineer-agent/AGENT.md) | Software Engineer Agent | Tech Lead |
| [`qa-validation-agent`](qa-validation-agent/AGENT.md) | QA & Validation Agent | Tech Lead |
| [`security-review-agent`](security-review-agent/AGENT.md) | Security Review Agent | Tech Lead ou Security Owner |
| [`architecture-review-agent`](architecture-review-agent/AGENT.md) | Architecture Review Agent | Tech Lead |
| [`adversarial-code-reviewer-agent`](adversarial-code-reviewer-agent/AGENT.md) | Adversarial Code Reviewer Agent | Tech Lead |
| [`pr-agent`](pr-agent/AGENT.md) | PR Agent | Tech Lead |
| [`product-validation-agent`](product-validation-agent/AGENT.md) | Product Validation Agent | Product Manager e UX |
| [`release-agent`](release-agent/AGENT.md) | Release Agent | Tech Lead |
| [`observability-agent`](observability-agent/AGENT.md) | Observability Agent | Tech Lead |
| [`knowledge-agent`](knowledge-agent/AGENT.md) | Knowledge Agent | owner do domínio |
| [`telemetry-agent`](telemetry-agent/AGENT.md) | Telemetry Agent | trio |
| [`auto-dream-agent`](auto-dream-agent/AGENT.md) | Auto Dream Agent | trio |
| [`critic-agent`](critic-agent/AGENT.md) | Critic Agent | owner da decisão |

---

## Uso

Leia o `AGENT.md` do papel escolhido e entregue ao agente a identidade da missão, os artefatos de entrada e as permissões autorizadas. O prompt não substitui essas entradas: ele define como o papel trabalha depois de recebê-las.

---

## Segurança e operação

**Isolamento.** Cada agente precisa de estado e diretório de trabalho próprios quando rodar em paralelo. O prompt não cria sandbox nem concede permissões: configure-os no runtime.

**Credenciais.** Não armazene tokens, OAuth, chaves, `.env`, sessões ou credenciais nestas pastas. Elas são versionadas.

**Exposição.** Configure bindings de canais somente depois de revisar identidade, acesso e comportamento público.

**Independência.** Papéis de autoria e crítica usam instâncias independentes sempre que houver risco de autoavaliação — é a mesma regra do [catálogo](catalog.md#3-mapa-dos-agentes), e ignorá-la anula o valor dos agentes adversariais.

---

## Registro auxiliar

[`registry.yaml`](registry.yaml) é um inventário dos papéis, destinado a automação e auditoria. Ele não é um manifesto de runtime.
