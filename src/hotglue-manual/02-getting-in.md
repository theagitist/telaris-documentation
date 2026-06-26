# Getting in

You reach the Hotglue editor from the editor surface of your Telaris instance (the part of the site you see after logging in as an editor). There are two ways in: page by page, attached to a single wormhole, or through a list view where you manage many Hotglue pages at once.

> [!important] Use a large screen to edit
> Composing a Hotglue page is a precise, drag-and-drop activity, so do it on a computer or a tablet. Editing on a phone is technically possible but is not optimized for small screens and can be awkward or error-prone. Visitors can of course *view* finished pages on a phone (see *How it looks on phones*); this note is about *editing* them.

## Attaching Hotglue to one wormhole

Every wormhole can show its media in one of two ways, chosen on a pair of tabs in the **Edit wormhole** window:

- **Classic** is the plain media layout (a heading, some text, an image or a video stacked in order). This is the default.
- **Hotglue** replaces that with a freeform Hotglue page of your own design.

To compose a wormhole's media as a Hotglue page:

1. Open the wormhole for editing.
2. In the media section, choose the **Hotglue** tab.
3. Click **Edit hotglue content**. The Hotglue canvas opens in a full-window overlay, already pointed at this wormhole's page.
4. Build the page (see *The canvas* and *Adding content*).
5. Close the overlay with **Close**.

![The Edit wormhole window with the Media section's Hotglue tab selected: a short help line and the Edit hotglue content button](assets/images/hotglue-manual/01-hotglue-tab.png)

The wormhole shows whichever tab is selected when you save it. So if you compose a Hotglue page but leave the wormhole on the **Classic** tab when you save, visitors still see the classic layout. Make sure **Hotglue** is the selected tab when you save the wormhole.

## The Hotglue content view

For working with several pages at once, the editor has a top-level **Hotglue content** view, next to **Wormholes**. It lists every Hotglue page you can reach, with its title, the wormhole it is assigned to (if any), and when it was last updated. From here you can create new pages, rename them, attach or detach them from wormholes, duplicate them, search them, and delete them in bulk. All of that is covered in *Managing pages*.

![The Hotglue content view: a list of pages with Title, Assigned wormhole, Updated, and Actions columns, plus New page and Search controls](assets/images/hotglue-manual/02-hotglue-content-list.png)

## Reviewing earlier versions

The Hotglue editor keeps a history of each page. A **Revisions** button in the editor opens that history, where you can look back through earlier versions of the page you are working on. This is your safety net in place of an undo key; see *Saving and history* in *The canvas* for how the history works.

## Who can edit what

Hotglue editing follows the same access rules as the rest of your editor account. In plain terms:

- You can edit a page **you created**.
- An **admin** can edit any page.
- If a page is **attached to a wormhole**, anyone with edit (read-write) access to that wormhole's galaxy can edit it too.

Two situations let you look but not change:

- A **read-only seat** on a galaxy. You can open a page attached to a wormhole there and see it, but the editor will not let you alter it.
- An **imported (mirrored) galaxy**. Galaxies pulled in from another instance are read-only by design, so their Hotglue pages cannot be edited locally.

If you try to do something you do not have access to, the editor tells you so ("You do not have access to do that.") rather than failing silently.
