#!/usr/bin/env python3
"""Gera docs/site.html: a documentação do Agent Team em uma única página navegável.

O script lê os documentos markdown vigentes, converte para HTML, preserva os blocos
Mermaid para renderização no navegador e emite um arquivo autocontido que abre com
duplo clique, sem servidor.

Uso:
    python3 scripts/build-docs-site.py
"""

import html
import json
import os.path
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "site.html"

# (arquivo, seção, título no menu)
PAGES = [
    ("README.md",                             "Visão geral",   "O que é o Agent Team"),
    ("docs/README.md",                        "Visão geral",   "Índice da documentação"),

    ("docs/operating-model.md",               "Modelo operacional", "Sistema operacional do trio humano"),
    ("docs/operating-model-90-10.md",         "Modelo operacional", "Modelo 90/10: gates e autonomia"),
    ("docs/repo-harness.md",                  "Modelo operacional", "Repo harness"),
    ("docs/end-to-end-journey.md",            "Modelo operacional", "Jornada de ponta a ponta"),
    ("docs/journey-by-phase.md",              "Modelo operacional", "Jornada por fases"),
    ("docs/documentation-standard.md",        "Modelo operacional", "Padrão de documentação"),

    ("docs/workflows/README.md",              "Workflows", "Mapa dos workflows"),
    ("docs/workflows/00-intake-and-triage.md",                  "Workflows", "00 · Intake e triagem"),
    ("docs/workflows/01-discovery-and-research.md",             "Workflows", "01 · Discovery e research"),
    ("docs/workflows/02-product-and-ux-planning.md",            "Workflows", "02 · Produto e UX"),
    ("docs/workflows/03-technical-specification.md",            "Workflows", "03 · Especificação técnica"),
    ("docs/workflows/04-autonomous-implementation.md",          "Workflows", "04 · Implementação autônoma"),
    ("docs/workflows/05-adversarial-validation.md",             "Workflows", "05 · Validação adversarial"),
    ("docs/workflows/06-pr-and-merge.md",                       "Workflows", "06 · PR e merge"),
    ("docs/workflows/07-release-candidate-validation.md",       "Workflows", "07 · Homologação"),
    ("docs/workflows/08-production-release-and-observation.md",  "Workflows", "08 · Produção e observação"),
    ("docs/workflows/09-knowledge-curation.md",                 "Workflows", "09 · Curadoria de conhecimento"),
    ("docs/workflows/10-continuous-improvement.md",             "Workflows", "10 · Melhoria contínua"),

    ("docs/agents/catalog.md",                "Agentes", "Catálogo de agentes"),
    ("docs/agents/README.md",                 "Agentes", "Pacotes importáveis"),

    ("skills/README.md",                      "Skills", "Catálogo de skills"),
    ("skills/references/workflow-contract.md", "Skills", "Contrato de artefatos"),
    ("skills/workspace-memory/SKILL.md",      "Skills", "workspace-memory"),
    ("skills/workspace-projects/SKILL.md",    "Skills", "workspace-projects"),
    ("skills/workspace-board/SKILL.md",       "Skills", "workspace-board"),
    ("skills/business-discovery/SKILL.md",    "Skills", "business-discovery"),
    ("skills/write-feature/SKILL.md",         "Skills", "write-feature"),
    ("skills/review-prd/SKILL.md",            "Skills", "review-prd"),
    ("skills/technical-discovery/SKILL.md",   "Skills", "technical-discovery"),
    ("skills/create-spec/SKILL.md",           "Skills", "create-spec"),
    ("skills/refine-spec/SKILL.md",           "Skills", "refine-spec"),
    ("skills/review-spec/SKILL.md",           "Skills", "review-spec"),
    ("skills/review-cross-prd-spec/SKILL.md", "Skills", "review-cross-prd-spec"),
    ("skills/dev-flow/SKILL.md",              "Skills", "dev-flow"),
    ("skills/implement/SKILL.md",             "Skills", "implement"),
    ("skills/test-integration-local/SKILL.md", "Skills", "test-integration-local"),
    ("skills/code-review/SKILL.md",           "Skills", "code-review"),
    ("skills/analyse-bug/SKILL.md",           "Skills", "analyse-bug"),
    ("skills/fix-bug/SKILL.md",               "Skills", "fix-bug"),
    ("skills/commit/SKILL.md",                "Skills", "commit"),
    ("skills/update-pr/SKILL.md",             "Skills", "update-pr"),
    ("skills/check-pr/SKILL.md",              "Skills", "check-pr"),
    ("skills/update-docs/SKILL.md",           "Skills", "update-docs"),

    ("docs/diagrams/tech-lead-workspace.md",  "Workspaces", "Anatomia do workspace"),
    ("workspaces/README.md",                  "Workspaces", "Workspaces de exemplo"),
]

FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
MERMAID_BLOCK = re.compile(r"^```mermaid\n(.*?)^```\s*$", re.DOTALL | re.MULTILINE)


def slugify(text: str) -> str:
    """Slug ASCII para ids de página, derivado do caminho do arquivo."""
    text = text.lower().strip()
    for a, b in zip("áàâãäéèêëíìîïóòôõöúùûüçñ", "aaaaaeeeeiiiiooooouuuucn"):
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"[\s-]+", "-", text).strip("-")


def github_slugify(value: str, separator: str = "-") -> str:
    """Reproduz o slug de heading do GitHub.

    Os documentos são escritos para serem lidos também no GitHub, e seus links
    internos (`#2-regras-de-formatação`) seguem aquela convenção: acentos são
    preservados, pontuação é removida e cada espaço restante vira um hífen — o que
    produz hífens duplos onde havia travessão. Usar o slug padrão do Python-Markdown,
    que remove acentos e colapsa hífens, quebraria esses links dentro do site.
    """
    value = unicodedata.normalize("NFC", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"\s", separator, value)


def parse_front_matter(text: str):
    meta = {}
    match = FRONT_MATTER.match(text)
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"').strip("'")
        text = text[match.end():]
    return meta, text


def extract_mermaid(text: str):
    """Troca blocos mermaid por placeholders, para não passarem pelo conversor."""
    diagrams = []

    def replace(match):
        diagrams.append(match.group(1).rstrip())
        return f"\n\nMERMAIDPLACEHOLDER{len(diagrams) - 1}ENDPLACEHOLDER\n\n"

    return MERMAID_BLOCK.sub(replace, text), diagrams


def restore_mermaid(rendered: str, diagrams: list) -> str:
    for index, source in enumerate(diagrams):
        placeholder = f"MERMAIDPLACEHOLDER{index}ENDPLACEHOLDER"
        block = (
            '<div class="mermaid-wrap">'
            '<div class="mermaid-tools">'
            '<button type="button" data-zoom="out" title="reduzir">−</button>'
            '<span data-zoom-label>ajustado</span>'
            '<button type="button" data-zoom="in" title="ampliar">+</button>'
            '<button type="button" data-zoom="fit" title="ajustar à largura">ajustar</button>'
            "</div>"
            f'<pre class="mermaid">{html.escape(source)}</pre>'
            f'<details class="mermaid-src"><summary>ver código do diagrama</summary>'
            f'<pre><code>{html.escape(source)}</code></pre></details>'
            "</div>"
        )
        rendered = rendered.replace(f"<p>{placeholder}</p>", block).replace(placeholder, block)
    return rendered


SEP = "~"  # separa id da página do id da âncora; não aparece em slugs


def rewrite_links(rendered: str, page_ids: dict, current: Path) -> str:
    """Converte links entre documentos incluídos em âncoras internas do site.

    Links para arquivos do repositório que não entram no site são reescritos como
    caminho relativo a `docs/`, para que continuem abrindo a partir do site.html.
    """

    def replace(match):
        href = match.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        target, _, fragment = href.partition("#")
        if not target:
            return match.group(0)
        resolved = (current.parent / target).resolve()
        try:
            key = str(resolved.relative_to(ROOT))
        except ValueError:
            return match.group(0)
        if key in page_ids:
            anchor = f"#{page_ids[key]}"
            if fragment:
                anchor += f"{SEP}{fragment}"
            return f'href="{anchor}"'
        relative = os.path.relpath(resolved, OUTPUT.parent)
        if fragment:
            relative += f"#{fragment}"
        return f'href="{relative}" class="ext" title="{key} — arquivo do repositório"'

    return re.sub(r'href="([^"]+)"', replace, rendered)


