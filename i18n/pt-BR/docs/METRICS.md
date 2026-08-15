# Métricas

DORA mede entrega; não mede o harness. Autonomia exige evidência de que o sistema de verificação detecta aquilo que afirma detectar.

## Sinal principal

**Taxa de escape de gate** é o número de defeitos encontrados depois do gate que deveria tê-los detectado, por Work Item aceito.

Segmente por ponto de detecção, severidade e gate responsável. Atribua o escape ao controle que falhou, nunca à pessoa ou ao agente que escreveu a mudança. O sucesso do pipeline informa o que os gates detectaram; a taxa de escape informa o que deixaram passar.

## Sinais auxiliares

- **Taxa de escalação:** uma taxa próxima de zero combinada com escapes crescentes indica inferência silenciosa; uma taxa alta isolada é inconclusiva.
- **Retrabalho após merge:** mudanças aceitas que foram materialmente reabertas ou corrigidas dentro de uma janela fixa.
- **Latência de feedback por camada:** latência do sensor, da fast lane e da deep lane medida separadamente.
- **Taxa de skip e degradação:** gates `skipped`, quarentenas e retries ([Falha](FAILURE.md)).
- **Custo por Work Item aceito:** custo total de agentes, modelos e revisão somando todas as tentativas.
- **Completude da evidência:** itens aceitos que um revisor independente consegue reverificar sem auxílio.
- **Latência e profundidade da revisão:** tempo até a decisão, acompanhado de evidência de revisão substantiva.

Não otimize nenhum sinal isoladamente. Custo menor com mais retrabalho, menos escalação com mais escapes ou revisão mais rápida sem profundidade são regressões.

## Promoção e rebaixamento

- **Promova** apenas quando os artefatos exigidos existirem ([Maturidade](MATURITY.md)) e os sinais se sustentarem por uma janela contínua.
- **Rebaixe** quando taxas de escape ou skip subirem, a evidência ficar obsoleta ou a escalação despencar sem redução correspondente da ambiguidade.

A escada precisa se mover nas duas direções; caso contrário, registra histórico em vez da capacidade atual.

## Rejeite como métricas de controle

- Rankings por pessoa ou agente.
- Commits, linhas, pull requests, tokens ou outros proxies de volume.
- Taxa de aprovação de gate sem canários e atribuição de escapes.

## Fontes

`gate-status.json` fornece os estados dos gates, `attestation.json` registra o contexto de produção, evidence packs contêm a saída da verificação e o histórico do controle de versão fornece retrabalho e tempo de revisão. Registros de defeito precisam acrescentar o gate que deveria ter detectado o escape; sem esse campo, o painel mede atividade, não verificação.

---

*Próximo: [Maturidade](MATURITY.md) — o que cada nível exige e como descobrir onde um repositório realmente está.*
