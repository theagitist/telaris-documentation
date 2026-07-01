# Users

The **Users** tab is where every account on the instance lives. This chapter covers the accounts you create yourself; the next chapter covers accounts that people create for themselves through self-service enrolment, which shares the same list.

![The Users tab: a table of accounts with name, email, role, and per-row actions](assets/images/admin-manual/02-users-list.png)

## The user list

The list shows every account: administrators and editors together. For each account you see its name, its email address, its role, and, where relevant, whether it has been vetted (the next chapter explains vetting). A count in the heading tells you how many accounts exist.

Each account has a row actions menu for editing and removing it, described below.

## Roles

Telaris has two roles:

- **Editor.** Can sign in and author content, within whatever access they have been granted (see *Editor access control*). Cannot reach the admin console.
- **Administrator.** Can do everything an editor can, and can reach the admin console. Give this role sparingly; every administrator can change settings, read every account, and remove content.

An account's role is set when you create it and can be changed by editing the account.

## Creating a user

Select **New User**. A form asks for the new account's name, email address, role, and, optionally, a password.

- **Name** is what the person is shown as, and what an editor's own galaxies are named after if you use the naming conventions in the next chapter.
- **Email** is the account's identity and the address Telaris writes to (sign-in links, notifications). It must be unique on the instance.
- **Role** is editor or administrator, as above.
- **Password** is optional. If you set one, the person can sign in with it. If you leave it blank, the account signs in by the passwordless email link described below. Many administrators leave it blank and let people use email links, so there is no password to manage or leak.

Save, and the account appears in the list immediately.

## Passwordless sign-in

Telaris accounts do not need a password. An account with no password signs in by asking for an email link: the person enters their email on the login page, Telaris sends them a one-time link, and following it signs them in. This is the same mechanism a self-enrolled editor uses.

For this to work, the instance must be able to send mail. If mail is not configured, email links cannot be delivered and password-less accounts cannot sign in. The *Global settings* chapter covers configuring mail and the warning the console shows when it is not set up.

## Editing a user

Open a row's actions menu and choose **Edit** to change an account's name, email, role, password, or vetted status. Changes save as one operation; if you change several fields at once, they all take effect together.

Changing an account's email changes the address Telaris writes to and the identity the person signs in with. Changing the role from editor to administrator grants console access immediately; changing it the other way removes it.

## Bulk import

When you need to create many accounts at once (a class, a cohort, a working group), use the **bulk import**. It takes a list of accounts, typically as a CSV with a column for each field (name, email, role), and creates them in one pass. Accounts whose email already exists are reported rather than duplicated, so re-running an import is safe.

Bulk import is the right tool for onboarding a known group. For a group you do not know in advance (an open call for contributors), self-service enrolment, in the next chapter, is the better fit.

## Removing a user

Choose **Delete** in a row's actions menu. Telaris confirms first, because removing an account is permanent.

If the account owns a **personal galaxy** (a galaxy created for that editor, by the naming conventions in the next chapter), Telaris asks what to do with it: remove the galaxy along with the account, or keep the galaxy and its content in place. Deleting the account never silently deletes content; you are always asked. Keep the galaxy when the content should outlive the person's access; remove it when the account and its galaxy were a single throwaway (a test account, a course demo).

## Things worth knowing

- **There is no way to see a password.** Passwords are stored so that even you cannot read them back. If someone forgets theirs, either clear it (so they use email links) or set a new one; you cannot recover the old one.
- **An administrator can see every account and every galaxy.** The privacy that scopes editors to their own work does not apply to you. Treat the list, and the content behind it, with the discretion that access implies.
- **Deleting the last administrator would lock you out.** Telaris will not leave the instance with no administrator; keep at least one admin account you can sign in to before removing others.
