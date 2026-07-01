#!/usr/bin/env python3
"""Capture admin-manual screenshots from a live Telaris instance.

Mirrors capture_editor_screenshots.py, but logs into an ADMIN account and
shoots the Admin Console tabs (Users, Galaxies, Clusters, Global Settings,
Pluriverse, Backup). Because the Users and Pluriverse tabs would expose real
account/peer data on a production instance, this is meant to run against a
DISPOSABLE instance seeded with synthetic data only.

Credentials come from the environment (never source):
    TELARIS_ADMIN_URL       base URL of the throwaway instance (no trailing /)
    TELARIS_ADMIN_USERNAME  admin login email
    TELARIS_ADMIN_PASSWORD  admin password

    set -a; source ~/.throwaway-admin-creds; set +a
    python3 tools/capture_admin_screenshots.py --locale en
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent

ACCEPT_LANGUAGE_HEADERS = {
    "en": "en-CA,en;q=0.9",
    "es": "es-ES,es;q=0.9",
    "pt": "pt-BR,pt;q=0.9",
    "fr": "fr-CA,fr;q=0.9",
}

VIEWPORT = {"width": 1440, "height": 900}
DEVICE_PIXEL_RATIO = 1.0


def shots_dir_for(locale: str) -> Path:
    if locale == "en":
        return REPO_ROOT / "assets" / "images" / "admin-manual"
    return REPO_ROOT / "assets" / "images" / f"admin-manual-{locale}"


def env_required(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        sys.exit(f"missing environment variable: {key}")
    return val


def login(page: Page, base_url: str, email: str, password: str) -> None:
    """Same passwordless-friendly login as the editor script: open the
    'I have a password' disclosure, then submit the password branch."""
    page.goto(f"{base_url}/utils/login.php", wait_until="domcontentloaded")
    page.fill('input[name="email"]', email)
    page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
    page.fill('input[name="password"]', password)
    page.click('button[name="action"][value="password"]')
    page.wait_for_load_state("networkidle", timeout=20_000)


@dataclass
class Shot:
    name: str
    tab: str          # ?tab= key
    description: str = ""


SHOTS: list[Shot] = [
    Shot("02-users-list", "users",
         "Users tab: synthetic accounts with name, email, role, vetted state."),
    Shot("05-galaxies-list", "constellations",
         "Galaxies tab: every galaxy on the instance with cluster and owner."),
    Shot("06-clusters-list", "clusters",
         "Clusters tab: galaxy clusters and their members."),
    Shot("07-global-settings", "settings",
         "Global Settings tab: mail settings, site settings, Allow-editors switch."),
    Shot("08-pluriverse", "pluriverse",
         "Pluriverse tab: federation status and the known-peers list."),
    Shot("09-backup", "backup",
         "Backup tab: Download-a-backup and Restore-from-a-backup panels."),
]


def capture_one(page: Page, base_url: str, shot: Shot, shots_dir: Path) -> Path:
    target = shots_dir / f"{shot.name}.png"
    page.goto(f"{base_url}/admin/index.php?tab={shot.tab}", wait_until="domcontentloaded")
    # Make sure the right pane is shown even if the on-load JS re-syncs tabs.
    page.evaluate(f"if (typeof showTab === 'function') showTab('{shot.tab}');")
    # Admin lists (users/galaxies/clusters) hydrate via fetch; let them settle.
    page.wait_for_load_state("networkidle", timeout=15_000)
    page.wait_for_timeout(2200)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(300)
    page.screenshot(path=str(target), full_page=False)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture admin-manual screenshots in a locale.")
    parser.add_argument("--locale", choices=["en", "es", "pt", "fr"], default="en")
    parser.add_argument("--shots", default="",
                        help="Comma-separated shot names/prefixes. Empty = all.")
    args = parser.parse_args()
    locale = args.locale
    shot_filter = [s.strip() for s in args.shots.split(",") if s.strip()]

    shots = SHOTS
    if shot_filter:
        shots = [s for s in SHOTS if any(s.name == f or s.name.startswith(f) for f in shot_filter)]
        if not shots:
            sys.exit(f"no shots matched: {shot_filter}")

    base_url = env_required("TELARIS_ADMIN_URL").rstrip("/")
    email = env_required("TELARIS_ADMIN_USERNAME")
    password = env_required("TELARIS_ADMIN_PASSWORD")

    shots_dir = shots_dir_for(locale)
    shots_dir.mkdir(parents=True, exist_ok=True)
    print(f"locale: {locale}  ->  {shots_dir}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=DEVICE_PIXEL_RATIO,
            locale=locale,
            extra_http_headers={"Accept-Language": ACCEPT_LANGUAGE_HEADERS[locale]},
        )
        page = context.new_page()
        page.on("pageerror", lambda exc: print(f"  [page error] {exc}"))
        page.on("response", lambda r: (
            print(f"  [response {r.status}] {r.request.method} {r.url}")
            if r.status >= 400 else None))

        print("logging in...")
        login(page, base_url, email, password)
        print(f"logged in as {email}")

        for shot in shots:
            time.sleep(8)  # Cloudflare per-IP pacing
            out = capture_one(page, base_url, shot, shots_dir)
            print(f"captured {out}")

        browser.close()

    print(f"\nall shots in {shots_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
