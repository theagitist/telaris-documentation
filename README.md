# Telaris documentation

Canonical home for all Telaris documentation that ships as a PDF. One repo, one build pattern, three (and growing) documents.

## Documents

| Slug | Audience | Status |
|---|---|---|
| `editor-manual` | Editors authoring galaxies, wormholes, keywords. | In progress (2026-05-21). |
| `admin-manual` | Telaris-instance operators (federation, keys, backups). | Queued. |
| `brand-book` | Visual identity, voice, palette. | Queued for migration from `~/apps/telaris/original_assets/brand/build_brand_book_pdf.py`. |

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

## Conventions

- Source is Markdown (CommonMark + GFM tables + footnotes). Wikilink syntax from Obsidian is not used here; documents are self-contained.
- One section per file, prefixed with a two-digit order (`01-introduction.md`, `02-galaxies.md`, ...).
- Section headings start at `# Section title` inside each file; the build script promotes / demotes as needed.
- Images live in `assets/images/<slug>/`. Reference as `![Alt](../../assets/images/<slug>/file.png)`.
- Page breaks: `<div class="page-break"></div>` between major sections; otherwise WeasyPrint handles them.
- Callouts use `> [!note] ... > [!warning] ... > [!tip] ... ` syntax; the build script translates to styled blocks.
- No em-dashes anywhere (project-wide rule); use colons, semicolons, parentheses, or restructure.
- Canadian English throughout English documents.
