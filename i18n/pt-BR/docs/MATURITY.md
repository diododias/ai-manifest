# Maturidade

Maturidade no desenvolvimento de software assistido por IA é a capacidade de uma squad transformar um problema real em um resultado de produto mensurável **de forma repetível, segura e sustentável**. Ela não é o número de ferramentas de IA em uso, a porcentagem de código gerado por um modelo nem o quanto a participação humana foi reduzida. Gerar código mais rápido sem clareza de produto, disciplina de engenharia e feedback rápido apenas produz mais trabalho em andamento e antecipa defeitos.

Esta página oferece um modelo completo para avaliar uma squad, escolher a próxima melhoria e decidir quanta autonomia o sistema atual consegue sustentar. Ele se aplica a um produto ou fluxo de valor — o caminho ponta a ponta de uma necessidade até um outcome observado em produção — independentemente de linguagem, plataforma, framework de processo ou provedor de IA.

## Como ler o modelo

A unidade de avaliação é a **squad que opera um produto ou fluxo de valor**, não uma pessoa, um modelo ou um repositório isolado. Maturidade é um perfil entre dimensões, não uma nota única para exibição.

Quatro regras mantêm a avaliação honesta:

1. **Os níveis são cumulativos.** Uma squad só sustenta um nível quando as práticas dos níveis anteriores continuam funcionando.
2. **Comportamento observado vale mais que processo declarado.** Use evidências de uma janela recente e representativa, não um checklist de ferramentas compradas ou documentos criados.
3. **Não esconda uma fraqueza crítica na média.** Uma plataforma forte não compensa um processo de release inseguro; automação excelente não compensa um resultado de usuário desconhecido.
4. **Autonomia acompanha risco e evidência.** Uma squad madura pode automatizar uma mudança reversível e bem observada e ainda exigir julgamento humano para uma decisão irreversível ou ambígua.

Uma janela de quatro a doze semanas costuma bastar para a primeira baseline. Use um período maior quando releases ou incidentes forem pouco frequentes.

## As seis dimensões

| Dimensão | A pergunta que responde | Evidência de maturidade |
|---|---|---|
| **Produto e valor para o usuário** | Sabemos qual problema de quem está sendo resolvido e se o resultado ajudou? | outcomes explícitos, telemetria de produto, feedback de usuários, métricas de proteção e decisões ligadas a evidências |
| **Fluxo e desenho do trabalho** | Uma ideia consegue avançar em lotes pequenos, visíveis e reversíveis? | trabalho em andamento limitado, estados explícitos, loops curtos de feedback, tamanho de lote administrável e bloqueios conhecidos |
| **Qualidade de engenharia e confiabilidade** | A squad consegue mudar o sistema sem transferir risco aos usuários? | controle de versão, verificação automatizada, padrões seguros, operabilidade, objetivos de nível de serviço (SLOs), entrega progressiva e prática de recuperação |
| **Conhecimento e dados** | Pessoas e IA conseguem recuperar contexto atual e autoritativo? | fontes canônicas, histórico de decisões, contratos localizáveis, dados saudáveis, proveniência e controles de frescor |
| **Plataforma e automação** | O ambiente torna o caminho correto o caminho mais fácil? | workflows self-service, ambientes reproduzíveis, pipelines observáveis, capacidades reutilizáveis e feedback claro |
| **Colaboração humano-IA e governança** | As tarefas são alocadas, revisadas e escaladas conforme o risco? | postura explícita sobre IA, ferramentas e dados autorizados, revisão independente, outputs rastreáveis, loops de aprendizado e owners responsáveis |

Avalie cada dimensão separadamente. Um resultado útil se parece com `Produto M2 · Fluxo M3 · Qualidade M2 · Conhecimento M1 · Plataforma M2 · Colaboração M1`. Esse perfil mostra o gargalo. Um rótulo único como “somos M3” o esconde.

## A escada de maturidade

