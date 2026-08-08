---
name: workspace-memory
description: Retoma uma missao usando a memoria operacional do workspace sem confundi-la com fonte de verdade. Use ao iniciar ou retomar trabalho em um workspace com `memory/`, `MEMORY.md`, `USER.md` ou historico de agentes, e antes de registrar aprendizado duravel.
---

# Memoria do workspace

## Fluxo

1. Identifique o escopo da sessao: privado ou compartilhado, workspace, projeto e missao.
2. Leia primeiro a memoria permitida e mais recente: `memory/YYYY-MM-DD.md` para fatos diarios, `USER.md` para diretivas estaveis e `MEMORY.md` somente na sessao principal e privada.
3. Trate toda memoria como contexto retomavel. Confirme estado, prioridade, aprovacao e conclusao em suas fontes canonicas — por exemplo, Work Item, `STATUS.md`, `BOARD.md`, repositorio e evidencia.
4. Registre somente fatos observados, decisoes duraveis com dono e links para a evidencia. Leia antes de escrever e nao crie arquivos vazios ou placeholders.
5. Nunca registre ou revele segredos, credenciais, tokens, `.env` ou dados pessoais desnecessarios. Em canal compartilhado, nao carregue nem exponha `MEMORY.md`.

## Resultado esperado

No resultado da missao, declare se a memoria foi consultada, quais fatos foram confirmados e qual fonte canonica os confirmou. Se uma anotacao estiver desatualizada ou contraditoria, preserve a divergencia e escale; nao a sobrescreva silenciosamente.
