# Maturidade

[Gates](GATES.md#autonomia-progressiva-e-o-teto-do-harness) estabelece a escada e a regra que a governa: o nível do harness é o teto da autonomia, nunca sua consequência. Esta página torna a escada operável — o que cada nível exige item a item e como um repositório descobre em qual nível realmente está, em vez daquele em que acredita estar.

Os níveis de autonomia concedidos pela escada, de A0 a A4, são definidos em [Checkpoints humanos](metodologia/02-checkpoints-humanos.md).

## O nível é calculado, não declarado

Um nível de maturidade é uma afirmação, e cada item abaixo foi escrito para que um script possa verificá-lo. Essa é toda a restrição de design desta página: um checklist que exige julgamento recebe uma resposta otimista de quem é consultado, e o nível declarado de um repositório, de outro modo, apenas registra a última vez em que alguém pensou sobre ele.

Duas regras decorrem de tornar o processo mecânico:

**O nível é o mínimo, não a média.** Um repositório que atende a todos os itens do HL2, exceto proteção de branch, está no HL1. Não há crédito parcial, porque o item ausente é exatamente aquele que um incidente encontrará.

**Um modo degradado declarado reduz o nível enquanto durar** ([Falha](FAILURE.md#declarando-um-modo-degradado)). Um gate em quarentena é um gate ausente enquanto a quarentena permanecer.

## HL1 — legível

O agente consegue entender o repositório e verificar o próprio trabalho localmente.

| Item | Verificável por |
|---|---|
| `AGENTS.md` na raiz, com todos os seis blocos presentes | o arquivo existe; o cabeçalho de cada bloco é encontrado; o bloco de escalação não está vazio |
| `docs/rules/` com pelo menos `architecture.md` e `testing.md` | os arquivos existem e não estão vazios |
| `testing.md` mapeia o tipo de mudança para os níveis obrigatórios | a tabela de mapeamento está presente ([Rules](RULES.md#a-estratégia-de-testes-como-rule)) |
| `scripts/verify.sh` existe e aceita `--staged`, `--affected`, `--full` | invocar cada opção com `--help` ou em uma execução simulada |
| `verify.sh` falha diante de uma entrada reconhecidamente ruim | executá-lo contra a fixture canário |
| `verify.sh` verifica se as próprias tools estão instaladas | remover uma tool do `PATH`; esperar falha, não um salto |
| `.hooks/` com um sensor de pre-commit, mais o bootstrap que define `core.hooksPath` | `git config core.hooksPath` retorna `.hooks` depois do bootstrap |
| Secret scanning roda no pre-commit | a fixture com credencial falsa é rejeitada |
| `.agent/settings.json` com `allowed` / `ask` / `denied` e um orçamento | o arquivo é interpretado; `allowed` não está vazio; não há curingas sobre famílias de comando |

## HL2 — verificável

Um ambiente limpo reproduz a verificação, e o resultado de uma mudança pode ser auditado por alguém que não a produziu.

| Item | Verificável por |
|---|---|
| Fast lane e deep lane de CI como configurações separadas | os dois arquivos existem; nenhum pode ser editado pelo fluxo que controla |
| Filtros de caminho da fast lane têm um teste | o teste dos filtros existe e roda ([Falha](FAILURE.md#verificando-o-verificador)) |
| Proteção de branch: sem push direto na branch padrão, com status checks obrigatórios | consultar a API da plataforma, não a documentação |
| `CODEOWNERS` cobrindo `.agent/`, `.hooks/`, configuração de CI e `docs/rules/` | cada caminho corresponde a um responsável que ainda existe |
| Evidence pack gerado por `scripts/evidence.sh` | executá-lo; o diretório contém `summary.md`, `verify-output.txt`, `gate-status.json` |
| `gate-status.json` distingue `passed`, `failed`, `skipped` | os três estados podem ser produzidos |
| `.agent/mcps.json` existe, ou o repositório declara que nenhum MCP está autorizado | o arquivo existe, ou a declaração explícita de escopo zero existe |
| `.agent/trust.md` declara quais caminhos são instrução | o arquivo existe; a lista de caminhos de instrução é exaustiva |
| `HARNESS_VERSION` e `.agent/CHANGELOG.md` | ambos existem; a versão pode ser interpretada ([Versionamento](VERSIONING.md)) |
| Um canário reconhecidamente ruim para os gates de arquitetura e de segredos | ambos os canários rodam de forma agendada e estão passando no momento |

## HL3 — operável por um time

Vários agentes operam o repositório ao mesmo tempo, e os controles se mantêm sem uma pessoa em cada loop.

| Item | Verificável por |
|---|---|
| Uma identidade distinta para cada papel de agente que escreve | as identidades existem e são diferentes; os commits são assinados |
| O gate de merge rejeita aprovação por um autor da mesma mudança | tentar em uma mudança de teste; esperar rejeição |
| `attestation.json` produzido e validado no merge | o gate de merge falha diante de uma atestação ausente ou divergente |
| Skills do repositório em `skills/<skill>/SKILL.md` | os procedimentos recorrentes deste repositório estão cobertos |
| O agente não possui credencial de produção | o inventário de credenciais mostra segredos de deploy apenas na identidade do pipeline |
| Baseline pós-deploy e critério de rollback automático | o critério está declarado e já foi exercitado pelo menos uma vez |
| Frescor da evidência verificado antes da integração | um pack obsoleto é rejeitado pela fila de merge ([Concorrência](CONCURRENCY.md)) |
| Um orçamento por Work Item, não apenas por invocação | excedê-lo escala em vez de truncar |
| Taxa de escape registrada por gate | o campo existe e foi preenchido por achados reais ([Métricas](METRICS.md)) |

## `harness-doctor`

Cada linha acima é uma verificação, e o conjunto de verificações é um script. `scripts/harness-doctor.sh` as executa e informa o nível que o repositório realmente alcançou:

```
$ scripts/harness-doctor.sh

HL1  legível             9/9   ✓
HL2  verificável         8/10  ✗
     ✗ proteção de branch: a branch padrão aceita push direto
     ✗ canário: não há fixture reconhecidamente ruim para o gate de arquitetura
HL3  operável por time   2/9   ✗

Nível: HL1        Autonomia sustentada: A0–A1
Operando atualmente em: A2   ← teto excedido
```

A última linha é o resultado que importa. Comparar o nível calculado com a autonomia efetivamente concedida transforma a regra central da escada, de princípio em alarme — e é a verificação que nenhum repositório realiza sobre si mesmo por acidente.

Executá-lo na deep lane e de forma agendada. Em geral, um repositório não desce a escada por decisão; ele cai quando um grupo no `CODEOWNERS` é excluído, um filtro de caminho deixa de corresponder ou uma tool sai da imagem.

## Chegando ao próximo nível

A ordem não é uma preferência. Cada camada remove uma classe de falha que torna a seguinte mensurável, e construir fora de ordem produz controles nos quais não se pode confiar:

| Construir | Antes de | Porque |
|---|---|---|
| `AGENTS.md` e as rules | qualquer automação | um agente sem contrato de entrada improvisa, e então a improvisação está sendo automatizada |
| `verify.sh` e os sensores | CI | uma CI que não corresponde à verificação local produz falhas que ninguém consegue reproduzir |
| Os canários | conceder autonomia quando tudo está verde | um gate que nunca rejeitou nada não demonstrou que funciona |
| Evidência e atestação | vários agentes | com vários agentes em voo, "quem produziu isto e contra o quê" deixa de ser respondido de memória |
| Identidade e proteção de branch | merge sem acompanhamento | a separação de responsabilidades ou é estrutural ou não existe |
| Métricas | promover o nível | promoção baseada apenas em artefatos mede intenção, não capacidade |

**A primeira semana de um repositório vazio** são as duas primeiras linhas e nada mais: escrever `AGENTS.md` com um bloco de escalação honesto, escrever os dois arquivos de rule, tornar `verify.sh` real, instalar o sensor de pre-commit com secret scanning e adicionar a verificação de instalação das tools para que nada disso pare de rodar silenciosamente. Isso é HL1, sustenta A0–A1 e vale mais que um checklist HL3 preenchido por aspiração — porque no HL1 o teto e a prática estão de acordo, a única propriedade capaz de dar significado a qualquer nível.

---

*Próximo: [Agentes](AGENTES.md) — como um agente funciona e o catálogo dos 23 papéis.*
