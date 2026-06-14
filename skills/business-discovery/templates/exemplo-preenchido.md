# Requisitos — Lista de espera para mês esgotado

> Exemplo preenchido (demanda fictícia) para servir de referência ("north star")
> ao formato de saída. Não é uma feature real do backlog.

- **Épico:** Capacidade · **Status:** 🟡 em descoberta
- **Atualizado:** 2026-06-13 · **Agendas:** [2026-06-13]
- **Participantes:** Luiz, PM

## Contexto & objetivo
Hoje, quando a capacidade do mês esgota, o cliente não compra e some sem deixar
rastro. Objetivo: capturar o interesse (waitlist) e notificar quando abrir vaga
(cancelamento ou reconciliação). Alvo de sucesso em SC-1.

## Glossário / domínio
- **SaleMonth** *(existe)* — mês de venda, capacidade em minutos.
- **Vaga** — minutos liberados por cancelamento ou reconciliação (RN-30).
- **WaitlistEntry** *(novo)* — (cliente_email, variante_id, sale_month_id).
  Unicidade: a tripla é única (RN-W2).

## User stories & cenários
- **US-1** *(Prioridade: P1)* Como cliente, com o mês esgotado, quero entrar na
  lista informando e-mail, pra ser avisado quando abrir vaga.
  - *Teste independente:* abrir um mês esgotado, inscrever um e-mail, ver a entry persistida.
  - **Cenários:**
    1. **Dado** um mês com 20 min livres e a variante Elaborado (180 min),
       **Quando** o cliente abre a página da variante, **Então** vê o botão
       "Entrar na lista" no lugar de "Comprar".
    2. **Dado** um cliente já inscrito em (e-mail, variante, mês), **Quando** ele
       se inscreve de novo, **Então** o sistema não cria 2ª linha e responde como sucesso.
    3. *(exceção)* **Dado** um e-mail em formato inválido, **Quando** o cliente
       envia, **Então** a inscrição é recusada com mensagem de validação.

- **US-2** *(Prioridade: P2)* Como inscrito, quero receber e-mail com link de
  checkout quando abrir vaga compatível.
  - **Cenários:**
    1. **Dado** uma fila com 3 inscritos numa variante, **Quando** abre vaga com
       minutos ≥ work_minutes, **Então** só o 1º da fila (FIFO) recebe e-mail com link.
    2. **Dado** que o 1º da fila recebeu o e-mail, **Quando** passa a janela de
       reserva ⟨X h — DA-1⟩ sem checkout, **Então** a vaga passa pro próximo da fila.
    3. *(exceção)* **Dado** vaga aberta e fila vazia, **Quando** o sistema
       processa, **Então** nada é enviado e a vaga segue disponível pra compra normal.

- **US-3** *(Prioridade: P3)* Como artesã (admin), quero ver a lista por mês pra
  dimensionar capacidade futura.
  - **Cenários:**
    1. **Dado** um mês com inscritos, **Quando** a admin abre o painel do mês,
       **Então** vê a lista (e-mail, variante, data) em ordem de inscrição.

## Regras de negócio
- **RN-W1** *(estado)* **Enquanto** `minutos_disponíveis < work_minutes` da
  variante, o sistema deve exibir "Entrar na lista" no lugar de "Comprar".
  *Ex: mês com 20 min livres, Elaborado pede 180 → mostra waitlist.*
  *(verifica: US-1 cenário 1)*
- **RN-W2** *(indesejado)* **Se** já existe inscrição em (email, variante, mês),
  **então** o sistema não deve criar 2ª entrada e deve responder como sucesso.
  *Ex: 2º envio igual → 1 linha, resposta de sucesso.* *(verifica: US-1 cenário 2)*
- **RN-W3** *(evento)* **Quando** `minutos_liberados ≥ work_minutes`, o sistema
  deve notificar o 1º inscrito da fila em ordem FIFO. *Ex: fila [A,B,C] → e-mail
  só pro A.* *(verifica: US-2 cenário 1)*
- **RN-W4** *(evento)* **Quando** a janela de reserva ⟨X h — DA-1⟩ expira sem
  checkout, o sistema deve liberar a vaga pro próximo da fila. *(verifica: US-2 cenário 2)*
- **RN-W5** *(evento)* **Quando** o mês de venda encerra, o sistema deve expirar
  as inscrições abertas ⟨ou rolar pro próximo mês? — DA-2⟩.

## Fluxos
**Happy:** mês esgota → cliente entra na lista → admin cancela um pedido →
sistema detecta vaga → e-mail FIFO → cliente fecha checkout na janela.
**Exceções / edge cases:** vaga abre e fila vazia; inscrito já comprou outra
variante; e-mail inválido/bounce; dois cancelamentos simultâneos liberando vaga
pro mesmo 1º da fila (concorrência — confirmar tratamento).

## Critérios de sucesso (mensuráveis)
- **SC-1** ⟨30%?⟩ dos inscritos numa vaga convertem em checkout dentro da janela
  de reserva. *(alvo a confirmar — DA-4)*
- **SC-2** Zerar os meses esgotados sem captura de interesse (hoje 100% some sem rastro).

## Fora de escopo
Cobrança antecipada · prioridade paga · push no app.

## Dúvidas em aberto
- **DA-1** Janela de reserva do e-mail = quantas horas? *(dono: PM · próxima agenda)*
- **DA-2** Inscrição expira no fim do mês ou rola pro próximo? *(dono: PM)*
- **DA-3** Notifica por variante exata ou qualquer que caiba nos minutos? *(dono: PM/Tech)*
- **DA-4** Alvo de conversão (SC-1) = quanto? *(dono: PM)*

## ⚠️ Gaps detectados na transcrição
- "do jeito que a gente fez na reserva" → qual TTL? Assumi 30 min
  (ReservationGroup atual) — **confirmar**.
- "manda o e-mail igual o de confirmação" → template não definido aqui;
  referenciar o entregável de e-mail transacional do Marco 1D.
- US-2 cenário 2 sem "Então" fechado pra quem perdeu a janela: volta pro fim da
  fila ou sai? — **confirmar** (vira DA se persistir).
- SC-1 sem número (alvo de conversão) → DA-4.

## Changelog por agenda
- **2026-06-13** — criação. Novo: US-1..3 (com cenários Dado/Quando/Então),
  RN-W1..W5 (estruturadas), SC-1..2, glossário WaitlistEntry. Pendências: DA-1..4.
  Suposição a confirmar: TTL de vaga = 30 min.
