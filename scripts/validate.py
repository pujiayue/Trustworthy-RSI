#!/usr/bin/env python3
"""Check catalog consistency, generated outputs, assets, and local Markdown links."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition: errors.append(message)

papers = json.loads((ROOT / 'data/papers.json').read_text())
taxonomy = json.loads((ROOT / 'data/taxonomy.json').read_text())
ids = [p['ID'] for p in papers]
require(len(ids) == len(set(ids)), 'Duplicate paper IDs')
require(len({k.lower() for k in ids}) == len(ids), 'Case-insensitive citation anchor collision')
require(len(taxonomy) == 8, 'The survey taxonomy must contain eight chapters')
require(not {'smith2024example', 'doe2023benchmark'} & set(ids), 'Template references included')
for p in papers:
    for field in ('ID', 'ENTRYTYPE', 'title', 'author', 'year'):
        require(bool(p.get(field)), f'{p.get("ID")}: missing {field}')
    require(str(p['year']).isdigit(), f'{p["ID"]}: invalid year')
    if p.get('url'):
        url = urlsplit(p['url'])
        require(url.scheme in ('http', 'https') and bool(url.netloc), f'{p["ID"]}: invalid source URL')

# Check every field against the braced BibTeX values emitted in this repository.
bib = (ROOT / 'bibliography/references.bib').read_text()
parsed = {}
for match in re.finditer(r'@(\w+)\s*\{([^,]+),', bib):
    pos = match.end(); depth = 1; end = pos
    while end < len(bib) and depth:
        if bib[end] == '{' and bib[end-1] != '\\': depth += 1
        if bib[end] == '}' and bib[end-1] != '\\': depth -= 1
        end += 1
    require(depth == 0, f'Unbalanced BibTeX entry: {match[2]}')
    block = bib[pos:end-1]; fields = {'ENTRYTYPE': match[1], 'ID': match[2]}
    cursor = 0
    while True:
        field = re.search(r'(\w+)\s*=\s*\{', block[cursor:])
        if not field: break
        begin = cursor+field.end(); i = begin; d = 1
        while i < len(block) and d:
            if block[i] == '{' and block[i-1] != '\\': d += 1
            if block[i] == '}' and block[i-1] != '\\': d -= 1
            i += 1
        require(d == 0, f'Unbalanced BibTeX field: {match[2]}.{field[1]}')
        fields[field[1]] = block[begin:i-1]; cursor = i
    require(match[2] not in parsed, f'Duplicate BibTeX key: {match[2]}')
    parsed[match[2]] = fields
require(set(parsed) == set(ids), 'BibTeX and JSON citation keys differ')
normalize = lambda s: ' '.join(s.split())
for p in papers:
    for field,value in p.items():
        require(field in parsed.get(p['ID'], {}) and normalize(parsed[p['ID']][field]) == normalize(value), f'BibTeX differs from JSON: {p["ID"]}.{field}')

anchors = set(); placements = 0
for section in taxonomy:
    for node in [section] + section['subsections']:
        require(node['id'] not in anchors, f'Duplicate section ID: {node["id"]}')
        anchors.add(node['id']); seen = set()
        for p in node['papers']:
            require(p['id'] in ids, f'Unresolved taxonomy reference: {p["id"]}')
            require(p['id'] not in seen, f'Duplicate within subsection: {p["id"]}')
            require(bool(p['label']), 'Empty paper label')
            seen.add(p['id']); placements += 1

# Check relative file links and fragment targets, including explicit HTML anchors.
mds = list(ROOT.rglob('*.md'))
def document_anchors(path):
    content = path.read_text(); found = set(re.findall(r'<a id="([^"]+)"', content))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', content, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0); counts[slug] = count+1
        found.add(slug + (f'-{count}' if count else ''))
    return found
for path in mds:
    content = path.read_text()
    require(not re.search(r'/Users/|your-name|your-project|example\.com|First Author', content), f'Private path or placeholder in {path.relative_to(ROOT)}')
    for link in re.findall(r'\]\(([^\s)]+)\)', content):
        parts = urlsplit(link)
        if parts.scheme or parts.netloc: continue
        file = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        require(file == ROOT or ROOT in file.parents, f'Link escapes repository: {link}')
        require(file.exists(), f'Missing local target: {path.relative_to(ROOT)} -> {link}')
        if file.exists() and parts.fragment and file.suffix == '.md':
            require(unquote(parts.fragment) in document_anchors(file), f'Missing anchor: {path.relative_to(ROOT)} -> {link}')
for file, signature in [('assets/overview.png', b'\x89PNG\r\n\x1a\n'), ('assets/overview.pdf', b'%PDF-')]:
    path = ROOT/file
    require(path.exists() and path.read_bytes().startswith(signature), f'Invalid or missing figure: {file}')
result = subprocess.run([sys.executable, str(ROOT/'scripts/build_readme.py'), '--check'], capture_output=True, text=True)
require(result.returncode == 0, result.stdout + result.stderr)
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'PASS: {len(papers)} references, {placements} taxonomy placements, BibTeX parity, generated files, figures, and local links.')
