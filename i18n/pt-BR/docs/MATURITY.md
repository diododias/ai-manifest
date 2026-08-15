# Maturidade

Nesta documentação, maturidade não significa adoção de IA. Significa a capacidade demonstrada de uma squad transformar uma necessidade em resultado observado, repetidamente, sem perder o controle de qualidade, risco, custo ou responsabilidade.

A unidade de avaliação é uma **squad operando um produto ou fluxo de valor**. O repositório é um subsistema dessa operação; o modelo é uma dependência. Nenhum dos dois representa sozinho a maturidade do fluxo completo.

## Três escalas, três decisões diferentes

O método usa três escalas relacionadas, mas não intercambiáveis:

- **M0–M5 descreve o perfil de maturidade da squad.** Avalia produto, fluxo, engenharia, conhecimento, plataforma e governança humano-IA. Serve para localizar a restrição operacional e escolher a próxima capacidade a melhorar.
- **HL0–HL3 descreve o repo harness.** Informa o que o repositório consegue verificar no estado atual e, portanto, estabelece um teto técnico para a autonomia. Os controles são definidos em [Gates](GATES.md#autonomia-progressiva-e-o-teto-do-harness).
- **A0–A4 descreve a autonomia em operação.** Registra quais transições os agentes podem executar sem uma pessoa e quais checkpoints continuam obrigatórios para o risco atual. Os níveis são definidos em [Checkpoints humanos](metodologia/02-checkpoints-humanos.md#autonomia--quantos-checkpoints-existem-hoje).

Um perfil de maturidade alto não autoriza uma autonomia que o harness não consegue verificar. Uma squad pode estar em M4 nas dimensões de produto e fluxo, enquanto um repositório em HL2 ainda limita a autonomia técnica a A2. O inverso também importa: a verificação de um HL3 não justifica delegar uma decisão de preço ou privacidade quando a evidência de produto ou a governança permanece em M1.

O estado operacional válido é contextual: a maturidade mostra o que o sistema sustenta de forma ampla, o harness impõe o teto técnico e o risco determina quanto desse teto pode ser usado em uma mudança específica.

## Regras da avaliação

**Os níveis são cumulativos dentro de cada dimensão.** A evidência de M3 deixa de valer quando uma capacidade de M1 ou M2 da qual ela depende deixa de funcionar.

**O comportamento observado prevalece sobre o processo declarado.** Uma política, ferramenta ou documento prova que uma capacidade existe; não prova que o trabalho representativo a utiliza nem que ela melhora um resultado.

**O resultado é um perfil, não uma média.** `Produto M3 · Fluxo M2 · Qualidade M3 · Conhecimento M1 · Plataforma M2 · Governança M2` preserva a restrição. Transformar o perfil em “M2,2” esconderia que contexto obsoleto ou difícil de localizar limita o sistema inteiro.

**Desconhecido não significa zero nem verde.** A ausência de telemetria gera uma lacuna explícita de confiança. Ela não sustenta promoção, mas também não deve ser convertida em uma pontuação inventada.

**O risco continua local à decisão.** Uma operação madura amplia primeiro a autonomia de trabalho delimitado, reversível e observável. Decisões irreversíveis, reguladas ou ambíguas podem manter checkpoints humanos em qualquer nível de maturidade.

Deve-se usar uma janela recente que inclua trabalho normal e caminhos de exceção relevantes. Entregas, migrações ou incidentes de baixa frequência exigem uma janela maior que a operação rotineira; um intervalo de calendário conveniente não é evidência quando deixa de fora o comportamento avaliado.

## As seis dimensões

Cada dimensão recebe seu próprio nível. A mesma squad pode estar avançada em uma e limitada em outra.

**Produto e valor para o usuário** mede se o trabalho começa em um problema explícito e termina em um efeito observado. A evidência conecta hipótese, usuário, resultado de produto, métricas de proteção e a decisão tomada após telemetria ou feedback. Volume produzido, adoção sem uso bem-sucedido e opinião de partes interessadas sem comportamento observado não estabelecem maturidade.

**Fluxo e desenho do trabalho** mede se uma mudança atravessa o sistema em lotes pequenos, visíveis e reversíveis. A evidência inclui estados explícitos, trabalho em andamento controlado, sinais de bloqueio e envelhecimento, tamanho de lote administrável e filas conhecidas. A dimensão é fraca quando a IA acelera a produção enquanto o trabalho se acumula em revisão, integração ou entrega.

**Qualidade de engenharia e confiabilidade** mede se a squad consegue alterar o sistema sem transferir risco não controlado para o usuário. A evidência inclui verificação determinística local, CI em ambiente limpo, gates independentes, controles de segurança, observabilidade, SLOs, exposição progressiva e recuperação exercitada. Pipeline verde é insuficiente quando canários não conseguem provar que os gates ainda rejeitam falhas conhecidas.

**Conhecimento e dados** mede se pessoas e agentes recuperam contexto atual, autoritativo e permitido. A evidência cobre fontes canônicas, histórico de decisões, responsáveis definidos, proveniência, frescor, qualidade dos dados e fronteiras de confiança. Mais conteúdo indexado não representa maturidade quando as fontes divergem, dados sensíveis ficam expostos ou contexto obsoleto não pode ser detectado.

**Plataforma e automação** mede se o caminho suportado é reproduzível, observável e mais barato que a improvisação. A evidência inclui ambientes self-service, interfaces estáveis, rotinas reutilizáveis, limites de permissão, falhas acionáveis e visibilidade de custo. Automação que depende de intervenção especializada ou salta controles indisponíveis silenciosamente ainda não se tornou uma capacidade de plataforma.

**Colaboração humano-IA e governança** mede se autoridade, revisão e escalação acompanham o risco, não a conveniência. A evidência inclui postura explícita sobre IA, ferramentas e dados autorizados, papéis delimitados, aprovação independente, resultados rastreáveis, escalação significativa e responsáveis claramente definidos. Menos interações humanas só indicam maturidade quando as decisões necessárias continuam visíveis e os escapes não aumentam.

## A escada de maturidade

A escada abaixo é aplicada separadamente a cada dimensão. O nível descreve como aquela capacidade é controlada, não um inventário fixo de ferramentas.

Cada resultado deve ser lido como o cruzamento entre uma dimensão e um mecanismo de controle. `Conhecimento M2` significa que contexto autoritativo, proveniência e frescor seguem um caminho compartilhado e usado por trabalhos comparáveis; não significa que a squad esteja genericamente “no M2”. `Produto M3` significa que a evidência de produto fecha um loop rastreável da hipótese ao resultado em produção e retorna para uma decisão. A dimensão define **o que** está sendo avaliado; o nível define **com que confiabilidade o sistema reproduz e governa essa capacidade**.

### M0 — Oportunista

Os resultados dependem de esforço individual e conhecimento implícito. O uso de IA é pessoal, prompts úteis e decisões não podem ser recuperados, e o sucesso não pode ser comparado com uma linha de base estável. O problema principal não é falta de automação; é a incapacidade do sistema de distinguir uma capacidade repetível de um sucesso isolado.

A evidência para sair do M0 é a observabilidade básica do escopo escolhido: responsável nomeado, resultado explícito, trabalho versionado, estados visíveis e linha de base baseada em definições consistentes. Nada disso concede autonomia; apenas torna as afirmações seguintes refutáveis.

### M1 — Assistido

O trabalho é delimitado e supervisionado. Contexto, critérios de aceitação, responsabilidades e fontes da verdade estão explícitos o suficiente para a assistência de um agente, enquanto as pessoas ainda verificam toda decisão e todo resultado material. Mudanças comuns têm um caminho reproduzível e a squad registra sinais iniciais de produto, entrega e qualidade.

O M1 se sustenta quando um trabalho comparável pode ser repetido por alguém diferente de quem estabeleceu o caminho. Avançar exige mostrar de onde vem a variação — contexto ausente, execução instável, filas manuais ou verificações frágeis — em vez de escondê-la dentro da experiência individual.

### M2 — Padronizado

O trabalho recorrente segue contratos compartilhados, não maneiras pessoais de escrever prompts. Critérios de entrada e saída, classes de risco, ferramentas autorizadas, limites de dados e evidências esperadas estão definidos. A verificação determinística é automatizada; as pessoas se concentram em ambiguidade, trade-offs e exceções.

A prova de M2 é a redução da variação, não a conformidade com um modelo. O caminho padronizado precisa reduzir tempo de ciclo, trabalho operacional repetitivo ou esforço de correção sem aumentar mudanças com falha, defeitos que escapam ou exceções de política. Se o caminho está documentado, mas é contornado com frequência, a dimensão continua em M1.

### M3 — Integrado

Decisões de produto, execução do trabalho, verificação de engenharia, entrega e observação em produção formam um único loop de feedback rastreável. A squad consegue ligar um resultado observado à hipótese, decisão, mudança, evidência e condição operacional que o produziram. O aprendizado de produção retorna ao planejamento, em vez de terminar em um painel isolado.

Os agentes podem coordenar trabalho delimitado entre ferramentas porque contexto, interfaces, permissões e contratos de saída estão explícitos. Checkpoints humanos existem onde risco ou ambiguidade exigem julgamento, não onde a automação por acaso termina. M3 exige vários ciclos representativos com rastreabilidade ponta a ponta e controles independentes capazes de detectar modos de falha conhecidos.

### M4 — Autonomia governada

O sistema delega trabalho reversível dentro de políticas explícitas. Agentes especializados podem operar simultaneamente, mas a autoridade continua limitada por papel, classe de risco, classificação dos dados, ambiente e orçamento. Identidade, proveniência e evidência acompanham toda mudança material; exposição progressiva e rollback testado limitam o efeito de uma decisão errada.

As pessoas governam políticas, resultados, arquitetura e exceções, em vez de supervisionar cada etapa. M4 só é demonstrado quando a autoridade delegada reduz espera ou esforço humano durante uma janela contínua, mantendo estabilidade, segurança, valor e responsabilidade dentro dos limites de proteção. Mais execução sem acompanhamento, isoladamente, não prova nada.

### M5 — Adaptativo

A squad trata seu sistema operacional como objeto de melhoria controlada. Mudanças em modelos, prompts, contexto, roteamento, workflow e plataforma começam com linha de base e hipótese, operam dentro de limites de proteção e produzem uma decisão de manter, alterar ou reverter. O roteamento pode se adaptar à tarefa, ao risco e ao custo porque o contrato de avaliação já é estável.

A atenção humana se desloca para direção, julgamento novo e mudança estrutural; ela não desaparece. A evidência de M5 é causal: resultados melhores podem ser atribuídos a uma mudança controlada no sistema e permanecem melhores depois que o esforço temporário do experimento termina. Mudança contínua sem atribuição é deriva, não adaptação.

## Evidência para promoção e regressão

A promoção de uma dimensão exige que três camadas de evidência concordem:

- **Capacidade:** a prática, contrato, caminho de plataforma ou controle existe, está versionado e tem responsável explícito.
- **Comportamento:** o trabalho representativo realmente o utiliza, inclusive em caminhos de falha, escalação e exceção.
- **Resultado:** o efeito pretendido sobre valor, velocidade, qualidade, custo ou time melhora enquanto seus indicadores de proteção permanecem saudáveis.

Capacidade sem comportamento é material de prateleira. Comportamento sem resultado é atividade. Resultado sem capacidade é um caso isolado que o sistema não consegue reproduzir de forma confiável.

A promoção se aplica a uma dimensão, escopo e janela de evidência nomeados; não é uma certificação permanente. Uma mudança material em time, arquitetura, plataforma, política ou dados invalida as premissas que ela afeta. Controles contornados repetidamente, contexto obsoleto, telemetria ausente, escapes crescentes ou recuperação não exercitada justificam regressão até que a capacidade seja demonstrada novamente. Um modo degradado declarado também reduz o teto aplicável do harness enquanto durar ([Falha](FAILURE.md#declarando-um-modo-degradado)).

## Como ler um resultado

Uma avaliação utilizável preserva contexto suficiente para orientar uma decisão:

```text
Escopo: fluxo de entrega do checkout
Janela: 12 entregas representativas

Perfil:
  Produto M3 · Fluxo M2 · Qualidade M3
  Conhecimento M1 · Plataforma M2 · Governança M2

Repo harness: HL2 → teto técnico A2
Autonomia em operação: A1
Restrição principal: contexto autoritativo fragmentado e frescor desconhecido
```

O resultado não afirma que a squad “é M2”. Ele mostra que integração e qualidade estão à frente do sistema de conhecimento, o que impede o reuso confiável de contexto e torna insegura uma delegação mais ampla. Operar em A1 é válido porque permanece abaixo do teto HL2; operar em A3 seria inválido mesmo que o perfil de maturidade fosse mais forte.

A próxima intervenção deve atacar a restrição mais baixa que seja **crítica para o risco**, não mecanicamente o menor número. Seu contrato nomeia responsável, efeito pretendido, indicador de proteção e data de revisão. Depois da janela de evidência, a squad mantém, altera ou reverte a intervenção e reavalia apenas as dimensões que ela poderia ter afetado.

## Usos que invalidam o modelo

- Tratar ferramentas compradas, licenças habilitadas ou acesso a modelos como capacidade.
- Promover um nível porque documentos e pipelines existem, sem observar seu uso e efeito.
- Reduzir o perfil a uma média ou usá-lo para ranquear squads, pessoas ou agentes.
- Presumir que maturidade só aumenta ou que todo escopo merece a mesma autonomia.
- Usar volume gerado, commits, pull requests ou tokens consumidos como aproximações de valor.

---

*Próximo: [Métricas](METRICS.md) — os sinais que governam promoção, regressão e autonomia.*
