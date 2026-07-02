# Telaris documentation

Canonical home for all Telaris documentation that ships as a PDF. One repo, one build pattern, seven public documents in four languages (English, Spanish, Portuguese, French) plus the internal brand book.

## Documents

The five public-facing documents each ship as four sibling PDFs (`<slug>.pdf`, `<slug>-es.pdf`, `<slug>-pt.pdf`, `<slug>-fr.pdf`). The Spanish, Portuguese, and French versions are not transliterations of the English: per the Telaris voice canon, the four languages carry the same observations in their own register, and the English is not the master.

| Slug | Audience | Status |
|---|---|---|
| `manifest` / `-es` / `-pt` / `-fr` | Anyone reading the project from outside. | **Draft** (2026-05-21; FR added 2026-05-22). Positioning statement, six principles plus citations. No TOC. Four locales. Published at <https://www.telaris.ca/docs/manifest.pdf>, `manifest-es.pdf`, `manifest-pt.pdf`, `manifest-fr.pdf`. |
| `editor-quick-start` / `-es` / `-pt` / `-fr` | New editors who need to add content right now. | **v0.1** (2026-05-21; FR added 2026-05-22). Five-step walkthrough, ~6 pages, 3 reused screenshots, no TOC (`show_toc: false`). Companion to `editor-manual`. Four locales. |
| `editor-manual` / `-es` / `-pt` / `-fr` | Editors authoring galaxies, wormholes, keywords. | **v0.3** (2026-07-01; covers Telaris v6.12.28). 15 chapters, ~80 pages, per-locale screenshots from the synthetic `[manual-demo]` galaxy including the templates trio. Strictly editor-side scope: no infra terminology, no admin / federation topics. Four locales. |
| `hotglue-manual` / `-es` / `-pt` / `-fr` | Editors composing freeform Hotglue media pages. | **v0.2** (2026-07-01; covers v6.12.28). 8 chapters, ~28 pages, screenshots from a `[manual-demo] Masterworks` galaxy. Companion to `editor-manual`. Four locales. |
| `admin-manual` / `-es` / `-pt` / `-fr` | The person running a Telaris instance. | **v0.1** (2026-07-01; covers v6.12.28). 10 chapters, ~32 pages, mirrors the Admin Console tabs (Users, self-service enrolment, editor access, galaxies/clusters, global settings, federation, backups, maintenance). Operator-facing; no cryptographic internals. Six console screenshots captured against a disposable synthetic instance. Four locales. |
| `privacy` / `-es` / `-pt` / `-fr` | Public-facing privacy notice. | **Draft** (2026-05-21; FR added 2026-05-22). Conservative draft naming the no-AI-training posture, no platform-pattern collection, withdrawal of consent, federation behaviour. Marked draft pending finalisation. Four locales. |
| `tos` / `-es` / `-pt` / `-fr` | Public-facing terms of use. | **Draft** (2026-05-21; FR added 2026-05-22). Conservative draft naming how the site is offered, software is offered, withdrawal, limitations of liability. Marked draft pending finalisation. Four locales. |
| `brand-book` | Visual identity, voice, palette. | v1 active; built by a transitional freestanding script at `tools/build_brand_book.py`. Internal-facing, not localized. Markdown decomposition into the shared `src/brand-book/` pipeline still pending. |

### Localization conventions

