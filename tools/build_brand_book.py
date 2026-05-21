#!/usr/bin/env python3
"""Build the Telaris brand book PDF from canonical colours, fonts, and motifs.

The PDF embodies the brand rather than describing it: dark cosmic ground,
monospace stack, mint accent and halos, pastel constellation palette as
actual swatches, real scanline overlays, real HUD chrome, the Telaris wordmark
as a centrepiece. Designed so a reader with no prior Telaris knowledge can
absorb the brand from the document alone.

This script is the **transitional builder** for the brand book PDF. It lives
under `tools/` in the `telaris-documentation` repo as a standalone freestanding
script; it does not yet use the shared `build.py <slug>` pipeline (markdown
sections + meta.yaml + Jinja template) that drives the other documents in this
repo. Full migration to that pipeline is queued as a follow-up: the brand book
will be decomposed into `src/brand-book/NN-*.md` plus visual-artefact
generators under `tools/` (starfield SVG, node-network SVG, swatch grids,
theme cards), at which point this monolithic script gets retired.

Output:
    dist/brand-book.pdf        Canonical build artefact (repo-relative).

Optional mirror:
    If the environment variable TELARIS_BRAND_BOOK_MIRROR is set to a target
    file path AND that path's parent directory already exists, the PDF is
    copied there after the canonical write. Intended for operators who want
    the PDF distributed alongside their working notes. If unset or the
    parent does not exist, the mirror step is silently skipped.

Build:
    python3 tools/build_brand_book.py        # from the repo root
"""

from __future__ import annotations

import os
import random
from pathlib import Path

from weasyprint import HTML

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = REPO_ROOT / "dist" / "brand-book.pdf"

# Optional mirror: set TELARIS_BRAND_BOOK_MIRROR in the operator's environment
# to a target file path (e.g. a vault location synced by Syncthing). When unset
# or when the parent directory does not exist, mirroring is skipped silently.
_mirror_env = os.environ.get("TELARIS_BRAND_BOOK_MIRROR")
MIRROR_PATH = Path(_mirror_env).expanduser() if _mirror_env else None

# ---------------------------------------------------------------------------
# Canonical brand colours (mirror the vault note at Brand book/Palette.md).
# ---------------------------------------------------------------------------

VOID = "#000000"
AURORA = "#e8eef0"
AURORA_60 = "rgba(232,238,240,0.6)"
AURORA_28 = "rgba(232,238,240,0.28)"
AURORA_18 = "rgba(232,238,240,0.18)"
MINT = "#00ffcc"
MINT_18 = "rgba(0,255,204,0.18)"
MINT_30 = "rgba(0,255,204,0.30)"
MINT_40 = "rgba(0,255,204,0.40)"
MINT_85 = "rgba(0,255,204,0.85)"

# Seventeen-colour constellation / keyword-chip palette. Source of truth:
# starmaps/js/keyword-chips.js → CHIP_FG.
PASTELS = [
    "#fca5a5", "#fdba74", "#fcd34d", "#fde047", "#bef264", "#86efac",
    "#6ee7b7", "#5eead4", "#67e8f9", "#7dd3fc", "#93c5fd", "#a5b4fc",
    "#c4b5fd", "#d8b4fe", "#f0abfc", "#f9a8d4", "#fda4af",
]

PASTEL_NAMES = [
    "Coral", "Apricot", "Amber", "Sun", "Lime", "Mint",
    "Sea", "Teal", "Sky-cyan", "Sky", "Cornflower", "Iris",
    "Lavender", "Violet", "Orchid", "Rose", "Blush",
]

# Lighter editorial-background pastel array (admin / editor surfaces).
LIGHTER_PASTELS = [
    "#FEF2F2", "#F0FAF0", "#EFF6FF", "#FFF8F0", "#F8F5FF",
    "#F0FDFA", "#FEFEF0", "#FFF5F5", "#F5F5F7", "#F5FAE8",
]


# ---------------------------------------------------------------------------
# SVG generators. Deterministic via seeded RNG so the document is reproducible.
# ---------------------------------------------------------------------------

def starfield_svg(width_mm: float, height_mm: float, count: int, seed: int) -> str:
    """Render a starfield as inline SVG circles in mm space."""
    rng = random.Random(seed)
    parts = []
    for _ in range(count):
        x = rng.uniform(0, width_mm)
        y = rng.uniform(0, height_mm)
        r = rng.uniform(0.10, 0.65)
        a = rng.uniform(0.20, 0.85)
        parts.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" '
            f'fill="rgba(255,255,255,{a:.2f})"/>'
        )
    return "\n".join(parts)


def node_network_svg(
    width_mm: float, height_mm: float, seed: int,
    *, node_count: int = 12,
    x_range: tuple | None = None, y_range: tuple | None = None,
) -> str:
    """Render a small pastel node-network with gradient links.

    Nodes get hand-distributed pastels from the constellation palette; links
    connect each node to its two nearest neighbours and use a linear gradient
    that fades from one node's pastel to the other's, mirroring the canvas
    animation on the Pluriverse landing.

    `x_range` / `y_range` constrain node placement to a sub-region. If `None`,
    nodes fill the canvas with a 25 mm margin.
    """
    rng = random.Random(seed)
    margin = 25.0
    x_lo, x_hi = x_range if x_range else (margin, width_mm - margin)
    y_lo, y_hi = y_range if y_range else (margin, height_mm - margin)
    nodes = []
    for i in range(node_count):
        x = rng.uniform(x_lo, x_hi)
        y = rng.uniform(y_lo, y_hi)
        colour = PASTELS[rng.randrange(len(PASTELS))]
        nodes.append((x, y, colour, i))

    # For each node, find two nearest neighbours.
    edges = set()
    for ax, ay, ac, ai in nodes:
        dists = sorted(
            ((((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5), bi, bx, by, bc)
            for bx, by, bc, bi in nodes if bi != ai
        )
        for _, bi, _bx, _by, _bc in dists[:2]:
            edges.add(tuple(sorted((ai, bi))))

    # Build the SVG.
    defs = []
    link_parts = []
    for ai, bi in edges:
        ax, ay, ac, _ = nodes[ai]
        bx, by, bc, _ = nodes[bi]
        gid = f"g{ai}_{bi}"
        defs.append(
            f'<linearGradient id="{gid}" '
            f'gradientUnits="userSpaceOnUse" '
            f'x1="{ax:.2f}" y1="{ay:.2f}" '
            f'x2="{bx:.2f}" y2="{by:.2f}">'
            f'<stop offset="0" stop-color="{ac}" stop-opacity="0.55"/>'
            f'<stop offset="1" stop-color="{bc}" stop-opacity="0.55"/>'
            f'</linearGradient>'
        )
        link_parts.append(
            f'<line x1="{ax:.2f}" y1="{ay:.2f}" '
            f'x2="{bx:.2f}" y2="{by:.2f}" '
            f'stroke="url(#{gid})" stroke-width="0.35"/>'
        )

    node_parts = []
    for x, y, c, _ in nodes:
        node_parts.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.2" '
            f'fill="{c}" fill-opacity="0.18"/>'
        )
        node_parts.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.9" '
            f'fill="{c}" fill-opacity="0.95"/>'
        )

    return (
        f'<defs>{"".join(defs)}</defs>\n'
        + "\n".join(link_parts)
        + "\n"
        + "\n".join(node_parts)
    )


# ---------------------------------------------------------------------------
# HTML / CSS.
# ---------------------------------------------------------------------------

PAGE_W_MM = 210
PAGE_H_MM = 297

COVER_STARS = starfield_svg(PAGE_W_MM, PAGE_H_MM, count=420, seed=1881)
# Constrain the cover network to the lower portion of the page so it sits
# beneath the text stack as a constellation map, leaving the upper area clear
# for the wordmark, tagline, and description.
COVER_NETWORK = node_network_svg(
    PAGE_W_MM, PAGE_H_MM, seed=8021,
    node_count=14, y_range=(170.0, 270.0),
)
ICONOG_STARS = starfield_svg(80, 60, count=110, seed=44)
ICONOG_NETWORK = node_network_svg(80, 60, seed=77)
SECTION_BAND_STARS = starfield_svg(180, 12, count=80, seed=909)


def pastel_chip(label: str, colour: str) -> str:
    return (
        f'<span class="chip" style="color:{colour};'
        f'text-shadow:0 0 4px {colour}80,0 0 10px {colour}55;">'
        f'#{label}</span>'
    )


def chip_swatch_row() -> str:
    """The seventeen chip pastels, rendered in their actual interaction style."""
    cells = []
    for name, hex_ in zip(PASTEL_NAMES, PASTELS):
        cells.append(
            f'<div class="palette-cell">'
            f'<div class="chip-display" style="color:{hex_};'
            f'text-shadow:0 0 5px {hex_}88,0 0 12px {hex_}55;">#{name.lower()}</div>'
            f'<div class="palette-meta">'
            f'<span class="palette-name">{name}</span>'
            f'<span class="palette-hex">{hex_.upper()}</span>'
            f'</div>'
            f'</div>'
        )
    return "".join(cells)


