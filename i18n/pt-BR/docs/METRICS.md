# Métricas

Métricas para uma squad AI-first precisam responder a uma pergunta prática: **o time está transformando ideias em valor para o usuário mais rapidamente sem transferir custo para qualidade, operação ou pessoas?** Nenhum número isolado responde. A IA pode aumentar o output enquanto a estabilidade cai, reduzir o tempo de codificação enquanto a fila de revisão cresce ou diminuir o custo do modelo enquanto a correção humana fica mais cara.

Esta página define um sistema equilibrado de medição para uma squad de produto. Ele combina outcomes de produto, fluxo, entrega de software, confiabilidade, qualidade, colaboração humano-IA, economia e saúde da equipe. O objetivo é melhorar o sistema, nunca ranquear pessoas ou maximizar atividade.

## Defina primeiro o contrato da medição

Toda métrica precisa de um contrato antes de entrar em um dashboard:

| Campo | O que precisa estar explícito |
|---|---|
| **Pergunta** | a decisão que a métrica deve orientar |
| **Definição e fórmula** | numerador, denominador, regras de inclusão e o que conta como sucesso ou falha |
| **Escopo** | produto, serviço, ambiente, tipo de trabalho e classe de risco representados |
| **Fonte** | sistema de registro e como os eventos são correlacionados |
| **Janela e estatística** | janela de calendário, fuso horário, mediana ou percentil e tratamento de dados parciais |
| **Owner e resposta** | quem investiga e qual ação uma mudança relevante pode disparar |
| **Guardrail** | o sinal complementar que impede otimização local |

Altere uma definição apenas para dados futuros e anote a mudança na série temporal. Uma tendência montada com definições diferentes não é uma tendência.

Cinco regras operacionais importam:

1. Leia **contagens e taxas em conjunto**. Três implantações com falha significam algo diferente entre cinco implantações e entre quinhentas.
2. Segmente antes de comparar: serviço, risco, tipo de trabalho e grau de envolvimento da IA podem explicar uma mudança que a média global esconde.
3. Prefira a mediana (P50) e percentis de cauda, como P85, para tempo. A média esconde os poucos itens que passam semanas bloqueados.
4. Compare a squad com sua própria baseline e sua meta. Benchmarks da indústria são contexto, não contrato de desempenho.
5. Trate dados ausentes, atrasados ou impossíveis de correlacionar como falha visível de qualidade da métrica, nunca como zero.

## O dashboard mínimo da squad

Um primeiro dashboard útil cabe em uma tela. Ele contém um outcome, guardrails e sinais de diagnóstico suficientes para explicar os movimentos:

| Área | Sinal mínimo | Pergunta respondida |
|---|---|---|
| **Produto** | um outcome principal mais um guardrail de dano ou qualidade | a mudança entregue ajudou o usuário sem causar um efeito colateral inaceitável? |
| **Entrega** | total de implantações, implantações bem-sucedidas e implantações com falha | quanto chegou à produção e quanto exigiu intervenção imediata? |
| **Estabilidade** | taxa de falha em mudanças e tempo de recuperação de implantação com falha | com que frequência a entrega desestabilizou o serviço e com que rapidez a squad se recuperou? |
| **Fluxo** | cycle time P50/P85, idade do trabalho em andamento e tempo bloqueado | onde o trabalho espera, especialmente na cauda longa? |
| **Qualidade** | defeitos que escaparam por severidade e taxa de retrabalho | quanto trabalho considerado pronto retornou como correção? |
| **Colaboração com IA** | aprovação independente na primeira passagem, esforço humano de correção e qualidade da escalação | a IA reduz o esforço total sem deixar de ser governável? |
| **Economia** | custo por Work Item aceito | o sistema inteiro está mais eficiente, não apenas cada invocação? |
| **Saúde da squad** | carga de revisão, toil e pulso curto de atrito | a velocidade está sendo financiada por sobrecarga ou trabalho manual oculto? |

Comece com esses sinais e só acrescente uma métrica quando uma decisão recorrente não puder ser tomada sem ela.

Aqui, um **Work Item** é uma unidade de mudança de produto ou engenharia aceita de forma independente e com critérios explícitos de conclusão. Mantenha essa unidade estável o suficiente para permitir comparações entre períodos.

## Entrega e estabilidade

A família de implantação é o núcleo operacional. Defina-a por serviço em produção ou produto publicável; misturar um serviço web diário com um release mobile trimestral destrói a comparabilidade.