- **One slug per language**, not nested locales: `editor-manual`, `editor-manual-es`, `editor-manual-pt`, `editor-manual-fr` are independent source directories under `src/`. Each builds with its own `python3 build.py <slug>` invocation. Languages can drift in sibling phrasing without lockstep updates.
- **UI labels (buttons, menu paths, field names) appear in the locale of the screenshot** since the application itself is now localized in all four languages (as of the localization sweep that closed 2026-05-22). Screenshots are captured per-locale via `python3 tools/capture_editor_screenshots.py --locale {en,es,pt,fr}` (editor + hotglue surfaces) and `python3 tools/capture_admin_screenshots.py --locale {en,es,pt,fr}` (admin console, run against a disposable synthetic instance, never a live one); outputs land under `assets/images/<slug>{,-es,-pt,-fr}/`.
- **Vocabulary mapping** (UI-side only): Galaxy / Galaxia / Galáxia / Galaxie, Wormhole / Agujero de Gusano / Buraco de Minhoca / Trou de Ver, Portal / Portal / Portal / Portail, Keyword canvas / Lienzo de palabras clave / Tela de palavras-chave / Toile de mots-clés. Code identifiers stay on the internal vocabulary (`constellation`, `node`, `portal`). See the brand book's *Naming* note for the full table.
- **House style across all languages**: no em-dashes, no exclamation marks, sentence-case headings. **Gender-neutral, MUST**: verb-first, role-as-account (`cuenta de administración` / `conta de administração` / `compte d'administration`), relational phrasing (`quien opera la instancia` / `quem opera a instância` / `qui exploite l'instance`); no agent nouns where avoidable. French specifics: Canadian-French leanings where there's a clean choice (courriel, fichier, téléversement); no median-dot inclusive writing (`éditeur·rice` is out).

## Build pattern

Markdown source under `src/<slug>/` is rendered through a Jinja template into HTML, which WeasyPrint turns into a PDF. The pipeline is one script (`build.py`) and one shared CSS layer (`styles/`); per-document overrides live in `styles/<slug>.css`.

```
documentation/
├── build.py                              # python3 build.py <slug>
├── requirements.txt
├── styles/
│   ├── base.css                          # Brand variables, typography, page chrome, callouts.
│   ├── manual.css                        # doc_class = manual (editor + admin).
│   └── brand-book.css                    # doc_class = brand-book.
├── templates/
│   └── document.html.jinja               # One template; CSS class differentiates the look.
├── src/
│   ├── editor-manual/                    # 15 chapters (v0.3), + -es/-pt/-fr siblings.
│   │   ├── meta.yaml
│   │   └── NN-section-slug.md
│   ├── hotglue-manual/                   # 8 chapters (v0.2), + -es/-pt/-fr siblings.
│   ├── admin-manual/                     # 10 chapters (v0.1), + -es/-pt/-fr siblings.
│   └── brand-book/                       # Placeholder; pending migration.
├── assets/
│   ├── images/<slug>{,-es,-pt,-fr}/      # Per-locale screenshots (editor, hotglue, admin).
│   └── generated/                        # Build-time generated SVGs (for brand book).
├── tools/
│   ├── build_brand_book.py               # Transitional brand-book builder.
│   ├── seed_demo_content.php             # Seeds the [manual-demo] galaxies on starmaps.
│   ├── seed_hotglue_demo.php             # Seeds the [manual-demo] Masterworks hotglue galaxy.
│   ├── capture_editor_screenshots.py     # Playwright capture (editor + templates).
│   ├── capture_hotglue_screenshots.py    # Playwright capture (hotglue surfaces).
│   └── capture_admin_screenshots.py      # Playwright capture (admin console; throwaway instance).
└── dist/                                 # PDF output (gitignored).
```

