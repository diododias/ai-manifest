# Concorrência

Quase todo harness pode ser desenhado como se um agente trabalhasse em um Work Item por vez. Essa premissa sobrevive ao primeiro piloto e falha em produção, porque a razão de operar agentes é justamente que vários deles rodam ao mesmo tempo.

Concorrência não introduz gates novos. Ela ataca o significado dos que já existem: **um gate verifica uma mudança contra uma base, e com vários agentes em voo a base deixa de ser aquilo que é mergeado.**

## Evidência tem prazo de validade

Um pacote de evidências é uma afirmação sobre um estado específico do mundo: esta mudança, sobre este commit de base, satisfez estas verificações. A afirmação é verdadeira quando produzida. Ela continua colada à mudança enquanto a base se move por baixo.

O Git resolve a parte textual disso e nada mais. Duas mudanças podem mergear limpas, passar em todas as verificações individualmente e estar erradas juntas — uma adiciona um ponto de chamada a uma função cujo contrato a outra estreitou, uma insere uma linha numa tabela que a outra acabou de começar a ler, uma relaxa uma validação da qual a outra agora depende. **Nenhum marcador de conflito aparece, porque nada conflita textualmente.** O agente não errou; a verificação simplesmente respondeu a uma pergunta sobre uma base que não existe mais.

Frescor é, portanto, uma propriedade que o gate de merge precisa verificar, não uma cortesia:

| Desde que a evidência foi produzida | Veredito |
|---|---|
| a base não se moveu | evidência atual |
| a base se moveu, sem sobreposição com o que a mudança tocou ou leu | atual, o merge segue |
| um arquivo que a mudança tocou também mudou | vencida — rode de novo a trilha afetada |
| um contrato compartilhado, schema ou interface pública mudou | vencida — rode de novo a trilha afetada, havendo ou não sobreposição de diffs |
| uma regra, gate ou dependência mudou | vencida — rode a trilha completa de novo ([Versionamento](VERSIONING.md)) |
| a janela de frescor expirou | vencida, independentemente do que mudou |

A janela existe porque "sem sobreposição" é calculado a partir do que a ferramenta consegue enxergar, e o conjunto de coisas de que uma mudança realmente depende é sempre maior que o conjunto de arquivos que ela edita. Uma janela medida em horas — curta o bastante para que o mundo não tenha se movido, longa o bastante para que uma revisão normal não expire — limita o quanto a análise de sobreposição tem permissão de errar.

A regra que decorre disso: **o último gate antes da integração revalida contra o estado no qual se está integrando, não contra o estado do qual o trabalho partiu.** Uma fila de merge que constrói cada mudança sobre a cabeça da fila é a implementação padrão, e é a razão pela qual filas de merge existem também para times humanos — agentes apenas elevam a frequência com que o problema ocorre.

## Reivindicar trabalho

Dois agentes que pegam o mesmo Work Item produzem duas soluções, ambas válidas, e nenhuma delas errada de um jeito que um gate consiga detectar. O desperdício fica invisível até a revisão, onde uma pessoa descobre que a segunda implementação existe.

Uma reivindicação é um lease, não um lock: ela nomeia o agente, o Work Item, a região do código que ele espera tocar e um vencimento. O vencimento é o que distingue um lease de um deadlock — um agente que morre no meio da tarefa não pode segurar uma região para sempre, e nenhum humano deveria ter que liberá-la à mão.

| Elemento | Por quê |
|---|---|
| O Work Item | evita trabalho duplicado sobre o mesmo objetivo |
| A região declarada | expõe a colisão antes do trabalho, não no merge |
| O vencimento | um agente que travou libera automaticamente |
| O commit de base | a entrada da verificação de frescor acima |

A região declarada é necessariamente aproximada — um agente não sabe tudo o que vai tocar antes de começar. Ainda assim vale declarar, porque a falha que isso evita é a cara: dois agentes refatorando o mesmo módulo em direções incompatíveis por uma hora cada.

## Ordenar o que não pode ser paralelo

Algumas sequências são seriais independentemente de quantos agentes estejam disponíveis. Tornar a restrição explícita é mais barato que descobri-la durante um merge:

- **Uma migração e o código que depende dela.** A ordem expand-migrate-contract é uma sequência, e cada passo é uma integração separada.
- **Uma mudança de contrato e seus consumidores.** O produtor mergeia primeiro a versão compatível; o consumidor vem depois; a remoção é uma terceira mudança.
- **Qualquer coisa que toque o próprio harness.** Uma mudança de regra, gate ou permissão serializa contra tudo que está em voo, porque invalida a evidência de todos.

O terceiro caso é o que surpreende. Uma mudança de harness não é uma mudança normal com um revisor diferente — é uma mudança que altera retroativamente o que todo Work Item aberto provou. É por isso que ela passa pelo dono do harness fora do fluxo normal, e por isso que ela é versionada.

## O que o trio deve ao sistema

Três coisas seguem sendo decisões humanas por mais agentes que estejam rodando, porque cada uma exige conhecer a intenção por trás do trabalho, e não o seu diff:

**Quantos agentes podem segurar o mesmo subsistema.** O paralelismo tem um teto por área do código, abaixo do teto imposto pelo orçamento.

**Quais conflitos são resolvidos e quais são escalados.** Um conflito textual pode ser resolvido por quem tocou por último. Uma divergência semântica — dois agentes que implementaram leituras incompatíveis do mesmo requisito — é um defeito de especificação, e mergear qualquer um dos lados esconde isso.

**Se o trabalho duplicado é descartado ou reconciliado.** Descartar costuma ser o certo e nunca é automático.

Nada disso pode ser inferido a partir do repositório, e é por isso que pertence à camada de workspace e não a esta. O que pertence aqui é a maquinaria que torna essas decisões visíveis a tempo de serem tomadas: leases, frescor e um ponto de integração ordenado.

---

*Próximo: [Orçamento](BUDGET.md) — a restrição que falha para cima quando nada está quebrado.*