def prefix_heading_ids(rendered: str, page_id: str):
    """Prefixa ids de heading com o id da página e devolve o sumário local."""
    toc = []

    def replace(match):
        level, attrs, inner = match.group(1), match.group(2), match.group(3)
        found = re.search(r'id="([^"]+)"', attrs)
        raw_id = found.group(1) if found else slugify(re.sub(r"<[^>]+>", "", inner))
        new_id = f"{page_id}{SEP}{raw_id}"
        if level in ("2", "3"):
            toc.append({"level": int(level), "id": new_id,
                        "text": re.sub(r"<[^>]+>", "", inner).strip()})
        attrs = re.sub(r'\s*id="[^"]+"', "", attrs)
        return f'<h{level}{attrs} id="{new_id}">{inner}</h{level}>'

    rendered = re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", replace, rendered, flags=re.DOTALL)
    rendered = re.sub(r'href="#([^"]+)"', lambda m: m.group(0) if SEP in m.group(1)
                      else f'href="#{page_id}{SEP}{m.group(1)}"', rendered)
    return rendered, toc


def build():
    converter = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
        extension_configs={"toc": {"slugify": github_slugify}},
        output_format="html5",
    )

    page_ids = {path: slugify(path.replace(".md", "").replace("/", "-")) for path, _, _ in PAGES}
    pages = []

    for path, section, title in PAGES:
        source = ROOT / path
        if not source.exists():
            print(f"aviso: {path} não existe, ignorado", file=sys.stderr)
            continue

        raw = source.read_text(encoding="utf-8")
        meta, body = parse_front_matter(raw)
        body, diagrams = extract_mermaid(body)

        converter.reset()
        rendered = converter.convert(body)
        rendered = restore_mermaid(rendered, diagrams)

        # Os SKILL.md são instruções para agentes, não documentos de leitura: muitos
        # abrem direto em `## User Input`, sem título nem resumo. O site reconstrói
        # esse cabeçalho a partir do front matter para que a página não comece no vazio.
        if "<h1" not in rendered:
            lede = (f"<blockquote><p>{html.escape(meta['description'])}</p></blockquote>"
                    if meta.get("description") else "")
            rendered = f"<h1>{html.escape(meta.get('name') or title)}</h1>{lede}{rendered}"

        # A ordem importa: as âncoras locais (`#secao`) são prefixadas primeiro,
        # enquanto ainda se distinguem dos links entre documentos (`arquivo.md#secao`).
        page_id = page_ids[path]
        rendered, toc = prefix_heading_ids(rendered, page_id)
        rendered = rewrite_links(rendered, page_ids, source)

        pages.append({
            "id": page_id,
            "path": path,
            "section": section,
            "title": title,
            "status": meta.get("status", ""),
            "updated": meta.get("updated_at", ""),
            "html": rendered,
            "toc": toc,
            "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", rendered)).lower(),
        })

    OUTPUT.write_text(
        TEMPLATE.replace("/*__PAGES__*/", json.dumps(pages, ensure_ascii=False))
                .replace("__BUILD_DATE__", date.today().isoformat()),
        encoding="utf-8",
    )
    print(f"site gerado: {OUTPUT.relative_to(ROOT)} ({len(pages)} documentos, "
          f"{OUTPUT.stat().st_size // 1024} KB)")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent Team — documentação</title>
