---
title: Agent Team — workspaces importáveis do OpenClaw
status: proposed
updated_at: 2026-08-08
---

# Agentes importáveis no OpenClaw

Cada subpasta deste diretório é um workspace independente do OpenClaw, materializado a partir do [catálogo operacional](catalog.md). A estrutura segue o contrato atual da ferramenta:

```text
<agent-id>/
├── AGENTS.md    # missão, regras operacionais, gates, tools e memória
├── SOUL.md      # personalidade, voz, convicções e limites
├── IDENTITY.md  # nome, tema e emoji sincronizáveis
└── USER.md      # diretivas estáveis sobre sponsor e interação
```

`MEMORY.md` e `memory/YYYY-MM-DD.md` não são pré-criados: memória deve nascer de fatos e decisões reais, nunca de placeholders. `BOOTSTRAP.md` também não é necessário porque as identidades já estão definidas.

`TOOLS.md` e `HEARTBEAT.md` foram aposentados nas versões atuais do OpenClaw. Convenções de ferramentas ficam em `AGENTS.md`; rotinas recorrentes devem ser configuradas pelos mecanismos atuais de automação da instalação.

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

## Importação

O OpenClaw não usa um arquivo único de importação para workspaces. A operação suportada é registrar cada pasta com `openclaw agents add` e então sincronizar `IDENTITY.md`.

Para revisar os comandos sem alterar a instalação:

```bash
bash import-openclaw.sh
```

Para registrar todos os agentes:

```bash
bash import-openclaw.sh --apply
```

O helper usa os caminhos absolutos derivados da própria localização, não copia credenciais, não configura modelo e não cria bindings de canal. Esses elementos devem ser definidos na instalação conforme ambiente e política.

Importação manual de um agente:

```bash
agent_workspace="/caminho/para/o/repositorio/docs/agents/product-manager-agent"
openclaw agents add product-manager-agent \
  --workspace "$agent_workspace" \
  --non-interactive
openclaw agents set-identity \
  --agent product-manager-agent \
  --from-identity
```

Depois da importação, valide:

```bash
openclaw agents list --bindings
```

## Segurança e operação

- Cada agente deve ter workspace e estado próprios.
- Não reutilize `agentDir` entre agentes.
- O workspace é o diretório de trabalho padrão, não um sandbox rígido.
- Defina sandbox e permissões por agente quando isolamento for necessário.
- Não armazene tokens, OAuth, chaves, `.env`, sessões ou credenciais nestas pastas.
- Configure bindings de canais somente depois de revisar identidade, acesso e comportamento público.
- Papéis de autoria e crítica devem usar instâncias independentes quando houver risco de autoavaliação.

## Registro auxiliar

[registry.yaml](registry.yaml) é um inventário deste repositório para automação e auditoria. Ele não substitui `openclaw.json` nem é um manifesto nativo do OpenClaw.
