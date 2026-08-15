# Métricas

O método afirma que a autonomia aumenta por métrica. Esta página nomeia as métricas, porque uma regra que concede autoridade mediante evidência vale apenas tanto quanto a evidência que ela aceita — e "tem funcionado bem" não é evidência, é a ausência de sinal de que algo deu errado.

Uma distinção antes, já que as duas coisas são rotineiramente confundidas: as métricas DORA medem *entrega* — com que frequência, com que velocidade, com que segurança o time entrega. Elas não dizem nada sobre o harness. Um repositório pode melhorar todos os números DORA rebaixando os seus gates. O que segue mede o próprio sistema de verificação.

## A que mais importa

**Taxa de escape de gate** — defeitos que passaram por todos os gates e foram encontrados depois, por unidade de trabalho entregue.

É a única métrica que responde diretamente à pergunta que o harness existe para responder. Todo o resto é indicador antecedente dela, e um pipeline verde não substitui: um pipeline reporta o que os gates pegaram, e a taxa de escape reporta o que eles não pegaram.

Duas propriedades a tornam utilizável. Ela é medida *por ponto de escape* — encontrado na revisão, no staging, em produção, por um cliente — porque o custo difere em uma ordem de grandeza a cada passo e a tendência entre eles diz qual gate está enfraquecendo. E ela é atribuída ao gate que *deveria* tê-lo pego, não a quem escreveu a mudança: a saída da medição é um gate para consertar, nunca uma pessoa com quem conversar.

## O restante do painel

| Métrica | Lê-se como | Degrada em, se otimizada diretamente |
|---|---|---|
| **Taxa de escalação** | com que frequência o agente para e devolve a decisão | agentes que nunca param — veja abaixo |
| **Retrabalho após merge** | mudança reaberta ou corrigida em até N dias | work items menores e mais numerosos |
| **Latência de feedback por camada** | segundos no sensor, minutos na trilha rápida, horas na trilha profunda | verificações movidas para uma camada mais barata do que aquela à qual pertencem |
| **Taxa de skip e degradação** | gates reportados como `skipped`, execuções que precisaram de retry ([Falha](FAILURE.md)) | quarentenas que nunca são revisitadas |
| **Custo por Work Item aceito** | gasto total somando todos os agentes e rodadas, dividido pelos itens aceitos | qualidade rebaixada para deixar as execuções mais baratas |
| **Completude da evidência** | pacotes que um terceiro conseguiria reverificar sozinho | preenchimento de template |
| **Latência de revisão vs. profundidade de revisão** | tempo entre a mudança ficar pronta e um humano decidir | aprovações mais rápidas do que a mudança poderia ser lida |

A taxa de escalação é a mais mal lida. Uma taxa alta parece um agente incapaz de trabalhar sozinho, e às vezes é. A taxa perto de zero é a alarmante: ela significa ou que o repositório não tem ambiguidade — o que nenhum repositório tem — ou que as condições de escalação não estão disparando, e o agente está escolhendo uma interpretação e seguindo em frente toda vez que encontra uma contradição. As falhas que isso produz não aparecem neste painel. Elas aparecem na taxa de escape, semanas depois.

A última linha é o detector de carimbo automático. Uma aprovação emitida mais rápido do que o diff poderia plausivelmente ter sido lido não é uma aprovação; é um gargalo se resolvendo sozinho. Vale medir precisamente porque é o controle que degrada em silêncio conforme a vazão dos agentes sobe, e porque a correção nunca é "leia mais rápido" — é menos mudanças, melhor verificadas, chegando ao gate humano.

## Métricas governam o nível, nos dois sentidos

A escada de maturidade é uma afirmação sobre o que um repositório consegue verificar. Estas métricas são como a afirmação é conferida, e a conferência roda continuamente, não no momento da promoção:

**Promoção** exige que os artefatos do nível existam ([Maturidade](MATURITY.md)) *e* que o painel se sustente no nível atual por uma janela contínua. Artefatos sozinhos medem intenção — um gate que existe e nunca rejeitou nada não teve seu funcionamento demonstrado.

**Rebaixamento** é a metade que costuma faltar, e é o que torna a escada um controle em vez de uma cerimônia. Uma taxa de escape subindo, uma taxa de skip subindo, ou uma taxa de escalação que despenca são, cada uma, motivo para reduzir a autonomia até que a causa seja encontrada. Uma escada que só sobe registra histórico, não capacidade.

## O que não medir

Três tentações, cada uma das quais produz um sistema pior do que não medir nada:

**Ranking por agente.** Comparar papéis de agente por vazão ou contagem de defeitos otimiza a unidade errada. A saída deste painel é uma mudança em um contrato, uma regra, uma ferramenta ou um gate — o harness é o que melhora, e um agente é sempre apenas evidência sobre ele. É o mesmo compromisso que o método assume em relação às pessoas, pelo mesmo motivo.

**Volume.** Commits, linhas, pull requests, tokens consumidos. Todos eles sobem quando o sistema piora, e agentes conseguem produzir qualquer quantidade de qualquer um deles sob demanda.

**Taxa de aprovação de gate como sinal de saúde.** Um gate que sempre passa ou não está verificando nada ou está sendo contornado, e ambos parecem excelência num dashboard.

## De onde vêm os números

A maior parte do painel já é registrada pela maquinaria das páginas anteriores, e é isso que a torna viável: o `gate-status.json` carrega as taxas de skip e degradação, o `attestation.json` carrega as regras e o modelo sob os quais cada item foi produzido, o pacote de evidências carrega a saída da verificação, e o histórico do controle de versão carrega retrabalho e latência de revisão. O que precisa ser acrescentado deliberadamente é o escape — alguém precisa registrar, quando um defeito é encontrado, qual gate deveria tê-lo pego. Esse único campo é a diferença entre um painel que descreve atividade e um que mede verificação.

---

*Próximo: [Maturidade](MATURITY.md) — o que cada nível exige, e como descobrir onde um repositório de fato está.*