## Build

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
python3 build.py editor-manual
```

PDF lands at `dist/editor-manual.pdf`.

### Optional vault / Syncthing mirror

Every document supports an optional mirror to a secondary location after the canonical write to `dist/`. Set `TELARIS_<SLUG_UPPER>_MIRROR` in your environment (hyphens in the slug become underscores). If the env var is unset, or the parent directory of the target does not exist, the mirror step is silently skipped. Example shell rc:

```
export TELARIS_EDITOR_QUICK_START_MIRROR="$HOME/notes/User Manuals/Editor Quick Start/Editor Quick Start.pdf"
export TELARIS_EDITOR_MANUAL_MIRROR="$HOME/notes/User Manuals/Editor Manual/Editor Manual.pdf"
export TELARIS_ADMIN_MANUAL_MIRROR="$HOME/notes/User Manuals/Admin Manual/Admin Manual.pdf"
export TELARIS_BRAND_BOOK_MIRROR="$HOME/notes/Brand book/Brand book.pdf"
```

The mirror is enforced by `build.py` for the shared pipeline and by `tools/build_brand_book.py` for the brand book (same env-var convention).

### Optional Pluriverse-website auto-publish

Setting `TELARIS_WWW_DOCS_DIR` to a writable directory makes every build also copy its PDF into that directory after the canonical `dist/` write. Used to keep `www.telaris.ca/docs/` (or any other web-served documentation directory) in sync without a deploy step. Skipped silently if unset or the directory does not exist. Example:

```
export TELARIS_WWW_DOCS_DIR="/var/www/www.telaris.ca/docs/"
```

When set, `python3 build.py editor-manual` writes `dist/editor-manual.pdf` and copies the same file to `${TELARIS_WWW_DOCS_DIR}/editor-manual.pdf`. The brand-book builder follows the same convention and publishes its output as `brand-book.pdf` in the target directory.

On the host this repo is developed on, the Pluriverse website's `docs/` directory is `/var/www/www.telaris.ca/docs/`, served directly by nginx; the `telaris_website` repo gitignores its contents (the PDFs are generated artefacts whose source lives here).

### Brand book (transitional)

The brand book is not yet on the shared `build.py <slug>` pipeline. Until the markdown decomposition lands, build it via the freestanding script:

```
python3 tools/build_brand_book.py
```

PDF lands at `dist/brand-book.pdf` (and at the mirror location if `TELARIS_BRAND_BOOK_MIRROR` is set).

## Screenshot pipeline (editor manual)

The editor manual references screenshots captured from a synthetic demo galaxy on the dev Telaris instance (`starmaps.polivoxia.ca`). Two tools support this end-to-end:

**`tools/seed_demo_content.php`** populates the dev instance with two `[manual-demo]` galaxies (`Coastal plants`, `Tide pools`) plus thirteen wormholes carrying neutral synthetic content (plants, tide-pool animals), seeds keyword-canvas relations and chip positions, and creates a sandboxed editor-only account `manual-capture-editor@telaris.local` assigned only to the demo galaxies. The seed is idempotent: rerunning detects existing rows and reuses them.

```sh
php tools/seed_demo_content.php
```

The script prints the editor credentials on first run; copy them into `~/.telaris-capture-credentials` (0600, outside any repo) in the form:

```sh
export TELARIS_EDITOR_URL="https://starmaps.polivoxia.ca"
export TELARIS_EDITOR_USERNAME="manual-capture-editor@telaris.local"
export TELARIS_EDITOR_PASSWORD='...'
```

**`tools/capture_editor_screenshots.py`** drives Playwright + headless Chromium against starmaps as the sandboxed editor. One `Shot` definition per surface; each shot has an optional `prepare` callable that opens a modal, switches a tab, or scrolls a section. Captures land in `assets/images/editor-manual/`.

```sh
set -a; source ~/.telaris-capture-credentials; set +a
python3 tools/capture_editor_screenshots.py
```

The sandboxed editor account is the privacy floor of this pipeline: every dropdown, sidebar, and chrome element in every screenshot only ever reveals the two demo galaxies. Real user content never appears.

If the dev UI changes, re-run the capture script and the manual rebuild picks up the new images automatically; if the change is structural (a new surface to document), add a new `Shot` to the script, capture, and reference the resulting filename from the markdown.

## Conventions

- Source is Markdown (CommonMark + GFM tables + footnotes). Wikilink syntax from Obsidian is not used here; documents are self-contained.
- One section per file, prefixed with a two-digit order (`01-introduction.md`, `02-galaxies.md`, ...).
- Section headings start at `# Section title` inside each file; the build script promotes / demotes as needed.
- Images live in `assets/images/<slug>/`. Reference them with paths **relative to the repo root**: `![Alt](assets/images/<slug>/file.png)`. WeasyPrint's `base_url` is the repo root, not the markdown file's directory.
- Page breaks: `<div class="page-break"></div>` between major sections; otherwise WeasyPrint handles them.
- Callouts use `> [!note] ... > [!warning] ... > [!tip] ... ` syntax; the build script translates to styled blocks.
- No em-dashes anywhere (project-wide rule); use colons, semicolons, parentheses, or restructure.
- Canadian English throughout English documents.
