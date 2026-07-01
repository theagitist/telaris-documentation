# Keywords

Keywords are short labels you attach to wormholes. They are how Telaris connects content without folders. A keyword is the difference between a galaxy that is a *list* and a galaxy that is a *web*; everything else, in the editor's day-to-day, is built on top.

This chapter covers assigning keywords from inside the wormhole modal, the chip palette, and how to work across many wormholes at once. The keyword **canvas** (the relational drawing surface for keywords) is its own chapter (8).

## Assigning keywords

Keywords are assigned inside the wormhole modal, in the **Keywords** field next to the wormhole's name (see chapter 5 for the full modal). The field is a chip input:

- Type a keyword and press **Enter** or **comma** to add it as a chip.
- Click the **×** on a chip to remove it.
- The same keyword can be added in any case; Telaris matches case-insensitively, so *native* and *Native* are the same keyword.

As you type, suggestions appear:

- Keywords already used in **this galaxy** appear first.
- Keywords used in **sibling galaxies** (galaxies that share the `[bracket]` prefix of your current galaxy) appear next.
- Other recent keywords appear last.

Accepting a suggestion is the same as typing the word fully. Telaris does not require you to use suggestions; you can always type a fresh keyword, in which case the new keyword joins the galaxy.

## Choosing keywords well

The most important keyword decision is **how few to use**. A wormhole tagged with three carefully chosen keywords is more legible than one tagged with twenty. Every keyword you add is a connection to every other wormhole carrying the same word; if the connection is not meaningful, the visitor's path through the galaxy gets noisier.

Some practical rules:

- **One per quality the wormhole genuinely embodies**. *Native* on a plant that is native; *edible* on one that is genuinely eaten. Not *plant* on every wormhole in a plant galaxy; that keyword carries no signal.
- **Reuse before inventing.** When two editors describe the same idea with different words (*medicinal* and *healing*), the conceptual link goes dark. Look at the autocomplete; if a word close to yours already exists, prefer it.
- **Avoid keywords you would never search.** A keyword nobody (visitor or editor) would type into a search box is one that does no work.

There is no review queue and no central vocabulary. Each editor decides the keywords on each wormhole; the system trusts you. Chapter 13 talks about editorial sovereignty in detail.

## The chip palette

Each keyword gets a deterministic pastel colour, chosen by the keyword's text. The colour is the **same** for that word across every galaxy on your instance: visitors who learn that *native* is the green-ish chip in one galaxy will recognise it instantly in another.

This is also why renaming a keyword changes the colour: the colour is keyed to the text, not to an internal id. If you rename *medicinal* to *healing*, the chip's colour shifts. (Practically: rename rarely; merging is a cleaner operation.)

## Editing keywords on an existing wormhole

Open the wormhole's Edit modal (chapter 5). The Keywords field shows the existing chips. Add chips as above; remove with the ×; save. Changes apply on the visitor's next page load.

## Acting on many wormholes at once

To find and act on every wormhole carrying a given keyword, type the keyword into the search box on the editor home. The list narrows to the matching wormholes, and you can open each one's actions menu to edit, move (by changing its galaxy in the Edit modal), or delete it. Searching first, then acting per wormhole, keeps you looking at exactly what you are about to change, rather than triggering a single sweeping action against a count you cannot see.

## Aliases (per-galaxy synonyms)

Telaris's keyword model treats two galaxies' use of the same word as the **same keyword**. There is no per-galaxy alias mechanism in v1 of the rollout; if you want *medicinal* in one galaxy to be treated as the same keyword as *healing* in another, the practical move is to **rename one to match the other** so both galaxies converge on a single word.

If the editorial intent is precisely the opposite (a word that means different things in two galaxies and should not connect them), use different words in each galaxy. Conceptual precision is more useful than syntactic cleverness here.

## Keyword counts in the visitor view

When the galaxy's **Keyword chips** discovery feature is on (chapter 4 covers the toggle; chapter 10 covers the resulting visitor experience), the visitor sees a row of chips at the bottom of the 3D scene showing the most-used keywords. Clicking a chip dims every wormhole that does *not* carry that keyword.

This is a soft filter (it does not remove wormholes from the scene, just dim them), and it is one of the main ways visitors navigate a galaxy without instructions. The keywords you choose are the navigation: clear keywords mean a clear scene.

## Things worth knowing

- **A wormhole without keywords is allowed but quiet.** Visitors can still reach it through name search or by 3D-clicking; they will not reach it through the keyword chip layer. Use zero keywords when the wormhole's role is purely solitary.
- **Keyword names are searched in the editor home search box** alongside wormhole names and descriptions. Searching for a keyword is the fastest way to audit which wormholes carry it.
- **Renaming a keyword updates it everywhere on the instance.** Renaming *medicinal* renames it in every galaxy that uses the word. There is no per-galaxy rename.
- **Deleting a keyword removes it from every wormhole that carries it.** The wormholes survive; the keyword chip drops off them. Deleting a keyword (through the keyword canvas, chapter 8) removes the word; deleting a wormhole (through its row actions menu, chapter 5) removes the content. They are different operations.
- **There is no maximum number of keywords per wormhole**, but practical legibility suggests three to seven is plenty. Past ten, the chip strip on the info card starts to wrap awkwardly.
