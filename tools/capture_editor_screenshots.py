#!/usr/bin/env python3
"""Capture editor-manual screenshots from a live Telaris instance.

Runs a headless Chromium browser via Playwright, logs into the editor
surface as the screenshot-capture account, navigates a list of named
"shots" (each describing a route plus framing instructions), and saves
PNGs into assets/images/editor-manual/. Re-runnable: each invocation
overwrites the existing PNGs, so the manual can be refreshed against the
current UI at any time.

Credentials are read from the environment so they never land in source:
    TELARIS_EDITOR_URL        base URL of the instance (no trailing slash)
    TELARIS_EDITOR_USERNAME   editor login email
    TELARIS_EDITOR_PASSWORD   editor login password

Suggested workflow:
    set -a; source ~/.telaris-capture-credentials; set +a
    python3 tools/capture_editor_screenshots.py

The shot list is small to start (just enough to verify login + capture).
It grows as the manual draft references more screenshots.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from playwright.sync_api import Page, sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
SHOTS_DIR = REPO_ROOT / "assets" / "images" / "editor-manual"

# Standard editor-manual screenshot dimensions. 1440x900 matches a common
# laptop viewport and keeps shots readable when scaled down for print.
VIEWPORT = {"width": 1440, "height": 900}

# Crop factor for headless device-pixel-ratio: keep 1x so the PNG dimensions
# match the viewport (no Retina-style 2x).
DEVICE_PIXEL_RATIO = 1.0


# ---------------------------------------------------------------------------
# Auth.
# ---------------------------------------------------------------------------

def env_required(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        sys.exit(f"missing environment variable: {key}")
    return val


def login(page: Page, base_url: str, email: str, password: str) -> None:
    """Submit the login form and wait for the post-login redirect."""
    page.goto(f"{base_url}/utils/login.php", wait_until="domcontentloaded")
    page.fill('input[name="email"]', email)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"], input[type="submit"]')
    # The login redirects to /admin/ or /edit/ depending on user type.
    page.wait_for_load_state("networkidle", timeout=15_000)


# ---------------------------------------------------------------------------
# Shot definitions.
#
# Each Shot has:
#   name      filename stem (becomes assets/images/editor-manual/<name>.png)
#   route     path relative to TELARIS_EDITOR_URL (no leading scheme)
#   prepare   optional callable(page) for any setup before the shot
#             (open a modal, scroll to an element, click a tab, etc.)
#   full_page True to capture the full scrollable page; False for viewport-only
# ---------------------------------------------------------------------------

@dataclass
class Shot:
    name: str
    route: str
    prepare: Callable[[Page], None] | None = None
    full_page: bool = False
    description: str = ""


def shot_login_page(page: Page) -> None:
    # No-op; the login page has nothing to prepare. Special-cased below
    # because it has to be visited before authentication.
    pass


# A small starter set. The list extends as the manual draft needs more shots.
SHOTS: list[Shot] = [
    Shot(
        name="01-login-form",
        route="/utils/login.php",
        prepare=None,
        full_page=False,
        description="Login form, empty fields, the very first screen an editor sees.",
    ),
    Shot(
        name="02-editor-home",
        route="/edit/",
        prepare=None,
        full_page=False,
        description="Editor home: galaxy picker, wormhole list, the top-level workspace.",
    ),
]


# ---------------------------------------------------------------------------
# Capture orchestration.
# ---------------------------------------------------------------------------

def capture_one(page: Page, base_url: str, shot: Shot) -> Path:
    target = SHOTS_DIR / f"{shot.name}.png"
    page.goto(f"{base_url}{shot.route}", wait_until="domcontentloaded")
    if shot.prepare:
        shot.prepare(page)
    # Settle: give animations and lazy-loaded content a moment.
    page.wait_for_load_state("networkidle", timeout=10_000)
    page.screenshot(path=str(target), full_page=shot.full_page)
    return target


def main() -> int:
    base_url = env_required("TELARIS_EDITOR_URL").rstrip("/")
    email = env_required("TELARIS_EDITOR_USERNAME")
    password = env_required("TELARIS_EDITOR_PASSWORD")

    SHOTS_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=DEVICE_PIXEL_RATIO,
        )
        page = context.new_page()

        # Capture the login page BEFORE authenticating, since the post-login
        # redirect leaves no clean way back to a fresh login form.
        login_shot = next(s for s in SHOTS if s.name == "01-login-form")
        out = capture_one(page, base_url, login_shot)
        print(f"captured {out}")

        # Authenticate.
        print("logging in...")
        login(page, base_url, email, password)
        print(f"logged in as {email}")

        # Capture the rest.
        for shot in SHOTS:
            if shot.name == "01-login-form":
                continue
            out = capture_one(page, base_url, shot)
            print(f"captured {out}")

        browser.close()

    print(f"\nall shots in {SHOTS_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