| Métrica | Definição | Uso |
|---|---|---|
| **Total de implantações** | contagem de implantações em produção ou releases para usuários na janela | fornece o denominador e mostra a cadência de entrega |
| **Frequência de implantação** | total de implantações por unidade de tempo, ou intervalo típico entre implantações | normaliza a cadência entre janelas de relatório |
| **Implantações bem-sucedidas** | implantações concluídas sem degradação causada pela mudança que exija correção imediata | distingue cadência útil de trabalho repetido de recuperação |
| **Implantações com falha** | implantações que causam degradação e exigem rollback, hotfix, fix-forward, patch ou intervenção imediata equivalente | expõe a carga operacional absoluta criada pelas mudanças |
| **Taxa de falha em mudanças** | `implantações com falha / total de implantações × 100` | torna a falha comparável entre janelas com volumes de implantação diferentes |
| **Lead time da mudança** | tempo entre o commit e a mudança operando com sucesso em produção; reportar P50 e P85 | mostra a rapidez com que trabalho commitado chega aos usuários e revela a cauda lenta |
| **Tempo de recuperação de implantação com falha** | tempo entre uma degradação causada por mudança e a restauração do serviço; reportar P50 e P85 | mede o fluxo de valor da recuperação, não a duração genérica de incidentes |
| **Taxa de retrabalho de implantação** | `implantações corretivas não planejadas / total de implantações × 100` | mostra quanto da capacidade de implantação corrige defeitos visíveis ao usuário |

Contagens, taxas e tempos precisam ser lidos juntos. Se as implantações dobrarem de 50 para 100 e as falhas subirem de 2 para 3, a **quantidade de implantações com falha** piorou, enquanto a **taxa de falha em mudanças** melhorou de 4% para 3%. A conclusão correta não é “a qualidade melhorou” nem “a qualidade piorou” isoladamente: a squad entregou com mais frequência e menor probabilidade de falha por implantação, mas criou mais eventos absolutos de recuperação. Impacto no usuário, severidade e tempo de recuperação determinam se o trade-off é aceitável.

O modelo atual de entrega do DORA agrupa lead time da mudança, frequência de implantação e tempo de recuperação de implantação com falha como throughput, e taxa de falha em mudanças mais taxa de retrabalho de implantação como instabilidade. As definições acima seguem esse modelo e preservam as contagens brutas necessárias à operação da squad.

## Fluxo e previsibilidade

As métricas de entrega começam no commit, mas muitos atrasos ocorrem antes. Métricas de fluxo expõem todo o caminho, do trabalho comprometido ao outcome observado.

| Métrica | Definição | Interpretação saudável |
|---|---|---|
| **Cycle time ponta a ponta** | selecionado/iniciado até aceito em produção; P50 e P85 | centro e cauda longa caem sem aumento das taxas de falha |
| **Idade do trabalho em andamento** | idade atual de cada item ativo | itens antigos provocam esforço conjunto ou redução de escopo antes de virarem estoque invisível |
| **Proporção de tempo bloqueado** | `tempo bloqueado / cycle time total × 100` | revela filas de dependência e decisão |
| **Eficiência de fluxo** | `tempo ativo / cycle time total × 100` | distingue esforço de trabalho de tempo de espera |
| **Tempo de espera por revisão** | pronto para revisão até a primeira revisão substantiva | detecta a fila humana criada quando a IA eleva o throughput de mudanças |
| **Tamanho do lote** | mudanças, arquivos ou comportamentos publicáveis de forma independente por item ou implantação | lotes menores e reversíveis devem melhorar feedback e recuperação |
| **Previsibilidade** | proporção de itens concluídos dentro da expectativa de serviço da sua classe | sustenta planejamento sem transformar estimativas em cotas individuais |

Throughput ou story points isolados não são métricas de outcome. Fechar mais itens pode significar tickets menores, divisão artificial ou mais trabalho de baixo valor.

## Qualidade, confiabilidade e segurança

