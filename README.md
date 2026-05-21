# Telaris documentation

Canonical home for all Telaris documentation that ships as a PDF. One repo, one build pattern, three (and growing) documents.

## Documents

| Slug | Audience | Status |
|---|---|---|
| `editor-manual` | Editors authoring galaxies, wormholes, keywords. | In progress (2026-05-21). |
| `admin-manual` | Telaris-instance operators (federation, keys, backups). | Queued. |
| `brand-book` | Visual identity, voice, palette. | Built by a transitional freestanding script at `tools/build_brand_book.py`. Source content lives in the maintainer's working notes (the brand book sibling notes: Palette, Type, Voice and tone, Naming, Taglines, Iconography, Screenshots). Migration into the shared `src/brand-book/` markdown pipeline is still pending. |

## Build pattern

Markdown source under `src/<slug>/` is rendered through a Jinja template into HTML, which WeasyPrint turns into a PDF. The pipeline is one script (`build.py`) and one shared CSS layer (`styles/`); per-document overrides live in `styles/<slug>.css`.

```
documentation/
├── build.py                   # python3 build.py <slug>
├── requirements.txt
├── styles/
│   ├── base.css               # Brand variables, typography, page chrome.
│   ├── manual.css             # Manual-class styling (editor + admin).
│   └── brand-book.css         # Brand-book-class styling.
├── templates/
│   └── document.html.jinja    # One template; CSS class differentiates the look.
├── src/
│   ├── editor-manual/
│   │   ├── meta.yaml          # Title, subtitle, version, doc_class, sections order.
│   │   └── NN-section-slug.md # Markdown sections, ordered by filename prefix.
│   ├── admin-manual/
│   └── brand-book/
├── assets/
│   ├── images/                # Screenshots, diagrams (committed).
│   └── generated/             # Build-time generated SVGs (committed; reproducible).
├── tools/                     # Generators (e.g., starfield SVG for brand book).
└── dist/                      # PDF output (gitignored).
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
export TELARIS_EDITOR_MANUAL_MIRROR="$HOME/notes/User Manuals/Editor Manual/Editor Manual.pdf"
export TELARIS_ADMIN_MANUAL_MIRROR="$HOME/notes/User Manuals/Admin Manual/Admin Manual.pdf"
export TELARIS_BRAND_BOOK_MIRROR="$HOME/notes/Brand book/Brand book.pdf"
```

The mirror is enforced by `build.py` for the shared pipeline and by `tools/build_brand_book.py` for the brand book (same env-var convention).

### Brand book (transitional)

The brand book is not yet on the shared `build.py <slug>` pipeline. Until the markdown decomposition lands, build it via the freestanding script:

```
python3 tools/build_brand_book.py
```

PDF lands at `dist/brand-book.pdf` (and at the mirror location if `TELARIS_BRAND_BOOK_MIRROR` is set).

## Conventions

- Source is Markdown (CommonMark + GFM tables + footnotes). Wikilink syntax from Obsidian is not used here; documents are self-contained.
- One section per file, prefixed with a two-digit order (`01-introduction.md`, `02-galaxies.md`, ...).
- Section headings start at `# Section title` inside each file; the build script promotes / demotes as needed.
- Images live in `assets/images/<slug>/`. Reference them with paths **relative to the repo root**: `![Alt](assets/images/<slug>/file.png)`. WeasyPrint's `base_url` is the repo root, not the markdown file's directory.
- Page breaks: `<div class="page-break"></div>` between major sections; otherwise WeasyPrint handles them.
- Callouts use `> [!note] ... > [!warning] ... > [!tip] ... ` syntax; the build script translates to styled blocks.
- No em-dashes anywhere (project-wide rule); use colons, semicolons, parentheses, or restructure.
- Canadian English throughout English documents.
