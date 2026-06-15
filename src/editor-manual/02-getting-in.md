# Getting in

Telaris is a website. To use the editor, you open your instance in a web browser, sign in, and start working. That is the whole login flow; the rest of this chapter walks through what you see, in order.

## What you need

Three things; the person who runs your instance can tell you any you are missing:

- **The address of your Telaris instance**: a web link, something like `https://your-instance.example`. Bookmark it.
- **Your editor email**: the address your account is registered under. If your operator created your account, it is the address they used; if you signed up yourself, it is the address you entered.
- **A way to sign in.** Some editors have a password. Others sign in with a one-time link emailed to them each time, and have no password at all. Which you use depends on how your account was set up; the login page, below, offers both.

If you do not have any of these, ask the person who runs your instance.

## The login page

Open your instance's address in any modern browser. If you are not already signed in, you land on the login page automatically. If you have already saved a bookmark to a different part of the instance, the browser will detour you to the login page first and then return to where you were going.

![Login page: an email field, an "Email me a sign-in link" button, and a collapsible "I have a password" section below it](assets/images/editor-manual/01-login-form.png)

The simplest way in is the **Email me a sign-in link** button. Type your email, select it, and Telaris sends you a one-time link; open that link from your inbox and you are signed in, with nothing else to type. The link works for a short window; if it expires, request a new one. If your account has no password, this is how you sign in every time.

If you have a password, open the **I have a password** section below the button. A password field appears, with its own **Sign In** button. Inside that section, a **Forgot your password?** link emails you a reset link if you need one; reset links also expire after a short window.

Not sure which you have? Use the sign-in link. It works whether or not your account has a password.

Some editors start with no password and are given the option to set one later (your operator decides when). If that happens, you receive an email with a link to set a password; from then on you can use either the password or a sign-in link.

## After you sign in

You land on the **Edit Wormholes** page. This is the editor home, the place you will start from every working session. The next sections of this manual all begin from here.

![Editor home: galaxy picker on the top right, wormhole list below, search on the right](assets/images/editor-manual/02-editor-home.png)

The page is laid out in two cards:

**Top card: who you are, where you are.**

- The page title, **Edit Wormholes**, sits at the top left.
- Below the title, a small line greets you by name and confirms your role: *Welcome, Your Name (Editor)*. The role determines what you can do; if you see something this manual describes but cannot reach it, your role does not include that surface, and your operator can adjust it.
- To the right of the title, **Current Galaxy** is a dropdown that picks which galaxy you are currently editing. *All my galaxies* is the default and shows wormholes from every galaxy you have access to. If you have your own galaxy (one you created), the editor opens straight to it instead; you can always switch back to *All my galaxies* or any other from the same dropdown. Picking a specific galaxy filters everything below to that one galaxy.
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
