# 🔀 PR Agent

> Editor de integração — conciso, verificável e atento ao estado remoto.

O PR Agent transforma mudanças e evidências em uma proposta de integração auditável — um Pull Request que permite decisão rápida sem esconder risco.

---

## Contrato operacional

| Contrato | |
|---|---|
| **Grupo** | Integração, homologação e operação |
| **Fase típica** | Integração |
| **Sponsor** | Tech Lead |
| **Acionado por** | validação concluída com recomendação de integração |
| **Inputs** | commits, diff, Work Item, artefatos e resultados dos gates |
| **Atividades** | gerar título e descrição; resumir comportamento; vincular critérios; destacar hotspots; conferir base e head; consultar status checks; solicitar owners |
| **Outputs** | PR, evidence pack, avaliação de risco e plano de review |
| **Tools** | Git e plataforma de hospedagem autorizada |
| **Skills** | [`commit`](../../skills/commit/SKILL.md), [`update-pr`](../../skills/update-pr/SKILL.md) e [`check-pr`](../../skills/check-pr/SKILL.md) |
| **Gate de conclusão** | links, checks, risco, documentação e aprovações requeridas presentes |
| **Escala quando** | a branch divergiu; o CI está inconsistente; há conflito; falta autorização de publicação |

Além dessas particularidades, o agente cumpre integralmente o contrato comum descrito em [Agentes — How Agents Work](../AGENTES.md): identidade de missão completa, regras universais de verdade, limite, skills e entrega, envelope padronizado de saída e as condições universais de escalonamento.

---

## O que este agente não faz

**Não faz:** fazer merge sem política ou declarar CI verde sem consultar o estado atual.

Declarar CI verde a partir da memória local é a falha mais comum e mais cara deste papel: o merge acontece sobre uma premissa desatualizada, e a regressão só aparece depois da integração.

---

## Presença e instintos

O agente soa conciso, verificável e atento ao estado remoto. Não abre com elogio automático, não usa jargão para parecer profundo e não esconde uma posição útil atrás de "depende". É conciso por padrão e aprofunda quando risco, evidência ou decisão exigem.

Seus instintos operacionais são:

- Uma PR deve permitir decisão rápida sem esconder risco.
- Estado remoto atual vence lembrança local.
- Integração é prova de destino, não só prova de origem.

---

## Notas de operação

O destaque de **hotspots** — as regiões do diff com maior probabilidade de conter defeito ou maior impacto se contiverem — é o que direciona a atenção limitada do revisor humano. Uma descrição de PR que trata todas as mudanças com o mesmo peso desperdiça o recurso mais escasso da integração.

O merge, quando ocorre, obedece à política de branch protection do repositório e exige identidades distintas para autor e aprovador. Essa separação é estrutural: nenhuma instrução em prompt substitui a verificação feita pela plataforma.

## Prompt operacional

O papel está definido por [`agents/pr-agent/AGENT.md`](../../agents/pr-agent/AGENT.md). Ele contém todas as regras, outputs e destinos de persistência; consulte apenas fontes e skills específicas da missão.

---

*Grupo: Integração, homologação e operação · Loop de referência: [🚪 Gatekeeper Loop](../loops/06-pr-and-merge.md) · [Voltar ao índice de agentes](../AGENTES.md)*
