---
id: PLAN-001
project: ai-manifest
status: implemented
owner: tech-lead
work_items: []
updated_at: 2026-08-09
---

# Documentacao imersiva do Agent Team em `index.html`

## Resultado esperado

Disponibilizar na raiz do repositorio um `index.html` estatico, navegavel e responsivo que apresente a documentacao vigente do Agent Team em uma experiencia dark, imersiva e orientada a descoberta. A pagina inicial deve evidenciar as macrosecoes do projeto e uma piramide interativa; a selecao de uma camada deve abrir sua pagina de secao, revelar as subsecoes relacionadas e manter uma URL navegavel por hash.

O HTML sera uma camada de apresentacao gerada a partir dos Markdown existentes. Os documentos do repositorio continuam sendo a fonte de verdade, evitando divergencia entre a documentacao visual e a documentacao versionada.

## Contexto e ponto de partida

- A reorganizacao documental atual define seis pilares, da base ao topo: **Harness, Agentes, Skills, Loops, Metodologia e Workspace**.
- A raiz ja possui `scripts/build-docs-site.py`, que converte Markdown em uma pagina unica, preserva diagramas Mermaid, reescreve links e oferece busca.
- O gerador atual aponta para caminhos antigos e emite `docs/site.html`; ele deve ser evoluido, nao substituido por uma nova stack.
- O repositorio nao possui uma aplicacao web ou infraestrutura de hosting dedicada. O primeiro incremento sera estatico, sem framework, backend, autenticacao ou persistencia.
- Ha uma reorganizacao ampla em andamento na arvore de trabalho. A implementacao deve preservar essas alteracoes e se basear na estrutura documental nova.

## Escopo do primeiro incremento

### Incluido

- Gerar `index.html` na raiz do repositorio.
- Tema dark como identidade principal, usando cinza-chumbo e ciano.
- Home editorial com proposta do Agent Team, pontos de entrada e piramide interativa.
- Navegacao em drilldown: macrosecao → subsecoes → documento.
- Rotas por hash, deep link e suporte aos botoes voltar/avancar do navegador.
- Busca global por titulo, caminho e texto dos documentos incluidos.
- Sumario local do documento e destaque da secao ativa.
- Renderizacao de Markdown, tabelas, codigo e diagramas Mermaid.
- Layout responsivo para desktop, tablet e celular.
- Navegacao completa por teclado, foco visivel, semantica e modo de movimento reduzido.
- Espacos visuais preparados para novos infograficos sem exigir reestruturacao da navegacao.

### Fora do escopo deste incremento

- CMS, edicao de conteudo pela interface, login ou dados persistentes.
- Publicacao em um provedor de hosting.
- Reescrita editorial de todos os documentos Markdown.
- Producao dos infograficos finais alem da piramide; entram somente componentes e slots preparados para recebe-los.
- Multiplos arquivos HTML ou uma aplicacao com roteamento de servidor.
- Tema claro ou seletor de tema.

## Arquitetura da informacao

A home nao sera apenas um indice. Ela funcionara como mapa mental do sistema: a piramide explica a dependencia entre as camadas, enquanto os cards de acesso rapido atendem quem ja sabe o que procura.

| Nivel | Macrosecao | Pergunta respondida | Drilldown inicial |
|---:|---|---|---|
| 6, topo | **Workspace** | Onde o trabalho e os artefatos vivem? | overview, estrutura, ownership, harness do workspace, board e Work Items |
| 5 | **Metodologia** | Como as pessoas operam o sistema? | papeis, checkpoints, gatilhos, ritmos, manual, jornada e documentacao |
| 4 | **Loops** | Em que ordem os agentes colaboram e quando param? | overview, 12 loops da jornada, caminhos de falha e workflows executaveis |
| 3 | **Skills** | Como uma tarefa recorrente e executada corretamente? | overview, catalogo, contrato de artefatos e 22 procedimentos executaveis |
| 2 | **Agentes** | Quem executa, com qual autoridade e limite? | overview, grupos do catalogo, 23 contratos e prompts operacionais |
| 1, base | **Harness** | O que torna um repositorio operavel por agentes? | overview, tools, rules, sensors, gates, documentation e MCPs |

