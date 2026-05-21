# Privacy

> [!warning] Draft
> This document is a placeholder. A finalised privacy notice is in progress and will replace this draft. For questions in the interim, write to the maintainer of the instance you are using.

Telaris is a research-grade decolonial knowledge archive. The privacy posture described here applies to **www.telaris.ca** (the marketing site you are now reading) and to the **Telaris software** that runs on independent operator instances. Each operator instance is run by an independent operator and may carry additional privacy notices of its own; those notices govern the instance's content. This document covers the rest.

## What the marketing site collects

The marketing site at `www.telaris.ca` is a single static page. It does not run an analytics tool, does not place advertising trackers, does not set cookies, and does not collect personal information from visitors. The page is served through Cloudflare; standard Cloudflare access logs (truncated IP, user agent, requested URL, response status, timestamp) are kept for short retention by Cloudflare per their own policy. Beyond those access logs, the site does not record visits.

The site links to downloadable PDFs and to independent Telaris instances. Following one of those links takes you to a different page; this notice does not govern what happens there.

## What Telaris instances may collect

Individual instances (any site running the Telaris software, including the three listed under *Active instances* on the landing page) may collect a small amount of information necessary for the software to function:

- **Editor accounts.** Each instance maintains a list of editors authorised to add content. An editor's name, email, and a password hash are stored for as long as the account is active. Operators may delete editor accounts on request.
- **Editorial content.** Wormholes, galaxies, keywords, descriptions, uploaded media, and the relationships between them are stored by each instance. This is the content the visitor sees. Editorial sovereignty is the principle: the editor decides what is published; nothing is reviewed before being shown.
- **Source-community consent.** When a source community contributes material to an instance, the community's consent governs the material. Withdrawal of consent is final and is acted on by the operator without negotiation.
- **Server-level access logs.** Instances may keep short-retention access logs for operational purposes (debugging, abuse mitigation). IP addresses, when stored, are hashed with a server-side key; clear-text IPs are not retained.

## What Telaris does not do

- **No advertising.** No third-party trackers, no advertising network, no behavioural profiling.
- **No AI training on the corpus.** Telaris content is not used to train AI models, internally or externally.
- **No third-party content scanning.** Content is not sent to external services for moderation or classification.
- **No selling of data.** Editor accounts, content, and access logs are not sold or shared with third parties for marketing purposes.

## Federation and cross-instance content

When Telaris instances federate (a planned feature, not yet active at the time of this draft), content that an editor explicitly publishes to a federation partner travels to that partner's instance under cryptographic signatures. The receiving instance hosts a mirror of the content; the origin instance retains sovereignty.

Editor accounts and operator email addresses **do not** cross federation boundaries. Operator-to-operator communication is mediated through a relay that hides email addresses on both sides.

## Withdrawal of consent

A source community, an editor, or any individual whose material is hosted on a Telaris instance may withdraw consent at any time. The instance's operator is responsible for honouring the withdrawal. Withdrawal removes the material; it does not require negotiation; it is final.

## Contact

Each Telaris instance lists the contact address of its operator on the instance's own site. Use that channel for instance-specific privacy questions. For questions about the marketing site, the software itself, or this notice, contact the maintainer named on the **/governance** page (forthcoming).

## Version

Draft, 2026-05-21. Replaces no prior version. To be revised before public-facing release.