<style>
  :root {
    --bg: #ffffff; --bg-soft: #f7f8fa; --bg-sunk: #eef1f5;
    --fg: #16191d; --fg-soft: #5b6472; --fg-faint: #8b95a3;
    --line: #e2e6ec; --line-strong: #cbd2dc;
    --accent: #2563eb; --accent-soft: #dbeafe;
    --canonical: #047857; --canonical-bg: #d1fae5;
    --proposed: #b45309; --proposed-bg: #fef3c7;
    --reference: #4f46e5; --reference-bg: #e0e7ff;
    --sidebar: 290px; --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #0f1216; --bg-soft: #161a20; --bg-sunk: #1c222a;
      --fg: #e6e9ee; --fg-soft: #a3adba; --fg-faint: #6d7885;
      --line: #262c35; --line-strong: #333b46;
      --accent: #60a5fa; --accent-soft: #1e3a5f;
      --canonical: #6ee7b7; --canonical-bg: #064e3b;
      --proposed: #fcd34d; --proposed-bg: #78350f;
      --reference: #a5b4fc; --reference-bg: #312e81;
    }
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0; background: var(--bg); color: var(--fg);
    font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
    -webkit-font-smoothing: antialiased;
  }

  /* ---------- layout ---------- */
  .shell { display: flex; min-height: 100vh; }
  aside {
    width: var(--sidebar); flex: 0 0 var(--sidebar); border-right: 1px solid var(--line);
    background: var(--bg-soft); height: 100vh; position: sticky; top: 0;
    display: flex; flex-direction: column;
  }
  .brand { padding: 20px 20px 14px; border-bottom: 1px solid var(--line); }
  .brand h1 { margin: 0; font-size: 15px; letter-spacing: -0.01em; }
  .brand p { margin: 3px 0 0; font-size: 12px; color: var(--fg-faint); }
  .search { padding: 12px 16px; border-bottom: 1px solid var(--line); }
  .search input {
    width: 100%; padding: 8px 11px; font-size: 13px; font-family: inherit;
    border: 1px solid var(--line-strong); border-radius: 7px;
    background: var(--bg); color: var(--fg);
  }
  .search input:focus { outline: 2px solid var(--accent-soft); border-color: var(--accent); }
  nav { flex: 1; overflow-y: auto; padding: 10px 10px 40px; }
  nav .group {
    font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .09em;
    color: var(--fg-faint); padding: 16px 10px 6px;
  }
  nav a {
    display: block; padding: 6px 10px; margin: 1px 0; border-radius: 6px;
    color: var(--fg-soft); text-decoration: none; font-size: 13.5px; line-height: 1.4;
  }
  nav a:hover { background: var(--bg-sunk); color: var(--fg); }
  nav a.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
  nav a.hidden { display: none; }

  main { flex: 1; min-width: 0; display: flex; justify-content: center; }
  .doc { width: 100%; max-width: 860px; padding: 44px 44px 140px; }
  .doc.wide { max-width: 1180px; }

  /* ---------- cabeçalho do documento ---------- */
  .meta { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-bottom: 6px; }
  .badge {
    font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em;
    padding: 3px 8px; border-radius: 20px;
  }
  .badge.canonical { color: var(--canonical); background: var(--canonical-bg); }
  .badge.proposed  { color: var(--proposed);  background: var(--proposed-bg); }
  .badge.reference { color: var(--reference); background: var(--reference-bg); }
  .path { font-family: var(--mono); font-size: 11.5px; color: var(--fg-faint); }

  /* ---------- conteúdo ---------- */
  .doc h1 { font-size: 31px; line-height: 1.2; letter-spacing: -0.02em; margin: 6px 0 20px; }
  .doc h2 {
    font-size: 22px; letter-spacing: -0.01em; margin: 46px 0 14px;
    padding-top: 18px; border-top: 1px solid var(--line);
  }
  .doc h3 { font-size: 17px; margin: 30px 0 10px; }
  .doc h4 { font-size: 14.5px; margin: 22px 0 8px; color: var(--fg-soft); }
  .doc p { margin: 0 0 14px; }
  .doc a { color: var(--accent); text-decoration: none; border-bottom: 1px solid transparent; }
  .doc a:hover { border-bottom-color: currentColor; }
  .doc a.ext { color: var(--fg-soft); border-bottom: 1px dotted var(--line-strong); }
  .doc blockquote {
    margin: 0 0 24px; padding: 12px 18px; border-left: 3px solid var(--accent);
    background: var(--bg-soft); border-radius: 0 8px 8px 0; color: var(--fg-soft);
  }
  .doc blockquote p:last-child { margin: 0; }
  .doc ul, .doc ol { margin: 0 0 16px; padding-left: 22px; }
  .doc li { margin: 4px 0; }
  .doc hr { border: 0; border-top: 1px solid var(--line); margin: 34px 0; }
  .doc code {
    font-family: var(--mono); font-size: .87em; background: var(--bg-sunk);
    padding: 1.5px 5px; border-radius: 4px;
  }
  .doc pre {
    background: var(--bg-sunk); border: 1px solid var(--line); border-radius: 9px;
    padding: 14px 16px; overflow-x: auto; margin: 0 0 20px; font-size: 12.5px; line-height: 1.55;
  }
  .doc pre code { background: none; padding: 0; }
  .doc table {
    border-collapse: collapse; width: 100%; margin: 0 0 22px; font-size: 14px;
    display: block; overflow-x: auto;
  }
  .doc th, .doc td {
    border: 1px solid var(--line); padding: 8px 12px; text-align: left; vertical-align: top;
  }
  .doc th { background: var(--bg-soft); font-weight: 650; white-space: nowrap; }
  .doc tr:nth-child(even) td { background: var(--bg-soft); }
  .doc details { margin: 0 0 18px; }
  .doc summary { cursor: pointer; font-size: 13px; color: var(--fg-soft); }

  /* ---------- mermaid ---------- */
  .mermaid-wrap {
    position: relative; margin: 0 0 26px; padding: 18px; border: 1px solid var(--line);
    border-radius: 11px; background: var(--bg-soft); overflow-x: auto;
  }
  pre.mermaid { background: none; border: 0; padding: 0; margin: 0; text-align: center; }
  pre.mermaid[data-processed] ~ .mermaid-src { display: block; }
  pre.mermaid svg { max-width: 100%; height: auto; }
  .mermaid-wrap.zoomed pre.mermaid { text-align: left; }
  .mermaid-tools {
    display: none; align-items: center; justify-content: flex-end;
    gap: 5px; margin: -4px 0 10px;
  }
  .mermaid-wrap:has(pre.mermaid[data-processed]) .mermaid-tools { display: flex; }
  .mermaid-tools button {
    font: inherit; font-size: 12px; line-height: 1; color: var(--fg-soft); cursor: pointer;
    background: var(--bg); border: 1px solid var(--line-strong);
    border-radius: 6px; padding: 5px 9px; min-width: 28px;
  }
  .mermaid-tools button:hover { border-color: var(--accent); color: var(--accent); }
  .mermaid-tools span {
    font-size: 11px; color: var(--fg-faint); min-width: 58px; text-align: center;
    font-variant-numeric: tabular-nums;
  }
  .mermaid-src { display: none; margin: 14px 0 0; }
  .mermaid-src pre { margin: 8px 0 0; }

  /* ---------- busca ---------- */
  .results { padding: 4px 0; }
  .results .hit { display: block; padding: 9px 10px; border-radius: 7px; text-decoration: none; }
  .results .hit:hover { background: var(--bg-sunk); }
  .results .hit strong { display: block; font-size: 13.5px; color: var(--fg); }
  .results .hit span { font-size: 11.5px; color: var(--fg-faint); }
  .empty { padding: 14px 10px; font-size: 13px; color: var(--fg-faint); }

  /* ---------- rodapé de navegação ---------- */
  .pager { display: flex; justify-content: space-between; gap: 14px; margin-top: 56px;
           padding-top: 22px; border-top: 1px solid var(--line); }
  .pager a {
    flex: 1; padding: 12px 16px; border: 1px solid var(--line); border-radius: 9px;
    text-decoration: none; color: var(--fg); font-size: 13.5px; background: var(--bg-soft);
  }
  .pager a:hover { border-color: var(--accent); }
  .pager a small { display: block; color: var(--fg-faint); font-size: 11px; margin-bottom: 2px; }
  .pager a.next { text-align: right; }
  .pager .spacer { flex: 1; }

  /* ---------- mobile ---------- */
  .menu-btn {
    display: none; position: fixed; z-index: 30; top: 12px; left: 12px;
    width: 40px; height: 40px; border-radius: 9px; border: 1px solid var(--line-strong);
    background: var(--bg); color: var(--fg); font-size: 17px; cursor: pointer;
  }
  @media (max-width: 900px) {
    .menu-btn { display: block; }
    aside {
      position: fixed; z-index: 25; transform: translateX(-100%);
      transition: transform .2s ease; box-shadow: 0 0 40px rgba(0,0,0,.18);
    }
    aside.open { transform: none; }
    .doc { padding: 66px 20px 100px; }
  }
  @media print {
    aside, .menu-btn, .pager { display: none; }
    .doc { max-width: none; padding: 0; }
  }
