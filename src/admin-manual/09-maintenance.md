# Maintenance and diagnostics

This chapter gathers the operational odds and ends: the **API Keys** and **PHP Information** tabs, how the instance keeps its own database structure current, and where the few file-level settings live. You will visit these rarely, which is exactly why it helps to know what they are before you need them.

## API Keys

The instance's own front end reads content through an internal API, and that API is protected by a key. The **API Keys** tab is where those keys are managed: you can see the keys that exist and generate a new one.

For an instance that was set up normally, a default key already exists and everything works; you never need this tab. It matters in two situations:

- **A hand-provisioned instance with no key.** If an instance was set up by hand rather than through the normal setup, it may have no default key, and the visitor scene or the admin views fail to load content (a "failed to load" error). Generating a key here fixes that.
- **Rotating a key.** If a key should be replaced, generate a new one here.

Unless you are troubleshooting one of those, leave this tab alone.

## PHP Information

The **PHP Information** tab reports the server environment the instance runs on: the PHP version, which important extensions are present, and the full list of loaded extensions. It is a read-only diagnostic. Its purpose is to answer, quickly, "does this server have what Telaris needs?" when something behaves oddly, without you logging in to the server itself. If you ever report a problem to whoever manages the server, the version and extension information here is what they will ask for.

## How the database structure stays current

Telaris manages its own database structure. When the instance runs a newer version of the code than the database was last prepared for, it brings the structure up to date on its own, adding what the new version needs, the first time it is needed. There is no separate "run the migrations" step for you to perform after a deploy; the instance handles it.

This is why deploying an update is, in the normal case, just putting the new code in place; the instance does the rest on the next request. The **schema-mismatch banner** (see *Backups and snapshots*) is the exception, the signal that this self-updating did not complete, and the rest of that chapter covers what it means.

## The few file-level settings

Almost everything an administrator sets lives in the console and the database, which is where you should set it. A small number of foundational values, principally the database connection the instance uses, live in a configuration file on the server rather than in the console, because the instance needs them before it can reach its own database to read anything else. You will not normally touch that file; it is set once when the instance is installed. The settings you *do* change day to day, mail, the instance's address, the default language, the editor switch, are all in *Global settings*, in the console, precisely so you do not have to edit files to run the instance.

If you did not install the instance yourself and something at this level seems wrong (the instance cannot reach its database, or email links point at the wrong address), that is the point to involve whoever set the server up, or to consult the code repository's own installation reference.

## Things worth knowing

- **Most of these tabs are "in case of," not "day to day."** API Keys and PHP Information are troubleshooting surfaces; a healthy instance rarely needs either.
- **Deploying is putting new code in place; the instance updates its own structure.** You do not run migrations by hand.
- **The console is the place for settings, not files.** If you find yourself wanting to edit a file to change how the instance behaves, check *Global settings* first; the setting is probably there.
