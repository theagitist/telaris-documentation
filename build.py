#!/usr/bin/env python3
"""Build a Telaris documentation PDF from markdown sources.

Usage:
    python3 build.py <doc-slug>           # e.g. editor-manual
    python3 build.py <doc-slug> --html    # also emit the intermediate HTML

Reads src/<doc-slug>/meta.yaml plus all *.md files in that directory (ordered
by filename), renders them through templates/document.html.jinja with the
shared styles/, and produces dist/<doc-slug>.pdf via WeasyPrint.

One script for every document in this repo: editor manual, admin manual, brand
book, anything future. Per-document look is controlled by meta.yaml's
doc_class field, which selects which per-class stylesheet is layered on top
of base.css.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt
from weasyprint import HTML

REPO_ROOT = Path(__file__).resolve().parent
SRC_DIR = REPO_ROOT / "src"
STYLES_DIR = REPO_ROOT / "styles"
TEMPLATES_DIR = REPO_ROOT / "templates"
ASSETS_DIR = REPO_ROOT / "assets"
DIST_DIR = REPO_ROOT / "dist"


@dataclass
class Section:
    """One markdown section file, in source-file order."""

    order: int
    slug: str
    body_md: str


@dataclass
class DocMeta:
    """Parsed contents of src/<slug>/meta.yaml."""

    slug: str
    title: str
    subtitle: str
    version: str
    doc_class: str  # 'manual' | 'brand-book'
    locale: str  # 'en' | 'es' | 'pt' | etc.
    cover_tagline: str
    page_size: str  # WeasyPrint accepts 'A4', 'Letter', etc.
    show_toc: bool  # render the dedicated TOC spread (default True)
    app_version: str  # optional: the Telaris app version this doc covers (cover line)


def load_meta(slug: str) -> DocMeta:
    """Read src/<slug>/meta.yaml into a DocMeta."""
    meta_path = SRC_DIR / slug / "meta.yaml"
    if not meta_path.exists():
        sys.exit(f"missing {meta_path}")
    raw = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    return DocMeta(
        slug=slug,
        title=raw.get("title", slug),
        subtitle=raw.get("subtitle", ""),
        version=raw.get("version", "v0"),
        doc_class=raw.get("doc_class", "manual"),
        locale=raw.get("locale", "en"),
        cover_tagline=raw.get("cover_tagline", ""),
        page_size=raw.get("page_size", "A4"),
        show_toc=bool(raw.get("show_toc", True)),
        app_version=raw.get("app_version", ""),
    )


SECTION_NAME_RE = re.compile(r"^(\d+)-(.+)\.md$")


def load_sections(slug: str) -> list[Section]:
    """Read every NN-slug.md under src/<slug>/, sorted by NN."""
    src = SRC_DIR / slug
    sections: list[Section] = []
    for path in sorted(src.glob("*.md")):
        match = SECTION_NAME_RE.match(path.name)
        if not match:
            # README.md, scratch notes, etc. are skipped.
            continue
        order = int(match.group(1))
        sec_slug = match.group(2)
        sections.append(
            Section(order=order, slug=sec_slug, body_md=path.read_text(encoding="utf-8"))
        )
    if not sections:
        sys.exit(f"no NN-slug.md sections found under {src}")
    return sections


# ---------------------------------------------------------------------------
# Obsidian-style callout to styled <div class="callout callout-<kind>">.
# Pattern: blockquote whose first line is "[!kind]" or "[!kind] Title".
# Supported kinds: note, warning, tip, important, danger, example.
# ---------------------------------------------------------------------------

CALLOUT_KINDS = {"note", "warning", "tip", "important", "danger", "example"}
CALLOUT_FIRST_LINE_RE = re.compile(r"^\s*\[!(?P<kind>[a-z]+)\](?:\s+(?P<title>.*))?$")


def transform_callouts(md: str) -> str:
    """Rewrite Obsidian callouts to fenced HTML blocks before markdown parsing.

    > [!note] Optional title
    > Body line one.
    > Body line two.

    becomes a literal HTML block, which markdown-it then passes through as-is.
    """
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith(">"):
            # Collect the whole blockquote.
            block: list[str] = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip(">").lstrip(" "))
                i += 1
            if block:
                first_match = CALLOUT_FIRST_LINE_RE.match(block[0])
                if first_match and first_match.group("kind") in CALLOUT_KINDS:
                    kind = first_match.group("kind")
                    title = (first_match.group("title") or kind.capitalize()).strip()
                    body_text = "\n".join(block[1:]).strip()
                    # We let markdown-it render the body, but we have not entered
                    # markdown parsing yet. Easiest: inject pre-rendered HTML by
                    # running a nested MarkdownIt on the body. Done in the caller.
                    out.append(f"<!--CALLOUT kind={kind} title={escape_attr(title)}-->")
                    out.append(body_text)
                    out.append("<!--CALLOUT-END-->")
                    continue
            # Not a callout; emit the blockquote untouched.
            for orig_line in block:
                out.append("> " + orig_line if orig_line else ">")
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def escape_attr(s: str) -> str:
    return s.replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


CALLOUT_BLOCK_RE = re.compile(
    r'<!--CALLOUT kind=(?P<kind>[a-z]+) title=(?P<title>[^>]*)-->'
    r'(?P<body>.*?)'
    r'<!--CALLOUT-END-->',
    re.DOTALL,
)


def render_callouts(html: str, md_renderer: MarkdownIt) -> str:
    """Replace callout marker pairs in the rendered HTML with styled divs."""

    def repl(match: re.Match[str]) -> str:
        kind = match.group("kind")
        title = match.group("title").replace("&quot;", '"')
        body_md = match.group("body").strip()
        body_html = md_renderer.render(body_md) if body_md else ""
        return (
            f'<div class="callout callout-{kind}">'
            f'<div class="callout-title">{title}</div>'
            f'<div class="callout-body">{body_html}</div>'
            f"</div>"
        )

    return CALLOUT_BLOCK_RE.sub(repl, html)


# ---------------------------------------------------------------------------
# Heading anchors, used by the TOC.
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r"<h([1-3])>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
SLUGIFY_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    return SLUGIFY_RE.sub("-", text).strip("-") or "section"


def add_heading_anchors(html: str, section_slug: str) -> tuple[str, list[tuple[int, str, str]]]:
    """Add id="..." attributes to h1/h2/h3 and return a TOC entry list.

    Returns (html_with_ids, [(level, anchor_id, plain_text), ...]).
    """
    toc: list[tuple[int, str, str]] = []

    def repl(match: re.Match[str]) -> str:
        level = int(match.group(1))
        inner = match.group(2)
        plain = re.sub(r"<[^>]+>", "", inner).strip()
        anchor = f"{section_slug}--{slugify(plain)}"
        toc.append((level, anchor, plain))
        return f'<h{level} id="{anchor}">{inner}</h{level}>'

    return HEADING_RE.sub(repl, html), toc


# A standalone image renders as <p><img ...></p>. Wrap it in a figure so the
# stylesheet can keep the screenshot whole and attached to its intro text
# (no image split across a page break, no image orphaned from the line above it).
SHOT_RE = re.compile(r"<p>\s*(<img\b[^>]*>)\s*</p>")


def wrap_shots(html: str) -> str:
    return SHOT_RE.sub(r'<figure class="shot">\1</figure>', html)


def render_section_html(section: Section, md_renderer: MarkdownIt) -> tuple[str, list[tuple[int, str, str]]]:
    """Markdown to HTML for one section, with callouts and heading anchors."""
    body = transform_callouts(section.body_md)
    raw_html = md_renderer.render(body)
    with_callouts = render_callouts(raw_html, md_renderer)
    with_shots = wrap_shots(with_callouts)
    with_ids, toc = add_heading_anchors(with_shots, section.slug)
    return with_ids, toc


# ---------------------------------------------------------------------------
# Stylesheet selection.
# ---------------------------------------------------------------------------

def collect_stylesheets(doc_class: str) -> list[Path]:
    """Return the ordered list of stylesheets to apply for this doc class."""
    base = STYLES_DIR / "base.css"
    per_class = STYLES_DIR / f"{doc_class}.css"
    sheets = [base]
    if per_class.exists():
        sheets.append(per_class)
    return sheets


# ---------------------------------------------------------------------------
# Optional vault / Syncthing mirror.
#
# For each document, the operator can opt in to copying the built PDF to a
# secondary location by setting an environment variable named
# TELARIS_<SLUG_UPPER>_MIRROR (hyphens become underscores). Typical use: a
# notes vault folder synced across devices so the PDF travels next to the
# canonical working notes. If the variable is unset OR the parent directory
# of the target path does not exist, the mirror step is skipped silently.
# Examples:
#   TELARIS_EDITOR_MANUAL_MIRROR=$HOME/notes/Editor Manual.pdf
#   TELARIS_ADMIN_MANUAL_MIRROR=$HOME/notes/Admin Manual.pdf
#   TELARIS_BRAND_BOOK_MIRROR=$HOME/notes/Brand book.pdf
# ---------------------------------------------------------------------------

def mirror_path_for(slug: str) -> Path | None:
    """Resolve the optional mirror target for `slug` from the environment.

    Returns None if the env var is unset or empty. Tilde-expansion is applied
    so `~/...` works. Existence of the parent directory is checked at copy
    time, not here.
    """
    env_key = f"TELARIS_{slug.upper().replace('-', '_')}_MIRROR"
    env_val = os.environ.get(env_key)
    if not env_val:
        return None
    return Path(env_val).expanduser()


# ---------------------------------------------------------------------------
# Build orchestration.
# ---------------------------------------------------------------------------

def build(slug: str, emit_html: bool = False) -> Path:
    meta = load_meta(slug)
    sections = load_sections(slug)

    md_renderer = (
        MarkdownIt("commonmark", {"breaks": False, "html": True, "linkify": True})
        .enable("table")
        .enable("strikethrough")
    )

    section_blocks: list[dict] = []
    full_toc: list[tuple[int, str, str]] = []
    for section in sections:
        html, toc = render_section_html(section, md_renderer)
        section_blocks.append({"slug": section.slug, "html": html})
        full_toc.extend(toc)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    template = env.get_template("document.html.jinja")

    stylesheet_paths = collect_stylesheets(meta.doc_class)
    stylesheets_inline = "\n\n".join(
        path.read_text(encoding="utf-8") for path in stylesheet_paths
    )

    rendered_html = template.render(
        meta=meta,
        stylesheets_inline=stylesheets_inline,
        sections=section_blocks,
        toc=full_toc,
    )

    DIST_DIR.mkdir(exist_ok=True)
    if emit_html:
        html_out = DIST_DIR / f"{slug}.html"
        html_out.write_text(rendered_html, encoding="utf-8")
        print(f"wrote {html_out}")

    pdf_out = DIST_DIR / f"{slug}.pdf"
    HTML(string=rendered_html, base_url=str(REPO_ROOT)).write_pdf(str(pdf_out))
    print(f"wrote {pdf_out}")

    mirror = mirror_path_for(slug)
    if mirror is not None and mirror.parent.exists():
        shutil.copyfile(pdf_out, mirror)
        print(f"mirrored to {mirror}")

    # Optional public-docs mirror. If TELARIS_WWW_DOCS_DIR is set to an
    # existing directory (typically /var/www/www.telaris.ca/docs/), every
    # built PDF is also copied there as <slug>.pdf. Used to keep the
    # Pluriverse website's download links in sync with the latest build
    # without an extra deploy step.
    www_docs_dir_env = os.environ.get("TELARIS_WWW_DOCS_DIR")
    if www_docs_dir_env:
        www_docs_dir = Path(www_docs_dir_env).expanduser()
        if www_docs_dir.exists() and www_docs_dir.is_dir():
            www_target = www_docs_dir / f"{slug}.pdf"
            shutil.copyfile(pdf_out, www_target)
            print(f"published to {www_target}")

    return pdf_out


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Telaris documentation PDF.")
    parser.add_argument("slug", help="Document slug (directory name under src/).")
    parser.add_argument("--html", action="store_true", help="Also emit intermediate HTML.")
    args = parser.parse_args()
    build(args.slug, emit_html=args.html)
    return 0


if __name__ == "__main__":
    sys.exit(main())
