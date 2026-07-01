# Self-service editor enrolment

Beyond creating accounts by hand, an instance can let people **enrol themselves** as editors. This is off by default. When you turn it on, a visitor can request an editor account through a form, confirm their email, and start editing, without you creating the account first. This chapter covers when to use it and every switch that governs it.

Self-service enrolment is configured from the admin console (the auto-enrolment settings; on most instances they sit with the other account controls). The whole feature is a single decision with several dials: *should strangers be able to become editors here, and under what limits?*

## When to use it

Turn it on for an open call: a community archive inviting contributors, a course where students self-register, a public project that wants a low barrier to helping. Leave it off for a closed instance where every editor should be someone you added deliberately. You can turn it on for a while (the span of a course, the run of a call) and turn it off again; existing accounts are unaffected when you do.

## Turning it on

The auto-enrolment control has a master switch. While it is off, the enrolment form is closed: a visitor who reaches it sees a notice that sign-up is not open, and the sign-up link is hidden from the login screen. While it is on, the form is open and the link appears.

Turning it on reveals the limits below. Set them before you announce the call, not after.

## The limits

- **Cap.** A maximum number of self-enrolled editors. Once the cap is reached, the form closes itself and the sign-up link disappears until you raise the cap or remove some accounts. Use it to keep an open call from running away from you. The cap counts self-enrolled editors, not accounts you created yourself.
- **Email-domain allowlist.** An optional list of email domains that may enrol (for example, a university's domain for a course). When set, only addresses at those domains can complete enrolment; everyone else is turned away. Leave it empty to allow any address.
- **Personal-galaxy naming.** When someone enrols, Telaris can create a **personal galaxy** for them to work in. You choose how it is named: from the person's full name, or from their first name only. First-name-only is the privacy-preserving default, because a galaxy name is public; a full name in a galaxy title is visible to every visitor. Choose full names only when that exposure is acceptable for your context.
- **Default access.** New self-enrolled editors can be given seats on demonstration galaxies, read-only or read-write, so they land with something to look at or work on. *Editor access control* explains seats.

## How a self-enrolled editor signs in

A self-enrolled editor has **no password**. They sign in every time by the email link: enter the address, receive a one-time link, follow it. This is why mail must be configured for enrolment to work at all; if the instance cannot send mail, no one can confirm an enrolment or sign in afterward. The *Global settings* chapter covers mail.

Because enrolment depends entirely on email, the flow is: the person submits the form, Telaris emails them to confirm the address is theirs, and only after they follow that confirmation are they a real editor. An unconfirmed enrolment is not yet an account and is cleaned up automatically if it is never confirmed.

## Vetting

A self-enrolled editor can edit as soon as they confirm their email; you do not have to approve them first. **Vetting** is a separate, optional step that says "I recognise this person." When you vet an account:

- the person may set a password, so they are no longer limited to email links, and
- Telaris tells them they have been vetted.

Vetting does **not** gate editing. An unvetted self-enrolled editor is a full editor already; vetting is a mark of recognition and a convenience (the password), not a permission. Unvetted accounts are highlighted in the user list so you can see at a glance who has joined but not yet been recognised.

## Keeping it safe

- **A cap is your safety valve.** An open form with no cap can be flooded. Set a cap you are comfortable moderating, and raise it deliberately.
- **The allowlist scopes the call.** For a course or an organisation, an email-domain allowlist turns "anyone" into "anyone here," which is usually what you actually meant.
- **First names by default.** Unless you have a reason otherwise, keep personal-galaxy naming on first names, so no one's full name becomes a public galaxy title without their say.
- **Turn it off when the call ends.** Enrolment left open indefinitely is a standing invitation you may have forgotten. Close it when the reason for opening it has passed; the accounts already made stay.
