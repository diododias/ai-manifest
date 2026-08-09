---
title: Agent Team — padrão de documentação
status: canonical
updated_at: 2026-08-09
---

# Padrão de documentação

> Como escrever documentos do Agent Team que servem ao leitor apressado e ao leitor detalhista no mesmo arquivo.

## Em 2 minutos

Todo documento canônico atende dois leitores. O primeiro chega sem contexto, tem poucos minutos e quer decidir se vale a pena continuar. O segundo já decidiu que vale e precisa do detalhe operacional para executar. Atender apenas um dos dois produz documentação que cansa ou documentação que não sustenta a operação.

A solução adotada é **um documento por tema, com duas camadas dentro dele**. A camada rápida fica no topo, em prosa, e responde "o que é isto, para que serve e o que muda no meu trabalho". A camada detalhada vem abaixo, organizada em blocos navegáveis, e responde "como executo isto na prática".

| Camada | Onde fica | Formato | Tamanho alvo |
|---|---|---|---|
| Rápida | Logo após o título | Prosa corrida + uma tabela-âncora | 200–400 palavras |
| Mapa | Entre as duas camadas | Tabela de seções com "leia se você…" | 5–15 linhas |
| Detalhada | Restante do documento | Blocos com abertura em prosa, tabelas e diagramas | sem limite |

A regra que resolve o problema de "bullets massivos" é simples: **nenhuma seção começa com uma lista, e nenhuma lista carrega o significado sozinha**. Listas descrevem itens; prosa e tabelas descrevem relações.

---

## Mapa deste documento

