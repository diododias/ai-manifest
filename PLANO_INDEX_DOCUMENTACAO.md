---
id: PLAN-001
project: ai-manifest
status: implemented
owner: tech-lead
work_items: []
updated_at: 2026-08-09
---

# Immersive Agent Team documentation at `index.html`

## Expected result

Make a static, navigable and responsive `index.html` available at the root of the repository that presents the current Agent Team documentation in a dark, immersive and discovery-oriented experience. The home page must highlight the project’s macrosections and an interactive pyramid; Selecting a layer should open its section page, reveal related subsections, and maintain a hash-navigable URL.

HTML will be a presentation layer generated from existing Markdown. The documents in the repository continue to be the source of truth, avoiding divergences between visual documentation and versioned documentation.

## Context and starting point

- The current document reorganization defines six pillars, from base to top: **Harness, Agents, Skills, Loops, Methodology and Workspace**.
- The root already has `scripts/build-docs-site.py`, which converts Markdown into a single page, preserves Mermaid diagrams, rewrites links and offers search.
- The current generator points to old paths and issues `docs/site.html`; it must be evolved, not replaced by a new stack.
- The repository does not have a web application or dedicated hosting infrastructure. The first increment will be static, without framework, backend, authentication or persistence.
- There is a broad reorganization underway in the work tree. The implementation must preserve these changes and be based on the new document structure.

## Scope of the first increment

### Included

- Generate `index.html` in the root of the repository.
- Dark theme as the main identity, using charcoal gray and cyan.
- Editorial home with Agent Team proposal, entry points and interactive pyramid.
- Drilldown navigation: macrosection → subsections → document.
- Routes by hash, deep link and support for browser back/forward buttons.
- Global search by title, path and text of included documents.
- Local summary of the document and highlighting of the active section.
- Rendering of Markdown, tables, code and Mermaid diagrams.
- Responsive layout for desktop, tablet and cell phone.
- Full keyboard navigation, visible focus, semantics and reduced movement mode.
- Visual spaces prepared for new infographics without requiring navigation restructuring.

### Outside the scope of this increment

- CMS, content editing through the interface, login or persistent data.
- Publication on a hosting provider.
- Editorial rewriting of all Markdown documents.
- Production of final infographics in addition to the pyramid; Only components and slots prepared to receive them enter.
- Multiple HTML files or an application with server routing.
- Clear theme or theme selector.

## Information architecture

The home will not just be an index. It will function as a mental map of the system: the pyramid explains the dependence between the layers, while the quick access cards serve those who already know what they are looking for.

| Level | Macrosecation | Question answered | Initial Drilldown |
|---:|---|---|---|
| 6, top | **Workspace** | Where do the work and artifacts live? | overview, structure, ownership, workspace harness, board and Work Items |
| 5 | **Methodology** | How do people operate the system? | roles, checkpoints, triggers, rhythms, manual, journey and documentation |
| 4 | **Loops** | In what order do agents collaborate and when do they stop? | overview, 12 journey loops, failure paths and executable workflows |
| 3 | **Skills** | As a recurring and correctly executed task? | overview, catalogue, artifact contract and 22 executable procedures |
| 2 | **Agents** | Who executes, with what authority and limits? | overview, catalog groups, 23 contracts and operational prompts |
| 1, base | **Harness** | What makes a repository operable by agents? | overview, tools, rules, sensors, gates, documentation and MCPs |

### Transversal content

- **Skills** have their own layer and also appear as related resources in the steps in which they are executed.
- **Workflows** appear in the Loops drilldown, distinguishing concept (`docs/loops/`) from executable contract (`workflows/`).
- **Templates and workspace examples** appear as related resources within the corresponding sections.
- **Overview** remains its own route and return point for the pyramid.

## Navigation model

### Proposed routes

The site will use hash routing to work both via double click and static hosting:

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

### Behaviors

1. When opening the website, the home page displays the pyramid, a short explanation of the model and quick access.
2. Hovering, focusing, or tapping a level highlights the layer and shows its central question and relationship to adjacent levels.
3. Click or `Enter` updates the route, performs a short transition and opens the macrosection page.
4. The section page features a striking header, summary, subsection map, and recommended reading track.
5. Clicking on a subsection opens the document in the same shell, keeping the breadcrumb, contextual menu and summary local.
6. Back/forward restores route, selection, page title and reading position when applicable.
7. On small screens, the side navigation becomes a drawer; the pyramid remains playable without relying on hover.

