# Troubleshooting

The everyday situations an editor runs into, what to try, and when to ask your operator. This chapter is organised by the symptom, not by the cause; look for what *you* see, not for what is *technically* happening.

## I cannot log in

**What you see**: the login form refuses your credentials, or you reach the login page when you expected to be already signed in.

**What to try**, in order:

1. Confirm the email address and password are correct. Both are case-sensitive.
2. Use the **Forgot your password?** link below the Sign In button. An email with a reset link arrives within a minute.
3. Check that you are on your instance's address. If your operator runs multiple instances, your login is scoped to one.

**When to ask your operator**: if the password reset link does not arrive (check spam first), if your reset email is bounced back, or if you are sure your password is correct and the form still refuses.

## A wormhole I created vanished

**What you see**: a wormhole you authored is no longer in the wormhole list.

**What to try**:

1. Confirm the **Current Galaxy** dropdown is on the right galaxy (or set to *All my galaxies*). The wormhole may be in a different galaxy than you expect, especially if you used the Galaxy dropdown inside the wormhole modal.
2. Use the search box on the editor home. Search for the wormhole's name; if it exists in any galaxy you can edit, search finds it.
3. Confirm you are on the **Wormholes** tab, not the Templates or Hotglue content tab; the wormhole list only shows under the first tab.

**When to ask your operator**: if search across All my galaxies returns nothing and you are certain you saved the wormhole. The wormhole may have been deleted (by you, or by another editor); your operator may be able to restore from a snapshot.

## I cannot edit a wormhole; the modal opens in viewer mode

**What you see**: clicking a wormhole row opens an info card or a read-only preview, not the edit modal.

**What you might be seeing**:

- The wormhole is in a galaxy you have **read access** to but not edit access to (some instances allow editors to see all galaxies but only edit some). The wormhole is editable by another editor.
- The wormhole was **imported** from an external source (a sister archive, a bridged community). Imported wormholes are read-only by design; changes must happen at the source.

**When to ask your operator**: if the wormhole was authored on this instance and you should have edit rights but the modal still opens read-only.

## An upload fails

**What you see**: the file picker accepts the file, the upload begins, then an error appears or the modal closes without the file attached.

**What to try**:

1. Check the file size. PDFs are commonly capped at 25 MB (your operator may have set a different cap); images and videos may have their own limits.
2. Check the file type. Telaris supports JPG and PNG (and most other common formats) for images; MP4 for video; MP3, OGG, and WAV for audio; PDF for documents. Files of other types are rejected at upload time.
3. Try a smaller file or a different format. If the original is too large, compress or transcode before uploading.

**When to ask your operator**: if uploads consistently fail for files within the stated limits, or if you need the limit raised.

## A keyword's chip is in the wrong place on the canvas

**What you see**: a chip on the keyword canvas is overlapping another chip, sitting outside the visible area, or floating in a position that does not match where you remember placing it.

**What to try**:

1. Drag the chip to where you want it; the new position saves automatically.
2. If many chips are arranged badly, use the **Reset all chip positions** option in the canvas help overlay (the **?** at the top of the canvas).
3. Refresh the page; the canvas re-fetches the latest layout.

**When to ask your operator**: rarely. The canvas is forgiving; almost every problem is solved by dragging.

## A change I made does not appear in the visitor view

**What you see**: you saved a change in the editor, but a visitor (or you in another tab) does not see it.

**What to try**:

1. Refresh the visitor tab. Telaris does not push live updates; the change is on the next page load.
2. Check that you saved with **Save**, not closed the modal with **Cancel** or by clicking outside.
3. Check that you are looking at the same galaxy. The visitor tab may be on a different galaxy than the one you edited.

**When to ask your operator**: if you saved and refreshed and the change is still not visible after a minute. Edge caches may take a brief moment to invalidate; if it persists, that is operator territory.

## A button is greyed out

**What you see**: a button in the editor home or in a modal is visible but not clickable.

**What you might be seeing**:

- The button is **conditional on something you have not done yet**. For instance, the Settings button next to the galaxy picker only enables when a specific galaxy is selected (not *All my galaxies*).
- The button is **gated by your role**. If you are an editor and the action is admin-only, the button may appear but stay disabled.

**When to ask your operator**: if you believe you should have access to the action and the button is still disabled. Your role may need adjusting.

## My session expired in the middle of editing

**What you see**: a save fails with an "unauthenticated" or "please log in" message; the editor returns you to the login page.

**What to try**:

1. Log back in. Your session expires periodically; this is normal.
2. If you were editing a wormhole when the session expired and the change was not saved, you may have lost work since the last save. The text in the modal is sometimes recoverable from the browser's form-restore behaviour; if not, the wormhole reverts to its last saved state.

**When to ask your operator**: if sessions expire unusually quickly. The default session lasts 30 days with activity renewal; if you are kicked out within minutes, something is off.

## A message I sent to another editor seems lost

**What you see**: you sent an in-app message to another editor (or to an instance operator) and the recipient has not replied, or you cannot find the sent message.

**What you might be seeing**:

- The recipient has not opened the inbox yet.
- The in-app messaging surface may live in a section of the admin UI that you do not have access to. Most editor-to-editor communication is best handled outside Telaris (email, Signal, whatever your operator and your team have agreed on).

**When to ask your operator**: if in-app messaging is the canonical channel on your instance and a message you sent through it does not arrive at the recipient.

## A wormhole opens to a blank info card

**What you see**: clicking a wormhole opens the info card but no description, no media, no keywords.

**What to try**:

1. Check that the wormhole you opened is the one you meant to author content for. Empty wormholes are allowed; they just have no body.
2. Open the wormhole in the editor and confirm the Description field has the text you expect.
3. If the description appears in the editor but not in the visitor view, refresh both browser tabs.

**When to ask your operator**: if the wormhole has content in the editor but is blank in the visitor view after refresh.

## The 3D scene is slow or stuttering

**What you see**: the visitor 3D scene takes a long time to load, animates jerkily, or freezes briefly.

**What you might be seeing**:

- A dense galaxy on an older device. The 3D scene runs in the visitor's browser; very dense galaxies are demanding on lower-power hardware.
- A galaxy with many image-iconified wormholes (each image renders into the scene as a texture).

**What to try**:

- Suggest the visitor toggle to the **2D view** (chapter 10) if that is enabled on the galaxy.
- For galaxies you author, consider whether all the image-as-icon flags are necessary; a galaxy with twelve image-iconified wormholes is faster than one with fifty.

**When to ask your operator**: if the slowness is universal (every visitor sees it) and not specific to one device.

## I do not know who runs this instance

**What you see**: this manual keeps telling you to "ask your operator." If you do not know who that is, you need to.

**What to try**:

- Check your instance's address. Many instances have a contact page at `/contact` or a governance page at `/governance` that names the operator.
- Look at the original email that invited you to be an editor. The sender is most often the operator.
- If nothing else, the next editor or visitor you talk to about Telaris is likely to know.

If you cannot identify the operator at all, that is itself a kind of problem worth solving; an instance without a reachable operator is one that drifts.