| Seção | Responde | Leia se você… |
|---|---|---|
| [1. As duas camadas](#1-as-duas-camadas) | Como estruturar o topo e o corpo | vai escrever ou reescrever um documento |
| [2. Regras de formatação](#2-regras-de-formatação) | Quando usar prosa, tabela, lista ou diagrama | está corrigindo um documento denso |
| [3. Front matter e estado](#3-front-matter-e-estado) | Quais metadados são obrigatórios | está criando um arquivo novo |
| [4. Navegação e links](#4-navegação-e-links) | Como um documento aponta para os outros | está movendo ou renomeando arquivos |
| [5. Checklist de revisão](#5-checklist-de-revisão) | Como validar antes do PR | está fechando uma alteração de documentação |

---

## 1. As duas camadas

### 1.1 Camada rápida — "Em 2 minutos"

É a primeira seção de todo documento canônico, sempre com esse título. Ela é escrita para alguém que já conhece workflows de desenvolvimento e quer avaliar o projeto antes de investir tempo. Não é um resumo executivo genérico: é o argumento central do documento em prosa.

Um bloco "Em 2 minutos" bem escrito contém três movimentos, nesta ordem:

1. **O problema** que o documento existe para resolver, em uma ou duas frases concretas.
2. **A resposta** do Agent Team a esse problema, com o mecanismo principal nomeado.
3. **Uma tabela-âncora** com as 3 a 7 entidades centrais do tema — papéis, fases, gates, artefatos — que o leitor detalhista vai reencontrar depois, mais desenvolvidas.

O que não entra na camada rápida: exceções, casos de borda, listas de responsabilidades completas, nomes de arquivos internos e qualquer coisa que só faça sentido depois de contexto.

### 1.2 Mapa do documento

Uma tabela curta entre as camadas, com três colunas: seção, pergunta que ela responde e para quem ela é. O mapa transforma um documento longo em algo que se navega por intenção, e não por rolagem. Documentos abaixo de 150 linhas podem omiti-lo.

**Documentos curtos de contrato** — os workflows em `docs/workflows/`, por exemplo — são exceção às duas camadas. Eles já cabem em uma tela, abrem com um parágrafo de propósito seguido da tabela de contrato, e não ganham nada com um bloco "Em 2 minutos" separado. A regra prática: se o documento inteiro é lido em menos tempo do que o resumo economizaria, não há resumo a escrever.

### 1.3 Camada detalhada

O corpo do documento é dividido em **blocos numerados**, e cada bloco segue o mesmo ritmo:

- um parágrafo de abertura que explica por que aquele bloco existe e como ele se conecta ao anterior;
- o conteúdo estruturado — tabela, diagrama, sequência numerada ou lista curta;
- quando houver decisão envolvida, uma frase final de consequência: o que acontece se a regra não for seguida.

Blocos com mais de 120 linhas devem virar um documento próprio, referenciado a partir do mapa.

---

## 2. Regras de formatação

### 2.1 A escolha do formato

A pergunta a fazer antes de escrever qualquer bloco é "que tipo de informação é esta?". Cada tipo tem um formato correto, e usar lista para tudo é a causa raiz da documentação cansativa.

| Tipo de informação | Formato correto | Formato errado comum |
|---|---|---|
| Relação entre entidades (quem decide o quê, quem entrega para quem) | Tabela | Lista de bullets |
| Sequência com ordem e dependência | Lista numerada ou diagrama Mermaid | Bullets |
| Argumento, motivo, trade-off | Prosa | Bullets |
| Enumeração curta sem estrutura interna | Lista com até 5 itens | Tabela |
| Estrutura hierárquica (pastas, artefatos) | Bloco `text` ou árvore | Bullets aninhados |
| Contrato de entrada/saída | Tabela de duas colunas | Subtítulos repetidos |

### 2.2 Limites que evitam a parede de bullets

Seis limites, em ordem de impacto:

| Limite | Regra |
|---|---|
| **Abertura** | Nenhuma seção `##` começa com uma lista — sempre há ao menos uma frase antes |
| **Tamanho** | Listas param em 7 itens; acima disso, agrupe em subcategorias nomeadas ou converta em tabela |
| **Paralelismo** | Se todos os itens seguem o padrão `**Campo:** valor`, isso é uma tabela, não uma lista |
| **Profundidade** | Sem bullets aninhados além do segundo nível; hierarquia mais profunda vira subtítulo ou bloco de código |
| **Adjacência** | Duas listas nunca se tocam; se houver duas seguidas sem prosa entre elas, o bloco precisa ser reescrito |
| **Proporção** | Em documentos canônicos, no máximo 30% das linhas devem ser bullets |

**Exceções à regra de abertura.** Três tipos de lista carregam o significado sozinhos e podem abrir uma seção: listas de links ou referências, checklists com `- [ ]`, e listas de perguntas usadas para conduzir uma discussão. Subseções `###` que são enumerações puras também podem abrir com lista, desde que a seção `##` que as contém tenha prosa.

### 2.3 Recursos visuais

Diagramas Mermaid são obrigatórios em qualquer documento que descreva fluxo entre fases, agentes ou gates — um `flowchart LR` no início da seção poupa dezenas de linhas de texto. Tabelas de contrato (entrada, quem consolida, quem colabora, saída, owner, gate) devem manter sempre a mesma ordem de colunas entre documentos, para que o leitor reconheça o padrão sem reler o cabeçalho.

Separadores `---` marcam a troca de bloco temático, não a troca de subtítulo. Ênfase em negrito serve para nomear a entidade sendo definida, não para dar destaque emocional.

---

## 3. Front matter e estado

Todo documento destinado a leitores humanos em `docs/` começa com front matter YAML. Os pacotes de agente (`docs/agents/<agente>/*.md`) são exceção: são consumidos pela ferramenta de execução e seguem o formato que ela espera.

```yaml
---
title: <título legível, prefixado por "Agent Team —" nos canônicos>
status: canonical | proposed | reference
updated_at: YYYY-MM-DD
---
```

O campo `status` comunica ao leitor o peso da informação e evita que material histórico oriente decisão corrente.

| Estado | Significado | Efeito prático |
|---|---|---|
| `canonical` | Referência vigente do sistema | Conflitos são resolvidos a favor deste documento |
| `proposed` | Pronto para validação em piloto | Pode ser seguido, mas ainda muda |
| `reference` | Apoio à compreensão ou apresentação | Não cria obrigação |

Não existe estado `archived`. Documentação que deixou de descrever o fluxo vigente é removida no mesmo PR que a substitui — o histórico permanece recuperável no Git, e o repositório passa a conter apenas uma versão de cada tema.

Quando um conceito muda, a alteração entra primeiro no documento `canonical` e só depois é propagada para os especializados. O caminho inverso produz divergência silenciosa.

---

## 4. Navegação e links

Cada documento abre com uma linha de citação (`>`) que o resume em uma frase e, quando aplicável, uma segunda linha com os documentos vizinhos. Todos os links internos são relativos ao arquivo, nunca absolutos ao repositório, para que o repositório continue navegável em qualquer host.

A hierarquia de `docs/` é fixa. Os documentos de modelo operacional ficam na raiz de `docs/`, sem pasta intermediária, porque são a camada conceitual do repositório inteiro; as pastas existem apenas onde há um conjunto homogêneo de arquivos.

```text
docs/
├── README.md                    # índice e mapa de leitura por perfil
├── operating-model.md           # fonte canônica: papéis, decisões e ciclo
├── operating-model-90-10.md     # gates, risco e autonomia progressiva
├── end-to-end-journey.md        # a jornada completa em um diagrama
├── journey-by-phase.md          # a mesma jornada, um bloco por vez
├── documentation-standard.md    # este padrão
├── site.html                    # documentação navegável em página única
├── agents/                      # catálogo, contratos e pacotes importáveis
├── workflows/                   # contratos de colaboração multiagente
└── diagrams/                    # organização de workspace e fontes de verdade
```

O repositório não mantém pasta de arquivo histórico. Documentação que deixou de valer é removida, e o histórico fica no Git — manter versões superadas ao lado das vigentes cria ambiguidade sobre qual delas orienta uma decisão.

Ao mover ou renomear um arquivo, os links que apontavam para ele precisam ser corrigidos no mesmo commit. Link quebrado em documentação canônica é defeito, não pendência.

---

## 5. Checklist de revisão

Antes de abrir o PR de uma alteração de documentação, confirme:

| Verificação | Critério |
|---|---|
| Camada rápida | Existe "Em 2 minutos", em prosa, com tabela-âncora |
| Abertura de seções | Nenhuma seção começa com lista |
| Densidade | Nenhuma lista com mais de 7 itens; bullets abaixo de 30% das linhas |
| Formato | Relações estão em tabela; sequências, em lista numerada ou diagrama |
| Front matter | `title`, `status` e `updated_at` presentes e corretos |
| Links | Todos os links relativos resolvem para arquivos existentes |
| Propagação | A fonte canônica foi atualizada antes dos documentos derivados |

Documentos que descrevem instruções executadas por agentes — `skills/*/SKILL.md` e os pacotes em `docs/agents/<agente>/` — seguem regras próprias de concisão e podem usar listas densas de forma intencional. Este padrão se aplica à documentação destinada a leitores humanos.
