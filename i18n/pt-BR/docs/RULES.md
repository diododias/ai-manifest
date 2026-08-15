# Rules

Rules descrevem estado desejado, não procedimento. "Módulos de domínio não importam de infraestrutura" é rule. "Para adicionar um adapter, crie a interface em X e a implementação em Y" é skill. A confusão entre os dois produz rules longas que ninguém lê e skills vagas que não se consegue executar.

Toda rule carrega o motivo junto. Isso não é cortesia editorial: um agente que conhece a razão de uma regra decide corretamente no caso de borda que a regra não previu, enquanto um agente que só conhece a regra ou a aplica cegamente ou a ignora.

## Arquivos de rules

As rules se dividem em arquivos separados, cada um cobrindo uma frente distinta. Essa separação é uma decisão de orçamento de contexto: rules são lidas sob demanda conforme a tarefa, não carregadas inteiras em toda execução.

| Arquivo | Define |
|---|---|
| `docs/rules/architecture.md` | módulos, fronteiras, dependências permitidas e proibidas |
| `docs/rules/coding.md` | convenções, padrões aceitos, naming, injeção de dependência |
| `docs/rules/testing.md` | níveis obrigatórios por tipo de mudança |
| `docs/rules/security.md` | dados, secrets, autenticação, privacidade |
| `docs/rules/operations.md` | SLOs, observabilidade, rollout, rollback |

O que `security.md` precisa responder não é uma declaração geral de política, mas quatro perguntas operacionais: quais classes de dados existem neste repositório e quais delas o agente pode ler; onde vivem os secrets e por que o agente nunca possui uma credencial de produção; contra o que um teste roda quando os dados reais são regulados (dados sintéticos ou anonimizados, nunca produção); e quais mudanças são relevantes para a segurança a ponto de exigir uma pessoa revisora nomeada. Um `security.md` que não responde a essas perguntas é um documento de política, não um arquivo de rule.

## `AGENTS.md` — o contrato de entrada

O `AGENTS.md` é lido antes de qualquer ação, o que torna cada linha dele um custo fixo por execução. Ele responde o que o agente precisa para agir corretamente na primeira tentativa, e delega o resto por ponteiro. Seus blocos são:

| Bloco | Conteúdo | Erro comum |
|---|---|---|
| Identidade | o que o serviço faz e para quem, em três frases | reescrever o pitch do produto |
| Comandos | instalar, buildar, testar, verificar, rodar local | listar comandos que ninguém usa mais |
| Fronteiras | o que não pode ser alterado sem autorização | descrever a arquitetura inteira |
| Verificação | o que precisa passar antes de considerar pronto | duplicar a configuração de CI |
| Escalonamento | as condições em que se para e devolve a decisão | omitir — é o bloco mais esquecido |
| Ponteiros | onde ficam rules, ADRs, skills e evidências | inlinar o conteúdo apontado |

O bloco de escalonamento é o que mais falta e o que mais importa. Sem ele, um agente diante de requisito contraditório escolhe uma interpretação e segue — e a escolha só aparece na revisão, quando o trabalho já foi feito.

## Condições de escalação

O agente deve parar e devolver a decisão diante de qualquer uma das situações abaixo:

- Requisito contraditório ou sem responsável definido
- Duas ou mais tentativas de correção sem progresso sobre a mesma falha
- Mudança fora do escopo aprovado
- Necessidade de nova permissão ou acesso externo
- Falha não reproduzível ou evidência inconsistente
- Decisão irreversível ou cujo raio de impacto não pode ser calculado — ver [Reversibilidade](#reversibilidade-é-um-requisito-de-entrada)
- Divergência entre agentes sem critério objetivo de desempate
- Orçamento do Work Item esgotado antes do gate de conclusão — ver [Orçamento](BUDGET.md)

Toda condição desta lista pode ser observada por uma terceira pessoa do lado de fora: um responsável ausente, uma falha repetida, um diff que sai do escopo declarado. Isso é deliberado. **A confiança autorreportada por um modelo não é critério de escalação** — ela não é calibrada, não é comparável entre modelos, e um limiar numérico em um arquivo de configuração produz a aparência de um controle sem seu mecanismo. A escalação é disparada por fatos sobre o trabalho, nunca por quão seguro o agente diz estar.

## Reversibilidade é um requisito de entrada

Rollback costuma ser tratado como preocupação pós-deploy. Para um repositório operado por agentes, ele é um critério de admissão: se uma mudança pode ser produzida autonomamente depende de como ela será desfeita.

| Classe | Caminho de reversão | Regra |
|---|---|---|
| Mudança apenas de código, protegida por testes existentes | reverter o commit | autônoma |
| Mudança de comportamento que alcança usuários | desligar a flag, depois reverter | a flag é precondição da mudança, não trabalho posterior |
| Mudança aditiva de schema | reverter o código, manter a coluna | autônoma apenas se a migração for retrocompatível |
| Mudança destrutiva de schema ou dados | restaurar a partir de backup | nunca autônoma — responsável nomeado mais ADR |
| Mudança em uma rule, sensor, gate ou configuração de CI | reverter e verificar novamente o que passou no intervalo | responsável pelo harness, fora do fluxo avaliado pelo gate |

A regra sob a tabela: **uma mudança que não pode ser desfeita com um comando exige autorização humana e um ADR que registre por que ainda assim foi aceita.** Um agente que não consegue classificar a própria mudança em uma dessas linhas já atingiu uma condição de escalação.

## A estratégia de testes como rule

A estratégia de testes merece destaque porque é a rule que os gates traduzem diretamente em bloqueio. A escada completa é:

```
unitário → arquitetura → integração → contrato → end-to-end → acessibilidade → mutação
```

A rule define quais níveis são obrigatórios por tipo de mudança. Sem esse mapeamento, o agente ou escreve testes de menos — e o gate reprova tarde — ou escreve testes demais, elevando o custo por entrega sem ganho de segurança.

O mapeamento pertence a `docs/rules/testing.md` e é específico de cada repositório. A matriz abaixo é o formato de referência — um ponto de partida para adaptar, não um padrão para copiar:

| Tipo de mudança | Obrigatórios | Sob demanda | Roda em |
|---|---|---|---|
| Refactor interno, sem mudança de comportamento | unitário, arquitetura | mutação no módulo tocado | pre-commit, pre-push |
| Nova rule de domínio | unitário, arquitetura | — | pre-commit, pre-push |
| Fronteira de módulo nova ou alterada | unitário, arquitetura | — | pre-push, deep lane |
| Mudança em API ou evento publicado | contrato, integração | end-to-end | deep lane |
| Mudança em persistência ou schema | integração, contrato | end-to-end | deep lane |
| Mudança em fluxo visível ao usuário | end-to-end, acessibilidade | — | deep lane |
| Mudança em autenticação, autorização ou tratamento de secrets | unitário, integração, contrato | mutação no módulo tocado | deep lane, pessoa revisora nomeada |
| Atualização de dependência | a escada completa para os paths afetados | — | deep lane |

Duas propriedades tornam essa matriz utilizável, em vez de decorativa. Cada linha nomeia o gate em que o nível roda, portanto o [critério de posicionamento](GATES.md#onde-cada-check-pertence) já está resolvido e o agente não o deriva novamente em cada tarefa. E a coluna "Sob demanda" existe para que um nível caro seja um pedido deliberado, com motivo declarado, nunca um padrão que infla toda entrega.

---

*Próximo: [Sensors](SENSORS.md) — os checks locais que rodam antes de o código sair da máquina.*
