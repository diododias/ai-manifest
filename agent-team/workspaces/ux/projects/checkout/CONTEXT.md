# Contexto — Checkout

Após um timeout, o cliente não sabe se o pagamento foi concluído nem se uma nova tentativa é segura. UX deve tornar processamento, resultado e recuperação compreensíveis sem prometer comportamento que o sistema não garante.

## Outcome recebido

Permitir repetição segura e reduzir incerteza sobre cobrança duplicada.

## Restrições conhecidas

- a confirmação do provedor pode ser assíncrona;
- conteúdo não pode expor detalhes internos ou dados sensíveis;
- estados precisam funcionar com teclado e tecnologia assistiva.
