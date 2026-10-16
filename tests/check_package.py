"""Offline package integrity checks. No external access or writes."""
import ast
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skill = root / 'skill' / 'manage-meeting-secretary'
files = [p for p in root.rglob('*') if p.is_file()]
assert (skill / 'SKILL.md').exists()
text = (skill / 'SKILL.md').read_text()
assert text.startswith('---\nname: manage-meeting-secretary\ndescription: ')
assert len(text.split('---', 2)) == 3
for p in files:
    assert not p.is_symlink(), f'Symlink: {p.relative_to(root)}'
    assert not any(x in {'.git', '__pycache__', '.env'} for x in p.parts), p
    if p.suffix == '.json': json.loads(p.read_text())
    if p.suffix == '.py': ast.parse(p.read_text())
    if p.suffix == '.md':
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
            if '://' not in target and not target.startswith('#'):
                assert (p.parent / target.split('#')[0]).exists(), (p, target)
assert json.loads((skill / 'templates/template-registry.json').read_text())['records'] == []
adapters = json.loads((skill / 'templates/adapters.example.json').read_text())
assert all(v['provider'] is None and v['status'] == 'unconfigured' for v in adapters['adapters'].values())
license_text = (root / 'LICENSE').read_text()
assert license_text.startswith('MIT License\n\nCopyright (c) 2026 Mohammad Khezri\n')
assert 'The above copyright notice and this permission notice shall be included in all' in license_text
assert 'THE SOFTWARE IS PROVIDED \"AS IS\"' in license_text
print('PASS: frontmatter, JSON, Python syntax, local links, clean packaging, empty registry, unconfigured adapters, approved MIT license')
