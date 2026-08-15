# Tools

Esta página é o índice de ferramentas do harness: de quais categorias de tool um agente precisa, o que cada uma oferece e onde roda na escada de verificação. Ela responde *o que instalar*.

Ela não responde *o que o agente está autorizado a invocar* — essa é a camada de permissão, e vive em [Permissões](PERMISSIONS.md). A distinção importa porque as duas envelhecem em ritmos diferentes: um modelo de permissão é propriedade do método e muda raramente, enquanto uma recomendação de ferramenta tem vida útil medida em meses. Mantê-las no mesmo documento fez a metade estável herdar a volatilidade da outra.

> **Índice de referência, revisado em 2026-08.** As tools nomeadas são o padrão atual de cada categoria no momento desta revisão, não uma imposição. Um repositório adota a linha que corresponde a seu stack e ao posicionamento de seus gates. Quando uma recomendação envelhece, a categoria e o critério de posicionamento ao redor permanecem válidos — substitua o nome, mantenha o raciocínio.

## `scripts/verify.sh`

O script `verify.sh` é a entrada única de todas as verificações locais. Hooks, CI e agente chamam o mesmo script. Sem essa centralização, a verificação local e a de CI divergem — e a divergência aparece da forma mais cara: o agente entrega, o CI reprova, e ninguém consegue reproduzir localmente.

Um único entrypoint e um sensor que responde em segundos são requisitos conflitantes, a menos que o escopo seja um argumento. O script recebe um:

| Invocação | Cobre | Chamado por |
|---|---|---|
| `verify.sh --staged` | apenas o que está no índice | pre-commit |
| `verify.sh --affected` | os paths alterados e aquilo que depende deles | pre-push |
| `verify.sh --full` | tudo, sem seleção de paths | CI e, localmente, antes de solicitar revisão |

Os estágios abaixo são o corpo de `--full`; os modos mais estreitos rodam os mesmos estágios sobre um conjunto menor de arquivos. Manter a seleção dentro do script — em vez de deixar cada hook implementar a própria — é o que impede a verificação local de se afastar silenciosamente da CI.

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

Conforme o repositório amadurece além do HL1, o `verify.sh` normalmente ganha estágios além desses quatro gates de base — cobertura por mutação, código morto e checagem de dependências circulares são as adições mais comuns. Cada estágio deve continuar sendo um script independente (`test:mutation`, `deadcode:check`, `deps:circular`) para que um estágio que falha possa ser executado, pulado ou depurado isoladamente:

```bash
echo "→ mutation testing"
npm run test:mutation

echo "→ dead code"
npm run deadcode:check

echo "→ circular dependencies"
npm run deps:circular
```

Esses estágios são mais caros que lint ou typecheck e pertencem ao pre-push ou ao CI, não ao pre-commit — veja [Sensores](SENSORS.md) e [Gates](GATES.md) para o critério de posicionamento.

## LSP, lint e formatação

O Language Server Protocol (LSP) é o canal por onde o agente recebe diagnósticos em tempo real sem precisar invocar compilador ou test runner. Um repositório com LSP configurado devolve erros de tipo, referências inválidas e avisos de lint no momento em que o código é escrito — não na próxima execução de `verify.sh`.

Lint e formatação determinística (Prettier, Black, gofmt) não são checagens de estilo: são a primeira defesa contra divergência entre o que o agente gera e o que o repositório aceita. A configuração deve ser compartilhada — `.eslintrc`, `pyproject.toml`, `.editorconfig` — e versionada junto com o código. Quando lint e formatação rodam no pre-commit como sensors, o ciclo de correção fica dentro da máquina do agente.

Biome e Ruff são a geração atual dessas checagens: ferramentas de binário único, escritas em Rust, que substituem ESLint+Prettier (Biome, para JS/TS/JSON/CSS) ou flake8+Black (Ruff, para Python) por um único arquivo de configuração e execuções ordens de magnitude mais rápidas. Não são obrigatórias — ESLint e Black seguem sendo escolhas válidas — mas um repositório que define seu stack de lint hoje deveria adotá-las por padrão, a menos que um plugin só exista no ecossistema antigo.