## Visual direction

### Base palette

| Token | Proposed color | Usage |
|---|---|---|
| `--bg-deep` | `#0B0F12` | main background |
| `--bg-charcoal` | `#161C21` | panels and navigation |
| `--bg-elevated` | `#20282E` | cards, code and raised surfaces |
| `--line` | `#31404A` | borders and separators |
| `--cyan` | `#22D3EE` | action, focus and level selected |
| `--cyan-strong` | `#06B6D4` | contrast and active states |
| `--text` | `#E8F0F3` | main text |
| `--text-muted` | `#93A4AE` | secondary text |

### Visual language

- Lead gray background with very subtle technical grid, controlled cyan halos and layered surfaces.
- Highly readable editorial typography, with broad titles and technical numbering in macrosections.
- Thin edges, cyan glow only in focus/active state and enough contrast for long reading.
- Transitions between 160 and 280 ms; No animations impede reading or browsing.
- Macrosection cards with clear hierarchy, short summary and explicit action, without quantitative indicators.
- Future infographics share color tokens, typography, caption, zoom controls, and responsive behavior.

## Interactive layers

The layers will be built with semantic HTML and CSS, without fixed images, to preserve responsiveness, accessibility and interactive states.

Each layer will be a real `button`/link with:

- layer name and number;
- accessible description;
- normal, hover, focus, active and visited status;
- minimum touch area of ​​44 px;
- visual relationship with the previous and next layers;
- direct destination for the macrosection route;
- keyboard and screen reader support.

On the desktop, the title occupies the top of the first viewport and the layers are next to the project manifest. On mobile, they are reorganized vertically without losing the reading of the base for the operation. With `prefers-reduced-motion`, movements are removed, keeping only instantaneous contrast changes.

## Technical strategy

### Source and generation

- Keep Markdown as the canonical source.
- Update the generator page manifest for the current paths.
- Change the output from `docs/site.html` to `index.html` at the root.
- Model each input with `id`, `macrosection`, `group`, `title`, `order`, `route`, `file`, `status` and `related`.
- Embed the converted content and search index in HTML, allowing local use without a server.
- Preserve link rewriting, heading ids, tables, code blocks and Mermaid.
- Display build warning for missing document or duplicate route; A missing mandatory macrosection must fail generation.

### Application shell

- `header`: brand, global search and return to home.
- `nav`: macrosections and context of the active section.
- `main`: home, section page, document page or results.
- `aside` contextual: subsections and local summary, collapsible on smaller screens.
- `footer`: previous/next page and corresponding Markdown font.

### Status in browser

JavaScript will be small and without a framework. The hash will be the source of truth for navigation; ephemeral state will be limited to search, drawer, diagram zoom and scroll restoration. No user data will be persisted.

## Implementation steps

### 1. Inventory and content contract

- [x] Reconcile all generator paths with the current document structure.
- [x] Define the explicit order of macrosections, groups, subsections and documents.
- [x] Resolve conceptual duplications between `docs/loops/` and `workflows/` by label and context, without deleting content.
- [x] Define which operational artifacts are fully included and which appear only as related resources.
- [x] Validate ids, titles, front matter, internal links and mandatory documents.

**Verifiable output:** content manifest without obsolete paths, duplicate ids or empty macrosections.

### 2. Evolution of the generator

- [x] Refactor `scripts/build-docs-site.py` to emit `index.html` in the root.
- [x] Separate navigation data, converted content and visual template within the generator.
- [x] Implement hash routes and Markdown link resolution for internal routes.
- [x] Preserve readable fallback for Mermaid when visual rendering is not available.
- [x] Produce clear errors for missing mandatory references.

**Verifiable output:** a command reproduces the same `index.html` from current Markdown.

### 3. Home and visual system

- [x] Implement lead/cyan tokens and responsive shell.
- [x] Build editorial hero, quick access and collection indicators.
- [x] Build the interactive pyramid with the six canonical levels.
- [x] Implement focus, selection, touch and reduced movement states.
- [x] Reserve reusable components for later infographics.

