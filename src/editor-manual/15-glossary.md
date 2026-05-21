# Glossary

Every named concept in the editor manual, in one place. Dictionary-style; each entry tells you what the term means and which chapter walks through it.

**Accentuate**. A per-wormhole flag (chapter 5) that makes the wormhole render larger and more prominent in the 3D scene. Often paired with auto-tour for narrative emphasis.

**Audio**. A media type a wormhole can carry, independent of the primary visual. Optional autoplay and loop toggles. Chapter 6.

**Auto-tour**. A self-running tour through a galaxy (chapter 11), configured in the galaxy settings Discovery section. Modes: manual, idle, immediate.

**Bracket prefix**. A naming convention (e.g., `[exhibit] Room A`) that groups galaxies into a visible family in the picker and a `/[exhibit]` union URL. Chapter 12.

**Bulk by keyword**. A modal (chapter 7) that operates on every wormhole in the current galaxy carrying a chosen keyword: delete them in bulk, or move them in bulk to another galaxy.

**Canvas**. Short for the keyword canvas (chapter 8). The drawing surface where editors lay out keyword chips and draw relationships between them.

**Chip**. The pastel pill that represents a keyword in the editor UI. Each keyword has a deterministic colour by text; the colour is the same everywhere on the instance.

**Cluster**. An admin-managed grouping of galaxies that behaves like a galaxy in its own right. Editors do not author clusters; they see them in the picker if they have access. Chapter 12 covers union behaviour generally.

**Cosmic theme**. The default visual theme for a galaxy: stars, planets, rockets. Other themes: Simple, Abstract, Rectangles, Stripes, Tech. Chapter 4.

**Description**. The body text of a wormhole, displayed inside the info card. Supports basic markdown. Chapter 5.

**Discovery**. The section of the galaxy settings modal that toggles visitor-side features: auto-tour, idle spotlight, keyword chips, related wormholes, 2D view. Chapter 4 (modal) and chapter 10 (visitor side).

**Dwell time**. The number of seconds an auto-tour pauses at each wormhole before moving on. Chapter 11.

**Editor**. The role assigned to a user who authors content. Distinguished from the operator (who runs the instance). This manual is written for editors.

**Editorial sovereignty**. The principle that editors decide what goes into a galaxy and how it is tagged, without a review queue or central vocabulary. Chapter 13.

**Galaxy**. The largest unit an editor works with. A collection of related wormholes plus a framing, a theme, and a set of tags. Chapter 4.

**Galaxy tag**. A short label (chapter 4) added to a galaxy in its settings modal. Two galaxies with the same tag form a union; visitors at `/tag/<slug>` see both. Chapter 12.

**Galaxy union**. A view that shows the wormholes of two or more galaxies together while keeping each wormhole in its source galaxy. Reached via galaxy tags, bracket prefix, or an explicit `?galaxies=` URL. Chapter 12.

**Icon**. The 3D representation of a wormhole in the scene. By default, the galaxy theme's icon; can be overridden per-wormhole (chapter 6).

**Idle spotlight**. A Discovery feature (chapter 10) that gently highlights a different wormhole every N seconds when the visitor has been idle.

**Image attribution**. A free-text field next to an uploaded image (chapter 6) for credit or licence notes. Travels with the image into the info card footer.

**Info card**. The panel that opens over the 3D scene when a visitor clicks a wormhole. Contains the wormhole's name, primary visual, description, audio, keywords, and Open Link button. Chapter 10.

**Instance**. A single deployment of Telaris at a web address. Your instance is the one whose URL is in your address bar. Multiple instances may federate (cross-instance content is operator territory).

**Keyword**. A short label attached to wormholes (chapter 7). Two wormholes sharing a keyword are connected. Keywords are case-insensitive and global by text across the instance.

**Keyword canvas**. The full-viewport drawing surface (chapter 8) where editors lay out keyword chips and draw relationship lines between them. Desktop-only.

