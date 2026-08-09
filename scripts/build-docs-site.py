#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["Markdown>=3.7,<4"]
# ///
"""Gera index.html: a documentação navegável e autocontida do Agent Team.

Uso:
    uv run scripts/build-docs-site.py

Os Markdown do repositório são a fonte de verdade. O arquivo gerado pode ser
aberto diretamente, sem servidor; Mermaid usa CDN com fallback para o código-fonte.
"""

from __future__ import annotations

import html
import json
import os.path
import re
import unicodedata
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "index.html"
SEP = "~"

SECTIONS = [
    {
        "id": "harness",
        "number": "01",
        "title": "Harness",
        "question": "O que torna um repositório operável por agentes?",
        "summary": "Contexto, ferramentas, regras e verificações transformam conhecimento tácito em uma base operacional confiável.",
    },
    {
        "id": "agentes",
        "number": "02",
        "title": "Agentes",
        "question": "Quem executa, com qual autoridade e limite?",
        "summary": "Papéis especializados com missão, contexto, permissões, verificação e um contrato explícito de saída.",
    },
    {
        "id": "skills",
        "number": "03",
        "title": "Skills",
        "question": "Como uma tarefa recorrente é executada corretamente?",
        "summary": "Procedimentos verificáveis reduzem improviso e mantêm artefatos, evidências e critérios consistentes.",
    },
    {
        "id": "loops",
        "number": "04",
        "title": "Loops",
        "question": "Em que ordem os agentes colaboram e quando param?",
        "summary": "Contratos de colaboração organizam tentativas, crítica, convergência, handoffs e gates ao longo da jornada.",
    },
    {
        "id": "metodologia",
        "number": "05",
        "title": "Metodologia",
        "question": "Como as pessoas operam o sistema no dia a dia?",
        "summary": "Papéis humanos, checkpoints, gatilhos e cadências mantêm intenção, risco e aprovação sob controle.",
    },
    {
        "id": "workspace",
        "number": "06",
        "title": "Workspace",
        "question": "Onde o trabalho e os artefatos vivem?",
        "summary": "O espaço operacional preserva ownership, estado, decisões, memória de retomada e evidências de cada execução.",
    },
]

SECTION_BY_ID = {section["id"]: section for section in SECTIONS}
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
MERMAID_BLOCK = re.compile(r"^```mermaid\n(.*?)^```\s*$", re.DOTALL | re.MULTILINE)


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9\s-]", "", value).lower().strip()
    return re.sub(r"[\s-]+", "-", value).strip("-")


def github_slugify(value: str, separator: str = "-") -> str:
    value = unicodedata.normalize("NFC", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"\s", separator, value)


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    meta: dict[str, str] = {}
    match = FRONT_MATTER.match(text)
    if not match:
        return meta, text
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, text[match.end() :]


def title_from(body: str, meta: dict[str, str], fallback: str) -> str:
    if meta.get("title"):
        return meta["title"]
    if meta.get("name"):
        return meta["name"]
    heading = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    return heading.group(1).strip() if heading else fallback


def page(path: str, section: str, group: str, title: str | None = None) -> dict[str, str]:
    return {"path": path, "section": section, "group": group, "title": title or ""}


PAGES = [
    page("README.md", "overview", "Comece aqui", "O que é o Agent Team"),
    page("docs/README.md", "overview", "Comece aqui", "Índice da documentação"),
    page("docs/REPO_HARNESS.md", "harness", "Fundamentos", "Harness do repositório"),
    page("docs/TOOLS.md", "harness", "Controles do repositório", "Tools"),
    page("docs/RULES.md", "harness", "Controles do repositório", "Rules"),
    page("docs/SENSORS.md", "harness", "Controles do repositório", "Sensors"),
    page("docs/GATES.md", "harness", "Controles do repositório", "Gates"),
    page("docs/DOCUMENTATION.md", "harness", "Controles do repositório", "Documentation"),
    page("docs/MCPS.md", "harness", "Controles do repositório", "MCPs"),
    page("docs/AGENTES.md", "agentes", "Fundamentos", "Como os agentes funcionam"),
    page("docs/agentes/README.md", "agentes", "Fundamentos", "Catálogo de contratos"),
    page("agents/README.md", "agentes", "Artefatos executáveis", "Prompts operacionais"),
    page("agents/catalog.md", "agentes", "Artefatos executáveis", "Catálogo materializado"),
    page("agents/meeting-context-agent.md", "agentes", "Materiais de apoio", "Meeting context agent"),
    page("docs/SKILLS.md", "skills", "Fundamentos", "Como as skills funcionam"),
    page("skills/README.md", "skills", "Fundamentos", "Catálogo de skills"),
    page("skills/references/workflow-contract.md", "skills", "Contratos compartilhados", "Contrato de artefatos"),
    page("docs/LOOPS.md", "loops", "Fundamentos", "Como os loops funcionam"),
    page("docs/loops/README.md", "loops", "Fundamentos", "Catálogo de loops"),
    page("workflows/README.md", "loops", "Workflows executáveis", "Mapa dos workflows"),
    page("docs/METODOLOGIA.md", "metodologia", "Fundamentos", "Ciclo de desenvolvimento"),
    page("docs/metodologia/README.md", "metodologia", "Fundamentos", "Páginas da metodologia"),
    page("docs/WORKSPACE.md", "workspace", "Fundamentos", "Onde o trabalho vive"),
    page("docs/workspace/README.md", "workspace", "Fundamentos", "Páginas do workspace"),
    page("workspaces/README.md", "workspace", "Implementações de referência", "Workspaces de exemplo"),
    page("templates/README.md", "workspace", "Templates", "Catálogo de templates"),
    page(
        "workspaces/tech-lead/docs/diagrams/tech-lead-workspace.md",
        "workspace",
        "Infográficos e diagramas",
        "Anatomia do workspace do Tech Lead",
    ),
]


