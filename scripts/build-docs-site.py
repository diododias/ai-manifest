#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["Markdown>=3.7,<4"]
# ///
"""Generates index.html and index.pt.html: Agent Team's navigable, self-contained documentation.

Uso:
    uv run scripts/build-docs-site.py

Repository Markdown files are the source of truth. The generated files can be
opened directly, without a server; Mermaid uses a CDN with a source-code fallback.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import quote

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "index.html"
OUTPUT_PT = ROOT / "index.pt.html"
SEP = "~"
GITHUB_REPOSITORY = "https://github.com/diododias/ai-manifest"
GITHUB_REF = "language/english"
GITHUB_REF_PT = "language/portuguese"
LINKEDIN_PROFILE = "https://www.linkedin.com/in/luiz-gustavo-dias/"
EMAIL_ADDRESS = "luizdiodo@icloud.com"

SECTIONS = [
    {
        "id": "harness",
        "number": "01",
        "title": "Harness",
        "question": "What makes a repository operable by agents?",
        "summary": "Context, tools, rules, and verification turn tacit knowledge into a reliable operating foundation.",
    },
    {
        "id": "agentes",
        "number": "02",
        "title": "Agents",
        "question": "Who executes, with what authority and limits?",
        "summary": "Specialized roles with a mission, context, permissions, verification, and an explicit output contract.",
    },
    {
        "id": "skills",
        "number": "03",
        "title": "Skills",
        "question": "How is a recurring task executed correctly?",
        "summary": "Verifiable procedures reduce improvisation and keep artifacts, evidence, and criteria consistent.",
    },
    {
        "id": "loops",
        "number": "04",
        "title": "Loops",
        "question": "In what order do agents collaborate, and when do they stop?",
        "summary": "Collaboration contracts organize attempts, critique, convergence, handoffs, and gates across the journey.",
    },
    {
        "id": "metodologia",
        "number": "05",
        "title": "Methodology",
        "question": "How do people operate the system day to day?",
        "summary": "Human roles, checkpoints, triggers, and cadences keep intent, risk, and approval under control.",
    },
    {
        "id": "workspace",
        "number": "06",
        "title": "Workspace",
        "question": "Where do work and artifacts live?",
        "summary": "The operating space preserves ownership, state, decisions, resumption memory, and evidence for every execution.",
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
    heading = re.search(r"^#\s*(?:\d+\s*[—\-]\s*)?(.+?)\s*$", body, re.MULTILINE)
    return heading.group(1).strip() if heading else fallback


def page(path: str, section: str, group: str, title: str | None = None) -> dict[str, str]:
    return {"path": path, "section": section, "group": group, "title": title or ""}


def github_file_url(path: str) -> str:
    encoded_path = quote(path, safe="/")
    kind = "tree" if (ROOT / path).is_dir() else "blob"
    return f"{GITHUB_REPOSITORY}/{kind}/{GITHUB_REF}/{encoded_path}"


PAGES = [
    page("README.md", "overview", "Start here", "What is Agent Team?"),
    page("docs/README.md", "overview", "Start here", "Documentation index"),
    page("docs/REPO_HARNESS.md", "harness", "Fundamentals", "Repository harness"),
    page("docs/TOOLS.md", "harness", "Repository controls", "Tools"),
    page("docs/RULES.md", "harness", "Repository controls", "Rules"),
    page("docs/SENSORS.md", "harness", "Repository controls", "Sensors"),
    page("docs/GATES.md", "harness", "Repository controls", "Gates"),
    page("docs/DOCUMENTATION.md", "harness", "Repository controls", "Documentation"),
    page("docs/MCPS.md", "harness", "Repository controls", "MCPs"),
    page("docs/AGENTES.md", "agentes", "Fundamentals", "How agents work"),
    page("docs/agentes/README.md", "agentes", "Fundamentals", "Contract catalog"),
    page("agents/README.md", "agentes", "Executable artifacts", "Operational prompts"),
    page("agents/catalog.md", "agentes", "Executable artifacts", "Materialized catalog"),
    page("agents/meeting-context-agent.md", "agentes", "Supporting materials", "Meeting context agent"),
    page("docs/SKILLS.md", "skills", "Fundamentals", "How skills work"),
    page("skills/README.md", "skills", "Fundamentals", "Skills catalog"),
    page("skills/references/workflow-contract.md", "skills", "Shared contracts", "Artifact contract"),
    page("docs/LOOPS.md", "loops", "Fundamentals", "How loops work"),
    page("docs/loops/README.md", "loops", "Fundamentals", "Loop catalog"),
    page("workflows/README.md", "loops", "Executable workflows", "Workflow map"),
    page("docs/METODOLOGIA.md", "metodologia", "Fundamentals", "Development cycle"),
    page("docs/metodologia/README.md", "metodologia", "Fundamentals", "Methodology pages"),
    page("docs/WORKSPACE.md", "workspace", "Fundamentals", "Where work lives"),
    page("docs/workspace/README.md", "workspace", "Fundamentals", "Workspace pages"),
    page("workspaces/README.md", "workspace", "Reference implementations", "Example workspaces"),
    page("templates/README.md", "workspace", "Templates", "Template catalog"),
    page(
        "workspaces/tech-lead/docs/diagrams/tech-lead-workspace.md",
        "workspace",
        "Infographics and diagrams",
        "Anatomy of the Tech Lead workspace",
    ),
]


def extend(pattern: str, section: str, group: str, excluded: set[str] | None = None) -> None:
    excluded = excluded or set()
    for source in sorted(ROOT.glob(pattern)):
        relative = source.relative_to(ROOT).as_posix()
        if relative not in excluded and all(item["path"] != relative for item in PAGES):
            PAGES.append(page(relative, section, group))


extend("docs/agentes/*.md", "agentes", "Individual contracts", {"docs/agentes/README.md"})
extend("agents/*/AGENT.md", "agentes", "Executable prompts")
extend("skills/*/SKILL.md", "skills", "Executable procedures")
extend("docs/loops/[0-9][0-9]-*.md", "loops", "Journey contracts")
extend("workflows/[0-9][0-9]-*.md", "loops", "Executable workflows")
extend("docs/metodologia/[0-9][0-9]-*.md", "metodologia", "Human operation")
extend("docs/workspace/[0-9][0-9]-*.md", "workspace", "Operating structure")
for role in ("pm", "ux", "tech-lead"):
    PAGES.append(page(f"workspaces/{role}/README.md", "workspace", "Reference implementations"))
    PAGES.append(page(f"workspaces/{role}/WORKSPACE.md", "workspace", "Reference implementations"))
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
            '<div class="mermaid-head"><figcaption>Interactive diagram</figcaption>'
            '<div class="mermaid-tools">'
            '<button type="button" data-zoom="out" aria-label="Zoom out">−</button>'
            '<span data-zoom-label>fitted</span>'
            '<button type="button" data-zoom="in" aria-label="Zoom in">+</button>'
            '<button type="button" data-zoom="fit">fit</button>'
            "</div></div>"
            f'<pre class="mermaid">{html.escape(source)}</pre>'
            '<p class="mermaid-fallback">The visualization uses Mermaid. If you are offline, the source code remains available below.</p>'
            '<details class="mermaid-src"><summary>View diagram source code</summary>'
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
        suffix = f"#{fragment}" if fragment else ""
        return (
            f'href="{html.escape(github_file_url(key) + suffix)}" '
            f'class="external-file" title="Open {html.escape(key)} on GitHub"'
        )

    return re.sub(r'href="([^"]+)"', replace, rendered)


def plain_text(rendered: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", rendered))).strip()


def build() -> None:
    missing = [item["path"] for item in PAGES if not (ROOT / item["path"]).is_file()]
    if missing:
        raise SystemExit("Required documents are missing:\n- " + "\n- ".join(missing))

    path_ids: dict[str, str] = {}
    route_ids: set[str] = set()
    for item in PAGES:
        page_id = slugify(item["path"].removesuffix(".md").replace("/", " "))
        if page_id in route_ids:
            raise SystemExit(f"Duplicate route: {page_id}")
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
            raise SystemExit(f"Empty macro section: {section['id']}")
        sections.append(section)

    payload = json.dumps(
        {"sections": sections, "pages": pages, "buildDate": date.today().isoformat()},
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")

    def render_html(default_lang: str) -> str:
        is_pt = default_lang == "pt"
        return (
            TEMPLATE.replace("/*__DATA__*/", payload)
            .replace("/*__GITHUB_REPOSITORY__*/", GITHUB_REPOSITORY)
            .replace("/*__GITHUB_REF__*/", GITHUB_REF_PT if is_pt else GITHUB_REF)
            .replace("/*__LINKEDIN_PROFILE__*/", LINKEDIN_PROFILE)
            .replace("/*__EMAIL_ADDRESS__*/", EMAIL_ADDRESS)
            .replace("/*__HTML_LANG__*/", "pt-BR" if is_pt else "en")
            .replace(
                "/*__META_DESCRIPTION__*/",
                (
                    "Documentação interativa Agent Team: harness, agentes, skills, loops, metodologia e workspace."
                    if is_pt
                    else "Interactive Agent Team documentation: harness, agents, skills, loops, methodology, and workspace."
                ),
            )
            .replace(
                "/*__PAGE_TITLE__*/",
                "Agent Team — documentação interativa" if is_pt else "Agent Team — interactive documentation",
            )
            .replace("/*__DEFAULT_LANG__*/", default_lang)
            .replace("/*__INITIAL_FLAG__*/", "🇺🇸" if is_pt else "🇧🇷")
            .replace("/*__INITIAL_LANG_CODE__*/", "EN" if is_pt else "PT-BR")
        )

    OUTPUT.write_text(render_html("en"), encoding="utf-8")
    print(f"site generated: {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size // 1024} KB)")
    OUTPUT_PT.write_text(render_html("pt"), encoding="utf-8")
    print(f"site generated: {OUTPUT_PT.relative_to(ROOT)} ({OUTPUT_PT.stat().st_size // 1024} KB)")


TEMPLATE = r'''<!DOCTYPE html>
<html lang="/*__HTML_LANG__*/">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b0f12">
<meta name="description" content="/*__META_DESCRIPTION__*/">
<title>/*__PAGE_TITLE__*/</title>
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
.brand{display:flex;gap:12px;align-items:center;padding:22px 20px 18px;text-decoration:none;border-bottom:1px solid var(--line-soft)}.brand-mark{width:37px;height:37px;border:1px solid rgba(34,211,238,.42);border-radius:9px;background:linear-gradient(145deg,rgba(34,211,238,.18),rgba(34,211,238,.02));display:grid;place-items:center;color:var(--cyan);font:bold 12px var(--mono)}.brand-copy strong{display:block;letter-spacing:-.01em}.brand-copy span{display:block;color:var(--faint);font:10px var(--mono);letter-spacing:.12em;text-transform:uppercase;margin-top:2px}
.search-box{padding:15px 14px 12px;position:relative}.search-box label{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.search-box input{width:100%;border:1px solid var(--line);background:var(--charcoal);color:var(--text);border-radius:10px;padding:10px 36px 10px 12px;font:13px var(--sans);outline:0}.search-box input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px var(--cyan-soft)}.shortcut{position:absolute;right:24px;top:25px;color:var(--faint);font:10px var(--mono);border:1px solid var(--line);border-radius:4px;padding:1px 5px}
.lang-fab{position:fixed;top:1rem;right:1rem;z-index:9999;display:flex;align-items:center;gap:.4rem;padding:.45rem .8rem;border-radius:2rem;background:var(--charcoal);border:1px solid var(--line);color:var(--muted);font:12px/1 var(--mono);cursor:pointer;backdrop-filter:blur(8px);transition:border-color .15s,color .15s;box-shadow:0 2px 12px rgba(0,0,0,.3)}.lang-fab:hover,.lang-fab:focus-visible{border-color:var(--cyan);color:var(--text);outline:0}.lang-flag{font-size:15px;line-height:1}
.nav-scroll{overflow:auto;padding:4px 10px 30px}.nav-label{color:var(--faint);font:10px var(--mono);letter-spacing:.14em;text-transform:uppercase;padding:15px 10px 7px}.nav-link{display:flex;align-items:center;gap:9px;text-decoration:none;color:var(--muted);border:1px solid transparent;border-radius:9px;padding:8px 9px;margin:2px 0;line-height:1.3}.nav-link:hover{color:var(--text);background:rgba(255,255,255,.025)}.nav-link.active{color:var(--cyan);border-color:rgba(34,211,238,.2);background:var(--cyan-soft)}.nav-num{font:10px var(--mono);color:var(--faint);width:21px}.nav-link.active .nav-num{color:var(--cyan)}.nav-divider{height:1px;background:var(--line-soft);margin:12px 10px}.context-group{margin-bottom:7px}.context-group summary{cursor:pointer;color:var(--faint);font:10px var(--mono);letter-spacing:.09em;text-transform:uppercase;padding:8px 10px;list-style:none}.context-group summary::-webkit-details-marker{display:none}.context-group summary::before{content:"+";margin-right:7px;color:var(--cyan)}.context-group[open] summary::before{content:"−"}.context-group .nav-link{font-size:12px;padding:7px 9px 7px 15px}
.link-icon{width:16px;height:16px;display:block;fill:currentColor}.footer-link-icon{width:14px;height:14px;vertical-align:-2px;margin-right:5px}
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
.site-footer{display:flex;justify-content:space-between;gap:20px;align-items:center;border-top:1px solid var(--line-soft);padding:22px clamp(24px,6vw,76px);color:var(--faint);font:10px var(--mono);letter-spacing:.04em}.footer-links{display:flex;gap:16px}.footer-links a{color:var(--muted);text-decoration:none}.footer-links a:hover{color:var(--cyan)}
@media(max-width:1080px){.hero{grid-template-columns:1fr;min-height:auto}.hero-heading{grid-column:auto}.layers-panel{max-width:720px;width:100%;margin:auto}.doc-grid{grid-template-columns:minmax(0,1fr) 200px;gap:36px}}
@media(max-width:900px){.app{display:block}.sidebar{position:fixed;left:0;transform:translateX(-105%);width:min(88vw,320px);transition:transform .2s ease}.sidebar.open{transform:none}.menu-toggle{display:block}.overlay{display:block;position:fixed;inset:0;z-index:40;background:rgba(0,0,0,.6);opacity:0;pointer-events:none;transition:opacity .2s}.overlay.open{opacity:1;pointer-events:auto}.home,.section-view,.doc-page,.search-view{padding-top:82px}.doc-grid{display:block}.toc{position:static;border-left:0;border-top:1px solid var(--line-soft);padding:24px 0 0;margin-top:45px;max-height:none}}
@media(max-width:650px){.home{padding-left:18px;padding-right:18px}.hero h1{font-size:clamp(46px,14vw,62px)}.layers-panel{padding:22px 14px}.layers-head{align-items:start;gap:12px}.layers-head span{line-height:1.4;text-align:right}.layer{grid-template-columns:28px 1fr;gap:8px;min-height:58px;padding:10px 12px}.layer-question{grid-column:2;font-size:10px}.page-grid{grid-template-columns:1fr}.section-view{padding-left:18px;padding-right:18px}.section-hero h1{font-size:55px}.layer-track span{display:none}.doc-page{padding-left:18px;padding-right:18px}.pager{grid-template-columns:1fr}.pager-link:last-child{text-align:left}.result{grid-template-columns:1fr}.result-path{display:none}.site-footer{align-items:flex-start;flex-direction:column;padding-left:18px;padding-right:18px}.footer-links{gap:12px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}.button:hover,.page-card:hover,.layer:hover{transform:none}}
@media print{.sidebar,.menu-toggle,.overlay,.reading-progress,.toc,.pager{display:none!important}.app{display:block}.doc-page{padding:20px}.doc-grid{display:block}.article{max-width:none}.article a{color:inherit}}
</style>
</head>
<body>
<div class="reading-progress" id="reading-progress"></div>
<button class="menu-toggle" id="menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false">☰</button>
<div class="app">
  <aside class="sidebar" id="sidebar">
    <a class="brand" href="#/" aria-label="Agent Team — home">
      <span class="brand-mark">AT</span><span class="brand-copy"><strong>Agent Team</strong><span>operating system</span></span>
    </a>
    <div class="search-box"><label for="global-search">Search documentation</label><input id="global-search" type="search" placeholder="Search concept, agent, skill…" autocomplete="off"><span class="shortcut">/</span></div>
    <nav class="nav-scroll" id="navigation" aria-label="Main navigation"></nav>
  </aside>
  <div class="overlay" id="overlay"></div>
  <main class="main"><div class="view" id="view"></div><footer class="site-footer"><span>Agent Team · interactive documentation</span><span class="footer-links"><a href="/*__GITHUB_REPOSITORY__*/" target="_blank" rel="noreferrer"><svg class="footer-link-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .5a12 12 0 0 0-3.79 23.39c.6.11.82-.26.82-.58v-2.26c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.75.08-.74.08-.74 1.2.08 1.84 1.23 1.84 1.23 1.07 1.84 2.8 1.31 3.49 1 .11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.34-5.47-5.95 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23A11.5 11.5 0 0 1 12 6.8c1.02 0 2.05.14 3.01.41 2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.62-2.81 5.64-5.48 5.94.43.37.81 1.1.81 2.22v3.29c0 .32.22.69.83.57A12 12 0 0 0 12 .5"/></svg>GitHub repository</a><a href="/*__LINKEDIN_PROFILE__*/" target="_blank" rel="noreferrer"><svg class="footer-link-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.44-2.13 2.94v5.67H9.35V8.99h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.26 2.37 4.26 5.46v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM3.56 20.45h3.56V8.99H3.56v11.46zM22.23 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.46c.98 0 1.77-.77 1.77-1.72V1.72C24 .77 23.21 0 22.23 0z"/></svg>LinkedIn</a><a href="mailto:/*__EMAIL_ADDRESS__*/">/*__EMAIL_ADDRESS__*/</a></span></footer></main>
</div>
<button class="lang-fab" id="language-toggle" type="button" aria-label="Switch language"><span class="lang-flag" aria-hidden="true">/*__INITIAL_FLAG__*/</span><span class="lang-code">/*__INITIAL_LANG_CODE__*/</span></button>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
const DATA=/*__DATA__*/;
const SITE_LINKS={repository:"/*__GITHUB_REPOSITORY__*/",ref:"/*__GITHUB_REF__*/",linkedin:"/*__LINKEDIN_PROFILE__*/",email:"/*__EMAIL_ADDRESS__*/"};
const ICONS={github:'<svg class="link-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .5a12 12 0 0 0-3.79 23.39c.6.11.82-.26.82-.58v-2.26c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.75.08-.74.08-.74 1.2.08 1.84 1.23 1.84 1.23 1.07 1.84 2.8 1.31 3.49 1 .11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.34-5.47-5.95 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23A11.5 11.5 0 0 1 12 6.8c1.02 0 2.05.14 3.01.41 2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.62-2.81 5.64-5.48 5.94.43.37.81 1.1.81 2.22v3.29c0 .32.22.69.83.57A12 12 0 0 0 12 .5"/></svg>',linkedin:'<svg class="link-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.44-2.13 2.94v5.67H9.35V8.99h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.26 2.37 4.26 5.46v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM3.56 20.45h3.56V8.99H3.56v11.46zM22.23 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.46C23.21 24 24 .77 24 1.72v20.56C24 23.23 23.21 24 22.23 24z"/></svg>'};
const view=document.querySelector('#view'),nav=document.querySelector('#navigation');
const searchInput=document.querySelector('#global-search'),sidebar=document.querySelector('#sidebar');
const menuToggle=document.querySelector('#menu-toggle'),overlay=document.querySelector('#overlay');
const progress=document.querySelector('#reading-progress');
const languageToggle=document.querySelector('#language-toggle');
const pagesById=new Map(DATA.pages.map(page=>[page.id,page]));
const sectionsById=new Map(DATA.sections.map(section=>[section.id,section]));
let activePage=null;
let language='/*__DEFAULT_LANG__*/';
const PT_TEXT=JSON.parse(new TextDecoder().decode(Uint8Array.from(atob('eyJvcGVyYXRpbmcgc3lzdGVtIjoic2lzdGVtYSBvcGVyYWNpb25hbCIsIk9wZW4gbmF2aWdhdGlvbiI6IkFicmlyIG5hdmVnYcOnw6NvIiwiQWdlbnQgVGVhbSDigJQgaG9tZSI6IkFnZW50IFRlYW0g4oCUIGluw61jaW8iLCJTZWFyY2ggZG9jdW1lbnRhdGlvbiI6IkJ1c2NhciBuYSBkb2N1bWVudGHDp8OjbyIsIlNlYXJjaCBjb25jZXB0LCBhZ2VudCwgc2tpbGzigKYiOiJCdXNjYXIgY29uY2VpdG8sIGFnZW50ZSwgc2tpbGzigKYiLCJNYWluIG5hdmlnYXRpb24iOiJOYXZlZ2HDp8OjbyBwcmluY2lwYWwiLCJJbiB0aGlzIGxheWVyIjoiTmVzdGEgY2FtYWRhIiwiRXhwbG9yZSI6IkV4cGxvcmFyIiwiT3ZlcnZpZXciOiJWaXPDo28gZ2VyYWwiLCJUaGUgc2l4IGxheWVycyI6IkFzIHNlaXMgY2FtYWRhcyIsIkxheWVyICI6IkNhbWFkYSAiLCJPcGVyYXRpb25hbCBkb2N1bWVudGF0aW9uIjoiRG9jdW1lbnRhw6fDo28gb3BlcmFjaW9uYWwiLCJBIHN5c3RlbSBmb3IgdGVhbXMgdGhhdCAiOiJVbSBzaXN0ZW1hIHBhcmEgdGltZXMgcXVlICIsImxlYWQgYWdlbnRzLiI6ImRpcmlnZW0gYWdlbnRlcy4iLCJBZ2VudCBUZWFtIHR1cm5zIGludGVudCwgY29udGV4dCwgYW5kIHZlcmlmaWNhdGlvbiBpbnRvIGFuIG9wZXJhYmxlIGRldmVsb3BtZW50IGN5Y2xlLiBFeHBsb3JlIGZyb20gdGhlIHRlY2huaWNhbCBmb3VuZGF0aW9uIHRvIHRoZSBwbGFjZSB3aGVyZSBldmVyeSBkZWNpc2lvbiBsZWF2ZXMgYSB0cmFjZS4iOiJPIEFnZW50IFRlYW0gdHJhbnNmb3JtYSBpbnRlbsOnw6NvLCBjb250ZXh0byBlIHZlcmlmaWNhw6fDo28gZW0gdW0gY2ljbG8gZGUgZGVzZW52b2x2aW1lbnRvIG9wZXLDoXZlbC4gRXhwbG9yZSBkYSBmdW5kYcOnw6NvIHTDqWNuaWNhIGFvIGx1Z2FyIG9uZGUgY2FkYSBkZWNpc8OjbyBkZWl4YSByYXN0cm8uIiwiU3RhcnQgZnJvbSB0aGUgZm91bmRhdGlvbiI6IkNvbWXDp2FyIHBlbGEgYmFzZSIsIlZpZXcgdGhlIGNvbXBsZXRlIGluZGV4IjoiVmVyIMOtbmRpY2UgY29tcGxldG8iLCJPcGVyYXRpbmcgbGF5ZXJzIjoiQ2FtYWRhcyBvcGVyYWNpb25haXMiLCJjbGljayB0byBleHBsb3JlIjoiY2xpcXVlIHBhcmEgZXhwbG9yYXIiLCJmb3VuZGF0aW9uIjoiZnVuZGHDp8OjbyIsIm9wZXJhdGlvbiI6Im9wZXJhw6fDo28iLCJQb3NpdGlvbiBpbiB0aGUgbGF5ZXJzIjoiUG9zacOnw6NvIG5hcyBjYW1hZGFzIiwib3BlbiDihpciOiJhYnJpciDihpciLCJIT01FIjoiSU7DjUNJTyIsIkxBWUVSICI6IkNBTUFEQSAiLCJvcGVyYXRpbmcgbGF5ZXIiOiJjYW1hZGEgb3BlcmFjaW9uYWwiLCJSZXR1cm4gdG8gdGhlIG1hcCI6IlZvbHRhciBhbyBtYXBhIiwiVmlldyBhbGwgc3Vic2VjdGlvbnMiOiJWZXIgdG9kYXMgYXMgc3Vic2XDp8O1ZXMiLCJJbiB0aGlzIGRvY3VtZW50IjoiTmVzdGUgZG9jdW1lbnRvIiwidXBkYXRlZCAiOiJhdHVhbGl6YWRvICIsIkFkamFjZW50IGRvY3VtZW50cyI6IkRvY3VtZW50b3MgYWRqYWNlbnRlcyIsIuKGkCBwcmV2aW91cyI6IuKGkCBhbnRlcmlvciIsIm5leHQg4oaSIjoicHLDs3hpbW8g4oaSIiwiRW50ZXIgYSBjb25jZXB0LCBhZ2VudCwgc2tpbGwsIGFydGlmYWN0LCBvciBqb3VybmV5IHN0YWdlLiI6IkRpZ2l0ZSB1bSBjb25jZWl0bywgYWdlbnRlLCBza2lsbCwgYXJ0ZWZhdG8gb3UgZXRhcGEgZGEgam9ybmFkYS4iLCJObyBkb2N1bWVudHMgZm91bmQuIFRyeSBhIGJyb2FkZXIgdGVybS4iOiJOZW5odW0gZG9jdW1lbnRvIGVuY29udHJhZG8uIFRlbnRlIHVtIHRlcm1vIG1haXMgYW1wbG8uIiwiR2xvYmFsIHNlYXJjaCI6IkJ1c2NhIGdsb2JhbCIsIlJlc3VsdHMgZm9yICI6IlJlc3VsdGFkb3MgcGFyYSAiLCJFeHBsb3JlIHRoZSBjb2xsZWN0aW9uIjoiRXhwbG9yZSBvIGFjZXJ2byIsIlNlYXJjaCBkb2N1bWVudCB0aXRsZXMsIHBhdGhzLCBhbmQgY29udGVudC4iOiJQZXNxdWlzZSBwb3IgdMOtdHVsb3MsIGNhbWluaG9zIGUgY29udGXDumRvIGRhIGRvY3VtZW50YcOnw6NvLiIsIlNlYXJjaCI6IkJ1c2NhIiwiVGhpcyByb3V0ZSBkb2VzIG5vdCBleGlzdC4iOiJFc3RhIHJvdGEgbsOjbyBleGlzdGUuIiwiVGhlIGRvY3VtZW50YXRpb24gbWF5IGhhdmUgbW92ZWQuIFJldHVybiB0byB0aGUgbWFpbiBtYXAgdG8gY29udGludWUuIjoiQSBkb2N1bWVudGF0aW9uIG1heSBoYXZlIG1vdmVkLiBSZXR1cm4gdG8gdGhlIG1haW4gbWFwIHRvIGNvbnRpbnVlLiIsIlJldHVybiBob21lIjoiVm9sdGFyIGFvIGluw61jaW8iLCJOb3QgZm91bmQg4oCUIEFnZW50IFRlYW0iOiJOw6NvIGVuY29udHJhZG8g4oCUIEFnZW50IFRlYW0iLCJJbnRlcmFjdGl2ZSBkaWFncmFtIjoiRGlhZ3JhbWEgaW50ZXJhdGl2byIsIlpvb20gb3V0IjoiUmVkdXppciBkaWFncmFtYSIsImZpdHRlZCI6ImFqdXN0YWRvIiwiWm9vbSBpbiI6IkFtcGxpYXIgZGlhZ3JhbWEiLCJmaXQiOiJhanVzdGFyIiwiVGhlIHZpc3VhbGl6YXRpb24gdXNlcyBNZXJtYWlkLiBJZiB5b3UgYXJlIG9mZmxpbmUsIHRoZSBzb3VyY2UgY29kZSByZW1haW5zIGF2YWlsYWJsZSBiZWxvdy4iOiJBIHZpc3VhbGl6YcOnw6NvIHVzYSBNZXJtYWlkLiBTZSBlc3RpdmVyIG9mZmxpbmUsIG8gY8OzZGlnby1mb250ZSBwZXJtYW5lY2UgZGlzcG9uw612ZWwgYWJhaXhvLiIsIlZpZXcgZGlhZ3JhbSBzb3VyY2UgY29kZSI6IlZlciBjw7NkaWdvIGRvIGRpYWdyYW1hIiwiT3BlbiAiOiJBYnJpciAiLCJBZ2VudCBUZWFtIOKAlCBpbnRlcmFjdGl2ZSBkb2N1bWVudGF0aW9uIjoiQWdlbnQgVGVhbSDigJQgZG9jdW1lbnRhw6fDo28gaW50ZXJhdGl2YSJ9'),char=>char.charCodeAt(0))));
Object.assign(PT_TEXT,JSON.parse(new TextDecoder().decode(Uint8Array.from(atob('eyJBZ2VudCBUZWFtIHR1cm5zIGludGVudCwgY29udGV4dCwgYW5kIHZlcmlmaWNhdGlvbiBpbnRvIGFuIG9wZXJhYmxlIGRldmVsb3BtZW50IGN5Y2xlLiAiOiJPIEFnZW50IFRlYW0gdHJhbnNmb3JtYSBpbnRlbsOnw6NvLCBjb250ZXh0byBlIHZlcmlmaWNhw6fDo28gZW0gdW0gY2ljbG8gZGUgZGVzZW52b2x2aW1lbnRvIG9wZXLDoXZlbC4gIiwiRXhwbG9yZSBmcm9tIHRoZSB0ZWNobmljYWwgZm91bmRhdGlvbiB0byB0aGUgcGxhY2Ugd2hlcmUgZXZlcnkgZGVjaXNpb24gbGVhdmVzIGEgdHJhY2UuIjoiRXhwbG9yZSBkYSBmdW5kYcOnw6NvIHTDqWNuaWNhIGFvIGx1Z2FyIG9uZGUgY2FkYSBkZWNpc8OjbyBkZWl4YSByYXN0cm8uIiwiU3dpdGNoIGxhbmd1YWdlIHRvIEVuZ2xpc2giOiJNdWRhciBpZGlvbWEgcGFyYSBpbmdsw6pzIiwiU3dpdGNoIGxhbmd1YWdlIHRvIEJyYXppbGlhbiBQb3J0dWd1ZXNlIjoiTXVkYXIgaWRpb21hIHBhcmEgcG9ydHVndcOqcyBicmFzaWxlaXJvIn0='),char=>char.charCodeAt(0)))));
const esc=value=>String(value??'').replace(/[&<>"]/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[char]));
function localize(){
  const pairs=(language==='pt'?[...Object.entries(PT_TEXT)]:Object.entries(PT_TEXT).map(([en,pt])=>[pt,en])).sort((a,b)=>b[0].length-a[0].length);
  const replace=value=>pairs.reduce((text,[from,to])=>text.split(from).join(to),value);
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
  const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
  nodes.forEach(node=>{node.nodeValue=replace(node.nodeValue)});
  document.querySelectorAll('[aria-label],[placeholder],[title]').forEach(node=>{for(const name of ['aria-label','placeholder','title'])if(node.hasAttribute(name))node.setAttribute(name,replace(node.getAttribute(name)))});
  const heroLede=document.querySelector('.hero-lede');
  if(heroLede){const englishLede='Agent Team turns intent, context, and verification into an operable development cycle. Explore from the technical foundation to the place where every decision leaves a trace.';heroLede.textContent=language==='pt'?PT_TEXT[englishLede]:englishLede}
  document.documentElement.lang=language==='pt'?'pt-BR':'en';
  languageToggle.querySelector('.lang-flag').textContent=language==='pt'?'🇺🇸':'🇧🇷';
  languageToggle.querySelector('.lang-code').textContent=language==='pt'?'EN':'PT-BR';
  languageToggle.setAttribute('aria-label',replace(language==='pt'?'Switch language to English':'Switch language to Brazilian Portuguese'));
}
const routeFor=page=>page.section==='overview'?`#/documento/${page.id}`:`#/secao/${page.section}/${page.id}`;
const sectionRoute=section=>`#/secao/${section.id}`;
const repositoryFileUrl=path=>`${SITE_LINKS.repository}/blob/${SITE_LINKS.ref}/${path.split('/').map(encodeURIComponent).join('/')}`;
function closeMenu(){sidebar.classList.remove('open');overlay.classList.remove('open');menuToggle.setAttribute('aria-expanded','false')}
function groupsFor(sectionId){const groups=new Map();DATA.pages.filter(p=>p.section===sectionId).forEach(page=>{if(!groups.has(page.group))groups.set(page.group,[]);groups.get(page.group).push(page)});return groups}
function renderNav(sectionId='',pageId=''){
  const layers=DATA.sections.map(section=>`<a class="nav-link ${section.id===sectionId?'active':''}" href="${sectionRoute(section)}"><span class="nav-num">${section.number}</span><span>${esc(section.title)}</span></a>`).join('');
  let context='';
  if(sectionsById.has(sectionId)){
    context='<div class="nav-divider"></div><div class="nav-label">In this layer</div>';
    for(const [group,pages] of groupsFor(sectionId)) context+=`<details class="context-group" open><summary>${esc(group)}</summary>${pages.map(page=>`<a class="nav-link ${page.id===pageId?'active':''}" href="${routeFor(page)}">${esc(page.title)}</a>`).join('')}</details>`;
  }
  nav.innerHTML=`<div class="nav-label">Explore</div><a class="nav-link ${!sectionId?'active':''}" href="#/"><span class="nav-num">00</span><span>Overview</span></a><div class="nav-label">The six layers</div>${layers}${context}<div class="nav-label">Links</div><a class="nav-link" href="${SITE_LINKS.repository}" target="_blank" rel="noreferrer"><span class="nav-num">${ICONS.github}</span><span>GitHub repository</span></a><a class="nav-link" href="${SITE_LINKS.linkedin}" target="_blank" rel="noreferrer"><span class="nav-num">${ICONS.linkedin}</span><span>LinkedIn</span></a><a class="nav-link" href="mailto:${SITE_LINKS.email}"><span class="nav-num">@</span><span>${SITE_LINKS.email}</span></a>`;
}
function homeMarkup(){
  const layers=DATA.sections.map(section=>`<a class="layer" href="${sectionRoute(section)}" aria-label="Layer ${section.number}, ${esc(section.title)}: ${esc(section.question)}"><span class="layer-number">${section.number}</span><span class="layer-title">${esc(section.title)}</span><span class="layer-question">${esc(section.question)}</span></a>`).join('');
  return `<section class="home"><div class="hero"><div class="hero-heading"><div class="eyebrow">Operational documentation</div><h1>A system for teams that <span>lead agents.</span></h1></div><div class="hero-copy"><p class="hero-lede">Agent Team turns intent, context, and verification into an operable development cycle. Explore from the technical foundation to the place where every decision leaves a trace.</p><div class="hero-actions"><a class="button primary" href="${sectionRoute(DATA.sections[0])}">Start from the foundation <span class="arrow">→</span></a><a class="button" href="${routeFor(DATA.pages[1])}">View the complete index</a></div></div><div class="layers-panel"><div class="layers-head"><strong>Operating layers</strong><span>click to explore</span></div><div class="layers">${layers}</div><div class="layers-base"><span>foundation</span><span>operation</span></div></div></div></section>`;
}
function renderHome(){activePage=null;view.innerHTML=homeMarkup();renderNav();document.title='Agent Team — interactive documentation';progress.style.width='0';window.scrollTo(0,0);renderDiagrams()}
function trackMarkup(active){return `<div class="layer-track" aria-label="Position in the layers">${DATA.sections.map(s=>`<a class="track-item ${s.id===active?'active':''}" href="${sectionRoute(s)}" aria-label="${esc(s.title)}"><span>${esc(s.title)}</span></a>`).join('')}</div>`}
function renderSection(section){
  activePage=null;let blocks='';
  for(const [group,pages] of groupsFor(section.id)) blocks+=`<section class="group-block"><div class="group-head"><h2>${esc(group)}</h2></div><div class="page-grid">${pages.map(page=>`<a class="page-card" href="${routeFor(page)}"><span class="card-action">open ↗</span><strong class="card-title">${esc(page.title)}</strong><p class="card-excerpt">${esc(page.excerpt)}</p><span class="card-path">${esc(page.path)}</span></a>`).join('')}</div></section>`;
  view.innerHTML=`<section class="section-view"><div class="breadcrumbs"><a href="#/">HOME</a><span>/</span><span>LAYER ${section.number}</span></div><header class="section-hero"><div class="section-index">operating layer</div><h1>${esc(section.title)}</h1><p class="section-question">${esc(section.question)}</p><p class="section-summary">${esc(section.summary)}</p></header>${trackMarkup(section.id)}${blocks}</section>`;
  renderNav(section.id);document.title=`${section.title} — Agent Team`;progress.style.width='0';window.scrollTo(0,0);closeMenu();
}
function tocMarkup(page){if(!page.toc.length)return page.section==='overview'?'<div class="toc-title">Overview</div><a href="#/">Return to the map</a>':`<div class="toc-title">In this layer</div><a href="${sectionRoute(sectionsById.get(page.section))}">View all subsections</a>`;return `<div class="toc-title">In this document</div>${page.toc.map(item=>`<a class="level-${item.level}" href="${routeFor(page)}~${encodeURIComponent(item.anchor)}">${esc(item.text)}</a>`).join('')}`}
function renderDocument(page,anchor=''){
  activePage=page;const siblings=DATA.pages.filter(item=>item.section===page.section);const index=siblings.findIndex(item=>item.id===page.id),previous=siblings[index-1],next=siblings[index+1];const section=sectionsById.get(page.section),sectionTitle=section?.title||'Overview',sectionHref=section?sectionRoute(section):'#/';
  const badge=page.status?`<span class="badge ${esc(page.status)}">${esc(page.status)}</span>`:'';
  const updated=page.updated?`<span class="badge">updated ${esc(page.updated)}</span>`:'';
  view.innerHTML=`<section class="doc-page"><div class="breadcrumbs"><a href="#/">HOME</a><span>/</span><a href="${sectionHref}">${esc(sectionTitle)}</a><span>/</span><span>${esc(page.group)}</span></div><div class="doc-grid"><article class="article"><div class="doc-meta">${badge}${updated}<a class="source-path" href="${repositoryFileUrl(page.path)}" target="_blank" rel="noreferrer" title="Open ${esc(page.path)} on GitHub">${esc(page.path)}</a></div>${page.html}<nav class="pager" aria-label="Adjacent documents">${previous?`<a class="pager-link" href="${routeFor(previous)}"><span>← previous</span><strong>${esc(previous.title)}</strong></a>`:'<span class="pager-spacer"></span>'}${next?`<a class="pager-link" href="${routeFor(next)}"><span>next →</span><strong>${esc(next.title)}</strong></a>`:'<span class="pager-spacer"></span>'}</nav></article><aside class="toc">${tocMarkup(page)}</aside></div></section>`;
  renderNav(section?page.section:'',page.id);document.title=`${page.title} — Agent Team`;closeMenu();renderDiagrams();
  requestAnimationFrame(()=>{if(anchor){const target=document.getElementById(`${page.id}~${decodeURIComponent(anchor)}`);if(target)target.scrollIntoView()}else window.scrollTo(0,0);updateProgress()});
}
function score(page,term){let value=0;if(page.title.toLowerCase().includes(term))value+=12;if(page.group.toLowerCase().includes(term))value+=6;if(page.path.toLowerCase().includes(term))value+=5;if(page.text.includes(term))value+=2;return value}
function renderSearch(term){
  activePage=null;const query=term.trim().toLowerCase();let content='';
  if(!query)content='<div class="empty-state">Enter a concept, agent, skill, artifact, or journey stage.</div>';
  else{const results=DATA.pages.map(page=>({page,score:score(page,query)})).filter(item=>item.score).sort((a,b)=>b.score-a.score||a.page.title.localeCompare(b.page.title)).slice(0,40);content=results.length?`<div class="result-list">${results.map(({page})=>`<a class="result" href="${routeFor(page)}"><span class="result-section">${esc(sectionsById.get(page.section)?.title||'Overview')}</span><span><strong>${esc(page.title)}</strong><p>${esc(page.excerpt)}</p></span><span class="result-path">${esc(page.path)}</span></a>`).join('')}</div>`:'<div class="empty-state">No documents found. Try a broader term.</div>'}
  view.innerHTML=`<section class="search-view"><div class="eyebrow">Global search</div><h1>${query?`Results for “${esc(term)}”`:'Explore the collection'}</h1><p class="search-intro">Search document titles, paths, and content.</p>${content}</section>`;renderNav();document.title=`Search${term?` — ${term}`:''} — Agent Team`;progress.style.width='0';window.scrollTo(0,0);
}
function renderNotFound(){view.innerHTML='<section class="not-found"><strong>404</strong><h1>This route does not exist.</h1><p>The documentation may have moved. Return to the main map to continue.</p><a class="button primary" href="#/">Return home</a></section>';renderNav();document.title='Not found — Agent Team';progress.style.width='0'}
function parseRoute(){const raw=location.hash.slice(1)||'/';const split=raw.indexOf('~'),path=split>=0?raw.slice(0,split):raw,anchor=split>=0?raw.slice(split+1):'';return {path,anchor}}
function route(){const {path,anchor}=parseRoute();if(path==='/'){renderHome();return}if(path.startsWith('/busca')){const query=new URLSearchParams(path.split('?')[1]||'').get('q')||'';searchInput.value=query;renderSearch(query);return}const parts=path.split('/').filter(Boolean);if(parts[0]==='documento'){const page=pagesById.get(parts[1]);if(page?.section==='overview'){renderDocument(page,anchor);return}}if(parts[0]==='secao'&&sectionsById.has(parts[1])){const section=sectionsById.get(parts[1]);if(parts.length===2){renderSection(section);return}const page=pagesById.get(parts[2]);if(page&&page.section===section.id){renderDocument(page,anchor);return}}renderNotFound()}
async function renderDiagrams(){const wraps=[...document.querySelectorAll('.mermaid-wrap')];if(!wraps.length)return;if(!window.mermaid)return;try{const nodes=wraps.map(wrap=>wrap.querySelector('.mermaid'));await mermaid.run({nodes});wraps.forEach(wrap=>wrap.classList.add('rendered'))}catch(error){console.warn('Mermaid unavailable',error)}}
function applyZoom(wrap,scale){const svg=wrap.querySelector('.mermaid svg');if(!svg)return;wrap.dataset.scale=String(scale);svg.style.maxWidth='none';svg.style.width=`${scale*100}%`;wrap.querySelector('[data-zoom-label]').textContent=scale===1?'fitted':`${Math.round(scale*100)}%`}
document.addEventListener('click',event=>{const button=event.target.closest('[data-zoom]');if(button){const wrap=button.closest('.mermaid-wrap');let scale=Number(wrap.dataset.scale||1);if(button.dataset.zoom==='in')scale=Math.min(2.5,scale+.25);if(button.dataset.zoom==='out')scale=Math.max(.5,scale-.25);if(button.dataset.zoom==='fit')scale=1;applyZoom(wrap,scale)}if(event.target.closest('a')&&innerWidth<=900)closeMenu()});
function updateProgress(){if(!activePage){progress.style.width='0';return}const height=document.documentElement.scrollHeight-innerHeight;const value=height>0?Math.min(100,scrollY/height*100):0;progress.style.width=`${value}%`}
searchInput.addEventListener('input',event=>{const term=event.target.value;history.replaceState(null,'',`#/busca?q=${encodeURIComponent(term)}`);renderSearch(term);localize()});
searchInput.addEventListener('keydown',event=>{if(event.key==='Enter')location.hash=`/busca?q=${encodeURIComponent(searchInput.value)}`});
menuToggle.addEventListener('click',()=>{const open=sidebar.classList.toggle('open');overlay.classList.toggle('open',open);menuToggle.setAttribute('aria-expanded',String(open))});overlay.addEventListener('click',closeMenu);
languageToggle.addEventListener('click',()=>{language=language==='en'?'pt':'en';route();localize()});
document.addEventListener('keydown',event=>{if(event.key==='/'&&!/input|textarea/i.test(document.activeElement.tagName)){event.preventDefault();searchInput.focus()}if(event.key==='Escape'){closeMenu();if(document.activeElement===searchInput){searchInput.value='';searchInput.blur();location.hash='/'}}});
window.addEventListener('hashchange',()=>{route();localize()});window.addEventListener('scroll',updateProgress,{passive:true});window.addEventListener('load',renderDiagrams);
if(window.mermaid)mermaid.initialize({startOnLoad:false,theme:'dark',securityLevel:'loose',themeVariables:{background:'#161c21',primaryColor:'#20282e',primaryTextColor:'#e8f0f3',primaryBorderColor:'#22d3ee',lineColor:'#60727d',secondaryColor:'#10161a',tertiaryColor:'#263139'}});
route();localize();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    build()
