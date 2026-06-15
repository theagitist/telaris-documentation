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

# Per-locale Accept-Language headers. EN uses no header (default UI),
# ES + PT receive the standard regional variant so the app's
# locale_resolve_from_request() returns the right code.
ACCEPT_LANGUAGE_HEADERS = {
    "en": "en-CA,en;q=0.9",
    "es": "es-ES,es;q=0.9",
    "pt": "pt-BR,pt;q=0.9",
    "fr": "fr-CA,fr;q=0.9",
}

def shots_dir_for(locale: str) -> Path:
    """EN shots stay in assets/images/editor-manual/ for backwards compat;
    ES / PT shots go into assets/images/editor-manual-<locale>/ so each
    manual references its own image directory."""
    if locale == "en":
        return REPO_ROOT / "assets" / "images" / "editor-manual"
    return REPO_ROOT / "assets" / "images" / f"editor-manual-{locale}"

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
    """Submit the login form and wait for the post-login redirect.

    The login page leads with the passwordless "email me a sign-in link"
    button and keeps the password field inside a collapsed <details> ("I have
    a password"). Open that disclosure first, then submit the password branch
    explicitly (its button carries name=action value=password) so we do not
    trip the sign-in-link button, which is the first submit on the form.
    """
    page.goto(f"{base_url}/utils/login.php", wait_until="domcontentloaded")
    page.fill('input[name="email"]', email)
    # Reveal the password field (it sits in a collapsed <details>).
    page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
    page.fill('input[name="password"]', password)
    page.click('button[name="action"][value="password"]')
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
    Shot(
        name="03-editor-home-single-galaxy",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=None,
        full_page=False,
        description="Editor home when a specific galaxy is selected: View, Settings, Canvas buttons appear next to the picker.",
    ),
    Shot(
        name="04-galaxy-settings-modal",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_galaxy_settings_modal(page),
        full_page=False,
        description="Galaxy settings modal opened from the editor home (name, tagline, theme, tags, discovery section).",
    ),
    Shot(
        name="05-new-wormhole-modal",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_create_wormhole_modal(page),
        full_page=False,
        description="New Wormhole modal (empty fields, Object/Portal type radios, keyword input).",
    ),
    Shot(
        name="06-edit-wormhole-modal",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_edit_wormhole_modal(page, "Beach Strawberry"),
        full_page=False,
        description="Edit Wormhole modal for Beach Strawberry (filled fields, media tabs visible).",
    ),
    Shot(
        name="07-media-video-tab",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_create_modal_on_tab(page, "video"),
        full_page=False,
        description="New Wormhole modal with the Video (MP4) media tab active.",
    ),
    Shot(
        name="08-media-pdf-tab",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_create_modal_on_tab(page, "pdf"),
        full_page=False,
        description="New Wormhole modal with the PDF media tab active.",
    ),
    Shot(
        name="09-bulk-by-keyword-modal",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_bulk_by_keyword_modal(page),
        full_page=False,
        description="Bulk by keyword modal: keyword list with counts and bulk-action buttons.",
    ),
    Shot(
        name="10-keyword-canvas",
        route="/edit/keyword-canvas.php?galaxy_id=413",
        prepare=lambda page: wait_for_canvas(page),
        full_page=False,
        description="Keyword canvas: pastel chips with relation lines drawn between them.",
    ),
    Shot(
        name="11-portal-type-selector",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_create_modal_as_portal(page),
        full_page=False,
        description="New Wormhole modal with Wormhole type set to Portal: target-galaxy dropdown visible.",
    ),
    Shot(
        name="12-galaxy-discovery-section",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_galaxy_settings_modal_scrolled(page),
        full_page=False,
        description="Galaxy settings modal scrolled to the Discovery section (auto-tour, idle spotlight, chips, related, 2D view).",
    ),
    Shot(
        name="13-visitor-scene",
        route="/manual-demo-coastal-plants",
        prepare=lambda page: wait_for_visitor_scene(page),
        full_page=False,
        description="Visitor 3D scene for the Coastal plants demo galaxy.",
    ),
    Shot(
        name="14-media-hotglue-tab",
        route="/edit/?slug=manual-demo-coastal-plants",
        prepare=lambda page: open_edit_modal_on_hotglue_tab(page, "Beach Strawberry"),
        full_page=False,
        description="Edit Wormhole modal with the Hotglue media tab active: the help line and the centered Edit hotglue content button.",
    ),
]


