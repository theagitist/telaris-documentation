# Introduction

This manual is for the person who runs a Telaris instance: the administrator. An administrator is not the same as an editor. An editor authors galaxies, wormholes, and connections inside the archive; an administrator decides who may edit, how the instance behaves, whether and how it connects to other instances, and how its data is kept safe. If your daily work is authoring content, the Editor Manual is your book; this one is for the surfaces an editor never sees.

## Three roles

It helps to keep three roles distinct, because this manual, the Editor Manual, and the day-to-day of running a Telaris network each speak to a different one.

- **Editor.** Someone with an editor account on your instance. They sign in, author content, and see only the editor surface. The Editor Manual is written for them.
- **Administrator (you).** Someone with an admin account on your instance. You reach the **Admin Console** and manage users, galaxies, settings, backups, and your instance's participation in the wider network. This manual is written for you.
- **Pluriverse operator.** The person who runs the central coordination site (the Pluriverse) that a family of instances federates through. Much of that work is the same admin console you already know; the parts that are specific to running the Pluriverse are gathered in the federation chapter. On a small network the administrator and the Pluriverse operator are often the same person.

A single account can, of course, be both an editor and an administrator. The distinction is about *surfaces*, not people: the admin console is a separate place from the editor home, reached separately, and this manual is your guide to it.

## Reaching the Admin Console

The Admin Console lives at the `/admin` path of your instance (for example, `https://your-instance.example.org/admin`). You must be signed in with an account that has the administrator role; an ordinary editor account that opens `/admin` is turned away.

Across the top of the console is a row of tabs. Each is a chapter of this manual:

- **Galaxies** and **Clusters**: the administrator's view of all content on the instance, including content imported from elsewhere. Covered in *Galaxies and clusters*.
- **Users**: every account on the instance, and the tools to create, edit, vet, and remove them. Covered in *Users* and *Self-service editor enrolment*.
- **Backup** and **Snapshots**: making and restoring copies of the whole instance. Covered in *Backups and snapshots*.
- **Global Settings**: mail, the instance's own address, the default language, and the instance-wide switch for editors. Covered in *Global settings*.
- **Pluriverse**: your instance's participation in a federation of instances. Covered in *Federation and the Pluriverse*.
- **API Keys** and **PHP Information**: operational odds and ends and diagnostics. Covered in *Maintenance and diagnostics*.

## What this manual assumes

It assumes the instance is already installed and running, and that you can sign in as an administrator. It does not cover installing Telaris on a server from nothing; that is a matter of the deployment method you chose (a direct checkout, a container image, or a hosted instance provisioned for you), and the code repository's own README is the reference for it. What this manual covers is everything you do *after* the instance is up: running it well, keeping it safe, and deciding how open it is.

## A note on language and terms

The console, like the rest of Telaris, is fully translated. Screens shown here are in English; your console may be in Spanish, Portuguese, or French, and the labels differ accordingly. Where this manual names a control, it names the English label; find the same control in your own language by its position, which is the same in every locale.

Telaris also keeps a deliberate split between the words visitors and editors read and the words the code uses. You will see *galaxy*, *wormhole*, and *portal* in the interface; the underlying data calls them *constellation*, *node*, and *portal*. This manual uses the interface words throughout. The glossary at the end collects the terms an administrator meets.
