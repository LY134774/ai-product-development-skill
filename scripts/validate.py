"""Validate this documentation-only skill without installing dependencies.

The YAML reader intentionally accepts only the block-mapping/scalar subset used
in this repository. It rejects all unsupported syntax instead of claiming to be
a general YAML parser. No network requests or external mutations are performed.
"""
import json
import re
import sys
from pathlib import Path


def mapping_subset(text):
    root = {}
    stack = [(-2, root)]
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if '\t' in line:
            raise ValueError('Tabs are unsupported')
        m = re.fullmatch(r'( *)([a-z_][a-z0-9_-]*):(?: (.+))?', line)
        if not m:
            raise ValueError(f'Unsupported YAML syntax: {line}')
        indent, key, value = len(m[1]), m[2], m[3]
        while stack[-1][0] >= indent:
            stack.pop()
        parent_indent, parent = stack[-1]
        if indent != parent_indent + 2 or key in parent:
            raise ValueError(f'Bad indentation or duplicate key: {key}')
        if value is None:
            parent[key] = {}
            stack.append((indent, parent[key]))
        elif value.startswith('"'):
            parent[key] = json.loads(value)
        elif value in ('true', 'false'):
            parent[key] = value == 'true'
        elif re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9-]*', value):
            parent[key] = value
        else:
            raise ValueError(f'Unsupported scalar: {key}')
    return root


def validate(root):
    skill = root / 'skills' / 'product-development-coach'
    entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
    fm = re.match(r'\A---\n(.*?)\n---\n', entry, re.S)
    assert fm, 'Missing frontmatter'
    meta = mapping_subset(fm[1])
    assert set(meta) <= {'name', 'description', 'license', 'metadata'}
    assert meta['name'] == skill.name
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', meta['name'])
    assert len(meta['name']) <= 64
    assert isinstance(meta['description'], str) and 1 <= len(meta['description']) <= 1024
    assert meta['license'] == 'MIT'
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in meta['metadata'].items())
    assert meta['metadata']['version'] == '1.0.0'
    ui = mapping_subset((skill / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))
    assert '$product-development-coach' in ui['interface']['default_prompt']
    assert 25 <= len(ui['interface']['short_description']) <= 64
    assert ui['policy']['allow_implicit_invocation'] is True
    assert (root / 'LICENSE').read_bytes() == (skill / 'LICENSE').read_bytes()
    expected = {'AGENTS.md', 'README.md', 'TODO.md', 'DECISIONS.md', 'HANDOFF.md',
                'SEO_GEO.md', 'SEO_GEO_LEDGER.md', 'RELEASE_CHECKLIST.md',
                'OPERATIONS.md', 'ANALYTICS.md'}
    assert {p.name for p in (skill / 'templates').glob('*.md')} == expected
    linked = set()
    files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts]
    for path in files:
        assert path.suffix in ('.md', '.yaml', '.py') or path.name == 'LICENSE', path
        text = path.read_text(encoding='utf-8')
        assert not text.startswith('\ufeff'), f'Unexpected BOM: {path}'
        if path.suffix == '.md':
            assert len(re.findall(r'^```', text, re.M)) % 2 == 0, f'Unclosed code fence: {path}'
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                target_path = (path.parent / target.split('#')[0]).resolve()
                assert target_path.is_relative_to(root.resolve()), f'Escaping link: {path}'
                assert target_path.exists(), f'Broken link: {path}: {target}'
                linked.add(target_path)
        if path.name != 'validate.py':
            for pattern in (r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}',
                            r'sk_(?:live|test)_[A-Za-z0-9]{16,}',
                            r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                            r'AKIA[0-9A-Z]{16}', r'C:\\Users\\Administrator'):
                assert not re.search(pattern, text), f'Secret or machine-path candidate: {path}'
    for ref in (skill / 'references').glob('*.md'):
        assert ref.resolve() in linked, f'Undiscoverable reference: {ref}'
    print(f'PASS: {len(files)} files; YAML subset/schema, names, metadata, templates,')
    print('      local links, reference discovery, UTF-8, fences and secret-pattern scan.')
    print('LIMITS: no external URL status, host auto-trigger, production or exhaustive secret audit.')


if __name__ == '__main__':
    try:
        validate(Path(__file__).resolve().parents[1])
    except (AssertionError, ValueError, KeyError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