def lighter_pastel_row() -> str:
    cells = []
    for hex_ in LIGHTER_PASTELS:
        cells.append(
            f'<div class="lighter-cell">'
            f'<div class="lighter-swatch" style="background:{hex_};">'
            f'<span class="lighter-hex">{hex_.upper()}</span>'
            f'</div>'
            f'</div>'
        )
    return "".join(cells)


def chip_bg_row() -> str:
    """The 25 %-alpha background pastels used by editor chips."""
    cells = []
    for hex_ in PASTELS:
        r = int(hex_[1:3], 16)
        g = int(hex_[3:5], 16)
        b = int(hex_[5:7], 16)
        bg = f"rgba({r},{g},{b},0.25)"
        cells.append(
            f'<div class="chipbg-cell">'
            f'<span class="chipbg-pill" style="background:{bg};color:{hex_};'
            f'border:1px solid {hex_}40;">#example</span>'
            f'</div>'
        )
    return "".join(cells)


def voice_card(num: int, title: str, body: str) -> str:
    return (
        f'<div class="voice-card">'
        f'<div class="voice-num">{num:02d}</div>'
        f'<div class="voice-title">{title}</div>'
        f'<div class="voice-body">{body}</div>'
        f'</div>'
    )


def dodont_row(do: str, dont: str) -> str:
    return (
        f'<div class="dodont-row">'
        f'<div class="do-cell"><span class="dodont-tag tag-do">DO</span>'
        f'<div class="dodont-text">{do}</div></div>'
        f'<div class="dont-cell"><span class="dodont-tag tag-dont">DON\'T</span>'
        f'<div class="dodont-text">{dont}</div></div>'
        f'</div>'
    )


def theme_card(name: str, role: str, body: str, accent: str = MINT) -> str:
    return (
        f'<div class="theme-card">'
        f'<div class="theme-head">'
        f'<span class="theme-name">{name}</span>'
        f'<span class="theme-role">{role}</span>'
        f'</div>'
        f'<div class="theme-body">{body}</div>'
        f'</div>'
    )


