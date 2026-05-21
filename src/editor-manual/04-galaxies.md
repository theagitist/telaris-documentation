# Galaxies

A galaxy is a container, a vantage point, and an editorial position all at once. It is the unit your operator hands you when they say "you can edit here"; it is the unit visitors arrive at; it is the unit you frame, name, and shape. This chapter walks through creating a galaxy, configuring it, and the everyday operations on it.

## Selecting a galaxy

The **Current Galaxy** dropdown at the top of the editor home is how you pick which galaxy you are working in. *All my galaxies* shows wormholes from everywhere you have access; selecting a specific galaxy filters everything below to that one.

The first thing the dropdown teaches you is the shape of your editorial responsibilities: every galaxy listed is a galaxy you can edit. If a colleague's galaxy is missing, your operator has not assigned it to you. (Visitors of your instance see every public galaxy; editors only see the ones they are responsible for.)

When you pick a specific galaxy, three new buttons appear next to the dropdown:

![Editor home with a single galaxy selected: View, Settings, Canvas buttons appear](assets/images/editor-manual/03-editor-home-single-galaxy.png)

- **View** opens the galaxy in visitor mode, in a new tab. Use it whenever you want to check how a change reads from the visitor's seat.
- **Settings** opens the galaxy's configuration. Most of this chapter is about what is inside that modal.
- **Canvas** opens the keyword canvas, the relational drawing surface covered in chapter 8.

## Creating a galaxy

Whether you can create a new galaxy depends on your operator's setup; some instances let editors create galaxies freely, others reserve creation for administrators. If you have permission, the new-galaxy button is in the same row as the picker; if not, ask your operator and they will set one up for you.

When a new galaxy is created, it lands empty: zero wormholes, no keywords, default theme. The next step is to fill in its settings.

## Galaxy settings

Open the **Settings** button next to the picker. A modal opens:

![Edit Galaxy modal: Name, Tagline, Visual Theme, Tags, bulk actions, and discovery toggles](assets/images/editor-manual/04-galaxy-settings-modal.png)

The modal is the central place where you shape what a galaxy is and how it behaves. The fields, in order:

**Name** (required). The name visitors see in the galaxy picker and at the top of the scene. Galaxy names are not unique across the network, but two galaxies with the same name on the same instance are confusing; choose something readable and distinct. You can change a galaxy's name at any time.

**Tagline** (optional, short). A one-line description shown next to or below the galaxy name in the visitor's UI. The tagline does not appear in the 3D scene; its main audience is the picker and the public listing.

**Visual Theme**. A dropdown that picks the look of the 3D scene: *Cosmic* (stars, planets, rockets) is the default and the most common; other themes are *Simple*, *Abstract*, *Rectangles*, *Stripes*, and *Tech*. Pick the one whose vocabulary matches your content. The theme can be changed any time; the change applies to all visitors immediately, but does not alter what you authored, only how it is rendered.

**Tags** (optional). Short labels that group this galaxy with other galaxies. Two galaxies that share a tag form a *galaxy union*: visitors who follow the tag see wormholes from both at once, with each wormhole keeping the visual style of its source galaxy. Use tags when several galaxies are siblings in some larger arrangement. The Tags input autocompletes from tags you have used in your other galaxies and from tags shared by galaxies prefixed with the same `[bracket]`.

**Bulk wormhole actions**. Two buttons that apply a single setting across every wormhole in this galaxy at once.

- **Use images as icons (all wormholes)** sets every image-bearing wormhole to render its image as the 3D node instead of the theme's default icon. Useful when you have a galaxy of photographs and want the photos to *be* the scene.
- **Revert all to theme icons** undoes the above: every wormhole goes back to the theme's icon, regardless of whether it has an image.

These act in bulk; individual wormholes can still be flipped one at a time afterwards (chapter 5).

**Discovery toggles**. A set of switches at the bottom of the modal that control how the visitor experiences your galaxy. They are off by default; turn each one on when you want the corresponding feature. Each toggle is covered in chapter 10 (Visitor views) where the feature it controls is also shown.

Save the modal with **Save**; close without changes via **Cancel** or by clicking outside the modal. Changes apply to visitors immediately.

## Editorial framing

A galaxy's framing is the short paragraph that opens it for visitors. It is the answer to the question *what is this galaxy?* before the visitor has met any wormhole. Two places to write it:

1. The **Tagline** field in the galaxy modal, for the one-line summary that appears next to the galaxy name.
2. (Some instances) a dedicated framing wormhole inside the galaxy, often the first one a visitor sees on entry. If your instance uses this pattern, your operator will let you know.

Both are editorial choices, not technical ones. Write the framing in your own voice; the galaxy is yours to introduce.

## Sharing wormholes across galaxies through tags

If you have a galaxy whose content is part of a larger constellation of work (an exhibit with several rooms; a journal with several issues; a series of related collections), the **Tags** field is how you say so. Add the same tag to each galaxy that belongs together; the union becomes reachable to visitors at `/tag/<tag-slug>` (your operator can share the link).

Tags do not create or modify wormholes. They are purely a viewing arrangement: in the union view, the visitor sees the wormholes of every tagged galaxy together, but each wormhole stays in its home galaxy. Edit one galaxy, the others are unchanged.

## Retiring a galaxy

There is no "delete galaxy" button for editors in the typical instance setup; if you genuinely need to retire a galaxy, ask your operator and they will arrange it. The reason for the friction is editorial: a galaxy that has been linked to from outside (by a tour, by a portal, by a tag union, by a visitor's bookmark) does not simply disappear; the link goes dark. The operator can decide how to handle the dark link.

The most common pattern is not to delete a galaxy but to make it invisible to visitors while keeping it in the editor side, so the editorial decision can be reversed later.

## Things worth knowing

- **You cannot move a galaxy.** Once a galaxy has a slug (the `/<short-name>` part of the URL), the slug is permanent. Renaming the galaxy changes the display name but not the slug. If a slug change is critical, the operator can arrange one, but the URL changes for everyone with the old link.
- **The galaxy picker groups galaxies with the same `[bracket]` prefix.** If your instance uses bracket prefixes (`[mocambos] Galaxy A`, `[mocambos] Galaxy B`), the picker groups them visually. The brackets are a convention, not a feature; use them when grouping helps your editors find related galaxies.
- **A galaxy with zero wormholes is allowed.** New galaxies start empty and remain editable. There is no requirement to have a minimum number of wormholes before saving.
- **The visual theme changes only the scene appearance.** Switching from Cosmic to Tech does not change what is in the galaxy; it changes how the wormholes are *drawn*. Try a theme; if it does not fit, switch back.
