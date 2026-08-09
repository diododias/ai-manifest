---
title: Agent Team — workspaces importáveis do OpenClaw
status: proposed
updated_at: 2026-08-08
---

# Agentes importáveis no OpenClaw

> Os 23 papéis do catálogo, materializados como workspaces prontos para importar — cada um com identidade, personalidade, contrato operacional e diretivas do sponsor.

## Em 2 minutos

O [catálogo](catalog.md) define o que cada agente deve fazer. Este diretório entrega os agentes **prontos para rodar**: uma pasta por papel, com quatro arquivos que o OpenClaw consome diretamente.

A separação em quatro arquivos não é cosmética. `AGENTS.md` carrega o contrato operacional que muda quando o processo muda; `SOUL.md` carrega a personalidade, que deve permanecer estável; `IDENTITY.md` é sincronizado com a ferramenta; e `USER.md` isola as diretivas do sponsor, que variam por instalação. Alterar o processo não deveria exigir reescrever a personalidade do agente — e vice-versa.

```text
<agent-id>/
├── AGENTS.md    # missão, regras operacionais, gates, tools e memória
├── SOUL.md      # personalidade, voz, convicções e limites
├── IDENTITY.md  # nome, tema e emoji sincronizáveis
├── USER.md      # diretivas estáveis sobre sponsor e interação
└── FULL.md      # os quatro anteriores consolidados em um prompt único
```

`FULL.md` existe para ferramentas que não suportam workspace multiarquivo. Ele é mantido manualmente: **ao alterar qualquer um dos quatro arquivos-fonte, atualize o `FULL.md` correspondente no mesmo commit**, ou o agente passará a executar uma versão diferente da que o catálogo declara.

Dois arquivos são deliberadamente ausentes: `MEMORY.md` e `memory.md` não são pré-criados, porque memória deve nascer de fatos e decisões reais e nunca de placeholders. `BOOTSTRAP.md` também não é necessário, já que as identidades estão definidas. `TOOLS.md` e `HEARTBEAT.md` foram aposentados nas versões atuais do OpenClaw — convenções de ferramentas ficam em `AGENTS.md`, e rotinas recorrentes usam os mecanismos de automação da instalação.

---

## Catálogo materializado

| Workspace | Identidade | Sponsor |
|---|---|---|
| [`intake-agent`](intake-agent/SOUL.md) | Intake Agent | Product Manager |
| [`meeting-context-agent`](meeting-context-agent/SOUL.md) | Meeting Context Agent | owner da reunião |
| [`orchestrator-agent`](orchestrator-agent/SOUL.md) | Orchestrator Agent | owner humano da fase |
| [`product-manager-agent`](product-manager-agent/SOUL.md) | Product Manager Agent | Product Manager |
| [`ux-specification-agent`](ux-specification-agent/SOUL.md) | UX Specification Agent | UX |
| [`tech-lead-discovery-agent`](tech-lead-discovery-agent/SOUL.md) | Tech Lead Discovery Agent | Tech Lead |
| [`adversarial-product-manager-agent`](adversarial-product-manager-agent/SOUL.md) | Adversarial Product Manager Agent | Product Manager |
| [`specification-tech-lead-agent`](specification-tech-lead-agent/SOUL.md) | Specification Tech Lead Agent | Tech Lead |
| [`adversarial-tech-lead-agent`](adversarial-tech-lead-agent/SOUL.md) | Adversarial Tech Lead Agent | Tech Lead |
| [`specialist-security-data-platform-agent`](specialist-security-data-platform-agent/SOUL.md) | Security, Data & Platform Specialist Agent | Tech Lead ou especialista |
| [`software-engineer-agent`](software-engineer-agent/SOUL.md) | Software Engineer Agent | Tech Lead |
| [`qa-validation-agent`](qa-validation-agent/SOUL.md) | QA & Validation Agent | Tech Lead |
| [`security-review-agent`](security-review-agent/SOUL.md) | Security Review Agent | Tech Lead ou Security Owner |
| [`architecture-review-agent`](architecture-review-agent/SOUL.md) | Architecture Review Agent | Tech Lead |
| [`adversarial-code-reviewer-agent`](adversarial-code-reviewer-agent/SOUL.md) | Adversarial Code Reviewer Agent | Tech Lead |
| [`pr-agent`](pr-agent/SOUL.md) | PR Agent | Tech Lead |
| [`product-validation-agent`](product-validation-agent/SOUL.md) | Product Validation Agent | Product Manager e UX |
| [`release-agent`](release-agent/SOUL.md) | Release Agent | Tech Lead |
| [`observability-agent`](observability-agent/SOUL.md) | Observability Agent | Tech Lead |
| [`knowledge-agent`](knowledge-agent/SOUL.md) | Knowledge Agent | owner do domínio |
| [`telemetry-agent`](telemetry-agent/SOUL.md) | Telemetry Agent | trio |
| [`auto-dream-agent`](auto-dream-agent/SOUL.md) | Auto Dream Agent | trio |
| [`critic-agent`](critic-agent/SOUL.md) | Critic Agent | owner da decisão |

---

## Importação no OpenClaw

O OpenClaw não usa um arquivo único de importação para workspaces. A operação suportada é registrar cada pasta com `openclaw agents add` e depois sincronizar `IDENTITY.md`.

```bash
agent_workspace="/caminho/para/o/repositorio/docs/agents/product-manager-agent"

openclaw agents add product-manager-agent \
  --workspace "$agent_workspace" \
  --non-interactive

openclaw agents set-identity \
  --agent product-manager-agent \
  --from-identity
```

Para verificar o resultado:

```bash
openclaw agents list --bindings
```

A importação não cobre credenciais, escolha de modelo nem bindings de canal — esses elementos são definidos na instalação, conforme ambiente e política.

---

## Segurança e operação

**Isolamento.** Cada agente tem workspace e estado próprios; `agentDir` nunca é reutilizado entre agentes. O workspace é o diretório de trabalho padrão, não um sandbox rígido — quando isolamento real for necessário, defina sandbox e permissões por agente.

**Credenciais.** Não armazene tokens, OAuth, chaves, `.env`, sessões ou credenciais nestas pastas. Elas são versionadas.

**Exposição.** Configure bindings de canais somente depois de revisar identidade, acesso e comportamento público.

**Independência.** Papéis de autoria e crítica usam instâncias independentes sempre que houver risco de autoavaliação — é a mesma regra do [catálogo](catalog.md#3-mapa-dos-agentes), e ignorá-la anula o valor dos agentes adversariais.

---

## Registro auxiliar

[`registry.yaml`](registry.yaml) é um inventário deste repositório, destinado a automação e auditoria. Ele não substitui `openclaw.json` nem é um manifesto nativo do OpenClaw.
