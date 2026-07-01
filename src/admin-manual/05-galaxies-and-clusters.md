# Galaxies and clusters

The **Galaxies** and **Clusters** tabs are the administrator's view of all the content on the instance. An editor sees only their own galaxies; you see every galaxy, including ones imported from elsewhere, and you can group them into clusters. This chapter covers both tabs.

## The Galaxies tab

![The Galaxies tab: a table of every galaxy on the instance with its cluster, owner, and whether it is imported](assets/images/admin-manual/05-galaxies-list.png)

The Galaxies tab lists every galaxy on the instance, whoever made it. For each galaxy you can see which cluster it belongs to (if any), who owns it, and whether it is **imported** from another instance. From here you can reach a galaxy's settings the same way its editor would, and you can move a galaxy into or out of a cluster.

The day-to-day authoring of a galaxy (its theme, its wormholes, its keywords) is editor work and lives in the Editor Manual. What is specific to you as administrator is the whole-instance view: seeing everything at once, and the two concerns below, imported content and clusters.

## Imported (read-only) galaxies

If your instance subscribes to a galaxy published by another instance (see *Federation and the Pluriverse*), that galaxy appears here as **imported**. An imported galaxy is a mirror: its content is copied to your instance so visitors can see it, but the authority for it stays with the instance that published it.

- Imported galaxies are **read-only** to everyone on your instance, editors and administrators alike. You cannot change their content, because the change has to happen at the source.
- A **Refresh** action pulls the latest version of an imported galaxy from its source, so your mirror catches up with edits made upstream. Federation also refreshes mirrors on a schedule; Refresh is the manual "now" button.
- If the source stops publishing the galaxy to you, or you stop subscribing, the mirror is dropped. The imported content was never yours to keep; it is present only while the subscription is.

The federation chapter covers subscribing, publishing, and blocking in full. Here it is enough to know that imported galaxies show up in this list, are read-only, and can be refreshed.

## The Clusters tab

A **cluster** groups galaxies. Clusters are how a family of related galaxies is presented together and how some instance settings are scoped to a subset of galaxies rather than the whole instance.

![The Clusters tab: a list of galaxy clusters, each with the galaxies it contains](assets/images/admin-manual/06-clusters-list.png)

From the Clusters tab you can create a cluster, name it, and put galaxies into it. A galaxy belongs to at most one cluster at a time. Clusters matter to an administrator for two reasons:

- They are a level in the **editing cascade** (see *Editor access control*): you can turn editing off for a whole cluster at once.
- They are a scope for **keyword matching**, below.

Self-service enrolment can also place each new editor's personal galaxy into a per-instance cluster automatically, so all the personal galaxies from an open call sit together rather than scattering through the list.

## Keyword matching (exact and fuzzy)

Telaris draws connections between wormholes that share a keyword. By default the match is **exact**: two wormholes connect only when they carry the very same word. You can loosen this to **fuzzy** matching, so near-spellings also connect: a plural and its singular, a small typo, a minor variant.

Fuzzy matching is a toggle, and it can be set at two scopes:

- for the **whole instance** (the toggle lives on the Global Settings tab, see *Global settings*), so every galaxy uses fuzzy matching, or
- for a **cluster** (in that cluster's own settings), so only that cluster's galaxies do.

It is **off by default**; connections stay exact until you turn it on. A guard keeps fuzzy matching from over-connecting on very common short words, so turning it on does not flood the network with spurious links, but it is still a change your editors will see (new relationship lines appearing between near-matched keywords across galaxies). Turn it on when your content's vocabulary drifts in spelling and you want those variants to connect; leave it off when your keywords are controlled and you want only exact matches to draw a line.

## Things worth knowing

- **You see everything; editors see their own.** The Galaxies tab is the one place with the whole instance in view. Use it to audit what exists, who owns it, and what came from outside.
- **Imported is not yours.** Read-only imported galaxies are a courtesy from another instance, present while the subscription lasts. Do not treat them as backup or as your content.
- **Fuzzy matching is a per-instance or per-cluster editorial choice**, not a per-wormhole one. If editors ask why near-spelled keywords are (or are not) connecting, this toggle is the answer.
