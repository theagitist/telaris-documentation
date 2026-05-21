# Portals

A portal is a special kind of wormhole. Instead of carrying its own content, it carries a destination: another galaxy. A visitor who opens a portal travels through it. The scene fades, a new galaxy loads, the portal closes behind them. Portals are how an editor builds intentional bridges between galaxies.

This chapter covers when to use a portal versus a shared keyword, how to create one, and the small set of editorial conventions that keep a portal network legible.

## When a portal is the right tool

Telaris already gives you two ways to connect content across galaxies:

1. **Shared keywords**: a wormhole in galaxy A and a wormhole in galaxy B both tagged *intertidal* form a *passive* connection. A visitor who follows *intertidal* in either galaxy lands on a view that shows both.
2. **Galaxy tags**: galaxy A and galaxy B sharing the tag *coast* create a union; visitors who follow `/tag/coast` see both galaxies' wormholes together.

A portal is a third kind of connection, and a much more *active* one: the editor says, in effect, *from this wormhole, go there now*. It is the right tool when:

- The connection is **directional and deliberate**. A shared keyword is a network; a portal is an arrow.
- The destination galaxy is a **continuation of the conversation**, not just a related topic. The reader should leave their current galaxy and arrive in another, not browse both at once.
- You want the portal itself to **show up in the 3D scene** as a navigable object. A portal renders as a distinct 3D node; visitors can recognise it and click it deliberately.

If none of those are true, a keyword or a galaxy tag is usually a better choice.

## Creating a portal

A portal is a wormhole whose Wormhole type is set to **Portal**. From the New Wormhole modal:

![New Wormhole modal with Wormhole type set to Portal: a Target Galaxy dropdown appears](assets/images/editor-manual/11-portal-type-selector.png)

Steps:

1. Open **New Wormhole** from the editor home (or open an existing wormhole's edit modal and change its type).
2. Set **Wormhole type** to **Portal**. A **Target Galaxy** field appears, with a dropdown listing every galaxy you have access to.
3. Pick the destination galaxy from the dropdown. The button next to it, **Create New Galaxy**, is a shortcut for the case where the destination does not exist yet; selecting it lets you author the destination inline. Most of the time, you pick an existing galaxy.
4. **Name** the portal something readable. A portal is a wormhole, so the name appears in lists and in the 3D scene; choose a name that signals the journey, not just the destination. *To the tide pools* reads better than *Tide pools*.
5. Add a **Description** if you want a short paragraph to appear when the visitor opens the portal's info card. The description is shown briefly before the journey to the destination galaxy begins; treat it as a threshold sentence.
6. Optional: assign a few **keywords**. Portals can carry keywords like any other wormhole; this helps the portal surface in keyword-based discovery.
7. Save.

The portal now appears in the wormhole list with a **Portal** tag in the Type column, and as a distinguishable node in the 3D scene.

## What visitors experience

A visitor who clicks a portal in the 3D scene sees:

- The portal's info card opens, just like any other wormhole.
- The card shows the portal's name, the description, and (depending on the instance's settings) a **Travel** or similarly named call-to-action button.
- Activating the call-to-action closes the current galaxy and loads the destination.
- In the destination galaxy, the visitor arrives at the galaxy's entrance (the default starting position), not at a specific wormhole.

The visitor can use the browser's Back button to return to the origin galaxy. Telaris does **not** automatically place a return portal in the destination galaxy; if you want the journey to be round-trip, you need to place a matching portal manually.

## Round-trip portals

When you place a portal from A to B, consider whether you also want a portal from B back to A. The two are independent: each is a wormhole in its own galaxy. There is no "linked portals" concept.

The decision is editorial:

- **Yes, place a return portal** when the two galaxies are equal partners in a conversation; visitors arriving in B should be invited back to A as naturally as they were invited from A to B.
- **No, leave the return implicit** when the visitor's natural path is one-way (A is the framing galaxy; B is the answer; the visitor returns through the browser, if at all).

If you place a return portal, name it for the destination it leads to, not for "going back." *To the coastal plants* reads better than *Back* or *Return*.

## Portals and the keyword canvas

A portal's keyword chips appear on the keyword canvas like any other wormhole's. A portal tagged *intertidal* contributes to the *intertidal* connection web. Sometimes editors tag portals with a specific keyword like *portal* so they can be filtered out of keyword-driven discovery (some visitors may not want portal-heavy hops); in our demo galaxy, the portal wormhole carries the tag *portal* for exactly that reason.

## Things worth knowing

- **A portal can only target one galaxy at a time.** If you want a "hub" that fans out to many galaxies, the answer is many portals, not one. You can place several portals in a single galaxy, each pointing somewhere different.
- **The target dropdown lists only galaxies you can edit.** If the galaxy you want to portal to is on another instance, that is federation territory and is the operator's domain; the editor surface does not author cross-instance portals.
- **A portal can be retargeted** by editing it and choosing a different galaxy in the Target Galaxy field. Visitors who had bookmarked the portal will continue to land on whichever galaxy is now selected. Plan for that when changing destinations after publication.
- **A portal targeting its own galaxy** is technically allowed but functionally pointless: the visitor lands back where they came from. The editor UI will not stop you, but the result is a no-op.
- **Deleting a portal removes the wormhole entirely.** The destination galaxy is unaffected; only the connection is gone. The destination's own portals (if any) still work.
- **Portals carry no media.** They have a name, a description, and keywords, plus the target galaxy. The image, video, audio, and PDF fields are still in the modal but should be left empty for portals; if you fill them, they are simply ignored by the portal's visitor experience.
