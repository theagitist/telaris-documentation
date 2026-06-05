# Privacy

Telaris is a research-grade decolonial knowledge archive. This notice applies to **www.telaris.ca** (the website you are reading) and to the **Telaris software** that runs on independent operator instances. Each instance is run by an independent operator and may carry additional privacy notices of its own that govern the content on that instance; this notice covers the rest.

## What www.telaris.ca collects

The site at `www.telaris.ca` is a small set of static informational pages. It runs no analytics tool, places no advertising trackers, sets no cookies, and collects no personal information from visitors. The site is served through Cloudflare; standard Cloudflare access logs (truncated IP, user agent, requested URL, response status, timestamp) are kept for short retention by Cloudflare under their own policy. Beyond those edge logs, the site does not record visits.

The site links to downloadable documents and to independent Telaris instances. Following one of those links takes you to a different site; this notice does not govern what happens there.

## What a Telaris instance collects

Any site running the Telaris software may collect a small amount of information needed for the software to work:

- **Editor accounts.** Each instance keeps a list of editors authorised to add content. For each editor it stores a name, an email address, a password hash, optional pronouns, and login timestamps, for as long as the account is active. See *Editors: your information and what you can ask for* below.
- **Editorial content.** Wormholes, galaxies, keywords, descriptions, uploaded media, and the relationships between them are stored by each instance. This is the content visitors see. Editorial sovereignty is the principle: the editor decides what is published, and nothing is reviewed before it is shown.
- **Source-community consent.** When a source community contributes material, that community's consent governs the material. Withdrawal of consent is final and is acted on by the operator without negotiation.
- **Server access logs.** An instance may keep short-retention access logs for operational purposes such as debugging and abuse mitigation. Where the application records an IP address (for example in its action-audit log), it is the operator's choice how long to keep it; the application hashes IPs with a server-side key where it can, and does not retain clear-text IPs in its own tables.

## Editors: your information and what you can ask for

If an operator gives you an editor account, the following applies to you.

- **Why we keep your data: because you agreed.** The first time you sign in as an editor, you are asked to review these documents and agree before you can use the editor. Your agreement is recorded together with the version of each document, so that a later revision asks you again. You may withdraw your consent at any time.
- **What is stored about you:** your name, email address, password hash, any pronouns you provide, login timestamps, the editorial content you publish, and an audit record of administrative actions you take (in which your email is stored only as a salted hash, never in the clear).
- **What you can ask for:** you can ask the operator of your instance to show you the data held about you, correct it, or delete your account and your content. You can withdraw consent, which removes your access and, on request, your content. These requests are honoured by the operator of your instance; they are not negotiated, and deletion is final.
- **Retention:** account data is kept while the account is active and removed on request. The action-audit log is kept for a limited, operator-set period (the default is 365 days) for accountability, then pruned.

## Logs and retention across instances

Telaris-the-software makes no platform-wide log-retention promise, because log rotation lives in each operator's own infrastructure (their web server, their operating system, their edge provider). What is consistent everywhere is this: the **application** logs no visitor browsing activity. The only visitor personal data that exists is the IP address recorded in an operator's own server or edge logs, governed by that operator's retention.

The Polivoxia-run instances rotate their server logs at 14 days; this is a recommended default, not a promise binding on other operators. Every operator sets and is responsible for their own retention, and we recommend short retention or IP anonymisation as the posture most consistent with this project's values.

## What Telaris does not do

- **No advertising.** No third-party trackers, no advertising network, no behavioural profiling.
- **No AI training or analysis on the corpus.** Telaris content is not used to train or feed AI models, internally or externally.
- **No third-party content scanning.** Content is not sent to external services for moderation or classification.
- **No selling of data.** Editor accounts, content, and logs are never sold or shared with third parties for advertising or commercial purposes.

## Federation and cross-instance content

When Telaris instances federate, content that an editor explicitly publishes to a federation partner travels to that partner under cryptographic signatures. The receiving instance hosts a mirror; the origin instance keeps sovereignty and can retract the content, which drops the mirror.

Editor accounts and operator email addresses **do not** cross federation boundaries. Operator-to-operator communication is mediated through a relay that hides the email addresses on both sides.

## Withdrawal of consent

A source community, an editor, or any individual whose material is hosted on a Telaris instance may withdraw consent at any time. The operator of that instance is responsible for honouring it. Withdrawal removes the material; it does not require negotiation; it is final.

## Contact

For questions about a specific instance, contact that instance's operator, whose address is listed on the instance's own site. For questions about www.telaris.ca, the software itself, or this notice, use the [Contact](https://www.telaris.ca/contact) page; the project's governance and the operator to contact about how data is handled are described on the [Governance](https://www.telaris.ca/governance) page.

## Version

Version 1.0, effective 2026-06-04. This is the first published version; it replaces the earlier draft. When this notice changes in a way that affects editors, the version is incremented and editors are asked to review the new version on their next sign-in.
