# 02 — Checkpoints humanos

> Onde exatamente uma pessoa entra, com qual pergunta, por quanto tempo e o que ela precisa ver para responder.

O princípio que organiza esta página: **o humano não revisa o processo — ele responde a uma pergunta objetiva.** Ninguém acompanha o diff inteiro nem lê o PRD linha por linha. Em cada checkpoint, o sistema entrega a decisão pedida, a recomendação dos agentes, as alternativas descartadas, os riscos e as evidências dos gates. A pessoa responde.

O que torna isso possível não é confiança no agente: é a [arquitetura de gates](../GATES.md). Cinco camadas de verificação filtram tudo que é determinístico antes de qualquer pessoa ser chamada. **Um checkpoint só existe onde uma máquina não pode decidir.** Se um humano está sendo chamado para algo verificável, o gate está no lugar errado — e isso é um defeito do harness, não do checkpoint.

---

## Os seis checkpoints

| Marco | Pergunta | Gatilho | Owner | Tempo esperado |
|---|---|---|---|---:|
| **H1** | Vale investir neste problema? | gate de discovery aprovado | PM ou sponsor | 5–10 min |
| **H2** | É isto que construiremos? | gate de produto aprovado | PM, com UX como coautor | 10–15 min |
| **H3** | Aceitamos o trade-off? | nova ADR, exceção arquitetural ou risco R3/R4 | Tech Lead ou especialista do domínio | 10–20 min |
| **H4** | Podemos integrar? | PR aberto com CI verde, conforme classe de risco | Code Owner do path | 5–15 min |
| **H5** | Podemos expor o risco? | release candidate aprovado, em R3/R4 ou exposição crítica | Tech Lead; PM coaprova | 3–10 min |
| **H6** | O sistema aprendeu corretamente? | ciclo semanal do [🌙 Dream Loop](../loops/10-continuous-improvement.md) | owner do sistema de trabalho | 10–20 min |

Somados, os seis representam entre 30 e 45 minutos de tempo humano por entrega de risco médio. **H3 e H5 são condicionais**: em um item de baixo risco com gates verdes, o ciclo vai de H2 direto a H4 — três decisões humanas do problema à produção.

### O que cada um decide

**H1 — vale investir?** Ocorre depois do [🔦 Scout Loop](../loops/01-discovery-and-research.md), sobre um `PB.md` consolidado. A pessoa revisa problema, usuário, valor, restrições e riscos, e decide avançar, ajustar a pergunta, adiar ou encerrar. Encerrar é uma resposta legítima e a mais barata de todas neste ponto.

**H2 — é isto que construiremos?** Ocorre depois do [🎨 Studio Loop](../loops/02-product-and-ux-planning.md), sobre um `PRD.md` já submetido a crítica adversarial. A revisão é sobre **decisões e gaps**, não sobre o documento inteiro: o que a crítica levantou e como foi respondido. Decide aprovar, reduzir, ampliar ou devolver.

**H3 — aceitamos o trade-off?** Condicional. Só ocorre quando o [🗺️ Drafting Loop](../loops/03-technical-specification.md) produz uma ADR nova, uma exceção arquitetural ou uma mudança de risco alto. A revisão cobre a decisão, as alternativas descartadas e o impacto futuro — não o desenho completo. Quando não há decisão estrutural nova, este checkpoint não acontece.

**H4 — podemos integrar?** Ocorre no [🚪 Gatekeeper Loop](../loops/06-pr-and-merge.md), e o peso varia por classe de risco. A pessoa revisa o evidence pack, os trechos de maior risco e as exceções — nunca o diff completo.

**H5 — podemos expor o risco?** Condicional, no [🐤 Canary Loop](../loops/08-production-release-and-observation.md). Revisa impacto, plano de rollout, rollback e sinais de saúde. R0 e R1 seguem sem checkpoint quando o rollback é comprovado.

**H6 — o sistema aprendeu corretamente?** Único checkpoint que não trata de produto: trata do próprio sistema de trabalho. Obrigatório para mudança sensível de memória, item P0/P1 e **qualquer alteração de gate**; por amostragem no restante.

---

## O que a pessoa recebe

Um checkpoint sem evidence pack não é uma decisão: é um pedido de confiança. O pacote é gerado automaticamente — evidência montada manualmente ao final da tarefa é seletiva por natureza.

| Item | Conteúdo |
|---|---|
| **Decisão solicitada** | uma frase, no formato de pergunta fechada |
| **Recomendação** | a posição dos agentes e sua confiança |
| **Alternativas** | o que foi considerado e por que foi descartado |
| **Riscos e trade-offs** | o que se aceita ao aprovar |
| **Delta** | o que mudou desde o checkpoint anterior |
| **Evidências** | resultado dos gates executados, com link para a saída bruta |
| **Pendências** | exceções em aberto e nível de confiança declarado |
| **Links** | artefatos completos, código e execução |

O **delta** é o campo que mais reduz tempo humano na segunda passagem: quando um item volta para nova decisão, a pessoa lê o que mudou, não o conjunto inteiro.

O detalhe da estrutura em disco do evidence pack está em [Documentation](../DOCUMENTATION.md). O teste de qualidade é o mesmo lá e aqui: **outra pessoa consegue refazer a verificação sem perguntar nada a quem a produziu?**