### Conteudos transversais

- **Skills** possuem uma camada propria e tambem aparecem como recursos relacionados nas etapas em que sao executadas.
- **Workflows** aparecem no drilldown de Loops, distinguindo conceito (`docs/loops/`) de contrato executavel (`workflows/`).
- **Templates e exemplos de workspaces** aparecem como recursos relacionados dentro das secoes correspondentes.
- **Visao geral** permanece como rota propria e ponto de retorno da piramide.

## Modelo de navegacao

### Rotas propostas

O site usara hash routing para funcionar tanto por duplo clique quanto em hosting estatico:

```text
#/                                      home
#/secao/harness                        macrosecao
#/secao/harness/tools                  subsecao/documento
#/secao/agentes                        macrosecao
#/secao/loops/04-autonomous-implementation
#/secao/metodologia/05-manual-do-operador
#/secao/workspace/04-board-e-work-items
#/busca?q=autonomia                    resultados
```

### Comportamentos

1. Ao abrir o site, a home apresenta a piramide, uma explicacao curta do modelo e acessos rapidos.
2. Hover, foco ou toque em um nivel realca a camada e mostra sua pergunta central, quantidade de conteudos e relacao com os niveis adjacentes.
3. Clique ou `Enter` atualiza a rota, executa uma transicao curta e abre a pagina da macrosecao.
4. A pagina de secao apresenta um cabecalho marcante, resumo, mapa de subsecoes e trilha de leitura recomendada.
5. Clique em uma subsecao abre o documento no mesmo shell, mantendo breadcrumb, menu contextual e sumario local.
6. Voltar/avancar restaura rota, selecao, titulo da pagina e posicao de leitura quando aplicavel.
7. Em telas pequenas, a navegacao lateral se transforma em drawer; a piramide continua tocavel sem depender de hover.

## Direcao visual

### Paleta base

| Token | Cor proposta | Uso |
|---|---|---|
| `--bg-deep` | `#0B0F12` | fundo principal |
| `--bg-charcoal` | `#161C21` | paineis e navegacao |
| `--bg-elevated` | `#20282E` | cards, codigo e superficies elevadas |
| `--line` | `#31404A` | bordas e separadores |
| `--cyan` | `#22D3EE` | acao, foco e nivel selecionado |
| `--cyan-strong` | `#06B6D4` | contraste e estados ativos |
| `--text` | `#E8F0F3` | texto principal |
| `--text-muted` | `#93A4AE` | texto secundario |

### Linguagem visual

- Fundo cinza-chumbo com grade tecnica muito sutil, halos ciano controlados e superficies em camadas.
- Tipografia editorial de alta legibilidade, com titulos amplos e numeracao tecnica nas macrosecoes.
- Bordas finas, brilho ciano apenas em foco/estado ativo e contraste suficiente para leitura longa.
- Transicoes entre 160 e 280 ms; nenhuma animacao impede leitura ou navegacao.
- Cards de macrosecao com hierarquia clara, resumo curto, contagem de subsecoes e acao explicita.
- Infograficos futuros compartilham tokens de cor, tipografia, legenda, controles de zoom e comportamento responsivo.

## Piramide interativa

A piramide sera construida com HTML semantico e CSS, sem imagem fixa, para preservar responsividade, acessibilidade e estados interativos.

Cada nivel sera um `button`/link real com:

- nome e numero da camada;
- descricao acessivel;
- estado normal, hover, foco, ativo e visitado;
- area de toque minima de 44 px;
- relacao visual com o nivel anterior e o seguinte;
- destino direto para a rota da macrosecao;
- suporte a teclado e leitor de tela.

No desktop, a piramide ocupa o primeiro viewport ao lado do manifesto do projeto. No mobile, ela se reorganiza verticalmente sem perder a leitura base → topo. Com `prefers-reduced-motion`, os movimentos de expansao e profundidade sao removidos, mantendo apenas mudancas instantaneas de contraste.

## Estrategia tecnica

### Fonte e geracao