| Métrica | Definição | Segmentação importante |
|---|---|---|
| **Defeitos que escaparam** | defeitos encontrados depois da etapa que deveria detectá-los | etapa de detecção, severidade, modo de falha e serviço afetado |
| **Taxa de retrabalho pós-aceite** | itens aceitos que foram reabertos ou corrigidos de forma material em até `N` dias / itens aceitos | melhoria planejada versus correção |
| **Aprovação de gate na primeira passagem** | itens aceitos por um gate independente sem correção material / itens avaliados | tipo de gate, risco da mudança e envolvimento da IA |
| **Cumprimento do objetivo de nível de serviço (SLO) e consumo de error budget** | confiabilidade percebida pelo usuário contra um objetivo acordado | serviço, jornada do usuário e janela de consumo |
| **Taxa de incidentes recorrentes** | incidentes que repetem uma causa conhecida / incidentes | classe de causa e conclusão da ação corretiva anterior |
| **Taxa de escape de segurança** | vulnerabilidades confirmadas encontradas depois do controle que deveria capturá-las | severidade, controle e exposição |
| **Taxa de verificação flaky** | resultados não determinísticos de checks / execuções de checks | suíte, owner e tempo até quarentena ou correção |

Um pipeline verde só demonstra que os checks executados passaram. Combine taxas de aprovação com escapes, canários ou testes reconhecidamente ruins para que um check que silenciosamente não verifica nada não pareça saudável.

## Valor de produto e aprendizado

Toda squad precisa de um outcome principal ligado ao comportamento ou resultado de usuário que existe para melhorar. A métrica exata depende do produto: conclusão bem-sucedida de tarefa, ativação, uso retido, conversão, tempo poupado, redução de erros ou outro resultado observável. Combine-a com guardrails como reclamações, abandono, acessibilidade, latência, privacidade ou contatos de suporte.

Sinais úteis de produto e aprendizado incluem:

| Métrica | O que mostra |
|---|---|
| **Movimento do outcome** | mudança no resultado de usuário ou negócio selecionado contra a baseline |
| **Adoção com uso bem-sucedido** | usuários que não apenas acessam a capacidade, mas concluem a tarefa pretendida |
| **Taxa de decisão de experimentos** | experimentos que produzem uma decisão de manter, alterar ou parar / experimentos concluídos |
| **Tempo até aprendizado validado** | hipótese registrada até decisão sustentada por evidências |
| **Carga de suporte após mudança** | contatos de suporte ou reclamações atribuíveis a um release |

Frequência de implantação sem movimento do outcome descreve uma fábrica de funcionalidades eficiente, não uma squad de produto de alto desempenho.

## Colaboração humano-IA

Primeiro classifique o envolvimento da IA em cada Work Item. Uma escala prática é `nenhum`, `assistido` (a IA propõe sob execução direta), `delegado` (a IA conclui uma tarefa delimitada) e `coordenado` (a IA orquestra várias tarefas delimitadas). Esse campo é contexto para análise, não uma meta a maximizar.

| Métrica | Definição | O que observar |
|---|---|---|
| **Dependência de IA por atividade** | proporção de atividades relevantes nas quais a squad depende de IA para concluir o trabalho | dependência é mais significativa que prompts, mensagens ou ativação de licenças |
| **Aprovação independente na primeira passagem** | outputs com IA aceitos sem correção material por um controle separado | segmente por tarefa e risco; nunca permita autoaprovação do produtor |
| **Esforço humano de correção** | tempo de revisão, reparo e esclarecimento por item com IA aceito | captura “geração rápida, limpeza lenta” |
| **Conclusão autônoma dentro do escopo** | itens delegados concluídos e aceitos sem expansão não autorizada / itens delegados | combine com sinais de qualidade e escalação |
| **Qualidade da escalação** | escalações necessárias feitas a tempo, além das perdidas e desnecessárias | taxa próxima de zero pode indicar adivinhação silenciosa, não maturidade |
| **Sucesso na recuperação de contexto** | tarefas que recuperaram contexto autoritativo atual / tarefas que o exigiam | combine com incidentes de contexto obsoleto ou conflitante |
| **Cobertura de evidência e proveniência** | itens aceitos com inputs, outputs, checks e owner responsável rastreáveis / itens aceitos | cobertura sem validade independente vira preenchimento de template |
| **Exceções de segurança de IA** | violações e quase incidentes de permissão, privacidade, segredo, escopo ou política | reporte contagem absoluta e severidade; não normalize violações graves até que desapareçam |

Compare classes de envolvimento da IA em outcome, cycle time, falha, retrabalho, esforço humano e custo. “O trabalho assistido por IA é mais rápido” é incompleto se tempo de revisão, escape de defeitos ou carga de suporte aumentaram.

## Economia e saúde da squad

**Custo por Work Item aceito** é a principal unidade econômica:

`(modelo + plataforma + CI + revisão humana + correção + custo alocado de incidentes) / Work Items aceitos`

