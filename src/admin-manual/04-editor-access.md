# Editor access control

Having an editor account is one thing; being able to edit a given galaxy is another. Telaris separates the two, so you can decide not only *who* is an editor but *what* each editor may touch. This chapter covers the two mechanisms: the editing switch that can be turned off at several levels, and the per-seat access that scopes an editor to specific galaxies.

## The editing switch (a cascade)

Editing can be turned on or off at four levels, from the widest to the narrowest:

- the **whole instance**,
- a **cluster** of galaxies,
- a single **galaxy**,
- a single **user**.

The switch cascades: turning editing off at a wider level turns it off for everything inside it, unless something narrower turns it back on. Turning off editing for the instance stops all editors; turning it off for one cluster stops editing in that cluster's galaxies; and so on. Editing is **on by default** at every level, so a fresh instance behaves as you would expect and you only reach for these switches when you want to stop something.

**Administrators are exempt.** The cascade never locks an administrator out of editing; it governs editors. This is deliberate, so you cannot accidentally switch off your own ability to fix things.

### When you would use it

- **A course or project has ended.** Turn editing off for the instance (or for that cluster) to freeze the content while keeping every account and everything they made. This is exactly what a demonstration instance does once its course is over: accounts and content stay, but nothing new can be edited.
- **A galaxy is being reviewed or handed over.** Turn editing off for that one galaxy while it is settled, without affecting the rest of the instance.
- **One editor should pause.** Turn editing off for a single user without touching anyone else.

The **Allow editors** switch in *Global settings* is the instance-level end of this cascade; the cluster, galaxy, and user levels are reached where those things are managed.

## Per-seat access: read-only and read-write

Editing being *on* still does not mean an editor can edit *everything*. An editor works on the galaxies they have a **seat** on, and each seat is either:

- **read-write**, the editor can change the galaxy's content, or
- **read-only**, the editor can see the galaxy in their editor view but cannot change it.

An editor always has read-write on the galaxies they created. Seats on other galaxies are granted: you (or the self-enrolment defaults) give an editor a seat on a galaxy, at the level you choose. A read-only seat is how you let someone study or reference a galaxy, or use it as a model, without being able to alter it. Read-only is also how imported content behaves for everyone: content mirrored from another instance is read-only to your editors, because the authority for it lives at its source (see *Galaxies and clusters*).

The two mechanisms combine. An editor can change a galaxy only when editing is on for them all the way up the cascade **and** they hold a read-write seat on that galaxy. If either is missing, the galaxy opens for them in a viewer state rather than an editor one.

## Things worth knowing

- **Off by default is nothing; the switches are opt-out.** You never have to turn editing on. You turn it off when you want to stop something, and back on when you are done.
- **Freezing is not deleting.** Turning editing off keeps every account and everything authored; it only prevents new changes. It is the safe way to end a project without discarding it.
- **Read-only is a first-class choice, not a lesser one.** Much of the value of a shared archive is being able to show a galaxy to collaborators who should not change it. Grant read-only seats freely.
