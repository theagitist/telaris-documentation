# Brand book

Placeholder until migration. The current brand-book PDF is built by a freestanding script at:

```
~/apps/telaris/original_assets/brand/build_brand_book_pdf.py
```

That script constructs HTML programmatically (with generated SVG starfields, node networks, swatches, wordmark, scanline overlays) and renders via WeasyPrint to the vault path. When this directory is populated, the brand book will move to the same `markdown source -> document.html.jinja -> WeasyPrint` pattern as the editor and admin manuals, using `styles/brand-book.css` for the dark-cosmic identity. Visual artefacts (starfield, node networks, etc.) get extracted to `tools/` as deterministic SVG generators whose output lands under `assets/generated/brand-book/` and is referenced from markdown.

Migration plan (rough): port the freestanding script's HTML construction into markdown + per-page CSS, move SVG generators to `tools/`, retire the freestanding script, point the brand-book vault note at the new PDF location.
