# Tours

A tour is a curated path through a galaxy. The editor picks the start, picks the order, sets a dwell time at each stop, and decides whether the tour loops or ends. Visitors can start the tour themselves by pressing Play; or the tour can run on its own when the visitor has been idle; or the tour can begin the instant the visitor lands on the galaxy. This chapter walks through each path of authoring a tour and the practical considerations.

A tour is **a configuration of a galaxy**, not a separate object. Turning on the tour configures the existing wormholes to be visited in a chosen order; turning it off leaves the wormholes untouched. A galaxy can carry one tour configuration at a time; if you want two tours, you publish a copy of the galaxy with the second tour.

## Where you author it

A tour lives inside the **Galaxy settings** modal, in the Discovery section (chapter 4 introduces the modal; chapter 10 introduces the Discovery toggles).

![Galaxy settings modal at the Discovery section](assets/images/editor-manual/12-galaxy-discovery-section.png)

The Discovery section's first toggle is **Auto-tour**. Switching it on reveals the tour configuration fields:

- Start mode.
- Node selection.
- Dwell time at each stop.
- Loop on / off.

Below these is a **Preview tour** button.

## Start mode

Choose how the tour begins:

- **Manual**: a small **Play** button appears in the lower-right corner of the visitor's 3D scene. The tour begins when the visitor presses it. Use when the tour is an *offered* path, not a default one.
- **Idle**: the tour begins automatically after the visitor has been inactive for a configurable number of seconds. The idle threshold field appears below this option. Use when the galaxy is meant to be encountered both interactively (the visitor explores) and ambiently (the gallery wakes up when nobody touches it).
- **Immediate**: the tour starts the instant the visitor lands on the galaxy. The visitor can stop the tour at any time with the in-scene controls. Use for galleries whose intended experience is the tour itself; the editor's path is the canonical reading.

There is no right answer; each option suits a different editorial intention. Most authored galaxies start with **Manual** and graduate to **Idle** or **Immediate** as the editor finds a path worth defaulting to.

## Node selection

Choose which wormholes the tour visits, and in what order:

- **All**: every wormhole in the galaxy, in the order they were created. The simplest selection; useful for short galaxies where every wormhole carries equal weight.
- **Accentuated only**: only wormholes flagged Accentuated. Use when you want some wormholes to be on the tour and others to remain reachable but not foregrounded. The Accentuated flag is set per wormhole (chapter 5).
- **Random N**: picks N wormholes at random each session. A field appears for N. Use for galleries that should feel fresh on revisit; the visitor sees a different slice each time.
- **Tagged keywords**: visits only wormholes carrying one of a chosen set of keywords. A keyword picker appears, similar to the keyword chip input on a wormhole modal. Use when you want a *thematic* tour (only wormholes tagged *medicinal*; only ones tagged *native*).

For tagged-keyword tours, the order in which wormholes are visited is the order in which they were created, filtered to the keyword set. There is no manual ordering field; if you need a strictly authored sequence, the order in which you create the wormholes is the order the tour will respect.

## Dwell time

A single number, in seconds, controlling how long the tour pauses at each wormhole before moving on. The dwell starts when the wormhole's info card opens; the next wormhole is selected when the dwell elapses.

A useful default is five to eight seconds; this is long enough for a visitor to read a short description and look at the image, short enough to keep momentum across a long tour. Wormholes with audio attached often deserve a longer dwell so the audio can resolve before the tour moves on; chapter 6 covers audio loop semantics.

The dwell is global to the tour; the editor cannot (yet) set a different dwell per wormhole.

## Loop

A single toggle:

- **On**: after the final wormhole, the tour returns to the first and continues. Use for ambient gallery installations where the visitor may wander in mid-cycle.
- **Off**: the tour ends quietly after the final wormhole; the scene returns to interactive mode and the visitor can explore freely. Use for narrative tours with a beginning and an end.

## Previewing a tour

Below the tour configuration fields, a **Preview tour** button appears. Selecting it opens the visitor view in a new tab with the tour running, regardless of whether you have saved the configuration. This is the right way to check timing, ordering, and dwell before publishing changes to visitors.

The preview reflects whatever you have entered in the modal, not what is currently saved. If you decide the preview is wrong, change the fields and select Preview again; the new tab updates.

## Tours and Accentuate

The Accentuate flag on a wormhole (chapter 5) overlaps with tour selection but is not the same thing. Accentuated wormholes are *visually larger* in the 3D scene regardless of whether a tour visits them. The **Accentuated only** node-selection option for the tour is one way to use the flag, but you can also Accentuate wormholes that are not in the tour and have a tour that includes wormholes that are not Accentuated.

The pattern that reads cleanest:

- Use Accentuate for wormholes that should stand out visually at all times.
- Use the tour to specify the *narrative path*, which may or may not overlap with the visual emphasis.

## Tours and the keyword canvas

A keyword-tagged tour (node selection set to *tagged keywords*) gives the editor a path through the galaxy that follows the keyword vocabulary the canvas authors. The two surfaces work together: choose the keywords the tour will follow on the canvas first, draw the relationships between them, then choose the tour to follow that thematic path on the visitor side.

The connection is editorial rather than structural; Telaris does not require the canvas to be populated before configuring a tour, but the resulting tour often feels more deliberate when the keyword vocabulary has been worked through.

## Things worth knowing

- **Auto-tour does not pause for audio.** If a wormhole has a 30-second audio track and the dwell is 8 seconds, the tour moves on at 8 seconds while the audio keeps playing in the background. To let the audio complete, lengthen the dwell.
- **The visitor can always stop the tour.** A Stop or Pause control appears during a running tour; the visitor can also click anywhere outside the info card to interrupt. Tours should feel offered, not forced.
- **Random-N tours change every session.** A visitor revisiting the page does not see the same N wormholes; the random selection re-rolls. Helpful for ambient feel; surprising if you expected a stable sequence.
- **Tagged-keyword tours follow the union of the chosen keywords.** A tour set to keywords *native* and *edible* visits every wormhole tagged with **either** *native* or *edible* (or both); it does not require both.
- **Tours are scoped to the current galaxy.** A tour cannot visit wormholes in another galaxy; for cross-galaxy paths, use portals (chapter 9).
- **The 2D view (chapter 10) interacts with tours gracefully.** A visitor in 2D mode sees the tour as a sequence of highlighted chips, not as camera motion. The dwell still applies; the visual is just flatter.
