# Orçamento

Todo gate descrito até aqui bloqueia algo que está errado. Este bloqueia algo que apenas não vale a pena — e é por isso que ele é a restrição mais frequentemente esquecida, e a única que falha para cima enquanto todos os indicadores seguem verdes.

Um agente que passa quatro horas em loop numa correção de duas linhas não quebrou regra nenhuma. Os testes passam, o diff está limpo, o pacote de evidências está completo. Nada na escada de verificação tem opinião sobre o fato de que a mudança custou mais que o problema.

## Quatro dimensões, não uma

| Dimensão | Limita | Acaba como |
|---|---|---|
| **Custo** | gasto por Work Item | a pergunta financeira, e a mais fácil de medir |
| **Turnos** | iterações antes de parar | o sinal de não convergência — um agente que não progride em geral continua tentando |
| **Tempo de relógio** | tempo decorrido antes de parar | uma ferramenta travada ou uma espera externa que nunca vai retornar |
| **Contexto** | quanto da janela a sessão já consumiu | perda de coerência, que aparece como degradação de qualidade e não como erro |

A última é a que se comporta diferente de um orçamento e a que mais importa para qualidade. Custo, turnos e tempo degradam linearmente e param num limite. Contexto degrada de um jeito que o agente não consegue autorreportar: uma sessão que consumiu a maior parte da janela não anuncia que começou a perder o fio, ela simplesmente passa a contradizer decisões que ela mesma tomou antes, na mesma tarefa. Tratar contexto como orçamento com um limiar — salvar o estado num checkpoint, começar limpo, levar adiante as conclusões em vez do transcript — converte um problema invisível de qualidade num problema operacional visível.

## Esgotamento é uma escalação, não um crash

Um orçamento sem comportamento de esgotamento definido é pior que orçamento nenhum, porque produz o seu estrago no momento menos recuperável: no meio de uma mudança, no meio de uma migração, com metade de um refactor aplicada.

Três comportamentos são possíveis, e o padrão é o terceiro:

**Abortar.** Descartar e parar. Correto apenas onde o trabalho é genuinamente sem estado, o que depois de qualquer arquivo escrito raramente é verdade.

**Entregar parcial.** Legítimo, mas só contra um contrato: o trabalho precisa estar num estado coerente por si só — compila, passa os gates daquilo que de fato contém e não deixa nada pela metade. Entrega parcial sem esse contrato não é uma entrega, é uma entrega interrompida.

**Escalar.** Parar, chegar a um estado retomável e devolver a uma pessoa o que foi feito, o que falta e qual era o obstáculo. Este é o padrão porque é o único que preserva a opção de escolher os outros dois.

O requisito comum aos três é que **o esgotamento é planejado, não detectado**. Um agente que se aproxima do seu limite precisa reservar orçamento suficiente para parar de forma limpa — escrevendo o estado, produzindo a evidência, deixando a árvore consistente. Um limite descoberto no momento em que é ultrapassado deixa exatamente a bagunça que ele deveria evitar. É por isso que o esgotamento de orçamento está listado como [condição de escalação](RULES.md#condições-de-escalação).

## O que degrada, e o que nunca degrada

Sob pressão sempre há algo a abrir mão. A ordem não é negociável:

| Abra mão primeiro | Nunca abra mão |
|---|---|
| Escopo — entregue menos, completo | Verificação do que foi entregue |
| Níveis de teste opcionais, marcados como "sob demanda" | Níveis de teste que o tipo de mudança torna obrigatórios |
| Exploração e alternativas consideradas | O pacote de evidências |
| Polimento, refactor adjacente à mudança | A escalação, quando uma condição é atendida |

A linha por baixo disso: **reduza o que é entregue, nunca o quão bem aquilo é verificado.** Uma mudança mais barata e não verificada não é uma mudança mais barata — ela transfere o custo para quem encontrar o defeito, a uma taxa de câmbio pior. Um agente que não consegue completar uma mudança dentro do orçamento *e* verificá-la atendeu a uma condição de escalação, não encontrou um motivo para pular o gate.

Este é também o ponto em que o orçamento interage com autonomia. Rebaixar a verificação para caber no orçamento rebaixa o nível de harness daquela mudança, e junto com ele a autonomia à qual a mudança era elegível ([Gates](GATES.md#autonomia-progressiva-e-o-teto-do-harness)).

## Orçamentos compõem, e loops adversariais multiplicam

Um orçamento por agente não é um orçamento por Work Item. Um loop com um agente produtor, dois revisores adversariais e uma rodada de revisão consome o orçamento do item várias vezes, e cada participante está individualmente dentro do seu limite.

Declaram-se, portanto, dois orçamentos:

- **Por invocação de agente** — limita uma única execução e é o que o `.agent/settings.json` carrega.
- **Por Work Item** — limita o total somado de todos os agentes e todas as rodadas que o item consome, e é o que reflete quanto o trabalho valia.

Loops também precisam de uma condição de parada que não dependa de sucesso. Uma rodada adversarial sempre consegue achar mais uma objeção; um crítico sempre consegue pedir mais uma revisão. Sem um número máximo de rodadas, "convergiu" é indistinguível de "ainda rodando", e o estado final natural de um loop de revisão sem limite é o orçamento acabar em vez de o trabalho ficar certo. O limite de rodadas é um controle de convergência primeiro e um controle de custo depois.

## Declarar e observar

Os limites vivem no `.agent/settings.json` ([Permissões](PERMISSIONS.md)), porque um orçamento é um limite operacional como qualquer outro e mudá-lo é uma mudança de harness.

Defini-los exige dados que o repositório não terá no primeiro dia. Comece medindo: o custo, os turnos e o tempo dos work items que foram aceitos sem incidente dão a distribuição, e o limite vai na borda superior dela, não na média — um orçamento fixado na média interrompe metade do trabalho saudável. **Custo por Work Item aceito** — e não custo por execução, que melhora sempre que a qualidade cai — é o número que diz se o sistema está ficando mais barato ou apenas mais rápido em produzir retrabalho ([Métricas](METRICS.md)).

---

*Próximo: [Versionamento](VERSIONING.md) — o que acontece com aprovações passadas quando o próprio harness muda.*