CSS = f"""
@page {{
    size: A4;
    margin: 18mm 18mm 18mm 18mm;
    background: {VOID};
    @bottom-center {{
        content: counter(page);
        color: {AURORA_28};
        font-family: var(--mono);
        font-size: 7pt;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        margin-bottom: 6mm;
    }}
    @bottom-left {{
        content: "Telaris · Brand book · v1";
        color: {AURORA_28};
        font-family: var(--mono);
        font-size: 7pt;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 6mm;
    }}
    @bottom-right {{
        content: "telaris.ca";
        color: {AURORA_28};
        font-family: var(--mono);
        font-size: 7pt;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 6mm;
    }}
}}

@page cover {{
    size: A4;
    margin: 0;
    background: {VOID};
    @bottom-left {{ content: none; }}
    @bottom-center {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

@page section {{
    size: A4;
    margin: 18mm 18mm 22mm 18mm;
    background: {VOID};
}}

:root {{
    --mono: "Liberation Mono", "DejaVu Sans Mono", "Nimbus Mono PS",
            "Courier New", monospace;
    --void: {VOID};
    --aurora: {AURORA};
    --aurora-60: {AURORA_60};
    --aurora-28: {AURORA_28};
    --mint: {MINT};
}}

* {{ box-sizing: border-box; }}

html, body {{
    margin: 0;
    padding: 0;
    background: {VOID};
    color: {AURORA};
    font-family: var(--mono);
    font-size: 9.5pt;
    line-height: 1.6;
    -weasy-font-feature-settings: "calt" 0;
}}

/* ------------------------------------------------------------- COVER */

.cover {{
    page: cover;
    position: relative;
    width: {PAGE_W_MM}mm;
    height: {PAGE_H_MM}mm;
    background: {VOID};
    overflow: hidden;
    color: {AURORA};
    page-break-after: always;
}}

.cover-svg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}}

.cover-inner {{
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    text-align: center;
    padding: 50mm 22mm 0;
}}

.cover-eyebrow {{
    color: {MINT};
    font-size: 8pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 16mm;
    opacity: 0.75;
}}

.wordmark {{
    font-size: 88pt;
    font-weight: 400;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: {AURORA};
    margin: 0;
    /* Scanline overlay via background-image on the text. */
    background-image: linear-gradient(
        rgba(0,0,0,0.30) 50%,
        rgba(0,0,0,0) 50%
    );
    background-size: 100% 4px;
    /* Mint halo. */
    text-shadow: 0 0 28px {MINT_18}, 0 0 60px {MINT_18};
}}

.cover-tagline {{
    margin-top: 6mm;
    font-size: 12pt;
    letter-spacing: 0.32em;
    color: {AURORA_60};
    text-transform: lowercase;
}}

.cover-rule {{
    width: 80mm;
    height: 1px;
    margin: 18mm 0 12mm 0;
    background: linear-gradient(
        90deg,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.45) 50%,
        rgba(255,255,255,0) 100%
    );
}}

.cover-desc {{
    max-width: 130mm;
    font-size: 10pt;
    line-height: 1.85;
    color: {AURORA_60};
    margin: 0;
}}

.cover-foot {{
    position: absolute;
    bottom: 14mm;
    left: 0; right: 0;
    text-align: center;
    color: {AURORA_28};
    font-size: 7pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
}}

.cover-foot .dot {{
    display: inline-block;
    width: 5px; height: 5px;
    border-radius: 50%;
    background: {MINT};
    vertical-align: middle;
    margin: 0 0.6em;
    box-shadow: 0 0 6px {MINT};
}}

/* ----------------------------------------------------------- SECTION */

.section {{
    page: section;
    page-break-before: always;
    color: {AURORA};
}}

.section-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1px solid {AURORA_18};
    padding-bottom: 4mm;
    margin-bottom: 10mm;
}}

.section-eyebrow {{
    color: {MINT};
    font-size: 7.5pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
}}
.section-eyebrow .dot {{
    display: inline-block;
    width: 5px; height: 5px;
    border-radius: 50%;
    background: {MINT};
    vertical-align: middle;
    margin-right: 0.8em;
    box-shadow: 0 0 6px {MINT};
}}

.section-num {{
    color: {MINT};
    font-size: 28pt;
    letter-spacing: 0.05em;
    opacity: 0.85;
}}

.section h1 {{
    font-size: 26pt;
    font-weight: 400;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: {AURORA};
    margin: 0 0 6mm 0;
}}

.section h2 {{
    font-size: 11pt;
    font-weight: 400;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: {MINT};
    margin: 9mm 0 4mm 0;
}}

.section h2.standalone {{
    margin-top: 0;
}}

.section p, .section li {{
    color: {AURORA_60};
    font-size: 9.5pt;
    line-height: 1.7;
}}

.section p.lead {{
    color: {AURORA};
    font-size: 10.5pt;
    line-height: 1.8;
    margin: 0 0 6mm 0;
}}

.section a {{ color: {MINT}; text-decoration: none; }}

.section strong {{
    color: {AURORA};
    font-weight: 700;
}}

/* ----------------------------------------------------- WHAT IS TELARIS */

.what {{ }}
.what .pull {{
    font-size: 22pt;
    letter-spacing: 0.04em;
    line-height: 1.45;
    color: {AURORA};
    margin: 8mm 0 12mm 0;
    text-transform: none;
}}
.what .pull em {{
    font-style: normal;
    color: {MINT};
    text-shadow: 0 0 6px {MINT_30};
}}
.what .pull-tag {{
    color: {AURORA_60};
    font-size: 12pt;
    letter-spacing: 0.32em;
    text-transform: lowercase;
    margin: 0 0 14mm 0;
}}
.what-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6mm 10mm;
    margin-top: 4mm;
}}
.what-card {{
    border: 1px solid {AURORA_18};
    padding: 5mm 5mm 6mm;
    background: rgba(255,255,255,0.02);
}}
.what-card .what-num {{
    color: {MINT};
    font-size: 8pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 2mm;
}}
.what-card .what-h {{
    color: {AURORA};
    font-size: 11pt;
    letter-spacing: 0.05em;
    margin: 0 0 2mm 0;
}}
.what-card .what-p {{
    color: {AURORA_60};
    font-size: 8.8pt;
    line-height: 1.6;
    margin: 0;
}}

/* ---------------------------------------------------------------- TOC */

.toc ol {{
    list-style: none;
    margin: 0;
    padding: 0;
    counter-reset: tocnum;
}}
.toc li {{
    counter-increment: tocnum;
    padding: 0;
    border-bottom: 1px dotted {AURORA_18};
}}
.toc li a {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    text-decoration: none;
    padding: 3.5mm 0;
}}
.toc li a::before {{
    content: counter(tocnum, decimal-leading-zero);
    color: {MINT};
    font-size: 8.5pt;
    letter-spacing: 0.2em;
    margin-right: 5mm;
    min-width: 14mm;
    display: inline-block;
}}
.toc li a::after {{
    content: "p. " target-counter(attr(href), page);
    color: {AURORA_60};
    font-size: 8.5pt;
    letter-spacing: 0.2em;
}}
.toc .toc-title {{
    flex: 1;
    color: {AURORA};
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-size: 10pt;
}}

/* ----------------------------------------------------------- PALETTE */

.system-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5mm;
    margin: 5mm 0 8mm 0;
}}
.system-card {{
    border: 1px solid {AURORA_18};
    padding: 0;
    overflow: hidden;
}}
.system-swatch {{
    height: 30mm;
    position: relative;
    border-bottom: 1px solid {AURORA_18};
}}
.system-swatch.starfield {{
    background: {VOID};
    overflow: hidden;
}}
.system-swatch.aurora {{ background: {AURORA}; }}
.system-swatch.mint {{
    background: {MINT};
}}
.system-swatch.halo {{
    background: {VOID};
    position: relative;
    text-align: center;
    line-height: 30mm;
}}
.system-swatch.halo .halo-text {{
    color: {AURORA};
    font-size: 16pt;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    text-shadow: 0 0 8px {MINT}, 0 0 18px {MINT}, 0 0 30px {MINT_40};
    line-height: 1;
    display: inline-block;
    vertical-align: middle;
}}
.system-meta {{
    padding: 4mm;
    font-size: 8pt;
    line-height: 1.5;
}}
.system-name {{
    color: {AURORA};
    font-size: 10pt;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    display: block;
    margin-bottom: 1.5mm;
}}
.system-hex {{
    color: {MINT};
    font-size: 8.5pt;
    letter-spacing: 0.1em;
    display: block;
}}
.system-role {{
    color: {AURORA_60};
    font-size: 7.5pt;
    line-height: 1.5;
    margin-top: 2mm;
}}

.palette-grid {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 2.5mm 3mm;
    margin: 4mm 0 6mm 0;
}}
.palette-cell {{
    background: {VOID};
    border: 1px solid {AURORA_18};
    padding: 2.5mm 2mm 2mm;
    text-align: center;
}}
.chip-display {{
    font-size: 8.5pt;
    font-weight: 500;
    letter-spacing: 0.03em;
    margin-bottom: 1.5mm;
    text-align: center;
    line-height: 1.1;
}}
.palette-meta {{
    display: block;
    font-size: 5pt;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    line-height: 1.4;
}}
.palette-name {{ color: {AURORA_60}; display: block; }}
.palette-hex {{ color: {MINT}; display: block; }}

.lighter-grid {{
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: 2mm 2mm;
    margin: 3mm 0 5mm 0;
}}
.lighter-swatch {{
    height: 12mm;
    position: relative;
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    padding: 1mm 1.5mm;
    border-radius: 2px;
}}
.lighter-hex {{
    color: rgba(0,0,0,0.55);
    font-size: 4.5pt;
    letter-spacing: 0.1em;
}}

.chipbg-grid {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 2mm 2.5mm;
    margin: 3mm 0 0 0;
}}
.chipbg-cell {{
    text-align: center;
}}
.chipbg-pill {{
    display: inline-block;
    padding: 1mm 2.5mm;
    border-radius: 9999px;
    font-size: 6.5pt;
    font-weight: 500;
}}

/* ---------------------------------------------------- PALETTE SURFACES */

.surfaces-panel {{
    position: relative;
    margin: 6mm 0;
    height: 60mm;
    background: {VOID};
    overflow: hidden;
    border: 1px solid {AURORA_18};
}}
.surfaces-panel .stars {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}}
.surfaces-panel .panel-stack {{
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
    padding: 0 4mm;
}}
.surfaces-panel .demo-panel {{
    color: {AURORA};
    font-size: 7pt;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 4mm 5mm;
    border-radius: 4px;
    text-align: center;
    line-height: 1.3;
}}
.demo-panel.tier-1 {{
    background: rgba(0,0,0,0.4);
    border: 1px solid {AURORA_18};
}}
.demo-panel.tier-2 {{
    background: rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.2);
}}
.demo-panel.tier-3 {{
    background: rgba(0,0,0,0.7);
    border: 1px solid rgba(255,255,255,0.3);
}}
.demo-panel.tier-4 {{
    background: rgba(10,10,12,0.9);
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 50px -10px rgba(0,255,204,0.3);
}}

.surfaces-legend {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 4mm;
    margin: 3mm 0 6mm 0;
    font-size: 7pt;
    letter-spacing: 0.18em;
    text-transform: uppercase;
}}
.surfaces-legend .leg {{
    text-align: center;
}}
.surfaces-legend .leg-tag {{
    color: {MINT};
    display: block;
    margin-bottom: 1mm;
}}
.surfaces-legend .leg-spec {{
    color: {AURORA_60};
    font-size: 6.5pt;
    letter-spacing: 0.1em;
    text-transform: none;
}}

.radius-row {{
    display: flex;
    align-items: center;
    gap: 8mm;
    margin: 6mm 0 4mm 0;
}}
.radius-demo {{
    width: 18mm; height: 14mm;
    background: rgba(255,255,255,0.06);
    border: 1px solid {AURORA_18};
    display: flex;
    align-items: center;
    justify-content: center;
    color: {MINT};
    font-size: 7pt;
    letter-spacing: 0.2em;
}}
.radius-2 {{ border-radius: 2px; }}
.radius-4 {{ border-radius: 4px; }}
.radius-12 {{ border-radius: 12px; }}
.radius-lg {{ border-radius: 6mm; }}
.radius-pill {{ border-radius: 999px; }}

/* -------------------------------------------------------------- TYPE */

.type-stack {{
    border: 1px solid {AURORA_18};
    padding: 4mm 6mm;
    margin: 3mm 0 4mm 0;
}}
.type-stack-name {{
    color: {MINT};
    font-size: 6.5pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 1.5mm;
}}
.type-stack-value {{
    color: {AURORA};
    font-size: 9pt;
    line-height: 1.5;
}}

.type-spec {{
    margin: 2.5mm 0 3mm 0;
    padding: 2.5mm 0 2.5mm 5mm;
    border-left: 1px solid {AURORA_18};
}}
.type-spec .spec-meta {{
    color: {MINT};
    font-size: 6.5pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 1.5mm;
}}
.type-spec.display {{
    border-left-color: {MINT_40};
}}
.type-spec .spec-sample {{
    color: {AURORA};
}}

.display-sample {{
    font-size: 30pt;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: {AURORA};
    line-height: 1;
    background-image: linear-gradient(
        rgba(0,0,0,0.25) 50%,
        rgba(0,0,0,0) 50%
    );
    background-size: 100% 4px;
    text-shadow: 0 0 18px {MINT_18};
}}
.h2-sample {{
    font-size: 14pt;
    letter-spacing: 0.06em;
    color: {AURORA};
}}
.body-sample {{
    font-size: 9pt;
    line-height: 1.65;
    color: {AURORA_60};
}}
.tagline-sample {{
    font-size: 12pt;
    letter-spacing: 0.32em;
    color: {AURORA_60};
    text-transform: lowercase;
}}
.label-sample {{
    font-size: 7pt;
    letter-spacing: 0.35em;
    color: {MINT};
    text-transform: uppercase;
}}
.micro-sample {{
    font-size: 6pt;
    letter-spacing: 0.25em;
    color: {AURORA_28};
    text-transform: uppercase;
}}

.weight-row {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 5mm;
    margin: 3mm 0 6mm 0;
}}
.weight-cell {{
    border: 1px solid {AURORA_18};
    padding: 4mm 5mm 5mm;
    text-align: center;
}}
.weight-glyph {{
    font-size: 30pt;
    color: {AURORA};
    line-height: 1.1;
    margin-bottom: 1mm;
}}
.weight-w {{
    color: {MINT};
    font-size: 7pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
}}
.weight-role {{
    color: {AURORA_60};
    font-size: 7pt;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 1mm;
}}

.spacing-row {{
    margin: 4mm 0 0 0;
}}
.spacing-cell {{
    padding: 3mm 0;
    border-bottom: 1px dotted {AURORA_18};
}}
.spacing-cell:last-child {{ border-bottom: none; }}
.spacing-tag {{
    color: {MINT};
    font-size: 7pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 1mm;
}}
.spacing-sample {{
    color: {AURORA};
    font-size: 12pt;
    text-transform: uppercase;
}}
.spacing-sample.s06 {{ letter-spacing: 0.06em; }}
.spacing-sample.s18 {{ letter-spacing: 0.18em; }}
.spacing-sample.s32 {{ letter-spacing: 0.32em; }}

/* ------------------------------------------------------------- VOICE */

.voice-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4mm 5mm;
    margin: 4mm 0 0 0;
}}
.voice-card {{
    border: 1px solid {AURORA_18};
    padding: 5mm 5mm 6mm;
    background: rgba(255,255,255,0.02);
}}
.voice-num {{
    color: {MINT};
    font-size: 8pt;
    letter-spacing: 0.4em;
    margin-bottom: 2mm;
}}
.voice-title {{
    color: {AURORA};
    font-size: 10pt;
    letter-spacing: 0.05em;
    line-height: 1.3;
    margin-bottom: 2mm;
    min-height: 10mm;
}}
.voice-body {{
    color: {AURORA_60};
    font-size: 8.2pt;
    line-height: 1.55;
}}

.dodont-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4mm;
    margin: 4mm 0;
    page-break-inside: avoid;
}}
.do-cell, .dont-cell {{
    padding: 4mm;
    border: 1px solid {AURORA_18};
}}
.do-cell {{ border-left: 2px solid {MINT}; }}
.dont-cell {{ border-left: 2px solid #fda4af; opacity: 0.85; }}
.dodont-tag {{
    display: inline-block;
    font-size: 7pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 2mm;
}}
.tag-do {{ color: {MINT}; }}
.tag-dont {{ color: #fda4af; }}
.dodont-text {{
    color: {AURORA};
    font-size: 8.5pt;
    line-height: 1.55;
}}
.dont-cell .dodont-text {{ color: {AURORA_60}; }}

/* ------------------------------------------------------------ NAMING */

.naming-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 3.5mm;
    margin: 3mm 0 4mm 0;
}}
.naming-card {{
    border: 1px solid {AURORA_18};
    padding: 3.5mm 4mm 4mm;
    background: rgba(255,255,255,0.02);
}}
.naming-card .nm-name {{
    color: {AURORA};
    font-size: 12pt;
    letter-spacing: 0.05em;
    margin: 0 0 2mm 0;
    line-height: 1.2;
}}
.naming-card .nm-tag {{
    color: {MINT};
    font-size: 6.5pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 2mm;
}}
.naming-card .nm-body {{
    color: {AURORA_60};
    font-size: 7.5pt;
    line-height: 1.5;
}}

.vocab-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 9pt;
}}
.vocab-table th, .vocab-table td {{
    padding: 3.5mm 4mm;
    text-align: left;
    border-bottom: 1px solid {AURORA_18};
}}
.vocab-table th {{
    color: {MINT};
    font-size: 7pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    font-weight: 400;
    border-bottom: 1px solid {MINT_40};
}}
.vocab-table td {{
    color: {AURORA};
    font-size: 9.5pt;
}}
.vocab-table td.code-col {{
    color: {MINT};
    font-size: 9pt;
}}
.vocab-table td.lang-tag {{
    color: {AURORA_28};
    font-size: 7pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
}}

/* ---------------------------------------------------------- TAGLINE */

.tagline-page {{
    text-align: center;
}}
.tagline-display {{
    font-size: 28pt;
    color: {AURORA};
    text-transform: lowercase;
    margin: 0 0 3mm 0;
    line-height: 1.15;
}}
.tagline-display.spacious {{ letter-spacing: 0.32em; }}
.tagline-loc {{
    color: {MINT};
    font-size: 7pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 2mm;
}}
.tagline-block {{
    margin: 10mm 0;
}}
.tagline-rule {{
    width: 80mm;
    height: 1px;
    margin: 6mm auto;
    background: linear-gradient(
        90deg,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.45) 50%,
        rgba(255,255,255,0) 100%
    );
}}
.tagline-desc {{
    max-width: 130mm;
    margin: 6mm auto 0;
    color: {AURORA_60};
    font-size: 9pt;
    line-height: 1.7;
    text-align: center;
}}

/* ---------------------------------------------------- ICONOGRAPHY */

.icon-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.5mm;
    margin: 2mm 0 0 0;
}}
.icon-card {{
    border: 1px solid {AURORA_18};
    overflow: hidden;
    background: {VOID};
}}
.icon-canvas {{
    position: relative;
    height: 18mm;
    background: {VOID};
    overflow: hidden;
}}
.icon-canvas svg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}}
.icon-meta {{
    padding: 2mm 3mm 2.5mm;
    border-top: 1px solid {AURORA_18};
}}
.icon-name {{
    color: {AURORA};
    font-size: 8.5pt;
    letter-spacing: 0.06em;
    margin-bottom: 0.5mm;
}}
.icon-body {{
    color: {AURORA_60};
    font-size: 6.3pt;
    line-height: 1.4;
}}

/* Halo demonstration. */
.halo-demo {{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}}
.halo-word {{
    color: {AURORA};
    font-size: 16pt;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    text-shadow: 0 0 14px {MINT_18}, 0 0 28px {MINT_18};
    background-image: linear-gradient(
        rgba(0,0,0,0.25) 50%,
        rgba(0,0,0,0) 50%
    );
    background-size: 100% 4px;
}}
.dot-demo {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6mm;
    height: 100%;
}}
.dot-demo .d {{
    width: 6mm; height: 6mm;
    border-radius: 50%;
    box-shadow: 0 0 10px currentColor;
}}
.dot-grid-demo {{
    width: 100%; height: 100%;
    background-color: {VOID};
    background-image: radial-gradient(
        circle, rgba(113,113,122,0.45) 1.1px, transparent 1.5px
    );
    background-size: 6mm 6mm;
}}
.scanline-demo {{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background: {VOID};
}}
.scanline-demo .s {{
    color: {AURORA};
    font-size: 14pt;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 4mm 6mm;
    background-image: linear-gradient(
        rgba(0,0,0,0.4) 50%,
        rgba(0,0,0,0) 50%
    );
    background-size: 100% 3px;
}}
.rule-demo {{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}}
.rule-demo .r {{
    width: 70%;
    height: 1px;
    background: linear-gradient(
        90deg,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.5) 50%,
        rgba(255,255,255,0) 100%
    );
}}
.chip-demo {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 3mm 4mm;
    height: 100%;
    padding: 4mm;
}}
.chip-demo .chip {{
    font-size: 9pt;
    font-weight: 500;
}}
.chip-demo .chip.active {{
    font-weight: 700;
}}
.chip-demo .chip.dim {{
    opacity: 0.25;
}}
.bokeh-demo {{
    position: relative;
    height: 100%;
    background: {VOID};
    overflow: hidden;
}}
.bokeh-demo .blur {{
    position: absolute;
    border-radius: 50%;
    filter: blur(6px);
    opacity: 0.55;
}}
.bokeh-demo .crisp {{
    position: absolute;
    border-radius: 50%;
    opacity: 0.95;
}}

/* ------------------------------------------------------------ THEMES */

.theme-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 5mm;
    margin: 4mm 0 0 0;
}}
.theme-card {{
    border: 1px solid {AURORA_18};
    padding: 0;
    overflow: hidden;
    background: {VOID};
}}
.theme-card .theme-canvas {{
    height: 32mm;
    background: {VOID};
    border-bottom: 1px solid {AURORA_18};
    position: relative;
    overflow: hidden;
}}
.theme-card .theme-meta {{
    padding: 4mm 4mm 5mm;
}}
.theme-card .theme-name {{
    color: {AURORA};
    font-size: 11pt;
    letter-spacing: 0.05em;
    display: inline-block;
    margin-right: 3mm;
}}
.theme-card .theme-role {{
    color: {MINT};
    font-size: 6.5pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
}}
.theme-card .theme-body {{
    color: {AURORA_60};
    font-size: 7.5pt;
    line-height: 1.5;
    margin-top: 2mm;
}}

/* Theme canvas variants. */
.tc-cosmic {{ background: {VOID}; }}
.tc-cosmic .tc-stars circle {{ fill: rgba(255,255,255,0.7); }}
.tc-abstract, .tc-rectangles, .tc-stripes {{
    background: {VOID};
    background-image: linear-gradient({AURORA_18} 1px, transparent 1px),
                      linear-gradient(90deg, {AURORA_18} 1px, transparent 1px);
    background-size: 5mm 5mm;
}}
.tc-simple {{
    background: {VOID};
}}
.tc-tech {{
    background: #000205;
    background-image: linear-gradient(rgba(0,255,204,0.10) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(0,255,204,0.10) 1px, transparent 1px);
    background-size: 6mm 6mm;
}}
.tc-node {{
    position: absolute;
    border-radius: 50%;
}}

/* ----------------------------------------------------------- COLOPHON */

.colophon {{
    padding-top: 10mm;
}}
.colophon .colo-block {{
    margin-bottom: 9mm;
}}
.colophon .colo-h {{
    color: {MINT};
    font-size: 7.5pt;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 3mm;
}}
.colophon .colo-p {{
    color: {AURORA_60};
    font-size: 9pt;
    line-height: 1.7;
    margin: 0 0 1mm 0;
}}
.colophon .colo-code {{
    color: {AURORA};
    font-size: 8.5pt;
}}

/* ----------------------------------------------------- chip generic */

.chip {{
    font-family: var(--mono);
    font-weight: 500;
    font-size: 10pt;
}}
"""


