# Maturidade

[Gates](GATES.md#autonomia-progressiva-e-o-teto-do-harness) define a regra: o nível do harness é o teto da autonomia, nunca sua consequência. Os níveis de autonomia A0–A4 são definidos em [Checkpoints humanos](metodologia/02-checkpoints-humanos.md).

## Calculado, não declarado

Cada requisito abaixo é verificável mecanicamente. O nível do repositório é o mais alto cujos requisitos estejam todos satisfeitos no momento.

Duas restrições se aplicam:

- **O nível é o mínimo, não a média.** Um único controle HL2 ausente mantém o repositório no HL1.
- **O modo degradado reduz o nível enquanto durar.** Um gate em quarentena é um gate ausente ([Falha](FAILURE.md#declarando-um-modo-degradado)).

## HL1 — legível

O agente consegue entender o repositório e verificar o próprio trabalho localmente.

| Item | Verificável por |
|---|---|
| `AGENTS.md` na raiz com todos os seis blocos | o arquivo existe; cada cabeçalho está presente; escalação não está vazia |
| `docs/rules/architecture.md` e `docs/rules/testing.md` | ambos existem e não estão vazios |
| Tipo de mudança mapeado para níveis de teste obrigatórios | o mapeamento existe ([Rules](RULES.md#a-estratégia-de-testes-como-rule)) |
| `scripts/verify.sh` suporta `--staged`, `--affected`, `--full` | cada modo aceita `--help` ou uma execução simulada |
| Canário de verificação reconhecidamente ruim | `verify.sh` rejeita a fixture |
| Disponibilidade das tools verificada | remover uma tool obrigatória falha em vez de saltar |
| Sensor de pre-commit instalado por `.hooks/` | o bootstrap define `core.hooksPath=.hooks` |
| Secret scanning no pre-commit | a fixture com credencial falsa é rejeitada |
| `.agent/settings.json` define `allowed`, `ask`, `denied` e orçamento | o arquivo é interpretado; `allowed` não está vazio; famílias de comando não têm curinga |

## HL2 — verificável

Um ambiente limpo reproduz a verificação, e um revisor independente consegue auditar o resultado.

| Item | Verificável por |
|---|---|
| Fast lane e deep lane de CI separadas | ambas as configurações existem; o fluxo controlado não pode editá-las |
| Filtros de caminho da fast lane testados | o teste dos filtros roda ([Falha](FAILURE.md#verificando-o-verificador)) |
| Branch padrão protegida e checks obrigatórios | a API da plataforma rejeita push direto e informa os checks obrigatórios |
| `CODEOWNERS` cobre `.agent/`, `.hooks/`, CI e `docs/rules/` | cada caminho resolve para um owner existente |
| Evidence pack de `scripts/evidence.sh` | a saída contém `summary.md`, `verify-output.txt`, `gate-status.json` |
| Estados de gate explícitos | `passed`, `failed` e `skipped` podem ser produzidos |
| Escopo de MCP explícito | `.agent/mcps.json` existe ou zero MCPs autorizados são declarados |
| Caminhos de instrução exaustivos | `.agent/trust.md` os enumera |
| Versionamento do harness | `HARNESS_VERSION` é válido e `.agent/CHANGELOG.md` existe ([Versionamento](VERSIONING.md)) |
| Canários de arquitetura e segredos | ambos rodam de forma agendada e estão passando |

## HL3 — operável por um time

Vários agentes conseguem operar simultaneamente sem eliminar a separação de responsabilidades.

| Item | Verificável por |
|---|---|
| Identidade distinta por papel que escreve | as identidades diferem; os commits são assinados |
| O autor não pode aprovar a própria mudança | o gate de merge rejeita a tentativa |
| Atestação no merge | `attestation.json` ausente ou divergente bloqueia o merge |
| Skills do repositório | procedimentos recorrentes existem em `skills/<skill>/SKILL.md` |
| Agentes sem credencial de produção | o inventário atribui segredos de deploy apenas à identidade do pipeline |
| Baseline pós-deploy e critério de rollback | o critério está declarado e já foi exercitado |
| Frescor da evidência antes da integração | a fila de merge rejeita packs obsoletos ([Concorrência](CONCURRENCY.md)) |
| Orçamento por Work Item | o esgotamento escala em vez de truncar |
| Taxa de escape por gate | achados reais preenchem a métrica ([Métricas](METRICS.md)) |

## `harness-doctor`

`scripts/harness-doctor.sh` executa as verificações e compara o teto calculado com a autonomia real:

```text
HL1  legível             9/9   ✓
HL2  verificável         8/10  ✗
     ✗ proteção de branch: a branch padrão aceita push direto
     ✗ canário: não há fixture reconhecidamente ruim para o gate de arquitetura
HL3  operável por time   2/9   ✗

Nível: HL1        Autonomia sustentada: A0–A1
Operando atualmente em: A2   ← teto excedido
```

Execute-o na deep lane e de forma agendada. Owners excluídos, filtros de caminho obsoletos e tools ausentes podem reduzir o nível sem uma decisão explícita.

## Ordem de construção

A ordem de dependência é estrita:

1. `AGENTS.md` e rules antes da automação.
2. `verify.sh` e sensores locais antes da CI.
3. Canários antes de a autonomia depender de gates verdes.
4. Evidência e atestação antes de agentes concorrentes.
5. Identidade e proteção de branch antes de merge sem acompanhamento.
6. Métricas sustentadas antes da promoção de nível.

---

*Próximo: [Agentes](AGENTES.md) — como um agente funciona e o catálogo dos 23 papéis.*
