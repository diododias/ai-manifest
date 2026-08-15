# Documentation

A camada de documentação do harness cobre três componentes distintos: o `AGENTS.md` como contrato de entrada, os ADRs como registro de decisões, e o evidence pack como rastro auditável de execução.

## `docs/adr/` — Registros de Decisão de Arquitetura

ADRs (Architecture Decision Records) registram as decisões tomadas, não a regra vigente. Essa distinção é fundamental: a rule em `architecture.md` diz "módulos de domínio não importam de infraestrutura"; o ADR correspondente diz por que essa decisão foi tomada, o que foi considerado, e o que ela custa.

Um agente que lê apenas rules sabe o que fazer. Um agente que também lê ADRs sabe por que — e decide corretamente no caso de borda que a rule não previu.

O template para criação de novos ADRs está em [`templates/tech-lead/adr.md`](../templates/tech-lead/adr.md).

## `docs/evidence/` — O rastro auditável

O evidence pack existe para que a aprovação de uma mudança seja baseada em fatos verificáveis, não na impressão que o resumo do agente causou.

Cada unidade de trabalho gera seu próprio diretório em `docs/evidence/<work-item>/`. A estrutura mínima:

```
docs/evidence/<work-item>/
├── summary.md          # o que foi feito, o que foi verificado
├── attestation.json    # quem produziu, sob qual versão do harness
├── verify-output.txt   # saída completa do scripts/verify.sh
├── gate-status.json    # por gate: passed, failed, skipped — e por quê
├── external-calls.log  # operações MCP e de rede, com parâmetros e respostas
├── test-results/       # artefatos dos testes executados
└── open-items.md       # o que permanece em aberto e por quê
```

O teste prático de um evidence pack bem construído: **outra pessoa consegue refazer a verificação sem perguntar nada a quem o produziu?** Se precisa de contexto adicional, o que existe ainda é um resumo, não evidência.

O evidence pack deve ser gerado automaticamente pelo script `scripts/evidence.sh`, e não montado manualmente pelo agente ao final da tarefa. Evidência manual é seletiva por natureza.

Dois dos arquivos acima existem porque um pack que registra apenas sucessos não é um rastro de auditoria. `gate-status.json` distingue *passed* de *skipped*, que é a diferença entre uma mudança verificada e outra não verificada que parece idêntica vista de fora ([Falha](FAILURE.md)). `external-calls.log` registra o que o agente fez fora do repositório, onde um gate local não consegue enxergar ([MCPs](MCPS.md#mcps-e-o-evidence-pack)).

## Identidade e proveniência

"Quem propõe não aprova" ou é uma propriedade do sistema de controle de versão ou não é nada. Instruções em prompt não conseguem impor isso, porque o mesmo processo que as obedeceria é o processo que está sendo restringido. O harness, portanto, registra estruturalmente quem produziu cada artefato.

Três coisas precisam ser verdadeiras:

**A identidade produtora é distinta e autenticada.** Cada papel de agente capaz de escrever commits faz isso sob sua própria identidade — uma conta ou credencial de aplicação separada, com commits assinados. A aprovação por uma identidade que aparece como autora da mesma mudança é rejeitada pelo gate de merge, não por convenção.

**O artefato registra o que o produziu.** `attestation.json` registra os fatos de que uma pessoa revisora precisa e que um agente não consegue autorreportar com credibilidade depois: papel do agente, modelo e versão, versão do harness, SHA de cada arquivo de rule efetivamente lido, Work Item e commit base de onde o trabalho começou.

```json
{
  "work_item": "WI-1043",
  "agent": "software-engineer-agent",
  "model": "claude-sonnet-5",
  "harness_version": "2.4.0",
  "rules_read": { "docs/rules/architecture.md": "9f2c…", "docs/rules/testing.md": "41ab…" },
  "base_commit": "e7d1c9a",
  "produced_at": "2026-08-14T18:22:04Z"
}
```

**A proveniência é verificada, não presumida.** O gate de merge confere a atestação contra os commits descritos por ela. Uma atestação que ninguém valida documenta uma intenção, e o modo de falha de uma afirmação não validada é estar errada apenas quando importa.

O campo `rules_read` é o que torna uma aprovação auditável depois do fato: ele responde "sob quais rules isto foi aceito?" sem depender da memória de ninguém sobre como o repositório estava naquela semana. Também é a chave de associação com [Versionamento](VERSIONING.md) — quando uma rule muda, esse campo identifica exatamente quais aprovações anteriores foram concedidas sob o texto antigo.

## A estrutura completa de arquivos

Um repositório em nível HL3 — o alvo de maturidade plena — apresenta a seguinte estrutura:

```text
<repositório>/
├── AGENTS.md                      # contrato de entrada do agente
├── README.md                      # uso humano: rodar, buildar, contribuir
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
│   ├── HARNESS_VERSION            # versão atual do harness deste repositório
│   ├── CHANGELOG.md               # o que mudou no harness e o que isso invalida
│   ├── settings.json              # tools permitidas, limites, orçamentos
│   ├── mcps.json                  # servidores MCP autorizados e escopos
│   ├── identity.md                # sob qual identidade cada papel de agente escreve
│   ├── trust.md                   # conteúdo confiável e não confiável neste repositório
│   └── permissions.md             # o que exige uma pessoa neste repositório
│
├── scripts/
│   ├── verify.sh                  # entrada única das verificações locais
│   ├── evidence.sh                # coleta e empacota evidência
│   └── harness-doctor.sh          # informa o nível de maturidade realmente atingido
│
├── .hooks/                        # sensors versionados (pre-commit, pre-push)
└── .github/workflows/             # fast lane e deep lane
```

O último path é o que deve ser adaptado: está escrito como GitHub Actions por ser o caso comum, e corresponde a `.gitlab-ci.yml` ou ao equivalente em outra plataforma. O que importa não é o diretório, mas que as duas lanes estejam em arquivos separados e que nenhum deles possa ser editado de dentro do fluxo que controla.

Repositórios em HL1 ou HL2 contêm subconjuntos dessa árvore. Os níveis de maturidade definem qual subconjunto é suficiente para cada patamar de autonomia — a decomposição item a item está em [Maturidade](MATURITY.md).

## O que cada arquivo carrega

| Arquivo | Carrega | Não carrega |
|---|---|---|
| `AGENTS.md` | como operar o repo, comandos, quando parar | arquitetura detalhada, histórico de decisões |
| `docs/rules/*.md` | a regra e o motivo dela | instruções de execução passo a passo |
| `docs/adr/` | por que a decisão foi tomada e o que custa | a regra vigente resultante |
| `skills/<skill>/SKILL.md` | passo a passo verificável de uma tarefa recorrente | conhecimento geral sobre o domínio |
| `.agent/identity.md` | qual identidade escreve o quê e quem pode aprovar | as credenciais em si |
| `.agent/trust.md` | quais entradas são conteúdo e quais são instruções | o modelo de ameaça da organização |
| `.agent/permissions.md` | o que exige autorização humana | política de risco global do time |
| `.agent/mcps.json` | servidores MCP autorizados e escopos permitidos | credenciais ou configuração de ambiente |

---

*Próximo: [MCPs](MCPS.md) — sistemas externos, escopos autorizados e por que são um tipo diferente de tool.*
