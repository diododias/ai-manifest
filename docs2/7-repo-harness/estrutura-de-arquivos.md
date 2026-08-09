---
title: A estrutura de arquivos do repo harness
status: canonical
updated_at: 2026-08-09
---

# A estrutura de arquivos do repo harness

> Onde cada peça do harness fica no repositório, o que vai em `AGENTS.md` e nas rules, e as decisões de organização que parecem burocráticas mas evitam custo no médio prazo.

## O alvo completo

A árvore abaixo é o alvo de um repositório maduro — o nível HL3 que você verá em [Níveis de maturidade](niveis-de-maturidade.md). Repositórios em níveis anteriores têm um subconjunto dela. Use-a como referência do que existe quando o harness está completo, não como checklist a cumprir de uma vez.

```text
<repositório>/
├── AGENTS.md                      # contrato de entrada do agente
├── README.md                      # uso humano: rodar, buildar, contribuir
├── CODEOWNERS                     # propriedade por path
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
│   └── permissions.md             # o que exige humano neste repositório
│
├── scripts/
│   ├── verify.sh                  # entrada única das verificações locais
│   └── evidence.sh                # coleta e empacota evidência
│
├── .hooks/                        # pre-commit e pre-push versionados
└── .ci/                           # fast lane e deep lane
```

## Três decisões que parecem burocráticas e não são

Três escolhas dessa árvore têm uma alternativa mais simples e aparentemente melhor — que se revela pior no médio prazo. Entender o porquê ajuda a não "simplificar" no lugar errado.

A primeira: **rules em arquivos separados, não em um `AGENTS.md` gigante**. O `AGENTS.md` é lido inteiro em toda execução; as rules são lidas sob demanda. Fundir os dois faz cada tarefa trivial pagar o custo de contexto da regra de migração de banco. É uma decisão de orçamento de contexto, não de estética.

A segunda: **`scripts/verify.sh` como entrada única**. Hooks, CI e agente chamam o mesmo script. Sem isso, a verificação local e a de CI divergem — e a divergência aparece na forma mais cara possível: o agente entrega, o CI reprova, e ninguém consegue reproduzir localmente.

A terceira: **`docs/evidence/` dentro do repositório**. A evidência acompanha o código que ela comprova. Guardada fora, sobrevive à troca de ferramenta de CI mas perde a ligação com o commit; guardada dentro, a ligação é o próprio histórico do Git.

## O que cada arquivo carrega — e o que não carrega

Cada peça do harness tem um escopo preciso. Colocar conteúdo na peça errada é o defeito mais comum de um harness mal montado, então vale a tabela.

| Arquivo | Carrega | Não carrega |
|---|---|---|
| `AGENTS.md` | como operar o repo, comandos, quando parar | arquitetura detalhada, histórico de decisões |
| `docs/rules/*.md` | a regra e o motivo dela | instruções de execução passo a passo |
| `docs/adr/` | por que a decisão foi tomada e o que custa | a regra vigente resultante |
| `skills/<skill>/SKILL.md` | passo a passo verificável de uma tarefa recorrente | conhecimento geral sobre o domínio |
| `.agent/permissions.md` | o que exige autorização humana | política de risco global do time |
| `CODEOWNERS` | quem aprova mudança em cada path | por que aquele path é sensível |

## O bloco mais esquecido do `AGENTS.md`

O `AGENTS.md` é lido antes de qualquer ação, o que torna cada linha dele um custo fixo por execução. Ele responde ao que o agente precisa para agir corretamente **na primeira tentativa** e delega o resto por ponteiro. Seus blocos são identidade, comandos, fronteiras, verificação, escalonamento e ponteiros.

De todos, o bloco de **escalonamento** é o que mais falta e o que mais importa. Sem ele, um agente diante de um requisito contraditório escolhe uma interpretação e segue — e a escolha só aparece na revisão, quando o trabalho já foi feito. As condições genéricas de escalonamento vêm do [contrato comum dos agentes](../4-agentes/contrato-comum.md); o `AGENTS.md` acrescenta as específicas do repositório.

## Rules descrevem estado; skills descrevem procedimento

Uma confusão vale desfazer, porque ela produz rules longas que ninguém lê e skills vagas que não se consegue executar. **Rules descrevem o estado desejado; skills descrevem o procedimento.** "Módulos de domínio não importam de infraestrutura" é uma rule. "Para adicionar um adapter, crie a interface em X e a implementação em Y" é uma skill.

E toda rule carrega o motivo junto — não por cortesia, mas por eficácia: um agente que conhece a razão de uma regra decide corretamente no caso de borda que a regra não previu. Um agente que só conhece a regra ou a aplica cegamente ou a ignora.

## Continue por aqui

Você tem a estrutura. Falta saber quanto dela seu repositório precisa ter para operar com um dado nível de autonomia — os [Níveis de maturidade](niveis-de-maturidade.md).
