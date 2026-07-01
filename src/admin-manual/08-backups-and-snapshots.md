# Backups and snapshots

An instance is content, and content should be recoverable. Telaris gives you two related tools: **backups** you download and keep, and **snapshots** the instance takes and stores for you, on a schedule if you like. This chapter covers both, and how to restore.

## Backups (the Backup tab)

![The Backup tab: a Download-a-backup panel and a Restore-from-a-backup panel](assets/images/admin-manual/09-backup.png)

The **Backup** tab has two halves:

- **Download a backup** produces a single file capturing the instance's content, which your browser downloads. Keep it somewhere safe and off the server. This is the copy you take before anything risky, and the copy you would use to move an instance or recover from a lost server.
- **Restore from a backup** takes a backup file and loads it back into the instance, replacing the current content. Restoring is destructive to what is there now, so Telaris confirms first. Restore onto a fresh or intended-to-be-overwritten instance; do not restore over content you still want.

A backup is portable: you can restore it onto another instance to clone or migrate. Remember, from *Global settings*, that the mail password is never in a backup; after restoring, re-enter the mail settings so the restored instance can send.

## Snapshots (the Snapshots tab)

Where a backup is a file you look after, a **snapshot** is a copy the instance keeps for you. The Snapshots tab has three parts:

- **Create snapshot now** takes a snapshot on demand. Do this before a bulk change or any edit you are unsure of, so there is a recent point to return to.
- **Snapshot scheduler** takes snapshots automatically at an interval you set, and keeps a rolling number of them, so there is always a recent snapshot without you remembering to make one. Turn it on for any instance whose content matters.
- **Available snapshots** lists the snapshots on hand, newest first, each restorable in place.

Snapshots are the everyday safety net: cheap, frequent, and close by. Backups are the off-site insurance: fewer, deliberate, and kept away from the server. Use both, snapshots for "undo," downloaded backups for "the server is gone."

## Restoring

Restoring, from either a downloaded backup or a stored snapshot, replaces current content with the saved content. Because it overwrites, treat it as a considered act:

1. Be sure you are restoring the version you mean to. Snapshots are timestamped; check the time.
2. Understand that edits made since that point will be gone after the restore.
3. If in any doubt, download a backup of the *current* state first, so even the state you are about to overwrite is recoverable.

When a restore completes, the console confirms it. Sign in again if the session was affected, and spot-check a galaxy to confirm the content is what you expected.

## The schema-mismatch banner

Telaris keeps its database structure in step with the running code automatically; when you deploy a new version, the instance brings its own structure up to date on its own. If the code and the database structure ever disagree in a way the instance cannot reconcile silently, the console shows a **schema-mismatch banner**. It is a signal that a deploy did not finish cleanly, not a routine state. If you see it, the safe response is to make sure the instance is running the intended version of the code and let it complete its structure update; if it persists, that is the moment to look at the deployment or ask whoever manages the server. Do not restore a backup to "fix" a schema banner; restoring content does not change the code-versus-structure mismatch.

## Things worth knowing

- **Back up before anything irreversible.** A bulk change, a restore, a big deletion: take a snapshot or download a backup first. It costs seconds and saves the day you need it.
- **Keep at least one backup off the server.** A snapshot stored on the same server is no help if the server is what you lose. Download a backup periodically and keep it elsewhere.
- **The mail password is not in backups or snapshots.** After restoring or cloning, re-enter mail settings (*Global settings*).
- **Test a restore before you depend on it.** If recovery matters, prove that a backup restores cleanly onto a spare instance once, rather than discovering a problem during a real recovery.
