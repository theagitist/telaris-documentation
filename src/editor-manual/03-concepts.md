# Concepts

Six words name almost everything in Telaris. Knowing them is enough to read the rest of this manual. Each gets a short page here, with an example drawn from the same sample galaxy ("Coastal plants") used in every screenshot in the rest of the manual.

The concepts are *galaxy*, *wormhole*, *keyword*, *portal*, *keyword canvas*, and *tour*. They build on each other; read them in order the first time, then come back for reference later.

## Galaxy

A **galaxy** is a collection of related content. It is the largest unit you work with as an editor. A galaxy has a name, an editorial framing (the short paragraph that opens it for visitors), a visual theme, and any number of wormholes inside it.

A galaxy is **not** a folder. There is no hierarchy; you do not put galaxies inside other galaxies. Galaxies sit beside each other; the relationships *between* galaxies are made by portals and by shared keywords, not by nesting.

> [!example] In the demo
> "Coastal plants" is one galaxy. It holds twelve wormholes (Beach Strawberry, Sea Lavender, Pacific Wax Myrtle, and so on) plus one portal to a second galaxy called "Tide pools".

Galaxies are the unit that visitors arrive at. A visitor's URL bar typically reads `.../coastal-plants`; that is the slug of the galaxy they are inside. Chapter 4 covers creating and configuring galaxies.

## Wormhole

A **wormhole** is the smallest unit of content in Telaris: a single thing the editor wants the reader to see, hear, or read. Most wormholes are about one item: a plant, a photograph, a passage of text, a recording, a film clip.

A wormhole has:

- a **name** (visible everywhere),
- a **description** (the body text shown when a visitor opens it),
- optional **media** (an image, an audio file, a video URL, a PDF, an embed),
- a set of **keywords** that connect it to other wormholes.

A wormhole lives inside exactly one galaxy at a time. If the same idea belongs in two galaxies, you do **not** copy the wormhole; you let the two galaxies share a keyword, or you place a portal. Chapter 12 covers multigalaxy work.

> [!example] In the demo
> "Beach Strawberry" is a wormhole. Its description tells the visitor what the plant looks like and where it grows; its keywords are *native*, *edible*, *ground-cover*, *perennial*, *salt-tolerant*; it has no media attached yet. Chapter 5 walks through authoring wormholes.

The word "wormhole" carries a specific image: each one is a small opening into a larger conversation. The reader steps through; on the other side is the description, the media, and the keywords that lead to the next opening.

## Keyword

A **keyword** is a short label you attach to wormholes. Telaris uses keywords for two purposes, both important:

1. **Connection.** Two wormholes that share a keyword are reachable from each other. The keyword is the conceptual bridge.
2. **Discovery.** Visitors can filter, search, and follow keyword chips to see what else has been tagged with the same word.

A keyword belongs to a galaxy (the canonical place it lives), but **the same word, used in another galaxy, is the same keyword**. Two galaxies that both tag wormholes with *native* connect through that shared word; visitors who follow *native* in one galaxy can find *native*-tagged wormholes in the other.

> [!example] In the demo
> *native* is a keyword applied to eight different wormholes in the coastal plants galaxy. *invasive* is applied to three. *intertidal* is applied across both demo galaxies: it links Sea Palm (in coastal plants) to Ochre Sea Star and other animals (in tide pools).

Keywords are the load-bearing material of a Telaris galaxy. They do most of the relational work that, in a hierarchical archive, would be done by folders and breadcrumbs. Chapter 7 covers assigning and shaping keywords.

## Portal

A **portal** is a special kind of wormhole. Instead of holding content of its own, a portal points to **another galaxy**. When a visitor opens a portal, they travel through it: the scene fades, a new galaxy loads, the portal becomes the doorway between the two.

Portals are how you move readers between galaxies on purpose. A keyword shared across galaxies is a *passive* connection (the reader can follow it if they choose). A portal is an *active* connection (the editor says: from here, go there).

> [!example] In the demo
> The coastal plants galaxy holds a portal wormhole called "To the tide pools". A visitor who opens it lands inside the tide pools galaxy, where they meet Ochre Sea Star, Giant Green Anemone, and the rest.

Portals are not bidirectional. If you want the visitor to be able to come back, place a corresponding portal in the destination galaxy that points the other way. Chapter 9 covers portals in detail.

## Keyword canvas

The **keyword canvas** is a drawing surface, separate from the wormhole list, where the editor lays out the keywords of a galaxy and draws relationships between them by hand. Each keyword appears as a coloured chip; you drag the chips around to compose; you draw lines between chips to record that those two keywords belong together; you can attach a short note to any line you draw.

The canvas does not replace the wormhole list; it complements it. The wormhole list is where you author content one wormhole at a time. The canvas is where you author the conceptual map of an entire galaxy.

> [!example] In the demo
> On the coastal plants canvas, the chips for *native* and *salt-tolerant* sit close together, with a line drawn between them and a note that reads "most natives here tolerate salt." The chips for *invasive* and *native* sit on opposite sides of the canvas, no line; the absence of a connection is also an editorial choice.

The canvas is a desktop-only surface (it does not currently work on phones). Chapter 8 walks through every part of it.

## Tour

A **tour** is a curated path a visitor can take through a galaxy. The editor picks the start, picks the order, sets a dwell time at each stop, and decides whether the tour loops back to the beginning or simply ends. Visitors can press a Play button to start the tour, or the tour can run on its own when the visitor has been idle for a while.

A tour is not a separate object: it is a *configuration* of an existing galaxy. The wormholes the tour visits are the ones already in the galaxy; the tour is what tells the scene which order to visit them in, and how long to sit at each one.

> [!example] In the demo
> The coastal plants galaxy could host a tour that visits, in order, Beach Strawberry, Sea Rocket, Wild Cucumber, Beach Pea, Yellow Bush Lupine, all of which share *edible* or *nitrogen-fixer*. The visitor presses Play; the scene drifts from one to the next with a five-second pause at each; at the end, it returns to Beach Strawberry and stops.

Chapter 11 covers tours; chapter 10 covers all the other visitor settings that interact with them.

## How the concepts fit together

A galaxy holds wormholes. Wormholes carry keywords. Keywords connect wormholes, both within a galaxy and across galaxies that share words. Portals are wormholes that take the visitor from one galaxy to another. The keyword canvas is the drawing where the editor authors the relationships between keywords. A tour is a curated path through a galaxy's wormholes.

If you understand those six relationships, you understand the editor's whole world. The rest of this manual is a series of practical walk-throughs of each one.