**Keyword chips**. (1) The pastel pills shown inside the editor for keyword editing. (2) The Discovery feature that paints a chip strip at the bottom of the visitor scene; visitors click a chip to dim wormholes that do not carry the keyword. Chapter 10.

**Loop**. (1) The audio loop toggle: an audio track restarts after it finishes. (2) The tour loop toggle: the auto-tour cycles back to the start after the final wormhole. Chapter 6 and chapter 11.

**Manual**. (1) This document. (2) An auto-tour start mode where the visitor must press Play. Chapter 11.

**Media**. The collective name for image, video, audio, PDF, and embed-code attached to a wormhole. Chapter 6.

**Multigalaxy**. The general name for views that show more than one galaxy at once. Achieved via tags, bracket prefix, or explicit URL list. Chapter 12.

**Multigalaxy view**. A union of multiple galaxies that visitors can browse as if it were one scene, with each wormhole keeping the visual theme of its source galaxy. Chapter 12.

**Object**. The default Wormhole type. An Object wormhole carries content (description, media). Contrast with Portal. Chapter 5.

**Operator**. The role of the person who runs the Telaris instance. Editors do not perform operator tasks (installation, federation, key management). When this manual says "ask your operator," this is who.

**PDF**. A document media type. Embedded in the visitor's info card with an in-page reader. Chapter 6.

**Per-peer keys, Pluriverse, federation**. Operator-domain concepts. Not relevant to editors; covered in the Admin Manual.

**Portal**. A wormhole whose type is Portal: instead of holding content, it points to another galaxy. Visitors who open it travel through. Chapter 9.

**Preview tour**. A button next to the auto-tour configuration (chapter 11) that opens a visitor view in a new tab with the tour running, so you can check the configuration before saving.

**Primary visual**. The single image, video, or PDF a wormhole carries. Mutually exclusive (the three tabs share a slot). Audio and embed code are separate. Chapter 6.

**Random N**. An auto-tour node-selection mode: pick N wormholes at random each session. Chapter 11.

**Related wormholes**. A Discovery feature: the info card shows up to five wormhole chips that share at least one keyword with the open wormhole; clicking jumps to the related wormhole. Chapter 10.

**Slug**. The short URL-safe form of a galaxy or wormhole name. Galaxies have a slug visible in the URL bar. Slugs do not change once set.

**Snapshot**. An operator-side backup of the entire instance. Editors do not take snapshots; the Admin Manual covers them.

**Sovereignty**. See *Editorial sovereignty*.

**Source community**. A community whose work is hosted in a Telaris galaxy. The community's consent is the editorial floor; withdrawal of consent is final. Chapter 13.

**Tagged keywords**. An auto-tour node-selection mode: visit only wormholes carrying one of a chosen set of keywords. Chapter 11.

**Theme**. The visual style of a galaxy: cosmic, simple, abstract, rectangles, stripes, tech. Chosen in the galaxy settings modal. Chapter 4.

**Tour**. See *Auto-tour*.

**Union**. See *Galaxy union*.

**Use as wormhole icon**. A per-wormhole toggle that renders the wormhole's image as its 3D scene icon, replacing the theme's default. Chapter 6.

**View** (button). A button next to the galaxy picker that opens the current galaxy in visitor mode, in a new tab. Chapter 4.

**Visitor**. The reader of a galaxy. A visitor reads the content the editor publishes; they do not see the editor surface. The visitor view is what shows after a click on the View button or a direct URL.

**Visitor view**. The 3D (or 2D) scene that visitors see. Driven by the editor's choices in the wormhole modal and the galaxy settings modal. Chapter 10.

**2D view**. An alternative visitor surface (chapter 10) that renders the galaxy as a flat grid of wormhole chips. Toggled by the visitor; the toggle is enabled on the galaxy settings Discovery section.

**Wormhole**. The smallest unit of content in Telaris. A single passage of text, image, video, PDF, audio, or composite. Chapter 5.

**Wormhole type**. A field in the wormhole modal: Object (default, carries content) or Portal (carries a destination galaxy). Chapter 5 and chapter 9.