</style>
</head>
<body>
<button class="menu-btn" id="menuBtn" aria-label="Menu">☰</button>
<div class="shell">
  <aside id="sidebar">
    <div class="brand">
      <h1>Agent Team</h1>
      <p>documentação · build __BUILD_DATE__</p>
    </div>
    <div class="search">
      <input id="q" type="search" placeholder="Buscar na documentação…" autocomplete="off">
    </div>
    <nav id="nav"></nav>
  </aside>
  <main><article class="doc" id="doc"></article></main>
</div>

<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
const PAGES = /*__PAGES__*/;
const nav = document.getElementById('nav');
const doc = document.getElementById('doc');
const q = document.getElementById('q');
const sidebar = document.getElementById('sidebar');
const byId = Object.fromEntries(PAGES.map(p => [p.id, p]));

function buildNav() {
  let html = '', section = null;
  PAGES.forEach(p => {
    if (p.section !== section) { section = p.section; html += `<div class="group">${section}</div>`; }
    html += `<a href="#${p.id}" data-id="${p.id}">${p.title}</a>`;
  });
  nav.innerHTML = html;
}

function render(id) {
  const page = byId[id] || PAGES[0];
  const wide = /journey|workspace|catalog/.test(page.id);
  doc.className = 'doc' + (wide ? ' wide' : '');
  const badge = page.status ? `<span class="badge ${page.status}">${page.status}</span>` : '';
  const updated = page.updated ? `<span class="path">atualizado em ${page.updated}</span>` : '';
  const i = PAGES.indexOf(page);
  const prev = PAGES[i - 1], next = PAGES[i + 1];
  const pager =
    `<div class="pager">` +
    (prev ? `<a href="#${prev.id}"><small>← anterior</small>${prev.title}</a>` : `<div class="spacer"></div>`) +
    (next ? `<a class="next" href="#${next.id}"><small>próximo →</small>${next.title}</a>` : `<div class="spacer"></div>`) +
    `</div>`;
  doc.innerHTML =
    `<div class="meta">${badge}<span class="path">${page.path}</span>${updated}</div>` +
    page.html + pager;

  document.querySelectorAll('nav a').forEach(a =>
    a.classList.toggle('active', a.dataset.id === page.id));
  renderDiagrams();
  sidebar.classList.remove('open');
}