| Nível | Modelo operacional | Papel da IA | Papel das pessoas | Evidência de que o nível é real |
|---|---|---|---|---|
| **M0 — Oportunista** | o trabalho depende de esforço individual e conhecimento implícito | assistência ocasional, sem governança | compensam manualmente a falta de processo e contexto | exemplos isolados, sem baseline comparável |
| **M1 — Assistido** | o trabalho básico é visível e repetível | copiloto em tarefas delimitadas, sob revisão direta | especificam, executam e verificam toda decisão material | trabalho versionado, testes básicos, ownership explícito e baseline inicial de métricas |
| **M2 — Padronizado** | a squad compartilha práticas, contexto e critérios de qualidade | executa etapas recorrentes por ferramentas e padrões aprovados | desenham o workflow, revisam exceções e melhoram padrões | lotes pequenos, definições compartilhadas, checks automatizados e dados de entrega comparáveis |
| **M3 — Integrado** | produto, engenharia e operação formam um fluxo único e medido | coordena trabalho delimitado entre etapas e sistemas | definem outcomes, resolvem ambiguidade e tomam decisões conforme o risco | rastreabilidade ponta a ponta, telemetria de produto, plataforma self-service e gates independentes |
| **M4 — Autonomia governada** | vários fluxos operam em paralelo dentro de políticas explícitas | executa e coordena trabalho reversível dentro da autoridade delegada | governam políticas, tratam exceções e decidem trade-offs de alto impacto | aplicação de políticas, privilégio mínimo, evidências, entrega progressiva, rollback e estabilidade sustentada |
| **M5 — Adaptativo** | o sistema sociotécnico melhora por experimentos controlados | seleciona ferramentas e estratégias dentro de limites medidos | definem direção, desafiam o sistema e aprovam mudanças estruturais | experimentos causais, aprendizado contínuo, roteamento dinâmico e melhores resultados sem enfraquecer proteções |

### M0 — Oportunista

O uso de IA começa por iniciativa pessoal. Prompts, decisões e contexto útil permanecem com quem executou a tarefa. O trabalho chega em lotes grandes, a validação é principalmente manual e a squad não sabe dizer se a IA melhorou a entrega ou apenas aumentou o output.

O objetivo no M0 não é autonomia. É visibilidade: selecionar um fluxo de valor, identificar o resultado para o usuário, colocar código e configuração sob controle de versão, tornar os estados do trabalho explícitos e registrar uma baseline antes de mudar o processo.

**Falha típica:** tratar acesso a ferramentas como transformação e escalar uma prática não medida por toda a organização.

### M1 — Assistido

A IA é uma assistente supervisionada. Pode explicar código, rascunhar testes, resumir evidências ou propor uma pequena mudança, mas uma pessoa fornece o contexto e verifica o output material antes que ele avance. Ownership, critérios de aceitação e fonte da verdade são explícitos.

A squad tem um caminho reproduzível para mudanças básicas, checks automatizados para as falhas mais comuns e um conjunto pequeno de métricas de entrega, qualidade e produto. O objetivo é tornar o bom trabalho repetível antes de torná-lo autônomo.

**Pronto para avançar quando:** trabalhos comparáveis seguem o mesmo caminho e a variação causada por contexto ou verificações ausentes fica visível.

### M2 — Padronizado

A squad deixa de depender da técnica individual de prompting. Atividades recorrentes têm procedimentos compartilhados, contexto reutilizável e critérios claros de entrada e saída. As mudanças são pequenas, o trabalho em andamento é controlado, as ferramentas de IA aprovadas são conhecidas e os dados sensíveis têm uma política explícita.

A automação cobre a verificação determinística; as pessoas se concentram em ambiguidade e julgamento. Trabalhos assistidos e não assistidos por IA podem ser comparados sem ranquear pessoas. Checks com falha, retrabalho e escalações alimentam melhorias no workflow.

**Pronto para avançar quando:** o caminho padronizado reduz cycle time ou toil sem aumentar mudanças com falha, defeitos que escapam ou esforço humano de correção.

### M3 — Integrado

Discovery, planejamento, implementação, revisão, release e observação formam um fluxo rastreável. Outcomes de produto orientam prioridades; feedback operacional retorna ao planejamento. A IA consegue coordenar tarefas delimitadas entre ferramentas porque contexto, interfaces, permissões e outputs esperados são explícitos.

A plataforma fornece ambientes reproduzíveis e feedback rápido. Checkpoints humanos ficam onde risco ou ambiguidade exigem julgamento, não onde a automação por acaso termina. A squad consegue ligar um resultado em produção à decisão, à mudança e às evidências que o produziram.

**Pronto para avançar quando:** o fluxo ponta a ponta permanece previsível por vários ciclos de release e controles independentes capturam modos de falha conhecidos.

### M4 — Autonomia governada

Agentes especializados podem planejar e executar trabalho reversível, operar em paralelo e entregar por exposição progressiva. A autoridade é limitada por política, classificação dos dados, classe de risco e ambiente. Identidade, proveniência, evidências e custo acompanham cada mudança material.

As pessoas supervisionam o sistema, não cada etapa. Elas são responsáveis por política, arquitetura, direção de produto e exceções. Rollback ou contenção automática limita o impacto quando o comportamento observado cruza um limite predefinido.

**Pronto para avançar quando:** maior autonomia delegada produz melhores resultados e menos atrito durante uma janela sustentada, sem degradar estabilidade, segurança ou accountability.