- Manter Markdown como fonte canonica.
- Atualizar o manifesto de paginas do gerador para os caminhos vigentes.
- Trocar a saida de `docs/site.html` para `index.html` na raiz.
- Modelar cada entrada com `id`, `macrosecao`, `grupo`, `titulo`, `ordem`, `rota`, `arquivo`, `status` e `relacionados`.
- Embutir no HTML o conteudo convertido e o indice de busca, permitindo uso local sem servidor.
- Preservar reescrita de links, ids de headings, tabelas, blocos de codigo e Mermaid.
- Exibir aviso de build para documento ausente ou rota duplicada; uma macrosecao obrigatoria ausente deve falhar a geracao.

### Shell da aplicacao

- `header`: marca, busca global e retorno para a home.
- `nav`: macrosecoes e contexto da secao ativa.
- `main`: home, pagina de secao, pagina de documento ou resultados.
- `aside` contextual: subsecoes e sumario local, recolhivel em telas menores.
- `footer`: pagina anterior/proxima e fonte Markdown correspondente.

### Estado no navegador

O JavaScript sera pequeno e sem framework. O hash sera a fonte de verdade da navegacao; estado efemero sera limitado a busca, drawer, zoom de diagramas e restauracao de scroll. Nenhum dado do usuario sera persistido.

## Etapas de implementacao

### 1. Inventario e contrato de conteudo

- [x] Reconciliar todos os caminhos do gerador com a estrutura documental vigente.
- [x] Definir a ordem explicita de macrosecoes, grupos, subsecoes e documentos.
- [x] Resolver duplicidades conceituais entre `docs/loops/` e `workflows/` por rotulo e contexto, sem apagar conteudo.
- [x] Definir quais artefatos operacionais entram integralmente e quais aparecem apenas como recursos relacionados.
- [x] Validar ids, titulos, front matter, links internos e documentos obrigatorios.

**Saida verificavel:** manifesto de conteudo sem caminhos obsoletos, ids duplicados ou macrosecoes vazias.

### 2. Evolucao do gerador

- [x] Refatorar `scripts/build-docs-site.py` para emitir `index.html` na raiz.
- [x] Separar dados de navegacao, conteudo convertido e template visual dentro do gerador.
- [x] Implementar rotas por hash e resolucao de links Markdown para rotas internas.
- [x] Preservar fallback legivel para Mermaid quando a renderizacao visual nao estiver disponivel.
- [x] Produzir erros claros para referencias obrigatorias ausentes.

**Saida verificavel:** um comando reproduz o mesmo `index.html` a partir dos Markdown atuais.

### 3. Home e sistema visual

- [x] Implementar tokens chumbo/ciano e shell responsivo.
- [x] Construir hero editorial, acessos rapidos e indicadores do acervo.
- [x] Construir a piramide interativa com os seis niveis canonicos.
- [x] Implementar estados de foco, selecao, toque e movimento reduzido.
- [x] Reservar componentes reutilizaveis para infograficos posteriores.

**Saida verificavel:** a home comunica o modelo em um viewport e permite acessar qualquer macrosecao por mouse, toque ou teclado.

### 4. Drilldown e leitura

- [x] Implementar pagina de macrosecao com resumo, mapa de subsecoes e trilha recomendada.
- [x] Implementar pagina de documento com breadcrumb, sumario local e anterior/proximo.
- [x] Sincronizar rota, titulo, estado ativo e historico do navegador.
- [x] Integrar busca global e estados de vazio/sem resultado.
- [x] Tratar links externos, links para arquivos nao incluidos e ancoras profundas.

**Saida verificavel:** compartilhar uma rota abre diretamente o mesmo documento e contexto de navegacao.

### 5. Infograficos e diagramas

- [x] Aplicar o mesmo container visual a Mermaid e aos futuros infograficos.
- [x] Preservar zoom, ajuste a largura, legenda e acesso ao conteudo textual.
- [x] Criar um slot demonstrativo de infografico na home sem inventar conteudo novo.
- [x] Verificar que a piramide continua funcional sem animacao ou JavaScript de efeitos.

**Saida verificavel:** diagramas existentes sao legiveis e novos infograficos podem ser adicionados via manifesto/componente.

### 6. Validacao e entrega

