# The keyword canvas

The keyword canvas is where you author the conceptual map of a galaxy. Wormholes give you objects; keywords give you ways to tag those objects; the canvas is where you draw, by hand, the relationships **between the keywords themselves**. Two chips lean closer because the editor decided they belong closer. Two chips have a line drawn between them because the editor decided to say *these two ideas are linked, and here is why*.

This chapter walks through the surface, its drawing affordances, and the editorial discipline of using it well.

## Opening the canvas

Select the galaxy you want to work on from the editor home. When a specific galaxy is selected, three buttons appear next to the galaxy picker; the third is **Canvas**. Select it. The canvas opens in a new tab.

> [!warning] Desktop only
> The canvas is a desktop-only surface. On a phone or tablet, the chip and line interactions do not behave well; the Canvas button is hidden in those contexts. If you need to work on a galaxy's keyword arrangement from a small screen, the wormhole list and the keyword field inside each wormhole modal still work; the canvas does not.

## What you see

The canvas opens in a full-viewport dark scene with the galaxy's keywords laid out as pastel chips on a dot grid:

![Keyword canvas: pastel chips with relation lines drawn between them, on a dark dotted-grid background](assets/images/editor-manual/10-keyword-canvas.png)

Each chip is one keyword. The colour of the chip matches the colour used elsewhere in the app: *native* is the same green-ish here as on a wormhole row. Chips drift slightly when the canvas is idle (a soft physics simulation keeps them alive); dragging a chip pins it in place from then on.

Lines between chips are **relations** the editor has drawn. Each line has two endpoints (the chips it connects), an optional note (a sentence explaining the connection), and a record of who drew it and when.

The top bar carries:
- **Back**: returns you to the editor home for this galaxy.
- The galaxy name.
- **?**: opens a small help overlay listing every canvas keyboard and mouse interaction.
- **Ready** (or **Saving…**): a small status indicator confirming the canvas has saved your most recent change.

## Drawing a relation

Two ways to draw a line between two chips:

1. **Click-click**: click one chip's anchor dot (a small circle that appears on the chip when you hover), then click another chip's anchor dot. A line snaps into place.
2. **Drag**: press on one chip's anchor dot and drag to the other chip; release. Same result.

When the line appears, a small inline input lets you type an optional note. Enter saves the note; Escape leaves the line without a note. The note is visible when a visitor (or another editor) hovers the line later.

The line **sticks to the chip edges** as you move chips around. Drag the *native* chip across the canvas; the line to *salt-tolerant* follows. There is no manual line routing; the geometry takes care of itself.

## Moving and arranging chips

- **Drag** a chip to reposition it. The new position is saved automatically.
- The canvas remembers position **per editor**: each editor has their own view of the canvas. Two editors working on the same galaxy do not fight over chip positions; each sees their own arrangement, and the visitor view uses the most recent or a merged layout (consult your operator about your instance's setting).
- Chips that you have not moved float in a gentle drift, slowly settling into a layout influenced by their relation lines (chips connected by a line are softly pulled towards each other). The drift stops once you drag a chip; from that moment on, the chip is pinned.

This is the canvas's small secret: the layout you see is partly the work of the simulation and partly the editorial choices you have made. Two galaxies whose editors have drawn no relations at all look like dust on the dot grid; two galaxies whose editors have drawn many look like constellations.

## Editing or deleting a relation

Hover a line; a small context menu appears with two options:

- **Edit note**: change the inline note attached to the line.
- **Delete**: remove the relation entirely.

Deletes are permanent at the line level (no undo within the canvas), but the chip endpoints remain on the canvas. You can re-draw a relation between the same two chips later; the new line is a fresh row in the underlying record, not a restoration of the old one.

## Renaming and merging keywords

Right-click (or long-press on touch) a chip to open its options:

- **Rename**: change the word. The rename applies to every wormhole carrying the keyword across every galaxy on the instance, because keywords are global by text. The chip's colour shifts to match the new text (colours are deterministic by the word).
- **Merge into…**: select another chip on the canvas to merge this keyword into. After the merge, every wormhole that carried the source keyword now carries the target keyword instead. The source chip disappears.
- **Delete**: removes the keyword from every wormhole that carried it on the instance.

These are sharp tools. Merging is the kindest of the three (no data loss; just relabelling), then renaming (also no data loss; the word changes but the connections stay), then deleting (the keyword goes away; the wormholes survive without it). Operate on a quiet day if a galaxy has many editors.

## Bulk reset

The canvas exposes two bulk-reset operations through the **?** help overlay:

- **Reset all chip positions** in this galaxy: every chip goes back to a uniform default position. Use when the layout has accumulated cruft and you want to start over.
- **Reset all relations** in this galaxy: deletes every relation line in this galaxy. The chips remain. Use when you want to re-draw the conceptual map from scratch.

Both are scoped to the **current galaxy**; they do not touch other galaxies.

## When to use the canvas (and when not to)

The canvas is most useful when:

- A galaxy's keywords carry a structure worth showing (some are siblings, some are opposites, some are scoped specifically to a sub-region of the content).
- An editorial point lives **between** keywords rather than inside a single one. *Native* on its own is just a label; *native* drawn close to *salt-tolerant* with a note ("most natives here tolerate salt") is an observation.
- You want a working surface to think on. The canvas is a sketchpad for the galaxy's vocabulary as well as a public artefact.

The canvas is **less useful** for:

- Tiny galaxies (under ten wormholes; the chip count is usually too small for a layout to be interesting).
- Galaxies whose keywords are mostly proper nouns or unique to one wormhole; the canvas is for relationships *between* concepts, and one-off concepts have nothing to relate to.

If a galaxy never feels like it warrants opening the canvas, that is a fine outcome. The canvas is offered, not required.

## Things worth knowing

- **The canvas saves every change automatically.** There is no Save button. The **Saving…** / **Ready** indicator at the top right reflects the persistence state.
- **No undo within the canvas surface.** A wrong move is corrected by another move; an accidental delete by re-drawing the line. If something goes badly wrong, ask your operator about a snapshot.
- **The visitor does not see the chips directly.** The canvas is an editor's surface; what visitors see in the 3D scene is influenced by the keyword arrangement (which wormholes share keywords; which chips have relations), but visitors do not look at the chip grid itself.
- **Line notes are surfaced to visitors only on hover** in the related-wormholes panel (chapter 10 has the visitor-side detail). The note is part of the public artefact; write it for a future reader, not for yourself.