def open_edit_modal_on_hotglue_tab(page: Page, wormhole_name: str) -> None:
    """Open the Edit Wormhole modal, switch the Media section to the Hotglue
    tab, and centre the media block so the help line and the Edit-hotglue-content
    button are framed."""
    open_edit_wormhole_modal(page, wormhole_name)
    page.click("#edit-media-hotglue-tab")
    page.wait_for_timeout(400)
    page.evaluate("""(() => {
        const el = document.getElementById('edit-media-hotglue-content');
        if (el) el.scrollIntoView({block: 'center'});
    })()""")
    page.wait_for_timeout(500)


def open_galaxy_settings_modal_scrolled(page: Page) -> None:
    """Open the galaxy settings modal and scroll to the Discovery section."""
    open_galaxy_settings_modal(page)
    # Scroll the modal body so the Discovery toggles section is in view.
    # page.evaluate runs the expression as a function body but a bare `return`
    # at the top level is a syntax error; wrap in an IIFE.
    page.evaluate("""(() => {
        const modal = document.querySelector('#constellation_modal');
        if (!modal) return;
        const body = modal.querySelector('.modal-box, .modal-content, form, [class*="overflow"]')
                  || modal;
        body.scrollTop = body.scrollHeight;
    })()""")
    page.wait_for_timeout(600)


def wait_for_visitor_scene(page: Page) -> None:
    """Let the visitor 3D scene paint a few animation frames."""
    # The Three.js scene paints asynchronously after a few hundred ms.
    page.wait_for_load_state("networkidle", timeout=20_000)
    page.wait_for_timeout(3500)


def open_create_modal_as_portal(page: Page) -> None:
    """Open the New Wormhole modal and switch the type to Portal."""
    open_create_wormhole_modal(page)
    page.select_option("#node-type", "portal")
    page.wait_for_timeout(500)


def wait_for_canvas(page: Page) -> None:
    """Let the keyword canvas hydrate (SVG + chip positions + relation lines)."""
    page.wait_for_load_state("networkidle", timeout=15_000)
    # The canvas paints animations + force-simulation tick frames; let it settle
    # so the chips are not mid-flight in the screenshot.
    page.wait_for_timeout(2500)


def open_bulk_by_keyword_modal(page: Page) -> None:
    """Open the Bulk by keyword modal via its trigger button."""
    page.wait_for_selector("#bulk-by-keyword-btn", timeout=15_000)
    page.wait_for_timeout(800)  # let the wormhole list finish loading first
    page.click("#bulk-by-keyword-btn")
    page.wait_for_selector("#bulk_by_keyword_modal[open]", timeout=10_000)
    page.wait_for_timeout(800)


def open_create_modal_on_tab(page: Page, tab: str) -> None:
    """Open the New Wormhole modal and switch the primary-visual tab.

    `tab` is one of 'image' (default), 'video', or 'pdf'. Image is the
    starting state; for other tabs we click the corresponding tab button.
    """
    open_create_wormhole_modal(page)
    if tab != "image":
        page.click(f"#create-{tab}-tab")
        page.wait_for_timeout(400)


def open_galaxy_settings_modal(page: Page) -> None:
    """Click the Settings button next to the galaxy picker and wait for the modal."""
    page.wait_for_selector("#galaxy-settings-btn:visible", timeout=10_000)
    page.click("#galaxy-settings-btn")
    page.wait_for_selector("dialog[open], .modal-open, #constellation_modal", timeout=10_000)
    page.wait_for_timeout(800)


def open_create_wormhole_modal(page: Page) -> None:
    """Open the New Wormhole modal by calling the global JS function."""
    # Wait for the wormhole list to render at least one visible row. The
    # selector below matches the row body (the area you'd click to open a
    # wormhole for edit); it is visible as soon as the list paints.
    page.wait_for_selector(
        '#nodes-list [onclick*="editNode"]:visible',
        timeout=20_000,
    )
    page.evaluate("openCreateNodeModal()")
    page.wait_for_selector("#create_node_modal[open]", timeout=10_000)
    page.wait_for_timeout(600)


# Wormhole IDs from tools/seed_demo_content.php. The seed creates rows in a
# deterministic order on a fresh install, so these IDs are stable for the
# demo content. If the demo is re-seeded with shifted IDs, refresh via:
#   php -r 'require_once "/var/www/starmaps.polivoxia.ca/config.php"; require_once "/var/www/starmaps.polivoxia.ca/inc/db.php"; foreach (getDB()->query("SELECT id, name FROM nodes WHERE constellation_id IN (412,413) ORDER BY id")->fetchAll() as $r) printf("  %s => %d,\n", $r["name"], $r["id"]);'
DEMO_WORMHOLE_IDS = {
    "Beach Strawberry": 279,
    "Sea Lavender": 280,
    "Yellow Bush Lupine": 282,
    "Coastal Sage": 285,
    "Coastal field guide": 290,
    "To the tide pools": 291,
    "Sea Palm": 289,
}


