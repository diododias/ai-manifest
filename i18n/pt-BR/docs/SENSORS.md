# Sensors

Sensors são verificações que rodam localmente, antes que o código deixe a máquina do agente. São a primeira camada da escada de verificação — as mais baratas de executar, as que devolvem feedback mais rápido.

## `.hooks/` — versionados com o repositório

Os sensors ficam em `.hooks/` e são versionados junto com o código, portanto todo clone carrega os mesmos checks que o time executa.

```bash
# instalar os sensors do repositório — uma vez por clone
git config core.hooksPath .hooks
```

O Git não ativa hooks versionados sozinho: `core.hooksPath` é uma configuração local, e um clone novo não roda sensor algum até que ela seja definida. Essa linha, portanto, faz parte da instalação, não é uma sugestão — ela pertence ao script de bootstrap e ao bloco de comandos do `AGENTS.md`, e sua ausência é exatamente o tipo de lacuna silenciosa que [Falha](FAILURE.md) existe para detectar.

Sensors versionados eliminam a divergência entre o que o agente verifica localmente e o que o time verifica em CI — uma das fontes mais comuns de falsos positivos e de "funciona aqui, falha lá".

## Pre-commit

O sensor de pre-commit roda a cada commit e deve completar em segundos. Seu escopo: checks determinísticos e de baixo custo — formatação, linting, typecheck, testes unitários afetados e secret scanning.

Lint e typecheck são sensores, não gates — são determinísticos, rodam em segundos e falham com frequência, que é exatamente o perfil da camada local. Tratá-los como gates de CI atrasa em minutos um sinal que o agente poderia ter tido antes do commit.

Secret scanning pertence aqui por um motivo diferente dos demais. Ele não fica no início por ser barato — fica no início porque é o único check da escada cuja falha não pode ser desfeita por um gate posterior. Uma credencial que chega ao remoto está comprometida mesmo que o commit seja revertido, portanto o check precisa rodar antes de o objeto sair da máquina. `gitleaks` ou `trufflehog` no pre-commit, e a proteção contra push da plataforma como segunda linha, formam a combinação padrão.

Uma falha deve indicar exatamente o que está errado e como corrigir. Um sensor que apenas diz "falhou" obriga o agente a tentar novamente sem informação — cada tentativa desperdiça um ciclo.

## Pre-push

O sensor de pre-push roda antes do push e tolera mais tempo. É o lugar certo para verificações que precisam de contexto maior: testes de integração locais, verificação de arquitetura entre módulos, e checagem de que `scripts/verify.sh` passa por completo.

O critério de posicionamento é a razão entre custo de execução e frequência de falha. Check barato que falha com frequência: pre-commit. Check que precisa de mais contexto ou tempo: pre-push.

## Escopo: como um único entrypoint continua rápido

`scripts/verify.sh` é o único entrypoint dos checks locais ([Tools](TOOLS.md#scriptsverifysh)), e um sensor precisa responder em segundos. Esses dois requisitos só coexistem se o entrypoint receber o escopo como argumento:

| Invocação | Cobre | Chamado por |
|---|---|---|
| `verify.sh --staged` | apenas o que está no índice | pre-commit |
| `verify.sh --affected` | os paths alterados e aquilo que depende deles | pre-push |
| `verify.sh --full` | tudo, sem seleção de paths | CI e, localmente, antes de solicitar revisão |

Sem esse contrato, o repositório escolhe uma entre duas falhas: o hook chama o script completo e o commit leva minutos, ou o hook reimplementa um check mais estreito e a verificação local silenciosamente deixa de corresponder à CI. O escopo é um argumento justamente para que a *lógica* permaneça em um único lugar enquanto o *custo* varia por gate.

Um sensor pulado precisa ser reportado como pulado, nunca como aprovado — ver [Falha](FAILURE.md#um-gate-que-não-rodou-não-passou).

---

*Próximo: [Gates](GATES.md) — onde cada check pertence, do commit ao deploy.*
