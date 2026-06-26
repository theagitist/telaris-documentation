# Introduction

This manual is for anyone who composes a **Hotglue page**: a freeform visual layout where text, images, video, and sound sit exactly where you place them, with no grid or template telling them where to go. If a normal text box feels too rigid for what you want a piece of content to look like, Hotglue is the surface that gives you a blank canvas instead.

## What Hotglue is

Hotglue is a visual page editor. You drag objects onto a page, move and resize them by hand, and what you arrange is what a visitor sees. There are no columns to fill in and no fixed shape: a page can be as wide and as tall as you like, and an object can overlap another, sit over a coloured background, or float wherever you put it.

Two things make Hotglue feel different from most editors, and it helps to know them from the start:

- **There is no Save button.** Every move, resize, and edit is saved the moment you make it. You never have to remember to save, and there is no "discard changes" either. If you want to step back from a mistake, Hotglue keeps a history (see *revisions* in *The canvas*).
- **What you edit is what gets published, immediately.** When you change a page, the change is live for visitors right away. There is no separate publish step and no cache to clear.

## Where Hotglue comes from

Hotglue is not ours originally. It was created by Danja Vasiliev and Gottfried Haider and became widely known through the hosted service at hotglue.me. It was built as a deliberate reaction against the conventions of ordinary web design: instead of templates, columns, and tidy hierarchies, it offers a free canvas where layout is non-linear and placement is entirely yours. That spirit, breaking out of the usual web standards and inviting creative, unplanned composition, is exactly why Telaris uses it.

The original project is no longer under active development upstream. Its source remains available and open, licensed under the GNU General Public License version 3 (GPL-3.0):

- Upstream project: <https://hotglue.me> and the source at <https://github.com/k0a1a/hotglue2>

## The Telaris version of Hotglue

This manual describes **Telaris's version of Hotglue**, which we maintain and actively develop as a fork. It stays open source under the same GPL-3.0 licence, and our source is public:

- Telaris fork: <https://github.com/theagitist/hotglue2>

Because we develop it ourselves, the Hotglue inside Telaris has a number of features that are not in the original. Most of what this manual covers is shared with classic Hotglue, but the following were added or substantially improved for Telaris:

- **WebP image support**, alongside JPEG, PNG, and GIF.
- **A refreshed editor interface**, with a modern icon set and a cleaner, Telaris-branded look.
- **More video sources.** Embeds work with YouTube, Vimeo, and PeerTube, including PeerTube videos hosted on any federated server.
- **A full in-page image editor** (based on miniPaint) for drawing a new image or retouching an existing one without leaving the page.
- **Soundboard mode**, where a published page becomes playable: tap video tiles to trigger clips, with self-hosted audio mixed so several can sound at once.
- **Accessibility on phones and small screens.** Published pages automatically scale to fit narrow screens, so a layout built wide is still usable on a phone.
- **Integration into Telaris**, including per-editor access control, attaching pages to wormholes, and the **Hotglue content** management view described later in this manual.
- **Localized interface.** The editor is available in English, Spanish, Portuguese, and French: the canvas menus, tooltips, and prompts, the in-app image editor, and the Telaris controls around them (the Hotglue content view, toolbar, buttons, and dialogs) all follow the language you are working in.

When this manual mentions one of these, it is describing the Telaris build specifically. If you have used Hotglue elsewhere, those are the differences to expect.

## How this manual is organized

The chapters move from how you get in, to the canvas itself, to each kind of content you can add, and then to managing your pages and how they look to visitors.

1. **Getting in.** Reaching the Hotglue editor in Telaris, and who can edit what.
2. **The canvas.** Edit mode, the two menus, and how to place, move, resize, and arrange objects.
3. **Adding content.** Images, text, web video, drawings, sound, and object tools.
4. **Managing pages.** The Hotglue content view: creating, naming, assigning, and tidying pages.
5. **How it looks on phones.** What a visitor sees on a small screen, and tips for authoring with that in mind.
6. **Keyboard shortcuts.** Every shortcut in one table.
7. **Glossary.** The named pieces, defined briefly.

## Conventions

- **Menu paths** appear like this: <span class="menu-path">PAGE menu &rarr; change the background color</span>.
- **Buttons and tooltips** appear in bold: **New page**, **place on page**, **Assigned wormhole**.
- **Keyboard shortcuts** use <kbd>alt</kbd> + <kbd>o</kbd>.
- *Italics* introduce a term the first time it appears.

> [!note] When something goes wrong
> If a page will not load, or the editor behaves in a way this manual does not describe, reach out to the person who runs your instance (your **operator**). This manual focuses on what you can do once everything is working as expected.