### M5 — Adaptativo

A squad trata seu modelo operacional como um produto. Ela testa mudanças em prompts, modelos, contexto, workflow e plataforma com baseline, hipótese e guardrails. O roteamento pode se adaptar a risco, custo e tipo de tarefa; conhecimento e controles evoluem quando as evidências revelam drift.

M5 não significa “sem pessoas”. Significa concentrar a atenção humana em direção, julgamento novo e mudança estrutural, enquanto decisões rotineiras, observáveis e reversíveis são tratadas no nível adequado de automação.

**Evidência de M5:** a melhoria pode ser atribuída a mudanças controladas no sistema, não a mais uso de modelos, mais output ou um pico temporário de esforço.

## Promoção, regressão e autonomia

Uma capacidade só está pronta para avançar quando três tipos de evidência concordam:

| Evidência | O que precisa ser verdade |
|---|---|
| **Capacidade** | a prática, skill, caminho de plataforma ou controle exigido existe e tem owner |
| **Comportamento** | a squad realmente o utiliza em trabalho representativo, incluindo exceções e caminhos de falha |
| **Resultado** | velocidade, qualidade, valor, custo ou experiência da squad melhora enquanto os guardrails permanecem saudáveis |

Promoção é uma decisão sobre dimensão e escopo específicos, não um selo permanente. Reavalie depois de uma mudança material de plataforma, arquitetura, equipe ou política. Bypasses recorrentes, contexto obsoleto, estabilidade piorando ou telemetria ausente justificam regressão até a capacidade ser restaurada.

A autonomia também depende do contexto. Uma squad pode sustentar automação M4 para atualização de dependências e permanecer no M2 para decisões de preço, privacidade ou migração de dados. O comportamento maduro é usar a maior autonomia **sustentada** pelo risco em questão, não a maior autonomia tecnicamente possível.

## Executando uma avaliação

1. Escolha um produto ou fluxo de valor e nomeie seus usuários, serviços e a fronteira da squad.
2. Colete uma baseline pelas mesmas definições e fontes durante quatro a doze semanas.
3. Para cada dimensão, encontre o nível mais alto sustentado por evidências de capacidade, comportamento e resultado.
4. Registre o perfil, as evidências, lacunas e confiança; use `unknown` quando faltar telemetria.
5. Selecione a dimensão crítica de risco mais baixa como a próxima restrição a melhorar.
6. Execute um experimento de melhoria delimitado, com owner, meta, guardrail e data de revisão.
7. Reavalie depois da janela; mantenha, altere ou reverta a intervenção conforme o resultado.

O output deve ser um backlog curto de melhorias, não um exercício de certificação. Se a avaliação produzir dezenas de iniciativas simultâneas, ela falhou em identificar a restrição.

## Os primeiros 90 dias na prática

| Janela | Foco | Resultado esperado |
|---|---|---|
| **Dias 0–30** | escolher um fluxo de valor, definir outcome e guardrails, publicar a postura sobre IA, inventariar dados e estabelecer a baseline | a squad consegue descrever seu sistema atual com evidências |
| **Dias 31–60** | reduzir o tamanho dos lotes, tornar trabalho e ownership visíveis, padronizar tarefas recorrentes, automatizar checks comuns e registrar o envolvimento da IA | trabalhos comparáveis seguem um caminho repetível |
| **Dias 61–90** | remover o maior gargalo medido, delegar uma atividade de baixo risco e comparar resultado, estabilidade, esforço e custo | uma capacidade avança sem enfraquecer outra |

## O que maturidade não é

- Taxa de adoção de IA, licenças compradas, quantidade de prompts, volume de tokens ou linhas de código geradas.
- Um ranking de pessoas, squads ou papéis de agentes.
- Um checklist que só pode subir.
- Automação máxima em toda decisão.
- Um substituto para estratégia de produto, julgamento de engenharia ou accountability.

A pesquisa atual do DORA descreve a IA como amplificadora do sistema organizacional ao redor e destaca foco no usuário, lotes pequenos, controle de versão forte, dados saudáveis, contexto interno acessível à IA, postura clara sobre IA e plataforma interna de qualidade como capacidades habilitadoras. Este modelo transforma essas ideias em um caminho operacional cumulativo; ele não exige a adoção de um framework ou provedor específico. Consulte o [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) e o [questionário do DORA AI Capabilities Model](https://dora.dev/ai/capabilities-model/questions/) para conhecer a pesquisa de base.

---

*Próximo: [Métricas](METRICS.md) — como medir entrega, valor, estabilidade e colaboração humano-IA sem premiar volume.*
