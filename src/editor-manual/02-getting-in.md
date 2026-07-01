# Getting in

Telaris is a website. To use the editor, you open your instance in a web browser, sign in, and start working. That is the whole login flow; the rest of this chapter walks through what you see, in order.

## What you need

Three things; the person who runs your instance can tell you any you are missing:

- **The address of your Telaris instance**: a web link, something like `https://your-instance.example`. Bookmark it.
- **Your editor email**: the address your account is registered under. If your operator created your account, it is the address they used; if you signed up yourself, it is the address you entered.
- **A way to sign in.** Some editors have a password. Others sign in with a one-time link emailed to them each time, and have no password at all. Which you use depends on how your account was set up; the login page, below, offers both.

If you do not have any of these, ask the person who runs your instance.

## Signing up yourself

This is optional, and not every instance has it. On many instances your operator creates your account for you, and there is nothing to sign up for: skip ahead to *The login page*. But some operators open their instance to self-service signup, so you can create your own editor account. You can tell which: when self-signup is open, an **Enrol as Editor** link appears in the instance's menu and on the login page. If you do not see it in either place, this instance has not opened self-signup (or has reached the number of self-enrolled editors it accepts); ask the operator for an account instead.

![The Enrol as an editor form: a name field, an email field, a consent checkbox for the Terms and Privacy, and a Request access button](assets/images/editor-manual/01b-enroll-form.png)

When the link is there, the whole flow is short:

1. Select **Enrol as Editor**. A small form opens, titled *Enrol as an editor*.
2. Fill in **Your name** and **Email**, and tick the box to agree to the Terms of Use and the Privacy Policy. Both are linked from the form, and agreeing is required.
3. Select **Request access**. The page tells you to check your email: a confirmation link is on its way, and it expires in 24 hours.
4. Open the **confirmation email** and select its link. That confirms your address, creates your account, and signs you in right away. There is no password to choose.
5. A short **welcome email** arrives next, pointing you to where the documentation lives. From here you are an editor, and the rest of this manual applies.

So a self-signed-up account has **no password**: you confirm by email once, and after that you sign in with a one-time link each time (see *The login page* below). If your operator later decides to give your account a password, you receive a separate email with a link to set one; from then on you can use either the password or a sign-in link.

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
- **New Wormhole** opens the form to create a new wormhole. Chapter 5 covers this in detail. Next to it is a small template dropdown (default **No template**) that lets a new wormhole start from a saved template; chapter 5 covers templates.
- **?** opens a small panel listing every keyboard shortcut the editor supports. Memorising even two or three will speed up your day; the most useful are `n` (new wormhole), `/` (focus the search box), and `g` (open galaxy settings).
- **Search** filters the wormhole list as you type. It searches across wormhole names, descriptions, galaxy names, and keywords; one search box, all four columns.

Across the top of the card are three tabs: **Wormholes** (the list described here), **Templates** (your reusable wormhole starting points), and **Hotglue content** (freeform media pages). Chapter 5 covers Templates; the separate Hotglue Manual covers Hotglue content.

The wormhole list itself shows: name, type, galaxy, keywords, an accentuated flag, created date, updated date, and an actions menu. Click any column header to sort by it. Subsequent chapters explain each column.

On a phone or a narrow screen, the same list re-flows into stacked cards, one wormhole per card, with each field labelled; the actions menu and every button stay reachable. The editor surface is usable on a phone, though a wider screen is more comfortable for laying out keywords and media.

## Logging out

The **Logout** button at the top right ends your session and returns you to the login page. Telaris will not log you out automatically; if you share a computer, log out at the end of your session.

## Things worth knowing

- **Multiple tabs are safe.** You can open the editor in several browser tabs without confusing it. Each tab keeps its own *Current Galaxy* selection.
- **Your session persists across browser restarts** until you explicitly log out or your operator invalidates sessions during maintenance. If you suddenly find yourself back at the login page, this is the most likely reason; sign in again and continue.
- **The mobile experience covers reading and light editing.** Some surfaces (notably the *keyword canvas* covered in chapter 8) are desktop-only. The manual flags each surface as it goes.
- **If a page fails to load**: refresh the browser. If it still fails, that is the moment to talk to your operator.