function renderDiagrams() {
  if (!window.mermaid) return;
  const nodes = doc.querySelectorAll('pre.mermaid');
  if (!nodes.length) return;
  try { mermaid.run({ nodes }); } catch (e) { console.warn('mermaid', e); }
}

// Os fluxogramas de jornada são grandes demais para caber legíveis na coluna de
// texto. Cada diagrama ganha zoom próprio: ajustado à largura por padrão, ampliável
// em passos, com rolagem horizontal no contêiner.
const ZOOM_STEPS = [0.5, 0.75, 1, 1.5, 2, 3, 4];

function applyZoom(wrap, scale) {
  const svg = wrap.querySelector('pre.mermaid svg');
  const label = wrap.querySelector('[data-zoom-label]');
  if (!svg) return;
  if (!svg.dataset.baseWidth) {
    const box = svg.viewBox && svg.viewBox.baseVal;
    svg.dataset.baseWidth = (box && box.width) || svg.getBoundingClientRect().width || 800;
  }
  svg.style.height = 'auto';
  if (scale === 'fit') {
    delete wrap.dataset.scale;
    wrap.classList.remove('zoomed');
    svg.style.maxWidth = '100%';
    svg.style.width = '';
    label.textContent = 'ajustado';
  } else {
    wrap.dataset.scale = scale;
    wrap.classList.add('zoomed');
    svg.style.maxWidth = 'none';
    svg.style.width = (parseFloat(svg.dataset.baseWidth) * scale) + 'px';
    label.textContent = Math.round(scale * 100) + '%';
  }
}

