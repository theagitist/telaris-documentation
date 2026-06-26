#!/usr/bin/env python3
"""Capture hotglue-manual screenshots from the live starmaps instance.

Mirrors tools/capture_editor_screenshots.py (same login, env, locale, and
Accept-Language machinery) but with a hotglue-specific shot list. Screenshots
land in assets/images/hotglue-manual/ (EN) or assets/images/hotglue-manual-<loc>/.

The Hotglue editor UI is localized (fork `telaris` i18n, wired via &lang=),
so each locale run produces screenshots with the editor chrome in that
language. The demo PAGE CONTENT is locale-independent; only the editor menus,
tooltips, prompts, and the surrounding Telaris controls change language.

Prereqs:
  - tools/seed_hotglue_demo.php has been run (seeds the Masterworks demo galaxy,
    its painting pages, and the registry rows the list view shows).
  - credentials sourced:
        set -a; source ~/.telaris-capture-credentials; set +a

Usage:
    python3 tools/capture_hotglue_screenshots.py                 # all, EN
    python3 tools/capture_hotglue_screenshots.py --locale es     # Spanish
    python3 tools/capture_hotglue_screenshots.py --shots 04,05   # subset
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from playwright.sync_api import Page, sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
SLUG = "hotglue-manual"

ACCEPT_LANGUAGE_HEADERS = {
    "en": "en-CA,en;q=0.9",
    "es": "es-ES,es;q=0.9",
    "pt": "pt-BR,pt;q=0.9",
    "fr": "fr-CA,fr;q=0.9",
}

VIEWPORT = {"width": 1440, "height": 900}
PHONE_VIEWPORT = {"width": 390, "height": 844}  # iPhone-ish portrait
DEVICE_PIXEL_RATIO = 1.0

# The demo wormhole the seed script composes a page on.
DEMO_NODE_ID = 296   # The Great Wave off Kanagawa (Masterworks demo galaxy)
DEMO_SLUG = "manual-demo-masterworks"


def shots_dir_for(locale: str) -> Path:
    if locale == "en":
        return REPO_ROOT / "assets" / "images" / SLUG
    return REPO_ROOT / "assets" / "images" / f"{SLUG}-{locale}"


def env_required(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        sys.exit(f"missing environment variable: {key}")
    return val


def login(page: Page, base_url: str, email: str, password: str) -> None:
    page.goto(f"{base_url}/utils/login.php", wait_until="domcontentloaded")
    page.fill('input[name="email"]', email)
    page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
    page.fill('input[name="password"]', password)
    page.click('button[name="action"][value="password"]')
    page.wait_for_load_state("networkidle", timeout=15_000)


# ---------------------------------------------------------------------------
# Prepare helpers.
# ---------------------------------------------------------------------------

def open_edit_modal_on_hotglue_tab(page: Page) -> None:
    """Edit-wormhole modal, Media section switched to the Hotglue tab, framed on
    the help line + the Edit-hotglue-content button."""
    page.wait_for_selector("#nodes-list", timeout=15_000)
    page.wait_for_timeout(1500)
    page.evaluate(f"editNode({DEMO_NODE_ID})")
    page.wait_for_selector("#edit_modal[open]", timeout=10_000)
    page.wait_for_timeout(1000)
    page.click("#edit-media-hotglue-tab")
    page.wait_for_timeout(400)
    page.evaluate("""(() => {
        const el = document.getElementById('edit-media-hotglue-content');
        if (el) el.scrollIntoView({block: 'center'});
    })()""")
    page.wait_for_timeout(500)


def open_hotglue_content_list(page: Page) -> None:
    """Switch the editor to the Hotglue-content view and wait for the seeded
    rows to render."""
    page.wait_for_selector("#etab-hotglue", timeout=15_000)
    page.wait_for_timeout(800)
    page.evaluate("switchEditorTab('hotglue')")
    page.wait_for_selector("#editor-tab-hotglue:not(.hidden)", timeout=15_000)
    # the row list loads via fetch; give it a moment to populate.
    page.wait_for_timeout(2500)


def wait_for_canvas(page: Page) -> None:
    """Let the hotglue edit canvas hydrate (jQuery + $.glue + the objects)."""
    page.wait_for_function("window.jQuery && window.jQuery.glue", timeout=15_000)
    # objects render after a few hundred ms; settle so text is laid out.
    page.wait_for_timeout(2500)


def show_menu(name: str) -> Callable[[Page], None]:
    """Open one of the canvas menus (`new` or `page`) at a fixed spot."""
    def _prep(page: Page) -> None:
        wait_for_canvas(page)
        # open the menu over the empty lower-left canvas so it does not cover
        # the demo page content.
        ok = page.evaluate(
            f"(() => {{ if (window.jQuery && jQuery.glue && jQuery.glue.menu) "
            f"{{ jQuery.glue.menu.show('{name}', 300, 640); return true; }} return false; }})()"
        )
        if not ok:
            print(f"  [warn] menu '{name}' could not be shown")
        page.wait_for_selector(".glue-menu", timeout=5_000)
        page.wait_for_timeout(500)
    return _prep


# ---------------------------------------------------------------------------
# Shot definitions.
# ---------------------------------------------------------------------------

@dataclass
class Shot:
    name: str
    route: str                         # {locale} is substituted
    prepare: Callable[[Page], None] | None = None
    full_page: bool = False
    phone: bool = False                # capture in a phone-sized context
    description: str = ""


SHOTS: list[Shot] = [
    Shot(
        name="01-hotglue-tab",
        route=f"/edit/?slug={DEMO_SLUG}",
        prepare=open_edit_modal_on_hotglue_tab,
        description="Edit-wormhole modal with the Hotglue media tab active: help line + Edit hotglue content button.",
    ),
    Shot(
        name="02-hotglue-content-list",
        route="/edit/",
        prepare=open_hotglue_content_list,
        description="The Hotglue content view: the page list with Title, Assigned wormhole, Updated, Actions.",
    ),
    Shot(
        name="03-canvas",
        route="/hg/?node-296/edit&lang={locale}",
        prepare=wait_for_canvas,
        description="The Hotglue edit canvas with The Great Wave demo page.",
    ),
    Shot(
        name="04-new-menu",
        route="/hg/?node-296/edit&lang={locale}",
        prepare=show_menu("new"),
        description="The NEW menu open on the canvas (tools for adding objects).",
    ),
    Shot(
        name="05-page-menu",
        route="/hg/?node-296/edit&lang={locale}",
        prepare=show_menu("page"),
        description="The PAGE menu open on the canvas (whole-page tools).",
    ),
    Shot(
        name="06-on-phone",
        # node-297 = The Starry Night, a deliberately narrow page
        route="/hg/?node-297&lang={locale}",
        prepare=lambda page: page.wait_for_timeout(2500),
        phone=True,
        description="A narrow published page scaled to fit a phone screen.",
    ),
]


def capture_one(page: Page, base_url: str, shot: Shot, shots_dir: Path, locale: str) -> Path:
    target = shots_dir / f"{shot.name}.png"
    route = shot.route.format(locale=locale)
    page.goto(f"{base_url}{route}", wait_until="domcontentloaded")
    if shot.prepare:
        shot.prepare(page)
    page.wait_for_load_state("networkidle", timeout=10_000)
    page.screenshot(path=str(target), full_page=shot.full_page)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture hotglue-manual screenshots in a target locale.")
    parser.add_argument("--locale", choices=["en", "es", "pt", "fr"], default="en")
    parser.add_argument("--shots", default="", help="Comma-separated shot name prefixes; empty means all.")
    args = parser.parse_args()
    locale = args.locale
    shot_filter = [s.strip() for s in args.shots.split(",") if s.strip()]

    shots = SHOTS
    if shot_filter:
        shots = [s for s in SHOTS if any(s.name.startswith(f) for f in shot_filter)]
        if not shots:
            sys.exit(f"no shots matched filter: {shot_filter}")
    print(f"shots: {[s.name for s in shots]}")

    base_url = env_required("TELARIS_EDITOR_URL").rstrip("/")
    email = env_required("TELARIS_EDITOR_USERNAME")
    password = env_required("TELARIS_EDITOR_PASSWORD")

    shots_dir = shots_dir_for(locale)
    shots_dir.mkdir(parents=True, exist_ok=True)
    print(f"locale: {locale}  ->  {shots_dir}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx_kwargs = dict(
            device_scale_factor=DEVICE_PIXEL_RATIO,
            locale=locale,
            extra_http_headers={"Accept-Language": ACCEPT_LANGUAGE_HEADERS[locale]},
        )
        context = browser.new_context(viewport=VIEWPORT, **ctx_kwargs)
        page = context.new_page()
        page.on("pageerror", lambda exc: print(f"  [page error] {exc}"))
        page.on("response", lambda r: print(f"  [response {r.status}] {r.request.method} {r.url}") if r.status >= 400 else None)

        print("logging in...")
        login(page, base_url, email, password)
        print(f"logged in as {email}")

        # Reuse the authenticated session cookie for a phone-sized context too.
        cookies = context.cookies()
        phone_context = browser.new_context(viewport=PHONE_VIEWPORT, **ctx_kwargs)
        phone_context.add_cookies(cookies)
        phone_page = phone_context.new_page()
        phone_page.on("pageerror", lambda exc: print(f"  [phone page error] {exc}"))

        for shot in shots:
            time.sleep(8)  # pace under Cloudflare's per-IP rate limiter
            tgt_page = phone_page if shot.phone else page
            out = capture_one(tgt_page, base_url, shot, shots_dir, locale)
            print(f"captured {out}")

        browser.close()

    print(f"\nall shots in {shots_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
