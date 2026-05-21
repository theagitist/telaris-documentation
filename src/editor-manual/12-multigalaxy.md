# Multigalaxy work

Sometimes an idea lives across more than one galaxy: a research topic that spans two collections; an exhibit with several rooms; a series of related issues. Telaris is built so the wormhole stays in its home galaxy and the *combination* is a viewing arrangement, not a structural one. This chapter walks through the three ways you can compose galaxies, and when each is the right choice.

## The three composition paths

Telaris offers three ways to put multiple galaxies in a single view:

1. **Galaxy tags** (chapter 4): two galaxies that share a tag form a *galaxy union*. Visitors arrive at the union via `/tag/<tag-slug>` and see wormholes from every tagged galaxy together, with each wormhole keeping the visual style of its source galaxy.
2. **Bracket prefix grouping**: galaxies whose names start with the same `[bracket]` prefix automatically union at `/[bracket]`. A natural fallback to galaxy tags; the prefix is also the visual signal for editors browsing the picker.
3. **Explicit galaxy lists**: passing a comma-separated list in the URL `?galaxies=slug1,slug2` produces a one-off union. Useful for sharing a curated combination without changing the underlying galaxies.

The choice between the three depends on **how lasting the combination is**:

- *Lasting*: galaxy tags. The connection is editorial and persists across sessions.
- *Conventional*: bracket prefix. Useful when the galaxies are siblings by naming convention, not just by tag.
- *Ad-hoc*: explicit list. Useful for an email or a link that walks a reader through a specific combination once.

## Sharing wormholes without duplicating

The first instinct in many archive systems is to copy a wormhole into a second galaxy when an idea belongs in both places. Telaris is built against this instinct: copying creates two wormholes to maintain, two places to update when the source changes, two places to retract from when the source community withdraws consent.

The intended path is: leave the wormhole in its single home galaxy and let **shared keywords** connect it to others. Visitors who follow *intertidal* in galaxy A reach the *intertidal*-tagged wormholes in galaxy B; the wormhole's content lives in one place; the connection is computed from the keyword.

When that is not enough, the editor's options are, in order of how invasive each is:

1. **Add a galaxy tag** to both galaxies that share the theme. Visitors who follow the tag see the union.
2. **Place a portal** (chapter 9) from one galaxy to the other. The portal is a wormhole, but it is a small, deliberate one; it does not duplicate any content.
3. **Duplicate the wormhole** (chapter 5's actions menu). Only when the wormhole's content genuinely needs to live in two places (e.g., a galaxy is being seeded with material from another, with the editorial decision to lift rather than link). The duplicate is independent from then on; both copies need to be maintained.

The first two of these are almost always preferable to the third.

## The visitor experience of a union

A visitor who arrives at a galaxy-tag union (e.g., `/tag/coast`) sees:

- A scene composed of the wormholes of every galaxy carrying the tag.
- **Per-wormhole origin themes**: each wormhole renders with its source galaxy's theme, not a single unified theme. This is intentional; the visitor sees the union as the *meeting of galaxies*, not as a flattening of them.
- A galaxy strip or picker at the top showing the constituent galaxies, with the option to switch into a single one.
- The same Discovery features as any galaxy (keyword chips, related wormholes, etc.), now drawing from the union.

The visitor's URL bar stays at `/tag/<tag>` while they are in the union; clicking on a wormhole opens its info card without leaving the union.

## When to add a galaxy tag

A tag is editorial. The two questions to ask:

- **Is the relationship between these galaxies long-lived?** A tag persists; if the relationship is one-off, an explicit URL is cleaner.
- **Is the relationship symmetric?** A tag is symmetric (every galaxy carrying the tag is equally a member). If the relationship is directional (galaxy A is the introduction to galaxy B), a portal is more honest.

Examples that justify a tag:
- A series of related research collections.
- An exhibit with multiple rooms.
- A regional grouping (galaxies that all describe content from a single landscape, geography, or community).

Examples that do not:
- "Old galaxies I want to bundle for a one-time link" (use `?galaxies=...`).
- "Galaxies that share a few keywords" (use the keywords directly).

## When to use bracket prefix grouping

Telaris recognises galaxy names beginning with the same `[bracket]` as a family. A galaxy named `[demo] Coastal plants` and another named `[demo] Tide pools` share the prefix `[demo]`; visitors who follow `/[demo]` see both in union.

The bracket prefix is most useful when:

- You have several editors working on related galaxies, and the prefix signals to them that the galaxies are siblings.
- The galaxies form a family that you also want visible-as-a-family in the editor picker (the picker groups galaxies by bracket prefix).
- You want union behaviour without explicitly authoring a tag on each galaxy.

The bracket prefix and an explicit galaxy tag are not mutually exclusive; both apply if both are present.

## When to use an explicit galaxy list

Sometimes you want a one-off union for a specific moment: an email to a curator showing them a particular combination; a teaching link that walks a class through three galaxies side by side; a temporary exhibit that does not warrant a long-lived tag.

The URL form is `?galaxies=slug1,slug2,slug3` appended to your instance's address. The result is identical to a tag union, but the combination exists only as the URL itself.

This is the right tool for ad-hoc curation. It also serves as a quick sanity-check: if a particular combination of galaxies reads well as an explicit URL, you have a candidate for a permanent tag.

## Cross-instance multigalaxy

What about galaxies that live on **other** Telaris instances? That belongs to the operator's domain: cross-instance content arrives in your editor surface via federation or bridge imports the operator configures. From the editor's seat, federated and bridged galaxies behave like local galaxies (a galaxy is a galaxy is a galaxy), but the editor cannot author cross-instance unions; only the operator can set up the federation that makes them possible.

## Things worth knowing

- **A wormhole belongs to exactly one galaxy at a time.** Multigalaxy is a *viewing* concept, not a structural one. The wormhole's home galaxy is its single source of truth.
- **The visitor in a union view cannot tell which galaxy authored a given wormhole at first glance** beyond the visual theme of the wormhole's icon. The info card shows the source galaxy in the footer; the icon's theme is the at-a-glance indicator.
- **A galaxy in a union does not lose its individuality.** Visitors can click into a single galaxy from within the union view; the union is a viewing layer, not a merge.
- **Keywords are global by text** (chapter 7). The keywords on a wormhole in galaxy A are the same keywords as the same words on a wormhole in galaxy B. A union view consolidates the keyword chip strip across all constituent galaxies; clicking a keyword in the union filters the union.
- **The keyword canvas is still per-galaxy** (chapter 8). There is no "union canvas"; each galaxy holds its own keyword arrangement. The keywords themselves are shared (renaming or merging applies everywhere), but the chip layout and the drawn relations are scoped to each galaxy.
