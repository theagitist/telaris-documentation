# The canvas

This chapter is the heart of the manual: how the editing surface works once you have opened it.

## Edit mode

A Hotglue page has two states: the published view that visitors see, and **edit mode**, where you can change things. You enter edit mode through the buttons described in *Getting in*. In edit mode the page gains its menus and every object becomes draggable.

![A Hotglue page open on the editing canvas: a title band, a subtitle, and two columns of text, each a separate object you can move](assets/images/hotglue-manual/03-canvas.png)

## The two menus

Almost everything you do starts from one of two menus, and which one you get depends on how you click the empty background of the page:

- **Single-click the background** to open the **NEW menu**: the tools for adding things to the page (upload a file, add text, embed a video, draw an image). The keyboard shortcut is <kbd>alt</kbd> + <kbd>o</kbd>.

  ![The NEW menu open on the canvas: small icons for adding a drawing, text, an uploaded file, an image, and a video](assets/images/hotglue-manual/04-new-menu.png)

- **Double-click the background** to open the **PAGE menu**: the tools that affect the whole page (background colour and image, the grid). The keyboard shortcut is <kbd>alt</kbd> + <kbd>p</kbd>.

  ![The PAGE menu open on the canvas: a grid of whole-page tools including title, page URL, start page, background colour and image, and the grid](assets/images/hotglue-manual/05-page-menu.png)

When you **select an object** (by clicking it), a third set of tools appears: the object's own **context menu**, a fan of small icons around the object. The icons differ by object type (an image has different tools than a text box), and they are covered per type in *Adding content*.

## Placing, selecting, and moving

**Adding an object** puts it where you clicked (for menu items) or where you dropped it (for drag-and-drop). You can then move it anywhere.

**Selecting:**

- Click an object to select it.
- Hold <kbd>shift</kbd> and click to add more objects to the selection (or remove one).
- Click the empty background to deselect everything.
- <kbd>ctrl</kbd> + <kbd>A</kbd> selects all objects, <kbd>ctrl</kbd> + <kbd>D</kbd> selects none, <kbd>ctrl</kbd> + <kbd>I</kbd> inverts the selection, and <kbd>tab</kbd> steps through objects one at a time.

**Moving:**

- Drag a selected object with the mouse.
- Hold <kbd>shift</kbd> while dragging to lock movement to one axis (purely horizontal or purely vertical).
- Hold <kbd>ctrl</kbd> while dragging to ignore the snap grid and place the object freely.
- The arrow keys nudge a selection one pixel at a time; <kbd>shift</kbd> + an arrow key moves it by one grid step.

**Resizing:** drag the resize handle at the corner of a selected object. A small readout shows the live width, height, and position as you drag. Hold <kbd>ctrl</kbd> to resize free of the grid.

**Deleting:** press <kbd>delete</kbd> with an object selected, or use the object's own delete icon.

## Layers and stacking order

When objects overlap, you control which sits in front:

- Drag the object's foreground/background icon left or right to move it forward or back one step at a time.
- <kbd>shift</kbd> + <kbd>page up</kbd> brings the selection to the very front; <kbd>shift</kbd> + <kbd>page down</kbd> sends it to the very back.

## The grid and snapping

By default, objects snap to an invisible grid as you move and resize them, which keeps a layout tidy. From the PAGE menu you can show or hide the grid, and you can change its spacing by dragging the grid tool (the readout shows the size as NxN). To place a single object off the grid without changing the grid itself, hold <kbd>ctrl</kbd> while you drag or resize it.

## The background

From the PAGE menu you can:

- **Change the background colour** with a colour wheel (or shift-click the wheel to type an exact value).
- **Upload a background image** for the page.
- Toggle whether the background image stays **fixed** as the page scrolls, or scrolls with it.
- Adjust which part of the background image shows, by dragging.

## Saving and history

There is **no Save button**. Every action you take (moving, resizing, editing text, changing a colour) is saved the instant you finish it.

Because of that, there is also no traditional **undo**. Instead, Hotglue keeps a history of a page called *revisions*. Open it with the **Revisions** button in the editor (or press <kbd>ctrl</kbd> + <kbd>z</kbd>, which offers to take you there). In the revisions view you can look back through earlier versions of the page. Hotglue takes an automatic snapshot of a page about once an hour while it is being edited, and keeps those snapshots for seven days.

> [!tip] Work in small, deliberate moves
> Since there is no undo and changes are immediate, it pays to make changes one at a time and glance at the result. If something goes wrong, the revisions history is your safety net, not an undo key.
