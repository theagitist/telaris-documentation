# Wormholes

A wormhole is the smallest unit of content in Telaris. Everything an editor publishes is, in the end, a wormhole: a passage of text, a photograph, an audio recording, a film clip, a PDF, a quotation, a single thought. This chapter walks through creating one, editing one, the fields that shape it, and the choices the form invites you to make.

## Creating a new wormhole

From the editor home, select the galaxy you are working in, then choose **New Wormhole**. A modal opens:

![Add New Wormhole modal: empty form with Name, Galaxy, Type, Keywords, Description, URL, and media tabs visible](assets/images/editor-manual/05-new-wormhole-modal.png)

The form has four broad regions, in order of how far down the modal you scroll:

1. **Identity** at the top: Name, Galaxy, Wormhole type, Keywords.
2. **Behaviour switches**: Accentuate, Show Keywords.
3. **Body**: Description, URL.
4. **Media**: image, video, audio, PDF, and the icon override.

Save with the button at the bottom of the modal; the new wormhole appears in the list immediately. Cancel or click outside the modal to discard.

## Identity fields

### Name

Required. The label the visitor reads in the 3D scene, in any list, and in the URL when they share it. Choose a name that reads cleanly on its own; it will be quoted out of context more often than you think.

Names within a galaxy must be unique; the modal will warn you if a name is taken before you save. Across galaxies, two wormholes can share a name without conflict.

### Galaxy

Required, but usually pre-filled. The dropdown shows every galaxy you can edit. If you started from a specific galaxy in the editor home, that galaxy is selected by default; if you started from *All my galaxies*, you choose here.

Changing the galaxy in this dropdown **moves** the wormhole to that galaxy. The wormhole's keywords come along with it, but its keyword *positions* on the destination galaxy's canvas may need re-touching.

### Wormhole type

A dropdown with two values:

- **Object** is the default and the right answer for almost every wormhole. An Object holds content (description, media).
- **Portal** turns the wormhole into a doorway to another galaxy. Selecting Portal reveals a second dropdown for the target galaxy. Chapter 9 covers portals.

### Keywords

A chip input. Type a keyword and press **Enter** (or comma) to add it; click the **×** on a chip to remove it. Suggestions appear as you type, drawn from:

- Keywords already used elsewhere in **this** galaxy.
- Keywords used in galaxies that share your galaxy's `[bracket]` prefix.

Choose keywords with the visitor's path in mind: each keyword you attach is a doorway from this wormhole to every other wormhole that shares the same word. The fewer keywords you assign, the more deliberate each connection feels; the more you assign, the denser the web. Chapter 7 covers keyword strategy.

## Behaviour switches

### Accentuate Wormhole

Off by default. When on, this wormhole renders larger and more prominent in the 3D scene. Use sparingly: if you accentuate everything, nothing is accentuated. The accentuated flag is also the marker the auto-tour feature can use to pick its stops (chapter 11).

### Show Keywords

Off by default. When on, the visitor sees this wormhole's keywords printed next to it in the 3D scene, before they open it. Useful for wormholes whose role in the galaxy is best understood through its tags (a reference document; a navigation hint; a definition).

## Body

### Description

The text the visitor reads when they open the wormhole. There is no length cap; one-line wormholes and long-form essays are both supported. The field accepts basic markdown formatting: paragraphs (a blank line), `**bold**`, `*italics* `, `[link](https://...)`, lists, and inline `code`. Headings and embedded media are not rendered inside the description; if you need a heading-like break, leave a blank line and start a new paragraph.

Write descriptions in your own voice. Telaris does not edit what you write; the platform frames the content, the content is yours.

### URL

Optional. If you fill this in, the wormhole becomes clickable as a link out: when the visitor opens the wormhole's info card, an *Open Link* button appears that takes them to the URL in a new tab.

Use this for source-of-truth references (a paper, a book page, a sound archive, a community website). Leave it empty when the wormhole is self-contained.

## Media

A wormhole can carry one **primary visual** plus an optional **audio** track and an optional **icon override**. The primary visual is what visitors see at the top of the info card when they open the wormhole; the audio plays in the background; the icon override changes how the wormhole appears in the 3D scene.

The modal organises the primary visual as a set of tabs: **Image**, **Video (MP4)**, **PDF**. Picking one and saving clears the others; only one primary visual at a time. Chapter 6 covers each tab in detail.

The audio field is independent of the primary visual; a wormhole with an image and an audio file plays the audio while the image is visible. Embed code (e.g., a Spotify or Vimeo iframe) is supported as an alternative to image / video / PDF when the visual is hosted externally.

## Editing an existing wormhole

To edit a wormhole, click anywhere on its row in the wormhole list, or open its row actions menu and choose **Edit**:

![Edit Wormhole modal for Beach Strawberry: filled name, keyword chips, description, media tabs](assets/images/editor-manual/06-edit-wormhole-modal.png)

The modal is the same as the create form, with the existing values populated. The wormhole's id appears in the upper-right corner (here, `#279`); editors rarely need to refer to ids, but the number is useful when reporting a problem to your operator.

Save persists the change immediately. Visitors viewing the galaxy see your update on their next page load.

## Duplicating, viewing, deleting

The actions menu on each wormhole row offers four operations:

- **View** opens a read-only preview of the wormhole's info card as the visitor would see it. Use this whenever you want to check a change before treating the work as done.
- **Edit** opens the modal above.
- **Duplicate** creates a copy of the wormhole, with the same content, in the same galaxy, named "Original Name (Copy)". The new wormhole gets a fresh position in the 3D scene; everything else carries over. Useful when you want a near-duplicate as a starting point.
- **Delete** removes the wormhole. A confirmation modal appears first; deletes are permanent (your operator can sometimes restore from a snapshot, but the answer should be: do not delete unless you mean it).

## Things worth knowing

- **Save before switching galaxies in the dropdown** if you are mid-edit; switching may close the modal without saving.
- **The 3D scene position is automatic.** Each wormhole gets a position assigned by the system at create time. You do not need to choose where the wormhole sits in space; the layout is generated. To re-randomise a wormhole's position, Duplicate it and delete the original (the duplicate gets a new position).
- **Keywords are case-insensitive matches.** "Native" and "native" are the same keyword; the chip will use whichever case was used first in the galaxy.
- **A wormhole without a description is allowed but quiet.** Visitors who open it see only the name. Use this pattern when the wormhole's job is purely visual (an image-only postcard) or when it serves as a navigation hint.
- **A wormhole's keyword chips are coloured deterministically** by the keyword text. The same keyword always gets the same pastel across every galaxy on your instance; this is intentional, so visitors can recognise *native* by colour as well as by spelling.
- **Imported wormholes are read-only.** If your instance imports content from an external source (a sister archive, an upstream community), those wormholes appear in your editor list but cannot be edited; the edit modal opens in a viewer state. The change has to happen at the source.