def extend(pattern: str, section: str, group: str, excluded: set[str] | None = None) -> None:
    excluded = excluded or set()
    for source in sorted(ROOT.glob(pattern)):
        relative = source.relative_to(ROOT).as_posix()
        if relative not in excluded and all(item["path"] != relative for item in PAGES):
            PAGES.append(page(relative, section, group))


extend("docs/agentes/*.md", "agentes", "Contratos individuais", {"docs/agentes/README.md"})
extend("agents/*/AGENT.md", "agentes", "Prompts executáveis")
extend("skills/*/SKILL.md", "skills", "Procedimentos executáveis")
extend("docs/loops/[0-9][0-9]-*.md", "loops", "Contratos da jornada")
extend("workflows/[0-9][0-9]-*.md", "loops", "Workflows executáveis")
extend("docs/metodologia/[0-9][0-9]-*.md", "metodologia", "Operação humana")
extend("docs/workspace/[0-9][0-9]-*.md", "workspace", "Estrutura operacional")
for role in ("pm", "ux", "tech-lead"):
    PAGES.append(page(f"workspaces/{role}/README.md", "workspace", "Implementações de referência"))
    PAGES.append(page(f"workspaces/{role}/WORKSPACE.md", "workspace", "Implementações de referência"))
    PAGES.append(page(f"templates/{role}/README.md", "workspace", "Templates"))


def extract_mermaid(text: str) -> tuple[str, list[str]]:
    diagrams: list[str] = []

    def replace(match: re.Match[str]) -> str:
        diagrams.append(match.group(1).rstrip())
        return f"\n\nMERMAIDPLACEHOLDER{len(diagrams) - 1}ENDPLACEHOLDER\n\n"

    return MERMAID_BLOCK.sub(replace, text), diagrams


def restore_mermaid(rendered: str, diagrams: list[str]) -> str:
    for index, source in enumerate(diagrams):
        placeholder = f"MERMAIDPLACEHOLDER{index}ENDPLACEHOLDER"
        block = (
            '<figure class="mermaid-wrap">'
            '<div class="mermaid-head"><figcaption>Diagrama interativo</figcaption>'
            '<div class="mermaid-tools">'
            '<button type="button" data-zoom="out" aria-label="Reduzir diagrama">−</button>'
            '<span data-zoom-label>ajustado</span>'
            '<button type="button" data-zoom="in" aria-label="Ampliar diagrama">+</button>'
            '<button type="button" data-zoom="fit">ajustar</button>'
            "</div></div>"
            f'<pre class="mermaid">{html.escape(source)}</pre>'
            '<p class="mermaid-fallback">A visualização usa Mermaid. Se estiver offline, o código-fonte permanece disponível abaixo.</p>'
            '<details class="mermaid-src"><summary>Ver código do diagrama</summary>'
            f'<pre><code>{html.escape(source)}</code></pre></details>'
            "</figure>"
        )
        rendered = rendered.replace(f"<p>{placeholder}</p>", block).replace(placeholder, block)
    return rendered


def prefix_heading_ids(rendered: str, page_id: str) -> tuple[str, list[dict[str, object]]]:
    toc: list[dict[str, object]] = []

    def replace(match: re.Match[str]) -> str:
        level, attrs, inner = match.group(1), match.group(2), match.group(3)
        found = re.search(r'id="([^"]+)"', attrs)
        raw_id = found.group(1) if found else slugify(re.sub(r"<[^>]+>", "", inner))
        full_id = f"{page_id}{SEP}{raw_id}"
        if level in ("2", "3"):
            toc.append(
                {
                    "level": int(level),
                    "id": full_id,
                    "anchor": raw_id,
                    "text": html.unescape(re.sub(r"<[^>]+>", "", inner)).strip(),
                }
            )
        attrs = re.sub(r'\s*id="[^"]+"', "", attrs)
        return f'<h{level}{attrs} id="{full_id}">{inner}</h{level}>'

    return re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", replace, rendered, flags=re.DOTALL), toc


def rewrite_links(
    rendered: str,
    page_map: dict[str, dict[str, str]],
    current: Path,
    current_page: dict[str, str],
) -> str:
    def route(target_page: dict[str, str], fragment: str = "") -> str:
        target = (
            f"#/documento/{target_page['id']}"
            if target_page["section"] == "overview"
            else f"#/secao/{target_page['section']}/{target_page['id']}"
        )
        return f"{target}{SEP}{fragment}" if fragment else target

    def replace(match: re.Match[str]) -> str:
        href = html.unescape(match.group(1))
        if href.startswith(("http://", "https://", "mailto:", "tel:")):
            return match.group(0)
        if href.startswith("#"):
            return f'href="{route(current_page, href[1:])}"'
        target, _, fragment = href.partition("#")
        resolved = (current.parent / target).resolve()
        try:
            key = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            return match.group(0)
        if key in page_map:
            return f'href="{route(page_map[key], fragment)}"'
        relative = os.path.relpath(resolved, OUTPUT.parent)
        suffix = f"#{fragment}" if fragment else ""
        return f'href="{html.escape(relative + suffix)}" class="external-file" title="Abrir {html.escape(key)}"'

    return re.sub(r'href="([^"]+)"', replace, rendered)


