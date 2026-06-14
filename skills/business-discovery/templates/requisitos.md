# Requisitos — <Nome da feature>

- **Épico:** <épico> · **Status:** 🟡 em descoberta
- **Atualizado:** AAAA-MM-DD · **Agendas:** [AAAA-MM-DD]
- **Participantes:** <nomes>

## Contexto & objetivo
<Que dor resolve, pra quem, qual o resultado esperado. 2–4 linhas. A métrica
com número fica em Critérios de sucesso (SC-XX).>

## Glossário / domínio
- **<Termo>** — <definição>. Marque *(existe)* se já é entidade do sistema,
  *(novo)* se nasce aqui. Quando a agenda definir, registre identidade/unicidade
  e atributos-chave.

## User stories & cenários
> Cada story carrega seus cenários em **Dado / Quando / Então** (Given · When ·
> Then). O **Então** é o resultado observável — se a agenda não deu, é gap; não
> invente o resultado.

- **US-1** *(Prioridade: P1)* Como <papel>, quero <ação>, pra <benefício>.
  - *Teste independente:* <como validar essa story sozinha> *(opcional)*
  - **Cenários:**
    1. **Dado** <estado inicial>, **Quando** <ação>, **Então** <resultado observável>.
    2. *(exceção)* **Dado** <estado>, **Quando** <ação>, **Então** <tratamento>.

## Regras de negócio
> Escreva cada RN com pré-condição + gatilho + resposta do sistema, então cláusula
> faltando vira gap (não invente). Marcador da obrigação = "o <sistema> **deve**
> <resposta>". Padrões:
> - **Ubíqua:** o <sistema> deve <resposta>. *(sempre ativa, sem keyword)*
> - **Estado:** **Enquanto** <pré-condição>, o <sistema> deve <resposta>.
> - **Evento:** **Quando** <gatilho>, o <sistema> deve <resposta>.
> - **Opcional:** **Onde** <feature/variante presente>, o <sistema> deve <resposta>.
> - **Indesejado:** **Se** <gatilho>, **então** o <sistema> deve <resposta>.
> - **Composta:** **Enquanto** <pré>, **quando** <gatilho>, o <sistema> deve <resposta>.
>
> A regra estruturada = a obrigação; o Gherkin **Dado/Quando/Então** (em Cenários)
> = o exemplo que a testa. "Quando/Então" aparecem nas duas camadas — a RN é
> declarativa e tem "deve"; o cenário é a sequência Dado→Quando→Então. Cada RN
> precisa de exemplo concreto e de ≥1 cenário que a verifique (rastreio RN ↔ US).
- **RN-1** Quando <gatilho>, o <sistema> deve <resposta>. *Ex: <exemplo concreto/numérico>.* *(verifica: US-1 cenário 1)*

## Fluxos
**Happy:** <jornada fim a fim>.
**Exceções / edge cases:** <erros, limites, estados inválidos, concorrência, vazio>.

## Critérios de sucesso (mensuráveis)
> Resultado de negócio, com número e sem tecnologia. Diferente do cenário (que é
> binário/testável); aqui é o alvo que diz se a feature deu certo.
- **SC-1** <métrica com alvo>. *Ex: 30% dos inscritos convertem em 7 dias.*

## Fora de escopo
<O que explicitamente NÃO é pra fazer.>

## Dúvidas em aberto
- **DA-1** <pergunta>? *(dono: <quem> · prazo: <quando>)*

## ⚠️ Gaps detectados na transcrição
<Referências citadas mas não definidas; regras sem exemplo; cenários sem "Então"
claro; adjetivos vagos sem número ("rápido", "fácil"); RN sem cenário que a
verifique. Cada uma com "confirmar".>

## Changelog por agenda
- **AAAA-MM-DD** — <delta: o que entrou / mudou / contradisse>.
