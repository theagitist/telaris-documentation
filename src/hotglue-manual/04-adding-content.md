# Adding content

This chapter covers every kind of object you can put on a page, and the tools each one offers once it is on the canvas. You add most of them from the **NEW menu** (single-click the empty background). Each object's own tools appear as small icons around it when you select it.

## Images

**To add an image,** use the upload tool in the NEW menu, or simply drag an image file from your computer and drop it anywhere on the page. Hotglue accepts JPEG, PNG, GIF, and WebP. If you drop in a very large image, Hotglue automatically scales it down to a sensible size for the page (animated GIFs are left at their original size).

When an image is selected, its tools let you:

- **Toggle image tiling**, so the image repeats to fill its box like a pattern.
- **Reset the image size** back to its natural dimensions. Hold <kbd>shift</kbd> or <kbd>ctrl</kbd> while doing this to keep the aspect ratio.
- **Adjust the image selection** by dragging, to show only part of the image.
- **Download the original file**.
- **Edit this image in the drawing editor** (see *Drawings* below).

## Text

**To add text,** choose "add a new text object" from the NEW menu. A text box appears. Click a selected text box to edit its words inline; press <kbd>esc</kbd> to stop editing.

A text box's tools let you shape it in detail:

- **Background colour** of the box, or **make the background transparent**.
- **Font size**: drag the tool to change it, click to reset.
- **Font colour**.
- **Typeface**: click to cycle through the available fonts.
- **Font style**: cycle through normal, bold, and italic.
- **Line height**, **letter spacing**, and **word spacing**.
- **Text alignment**: left, centre, right, then justified.
- **Padding** inside the box.
- **Scrolling**: keep the box at the size you set and show a scrollbar when the words run past it.

### Scrolling text

Normally a text box grows to fit its words: type more than fits and the box spills past the size you drew. The **scrolling** tool (the up-and-down arrows icon) changes that. Turn it on and the box keeps exactly the size you gave it; if the text is longer than the box, a vertical scrollbar appears and the reader scrolls through it in place. The text still wraps to the box's width, so only a vertical scrollbar is ever added, never a horizontal one.

Use it when a box's size matters to your layout (a fixed panel, a column that must line up with a neighbour) but the text inside it may be long. The tool is per box: one text box can scroll while the box beside it grows freely. Click the icon again to turn scrolling off and return the box to its normal spill behaviour. The setting is saved with the page, so the scrollbar is there for visitors, not only while you edit.

Text boxes also understand a few macros that fill themselves in automatically, such as `$BASEURL$` and `$PAGE$`. Type them into a text box and they are replaced when the page is shown.

## Web video

**To embed a video,** choose "embed a youtube, vimeo or peertube video" from the NEW menu and paste the video's address when prompted. Hotglue recognizes YouTube, Vimeo, and PeerTube links (including PeerTube videos on any federated host) and creates the right embedded player for each.

When the video object is selected, its tools let you:

- **Toggle automatic playback** of the video (the change takes effect after the published page is reloaded).
- **Toggle looping** of the video (also after a reload).

In edit mode a small "drag here" strip sits over the player so you can move the object without the video capturing your clicks.

## Drawings

Hotglue includes a full in-page image editor (miniPaint) for making or retouching an image without leaving the canvas. There are two ways in:

- From the NEW menu, choose **draw a new image** to start on a blank canvas.
- With an image selected, choose **edit this image in the drawing editor** to open that image for changes.

The drawing editor opens in a window with the usual painting tools. When you are finished, click **place on page** to drop the result back onto your Hotglue page (it flattens your layers into a single image), or **cancel** to discard it. If you were editing an existing image, the new version takes its place.

## Sound (the soundboard)

The **soundboard** turns a page into something you can play. It is a per-page setting you turn on from the PAGE menu: "toggle soundboard mode". When it is on, the published page treats your video tiles as triggers, and tapping a tile starts its clip.

What makes it a soundboard rather than just several videos is the audio mixing:

- **Self-hosted video clips** you uploaded play through a single shared audio engine, so several clips can sound at once and layer together. This works on phones as well as on desktop.
- **Embedded videos** (YouTube, PeerTube, Vimeo) play through their own built-in player controls. Several can play in parallel; this is reliable on desktop and more limited on phones.

The change takes effect after the published page is reloaded. Soundboard mode is off unless you turn it on, so an ordinary page with videos behaves normally.

## Object tools (any object)

Beyond the per-type tools above, every object shares a common set:

- **Clone** the object.
- **Change transparency** by dragging.
- **Make the object a link**: point it at a web address, another page, or an anchor, with an optional choice to open in a new tab.
- **Get the name of this object**, so you can link to it from elsewhere.
- **Make this object appear on all pages** (handy for a logo or a footer).
- **Lock** the object so it cannot be moved or resized by accident; click again to unlock.
- **Flip** the object.
- **Delete** the object.

> [!note] No custom code
> The Telaris build of Hotglue intentionally leaves out the modules that would let you paste in arbitrary HTML or scripts. Everything you add is one of the content types above. This is a safety choice, not an oversight.