Mantenha a alocação de infraestrutura pragmática; consistência direcional vale mais que falsa precisão contábil. Acompanhe também custo de modelos e ferramentas por atividade, desperdício com retries e custo de trabalho com falha ou abandonado, mas nunca otimize o custo da invocação ignorando correção e incidentes.

A saúde da squad fornece o guardrail que a telemetria do sistema não consegue oferecer:

- pulso curto e regular sobre atrito, carga cognitiva e confiança no sistema de entrega;
- tempo gasto em toil, interrupções e espera evitável;
- carga e concentração de revisão, para que uma pessoa especialista não se torne o gate invisível de todo output de IA;
- distribuição de conhecimento e capacidade de operar sem uma única pessoa específica;
- tempo protegido para aprendizado, manutenção e melhoria.

Use esses sinais no nível da squad, com segurança psicológica e tamanho mínimo de grupo. São diagnósticos do sistema, não avaliações de desempenho.

## Como ler o painel

| Movimento observado | Interpretação provável | Primeira investigação |
|---|---|---|
| throughput sobe; estabilidade e outcomes se mantêm ou melhoram | ganho sustentável | identificar a capacidade que merece ser padronizada |
| implantações sobem; falhas, retrabalho ou contatos de suporte sobem mais rápido | IA ou automação amplificou um sistema de entrega fraco | tamanho de lote, cobertura de verificação e controles de release |
| tempo de geração cai; espera por revisão e esforço de correção sobem | o trabalho foi transferido para a fila humana | limites das tarefas, qualidade do contexto e checks independentes |
| custo de IA cai; custo por item aceito sobe | falsa economia | retries, retrabalho, roteamento de modelos e custo de falha |
| entrega melhora; outcome de produto fica estável | output está desconectado de valor | priorização, evidência de usuário e desenho de experimentos |
| escalação se aproxima de zero; falhas de escopo ou fatos sobem | o sistema está adivinhando em silêncio | condições de escalação e detecção de ambiguidade |
| médias melhoram; P85 piora | a cauda longa está sendo escondida | trabalho bloqueado, dependências e segmentação por tipo de trabalho |

Métricas indicam onde investigar; não provam causalidade. Mude uma parte material do sistema por vez, registre a hipótese e os guardrails e compare durante uma janela representativa.

## Coleta e cadência

Use identificadores estáveis para conectar Work Item, commit, build, implantação, incidente, evento de produto e execução de IA. Minimize a captura de prompts ou conteúdo; colete classificação, tempo, custo, resultado e proveniência, a menos que conteúdo mais profundo esteja explicitamente autorizado.

| Cadência | Revisão |
|---|---|
| **Contínua / diária** | SLOs, error budget, implantações com falha, eventos de segurança e safety |
| **Revisão semanal da squad** | fluxo, quantidade de implantações, falhas, retrabalho, carga de revisão e itens bloqueados |
| **Revisão mensal de melhoria** | outcome de produto, comparação de IA, economia, pulso da squad e qualidade das métricas |
| **Trimestral** | perfil de maturidade, definições das metas, política e investimento de plataforma |

Comece com quatro a seis semanas de baseline, escolha um gargalo e defina uma meta mais guardrails. As metas devem expressar uma mudança desejada no sistema — por exemplo, “reduzir o cycle time P85 em 20% sem piorar a taxa de falha em mudanças nem o esforço de correção” — em vez de uma cota nua de volume.

## O que não usar como produtividade

- commits, pull requests, linhas de código, story points, prompts ou tokens produzidos;
- ativação de licenças de IA ou porcentagem de código gerado por IA;
- uma pontuação composta única que esconde trade-offs;
- rankings individuais de pessoas ou agentes;
- taxa de aprovação dos gates sem evidências de escape e canários;
- utilização próxima de 100%, que remove a capacidade de revisar, recuperar e aprender.

A orientação atual do DORA define cinco métricas de desempenho de entrega de software entre throughput e instabilidade, e sua pesquisa de IA de 2025 enfatiza que a IA amplifica o sistema ao redor. Consulte as [métricas de desempenho de entrega de software do DORA](https://dora.dev/guides/dora-metrics/) e o [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/). O dashboard mais amplo desta página acrescenta os sinais de produto, pessoas, governança e economia de que uma squad precisa para interpretar essas métricas de entrega em um ambiente AI-first.

---

*Próximo: [Maturidade](MATURITY.md) — como esses sinais sustentam um caminho da assistência oportunista à operação governada e adaptativa.*
