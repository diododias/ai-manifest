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

## Condições de escalonamento

O agente deve parar e devolver a decisão diante de qualquer uma das situações abaixo:

- Requisito contraditório ou sem owner definido
- Confiança abaixo do threshold declarado em `settings.json`
- Duas ou mais tentativas de correção sem progresso
- Mudança fora do escopo aprovado
- Necessidade de nova permissão ou acesso externo
- Falha não reproduzível ou evidência inconsistente
- Decisão irreversível ou impacto não calculável
- Divergência entre agentes sem critério objetivo de desempate

## A estratégia de testes como rule

A estratégia de testes merece destaque porque é a rule que os gates traduzem diretamente em bloqueio. A escada completa é:

```
unitários → arquitetura → integração → contrato → end-to-end → acessibilidade → mutação
```

A rule define quais níveis são obrigatórios por tipo de mudança. Sem esse mapeamento, o agente ou escreve testes de menos — e o gate reprova tarde — ou escreve testes demais, elevando o custo por entrega sem ganho de segurança.
