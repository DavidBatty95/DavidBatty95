#!/usr/bin/env python3
"""Check local profile links, SVGs and captured screenshot identities."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ('src', 'href') and value:
                self.targets.append(value)
            if name == 'id' or (tag == 'a' and name == 'name'):
                self.anchors.add(value)


def main():
    errors = []
    for path in [ROOT/'README.md', ROOT/'assets/README.md']:
        text = path.read_text()
        parser = Links()
        parser.feed(text)
        targets = parser.targets + re.findall(r'\]\(([^)]+)\)', text)
        for target in targets:
            if '://' in target or target.startswith('mailto:'):
                continue
            destination, _, fragment = target.partition('#')
            resolved = (path.parent/unquote(destination)).resolve() if destination else path
            if not resolved.exists():
                errors.append(f'{path.name}: missing {target}')
            elif fragment and resolved.suffix == '.md':
                headings = re.findall(r'^#+\s+(.+)$', resolved.read_text(), re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                anchors = Links()
                anchors.feed(resolved.read_text())
                slugs.update(anchors.anchors)
                if fragment not in slugs:
                    errors.append(f'{path.name}: missing anchor {target}')
    for path in (ROOT/'assets').glob('*.svg'):
        ET.parse(path)
    for capture in json.loads((ROOT/'assets/aardvark-capture.json').read_text()):
        path = ROOT/capture['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != capture['sha256']:
            errors.append(f'Screenshot hash mismatch: {capture["file"]}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Profile links, SVG XML and screenshot hashes passed')


if __name__ == '__main__':
    main()
