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
├── verify-output.txt   # saída completa do scripts/verify.sh
├── test-results/       # artefatos dos testes executados
└── open-items.md       # o que permanece em aberto e por quê
```

O teste prático de um evidence pack bem construído: **outra pessoa consegue refazer a verificação sem perguntar nada a quem o produziu?** Se precisa de contexto adicional, o que existe ainda é um resumo, não evidência.

O evidence pack deve ser gerado automaticamente pelo script `scripts/evidence.sh`, e não montado manualmente pelo agente ao final da tarefa. Evidência manual é seletiva por natureza.

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
│   ├── settings.json              # tools permitidas, limites, modelos
│   ├── mcps.json                  # servidores MCP autorizados e escopos
│   └── permissions.md             # o que exige humano neste repositório
│
├── scripts/
│   ├── verify.sh                  # entrada única das verificações locais
│   └── evidence.sh                # coleta e empacota evidência
│
├── .hooks/                        # sensors versionados (pre-commit, pre-push)
└── .ci/                           # fast lane e deep lane
```

Repositórios em HL1 ou HL2 contêm subconjuntos dessa árvore. Os níveis de maturidade definem qual subconjunto é suficiente para cada patamar de autonomia.

## O que cada arquivo carrega

| Arquivo | Carrega | Não carrega |
|---|---|---|
| `AGENTS.md` | como operar o repo, comandos, quando parar | arquitetura detalhada, histórico de decisões |
| `docs/rules/*.md` | a regra e o motivo dela | instruções de execução passo a passo |
| `docs/adr/` | por que a decisão foi tomada e o que custa | a regra vigente resultante |
| `skills/<skill>/SKILL.md` | passo a passo verificável de uma tarefa recorrente | conhecimento geral sobre o domínio |
| `.agent/permissions.md` | o que exige autorização humana | política de risco global do time |
| `.agent/mcps.json` | servidores MCP autorizados e escopos permitidos | credenciais ou configuração de ambiente |