# ---------------------------------------------------------------------------
# Document body.
# ---------------------------------------------------------------------------

def build_html() -> str:
    # ----- Cover -----
    cover = f"""
<section class="cover">
    <svg class="cover-svg" viewBox="0 0 {PAGE_W_MM} {PAGE_H_MM}"
         preserveAspectRatio="xMidYMid slice"
         xmlns="http://www.w3.org/2000/svg">
        {COVER_STARS}
        {COVER_NETWORK}
    </svg>
    <div class="cover-inner">
        <div class="cover-eyebrow">Brand book &middot; v1 &middot; 2026·05·21</div>
        <h1 class="wordmark">Telaris</h1>
        <div class="cover-tagline">weaving memory</div>
        <div class="cover-rule"></div>
        <p class="cover-desc">A decolonial knowledge archive project.
        Relational, P2P, non-hierarchical. Threaded by meaning.</p>
    </div>
    <div class="cover-foot">
        <span class="dot"></span> telaris.ca
        <span class="dot"></span> A UBC GRSJ graduate project
        <span class="dot"></span>
    </div>
</section>
"""

    # ----- What is Telaris -----
    what = f"""
<section class="section what" id="sec-what">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 01 &middot; What is Telaris</div>
        <div class="section-num">01</div>
    </div>
    <p class="pull">Telaris is a <em>decolonial knowledge archive</em>
    rendered as a relational cosmos: galaxies of wormholes, threaded by meaning,
    held open by the people who write into them and the communities they
    belong to.</p>
    <div class="pull-tag">tejiendo memoria &middot; tecendo memória</div>
    <div class="what-grid">
        <div class="what-card">
            <div class="what-num">A</div>
            <div class="what-h">Relational, not hierarchical</div>
            <div class="what-p">No parent/child trees. Wormholes connect through
            shared keywords and editorial gestures; meaning emerges from the
            density of relations, not from a taxonomy imposed from above.</div>
        </div>
        <div class="what-card">
            <div class="what-num">B</div>
            <div class="what-h">P2P, sovereign</div>
            <div class="what-p">Each Telaris instance is owned by its operator;
            galaxies are published peer-to-peer through a coordination layer
            called the Pluriverse. No platform sits above the network.</div>
        </div>
        <div class="what-card">
            <div class="what-num">C</div>
            <div class="what-h">Multilingual by design</div>
            <div class="what-p">English, Spanish, and Portuguese from v1, as
            sibling phrasings rather than translations of an English master.
            The project refuses to give the analytical ground to a single
            colonial language.</div>
        </div>
        <div class="what-card">
            <div class="what-num">D</div>
            <div class="what-h">A cosmic interface for a careful practice</div>
            <div class="what-p">Visitors enter galaxies and pass through
            wormholes; editors weave keyword canvases; source communities hold
            consent. The cosmic surface is what makes a careful editorial
            practice feel inhabitable, not abstract.</div>
        </div>
    </div>
</section>
"""

    # ----- Table of contents -----
    toc_items = [
        ("What is Telaris", "sec-what"),
        ("Contents", "sec-toc"),
        ("Palette &middot; the system", "sec-palette-system"),
        ("Palette &middot; constellation chips", "sec-palette-chips"),
        ("Palette &middot; surfaces & radii", "sec-palette-surfaces"),
        ("Type &middot; the stack & the scale", "sec-type-stack"),
        ("Type &middot; weight, case, spacing", "sec-type-weights"),
        ("Voice &middot; principles", "sec-voice-principles"),
        ("Voice &middot; do / don't", "sec-voice-dodont"),
        ("Naming &middot; project & sub-products", "sec-naming-main"),
        ("Naming &middot; vocabulary mapping", "sec-naming-vocab"),
        ("Tagline", "sec-tagline"),
        ("Iconography &middot; signature motifs", "sec-iconog"),
        ("Iconography &middot; the six themes", "sec-themes"),
        ("Colophon", "sec-colophon"),
    ]
    toc_lis = "\n".join(
        f'<li><a href="#{anchor}"><span class="toc-title">{title}</span></a></li>'
        for title, anchor in toc_items
    )
    toc = f"""
<section class="section toc" id="sec-toc">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 02 &middot; Contents</div>
        <div class="section-num">02</div>
    </div>
    <h1>Contents</h1>
    <ol>{toc_lis}</ol>
</section>
"""

    # ----- Palette: system -----
    palette_system = f"""
<section class="section" id="sec-palette-system">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 03 &middot; Palette &middot; the system</div>
        <div class="section-num">03</div>
    </div>
    <h1>Palette</h1>
    <p class="lead">Two layers. A small <strong>system palette</strong> carries
    the cosmic-HUD chrome: deep black ground, cool off-white type, and a single
    mint accent. A wider <strong>constellation palette</strong> (next page)
    carries the relational meaning.</p>
    <div class="system-grid">
        <div class="system-card">
            <div class="system-swatch starfield">
                <svg viewBox="0 0 100 30" preserveAspectRatio="xMidYMid slice"
                     style="position:absolute;inset:0;width:100%;height:100%;">
                    {starfield_svg(100, 30, count=70, seed=11)}
                </svg>
            </div>
            <div class="system-meta">
                <span class="system-name">Void</span>
                <span class="system-hex">#000000</span>
                <div class="system-role">The ground. True black. The starfield
                draws onto this; no gradients on the base.</div>
            </div>
        </div>
        <div class="system-card">
            <div class="system-swatch aurora"></div>
            <div class="system-meta">
                <span class="system-name">Aurora white</span>
                <span class="system-hex">#E8EEF0</span>
                <div class="system-role">Body type at full opacity. At 60 %
                for taglines and descriptions; 28 % for footer-tier labels.</div>
            </div>
        </div>
        <div class="system-card">
            <div class="system-swatch mint"></div>
            <div class="system-meta">
                <span class="system-name">Wormhole mint</span>
                <span class="system-hex">#00FFCC</span>
                <div class="system-role">The single chrome accent. Eyebrows,
                CTAs, status dots, focus outlines, halo. Never a body colour.</div>
            </div>
        </div>
        <div class="system-card">
            <div class="system-swatch halo">
                <span class="halo-text">Halo</span>
            </div>
            <div class="system-meta">
                <span class="system-name">Mint halo</span>
                <span class="system-hex">rgba(0,255,204,0.18)</span>
                <div class="system-role">The brand's warmth signature. Sits on
                the wordmark and around the elevated modal class. Reserved.</div>
            </div>
        </div>
    </div>
    <h2>Foreground tiers</h2>
    <p>Aurora at 100 % / 60 % / 28 % alpha is the full foreground scale.
    Body text at 100 %, taglines and descriptions at 60 %, footer-level labels
    at 28 %. The same single hue, three readings.</p>
</section>
"""

    # ----- Palette: chips -----
    chips_html = chip_swatch_row()
    lighter_html = lighter_pastel_row()
    chipbg_html = chip_bg_row()
    palette_chips = f"""
<section class="section" id="sec-palette-chips">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 04 &middot; Palette &middot; chips</div>
        <div class="section-num">04</div>
    </div>
    <h1>Constellation</h1>
    <p class="lead">Seventeen pastels. Same array drives the keyword chips in
    the app and the floating nodes on the Pluriverse landing. A hash of the
    keyword (or node id) chooses the colour, so the same word is always the
    same colour across surfaces and sessions.</p>
    <div class="palette-grid">{chips_html}</div>
    <h2>Editorial backgrounds &middot; ten lighter pastels</h2>
    <p>Pale background plates used to cluster related items in admin tables
    and editor lists. Foreground job, not content; never interchangeable with
    the seventeen-colour constellation palette.</p>
    <div class="lighter-grid">{lighter_html}</div>
    <h2>Editor chip backgrounds &middot; 25 % alpha</h2>
    <p>Parallel to the constellation palette, each colour at 25 % alpha. Used
    inside the editor when a chip needs a tinted plate instead of a bare run.</p>
    <div class="chipbg-grid">{chipbg_html}</div>
</section>
"""

    # ----- Palette: surfaces & radii -----
    surfaces_stars = starfield_svg(180, 70, count=180, seed=303)
    palette_surfaces = f"""
<section class="section" id="sec-palette-surfaces">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 05 &middot; Palette &middot; surfaces</div>
        <div class="section-num">05</div>
    </div>
    <h1>In-app surfaces</h1>
    <p class="lead">HUD panels, modals, and overlays are translucent black
    over the cosmos, layered with backdrop blur so the chrome reads as a
    layer <em>above</em> the cosmos rather than mixed into it. Four panel
    tiers and one elevated modal class.</p>
    <div class="surfaces-panel">
        <svg class="stars" viewBox="0 0 180 70" preserveAspectRatio="xMidYMid slice">
            {surfaces_stars}
        </svg>
        <div class="panel-stack">
            <div class="demo-panel tier-1">Tier 1 &middot; .40</div>
            <div class="demo-panel tier-2">Tier 2 &middot; .50</div>
            <div class="demo-panel tier-3">Tier 3 &middot; .70</div>
            <div class="demo-panel tier-4">Elevated &middot; .90</div>
        </div>
    </div>
    <div class="surfaces-legend">
        <div class="leg">
            <span class="leg-tag">Tier 1</span>
            <span class="leg-spec">rgba(0,0,0,0.4) / blur 4-6px</span>
        </div>
        <div class="leg">
            <span class="leg-tag">Tier 2</span>
            <span class="leg-spec">rgba(0,0,0,0.5) / standard HUD</span>
        </div>
        <div class="leg">
            <span class="leg-tag">Tier 3</span>
            <span class="leg-spec">rgba(0,0,0,0.7) / dense controls</span>
        </div>
        <div class="leg">
            <span class="leg-tag">Elevated</span>
            <span class="leg-spec">#0A0A0C·.9 + mint halo box-shadow</span>
        </div>
    </div>
    <h2>Border-radius vocabulary</h2>
    <div class="radius-row">
        <div class="radius-demo radius-2">2px</div>
        <div class="radius-demo radius-4">4px</div>
        <div class="radius-demo radius-12">12px</div>
        <div class="radius-demo radius-lg">lg</div>
        <div class="radius-demo radius-pill">pill</div>
    </div>
    <p>Five values. Square-ish buttons (2px); standard chrome (4px); tooltips
    (12px); modal containers (lg); pills, dots, and switches (pill). Stay
    inside this vocabulary unless there is a strong content reason to break it.</p>
</section>
"""

    # ----- Type: stack & scale -----
    type_stack_html = f"""
<section class="section" id="sec-type-stack">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 06 &middot; Type &middot; stack & scale</div>
        <div class="section-num">06</div>
    </div>
    <h1>Type</h1>
    <p class="lead">Monospace only. No display face, no humanist sans, no
    serif body. Every visible character in Telaris is set in the system
    monospace; this page is set in it; the wordmark is set in it; admin tables
    and visitor canvases share it.</p>
    <div class="type-stack">
        <div class="type-stack-name">Stack</div>
        <div class="type-stack-value">ui-monospace, SFMono-Regular, Menlo,
        Monaco, Consolas, "Liberation Mono", "Courier New", monospace</div>
    </div>
    <div class="type-spec display">
        <div class="spec-meta">Display &middot; clamp(2.75rem, 11vw, 6.5rem) &middot; uppercase &middot; spacing 0.18em</div>
        <div class="display-sample">Telaris</div>
    </div>
    <div class="type-spec">
        <div class="spec-meta">H2 &middot; 16pt &middot; spacing 0.06em</div>
        <div class="h2-sample spec-sample">Weaving the cosmos</div>
    </div>
    <div class="type-spec">
        <div class="spec-meta">Body &middot; 10pt &middot; line-height 1.7</div>
        <div class="body-sample spec-sample">A decolonial knowledge archive
        project. Relational, P2P, non-hierarchical. Threaded by meaning.
        Visitors enter galaxies and pass through wormholes; editors weave
        keyword canvases; source communities hold consent.</div>
    </div>
    <div class="type-spec">
        <div class="spec-meta">Tagline &middot; lowercase &middot; spacing 0.32em</div>
        <div class="tagline-sample spec-sample">weaving memory</div>
    </div>
    <div class="type-spec">
        <div class="spec-meta">Label / eyebrow &middot; uppercase &middot; spacing 0.35em</div>
        <div class="label-sample spec-sample">Active instances</div>
    </div>
    <div class="type-spec">
        <div class="spec-meta">Micro / footer &middot; uppercase &middot; spacing 0.25em</div>
        <div class="micro-sample spec-sample">System &middot; Online</div>
    </div>
</section>
"""

    # ----- Type: weights, case, spacing -----
    type_weights = f"""
<section class="section" id="sec-type-weights">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 07 &middot; Type &middot; weights, case, spacing</div>
        <div class="section-num">07</div>
    </div>
    <h1>Weight, case, spacing</h1>
    <h2 class="standalone">Three weights only</h2>
    <div class="weight-row">
        <div class="weight-cell">
            <div class="weight-glyph" style="font-weight:400;">Aa</div>
            <div class="weight-w">400</div>
            <div class="weight-role">Body, taglines, eyebrows</div>
        </div>
        <div class="weight-cell">
            <div class="weight-glyph" style="font-weight:500;">Aa</div>
            <div class="weight-w">500</div>
            <div class="weight-role">Chip default, HUD labels</div>
        </div>
        <div class="weight-cell">
            <div class="weight-glyph" style="font-weight:700;">Aa</div>
            <div class="weight-w">700</div>
            <div class="weight-role">Chip active, sparing emphasis</div>
        </div>
    </div>
    <p>No 300, no 600, no 800+. Emphasis comes from <strong>letter-spacing</strong>,
    <strong>case</strong>, and <strong>glow</strong> instead of weight.</p>
    <h2>Letter-spacing as signature</h2>
    <div class="spacing-row">
        <div class="spacing-cell">
            <div class="spacing-tag">Tight HUD &middot; 0.06em</div>
            <div class="spacing-sample s06">Galaxies &middot; Back &middot; Tour</div>
        </div>
        <div class="spacing-cell">
            <div class="spacing-tag">Standard label &middot; 0.18em</div>
            <div class="spacing-sample s18">Telaris &middot; View repository</div>
        </div>
        <div class="spacing-cell">
            <div class="spacing-tag">Wide ceremonial &middot; 0.32em</div>
            <div class="spacing-sample s32">Active instances</div>
        </div>
    </div>
    <h2>Case discipline</h2>
    <p><strong>Uppercase + label spacing</strong> for the wordmark, eyebrows,
    buttons, footer status. <strong>Lowercase + ceremonial spacing</strong>
    for the tagline (the deliberate inversion: most brands shout their
    tagline; Telaris murmurs it). <strong>Sentence case</strong> for body,
    descriptions, modal text. <strong>No title-case headlines.</strong>
    Title Case Reads As Generic Web Marketing And Is Out Of Brand.</p>
</section>
"""

    # ----- Voice: principles -----
    voice_principles = f"""
<section class="section" id="sec-voice-principles">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 08 &middot; Voice &middot; principles</div>
        <div class="section-num">08</div>
    </div>
    <h1>Voice</h1>
    <p class="lead">Telaris's voice is constant. The tone moves between two
    registers without breaking: a cosmic-HUD chrome (eyebrows, labels, status
    footers, system messages) and a humanistic content register (taglines,
    descriptions, governance language, errors that explain a real consequence
    to a real person).</p>
    <div class="voice-grid">
        {voice_card(1, "Observational over promotional",
            "Telaris describes itself the way an instrument describes a "
            "reading. It does not sell, persuade, or court.")}
        {voice_card(2, "Terse over decorative",
            "Short declarative sentences. Few qualifiers. The reader does "
            "the work of building the picture.")}
        {voice_card(3, "Decolonial framings are analytical, not metaphor",
            "&lsquo;Decolonial&rsquo; names a method. Never soften to "
            "&lsquo;diverse&rsquo;, &lsquo;inclusive&rsquo;, or &lsquo;global&rsquo;.")}
        {voice_card(4, "Name people or roles, never institutions",
            "No &lsquo;team&rsquo;, &lsquo;board&rsquo;, or &lsquo;organisation behind Telaris&rsquo;. "
            "Institutional framing imports the pattern Telaris refuses.")}
        {voice_card(5, "Cosmic surface, humanistic content",
            "Chrome reads as a HUD on a quiet observation deck. Content reads "
            "as careful, lowercase, plain. The frame is HUD; the speech is human.")}
        {voice_card(6, "Plurality, never neutrality",
            "Telaris speaks as an authored project. &lsquo;We&rsquo; names a concrete "
            "plurality (operators, editors) or recasts to the named role.")}
    </div>
</section>
"""

    # ----- Voice: do / don't -----
    voice_dodont = f"""
<section class="section" id="sec-voice-dodont">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 09 &middot; Voice &middot; do / don't</div>
        <div class="section-num">09</div>
    </div>
    <h1>Do / don't</h1>
    <p class="lead">The same surface, side by side. The version in brand is
    on the mint side; the version out of brand is on the rose side.</p>
    {dodont_row(
        "weaving memory",
        "Weaving Memory.")}
    {dodont_row(
        "Graduate project &middot; UBC GRSJ",
        "Powered by cutting-edge decolonial AI")}
    {dodont_row(
        "A decolonial knowledge archive project. Relational, P2P, "
        "non-hierarchical. Threaded by meaning.",
        "Telaris is a revolutionary platform that empowers diverse "
        "communities to share their stories through stunning 3D visualization.")}
    {dodont_row(
        "View repository &rarr;",
        "Get started now! &#x26A1;")}
    {dodont_row(
        "This wormhole could not load. The source community may have "
        "withdrawn consent. Try again, or move to the next wormhole.",
        "Oops! Something went wrong. Please try again later.")}
    {dodont_row(
        "Schema migration applied: 3 columns added to constellations table.",
        "Success! Your changes have been saved.")}
</section>
"""

    # ----- Naming: project & sub-products -----
    naming_main = f"""
<section class="section" id="sec-naming-main">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 10 &middot; Naming &middot; project</div>
        <div class="section-num">10</div>
    </div>
    <h1>Naming</h1>
    <p class="lead">Telaris's nouns carry political and architectural
    commitments. Each name was chosen to refuse a more obvious-but-wrong
    alternative; choosing the right one in the right place is voice work,
    not bookkeeping.</p>
    <div class="naming-grid">
        <div class="naming-card">
            <div class="nm-tag">The project</div>
            <div class="nm-name">Telaris</div>
            <div class="nm-body">The project, the software, any deployed
            instance. Reads (pending author confirmation) as a hybrid of
            <em>telar</em> (loom, ES/PT) with a Latinate ending evocative of
            <em>stellaris</em>: weaving and cosmos in a single coined word.</div>
        </div>
        <div class="naming-card">
            <div class="nm-tag">The coordinator</div>
            <div class="nm-name">the Pluriverse</div>
            <div class="nm-body">The application at <code>www.telaris.ca</code>:
            discovery, identity, magic-link auth, in-app messaging via the
            relay, version-mismatch handling. Renamed from &lsquo;Registry&rsquo; in v6;
            draws on Escobar, Mignolo, Reiter, Césaire.</div>
        </div>
        <div class="naming-card">
            <div class="nm-tag">The framework</div>
            <div class="nm-name">Bridges</div>
            <div class="nm-body">Brings galaxies into a Telaris instance from
            non-Telaris upstream archives. First bridge: Mocambos / Baobáxia.
            Capitalise as a proper noun; lowercase &lsquo;a bridge&rsquo; in prose.</div>
        </div>
        <div class="naming-card">
            <div class="nm-tag">The relay</div>
            <div class="nm-name">no-reply@telaris.ca</div>
            <div class="nm-body">Used for all inter-peer email communication.
            Always with the full address, lowercase, code-font. The other side
            sees only the relay address; personal emails are never shared.</div>
        </div>
        <div class="naming-card">
            <div class="nm-tag">The upstream archive</div>
            <div class="nm-name">Mocambos &middot; Baobáxia</div>
            <div class="nm-body">A community archive Telaris imports from.
            Capitalise both; treat as proper nouns belonging to the upstream
            community, not Telaris&rsquo;s to retranslate or restyle.</div>
        </div>
        <div class="naming-card">
            <div class="nm-tag">The locales</div>
            <div class="nm-name">en &middot; es &middot; pt</div>
            <div class="nm-body">Translated into English, Spanish, Portuguese
            from federation v1. French queued. Localisations are sibling
            phrasings, not translations of an English master.</div>
        </div>
    </div>
</section>
"""

    # ----- Naming: vocabulary mapping -----
    naming_vocab = f"""
<section class="section" id="sec-naming-vocab">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 11 &middot; Naming &middot; vocabulary</div>
        <div class="section-num">11</div>
    </div>
    <h1>Vocabulary</h1>
    <p class="lead">UI strings use the public Telaris vocabulary
    (<strong>Galaxy, Wormhole, Portal</strong>). Code identifiers, DB columns,
    API paths, URL parameters stay on the internal vocabulary
    (<code>constellation</code>, <code>node</code>, <code>portal</code>).
    The mapping is the contract: do not let the internal vocabulary leak
    into UI; do not rename the code identifiers.</p>
    <table class="vocab-table">
        <thead>
            <tr>
                <th>UI &middot; English</th>
                <th>UI &middot; Español</th>
                <th>UI &middot; Português</th>
                <th>Code identifier</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Galaxy</td>
                <td>Galaxia</td>
                <td>Galáxia</td>
                <td class="code-col">constellation</td>
            </tr>
            <tr>
                <td>Wormhole</td>
                <td>Agujero de Gusano</td>
                <td>Buraco de Minhoca</td>
                <td class="code-col">node</td>
            </tr>
            <tr>
                <td>Portal</td>
                <td>Portal</td>
                <td>Portal</td>
                <td class="code-col">portal</td>
            </tr>
        </tbody>
    </table>
    <h2>Why the public vocabulary changed</h2>
    <p>A <strong>galaxy</strong> is something one enters and moves through; a
    constellation is something one looks up at from outside. Telaris is an
    inside-the-cosmos experience.</p>
    <p>A <strong>wormhole</strong> is non-hierarchical and content-bearing
    (it goes somewhere, it carries you); a node is graph-theoretic and
    merely positional.</p>
    <p><strong>Portal</strong> kept its name because it was already doing
    exactly the right work: a gateway that opens onto a different space.</p>
</section>
"""

    # ----- Tagline -----
    tagline = f"""
<section class="section tagline-page" id="sec-tagline">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 12 &middot; Tagline</div>
        <div class="section-num">12</div>
    </div>
    <div class="tagline-block">
        <div class="tagline-loc">English</div>
        <div class="tagline-display spacious">weaving memory</div>
    </div>
    <div class="tagline-block">
        <div class="tagline-loc">Español</div>
        <div class="tagline-display spacious">tejiendo memoria</div>
    </div>
    <div class="tagline-block">
        <div class="tagline-loc">Português</div>
        <div class="tagline-display spacious">tecendo memória</div>
    </div>
    <div class="tagline-rule"></div>
    <p class="tagline-desc">Lowercase. Wide ceremonial spacing (0.32em). Aurora
    white at 60% alpha. The three languages carry the tagline at the same
    weight; the English is not the master. <em>Tejiendo</em> and
    <em>tecendo</em> are the same active present participle in each language;
    <em>memoria</em> and <em>memória</em> are the same noun. Two words; a
    whole project.</p>
</section>
"""

    # ----- Iconography: motifs -----
    icon_stars_for_card = starfield_svg(80, 36, count=80, seed=121)
    icon_network_for_card = node_network_svg(80, 36, seed=212)
    iconog = f"""
<section class="section" id="sec-iconog">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 13 &middot; Iconography &middot; motifs</div>
        <div class="section-num">13</div>
    </div>
    <h1>Motifs</h1>
    <p class="lead">The signature behaviours of the canvas, the chrome, and
    the data, repeated until they become recognisable. Telaris has no
    logomark; the wordmark plus these motifs are the brand's visible identity.</p>
    <div class="icon-grid">
        <div class="icon-card">
            <div class="icon-canvas">
                <svg viewBox="0 0 80 36" preserveAspectRatio="xMidYMid slice">
                    {icon_stars_for_card}
                </svg>
            </div>
            <div class="icon-meta">
                <div class="icon-name">Canvas starfield</div>
                <div class="icon-body">The floor of every cosmic surface.
                90&ndash;220 white dots, random alpha, slow twinkle. Drops
                only when the editor explicitly leaves the cosmic theme.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <svg viewBox="0 0 80 36" preserveAspectRatio="xMidYMid slice">
                    {icon_network_for_card}
                </svg>
            </div>
            <div class="icon-meta">
                <div class="icon-name">Pastel node-network</div>
                <div class="icon-body">Pastel nodes from the constellation
                palette, gradient links whose colour fades node-to-node.
                Always above the starfield, never on a flat plate.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <div class="halo-demo">
                    <span class="halo-word">Telaris</span>
                </div>
            </div>
            <div class="icon-meta">
                <div class="icon-name">Mint halo + scanline</div>
                <div class="icon-body">A soft mint glow plus a 4px CRT interlace
                overlay. Reserved for the wordmark and the elevated modal class.
                Type-system motif: scanlines sit on type, never under it.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <div class="scanline-demo">
                    <span class="s">System &middot; Online</span>
                </div>
            </div>
            <div class="icon-meta">
                <div class="icon-name">CRT scanline overlay</div>
                <div class="icon-body">Linear-gradient interlace, 4px band.
                Used on the wordmark, on the in-app tooltip, on dense floating
                panels. Never on body prose.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <div class="dot-demo">
                    <span class="d" style="background:{MINT};color:{MINT};"></span>
                    <span class="d" style="background:#7dd3fc;color:#7dd3fc;"></span>
                    <span class="d" style="background:#86efac;color:#86efac;"></span>
                    <span class="d" style="background:#fdba74;color:#fdba74;"></span>
                </div>
            </div>
            <div class="icon-meta">
                <div class="icon-name">Status dot</div>
                <div class="icon-body">Mint by default for &lsquo;system online&rsquo;;
                recoloured to a pastel for instance markers, each glowing in its
                own colour. Smallest possible &lsquo;is this alive?&rsquo; affordance.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <div class="rule-demo"><div class="r"></div></div>
            </div>
            <div class="icon-meta">
                <div class="icon-name">HUD rule</div>
                <div class="icon-body">1px centred gradient, max 560px wide.
                The brand's paragraph break for headers; separates logical
                groups inside a panel.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <div class="chip-demo">
                    {pastel_chip("relational", "#7dd3fc")}
                    {pastel_chip("memoria", "#fcd34d")}
                    {pastel_chip("rhizome", "#86efac")}
                    {pastel_chip("decolonial", "#f0abfc")}
                    {pastel_chip("p2p", "#fda4af")}
                </div>
            </div>
            <div class="icon-meta">
                <div class="icon-name">Keyword chip glow</div>
                <div class="icon-body">Hover or activate a chip and its text
                glows in its own colour; siblings dim. The strip pulses with
                the visitor's attention. The brand's most expressive interaction.</div>
            </div>
        </div>
        <div class="icon-card">
            <div class="icon-canvas">
                <div class="dot-grid-demo"></div>
            </div>
            <div class="icon-meta">
                <div class="icon-name">Dot-grid surface</div>
                <div class="icon-body">Soft grey dots on black at 28px pitch.
                Editor-only: the artboard the visitor never sees. Marks
                editorial / design-tool surfaces.</div>
            </div>
        </div>
    </div>
</section>
"""

    # ----- Themes -----
    # Build a small 3-node sample for each theme card.
    def theme_nodes(positions, theme_class):
        parts = []
        for x, y, colour in positions:
            parts.append(
                f'<span class="tc-node" style="left:{x}%;top:{y}%;'
                f'width:5mm;height:5mm;background:{colour};"></span>'
            )
        return "".join(parts)

    cosmic_nodes = theme_nodes([
        (20, 30, "#7dd3fc"), (55, 55, "#fcd34d"),
        (75, 25, "#f0abfc"), (40, 70, "#86efac"),
    ], "tc-cosmic")
    abstract_nodes = theme_nodes([
        (25, 35, "#fda4af"), (65, 30, "#a5b4fc"),
        (45, 65, "#fde047"),
    ], "tc-abstract")
    rect_nodes = ""
    for x, y, colour in [(20, 30, "#86efac"), (55, 50, "#7dd3fc"), (75, 25, "#fdba74")]:
        rect_nodes += (
            f'<span class="tc-node" style="left:{x}%;top:{y}%;'
            f'width:7mm;height:4mm;background:{colour};border-radius:1mm;"></span>'
        )
    simple_nodes = theme_nodes([
        (30, 40, AURORA), (60, 60, AURORA),
    ], "tc-simple")
    tech_nodes = theme_nodes([
        (25, 30, MINT), (60, 50, "#7dd3fc"), (45, 70, "#86efac"),
    ], "tc-tech")
    stripe_nodes = ""
    for x, y, colour in [(20, 30, "#a5b4fc"), (55, 50, "#fda4af"), (75, 65, "#fde047")]:
        stripe_nodes += (
            f'<span class="tc-node" style="left:{x}%;top:{y}%;'
            f'width:5mm;height:8mm;background:repeating-linear-gradient(45deg,{colour},{colour} 1mm,transparent 1mm,transparent 2mm);'
            f'border:1px solid {colour}aa;"></span>'
        )

    tc_cosmic_stars = starfield_svg(80, 32, count=50, seed=901)

    themes_html = f"""
<section class="section" id="sec-themes">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 14 &middot; Iconography &middot; the six themes</div>
        <div class="section-num">14</div>
    </div>
    <h1>The six themes</h1>
    <p class="lead">The app carries six visual presentations of the same data
    model. <strong>Cosmic is the brand default.</strong> The others are
    intentional departures, chosen per-galaxy by editors when the content
    asks for a different register. All six share the dark ground, the
    monospace stack, the pastel content palette, the mint accent, and the HUD
    chrome; they differ only in what is in the canvas.</p>
    <div class="theme-grid">
        <div class="theme-card">
            <div class="theme-canvas tc-cosmic">
                <svg class="tc-stars" viewBox="0 0 80 32" preserveAspectRatio="xMidYMid slice"
                     style="position:absolute;inset:0;width:100%;height:100%;">
                    {tc_cosmic_stars}
                </svg>
                {cosmic_nodes}
            </div>
            <div class="theme-meta">
                <span class="theme-name">Cosmic</span>
                <span class="theme-role">Default &middot; the brand</span>
                <div class="theme-body">Starfield + nebulae + cosmic animations.
                Geometric pastel nodes (star, moon, asteroid, sparkle).</div>
            </div>
        </div>
        <div class="theme-card">
            <div class="theme-canvas tc-abstract">{abstract_nodes}</div>
            <div class="theme-meta">
                <span class="theme-name">Abstract</span>
                <span class="theme-role">Editor variant</span>
                <div class="theme-body">Black + grid. 73 abstract icons,
                pastel-tinted. For non-cosmic content.</div>
            </div>
        </div>
        <div class="theme-card">
            <div class="theme-canvas tc-rectangles">{rect_nodes}</div>
            <div class="theme-meta">
                <span class="theme-name">Rectangles</span>
                <span class="theme-role">Editor variant</span>
                <div class="theme-body">Black + grid. Six rectangular icons.</div>
            </div>
        </div>
        <div class="theme-card">
            <div class="theme-canvas tc-stripes">{stripe_nodes}</div>
            <div class="theme-meta">
                <span class="theme-name">Stripes</span>
                <span class="theme-role">Editor variant</span>
                <div class="theme-body">Black + grid. Six striped icons.</div>
            </div>
        </div>
        <div class="theme-card">
            <div class="theme-canvas tc-simple">{simple_nodes}</div>
            <div class="theme-meta">
                <span class="theme-name">Simple</span>
                <span class="theme-role">Accessibility fallback</span>
                <div class="theme-body">Plain spheres on black. Minimum-stimulation
                fallback for low-power devices or visitors who need it.</div>
            </div>
        </div>
        <div class="theme-card">
            <div class="theme-canvas tc-tech">{tech_nodes}</div>
            <div class="theme-meta">
                <span class="theme-name">Tech</span>
                <span class="theme-role">Editor variant</span>
                <div class="theme-body">Deep blue-black (#000205) + tech grid.
                Twelve schematic icons. When the content fits a schematic register.</div>
            </div>
        </div>
    </div>
</section>
"""

    # ----- Colophon -----
    colophon = f"""
<section class="section colophon" id="sec-colophon">
    <div class="section-header">
        <div class="section-eyebrow"><span class="dot"></span> 15 &middot; Colophon</div>
        <div class="section-num">15</div>
    </div>
    <h1>Colophon</h1>
    <div class="colo-block">
        <div class="colo-h">Version</div>
        <div class="colo-p colo-code">Brand book v1 &middot; 2026-05-21</div>
        <div class="colo-p">Compiled from the canonical brand-book notes
        (Palette, Type, Voice and tone, Naming, Taglines, Iconography,
        Screenshots), the Pluriverse landing page, and the Telaris app
        itself. The Telaris codebase is the practical reference; the
        notes are the editorial one.</div>
    </div>
    <div class="colo-block">
        <div class="colo-h">Sibling notes</div>
        <div class="colo-p">Palette &middot; Type &middot; Voice and tone &middot;
        Naming &middot; Taglines &middot; Iconography &middot; Screenshots.
        Read the notes for the long form; this PDF is the visual primer.</div>
    </div>
    <div class="colo-block">
        <div class="colo-h">Type</div>
        <div class="colo-p">Set in the brand's monospace stack
        (<code>ui-monospace</code> &rarr; SF Mono &rarr; Menlo &rarr; Consolas
        &rarr; Liberation Mono &rarr; Courier New). Rendered for this PDF in
        Liberation Mono / DejaVu Sans Mono, the Linux tail of the stack.</div>
    </div>
    <div class="colo-block">
        <div class="colo-h">Build</div>
        <div class="colo-p colo-code">python3 tools/build_brand_book.py</div>
        <div class="colo-p">Renders with WeasyPrint from a single freestanding
        script under <code>tools/</code> in the <code>telaris-documentation</code>
        repo. Deterministic (seeded RNG) so the document is reproducible.</div>
    </div>
    <div class="colo-block">
        <div class="colo-h">Open questions</div>
        <div class="colo-p">Etymology of &lsquo;Telaris&rsquo; awaits author confirmation;
        Spanish-voice sub-note pending; screenshot inventory not yet captured.
        See the vault notes for the full list.</div>
    </div>
</section>
"""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Telaris — Brand book</title>
<style>{CSS}</style>
</head>
<body>
{cover}
{what}
{toc}
{palette_system}
{palette_chips}
{palette_surfaces}
{type_stack_html}
{type_weights}
{voice_principles}
{voice_dodont}
{naming_main}
{naming_vocab}
{tagline}
{iconog}
{themes_html}
{colophon}
</body>
</html>
"""


def main() -> None:
    import shutil

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    html_str = build_html()
    HTML(string=html_str, base_url=str(OUT_PATH.parent)).write_pdf(str(OUT_PATH))
    print(f"Wrote {OUT_PATH}")

    # Optional mirror to an operator-configured location (e.g. a notes vault
    # synced across devices). Only fires if TELARIS_BRAND_BOOK_MIRROR is set
    # and the destination parent directory already exists.
    if MIRROR_PATH is not None and MIRROR_PATH.parent.exists():
        shutil.copyfile(OUT_PATH, MIRROR_PATH)
        print(f"Mirrored to {MIRROR_PATH}")


if __name__ == "__main__":
    main()