---

## As duas travas

Duas regras protegem o mecanismo inteiro. Elas não são recomendações de etiqueta — são condições de validade da aprovação.

**Silêncio nunca é aprovação.** Ausência de resposta mantém o item parado. A pressão de prazo aparece como item parado e visível, não como avanço tácito. O [☀️ Daily Loop](../loops/11-daily-operations.md) existe, em parte, para que um item parado apareça no dia seguinte.

**Mudança material invalida a aprovação relacionada.** Se o artefato mudou de forma relevante depois do aval, o aval não cobre a nova versão. O que conta como material é definido por classe de risco e verificado por automação — não pela avaliação de quem fez a mudança.

---

## Como o risco muda o checkpoint

A classe de risco é o que determina quantas aprovações a mudança exige e quanto de automação ela pode usar. Ela é proposta por um agente e contestada por outro; **o maior risco justificado prevalece**.

| Classe | Caracteriza | O que exige em H4 e H5 |
|---|---|---|
| **R0 — mínimo** | documentação e formatação; sem mudança de comportamento, dados ou contratos | merge automático após gates; revisão por amostragem |
| **R1 — baixo** | refatoração ou mudança localizada coberta por testes existentes | uma revisão curta do owner; deploy automático com observação |
| **R2 — médio** | novo comportamento de produto ou mudança de contrato interno | aprovação do responsável afetado; canary e rollback automatizados |
| **R3 — alto** | dados persistidos, migrações, contratos públicos, autenticação, secrets, pagamentos, disponibilidade | aprovação técnica **e** de produto; aval explícito antes de produção |
| **R4 — crítico** | impacto regulatório, financeiro ou destrutivo; ação irreversível | dupla aprovação com segregação de função e acompanhamento durante a liberação |

Redução manual de risco exige justificativa registrada. Mudança de escopo recalcula o risco. Paths sensíveis elevam risco automaticamente. E **dúvida não resolvida impede classificação como R0 ou R1** — a ausência de informação é um risco, não a ausência dele.

---

## Autonomia — quantos checkpoints existem hoje

O número de checkpoints não é fixo: ele diminui conforme o sistema demonstra que os gates são confiáveis. Essa é a única dimensão do modelo que se move deliberadamente ao longo do tempo.

| Nível | O sistema faz | A pessoa faz |
|---|---|---|
| **A0 — assistido** | executa sob supervisão | aprova todas as transições |
| **A1 — execução autônoma** | implementa e valida | mantém H1, H2, H4 e H5 |
| **A2 — merge por risco** | auto-merge em R0 | revisão curta em R1; owners específicos em R2+ |
| **A3 — entrega autônoma controlada** | deploy automático em R0/R1, com rollback obrigatório | atua em exceções e riscos altos |
| **A4 — orientado a exceções** | opera o fluxo saudável sem intervenção | recebe decisões e incidentes; audita por amostragem |

**Elevar autonomia exige todos os critérios simultaneamente:** volume mínimo de entregas observado, baixa taxa de defeitos escapados, rollback testado e confiável, gates com poucos falsos positivos, risco classificado corretamente, evidências auditáveis e tempo humano de fato reduzido.

A restrição que fecha o mecanismo: **o harness impõe teto à autonomia.** Um repositório sem a camada de verificação correspondente não sustenta o nível, independentemente do histórico do time. O detalhe dos níveis de maturidade está em [Gates](../GATES.md).

---

## Onde cortar checkpoint com segurança

Cada corte abaixo só é seguro depois que o histórico demonstrar que o gate correspondente é confiável. Cortar antes disso não aumenta autonomia — aumenta risco não observado, que é o pior tipo.

| Movimento | Pré-requisito |
|---|---|
| Combinar H2 e H3 em mudanças pequenas e conhecidas | padrão já validado em ciclos anteriores |
| Eliminar H3 quando não houver ADR, exceção ou risco relevante | classificação de risco confiável |
| Aplicar H4 por amostragem em R0 | histórico baixo de defeitos escapados |
| Tornar H5 automático em R0/R1 | rollback comprovado em produção |
| Mostrar apenas o delta desde a última aprovação | evidence pack com delta |
| Direcionar a pessoa aos hotspots, não ao diff | análise de risco por trecho |
| Remover um gate sem valor | medição de falsos positivos |

O sinal de que o corte foi cedo demais não é o incidente: é o **retrabalho após o checkpoint seguinte**. Ele aparece antes, e é a métrica a observar.

---

## O que degrada primeiro

Quando este mecanismo começa a falhar, o sintoma não é um checkpoint a mais. É a proporção humana subindo silenciosamente, sempre por uma destas três causas.

| Sintoma | Causa provável | Onde corrigir |
|---|---|---|
| A pessoa pede o artefato completo antes de responder | evidence pack incompleto ou sem delta | [Workflows de documentação](07-workflows-de-documentacao.md) |
| Checkpoints se acumulam sem resposta | pergunta mal formulada, ou owner errado | [Papéis](01-papeis.md) |
| A mesma decisão volta duas vezes | mudança material sem invalidação automática | [Gates](../GATES.md) |

---

*Anterior: [Papéis](01-papeis.md) · Próximo: [Gatilhos e disparos](03-gatilhos-e-disparos.md).*
