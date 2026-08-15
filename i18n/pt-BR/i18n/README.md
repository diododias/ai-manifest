# Tradução

Este repositório publica sua documentação em **inglês (`en`)** e **português brasileiro (`pt-BR`)** a partir de um único branch. Esta página é o contrato de como isso funciona.

## O modelo: um branch, um diretório por idioma

A documentação vivia com um idioma por branch. Isso não funciona: branches divergem estruturalmente, `git merge` não sabe mesclar tradução, e toda reestruturação de um lado silenciosamente órfã o outro. A árvore em inglês ganhou `kb-store/` enquanto o branch em português ainda tinha `docs/` — as duas deixaram de ser a mesma documentação.

O modelo aqui é o usado pelo Docusaurus, pelo Astro Starlight e pela documentação do Kubernetes: **a árvore canônica na raiz do repositório é o idioma-fonte, e todo outro idioma espelha os mesmos caminhos sob `i18n/<locale>/`.**

```
README.md                      canônico (en)
docs/TOOLS.md                  canônico (en)
i18n/pt-BR/README.md           tradução de README.md
i18n/pt-BR/docs/TOOLS.md       tradução de docs/TOOLS.md
i18n/pt-BR/_manifest.json      de qual versão canônica cada tradução foi feita
i18n/ui.json                   strings de interface e metadados de seção, por idioma
i18n/GLOSSARY.md               terminologia que precisa permanecer consistente
```

O caminho depois de `i18n/<locale>/` é sempre idêntico ao caminho canônico. Nada mais precisa ser configurado: o espelho *é* o mapeamento.

O idioma-fonte é declarado uma vez, em `SOURCE_LOCALE` no `scripts/i18n.py` e no `scripts/build-docs-site.py`. Mudar qual idioma é canônico é uma alteração de uma linha mais a renomeação de um diretório.

## Fallback: uma tradução ausente é visível, nunca invisível

O site gera um arquivo por idioma — `index.html` e `index.pt.html`. Quando uma página não tem tradução, o idioma cai para o texto canônico e exibe um aviso no topo dessa página dizendo isso. Um leitor nunca é servido silenciosamente com o idioma errado, e uma lacuna nunca bloqueia uma publicação.

## Defasagem: medida, não descoberta pelo leitor

O modo de falha real de uma documentação bilíngue não é o arquivo ausente, é a tradução que ficou para trás enquanto o original mudou. O `_manifest.json` registra o SHA-256 do arquivo canônico **no momento em que ele foi traduzido**. Comparar esse carimbo com o arquivo canônico de hoje dá a cada página um de quatro estados:

| Estado | Significado |
|---|---|
| `current` | a tradução corresponde à versão canônica da qual foi carimbada |
| `outdated` | o arquivo canônico mudou depois que a tradução foi escrita |
| `missing` | não existe arquivo de tradução; a página cai para o idioma-fonte |
| `orphan` | existe uma tradução para um documento que não é mais publicado |

```bash
uv run scripts/i18n.py status              # relatório completo por arquivo
uv run scripts/i18n.py status --summary    # apenas as contagens
uv run scripts/i18n.py status --porcelain  # uma linha por arquivo, para ferramentas
```

O hash ignora ruído de fim de linha e de espaço em branco no fim da linha, então uma reformatação não marca a página como defasada.

## O fluxo

**Mudar um documento.** Edite o arquivo canônico normalmente. Não trave esperando a tradução — o `status` vai reportar a página como `outdated` e o site continua publicando.

**Traduzir.** Edite o arquivo espelhado sob `i18n/<locale>/` e depois registre de qual versão canônica você traduziu:

```bash
uv run scripts/i18n.py stamp docs/TOOLS.md
```

Carimbar é afirmar que a tradução reflete o arquivo canônico como ele está agora. Carimbar sem traduzir é a única coisa que quebra este sistema, porque torna a defasagem invisível de novo.

**Adicionar uma página.** Adicione-a a `PAGES` no `scripts/build-docs-site.py`. Ela é publicada imediatamente em todos os idiomas, caindo para o idioma-fonte onde ainda não estiver traduzida.

**Mudar uma string de interface.** Edite o `i18n/ui.json` para todos os idiomas. O build falha se um idioma estiver sem uma chave — strings de interface nunca caem silenciosamente para o idioma-fonte.

**Adicionar um idioma.** Crie `i18n/<locale>/`, adicione um bloco ao `i18n/ui.json` com as mesmas chaves, e adicione uma entrada a `LOCALES` no `scripts/build-docs-site.py` e a `TARGET_LOCALES` no `scripts/i18n.py`.

## Regras de tradução

1. **A terminologia vem do [`GLOSSARY.md`](GLOSSARY.md).** Termos na lista de não-traduzir permanecem em inglês em todos os idiomas — eles são o vocabulário do método, não prosa.
2. **A estrutura é espelhada, não reinventada.** Mesmos títulos, mesma ordem, mesmas tabelas, mesmos blocos de código. O site deriva a navegação e o índice a partir dos títulos, e uma página que os reordena deixa de corresponder à sua contraparte.
3. **Âncoras são localizadas.** Um link para `RULES.md#the-testing-strategy-as-a-rule` vira o slug do título *traduzido*. Slugs preservam acentos (`#a-estratégia-de-testes-como-rule`).
4. **Links relativos permanecem canônicos.** Escreva `docs/TOOLS.md`, não `i18n/pt-BR/docs/TOOLS.md`. O build resolve cada link para o idioma certo.
5. **O front matter também é traduzido** — `title`, `description` e `summary` são renderizados.
6. **Código, comandos, caminhos e identificadores nunca são traduzidos.** Apenas a prosa ao redor deles.

## Sensor, não gate

O `i18n.py status` é um **sensor**: reporta e sai com 0. Defasagem de tradução é informação de que o autor precisa, não motivo para bloquear um commit que no mais está correto — segurar uma correção em inglês como refém da sua tradução é como a documentação deixa de ser atualizada. Passe `--strict` para que ele saia com código diferente de zero onde um pipeline genuinamente queira isso.

## Importar traduções que vivem em outro lugar

O `adopt` importa texto traduzido de outra ref do git, que foi como o branch em português foi incorporado a esta estrutura:

```bash
uv run scripts/i18n.py adopt --from main --source-ref 16f3664 \
  --rename workspaces/tech-lead/docs=workspaces/tech-lead/kb-store
```

`--from` é a ref que contém o texto traduzido, `--source-ref` é a versão canônica da qual esse texto foi traduzido (ela vira o carimbo), e `--rename` mapeia prefixos de caminho que mudaram desde então. Arquivos cujo texto na ref é idêntico ao texto canônico atual não são traduções e ficam como `missing`.