def plain_text(rendered: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", rendered))).strip()


def build() -> None:
    missing = [item["path"] for item in PAGES if not (ROOT / item["path"]).is_file()]
    if missing:
        raise SystemExit("Documentos obrigatórios ausentes:\n- " + "\n- ".join(missing))

    path_ids: dict[str, str] = {}
    route_ids: set[str] = set()
    for item in PAGES:
        page_id = slugify(item["path"].removesuffix(".md").replace("/", " "))
        if page_id in route_ids:
            raise SystemExit(f"Rota duplicada: {page_id}")
        route_ids.add(page_id)
        path_ids[item["path"]] = page_id

    converter = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
        extension_configs={"toc": {"slugify": github_slugify}},
        output_format="html5",
    )
    page_map: dict[str, dict[str, str]] = {}
    prepared: list[tuple[dict[str, str], Path, dict[str, str], str, list[str]]] = []

    for item in PAGES:
        source = ROOT / item["path"]
        meta, body = parse_front_matter(source.read_text(encoding="utf-8"))
        title = item["title"] or title_from(body, meta, source.stem.replace("-", " ").title())
        body, diagrams = extract_mermaid(body)
        enriched = {**item, "id": path_ids[item["path"]], "title": title}
        page_map[item["path"]] = enriched
        prepared.append((enriched, source, meta, body, diagrams))

    pages: list[dict[str, object]] = []
    for item, source, meta, body, diagrams in prepared:
        converter.reset()
        rendered = converter.convert(body)
        rendered = restore_mermaid(rendered, diagrams)
        if "<h1" not in rendered:
            description = meta.get("description", "")
            lede = f"<blockquote><p>{html.escape(description)}</p></blockquote>" if description else ""
            rendered = f"<h1>{html.escape(item['title'])}</h1>{lede}{rendered}"
        rendered, toc = prefix_heading_ids(rendered, item["id"])
        rendered = rewrite_links(rendered, page_map, source, item)
        text = plain_text(rendered)
        pages.append(
            {
                **item,
                "status": meta.get("status", ""),
                "updated": meta.get("updated_at", ""),
                "html": rendered,
                "toc": toc,
                "excerpt": text[:210] + ("…" if len(text) > 210 else ""),
                "text": text.lower(),
            }
        )

    sections = []
    for section in SECTIONS:
        if not any(item["section"] == section["id"] for item in pages):
            raise SystemExit(f"Macro seção vazia: {section['id']}")
        sections.append(section)

    payload = json.dumps(
        {"sections": sections, "pages": pages, "buildDate": date.today().isoformat()},
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")
    OUTPUT.write_text(TEMPLATE.replace("/*__DATA__*/", payload), encoding="utf-8")
    print(f"site gerado: {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size // 1024} KB)")


TEMPLATE = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b0f12">
<meta name="description" content="Documentação interativa do Agent Team: harness, agentes, skills, loops, metodologia e workspace.">
<title>Agent Team — documentação interativa</title>
<style>
:root {
  color-scheme: dark;
  --bg-deep:#0b0f12; --bg:#10161a; --charcoal:#161c21; --elevated:#20282e;
  --elevated-2:#263139; --line:#31404a; --line-soft:rgba(124,157,171,.17);
  --cyan:#22d3ee; --cyan-strong:#06b6d4; --cyan-soft:rgba(34,211,238,.12);
  --text:#e8f0f3; --muted:#93a4ae; --faint:#60727d; --success:#5ee6b3;
  --warning:#f2c66d; --sidebar:288px; --reading:820px;
  --sans:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"SFMono-Regular",Consolas,"Liberation Mono",monospace;
}
*{box-sizing:border-box} html{scroll-behavior:smooth} body{margin:0;background:var(--bg-deep);color:var(--text);font:15px/1.68 var(--sans);-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0;z-index:-2;background:radial-gradient(circle at 75% 12%,rgba(34,211,238,.08),transparent 27rem),linear-gradient(rgba(255,255,255,.017) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.017) 1px,transparent 1px);background-size:auto,36px 36px,36px 36px}
a{color:inherit}.reading-progress{position:fixed;z-index:90;top:0;left:0;height:2px;width:0;background:var(--cyan);box-shadow:0 0 14px var(--cyan);transition:width .08s linear}
.app{display:grid;grid-template-columns:var(--sidebar) minmax(0,1fr);min-height:100vh}.sidebar{position:sticky;top:0;height:100vh;border-right:1px solid var(--line-soft);background:rgba(14,20,24,.92);backdrop-filter:blur(20px);display:flex;flex-direction:column;z-index:50}
.brand{display:flex;gap:12px;align-items:center;padding:22px 20px 18px;text-decoration:none;border-bottom:1px solid var(--line-soft)}.brand-mark{width:37px;height:37px;border:1px solid rgba(34,211,238,.42);background:linear-gradient(145deg,rgba(34,211,238,.18),rgba(34,211,238,.02));display:grid;place-items:center;color:var(--cyan);font:bold 12px var(--mono);clip-path:polygon(50% 0,100% 100%,0 100%)}.brand-copy strong{display:block;letter-spacing:-.01em}.brand-copy span{display:block;color:var(--faint);font:10px var(--mono);letter-spacing:.12em;text-transform:uppercase;margin-top:2px}
.search-box{padding:15px 14px 12px;position:relative}.search-box label{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.search-box input{width:100%;border:1px solid var(--line);background:var(--charcoal);color:var(--text);border-radius:10px;padding:10px 36px 10px 12px;font:13px var(--sans);outline:0}.search-box input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px var(--cyan-soft)}.shortcut{position:absolute;right:24px;top:25px;color:var(--faint);font:10px var(--mono);border:1px solid var(--line);border-radius:4px;padding:1px 5px}
.nav-scroll{overflow:auto;padding:4px 10px 30px}.nav-label{color:var(--faint);font:10px var(--mono);letter-spacing:.14em;text-transform:uppercase;padding:15px 10px 7px}.nav-link{display:flex;align-items:center;gap:9px;text-decoration:none;color:var(--muted);border:1px solid transparent;border-radius:9px;padding:8px 9px;margin:2px 0;line-height:1.3}.nav-link:hover{color:var(--text);background:rgba(255,255,255,.025)}.nav-link.active{color:var(--cyan);border-color:rgba(34,211,238,.2);background:var(--cyan-soft)}.nav-num{font:10px var(--mono);color:var(--faint);width:21px}.nav-link.active .nav-num{color:var(--cyan)}.nav-divider{height:1px;background:var(--line-soft);margin:12px 10px}.context-group{margin-bottom:7px}.context-group summary{cursor:pointer;color:var(--faint);font:10px var(--mono);letter-spacing:.09em;text-transform:uppercase;padding:8px 10px;list-style:none}.context-group summary::-webkit-details-marker{display:none}.context-group summary::before{content:"+";margin-right:7px;color:var(--cyan)}.context-group[open] summary::before{content:"−"}.context-group .nav-link{font-size:12px;padding:7px 9px 7px 15px}
.main{min-width:0}.view{min-height:100vh}.menu-toggle{display:none;position:fixed;z-index:70;top:14px;left:14px;border:1px solid var(--line);background:var(--charcoal);color:var(--text);border-radius:9px;width:42px;height:42px;font-size:18px}.overlay{display:none}
.home{max-width:1440px;margin:auto;padding:clamp(34px,5vw,76px)}.hero{min-height:calc(100vh - 152px);display:grid;grid-template-columns:minmax(0,.82fr) minmax(520px,1.18fr);column-gap:clamp(36px,6vw,92px);row-gap:clamp(30px,4vw,54px);align-items:center}.hero-heading{grid-column:1/-1;max-width:1040px}.eyebrow{color:var(--cyan);font:11px var(--mono);letter-spacing:.16em;text-transform:uppercase;display:flex;align-items:center;gap:10px}.eyebrow::before{content:"";width:28px;height:1px;background:var(--cyan)}.hero h1{font-size:clamp(52px,7.2vw,104px);line-height:.92;letter-spacing:-.06em;margin:20px 0 0;max-width:980px}.hero h1 span{color:var(--cyan)}.hero-copy{align-self:start;padding-top:8px}.hero-lede{color:var(--muted);font-size:clamp(16px,1.4vw,20px);max-width:590px;margin-top:0}.hero-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:32px}.button{display:inline-flex;align-items:center;gap:10px;text-decoration:none;border:1px solid var(--line);border-radius:10px;padding:11px 15px;font-weight:650}.button.primary{background:var(--cyan);border-color:var(--cyan);color:#062127}.button:hover{transform:translateY(-1px);border-color:var(--cyan)}.button .arrow{font-family:var(--mono)}
.layers-panel{position:relative;padding:28px 26px 24px;border:1px solid var(--line-soft);background:linear-gradient(160deg,rgba(32,40,46,.86),rgba(11,15,18,.52));border-radius:24px;box-shadow:0 34px 90px rgba(0,0,0,.35),inset 0 1px rgba(255,255,255,.04);overflow:hidden}.layers-panel::after{content:"";position:absolute;width:320px;height:320px;border:1px solid rgba(34,211,238,.08);border-radius:50%;right:-150px;top:-150px;box-shadow:0 0 80px rgba(34,211,238,.04)}.layers-head{display:flex;justify-content:space-between;align-items:end;margin:0 4px 18px}.layers-head strong{font-size:14px}.layers-head span{color:var(--faint);font:10px var(--mono);letter-spacing:.08em;text-transform:uppercase}.layers{display:grid;gap:8px;position:relative;z-index:1}.layer{width:100%;min-height:66px;padding:12px 18px;display:grid;grid-template-columns:34px minmax(118px,.42fr) minmax(0,1fr);align-items:center;gap:12px;text-decoration:none;background:linear-gradient(90deg,rgba(34,211,238,.04),rgba(34,211,238,.12),rgba(34,211,238,.04));border:1px solid rgba(34,211,238,.18);border-radius:10px;transition:transform .22s ease,filter .22s ease,background .22s ease}.layer:hover,.layer:focus-visible{background:linear-gradient(90deg,rgba(34,211,238,.13),rgba(34,211,238,.28),rgba(34,211,238,.13));filter:drop-shadow(0 0 14px rgba(34,211,238,.2));transform:translateX(5px);outline:0}.layer-number{font:10px var(--mono);color:var(--cyan)}.layer-title{font-weight:750;letter-spacing:.02em}.layer-question{color:var(--muted);font-size:11px;line-height:1.45}.layers-base{display:flex;justify-content:space-between;color:var(--faint);font:9px var(--mono);text-transform:uppercase;letter-spacing:.13em;margin:14px 5px 0}
.section-view{max-width:1260px;margin:auto;padding:clamp(70px,8vw,110px) clamp(26px,6vw,82px)}.breadcrumbs{display:flex;align-items:center;gap:8px;color:var(--faint);font:11px var(--mono);margin-bottom:32px}.breadcrumbs a{text-decoration:none}.breadcrumbs a:hover{color:var(--cyan)}.section-hero{padding-bottom:44px;border-bottom:1px solid var(--line-soft)}.section-index{font:11px var(--mono);color:var(--cyan);letter-spacing:.14em;text-transform:uppercase}.section-hero h1{font-size:clamp(54px,8vw,102px);line-height:.9;letter-spacing:-.055em;margin:16px 0 23px}.section-question{font-size:clamp(18px,2vw,25px);margin:0 0 12px;max-width:770px}.section-summary{color:var(--muted);max-width:760px;margin:0}
.layer-track{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin:30px 0 62px}.track-item{height:6px;background:var(--elevated);border-radius:9px;position:relative}.track-item.active{background:var(--cyan);box-shadow:0 0 14px rgba(34,211,238,.34)}.track-item span{position:absolute;top:13px;left:0;color:var(--faint);font:8px var(--mono);text-transform:uppercase;white-space:nowrap}.track-item.active span{color:var(--cyan)}
.group-block{margin-top:50px}.group-head{margin-bottom:16px}.group-head h2{font-size:13px;text-transform:uppercase;letter-spacing:.12em;margin:0}.page-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.page-card{display:flex;flex-direction:column;min-height:194px;text-decoration:none;border:1px solid var(--line-soft);border-radius:14px;padding:21px;background:rgba(22,28,33,.66);transition:border .18s ease,transform .18s ease,background .18s ease}.page-card:hover,.page-card:focus-visible{border-color:rgba(34,211,238,.45);background:var(--charcoal);transform:translateY(-2px);outline:0}.card-action{align-self:flex-end;color:var(--faint);font:9px var(--mono);text-transform:uppercase;letter-spacing:.08em}.card-title{font-size:18px;line-height:1.25;margin:17px 0 10px}.card-excerpt{color:var(--muted);font-size:12px;line-height:1.55;margin:0}.card-path{color:var(--faint);font:9px var(--mono);margin-top:auto;padding-top:17px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.doc-page{max-width:1220px;margin:auto;padding:72px clamp(24px,6vw,76px) 120px}.doc-grid{display:grid;grid-template-columns:minmax(0,var(--reading)) 230px;gap:64px;align-items:start}.doc-meta{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:20px}.badge{font:9px var(--mono);letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--line);border-radius:99px;padding:4px 8px;color:var(--muted)}.badge.canonical{color:var(--success);border-color:rgba(94,230,179,.28)}.badge.proposed{color:var(--warning);border-color:rgba(242,198,109,.28)}.source-path{font:10px var(--mono);color:var(--faint);text-decoration:none}.source-path:hover{color:var(--cyan)}
.article h1{font-size:clamp(38px,5vw,62px);line-height:1.02;letter-spacing:-.04em;margin:0 0 29px}.article h2{font-size:27px;line-height:1.2;letter-spacing:-.025em;margin:58px 0 18px;padding-top:24px;border-top:1px solid var(--line-soft)}.article h3{font-size:19px;margin:36px 0 13px}.article h4{font-size:15px;color:var(--muted);margin:28px 0 10px}.article p{margin:0 0 17px}.article a{color:var(--cyan);text-decoration:none;border-bottom:1px solid rgba(34,211,238,.26)}.article a:hover{border-color:var(--cyan)}.article blockquote{margin:0 0 28px;border-left:2px solid var(--cyan);padding:14px 18px;background:var(--cyan-soft);color:#bdd0d8}.article ul,.article ol{padding-left:22px;margin:0 0 21px}.article li{margin:6px 0}.article hr{border:0;border-top:1px solid var(--line-soft);margin:42px 0}.article code{font:13px var(--mono);background:var(--elevated);padding:2px 5px;border-radius:4px;color:#bdebf3}.article pre{background:#0c1114;border:1px solid var(--line-soft);border-radius:12px;padding:17px 19px;overflow:auto;margin:0 0 23px;line-height:1.55}.article pre code{background:none;padding:0;color:#c5d1d6}.article table{display:block;width:100%;overflow:auto;border-collapse:collapse;margin:0 0 27px;font-size:13px}.article th,.article td{border:1px solid var(--line-soft);padding:10px 12px;text-align:left;vertical-align:top}.article th{background:var(--elevated);white-space:nowrap}.article tr:nth-child(even) td{background:rgba(32,40,46,.36)}.article img{max-width:100%}.article details{margin:16px 0}.article summary{cursor:pointer;color:var(--cyan)}
.toc{position:sticky;top:36px;border-left:1px solid var(--line-soft);padding-left:20px;max-height:calc(100vh - 72px);overflow:auto}.toc-title{font:9px var(--mono);letter-spacing:.13em;text-transform:uppercase;color:var(--faint);margin-bottom:13px}.toc a{display:block;color:var(--muted);text-decoration:none;font-size:11px;line-height:1.35;padding:6px 0}.toc a.level-3{padding-left:12px;color:var(--faint)}.toc a:hover{color:var(--cyan)}
.pager{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:70px;padding-top:24px;border-top:1px solid var(--line-soft)}.pager-link{border:1px solid var(--line-soft);border-radius:12px;padding:15px;text-decoration:none}.pager-link:last-child{text-align:right}.pager-link:hover{border-color:var(--cyan)}.pager-link span{display:block;color:var(--faint);font:9px var(--mono);text-transform:uppercase}.pager-link strong{display:block;margin-top:4px;font-size:13px}.pager-spacer{min-height:1px}
.mermaid-wrap{margin:28px 0;border:1px solid var(--line-soft);border-radius:14px;background:var(--charcoal);padding:15px;overflow:auto}.mermaid-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}.mermaid-head figcaption{font:9px var(--mono);text-transform:uppercase;letter-spacing:.1em;color:var(--faint)}.mermaid-tools{display:flex;gap:5px;align-items:center}.mermaid-tools button{border:1px solid var(--line);background:var(--bg);color:var(--muted);border-radius:6px;padding:5px 8px;font:11px var(--mono);cursor:pointer}.mermaid-tools button:hover{color:var(--cyan);border-color:var(--cyan)}.mermaid-tools span{font:9px var(--mono);color:var(--faint);min-width:54px;text-align:center}.mermaid{background:transparent!important;border:0!important;text-align:center;margin:0!important}.mermaid svg{max-width:100%;height:auto}.mermaid-fallback{font-size:11px;color:var(--faint);margin:10px 0 0!important}.mermaid-wrap.rendered .mermaid-fallback{display:none}.mermaid-src{font-size:11px;margin-top:10px!important}
.search-view{max-width:1000px;margin:auto;padding:90px clamp(24px,6vw,70px)}.search-view h1{font-size:clamp(42px,6vw,74px);letter-spacing:-.05em;margin:10px 0}.search-intro{color:var(--muted);margin-bottom:40px}.result-list{display:grid;gap:10px}.result{display:grid;grid-template-columns:95px 1fr auto;gap:18px;align-items:start;text-decoration:none;padding:18px;border:1px solid var(--line-soft);border-radius:12px;background:rgba(22,28,33,.55)}.result:hover{border-color:var(--cyan)}.result-section{font:9px var(--mono);text-transform:uppercase;color:var(--cyan)}.result strong{display:block}.result p{margin:5px 0 0;color:var(--muted);font-size:12px}.result-path{font:9px var(--mono);color:var(--faint)}.empty-state{border:1px dashed var(--line);border-radius:14px;padding:36px;color:var(--muted)}
.not-found{max-width:700px;margin:auto;padding:120px 30px}.not-found strong{font:100px/1 var(--mono);color:var(--cyan)}.not-found h1{font-size:42px}.not-found p{color:var(--muted)}
@media(max-width:1080px){.hero{grid-template-columns:1fr;min-height:auto}.hero-heading{grid-column:auto}.layers-panel{max-width:720px;width:100%;margin:auto}.doc-grid{grid-template-columns:minmax(0,1fr) 200px;gap:36px}}
@media(max-width:900px){.app{display:block}.sidebar{position:fixed;left:0;transform:translateX(-105%);width:min(88vw,320px);transition:transform .2s ease}.sidebar.open{transform:none}.menu-toggle{display:block}.overlay{display:block;position:fixed;inset:0;z-index:40;background:rgba(0,0,0,.6);opacity:0;pointer-events:none;transition:opacity .2s}.overlay.open{opacity:1;pointer-events:auto}.home,.section-view,.doc-page,.search-view{padding-top:82px}.doc-grid{display:block}.toc{position:static;border-left:0;border-top:1px solid var(--line-soft);padding:24px 0 0;margin-top:45px;max-height:none}}
@media(max-width:650px){.home{padding-left:18px;padding-right:18px}.hero h1{font-size:clamp(46px,14vw,62px)}.layers-panel{padding:22px 14px}.layers-head{align-items:start;gap:12px}.layers-head span{line-height:1.4;text-align:right}.layer{grid-template-columns:28px 1fr;gap:8px;min-height:58px;padding:10px 12px}.layer-question{grid-column:2;font-size:10px}.page-grid{grid-template-columns:1fr}.section-view{padding-left:18px;padding-right:18px}.section-hero h1{font-size:55px}.layer-track span{display:none}.doc-page{padding-left:18px;padding-right:18px}.pager{grid-template-columns:1fr}.pager-link:last-child{text-align:left}.result{grid-template-columns:1fr}.result-path{display:none}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}.button:hover,.page-card:hover,.layer:hover{transform:none}}
@media print{.sidebar,.menu-toggle,.overlay,.reading-progress,.toc,.pager{display:none!important}.app{display:block}.doc-page{padding:20px}.doc-grid{display:block}.article{max-width:none}.article a{color:inherit}}
</style>
</head>
<body>
<div class="reading-progress" id="reading-progress"></div>
<button class="menu-toggle" id="menu-toggle" type="button" aria-label="Abrir navegação" aria-expanded="false">☰</button>
<div class="app">
  <aside class="sidebar" id="sidebar">
    <a class="brand" href="#/" aria-label="Agent Team — início">
      <span class="brand-mark">AT</span><span class="brand-copy"><strong>Agent Team</strong><span>operating system</span></span>
    </a>
    <div class="search-box"><label for="global-search">Buscar na documentação</label><input id="global-search" type="search" placeholder="Buscar conceito, agente, skill…" autocomplete="off"><span class="shortcut">/</span></div>
    <nav class="nav-scroll" id="navigation" aria-label="Navegação principal"></nav>
  </aside>
  <div class="overlay" id="overlay"></div>
  <main class="main"><div class="view" id="view"></div></main>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
