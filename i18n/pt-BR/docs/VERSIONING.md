# Versionamento

O harness é o código de controle do repositório. É a única parte da árvore cuja modificação muda o significado de um trabalho já terminado: quando uma regra muda, toda aprovação concedida sob o texto anterior foi concedida sob um contrato que não existe mais.

Código comum não se comporta assim. Um refactor não desaprova retroativamente o pull request da semana passada. Uma mudança de regra desaprova, e um harness editado como documentação — melhorado no lugar, sem versão, sem registro — não consegue responder à primeira pergunta que uma auditoria faz: **sob quais regras isto foi aceito?**

## `HARNESS_VERSION` e o changelog

Dois arquivos, ambos em `.agent/`:

`HARNESS_VERSION` guarda uma única versão semântica. `CHANGELOG.md` registra, para cada versão, o que mudou, por quê e — o campo que distingue isso de um changelog comum — **o que aquilo invalida**.

Os números de versão carregam significado específico do harness:

| Incremento | Significa | Consequência para o trabalho em voo |
|---|---|---|
| **Major** | algo antes permitido passa a ser proibido, ou um gate novo bloqueia | work items abertos revalidam contra as novas regras antes do merge |
| **Minor** | uma regra, gate ou skill nova que não contradiz as anteriores | o trabalho novo adota; o trabalho em voo não é afetado |
| **Patch** | redação, exemplos, ponteiros, esclarecimento sem mudança de significado | nada |

A distinção entre minor e patch é a que mais se abusa. Se um agente razoável poderia ter se comportado de forma diferente antes e depois da edição, aquilo não é um patch — esclarecer uma regra ambígua a *muda*, porque a ambiguidade estava fazendo trabalho.

## O que uma mudança invalida

O `attestation.json` registra o SHA de cada arquivo de regra que o agente de fato leu ([Documentação](DOCUMENTATION.md#identidade-e-proveniência)). Esse campo é a chave de junção: dada uma regra alterada, ele identifica exatamente quais work items abertos foram produzidos sob o texto antigo, sem depender da memória de ninguém sobre quando a mudança entrou.

| O que mudou | Invalida |
|---|---|
| Um arquivo de regra | a evidência dos itens abertos cuja atestação registra o SHA antigo daquele arquivo |
| Um gate, ou a configuração de um gate | a evidência produzida pela trilha à qual aquele gate pertence |
| Um sensor | nada que já esteja no CI; a próxima execução local absorve |
| O modelo de permissão | qualquer operação em voo que dependa de um escopo que estreitou |
| Uma skill | nada retroativamente — uma skill é um procedimento, não um critério |
| O prompt do agente ou o modelo em uso | nada formalmente, mas fica registrado, porque é a primeira coisa que uma revisão de incidente pergunta |

As linhas do meio mostram por que essa maquinaria vale a pena: o raio de impacto de uma mudança de harness quase nunca é "tudo", e um time sem forma de calculá-lo ou revalida tudo — o que é caro o bastante para que as pessoas parem de mudar o harness — ou não revalida nada, que é o status quo que esta página existe para substituir.

## Mudar o harness

Uma mudança de harness segue a regra de [Gates](GATES.md#regras-inegociáveis-para-gates-com-agentes): ela é feita pelo dono do harness, fora do fluxo que a mudança afeta, e nunca por um agente dentro do fluxo que o gate avalia.

A entrada do changelog declara cinco coisas:

- **O que** mudou, como referência a um diff
- **Por quê** — a falha que motivou, idealmente um incidente ou escape específico
- **O que aquilo invalida**, usando a tabela acima
- **A transição** — como o trabalho em voo é tratado
- **Quem** aprovou

O campo de transição é o que determina se a mudança sobrevive ao contato com um time trabalhando. Uma regra nova aplicada retroativamente a tudo que está em voo bloqueia todos os itens abertos de uma vez e é revertida na mesma tarde. Os dois formatos que funcionam são o *grandfathering* — a regra vale para o trabalho iniciado depois da versão — e a *varredura agendada*, em que as violações existentes ficam registradas como dívida conhecida, com dono e prazo. Uma regra sem plano de transição é uma regra que será aplicada de forma inconsistente, e aplicação inconsistente é pior que regra nenhuma, porque remove do agente a capacidade de prever o que o gate vai fazer.

## Duas versões, não uma

Existe uma versão *do método* — este manifesto, suas camadas e seus contratos — e uma versão *do harness de um dado repositório*, que é a instanciação local dele. Elas se movem de forma independente: um repositório pode estar três versões de método atrás e ser perfeitamente consistente internamente, e adotar uma nova versão do método é uma migração deliberada, não um fato que passa a ser verdade quando alguém lê um documento.

O `HARNESS_VERSION` registra, portanto, as duas: a versão local do harness e a versão do método que ela implementa. A segunda é o que torna uma frota de repositórios comparável — ela responde quais repositórios adotaram um novo controle e quais não, uma pergunta que de outra forma só se responde lendo um por um.

---

*Próximo: [Métricas](METRICS.md) — como saber se algo disso está funcionando.*
