#!/usr/bin/env python3
"""Capture the public Scout website for the profile portfolio.

Requires playwright==1.58.0 and `python -m playwright install chromium`.
Only the unauthenticated homepage is visited; no forms or portal are accessed.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://aardvarkesuwebsite.onrender.com/'


def main():
    captures = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        for name, width, height, mobile in (('desktop', 1440, 1000, False), ('mobile', 390, 844, True)):
            context = browser.new_context(viewport={'width': width, 'height': height},
                device_scale_factor=1, is_mobile=mobile, has_touch=mobile, reduced_motion='reduce')
            page = context.new_page()
            response = page.goto(URL, wait_until='networkidle', timeout=120000)
            if response is None or not response.ok:
                raise RuntimeError(f'Homepage failed to load: {response.status if response else "no response"}')
            page.get_by_role('heading', level=1).wait_for()
            page.evaluate('document.fonts.ready')
            page.wait_for_function('''() => Array.from(document.images).filter(img => {
                const r = img.getBoundingClientRect();
                return r.bottom > 0 && r.top < innerHeight && r.width > 0;
            }).every(img => img.complete && img.naturalWidth > 0)''', timeout=60000)
            path = ROOT/'assets'/f'aardvark-{name}.png'
            page.screenshot(path=str(path), full_page=False, animations='disabled')
            captures.append({'file': str(path.relative_to(ROOT)), 'url': page.url,
                'title': page.title(), 'captured_at_utc': datetime.now(timezone.utc).isoformat(),
                'viewport': {'width': width, 'height': height}, 'device_scale_factor': 1,
                'mobile_emulation': mobile, 'reduced_motion': True, 'browser': browser.version,
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size})
            context.close()
        browser.close()
    (ROOT/'assets/aardvark-capture.json').write_text(json.dumps(captures, indent=2)+'\n')
    print(json.dumps(captures, indent=2))


if __name__ == '__main__':
    main()
