# Federation and the Pluriverse

Telaris instances can stand alone, or they can join a **federation**: a family of independent instances that can see and share each other's galaxies without any of them being in charge. This chapter covers your instance's side of that, and, for the person who runs the coordination site, the extra surface that comes with it.

Federation is optional. Many instances never turn it on, and a course or a personal archive rarely needs it. Turn to this chapter when you want your instance to be part of a wider network of Telaris instances.

## The shape of it

A federation is coordinated by a **Pluriverse**: a central site that keeps the directory of member instances and helps them find and trust one another. The Pluriverse is a coordinator, not an owner; it does not hold anyone's content, and no instance answers to it for editorial decisions. Each instance stays sovereign over its own galaxies.

Between two instances, sharing works in one direction at a time:

- an instance **publishes** a galaxy to a peer it trusts, and
- the peer **subscribes** and pulls a **read-only mirror** of that galaxy (the imported galaxies of the previous chapter).

Nothing is shared until both a trust relationship and a publish decision exist. Federation is opt-in at every step: you choose to join, you choose whom to trust, you choose what to publish, and you can withdraw any of it.

## Joining a Pluriverse

Your instance's participation is managed from the **Pluriverse** tab of the console. Joining is a request-and-admission flow: your instance applies to a Pluriverse, and that Pluriverse's operator admits it. Once admitted, your instance appears in the directory and can begin forming trust with peers.

![The Pluriverse tab on an instance not yet federated: the join-the-Pluriverse form with this instance's URL, name, and operator contact](assets/images/admin-manual/08-pluriverse.png)

## The peer list

The Pluriverse tab shows the peers your instance knows about, each with its status: discovered (known but not yet trusted), trusted (a mutual trust relationship exists), or blocked. A **Refresh** action updates the list from the Pluriverse now, rather than waiting for the scheduled refresh. There is also an advanced path to add a peer by hand, for a peer you know directly, which asks you to re-confirm because adding a peer by hand skips the directory's introduction.

## Establishing trust

Before two instances can share, they establish **trust**: a handshake in which each confirms the other's identity and both agree to be peers. You start or accept a handshake from the peer list; when it completes, the peer's status becomes trusted (whitelisted) on both sides. Trust is mutual and symmetric; it does not, by itself, share any content. It only makes sharing possible.

## Publishing your galaxies

To let a trusted peer mirror one of your galaxies, you **publish** it to that peer. Publishing is per galaxy and per peer: you decide, for each peer, which of your galaxies they may pull. A galaxy you have not published is invisible to peers, even trusted ones.

Publishing shares the galaxy's content, including its media, in a form the peer can verify came from you unaltered. You can **retract** a publication later; the peer's mirror is then dropped on its next pull. Publishing is a standing offer, not a one-time send: while it stands, the peer's mirror keeps up with your edits.

## Subscribing to a peer's galaxies

The other direction: when a trusted peer publishes a galaxy to you, you can **subscribe** to it and pull a read-only mirror. The mirror appears in your Galaxies tab as an imported galaxy (previous chapter), read-only, refreshable. You can unsubscribe to drop the mirror. What you may subscribe to is whatever your peers have chosen to publish to you; you cannot pull a galaxy that has not been published to you.

## Blocking a peer

If you need to sever a relationship, **block** the peer. Blocking is the strong stop: it drops any mirrors you pulled from them, withdraws anything you published to them, and stops further sharing in both directions. Blocking is deliberately uniform, it does not leave content half-shared, so it is the clean way to end a relationship that has gone wrong. Unblocking later returns the peer to merely discovered; it does not restore the content that blocking dropped, which would have to be re-published and re-pulled.

## For the Pluriverse operator

If you run the coordination site rather than only a member instance, you have an extra responsibility: **admission**. New instances apply to your Pluriverse, and you decide which to admit into the directory. Admission is a vetting step; you are deciding who belongs in this particular federation. The console surface for it lets you review a pending application and admit or decline it. Beyond admission, the operator keeps the directory honest: removing an instance that has gone permanently silent, and responding if a member reports a problem with a peer.

Running a Pluriverse does not give you power over members' content or editorial choices. It gives you the guest list, not the archive.

## Things worth knowing

- **Federation is entirely opt-in and reversible.** You join by choice, trust by choice, publish by choice, and can withdraw at each level. Nothing federates by default.
- **Imported galaxies are read-only and impermanent** (previous chapter). Treat a peer's published galaxy as a live view, not as your copy.
- **Blocking is uniform and final for the content it drops.** It is the right tool to end a bad relationship cleanly; it is not a pause. Use trust and publish/retract for softer adjustments.
- **Sovereignty is the whole point.** No instance, and not the Pluriverse, overrides another's editorial decisions. The only power a source has over a mirror is to stop publishing; the only power you have over what you imported is to stop subscribing.