def open_edit_wormhole_modal(page: Page, wormhole_name: str) -> None:
    """Open the Edit Wormhole modal for one of the demo wormholes."""
    if wormhole_name not in DEMO_WORMHOLE_IDS:
        raise RuntimeError(f"unknown demo wormhole: {wormhole_name!r}; "
                           f"add it to DEMO_WORMHOLE_IDS")
    node_id = DEMO_WORMHOLE_IDS[wormhole_name]
    page.wait_for_selector("#nodes-list", timeout=15_000)
    page.wait_for_timeout(1500)  # let async list render settle
    page.evaluate(f"editNode({node_id})")
    page.wait_for_selector("#edit_modal[open]", timeout=10_000)
    page.wait_for_timeout(1200)  # let media tabs and keyword chips populate


# ---------------------------------------------------------------------------
# Capture orchestration.
# ---------------------------------------------------------------------------

def capture_one(page: Page, base_url: str, shot: Shot, shots_dir: Path) -> Path:
    target = shots_dir / f"{shot.name}.png"
    page.goto(f"{base_url}{shot.route}", wait_until="domcontentloaded")
    if shot.prepare:
        shot.prepare(page)
    # Settle: give animations and lazy-loaded content a moment.
    page.wait_for_load_state("networkidle", timeout=10_000)
    page.screenshot(path=str(target), full_page=shot.full_page)
    return target


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Capture editor-manual screenshots in a target locale.")
    parser.add_argument("--locale", choices=["en", "es", "pt", "fr"], default="en",
                        help="UI locale to capture against (sent via Accept-Language). Defaults to en.")
    parser.add_argument("--shots", default="",
                        help="Comma-separated shot names (or name prefixes) to capture. "
                             "Empty means all shots. Example: '04-galaxy-settings-modal,10-keyword-canvas'.")
    args = parser.parse_args()
    locale = args.locale
    shot_filter = [s.strip() for s in args.shots.split(",") if s.strip()]

    shots_to_capture = SHOTS
    if shot_filter:
        shots_to_capture = [s for s in SHOTS
                            if any(s.name == f or s.name.startswith(f) for f in shot_filter)]
        if not shots_to_capture:
            sys.exit(f"no shots matched filter: {shot_filter}")
        print(f"shot filter: {[s.name for s in shots_to_capture]}")

    base_url = env_required("TELARIS_EDITOR_URL").rstrip("/")
    email = env_required("TELARIS_EDITOR_USERNAME")
    password = env_required("TELARIS_EDITOR_PASSWORD")

    shots_dir = shots_dir_for(locale)
    shots_dir.mkdir(parents=True, exist_ok=True)
    print(f"locale: {locale}  ->  shots dir: {shots_dir}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=DEVICE_PIXEL_RATIO,
            locale=locale,
            extra_http_headers={"Accept-Language": ACCEPT_LANGUAGE_HEADERS[locale]},
        )
        page = context.new_page()

        # Surface page console errors so capture-time bugs are visible.
        page.on("pageerror", lambda exc: print(f"  [page error] {exc}"))
        page.on("console", lambda msg: (
            print(f"  [console.{msg.type}] {msg.text}")
            if msg.type in ("error", "warning") else None
        ))
        # Surface failed network requests too.
        page.on("requestfailed", lambda req: print(
            f"  [request failed] {req.method} {req.url}: {req.failure}"
        ))
        page.on("response", lambda r: (
            print(f"  [response {r.status}] {r.request.method} {r.url}")
            if r.status >= 400 else None
        ))

        # Capture the login page BEFORE authenticating, since the post-login
        # redirect leaves no clean way back to a fresh login form. Only if the
        # login shot is in the active filter (or no filter is set).
        login_in_filter = any(s.name == "01-login-form" for s in shots_to_capture)
        if login_in_filter:
            login_shot = next(s for s in SHOTS if s.name == "01-login-form")
            out = capture_one(page, base_url, login_shot, shots_dir)
            print(f"captured {out}")

        # Authenticate.
        print("logging in...")
        login(page, base_url, email, password)
        print(f"logged in as {email}")

        # Capture the rest. Pace requests so Cloudflare's rate limiter does
        # not throttle the editor API and leave the page in an error state
        # behind the modal we are screenshotting. Six seconds between shots
        # is comfortable for the per-IP rate limiter under a chain of ~10
        # API calls per shot.
        import time
        for shot in shots_to_capture:
            if shot.name == "01-login-form":
                continue
            time.sleep(10)
            out = capture_one(page, base_url, shot, shots_dir)
            print(f"captured {out}")

        browser.close()

    print(f"\nall shots in {shots_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
