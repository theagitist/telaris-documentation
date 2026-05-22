# Manifest

> [!warning] Draft
> This Manifest is a draft, written 2026-05-21. Refinement will follow as the documentation matures.

A statement of what Telaris is, what it refuses, and the principles that hold it together. Written for anyone reading the project from outside (a potential operator, a source community considering contributing, a student reading the documentation, a curator weighing whether to use the software). The rest of the documentation builds on the positions named here.

## What Telaris is

A decolonial knowledge archive project. Relational, non-hierarchical, federated peer-to-peer, threaded by meaning. Content lives in **galaxies**: clusters of small content units (a passage, an image, a sound, a film clip, a document) that connect through shared **keywords**. There are no folders, no parents, no breadcrumbs, no algorithm; the structure is a rhizome maintained by editors and read by visitors as a three-dimensional scene.

Telaris is a graduate research project at the University of British Columbia's Institute for Gender, Race, Sexuality and Social Justice. It is open-source software run by independent operators across countries and communities, not a platform run by a single owner.

## Decolonial as method, not metaphor

"Decolonial" names a practice, not an aesthetic. The practice has concrete consequences in how Telaris is designed and operated:

- Refusal of imposed categorical reductions: there is no central vocabulary, no required ontology, no editor-in-chief.
- Data sovereignty for source communities: the people whose material is hosted on a Telaris instance retain authority over it; withdrawal of consent is final and acted on without negotiation.
- Editorial sovereignty for editors: editors decide what to publish in the galaxies they tend; there is no review queue, no approval flow.
- Operator sovereignty for instance operators: each operator runs their instance under their own rules; no central authority dictates content or access.

These are method choices, not slogans. They show up in the code (no review-queue feature, no central-vocabulary table, no platform-administrator override) as readily as in the documentation.

## Localization, all the way down

A common pattern in software is to localize the visible strings and leave the identifiers, the error codes, the status keys, and other tokens in English. Telaris refuses this. The implicit logic of "English identifiers are neutral; user-visible English is what gets translated" presupposes that meaning lives in English; that the moment a system stops being English, it must become abstract or random. It is the same colonial pattern at a quieter layer.

In practice: every token an end user or operator might encounter outside the source code is locale-invariant. API error codes use the form `<http-status>.<3-digit-subcode>` (RFC 9457 Problem Details), e.g., `404.001`. They carry meaning through positioning, not through English shorthand. The same principle extends to status keys, log categories, and any future identifier that crosses out of source code onto a user-visible surface. When a translation is missing for a given locale, the fallback is the code itself, not the English source string: the worst-case user-visible token is the documented identifier, not an unstated default-to-English.

Source-code identifiers (variable names, function names, file paths, internal config keys) remain English: they live in the development context and the team reads them every day. The line is whether the token reaches a user or operator outside the source.

## What Telaris is not

A clear refusal is a clearer position than a long manifesto.

- **Not a platform.** No single owner. No central catalogue. No advertising. No tracking. No data sold or shared for commercial purposes.
- **Not an AI training corpus.** Telaris content is not used to train AI models, internally or externally. The corpus is not piped to language-model providers for moderation, classification, summarisation, or any other purpose.
- **Not a hierarchy.** No tree structure on the content. No editorial review queue. No "best content" promoted by an algorithm.
- **Not extractive.** Content contributed by source communities does not become Telaris's property. Editors do not lose authorship by publishing on Telaris. Operators do not have rights over editors' content beyond what each instance's contract makes explicit.
- **Not anonymous by default.** Attribution travels with the work. The editor's authorship is recorded; the source community's name is recorded; the licence (when supplied) is recorded. Anonymity is available when an editor or community asks for it, not the default.

## Principles, six

**1. Editorial sovereignty.** Editors decide what to publish in the galaxies they tend. No review queue, no centrally-approved vocabulary, no "wrong" keyword. The cost is responsibility: an editor's choice is the editor's; the software does not police it.

**2. Source-community consent.** When a community contributes material, the community's consent governs the material. Withdrawal of consent is final. Removal is acted on by the operator without negotiation, regardless of any editorial position the operator may hold.

**3. Operator sovereignty.** Each Telaris instance is run by an independent operator under their own rules. There is no central authority over operators. Operators agree to a small set of cross-network commitments (cryptographic identity, honouring federation withdrawals, abiding by these principles) but otherwise govern their instances independently.

**4. Federation, not true P2P.** Galaxies have single authoritative origins; peers mirror them read-only; no merge conflicts, no edit-from-anywhere. Federation is bilateral and consent-based: two operators federate only when both agree, and either can withdraw at any time. The terminology refuses both the dishonest claim of "true P2P" (which Telaris is not) and the platform pattern of a central authority (which Telaris refuses).

**5. Refusal of the platform pattern.** Each design choice is asked against this question: *does this import the platform pattern Telaris is built to refuse?* Single sign-on, advertising telemetry, central moderation, behavioural algorithms, lock-in formats, captive vocabularies. The answer determines whether the choice is in.

**6. Software open-source, content licensed by editors.** The Telaris instance software is open-source under GPL v3; the central coordination layer (the Pluriverse, when it ships) is AGPL v3. Editorial content carries whatever licence the editor or source community supplies, attached to each piece of content. The software is given away; the content is not annexed to give-away.

## Where Telaris comes from

The project is named *Telaris* (from the Latin *tela*, a woven web). It draws on:

- *Designs for the Pluriverse* and *Pluriversal Politics* by Arturo Escobar.
- *The Darker Side of Western Modernity* by Walter Mignolo.
- *Constructing the Pluriverse* edited by Bernd Reiter.
- *Discourse on Colonialism* by Aimé Césaire.
- The Mocambos / Baobáxia archives and the quilombola tradition of communal digital archiving.
- *African Fractals* by Ron Eglash, for a fractal-as-structure understanding that is grounded outside the European mathematical canon.
- Indigenous Pacific Northwest forest knowledge and the mycorrhizal-network metaphor of Suzanne Simard and Robin Wall Kimmerer, for the mutual-exchange image of federation.

These are references, not authorities. The project sits in a conversation with this body of work and contributes a small technical artefact to it. The artefact's correctness against the politics it claims is the test the documentation is structured around.

## What this document is

A position statement, kept short on purpose. The full architecture, the editorial conventions, the operator runbooks, and the federation specification live in their own documents. Read this one to know where Telaris stands; read the others to know how it works.