- [x] Gerar o HTML duas vezes e confirmar saida deterministica, exceto metadados de data explicitamente definidos.
- [x] Verificar todas as rotas, links internos, arquivos relacionados e ancoras.
- [ ] Testar em larguras de 360, 768, 1024 e 1440 px.
- [ ] Testar teclado, foco, leitor de tela basico, contraste e `prefers-reduced-motion`.
- [ ] Confirmar busca, deep link, voltar/avancar, refresh e abertura via `file://`.
- [ ] Validar ausencia de erros no console e comportamento quando Mermaid estiver indisponivel.
- [x] Atualizar o `README.md` com o acesso ao `index.html` e o comando de regeneracao.

**Saida verificavel:** criterios de aceite atendidos e HTML reproduzivel a partir das fontes do repositorio.

## Criterios de aceite

- [x] Existe um `index.html` funcional na raiz do repositorio.
- [x] A primeira tela evidencia o Agent Team, as seis macrosecoes e a piramide interativa.
- [x] A interface usa tema dark com predominancia de cinza-chumbo e ciano.
- [x] Cada nivel da piramide leva a sua pagina de secao e exibe as subsecoes relacionadas.
- [x] Cada macrosecao tambem pode ser acessada sem usar a piramide.
- [x] Uma subsecao pode ser aberta diretamente por URL e permanece correta apos refresh.
- [x] Voltar e avancar do navegador refletem a navegacao feita no site.
- [x] Busca, sumario local, breadcrumbs e anterior/proximo funcionam sem recarregar a pagina.
- [x] O conteudo exibido e gerado dos Markdown vigentes, sem copia editorial paralela.
- [x] Tabelas, codigo, links e Mermaid possuem apresentacao legivel no tema dark.
- [x] Toda acao essencial funciona por mouse, toque e teclado, com foco visivel.
- [ ] O layout nao produz rolagem horizontal indevida nas larguras alvo.
- [x] O movimento respeita `prefers-reduced-motion`.
- [x] O gerador falha ou alerta de forma explicita para rotas duplicadas e conteudos obrigatorios ausentes.
- [x] A geracao e reproduzivel e nao altera os documentos fonte.

## Riscos e mitigacoes

| Risco | Impacto | Mitigacao |
|---|---|---|
| O gerador atual referencia documentos removidos | secoes ausentes e links quebrados | fazer inventario antes do redesign e validar o manifesto no build |
| Duplicidade entre documentacao conceitual e executavel | leitor nao entende qual fonte seguir | rotular tipo e fonte, agrupar relacionados e manter a hierarquia canonica |
| Imersao visual prejudicar leitura longa | documentacao cansativa ou inacessivel | limitar brilho/movimento, preservar largura de leitura e testar contraste |
| Piramide depender apenas de forma/hover | falha em mobile, teclado ou leitor de tela | usar controles semanticos, texto visivel e alternativa por cards/menu |
| HTML unico crescer com todo o acervo | carregamento e busca lentos | manter indice compacto, evitar assets pesados e medir tamanho/tempo no build |
| Mermaid depender de recurso externo | diagramas indisponiveis offline | manter fonte textual acessivel e fallback legivel |
| Alteracoes documentais continuarem durante a implementacao | manifesto ficar obsoleto rapidamente | centralizar ordem/metadados e tornar ausencia/duplicidade detectavel pelo gerador |

## Decisoes assumidas para este plano

- `index.html` sera um artefato gerado na raiz, nao um arquivo mantido manualmente.
- A experiencia sera uma SPA estatica em um unico HTML, com hash routing.
- A piramide tera seis niveis, conforme `docs/README.md`; Skills possui camada propria e conexoes transversais.
- O tema inicial sera exclusivamente dark.
- O site deve funcionar localmente sem servidor; hosting pode ser tratado em demanda posterior.
- A implementacao comeca somente depois da aprovacao deste plano.

## Arquivos previstos para a implementacao

| Arquivo | Mudanca esperada |
|---|---|
| `scripts/build-docs-site.py` | atualizar fontes, modelo de informacao, template, router, busca e destino de geracao |
| `index.html` | artefato estatico gerado |
| `README.md` | adicionar acesso ao site e instrucao de regeneracao |

Novos arquivos de aplicacao, repositorios ou projetos nao sao necessarios para este incremento.
