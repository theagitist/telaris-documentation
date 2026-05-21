# Introduction

This manual is for **editors**: the people who shape what a Telaris instance holds. If you author galaxies, place wormholes, link keywords, or curate the relationships between pieces of content, this manual is the day-to-day reference for how the editor surfaces work.

Operators (the people who run a Telaris instance) have their own manual, the **Admin Manual**, covering installation, federation, keys, backups, and the Pluriverse. There is overlap at the edges; pointers cross-reference between the two.

## What Telaris is, in one paragraph

Telaris is a three-dimensional, non-hierarchical archive. Content lives in **galaxies**: clusters of **wormholes**, which are the smallest units of content (a passage, an image, a video, a thought). Wormholes connect to each other through shared **keywords**, and the keywords themselves connect to each other through the **keyword canvas**. There are no folders, no parents, no breadcrumbs; the rhizome is the structure. Editors do not build a tree; they tend a thicket.

## Who this manual is for

You are an editor if you have been given login credentials to the editor surface of a Telaris instance and asked to add or organize content. You do not need to know PHP, MySQL, or anything about federation to use this manual. You will need to know the URL of your instance, your editor username, and your password.

> [!note] What you do not need
> You do not need to know how the Pluriverse, the federation between instances, or the keyrings work. Those belong to the operator. If something feels like it crosses into operator territory (a peer goes "outdated", a key rotation message appears, a federation pull fails), this manual will point you at the right place to ask for help; you will not need to fix it yourself.

## How this manual is organized

This is a working draft. The full structure will land in the next iteration; for now, expect the manual to cover, in order:

1. Getting into the editor.
2. Galaxies (creating, naming, framing).
3. Wormholes (text, images, video, PDFs).
4. Keywords (assigning, weighting, aliasing).
5. The keyword canvas (the editor's relational drawing surface).
6. Cross-galaxy work (multigalaxy views, when an idea belongs to two places).
7. Snapshots and versioning (what is reversible, what is not).
8. Editorial sovereignty (when *not* to apply a keyword, when to refuse a connection).
9. Working alongside federation (what changes when your instance is part of the network).

Each section opens with what the surface does, then walks through it with screenshots, and closes with a "things to know" list (gotchas, hidden behaviours, current limitations).

## Conventions

- **Menu paths** appear like this: <span class="menu-path">Admin &rarr; Galaxies &rarr; New galaxy</span>.
- **Buttons and form fields** appear in bold: **Save**, **Title**, **Visible to visitors**.
- **Keyboard shortcuts** use <kbd>Cmd</kbd> + <kbd>S</kbd> (or <kbd>Ctrl</kbd> + <kbd>S</kbd> on Windows / Linux).
- Code, identifiers, URLs, file paths, and database column names appear in `monospace`.

> [!tip] If you find a mistake
> This manual ships from the same repository the editor surface itself does. If a screenshot is wrong, a button is named differently, or a step is missing, tell the operator of your instance; the change lands in the next build.
