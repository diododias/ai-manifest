# Tools

A camada de permissão do harness define quais ferramentas o agente está autorizado a invocar, com que limites, e o que exige autorização humana antes de prosseguir. Essa definição é estrutural — não vive em instruções de prompt, mas em arquivos versionados dentro do repositório.

## `.agent/settings.json`

O arquivo `settings.json` declara os limites operacionais do agente naquele repositório: quais tools estão permitidas, quais estão explicitamente proibidas, quais modelos podem ser usados e qual é o threshold de confiança abaixo do qual o agente deve escalar. Um agente que não encontra esse arquivo deve tratar o repositório como não autorizado para operação autônoma.

```json
{
  "tools": {
    "allowed": ["read_file", "write_file", "run_tests", "run_lint"],
    "forbidden": ["delete_branch", "force_push", "modify_ci"]
  },
  "models": {
    "default": "claude-sonnet-5",
    "max_cost_per_task_usd": 2.00
  },
  "escalation": {
    "confidence_threshold": 0.85,
    "max_retries_before_escalation": 2
  }
}
```

## `.agent/permissions.md`

O arquivo `permissions.md` descreve, em linguagem natural, o que exige autorização humana naquele repositório específico. Ele complementa o `settings.json` com o julgamento que nenhum JSON consegue capturar: quando a situação é ambígua o suficiente para parar.

Categorias típicas cobertas por esse arquivo incluem paths que exigem owner antes de qualquer mudança, operações que alteram estado persistido (migrações, schemas, secrets), ações irreversíveis com janela de rollback limitada, e qualquer mudança que afete os próprios gates de verificação.

## `scripts/verify.sh`

O script `verify.sh` é a entrada única de todas as verificações locais. Hooks, CI e agente chamam o mesmo script. Sem essa centralização, a verificação local e a de CI divergem — e a divergência aparece da forma mais cara: o agente entrega, o CI reprova, e ninguém consegue reproduzir localmente.

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "→ lint"
npm run lint

echo "→ typecheck"
npm run typecheck

echo "→ unit tests"
npm run test:unit

echo "→ architecture check"
npm run arch:check

echo "✓ verify.sh concluído"
```

O script deve produzir mensagens acionáveis em caso de falha — arquivo, regra violada e correção esperada. Um gate que só diz "falhou" transfere para a revisão humana o trabalho que ele existia para evitar.

## LSP, lint e formatação

O Language Server Protocol (LSP) é o canal por onde o agente recebe diagnósticos em tempo real sem precisar invocar compilador ou test runner. Um repositório com LSP configurado devolve erros de tipo, referências inválidas e avisos de lint no momento em que o código é escrito — não na próxima execução de `verify.sh`.

Lint e formatação determinística (Prettier, Black, gofmt) não são checagens de estilo: são a primeira defesa contra divergência entre o que o agente gera e o que o repositório aceita. A configuração deve ser compartilhada — `.eslintrc`, `pyproject.toml`, `.editorconfig` — e versionada junto com o código. Quando lint e formatação rodam no pre-commit como sensors, o ciclo de correção fica dentro da máquina do agente.

## Typecheck e análise estática

Typecheck é o gate mais barato para capturar contratos quebrados entre módulos. TypeScript (`tsc --noEmit`), mypy, rustc e equivalentes devem rodar antes dos testes — um erro de tipo torna o resultado dos testes ambíguo.

Análise estática vai além do tipo: verifica fluxo de dados, dependências proibidas entre módulos (ArchUnit, dependency-cruiser) e padrões que o lint não captura. O resultado de uma análise estática bem configurada é que o agente sabe, antes de abrir um PR, se a mudança viola uma fronteira de arquitetura declarada nas rules.

## Navegação e compreensão da codebase

Um agente que navega o repositório às cegas — procurando por string, abrindo arquivos sequencialmente — gasta contexto sem precisão. Ferramentas de compreensão de codebase convertem esse custo em uma operação direcionada.

**Serena** oferece navegação semântica sobre o repositório: encontrar declarações, listar implementações de uma interface, mapear referências de um símbolo. Em vez de grep, o agente usa `find_symbol`, `find_implementations`, `find_referencing_symbols` — e chega ao ponto certo sem varredura linear. Serena é o ponto de partida recomendado para qualquer tarefa de discovery antes de implementação.

**Dora** complementa Serena com uma camada de observabilidade sobre o próprio processo de desenvolvimento: rastreia o que foi tocado, o que mudou entre sessões, e onde o trabalho parou. Em repositórios com múltiplas sessões de agente operando em paralelo, Dora é o mecanismo que evita que duas sessões trabalhem sobre a mesma região sem coordenação.

## Redução e gestão de contexto

Contexto é o recurso mais escasso de uma sessão de agente. Carregá-lo sem critério — arquivos inteiros quando só um símbolo é necessário, histórico completo quando só o delta importa — é o caminho mais direto para sessões longas que perdem coerência.

**RTK (Repo Tool Kit)** é o conjunto de ferramentas de gestão de contexto do repositório. Ele expõe operações de leitura seletiva — ler só os símbolos relevantes para a tarefa atual, recuperar o estado de uma sessão anterior sem recarregar o histórico completo, e compactar evidência já verificada antes que ela ocupe espaço do que ainda está sendo trabalhado. Um repositório sem RTK transfere para o agente a responsabilidade de decidir o que lembrar — e essa decisão, feita sem instrução explícita, tende para o excesso.

## Testes, containers e observabilidade

Testes são a camada de verificação mais custosa de executar e mais cara de ignorar. A separação entre níveis — unitário, integração, contrato, end-to-end — define qual ferramenta está disponível em qual gate. Testes unitários rodam sem dependências externas e pertencem ao pre-commit. Testes de integração exigem serviços e pertencem ao pre-push ou CI.

Containers (Docker, Testcontainers) são o mecanismo que torna testes de integração reproduzíveis sem estado compartilhado. Um repositório que não usa containers para isolar testes de integração introduz dependência de ambiente — e o agente que reproduz localmente o que o CI vai executar precisa do mesmo ambiente, não de uma aproximação.

Observabilidade — logs estruturados, traces distribuídos, métricas com baseline — fecha o ciclo de verificação no pós-deploy. A diferença entre um deploy e um rollout controlado é que o segundo tem um baseline definido antes e um critério objetivo de rollback se o baseline for violado. O agente não decide rollback: ele lê o sinal de observabilidade e escala se o critério for atingido.
