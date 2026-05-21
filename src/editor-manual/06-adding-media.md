# Adding media

A wormhole's body is the description; its **media** is everything visual or sonic the visitor encounters alongside the body: an image, a film clip, a sound recording, a PDF document, an embedded player from another site. This chapter walks through each kind, in the order the modal presents them.

A wormhole carries at most **one primary visual** at a time. Image, Video, and PDF are three tabs in the modal that share a single underlying slot; picking one and saving clears the others. The fourth media type, **audio**, is independent of the primary visual: a wormhole with an image *and* an audio track plays the audio while the image stays on screen.

## The Image tab

The default tab, and the most common media choice. Use it for photographs, illustrations, scans, diagrams, anything still.

![Image tab in the New Wormhole modal: URL field and file picker, plus the Use-as-wormhole-icon toggle](assets/images/editor-manual/05-new-wormhole-modal.png)

Two ways to attach an image:

- **Image URL**: paste the address of an image hosted elsewhere on the web. Use when the image's home is somewhere stable (a museum archive, a community website, a CDN under your control). The URL must point at the image itself, not at a page containing the image.
- **File picker**: choose **Choose File** and upload an image from your computer. Telaris keeps the uploaded file on your instance and serves it back to visitors.

Either way, the image becomes the visitor's primary visual when they open the wormhole.

**Use as wormhole icon** is a toggle below the image fields. When on, the image replaces the theme's default 3D node icon: visitors see the image *as* the wormhole in the 3D scene, not just inside the info card. Useful when the image is the wormhole's identity (a portrait, a cover, a logo). When off, the 3D scene shows the theme's default icon and the image only appears inside the opened info card.

**Image attribution** is a small free-text field that travels with the image. Use it for photographer credit, source archive, licence note, anything that would attach to the image if it appeared in a printed book. Visitors see it next to the image in the info card.

## The Video tab

Use for film clips, recorded interviews, animations, anything that moves. Telaris supports MP4 only at this stage; other formats (WebM, MOV, AVI) need to be transcoded first or hosted on a video service and embedded (see Embed code below).

![Video tab in the New Wormhole modal: Video URL / file picker for an MP4](assets/images/editor-manual/07-media-video-tab.png)

Same two paths as image: paste a URL to an MP4 hosted elsewhere, or upload a file. Once the wormhole is saved, the visitor's info card shows a video player with standard controls (play, pause, scrub, volume, full-screen).

**Sizing matters.** Video files are typically much larger than images; an instance's upload limit may stop you well before you exhaust your patience. If the upload fails, ask your operator about the limit or host the video externally and use the URL field.

If your video lives on a streaming service (Vimeo, YouTube, archive.org), the Embed code field below is the right tool, not the Video tab.

## The PDF tab

For documents: papers, field guides, photocopies, reports, score sheets, manuscripts.

![PDF tab in the New Wormhole modal: PDF URL / file picker](assets/images/editor-manual/08-media-pdf-tab.png)

Same two paths. Once saved, the visitor's info card embeds an in-page PDF reader: they can scroll the document, search it, copy text, and download it (the standard PDF viewer affordances).

PDF uploads have a size cap set by your operator (commonly 25 MB). If your file is larger, either split it, host it externally and link with the URL field, or ask your operator to raise the cap.

## Audio

The Audio field appears below the primary-visual tabs. It is independent of the image / video / PDF choice; a wormhole can have any combination of audio and one primary visual.

- **Audio URL / File**: paste an URL to an audio file or upload one. MP3 is the safest choice; many browsers also support OGG and WAV.

When audio is attached, two toggles control playback:

- **Autoplay**: when on, the audio starts as soon as the visitor opens the wormhole's info card. When off, the visitor sees a play button and starts the audio themselves. Autoplay is usually right for short, ambient, or atmospheric tracks; off is right for spoken-word, music, anything that demands attention.
- **Loop**: when on, the audio restarts from the beginning each time it finishes. Use for ambient loops, drones, soundscapes; turn off for any audio with a narrative arc.

The audio plays in the background of the info card; the visitor can pause or scrub it at any time using the standard audio controls.

## Embed code

The fourth media path, for content hosted on another service that already provides an embed snippet: a Vimeo iframe, a Spotify player, a SoundCloud track, an archive.org viewer, a SketchFab 3D scene.

Find the **Embed code** field (below the primary-visual tabs) and paste the snippet exactly as the host gives it to you. Telaris does not transform or sanitise embed code; what you paste is what visitors get. Test the wormhole afterwards by opening it in a visitor view; if the embed is broken, the field is the place to fix it.

Embed code and the primary visual are not mutually exclusive (the embed appears separately in the info card), but for clarity it usually makes sense to pick one or the other.

## The icon override

Below the media fields, an **Icon URL / File** appears. This sets the wormhole's appearance in the 3D scene, *separately* from the primary visual. Use it when:

- You want a custom 3D icon (a small graphic that represents the wormhole at scene scale), distinct from the larger image visitors see inside the info card.
- The Use-as-wormhole-icon toggle on the Image tab is not enough because you have an Image *and* you want the scene icon to be something else.

Most editors do not need this; the theme's default icons cover most cases. When you do need it, supply a small square image (PNG or SVG) and Telaris uses it in the 3D scene.

## Storage and what travels with a wormhole

Uploaded media is stored on your instance. Each wormhole's uploads live under a folder identified by the wormhole's id; restoring a snapshot brings uploads with it, deleting a wormhole removes its uploads.

URL-linked media stays at its original host; if the host removes the file, the wormhole's media goes dark. Editors with valuable external references should consider uploading the file rather than linking, so the archive survives the original host.

## Things worth knowing

- **Switching between primary-visual tabs clears the field you were on.** A safety prompt before saving warns you about this. If you change your mind, switch back before saving.
- **Audio that loops can be jarring on first visit.** If you ship an audio loop, listen to the boundary (the moment the loop restarts); the seam is what visitors will notice.
- **An image at high resolution is more useful than at low.** Telaris scales images down for the 3D scene automatically; uploading at full quality means a sharper info-card view, and means future format changes do not need re-uploading.
- **PDF text is searchable in the in-page viewer**, but only if the PDF itself has a text layer. Scanned documents without OCR are flat images inside a PDF wrapper; the search box will find nothing.
- **Video files do not stream by chunks**: when a visitor opens the wormhole, the entire file downloads. Keep video files short and well-compressed.
- **External embeds may break over time.** Services change their embed format, deprecate players, or remove content. A wormhole that depends on an embed is a wormhole whose half-life is shorter than one whose media lives on your instance.
