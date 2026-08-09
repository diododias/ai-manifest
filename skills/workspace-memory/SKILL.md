---
name: workspace-memory
description: Retoma uma missão usando a memória operacional do workspace sem confundi-la com fonte de verdade. Use ao iniciar ou retomar trabalho em um workspace com `memory/`, `MEMORY.md`, `USER.md` ou histórico de agentes, e antes de registrar aprendizado durável.
---

# Memória do workspace

## Fluxo

1. Identifique o escopo da sessão: privado ou compartilhado, workspace, projeto e missão.
2. Leia primeiro a memória permitida e mais recente: `memory/YYYY-MM-DD.md` para fatos diários, `USER.md` para diretivas estáveis e `MEMORY.md` somente na sessão principal e privada.
3. Trate toda memória como contexto retomável. Confirme estado, prioridade, aprovação e conclusão em suas fontes canônicas — por exemplo, Work Item, `STATUS.md`, `BOARD.md`, repositório e evidência.
4. Registre somente fatos observados, decisões duráveis com dono e links para a evidência. Leia antes de escrever e não crie arquivos vazios ou placeholders.
5. Nunca registre ou revele segredos, credenciais, tokens, `.env` ou dados pessoais desnecessários. Em canal compartilhado, não carregue nem exponha `MEMORY.md`.

## Resultado esperado

No resultado da missão, declare se a memória foi consultada, quais fatos foram confirmados e qual fonte canônica os confirmou. Se uma anotação estiver desatualizada ou contraditória, preserve a divergência e escale; não a sobrescreva silenciosamente.
