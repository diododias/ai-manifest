# Translation

This repository publishes its documentation in **English (`en`)** and **Brazilian Portuguese (`pt-BR`)** from a single branch. This page is the contract for how that works.

## The model: one branch, one directory per locale

Documentation used to live one language per branch. That does not work: branches diverge structurally, `git merge` cannot merge a translation, and every restructure on one side silently orphans the other. The English tree gained `kb-store/` while the Portuguese branch still had `docs/` — the two stopped being the same documentation.

The model here is the one used by Docusaurus, Astro Starlight and the Kubernetes docs: **the canonical tree at the repository root is the source language, and every other locale mirrors the same paths under `i18n/<locale>/`.**

```
README.md                      canonical (en)
docs/TOOLS.md                  canonical (en)
i18n/pt-BR/README.md           translation of README.md
i18n/pt-BR/docs/TOOLS.md       translation of docs/TOOLS.md
i18n/pt-BR/_manifest.json      which canonical version each translation was made from
i18n/ui.json                   interface strings and section metadata, per locale
i18n/GLOSSARY.md               terminology that must stay consistent
```

The path after `i18n/<locale>/` is always identical to the canonical path. Nothing else needs to be configured: the mirror *is* the mapping.

The source language is declared once, in `SOURCE_LOCALE` in `scripts/i18n.py` and `scripts/build-docs-site.py`. Changing which language is canonical is a one-line change plus a directory rename.

## Fallback: a missing translation is visible, never invisible

The site builds one file per locale — `index.html` and `index.pt.html`. When a page has no translation, the locale falls back to the canonical text and renders a banner at the top of that page saying so. A reader is never silently served the wrong language, and a gap never blocks a release.

## Drift: measured, not discovered by the reader

The real failure mode of bilingual docs is not the missing file, it is the translation that stayed behind while the original changed. `_manifest.json` records the SHA-256 of the canonical file **at the moment it was translated**. Comparing that stamp against the canonical file today gives each page one of four states:

| State | Meaning |
|---|---|
| `current` | translation matches the canonical version it was stamped from |
| `outdated` | the canonical file changed after the translation was written |
| `missing` | no translation file exists; the page falls back to the source language |
| `orphan` | a translation exists for a document that is no longer published |

```bash
uv run scripts/i18n.py status              # full report per file
uv run scripts/i18n.py status --summary    # counts only
uv run scripts/i18n.py status --porcelain  # one line per file, for tooling
```

The hash ignores line-ending and trailing-whitespace noise, so reformatting does not mark a page stale.

## The workflow

**Changing a document.** Edit the canonical file normally. Do not block on the translation — `status` will report the page as `outdated` and the site keeps publishing it.

**Translating.** Edit the mirrored file under `i18n/<locale>/`, then record which canonical version you translated:

```bash
uv run scripts/i18n.py stamp docs/TOOLS.md
```

Stamping is a claim that the translation reflects the canonical file as it is right now. Stamping without translating is the one thing that breaks this system, because it makes drift invisible again.

**Adding a page.** Add it to `PAGES` in `scripts/build-docs-site.py`. It is published immediately in every locale, falling back where it is not translated yet.

**Changing an interface string.** Edit `i18n/ui.json` for every locale. The build fails if a locale is missing a key — interface strings are never silently falling back.

**Adding a locale.** Create `i18n/<locale>/`, add a block to `i18n/ui.json` with the same keys, and add an entry to `LOCALES` in `scripts/build-docs-site.py` and to `TARGET_LOCALES` in `scripts/i18n.py`.

## Translation rules

1. **Terminology comes from [`GLOSSARY.md`](GLOSSARY.md).** Terms in the do-not-translate list stay in English in every language — they are the vocabulary of the method, not prose.
2. **Structure is mirrored, not reinvented.** Same headings, same order, same tables, same code blocks. The site derives navigation and the table of contents from headings, and a page that reorders them stops matching its counterpart.
3. **Anchors are localized.** A link to `RULES.md#the-testing-strategy-as-a-rule` becomes the slug of the *translated* heading. Slugs keep accents (`#a-estratégia-de-testes-como-rule`).
4. **Relative links stay canonical.** Write `docs/TOOLS.md`, not `i18n/pt-BR/docs/TOOLS.md`. The build resolves each link to the right locale.
5. **Front matter is translated too** — `title`, `description` and `summary` are rendered.
6. **Code, commands, paths and identifiers are never translated.** Only the prose around them.

## Sensor, not gate

`i18n.py status` is a **sensor**: it reports and exits 0. Translation drift is information the author needs, not a reason to block a commit that is otherwise correct — holding an English fix hostage to its translation is how documentation stops being updated at all. Pass `--strict` to make it exit non-zero where a pipeline genuinely wants that.

## Importing translations that live elsewhere

`adopt` imports translated text from another git ref, which is how the Portuguese branch was folded into this structure:

```bash
uv run scripts/i18n.py adopt --from main --source-ref 16f3664 \
  --rename workspaces/tech-lead/docs=workspaces/tech-lead/kb-store
```

`--from` is the ref holding the translated text, `--source-ref` is the canonical version that text was translated from (it becomes the stamp), and `--rename` maps path prefixes that moved since. Files whose text on the ref is identical to the current canonical text are not translations and are left as `missing`.
