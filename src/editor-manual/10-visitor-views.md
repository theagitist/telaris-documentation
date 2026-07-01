# Visitor views

The editor's work is read by visitors. Almost every editorial choice you make eventually shows up on the visitor side, either directly (the description, the media, the keywords) or indirectly (the relationships drawn on the keyword canvas, the way wormholes are tagged). This chapter is your map of what visitors see, and the editor-side switches that shape it.

The visitor view is reached by following any visitor URL of your instance: typically the galaxy slug, sometimes with no slug at all (your operator can confirm the entry path).

![Visitor 3D scene for the Coastal plants demo galaxy](assets/images/editor-manual/13-visitor-scene.png)

## The 3D scene

The default visitor view is a three-dimensional scene where each wormhole is a small object floating in space against the galaxy's chosen theme background. The visitor's mouse rotates the view; scrolling or pinching zooms; clicking on a wormhole opens its info card.

What you choose as an editor that shows here:

- **The galaxy's theme** (chapter 4) controls the look: which icons render the wormholes, what the background looks like, what the lighting feels like.
- **The Use-as-wormhole-icon toggle** on each wormhole (chapter 5) decides whether that wormhole renders as its image (when on) or as the theme's default icon (when off).
- **The Accentuate flag** on a wormhole renders it larger and more prominent in the scene.
- **The Show Keywords flag** prints the wormhole's keywords as floating labels next to the icon.

These four choices interact: a galaxy of Accentuated, image-iconified, keyword-displaying wormholes is a busy scene; a galaxy of theme-iconified, plain wormholes is a quiet one. There is no "right" mode; pick the visual register that matches the content's editorial register.

## The info card

A visitor who clicks a wormhole sees its **info card** open over the scene. The card contains, in order:

- The wormhole's **name** at the top.
- The **primary visual** (image, video, or PDF) below the name, sized to the card.
- The **description** as a body paragraph.
- The **audio player** if audio is attached.
- The **embed code** if one was supplied.
- A row of **keyword chips** at the bottom of the card, each clickable.
- The **Open Link** button if the wormhole carries a URL.

When the visitor clicks a keyword chip on the info card, the scene dims wormholes that do not carry that keyword. The card closes. This is one of the main ways visitors navigate by tags rather than by name.

## The Discovery toggles

The galaxy settings modal carries a Discovery section (chapter 4 introduced the modal; here is what each toggle does on the visitor side):

![Galaxy settings modal scrolled to the Discovery toggles](assets/images/editor-manual/12-galaxy-discovery-section.png)

Each toggle is off by default. Turn one on when you want the corresponding feature.

### Auto-tour

A self-running tour through the galaxy. When on, additional options appear:

- **Start mode** (manual, idle, immediate):
  - **Manual**: the visitor must press a Play button to start the tour.
  - **Idle**: the tour starts automatically after the visitor has not interacted with the scene for a number of seconds (configurable).
  - **Immediate**: the tour starts as soon as the visitor lands on the galaxy.
- **Node selection** (all, accentuated, random N, tagged keywords):
  - **All**: the tour visits every wormhole in the galaxy in order.
  - **Accentuated only**: visits only wormholes flagged Accentuated.
  - **Random N**: picks N wormholes at random each session; the number is configurable.
  - **Tagged keywords**: visits only wormholes carrying one of a chosen set of keywords. The list of keywords is set in a sub-field that appears when this option is selected.
- **Dwell time** in seconds at each stop, before the tour moves to the next.
- **Loop**: when on, the tour cycles back to the beginning after the final stop; when off, it ends quietly.

A **Preview tour** button appears next to the Auto-tour fields; selecting it opens the visitor view in a new tab with the tour running, so you can check the timing without saving the configuration.

Chapter 11 walks through tours in more depth.

### Idle spotlight

When on, the scene gently spotlights a different wormhole every N seconds when the visitor is idle. Unlike auto-tour, it does not move the camera or open info cards; it just brings one wormhole forward, softly, like a museum changing the room lighting.

Two settings:

- **Idle threshold** in seconds before the spotlight begins.
- **Selection** (all, accentuated only).

Idle spotlight is well-suited to ambient-feeling galaxies (a poem cycle; a sequence of photographs); it gives the room something to do when the visitor has stopped clicking.

### Keyword chips

When on, the scene paints a strip of pastel chips at the bottom of the visitor's screen, one chip per most-used keyword in the galaxy. Visitors can click a chip to dim every wormhole that does not carry it.

Use when the galaxy has a strong keyword vocabulary that visitors would naturally browse by; turn off when keywords are too granular or too numerous for chips to be useful.

### Related wormholes

When on, an info card opens with up to five **related** wormhole chips at the bottom: other wormholes (in this or sibling galaxies) that share at least one keyword with the open one. The visitor can click a chip to jump directly to the related wormhole.

This is the main way visitors travel laterally through a network without opening a portal. Turn it on when you want the visitor to discover the web; turn it off when you want the visitor to stay focused on one wormhole at a time.

### 2D view

When on, a small **3D / 2D** toggle appears at the top of the visitor's screen. Switching to 2D collapses the scene into a flat map of wormhole chips: each chip is the wormhole's icon plus name. The 2D view is faster to load and easier to scan; some visitors prefer it for finding a specific wormhole quickly.

The 2D map can be **zoomed and panned** (scroll or pinch to zoom, drag to pan), and a **Fit** control returns every wormhole to view at once, so nothing stays stacked off-screen no matter how many wormholes the galaxy holds. When more than one galaxy is in view (a galaxy union, chapter 12), the galaxy list beside the map dims the galaxies you are not pointing at, and each wormhole chip carries its galaxy's name as a prefix so you can tell same-named wormholes apart.

The visitor's choice between 3D and 2D persists in their browser (you do not have to keep choosing).

## Provenance footers and attribution

When a wormhole's editorial provenance carries an attribution (`Image attribution`, source-community credit, or a federated mirror notice), the info card shows it as a small footer line below the description.

There is no global toggle to hide provenance footers; if your work credits a photographer or a source community, that credit appears whenever the wormhole is opened. Author attribution and source-community consent are first-class editorial concerns; chapter 13 covers the editorial discipline around them.

## Things worth knowing

- **The visitor sees what you have published, not your draft.** There is no "preview" mode separate from the published view; once you save a wormhole or a galaxy setting, the visitor's next page load reflects the change. To preview a change without affecting visitors, you would need to make the change in a galaxy that is not yet public.
- **The 3D scene runs in the visitor's browser.** Older devices or low-power computers may struggle with very dense galaxies. The 2D view toggle is the standard remedy.
- **Audio that autoplays may be blocked by the visitor's browser.** Most browsers do not allow audio to start without the visitor's interaction. If you turn on Autoplay (chapter 6) and a visitor reports no sound, this is the most likely cause; the visitor's first click on the page usually un-blocks the audio. A galaxy with a soundscape shows a small **sound on/off** control in the scene; the first time a visitor turns it on, the soundscape starts (the same browser gesture rule applies).
- **The Discovery toggles are independent of each other.** Auto-tour and idle spotlight can both be on at the same time (the spotlight kicks in if the tour ends or is not started). Pick the combinations that fit your editorial intent; the toggles do not gate each other.