doc.addEventListener('click', e => {
  const btn = e.target.closest('[data-zoom]');
  if (!btn) return;
  const wrap = btn.closest('.mermaid-wrap');
  const action = btn.dataset.zoom;
  if (action === 'fit') return applyZoom(wrap, 'fit');
  const current = parseFloat(wrap.dataset.scale || 1);
  let index = ZOOM_STEPS.findIndex(s => s >= current - 0.001);
  index = action === 'in' ? Math.min(index + 1, ZOOM_STEPS.length - 1) : Math.max(index - 1, 0);
  applyZoom(wrap, ZOOM_STEPS[index]);
});

// Um termo como "refine-spec" aparece de passagem em vários documentos, mas o que
// o leitor quer é a página daquele nome. Título e caminho pesam mais que corpo.
function score(page, term) {
  const title = page.title.toLowerCase();
  if (title === term) return 0;
  if (title.startsWith(term)) return 1;
  if (title.includes(term)) return 2;
  if (page.path.toLowerCase().includes(term)) return 3;
  return page.text.includes(term) ? 4 : Infinity;
}

function search(term) {
  term = term.trim().toLowerCase();
  if (!term) { buildNav(); highlightCurrent(); return; }
  const hits = PAGES.map(p => [p, score(p, term)])
                    .filter(([, s]) => s < Infinity)
                    .sort((a, b) => a[1] - b[1] || PAGES.indexOf(a[0]) - PAGES.indexOf(b[0]))
                    .map(([p]) => p);
  nav.innerHTML = hits.length
    ? `<div class="group">${hits.length} resultado${hits.length > 1 ? 's' : ''}</div>` +
      `<div class="results">` + hits.map(p =>
        `<a class="hit" href="#${p.id}"><strong>${p.title}</strong><span>${p.section} · ${p.path}</span></a>`
      ).join('') + `</div>`
    : `<div class="empty">Nenhum documento contém “${term}”.</div>`;
}

function highlightCurrent() {
  const id = (location.hash || '').slice(1).split('~')[0];
  document.querySelectorAll('nav a').forEach(a => a.classList.toggle('active', a.dataset.id === id));
}

function route() {
  const raw = (location.hash || '').slice(1);
  const [id, anchor] = raw.split('~');
  render(id);
  if (anchor) {
    const el = document.getElementById(`${id}~${anchor}`);
    if (el) el.scrollIntoView();
  } else {
    window.scrollTo(0, 0);
  }
}

q.addEventListener('input', e => search(e.target.value));
q.addEventListener('keydown', e => {
  if (e.key === 'Escape') { q.value = ''; search(''); }
  if (e.key === 'Enter') { const first = nav.querySelector('a'); if (first) location.hash = first.getAttribute('href'); }
});
document.addEventListener('keydown', e => {
  if ((e.key === '/' || (e.key === 'k' && (e.metaKey || e.ctrlKey))) && document.activeElement !== q) {
    e.preventDefault(); q.focus(); q.select();
  }
});
document.getElementById('menuBtn').onclick = () => sidebar.classList.toggle('open');
window.addEventListener('hashchange', route);

if (window.mermaid) {
  const dark = matchMedia('(prefers-color-scheme: dark)').matches;
  mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'default', securityLevel: 'loose' });
}
buildNav();
route();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
