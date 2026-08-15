---
name: business-discovery
description: Extrai e acumula requisitos de negócio de transcrições de discovery, preservando baseline, changelog e lacunas. Use ao processar uma transcrição de levantamento de requisitos ou atualizar os requisitos vivos de uma feature.
---

# Skill: Business Discovery

Transforma a transcrição de uma agenda (você + PM) em requisitos de negócio
estruturados e **acumulativos**. Cada agenda atualiza um documento vivo por
feature — não é extração one-shot.

## Problema que resolve

Transcrições perdem o contexto implícito: como você e a PM já compartilham
histórico, a agenda fala só um pedaço da demanda e referencia coisas sem
definir ("aquele fluxo que a gente falou"). Esta skill (a) acumula o contexto
das agendas anteriores no documento e (b) **sinaliza** explicitamente as
referências não resolvidas, em vez de inventar.

## Input

- **Obrigatório:** caminho (ou conteúdo) da transcrição da agenda.
- **Opcional:** nome/slug da feature (se não der pra inferir, pergunte).
- **Opcional:** materiais que a PM trouxe (PRD, mockup, planilha).

## Saída

Documento em `business-discovery/<feature-slug>/requisitos.md`, usando
`templates/requisitos.md` desta skill. Consulte
`templates/exemplo-preenchido.md` apenas como referência de preenchimento.

## Contrato de artefatos

Antes de escrever, siga [o contrato compartilhado](../references/workflow-contract.md).
O caminho acima é o padrão; use a convenção do repositório consumidor se ela
existir.

## Passos

### 1. Identificar a feature
Infira o slug do conteúdo (ex: `lista-de-espera`). Se ambíguo, **pergunte**
antes de prosseguir. Alvo: `business-discovery/<feature-slug>/requisitos.md`.

### 2. Carregar baseline
Se o arquivo já existe, leia-o inteiro — é o contexto acumulado das agendas
anteriores. Toda extração desta agenda é um **delta** contra esse baseline.
Se não existe, esta é a primeira agenda da feature.

### 2.5. Limpeza da transcrição (se VTT)
Se o arquivo de entrada for um `.vtt` bruto gerado por ferramentas de reunião (Teams, Meet, Zoom), **antes de processar**, execute o script de limpeza auxiliar para remover timestamps e reduzir o consumo de tokens.
Comando a ser executado no terminal:
`python3 scripts/business-discovery-clean-vtt.py <caminho_do_vtt> -o <caminho_do_vtt_limpo.txt>`
Em seguida, leia o arquivo `.txt` gerado e use-o como base para a extração. Se a transcrição já for texto limpo, pule esta etapa.

### 3. Extrair da transcrição
Levante (citando trechos quando útil):
- **User stories** — quem, quer o quê, pra quê. Capture a **prioridade** se a
  agenda deu sinal (P1 = MVP, sem isso não entrega valor; P2/P3 = incrementos).
- **Cenários (Dado / Quando / Então)** — pra cada story, os exemplos testáveis
  ditos na agenda. O **Então** é o resultado observável; se não foi dito, é
  lacuna — **não invente o resultado**. Inclua o caminho de exceção quando citado.
- **Regras de negócio** — atenção ao marcador falado "regra de
  negócio:". Normalize cada uma com pré-condição + gatilho + "o sistema deve" + resposta.
  Cada regra precisa de exemplo concreto; se faltou o exemplo ou alguma cláusula, registre como lacuna — **não invente número,
  valor nem gatilho**. Aponte qual cenário a verifica.
- **Critérios de sucesso (mensuráveis)** — métrica de negócio com número e sem
  tecnologia (SC-XX). Adjetivo vago ("rápido", "fácil") sem número é lacuna.
- **Fluxos** — happy path e exceções / edge cases (vazio, limite, concorrência).
- **Decisões** tomadas na agenda.
- **Dúvidas** levantadas e não resolvidas.
- **Termos de domínio** novos → glossário (marque unicidade/identidade se dita).
- **Fora de escopo** dito explicitamente.

### 4. Diff contra o baseline
Para cada item, classifique:
- **novo** — não existia no baseline.
- **alterado** — refina/muda um item existente (mostre antes → depois).
- **contradito** — conflita com o baseline. NÃO sobrescreva calado: registre o
  conflito e levante como dúvida (DA-XX) pra confirmar na próxima agenda.

