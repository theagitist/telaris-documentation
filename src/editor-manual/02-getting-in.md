# Getting in

Telaris is a website. To use the editor, you open your instance in a web browser, sign in, and start working. That is the whole login flow; the rest of this chapter walks through what you see, in order.

## What you need

Three things, all supplied by your operator:

- **The address of your Telaris instance**: a web link, something like `https://your-instance.example`. Bookmark it.
- **Your editor email**: the address your operator created the account under.
- **Your password**: chosen by you or sent to you by your operator. If your operator created your account, expect to be asked to set a new password the first time you log in.

If you do not have any of these, ask the person who runs your instance.

## The login page

Open your instance's address in any modern browser. If you are not already signed in, you land on the login page automatically. If you have already saved a bookmark to a different part of the instance, the browser will detour you to the login page first and then return to where you were going.

![Login form](assets/images/editor-manual/01-login-form.png)

Two fields: **Email** and **Password**. Type your credentials and select **Sign In**.

If you forget your password, there is a **Forgot your password?** link below the Sign In button. The link asks for your email; an email with a reset link lands in your inbox within a minute. Reset links expire after a short window; if the link no longer works, request a new one.

## After you sign in

You land on the **Edit Wormholes** page. This is the editor home, the place you will start from every working session. The next sections of this manual all begin from here.

![Editor home: galaxy picker on the top right, wormhole list below, search on the right](assets/images/editor-manual/02-editor-home.png)

The page is laid out in two cards:

**Top card: who you are, where you are.**

- The page title, **Edit Wormholes**, sits at the top left.
- Below the title, a small line greets you by name and confirms your role: *Welcome, Your Name (Editor)*. The role determines what you can do; if you see something this manual describes but cannot reach it, your role does not include that surface, and your operator can adjust it.
- To the right of the title, **Current Galaxy** is a dropdown that picks which galaxy you are currently editing. *All my galaxies* is the default and shows wormholes from every galaxy you have access to. Picking a specific galaxy filters everything below to that one galaxy.
- Next to the dropdown, the **View** button opens your current galaxy in the visitor view (the 3D scene). It is the same view your readers see; it is useful to flip into it from time to time to check that the changes you are making read the way you expect.
- The **Logout** button at the far right ends your session. Telaris keeps your session active across browser restarts unless you log out explicitly.

**Bottom card: your wormholes.**

- **Wormholes (N)** at the top left tells you how many wormholes are in the current galaxy view. *N* is a number; when you pick *All my galaxies*, it counts across every galaxy.
- **New Wormhole** opens the form to create a new wormhole. Chapter 5 covers this in detail.
- **Touched today** narrows the list to wormholes you have edited since midnight. Useful for picking up where you left off.
- **Bulk by keyword** opens a modal for batch operations across many wormholes at once (delete every wormhole tagged with a keyword, move them all to another galaxy). Chapter 7 covers this surface.
- **?** opens a small panel listing every keyboard shortcut the editor supports. Memorising even two or three will speed up your day; the most useful are `n` (new wormhole), `/` (focus the search box), and `g` (open galaxy settings).
- **Search** filters the wormhole list as you type. It searches across wormhole names, descriptions, galaxy names, and keywords; one search box, all four columns.

The wormhole list itself shows: name, type, galaxy, keywords, an accentuated flag, created date, updated date, and an actions menu. Subsequent chapters explain each column.

## Logging out

The **Logout** button at the top right ends your session and returns you to the login page. Telaris will not log you out automatically; if you share a computer, log out at the end of your session.

## Things worth knowing

- **Multiple tabs are safe.** You can open the editor in several browser tabs without confusing it. Each tab keeps its own *Current Galaxy* selection.
- **Your session persists across browser restarts** until you explicitly log out or your operator invalidates sessions during maintenance. If you suddenly find yourself back at the login page, this is the most likely reason; sign in again and continue.
- **The mobile experience covers reading and light editing.** Some surfaces (notably the *keyword canvas* covered in chapter 8) are desktop-only. The manual flags each surface as it goes.
- **If a page fails to load**: refresh the browser. If it still fails, that is the moment to talk to your operator.
