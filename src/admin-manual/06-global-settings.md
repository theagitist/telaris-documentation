# Global settings

The **Global Settings** tab holds the instance-wide settings: what the instance is called, which galaxy greets a visitor, how large an upload may be, how keywords match, how the instance sends mail, what address it answers at, what language it defaults to, and whether editors are enabled at all. These settings are stored in the instance's own database, so you change them here in the console rather than by editing files on the server.

![The Global Settings tab: the instance name, default galaxy, upload limit, fuzzy-keyword toggle, and (below) the mail and site settings](assets/images/admin-manual/07-global-settings.png)

## Instance basics

The top of the tab carries the plain facts about the instance:

- **Name.** The public name of the instance. It shows on the visitor side and becomes the instance's label in the Pluriverse directory if you apply to publish (chapter 7). Left blank, it defaults to the first part of the hostname.
- **Default Galaxy.** Which galaxy a visitor sees at the root of the site, before choosing one. Pick the galaxy that should be the front door.
- **PDF max size.** The largest PDF a wormhole may carry, in megabytes (25 by default). An editor who uploads a bigger file is told the file exceeds the limit. Raise it if your content needs it and your server has the room.
- **Fuzzy keyword matching.** The instance-wide toggle for the loosened keyword matching described in *Galaxies and clusters*: when on, near-spellings connect across galaxies, not only identical words. Off by default. A cluster can override this default in its own settings.

## Mail settings

Almost everything Telaris emails, sign-in links, enrolment confirmations, notifications, depends on the instance being able to send mail. The mail settings form is where you set that up:

- **SMTP host** and **port** of your mail relay.
- **Username** and **password** for the relay.
- **Encryption** (typically TLS).
- **From address** and **from name** that recipients see.

Two aids sit with the form:

- A **Send test** button emails a test message to an address you give, so you can confirm the settings work before relying on them.
- A **not-configured warning**. While mail is not set up, the console shows a warning, and the places that depend on mail (the self-enrolment settings, for one) repeat it, because turning on a feature that needs mail while mail is broken only produces silent failures.

If mail is not configured, password-less accounts cannot sign in and self-enrolment cannot work, because both rely on emailed links. Configure mail before you turn on either.

> [!important] The mail password is the one secret here
> The SMTP password is the single sensitive value in these settings. Telaris treats it specially: it is never included in any backup, snapshot, or federation export. This means it is safe to share a backup, but also that restoring an instance elsewhere will not carry the password; you re-enter it after a restore. The *Backups and snapshots* chapter returns to this.

## Site settings

These tell the instance about itself:

- **Instance hostname** and **base URL**: the address the instance is reached at. Telaris uses these to build the links it puts in emails, so they point at the right place regardless of how a given request happened to arrive. Set them to your real public address.
- **Default language**: the locale a visitor sees before any choice of their own, one of English, Spanish, Portuguese, or French. Set it to your audience's language.

Setting the hostname and base URL here means you do not have to hand-edit configuration files to make email links correct; the console is the source of truth for them.

## The instance switches

One switch here decides a whole feature for the instance:

- **Allow editors.** The instance-wide end of the editing cascade (see *Editor access control*). Turn it off to freeze all editing on the instance at once, for example when a project has ended, while keeping every account and everything authored. On by default.

## Things worth knowing

- **These settings live in the database, not in a file.** Changing them here takes effect without touching the server. They also override the fallback values baked into the instance's configuration file, so the console is where you should change them.
- **Test mail after any change.** The Send-test button exists so you never discover a broken relay by way of an editor who could not sign in. Use it whenever you touch the mail settings.
- **The from-address should be a real, sending-allowed address at your domain.** Relays and recipients increasingly reject mail whose from-address is not authorised to send; set it to something your relay is permitted to send as.