Reaproveite numerações existentes (RN-XX, US-X); só crie número novo pra item
novo.

### 5. Detectar lacunas (gap detection)
É a parte que aumenta a assertividade. Liste em `⚠️ Gaps detectados`:
- **Referências não resolvidas** — "aquele fluxo", "igual o outro e-mail", "do
  jeito que a gente fez": algo citado mas não definido nesta transcrição nem no
  baseline. Diga o que assumiu (se assumiu) e marque "confirmar".
- **Regras sem exemplo concreto.**
- **Cenários sem "Então" claro** — story ou regra sem resultado observável definido.
- **Regra de negócio sem cenário** que a verifique (Dado/Quando/Então).
- **Regra incompleta** — sem gatilho/pré-condição, ou "deve" com resposta vaga.
- **Critério de sucesso sem número** — métrica com adjetivo vago em vez de alvo.
- **Dúvidas sem dono/prazo** → vira DA-XX.

Se precisou assumir algo pra fechar uma regra, isso é uma lacuna — registre.

### 6. Escrever o documento
Atualize `requisitos.md` seguindo o template. Regras:
- **Estado Atual Consolidado:** Mantenha a versão final e consolidada dos requisitos no topo do documento. Se houver mudanças ou contradições resolvidas na nova agenda, atualize este estado consolidado para refletir a decisão final.
- **Changelog é append-only e fica no final:** Adicione uma entrada nova com a data da agenda e o resumo do delta (novo/alterado/contradito) no final do documento para servir de histórico de auditoria. Nunca apague entradas anteriores.
- Atualize o cabeçalho (data, lista de agendas, status).
- Mantenha as seções na ordem do template.

### 7. Reportar no chat
Devolva, curto:
- Resumo do delta (X regras novas, Y alteradas, Z contraditas).
- A lista de `⚠️ Gaps` + `DA-XX` — **as perguntas pra levar na próxima agenda.**

Não resolva as lacunas inventando; o valor é a lista de perguntas.

## Convenções

- `RN-XX` regras de negócio (alinhado com o RN-30 do projeto).
- `US-X` user stories (com prioridade `P1`/`P2`/`P3`) · `SC-X` critérios de
  sucesso mensuráveis · `DA-X` dúvidas em aberto (com dono + prazo).
- Cenários em Gherkin pt-BR: **Dado** / **Quando** / **Então** (+ **E** / **Mas**).
- Regras (RN) estruturadas em português (marcador "o sistema **deve**"):
  **Enquanto** (estado), **Quando** (evento), **Onde** (opcional), **Se…então**
  (indesejado), ubíqua (sem keyword), composta (Enquanto+Quando). ⚠️ "Quando/Então"
  aparecem em regras e em Gherkin — a RN é declarativa com "deve"; o cenário é a
  sequência Dado→Quando→Então.
- Status: 🟡 em descoberta · 🟢 pronto pra especificar · ✅ virou spec.
- Escreva em português. Prefira exemplo numérico a descrição vaga.

## Handoff pra review-prd e create-spec

O `requisitos.md` é o artefato de descoberta — alimenta a skill
[`review-prd`](../review-prd/SKILL.md) quando a feature vira 🟢, e depois a
skill [`create-spec`](../create-spec/SKILL.md) para a especificação técnica. O
formato espelha o PRD produzido por essas skills pra a passagem ser direta:

| business-discovery        | PRD / SPEC                            |
|---------------------------|----------------------------------------|
| US-X + Cenários D/Q/E     | User Scenarios → Acceptance Scenarios |
| Prioridade P1/P2/P3       | User Story priority                   |
| RN-XX                     | Requisitos funcionais                 |
| SC-XX                     | Critérios de sucesso                  |
| Glossário / domínio       | Entidades-chave                       |
| Fluxos → exceções         | Edge cases                            |
| Fora de escopo            | Out of scope                          |

RN estruturada ≈ os requisitos funcionais ("o sistema deve …" segue a mesma
estrutura), então a conversão RN→requisito fica quase 1:1.

As `⚠️ Gaps` e `DA-XX` em aberto viram pendências de clarificação no PRD/SPEC —
resolva na agenda antes de especificar.

## Antes da agenda

Use `templates/roteiro-agenda.md` desta skill para preparar a pauta — ele
força explicitar o contexto implícito que senão não entra na transcrição.
Quanto melhor o roteiro for seguido, menos lacunas a skill precisa sinalizar.
