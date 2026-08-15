# Gates

A arquitetura de gates define onde cada verificação acontece na trajetória de um Work Item, do commit ao deploy. O objetivo é que o feedback barato chegue primeiro e que nada que possa ser verificado por máquina chegue a uma pessoa.

## A escada completa

| Camada | Latência | Verifica | Falha bloqueia |
|---|---|---|---|
| **Local** (sensors) | segundos | checks determinísticos, baixo custo | commit ou push |
| **CI** | minutos | build, testes, segurança, arquitetura em ambiente limpo | merge |
| **Merge** | decisão consolidada | aprovações, status checks, proveniência da automação | integração |
| **Ambiente** | antes da exposição | secrets, branches e artefatos permitidos, aprovação por risco | deploy |
| **Pós-deploy** | janela de observação | comparação com baseline, regressão, rollback automático | rollout |

## Onde cada check pertence

O critério de posicionamento é a razão entre custo de execução e frequência de falha:

| Se o check… | …pertence a | Porque |
|---|---|---|
| roda em segundos e falha com frequência | pre-commit | corrigir custa quase nada e o loop é imediato |
| precisa de container ou serviço externo | pre-push ou CI | inviável a cada commit |
| depende de ambiente limpo ou build completo | CI | resultado local não é confiável |
| exige julgamento sobre risco ou trade-off | merge | é decisão, não verificação |
| só é observável com tráfego real | pós-deploy | não existe forma de antecipar |

Colocar um check caro cedo trava o agente em cada commit. Colocar um check barato tarde desperdiça um turno inteiro de um agente para informar algo que se saberia em dois segundos.

## CI — fast lane e deep lane

O CI do repositório opera com duas lanes, e a separação existe por razão econômica.

A **fast lane** roda a cada push e devolve sinal ao agente em minutos. Ela cobre apenas os checks selecionados pelos paths alterados — não é o pipeline completo. Um pipeline único e completo transforma cada tentativa em uma espera longa, e o agente ocioso custa tanto quanto o agente errado.

A **deep lane** roda antes do merge ou em schedule, e cobre a bateria completa: segurança, arquitetura, contratos, testes de ponta a ponta. Ela existe para garantir que o que passou pela fast lane também resiste a verificação mais cara.

A economia só se sustenta se a seleção de paths da fast lane também for verificada. Um filtro de caminho que silenciosamente deixa de corresponder — um diretório renomeado, um novo módulo fora do glob — transforma a fast lane em sinal verde para código não verificado. Trate o filtro como um gate que precisa do próprio teste, como descrito em [Falha](FAILURE.md#verificando-o-verificador).

## O gate de ambiente

A camada de ambiente é onde o repositório deixa de ser apenas um repositório e começa a representar exposição. Três regras a definem, e nenhuma delas trata do código:

**O agente nunca possui uma credencial de produção.** O deploy roda por uma identidade que o agente pode acionar, mas não personificar — um pipeline com seus próprios secrets, invocado por um evento autorizado. Um agente que consegue ler o secret de produção consegue exfiltrá-lo, e todo controle posterior pressupõe que ele não consiga.

**Testes nunca rodam contra dados de produção.** Onde os dados são regulados, o ambiente fornece um conjunto sintético ou anonimizado. "Acesso somente leitura à produção" não é uma mitigação: a leitura é o incidente quando o dado é o ativo.

**A aprovação escala com a exposição, não com o tamanho do diff.** Uma mudança de uma linha em um caminho de autenticação atravessa um gate mais alto do que uma mudança de cem linhas em um utilitário interno. A classificação de risco vive em `docs/rules/operations.md` e `docs/rules/security.md`; o gate a lê em vez de derivá-la novamente.

## Regras inegociáveis para gates com agentes

Três separações se aplicam especificamente quando agentes operam o repositório, e não podem ser relaxadas:

O mesmo agente não produz e aprova a própria mudança. Isso exige identidades distintas e verificáveis no sistema de versionamento — não basta instrução em prompt, porque a proteção precisa ser estrutural. O que essa identidade precisa carregar, e como é atestada, está em [Documentation](DOCUMENTATION.md#identidade-e-proveniência).

Agentes não alteram gates dentro do mesmo fluxo que aqueles gates avaliam. Sem essa separação, o caminho de menor resistência para um agente bloqueado passa a ser afrouxar o bloqueio.

Mudança em rules, sensors ou CI eleva o risco automaticamente e exige o owner do harness, fora do fluxo normal. Como essa mudança também invalida aprovações concedidas sob a versão anterior, ela é versionada em vez de apenas revisada — ver [Versionamento](VERSIONING.md).

## Autonomia progressiva e o teto do harness

Os gates sustentam níveis crescentes de autonomia. A regra central: **o nível do harness é o teto da autonomia, nunca a consequência dela**.

| Nível | O repositório tem | Autonomia sustentada |
|---|---|---|
| **HL0 — nu** | README, testes eventuais, CI de build | nenhuma — assistido |
| **HL1 — legível** | `AGENTS.md`, rules mínimas, `verify.sh`, pre-commit | A0–A1 |
| **HL2 — verificável** | CI por risco e paths, proteção de branch, evidence pack | A2 |
| **HL3 — operável por time** | skills do repo, worktree limpo, identidades por agente, gates de ambiente e pós-deploy | A3–A4 |

Um repositório em HL1 operando com autonomia A2 não é um repositório adiantado — é um repositório com um gate faltando que ninguém percebeu ainda.

Esses níveis HL se aplicam especificamente à verificação do repositório e definem o teto de autonomia desse escopo. A avaliação mais ampla da squad entre produto, fluxo, engenharia, conhecimento, plataforma e colaboração humano-IA está em [Maturidade](MATURITY.md).

## O que a escada não cobre

Três modos de falha atravessam todas as camadas da escada em vez de permanecerem em um único degrau, razão pela qual cada um tem seu próprio documento, em vez de uma linha na tabela acima:

| Modo de falha | Por que nenhum gate isolado o detecta | Onde |
|---|---|---|
| O próprio gate não roda ou passa pelo motivo errado | foi a verificação que falhou, não a mudança | [Falha](FAILURE.md) |
| A evidência era válida quando produzida, e a base mudou sob ela | cada gate passou em um estado que já não existe | [Concorrência](CONCURRENCY.md) |
| O trabalho consumiu mais do que valia | nada está quebrado, portanto nada bloqueia | [Orçamento](BUDGET.md) |

---

*Próximo: [Documentation](DOCUMENTATION.md) — ADRs, evidence pack e a estrutura completa de arquivos.*
