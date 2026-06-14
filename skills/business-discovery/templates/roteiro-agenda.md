# Roteiro de Agenda — <feature / épico>

- **Data:** AAAA-MM-DD
- **Participantes:** <você>, <PM>, <outros>
- **Demanda:** <1 linha>
- **Gravação:** <link>

> Preencha o que der antes da agenda. Durante a reunião, use como pauta. O
> objetivo é forçar explicitar o contexto que "todo mundo já sabe" — é isso que
> não entra na transcrição e derruba a assertividade da extração.

## 0. Contexto em voz alta  (mesmo que óbvio — vira âncora da transcrição)
> O que é, qual épico, por que agora.

## 1. Recap do já decidido  (captura o contexto implícito das agendas anteriores)
> "Última vez fechamos X, Y. Hoje é sobre Z."

## 2. Problema de negócio
> Que dor, pra quem, e a **métrica de sucesso COM número** (alvo). Vira SC-XX.
> Adjetivo vago ("rápido", "melhor") sem número volta como lacuna.

## 3. Fluxo principal (happy path)
> Passo a passo do usuário. Quem faz o quê. Diga a **prioridade** de cada pedaço
> (o que é MVP / P1 vs. incremento / P2-P3).

## 4. Regras de negócio   ← falar "regra de negócio:" antes de cada uma
> Cada regra COM exemplo concreto/numérico (o exemplo é o que a IA não infere) e
> COM a estrutura: a pré-condição/gatilho ("quando…", "enquanto…", "se…") + o que
> **o sistema deve** fazer. Estrutura clara = facilita normalização sem inventar cláusula.

## 5. Exceções / edge cases
> Erro, limites, estados inválidos.

## 6. Fora de escopo
> O que explicitamente NÃO é pra fazer.

## 7. Cenários de aceite  ← pra cada story, fale **Dado / Quando / Então**
> O "Então" é o resultado observável que a IA não infere. Inclua o caminho de
> exceção (e-mail inválido, fila vazia, concorrência). Ex: "Dado mês esgotado,
> Quando o cliente entra na lista, Então vê confirmação e fica na fila".

## 8. Dúvidas em aberto
> O que ficou sem resposta — quem decide, até quando.

## 9. Materiais de apoio
> Links, mockups, docs que a PM trouxe (ou que faltam).
