# Sensors

Sensors são verificações que rodam localmente, antes que o código deixe a máquina do agente. São a primeira camada da escada de verificação — as mais baratas de executar, as que devolvem feedback mais rápido.

## `.hooks/` — versionados com o repositório

Os sensors ficam em `.hooks/` e são versionados junto com o código. Qualquer clone instala sem configuração manual.

```bash
# instalar os sensors do repositório
git config core.hooksPath .hooks
```

Sensors versionados eliminam a divergência entre o que o agente verifica localmente e o que o time verifica em CI — uma das fontes mais comuns de falsos positivos e de "funciona aqui, falha lá".

## Pre-commit

O sensor de pre-commit roda a cada commit e deve completar em segundos. Seu escopo: checks determinísticos e de baixo custo — formatação, linting, typecheck, testes unitários afetados e verificação de secrets acidentais.

Uma falha deve indicar exatamente o que está errado e como corrigir. Um sensor que apenas diz "falhou" obriga o agente a tentar novamente sem informação — cada tentativa desperdiça um ciclo.

## Pre-push

O sensor de pre-push roda antes do push e tolera mais tempo. É o lugar certo para verificações que precisam de contexto maior: testes de integração locais, verificação de arquitetura entre módulos, e checagem de que `scripts/verify.sh` passa por completo.

O critério de posicionamento é a razão entre custo de execução e frequência de falha. Check barato que falha com frequência: pre-commit. Check que precisa de mais contexto ou tempo: pre-push.