## Typecheck e análise estática

Typecheck é um sensor, não um gate: roda localmente, em segundos, e pertence ao pre-commit junto com o lint — a camada mais barata da escada de verificação ([Sensores](SENSORS.md)). É a forma mais barata de capturar contratos quebrados entre módulos. TypeScript (`tsc --noEmit`), mypy ou Pyright, rustc e equivalentes devem rodar antes dos testes — um erro de tipo torna o resultado dos testes ambíguo.

Análise estática vai além do tipo: verifica fluxo de dados, dependências proibidas entre módulos (ArchUnit, dependency-cruiser) e padrões que o lint não captura. O resultado de uma análise estática bem configurada é que o agente sabe, antes de abrir um PR, se a mudança viola uma fronteira de arquitetura declarada nas rules.

## Navegação e compreensão da codebase

Um agente que navega o repositório às cegas — procurando por string, abrindo arquivos sequencialmente — gasta contexto sem precisão. Ferramentas de compreensão de codebase convertem esse custo em uma operação direcionada.

**Serena** ([oraios/serena](https://github.com/oraios/serena)) oferece navegação semântica sobre o repositório: encontrar declarações, listar implementações de uma interface, mapear referências de um símbolo. Em vez de grep, o agente usa `find_symbol`, `find_implementations`, `find_referencing_symbols` — e chega ao ponto certo sem varredura linear. Roda como servidor MCP, opera no nível de símbolo em TypeScript, Python, Java, C# e outras linguagens, e é o ponto de partida recomendado para qualquer tarefa de discovery antes de implementação.

**dora-cli** complementa Serena com uma camada de observabilidade sobre o próprio processo de desenvolvimento — não sobre a codebase, mas sobre como ela foi produzida. Calcula as quatro métricas DORA (frequência de deploy, lead time para mudanças, taxa de falha em mudanças, tempo de restauração) direto do histórico do git e do GitHub. Em repositórios com múltiplas sessões de agente operando em paralelo, esse é o sinal que mostra se o ritmo de mudança está de fato melhorando a entrega, e não apenas produzindo mais commits.

**Graphify** vai uma camada mais fundo que Serena: em vez de consultas pontuais sob demanda, constrói de antemão um grafo de conhecimento persistente de todo o repositório — código, schemas SQL, configs e docs — usando parsing AST local (tree-sitter), com zero chamadas a LLM e nada saindo da máquina. O ganho aparece em repositórios grandes ou desconhecidos, onde uma única consulta ao grafo substitui dezenas de leituras exploratórias. É um setup mais pesado que o da Serena e vale a adoção quando o custo de discovery — não o de implementação — vira o gargalo.

## Redução e gestão de contexto

Contexto é o recurso mais escasso de uma sessão de agente. Carregá-lo sem critério — arquivos inteiros quando só um símbolo é necessário, histórico completo quando só o delta importa, saída bruta de comando quando só a linha da falha importa — é o caminho mais direto para sessões longas que perdem coerência.

**RTK** ([rtk-ai](https://github.com/rtk-ai)) é um proxy de CLI de binário único que intercepta a saída de comandos comuns de desenvolvimento — `pytest`, `cargo test`, `go test` e mais de 30 outros — e filtra, comprime e reformata essa saída antes que ela chegue ao contexto do agente. Remove boilerplate e linhas redundantes com overhead abaixo de 10 ms, tipicamente eliminando 60–90% do ruído da saída bruta de um comando.

**Repomix** empacota um repositório inteiro — respeitando o `.gitignore` — em um único arquivo amigável a IA, com contagem de tokens por arquivo e compressão opcional via tree-sitter. É a ferramenta certa quando a tarefa precisa de um retrato único da codebase, em vez de consultas incrementais por símbolo; Serena e Graphify seguem preferíveis para consultas direcionadas e repetidas.

**Headroom** opera como proxy ou servidor MCP que comprime saídas de ferramentas, logs, arquivos e chunks de RAG antes que cheguem ao modelo, mantendo os originais comprimidos recuperáveis sob demanda (compress-cache-retrieve). A redução reportada é de 60–95% em saídas estruturadas como JSON e logs, e em torno de 20% no tráfego geral de um agente de código.

Um repositório sem nenhuma dessas ferramentas transfere para o agente a responsabilidade de decidir o que lembrar — e essa decisão, feita sem instrução explícita, tende para o excesso.

## Saúde estrutural do código

Lint e typecheck capturam problemas no nível da sintaxe e do contrato. Uma classe separada de ferramenta é necessária para problemas que só são visíveis no nível do grafo de dependências ou do próprio design — problemas que compilam sem erro e passam em todos os testes, mas tornam a codebase mais difícil de mudar com segurança ao longo do tempo.

**Dependências circulares.** Madge gera um grafo visual de dependências para projetos JS/TS e aponta ciclos diretamente — captura apenas ciclos diretos, não ciclos que passam por um terceiro módulo. O `dependency-cruiser`, já citado acima para fronteiras de arquitetura, também valida ciclos e pode ser integrado ao ESLint via `eslint-plugin-dependency-cruiser`. A regra `no-cycle` do `eslint-plugin-import` captura a mesma classe de problema inline durante o lint, sem ferramenta separada. Repositórios Python usam **import-linter** para impor arquitetura em camadas e proibir ciclos entre módulos — o mesmo papel que o ArchUnit cumpre em Java.

**Código morto.** **Knip** é o padrão atual para JS/TS: encontra exports não usados, arquivos não usados e dependências não usadas analisando o manifesto e o código-fonte em conjunto, com modo de auto-fix e saída amigável a CI (o `ts-prune` cobria uma fatia mais estreita do mesmo problema e hoje está em manutenção — prefira Knip em setups novos). **Vulture** faz o equivalente em Python via análise de AST com pontuação de confiança, o que importa dado quanto os padrões dinâmicos do Python produzem falsos positivos. **depcheck** estreita ainda mais o escopo, para entradas não usadas apenas no `package.json`.

**SOLID e design smells.** SonarQube/SonarLint é o padrão multi-linguagem e a opção pela qual a maioria dos repositórios deveria começar, já que cobre lint, segurança e code smell em uma única passada. Onde é necessária detecção mais profunda no nível de design: NDepend mede aderência a SOLID diretamente para .NET; DesigniteJava classifica code smells de Java pelo princípio de design que violam; PMD e Checkstyle capturam problemas de convenção e complexidade em Java que frequentemente correlacionam com violações de SOLID, ainda que não nomeiem o princípio explicitamente.

Essas checagens são mais caras de interpretar que lint — uma dependência circular ou uma violação de SOLID exige um julgamento sobre escopo de refatoração, não apenas uma correção. Pertencem à trilha profunda de CI descrita em [Gates](GATES.md), não ao pre-commit.

## Secrets e risco de dependências

Dois checks desta classe diferem de todos os anteriores em um aspecto: falham por coisas que o agente não escreveu.

**Secret scanning** é o único check da escada cuja falha um gate posterior não consegue desfazer. Uma credencial que chega ao remoto está comprometida mesmo depois de um revert, portanto o check roda antes de o objeto sair da máquina. **gitleaks** é o padrão comum — binário único, regex mais entropia, rápido o bastante para pre-commit; **trufflehog** vai além ao verificar se uma credencial encontrada está ativa, e seu tempo extra vale a pena na CI, não em um hook. A proteção contra push da própria plataforma é a segunda linha, nunca a primeira: ela captura o que o sensor local não detectou, e faz isso depois que o objeto já existe.

**Checks de dependências e supply chain** respondem a uma pergunta que os testes do próprio repositório não conseguem: se o código que ele traz para dentro é seguro para executar. **Dependabot** ou **Renovate** mantêm versões atualizadas e abrem o upgrade como uma mudança revisável; a revisão continua necessária, porque um upgrade automatizado é uma mudança como qualquer outra. **npm audit**, **pip-audit** e **osv-scanner** informam vulnerabilidades conhecidas contra o manifesto, e uma **SBOM** (syft ou o gerador nativo da plataforma) registra o que realmente foi entregue, que é aquilo de que uma resposta a incidente precisa e que nenhum lockfile fornece depois do fato. **Semgrep** e **CodeQL** cobrem a fatia de SAST — padrões perigosos, e não apenas incorretos.

O posicionamento segue o critério habitual com uma exceção. Secret scanning é barato e vai para o pre-commit; SAST, SBOM e scanning de vulnerabilidades são caros e pertencem à deep lane. A exceção é uma mudança de dependência: adicionar ou atualizar uma dependência executa o conjunto completo para aquele path antes do merge, porque esse é o momento em que o risco entra no repositório e porque — como explica [Confiança](TRUST.md#o-harness-é-uma-supply-chain) — uma nova dependência do próprio *harness* é código com acesso à sessão do agente.

## Testes, containers e observabilidade

Testes são a camada de verificação mais custosa de executar e mais cara de ignorar. A separação entre níveis — unitário, integração, contrato, end-to-end — define qual ferramenta está disponível em qual gate. Testes unitários rodam sem dependências externas e pertencem ao pre-commit. Testes de integração exigem serviços e pertencem ao pre-push ou CI.

Teste de mutação é o gate que responde a uma pergunta que cobertura não responde: se os testes existentes de fato capturariam uma regressão, e não apenas executariam a linha. **Stryker** cobre JS/TS e, separadamente, .NET via analisadores Roslyn, com gating de CI por threshold (high/low/break) e relatório em HTML. **PIT** é o equivalente para Java, com análise incremental para manter execuções rápidas em suítes grandes. **mutmut** cobre Python, com uma flag `--CI` que produz códigos de saída apropriados para pipeline. Teste de mutação é o item mais caro da [escada de testes](RULES.md#a-estratégia-de-testes-como-rule) e pertence ao fim da trilha profunda de CI, executado em agenda ou antes do merge — nunca a cada commit.

Containers (Docker, Testcontainers) são o mecanismo que torna testes de integração reproduzíveis sem estado compartilhado. Um repositório que não usa containers para isolar testes de integração introduz dependência de ambiente — e o agente que reproduz localmente o que o CI vai executar precisa do mesmo ambiente, não de uma aproximação.

Observabilidade — logs estruturados, traces distribuídos, métricas com baseline — fecha o ciclo de verificação no pós-deploy. A diferença entre um deploy e um rollout controlado é que o segundo tem um baseline definido antes e um critério objetivo de rollback se o baseline for violado. O agente não decide rollback: ele lê o sinal de observabilidade e escala se o critério for atingido.

## Git hooks e automação local

Sensores precisam de um mecanismo de instalação que sobreviva a um clone novo sem setup manual. O padrão descrito em [Sensores](SENSORS.md) são hooks nativos do Git versionados em `.hooks/` e ativados com `git config core.hooksPath .hooks` — agnóstico de linguagem, sem dependências, e o padrão certo para repositórios poliglotas ou não-JS.

**Husky** é o equivalente para repositórios centrados em JS/TS: instala os hooks automaticamente via um script `prepare` do npm, de modo que todo `npm install` re-sincroniza o `.husky/` sem um passo manual de `git config`, e é a convenção que a maioria dos contribuidores JS/TS já espera. Adote Husky no lugar da abordagem nativa `.hooks/` quando o repositório for exclusivamente JS/TS e o atrito de onboarding de um `git config` manual superar o valor de permanecer agnóstico de linguagem; mantenha hooks nativos em qualquer repositório que misture stacks ou onde a lógica do hook precise permanecer portátil fora do ecossistema npm.

---

## Todas as ferramentas citadas, classificadas por tipo de uso

A tabela abaixo consolida todas as ferramentas nomeadas neste documento. É um índice de referência, não um mandato — um repositório adota a linha que corresponde ao seu stack e ao seu posicionamento de gate, não a tabela inteira.

| Ferramenta | Tipo de uso | Stack / observações |
|---|---|---|
| Serena | Navegação de codebase | nível de símbolo, servidor MCP, multi-linguagem |
| LSP (language server) | Navegação de codebase | diagnósticos em tempo real, nível de IDE |
| Graphify | Grafo de conhecimento / mapeamento de repo | AST local (tree-sitter), 40+ linguagens, build único |
| dora-cli | Observabilidade de processo / métricas DORA | lê histórico do git + GitHub |
| RTK | Redução de contexto | proxy de CLI, comprime saída de comando |
| Repomix | Redução de contexto | empacotamento único do repo para entrada de LLM |
| Headroom | Redução de contexto | proxy/MCP, compress-cache-retrieve |
| ESLint / Prettier | Lint e formatação | JS/TS |
| Biome | Lint e formatação | JS/TS/JSON/CSS, binário único |
| Black | Formatação | Python |
| Ruff | Lint e formatação | Python, binário único |
| gofmt | Formatação | Go |
| `tsc --noEmit` | Typecheck | TypeScript |
| mypy / Pyright | Typecheck | Python |
| rustc | Typecheck | Rust |
| ArchUnit | Fronteiras de arquitetura | Java |
| dependency-cruiser | Fronteiras de arquitetura / dependências circulares | JS/TS |
| import-linter | Fronteiras de arquitetura / dependências circulares | Python |
| Madge | Dependências circulares | JS/TS, apenas ciclos diretos |
| `eslint-plugin-import` (`no-cycle`) | Dependências circulares | JS/TS, inline com o lint |
| Knip | Código morto / dependências não usadas | JS/TS, sucessor do ts-prune |
| ts-prune | Código morto (legado) | JS/TS, em manutenção — prefira Knip |
| Vulture | Código morto | Python, AST + pontuação de confiança |
| depcheck | Dependências não usadas | JS/TS, escopo apenas do `package.json` |
| SonarQube / SonarLint | SOLID / code smell / segurança | multi-linguagem |
| gitleaks | Secret scanning | binário único, rápido o bastante para pre-commit |
| trufflehog | Secret scanning | verifica se uma credencial encontrada está ativa; CI |
| Proteção contra push (plataforma) | Secret scanning | segunda linha, depois que o objeto existe |
| Dependabot / Renovate | Atualizações de dependências | abre cada upgrade como uma mudança revisável |
| npm audit / pip-audit / osv-scanner | Vulnerabilidades conhecidas | baseado no manifesto, por stack |
| Semgrep / CodeQL | SAST | padrões perigosos, deep lane |
| syft (SBOM) | Inventário de supply chain | registra o que realmente foi entregue |
| NDepend | Aderência a SOLID | .NET |
| DesigniteJava | Classificação de design smells | Java |
| PMD / Checkstyle | Convenção / complexidade | Java |
| Test runner (Jest, Vitest, pytest, `go test`, ...) | Testes unitários e de integração | por stack |
| Stryker | Teste de mutação | JS/TS, .NET |
| PIT | Teste de mutação | Java, incremental |
| mutmut | Teste de mutação | Python, códigos de saída amigáveis a CI |
| Docker / Testcontainers | Isolamento por container | testes de integração |
| Hooks nativos do Git (`.hooks/` + `core.hooksPath`) | Sensores locais / hooks | agnóstico de linguagem, padrão do repo |
| Husky | Sensores locais / hooks | convenção JS/TS, instalação gerenciada por npm |
| `scripts/verify.sh` (+ scripts por estágio) | Orquestração de gates | ponto de entrada único para checagens locais e CI |

---

*Próximo: [Rules](RULES.md) — o estado desejado do repositório e o contrato de entrada.*