**Verifiable output:** home communicates the model in a viewport and allows access to any macrosection by mouse, touch or keyboard.

### 4. Drilldown and reading

- [x] Implement macrosection page with summary, subsection map and recommended trail.
- [x] Implement document page with breadcrumb, local summary and previous/next.
- [x] Synchronize route, title, active state and browser history.
- [x] Integrate global search and empty/no result states.
- [x] Treat external links, links to files not included and deep anchors.

**Verifiable output:** sharing a route directly opens the same document and navigation context.

### 5. Infographics and diagrams

- [x] Apply the same visual container to Mermaid and future infographics.
- [x] Preserve zoom, adjust width, caption and access to textual content.
- [x] Create a demonstrative infographic slot on the home page without inventing new content.
- [x] Check that the pyramid remains functional without animation or effects JavaScript.

**Verifiable output:** existing diagrams are readable and new infographics can be added via manifest/component.

### 6. Validation and delivery

- [x] Generate HTML twice and confirm deterministic output, except explicitly defined date metadata.
- [x] Check all routes, internal links, related files and anchors.
- [ ] Test at widths of 360, 768, 1024 and 1440 px.
- [ ] Test keyboard, focus, basic screen reader, contrast and `prefers-reduced-motion`.
- [ ] Confirm search, deep link, back/forward, refresh and opening via `file://`.
- [ ] Validate the absence of errors in the console and behavior when Mermaid is unavailable.
- [x] Update `README.md` with access to `index.html` and the regeneration command.

**Verifiable output:** acceptance criteria met and HTML reproducible from repository sources.

## Acceptance criteria

- [x] There is a working `index.html` in the root of the repository.
- [x] The first screen highlights the Agent Team, the six macrosections and the interactive pyramid.
- [x] The interface uses a dark theme with a predominance of charcoal gray and cyan.
- [x] Each level of the pyramid leads to its section page and displays related subsections.
- [x] Each macrosection can also be accessed without using the pyramid.
- [x] A subsection can be opened directly by URL and remains correct after refresh.
- [x] Back and forth of the browser reflect the navigation carried out on the website.
- [x] Search, local summary, breadcrumbs and previous/next work without reloading the page.
- [x] The content displayed is generated from the current Markdown, without parallel editorial copy.
- [x] Tables, code, links and Mermaid have readable presentation in the dark theme.
- [x] Every essential action works via mouse, touch and keyboard, with visible focus.
- [ ] The layout does not produce undue horizontal scrolling at target widths.
- [x] The movement respects `prefers-reduced-motion`.
- [x] The generator fails or explicitly alerts for duplicate routes and missing mandatory content.
- [x] The generation is reproducible and does not alter the source documents.

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Current generator references removed documents | missing sections and broken links | take inventory before redesign and validate the manifest at build |
| Duplicity between conceptual and executable documentation | reader does not understand which source to follow | label type and source, group related and maintain canonical hierarchy |
| Visual immersion harms long reading | tiring or inaccessible documentation | limit brightness/motion, preserve reading width and test contrast |
| Layers only depend on shape/hover | mobile, keyboard or screen reader failure | use semantic controls, visible text and alternatives via cards/menu |
| Unique HTML grow with the entire collection | slow loading and searching | keep index compact, avoid heavy assets and measure size/time in build |
| Mermaid depend on external resource | diagrams unavailable offline | keep textual font accessible and fallback readable |
| Documentary changes continue during implementation | manifesto quickly become obsolete | centralize order/metadata and make absence/duplicity detectable by the generator |

## Decisions made for this plan

- `index.html` will be a root-generated artifact, not a manually maintained file.
- The experience will be a static SPA in a single HTML, with hash routing.
- The pyramid will have six levels, according to `docs/README.md`; Skills have their own layer and transversal connections.
- The initial theme will be exclusively dark.
- The website must work locally without a server; hosting can be handled on later demand.
- Implementation begins only after approval of this plan.

## Files planned for implementation

| Archive | Expected change |
|---|---|
| `scripts/build-docs-site.py` | update sources, information model, template, router, search and generation destination |
| `index.html` | generated static artifact |
| `README.md` | add site access and regeneration instruction |

New application files, repositories or projects are not required for this increment.