const DATA=/*__DATA__*/;
const view=document.querySelector('#view'),nav=document.querySelector('#navigation');
const searchInput=document.querySelector('#global-search'),sidebar=document.querySelector('#sidebar');
const menuToggle=document.querySelector('#menu-toggle'),overlay=document.querySelector('#overlay');
const progress=document.querySelector('#reading-progress');
const pagesById=new Map(DATA.pages.map(page=>[page.id,page]));
const sectionsById=new Map(DATA.sections.map(section=>[section.id,section]));
let activePage=null;
const esc=value=>String(value??'').replace(/[&<>"]/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[char]));
const routeFor=page=>page.section==='overview'?`#/documento/${page.id}`:`#/secao/${page.section}/${page.id}`;
const sectionRoute=section=>`#/secao/${section.id}`;
function closeMenu(){sidebar.classList.remove('open');overlay.classList.remove('open');menuToggle.setAttribute('aria-expanded','false')}
function groupsFor(sectionId){const groups=new Map();DATA.pages.filter(p=>p.section===sectionId).forEach(page=>{if(!groups.has(page.group))groups.set(page.group,[]);groups.get(page.group).push(page)});return groups}
function renderNav(sectionId='',pageId=''){
  const layers=DATA.sections.map(section=>`<a class="nav-link ${section.id===sectionId?'active':''}" href="${sectionRoute(section)}"><span class="nav-num">${section.number}</span><span>${esc(section.title)}</span></a>`).join('');
  let context='';
  if(sectionsById.has(sectionId)){
    context='<div class="nav-divider"></div><div class="nav-label">Nesta camada</div>';
    for(const [group,pages] of groupsFor(sectionId)) context+=`<details class="context-group" open><summary>${esc(group)}</summary>${pages.map(page=>`<a class="nav-link ${page.id===pageId?'active':''}" href="${routeFor(page)}">${esc(page.title)}</a>`).join('')}</details>`;
  }
  nav.innerHTML=`<div class="nav-label">Explorar</div><a class="nav-link ${!sectionId?'active':''}" href="#/"><span class="nav-num">00</span><span>Visão geral</span></a><div class="nav-label">As seis camadas</div>${layers}${context}`;
}
function homeMarkup(){
  const layers=DATA.sections.map(section=>`<a class="layer" href="${sectionRoute(section)}" aria-label="Camada ${section.number}, ${esc(section.title)}: ${esc(section.question)}"><span class="layer-number">${section.number}</span><span class="layer-title">${esc(section.title)}</span><span class="layer-question">${esc(section.question)}</span></a>`).join('');
  return `<section class="home"><div class="hero"><div class="hero-heading"><div class="eyebrow">Documentação operacional</div><h1>Um sistema para times que <span>dirigem agentes.</span></h1></div><div class="hero-copy"><p class="hero-lede">O Agent Team transforma intenção, contexto e verificação em um ciclo de desenvolvimento operável. Explore da fundação técnica ao lugar onde cada decisão deixa rastro.</p><div class="hero-actions"><a class="button primary" href="${sectionRoute(DATA.sections[0])}">Começar pela base <span class="arrow">→</span></a><a class="button" href="${routeFor(DATA.pages[1])}">Ver índice completo</a></div></div><div class="layers-panel"><div class="layers-head"><strong>Camadas operacionais</strong><span>clique para explorar</span></div><div class="layers">${layers}</div><div class="layers-base"><span>fundação</span><span>operação</span></div></div></div></section>`;
}
function renderHome(){activePage=null;view.innerHTML=homeMarkup();renderNav();document.title='Agent Team — documentação interativa';progress.style.width='0';window.scrollTo(0,0);renderDiagrams()}
function trackMarkup(active){return `<div class="layer-track" aria-label="Posição nas camadas">${DATA.sections.map(s=>`<a class="track-item ${s.id===active?'active':''}" href="${sectionRoute(s)}" aria-label="${esc(s.title)}"><span>${esc(s.title)}</span></a>`).join('')}</div>`}
function renderSection(section){
  activePage=null;let blocks='';
  for(const [group,pages] of groupsFor(section.id)) blocks+=`<section class="group-block"><div class="group-head"><h2>${esc(group)}</h2></div><div class="page-grid">${pages.map(page=>`<a class="page-card" href="${routeFor(page)}"><span class="card-action">abrir ↗</span><strong class="card-title">${esc(page.title)}</strong><p class="card-excerpt">${esc(page.excerpt)}</p><span class="card-path">${esc(page.path)}</span></a>`).join('')}</div></section>`;
  view.innerHTML=`<section class="section-view"><div class="breadcrumbs"><a href="#/">INÍCIO</a><span>/</span><span>CAMADA ${section.number}</span></div><header class="section-hero"><div class="section-index">camada operacional</div><h1>${esc(section.title)}</h1><p class="section-question">${esc(section.question)}</p><p class="section-summary">${esc(section.summary)}</p></header>${trackMarkup(section.id)}${blocks}</section>`;
  renderNav(section.id);document.title=`${section.title} — Agent Team`;progress.style.width='0';window.scrollTo(0,0);closeMenu();
}
function tocMarkup(page){if(!page.toc.length)return page.section==='overview'?'<div class="toc-title">Visão geral</div><a href="#/">Voltar ao mapa</a>':`<div class="toc-title">Nesta camada</div><a href="${sectionRoute(sectionsById.get(page.section))}">Ver todas as subseções</a>`;return `<div class="toc-title">Neste documento</div>${page.toc.map(item=>`<a class="level-${item.level}" href="${routeFor(page)}~${encodeURIComponent(item.anchor)}">${esc(item.text)}</a>`).join('')}`}
function renderDocument(page,anchor=''){
  activePage=page;const siblings=DATA.pages.filter(item=>item.section===page.section);const index=siblings.findIndex(item=>item.id===page.id),previous=siblings[index-1],next=siblings[index+1];const section=sectionsById.get(page.section),sectionTitle=section?.title||'Visão geral',sectionHref=section?sectionRoute(section):'#/';
  const badge=page.status?`<span class="badge ${esc(page.status)}">${esc(page.status)}</span>`:'';
  const updated=page.updated?`<span class="badge">atualizado ${esc(page.updated)}</span>`:'';
  view.innerHTML=`<section class="doc-page"><div class="breadcrumbs"><a href="#/">INÍCIO</a><span>/</span><a href="${sectionHref}">${esc(sectionTitle)}</a><span>/</span><span>${esc(page.group)}</span></div><div class="doc-grid"><article class="article"><div class="doc-meta">${badge}${updated}<a class="source-path" href="${esc(page.path)}">${esc(page.path)}</a></div>${page.html}<nav class="pager" aria-label="Documentos adjacentes">${previous?`<a class="pager-link" href="${routeFor(previous)}"><span>← anterior</span><strong>${esc(previous.title)}</strong></a>`:'<span class="pager-spacer"></span>'}${next?`<a class="pager-link" href="${routeFor(next)}"><span>próximo →</span><strong>${esc(next.title)}</strong></a>`:'<span class="pager-spacer"></span>'}</nav></article><aside class="toc">${tocMarkup(page)}</aside></div></section>`;
  renderNav(section?page.section:'',page.id);document.title=`${page.title} — Agent Team`;closeMenu();renderDiagrams();
  requestAnimationFrame(()=>{if(anchor){const target=document.getElementById(`${page.id}~${decodeURIComponent(anchor)}`);if(target)target.scrollIntoView()}else window.scrollTo(0,0);updateProgress()});
}
function score(page,term){let value=0;if(page.title.toLowerCase().includes(term))value+=12;if(page.group.toLowerCase().includes(term))value+=6;if(page.path.toLowerCase().includes(term))value+=5;if(page.text.includes(term))value+=2;return value}
function renderSearch(term){
  activePage=null;const query=term.trim().toLowerCase();let content='';
  if(!query)content='<div class="empty-state">Digite um conceito, agente, skill, artefato ou etapa da jornada.</div>';
  else{const results=DATA.pages.map(page=>({page,score:score(page,query)})).filter(item=>item.score).sort((a,b)=>b.score-a.score||a.page.title.localeCompare(b.page.title)).slice(0,40);content=results.length?`<div class="result-list">${results.map(({page})=>`<a class="result" href="${routeFor(page)}"><span class="result-section">${esc(sectionsById.get(page.section)?.title||'Visão geral')}</span><span><strong>${esc(page.title)}</strong><p>${esc(page.excerpt)}</p></span><span class="result-path">${esc(page.path)}</span></a>`).join('')}</div>`:'<div class="empty-state">Nenhum documento encontrado. Tente um termo mais amplo.</div>'}
  view.innerHTML=`<section class="search-view"><div class="eyebrow">Busca global</div><h1>${query?`Resultados para “${esc(term)}”`:'Explore o acervo'}</h1><p class="search-intro">Pesquise por títulos, caminhos e conteúdo da documentação.</p>${content}</section>`;renderNav();document.title=`Busca${term?` — ${term}`:''} — Agent Team`;progress.style.width='0';window.scrollTo(0,0);
}
function renderNotFound(){view.innerHTML='<section class="not-found"><strong>404</strong><h1>Esta rota não existe.</h1><p>A documentação pode ter mudado de lugar. Volte ao mapa principal para continuar.</p><a class="button primary" href="#/">Voltar ao início</a></section>';renderNav();document.title='Não encontrado — Agent Team';progress.style.width='0'}
function parseRoute(){const raw=location.hash.slice(1)||'/';const split=raw.indexOf('~'),path=split>=0?raw.slice(0,split):raw,anchor=split>=0?raw.slice(split+1):'';return {path,anchor}}
function route(){const {path,anchor}=parseRoute();if(path==='/'){renderHome();return}if(path.startsWith('/busca')){const query=new URLSearchParams(path.split('?')[1]||'').get('q')||'';searchInput.value=query;renderSearch(query);return}const parts=path.split('/').filter(Boolean);if(parts[0]==='documento'){const page=pagesById.get(parts[1]);if(page?.section==='overview'){renderDocument(page,anchor);return}}if(parts[0]==='secao'&&sectionsById.has(parts[1])){const section=sectionsById.get(parts[1]);if(parts.length===2){renderSection(section);return}const page=pagesById.get(parts[2]);if(page&&page.section===section.id){renderDocument(page,anchor);return}}renderNotFound()}
async function renderDiagrams(){const wraps=[...document.querySelectorAll('.mermaid-wrap')];if(!wraps.length)return;if(!window.mermaid)return;try{const nodes=wraps.map(wrap=>wrap.querySelector('.mermaid'));await mermaid.run({nodes});wraps.forEach(wrap=>wrap.classList.add('rendered'))}catch(error){console.warn('Mermaid indisponível',error)}}
function applyZoom(wrap,scale){const svg=wrap.querySelector('.mermaid svg');if(!svg)return;wrap.dataset.scale=String(scale);svg.style.maxWidth='none';svg.style.width=`${scale*100}%`;wrap.querySelector('[data-zoom-label]').textContent=scale===1?'ajustado':`${Math.round(scale*100)}%`}
document.addEventListener('click',event=>{const button=event.target.closest('[data-zoom]');if(button){const wrap=button.closest('.mermaid-wrap');let scale=Number(wrap.dataset.scale||1);if(button.dataset.zoom==='in')scale=Math.min(2.5,scale+.25);if(button.dataset.zoom==='out')scale=Math.max(.5,scale-.25);if(button.dataset.zoom==='fit')scale=1;applyZoom(wrap,scale)}if(event.target.closest('a')&&innerWidth<=900)closeMenu()});
function updateProgress(){if(!activePage){progress.style.width='0';return}const height=document.documentElement.scrollHeight-innerHeight;const value=height>0?Math.min(100,scrollY/height*100):0;progress.style.width=`${value}%`}
searchInput.addEventListener('input',event=>{const term=event.target.value;history.replaceState(null,'',`#/busca?q=${encodeURIComponent(term)}`);renderSearch(term)});
searchInput.addEventListener('keydown',event=>{if(event.key==='Enter')location.hash=`/busca?q=${encodeURIComponent(searchInput.value)}`});
menuToggle.addEventListener('click',()=>{const open=sidebar.classList.toggle('open');overlay.classList.toggle('open',open);menuToggle.setAttribute('aria-expanded',String(open))});overlay.addEventListener('click',closeMenu);
document.addEventListener('keydown',event=>{if(event.key==='/'&&!/input|textarea/i.test(document.activeElement.tagName)){event.preventDefault();searchInput.focus()}if(event.key==='Escape'){closeMenu();if(document.activeElement===searchInput){searchInput.value='';searchInput.blur();location.hash='/'}}});
window.addEventListener('hashchange',route);window.addEventListener('scroll',updateProgress,{passive:true});window.addEventListener('load',renderDiagrams);
if(window.mermaid)mermaid.initialize({startOnLoad:false,theme:'dark',securityLevel:'loose',themeVariables:{background:'#161c21',primaryColor:'#20282e',primaryTextColor:'#e8f0f3',primaryBorderColor:'#22d3ee',lineColor:'#60727d',secondaryColor:'#10161a',tertiaryColor:'#263139'}});
route();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    build()
