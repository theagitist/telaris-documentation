# Managing pages

The **Hotglue content** view is where you keep track of your Hotglue pages: making them, naming them, attaching them to wormholes, and tidying up. This chapter walks through it.

## The list

The view shows a table of the Hotglue pages you can reach, with a count in the heading. The columns are:

- a checkbox for selecting the row,
- **Title**,
- **Assigned wormhole** (the wormhole this page is shown in, or blank if none),
- **Updated**,
- **Actions**.

![The Hotglue content list with three pages: one assigned to a wormhole, one not assigned, and a second assigned page, each with an Updated date and an actions menu](assets/images/hotglue-manual/02-hotglue-content-list.png)

Click a page's title to open it in the editor overlay.

## Creating and naming a page

Click **New page** to create one. It opens immediately in the editor as an untitled, unassigned page, ready to compose.

To rename a page, open it and edit the **Page Name** field at the top of the overlay. The new name saves on its own when you click away; a small status note confirms it.

## Assigning a page to a wormhole

A Hotglue page only appears to visitors once it is attached to a wormhole. Inside the editor overlay, use the **Assigned wormhole** control:

- It is a searchable list. Start typing a wormhole's name to narrow it down. Each option is shown as the wormhole name followed by its galaxy, so you can tell similarly named wormholes apart.
- Choose a wormhole to assign the page to it. Choose **Not assigned** to detach the page again (the wormhole then falls back to its classic media; the page itself is not deleted).

If the wormhole you pick already shows a different Hotglue page, Hotglue asks first: "This wormhole already shows a hotglue page. Replace it? The page it shows now will become unassigned (it is not deleted)." So you never lose a page by reassigning a wormhole; the displaced page simply becomes unassigned.

> [!note] You need edit access to the target galaxy
> Assigning or detaching a page requires a read-write seat on the wormhole's galaxy. A read-only seat lets you see pages but not change what they are attached to.

## Duplicating a page

The **Duplicate** action in a row's menu makes a copy of a page (its title gains a "(copy)" suffix). The copy is always created **unassigned**, so duplicating never disturbs the original's wormhole. Right after duplicating, Hotglue offers to assign the new copy somewhere.

## Viewing a page

A row's actions menu gives three ways to look at a page:

- **View in browser** opens the bare Hotglue page in a new tab, exactly as a visitor would see it, and copies its address to your clipboard. This works for any page, assigned or not.
- **View in wormhole** opens a preview of the page inside its wormhole, in the same window. Available only for assigned pages.
- **View in galaxy** opens the live three-dimensional galaxy viewer focused on the wormhole, in a new window. Available only for assigned pages.

## Reviewing earlier versions

While a page is open in the editor, the **Revisions** button opens its history, so you can look back through earlier versions and recover from a change you did not mean to keep. See *Saving and history* in *The canvas* for how the history works.

## Searching and filtering

- The **Search** box filters the list as you type, matching on page title, wormhole name, and galaxy name.
- The editor's header galaxy selector doubles as a filter: pick a galaxy to show only the Hotglue pages whose wormholes live there, or leave it on all galaxies to see everything.

## Working in bulk

Tick the checkboxes (or the select-all box in the header) to act on several pages at once. A bar appears showing how many are selected, with:

- **Clear Selection**,
- **Unassign Selected** (detach the chosen pages from their wormholes),
- **Delete Selected**.

## Deleting a page

Delete a single page from its row's actions menu, or several at once with **Delete Selected**. Either way Hotglue confirms first, because deletion is permanent: "Delete this hotglue page? This permanently removes its content. If it is assigned to a wormhole, that wormhole returns to classic media." Deleting a page removes its content for good; any wormhole it was attached to simply goes back to showing classic media.
