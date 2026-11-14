"""Validate this documentation-only skill without installing dependencies.

The YAML reader intentionally accepts only the block-mapping/scalar subset used
in this repository. It rejects all unsupported syntax instead of claiming to be
a general YAML parser. No network requests or external mutations are performed.
"""
import argparse
import json
import re
import sys
from pathlib import Path


def mapping_subset(text):
    root = {}
    stack = [(-2, root)]
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if '\t' in line:
            raise ValueError('Tabs are unsupported')
        m = re.fullmatch(r'( *)([a-z_][a-z0-9_-]*):(?: (.+))?', line)
        if not m:
            raise ValueError(f'Unsupported YAML syntax at line {line_number}')
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


class ValidationError(ValueError):
    """An explicit validation failure that remains active under python -O."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def validate(root):
    root = Path(root).resolve()
    skill = root / 'skills' / 'product-development-coach'
    entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
    fm = re.match(r'\A---\n(.*?)\n---\n', entry, re.S)
    require(fm is not None, 'Missing frontmatter')
    meta = mapping_subset(fm[1])
    require(set(meta) <= {'name', 'description', 'license', 'metadata'}, 'Unexpected frontmatter keys')
    require(meta.get('name') == skill.name, 'Skill name must match directory')
    require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', meta['name']) is not None
            and len(meta['name']) <= 64, 'Invalid skill name')
    description = meta.get('description')
    require(isinstance(description, str) and 1 <= len(description) <= 1024, 'Invalid description')
    require(meta.get('license') == 'MIT', 'Expected MIT license')
    metadata = meta.get('metadata')
    require(isinstance(metadata, dict)
            and all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()),
            'Metadata must map strings to strings')
    require(re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?', metadata.get('version', ''))
            is not None, 'Invalid version')
    ui = mapping_subset((skill / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))
    interface = ui.get('interface', {})
    require(isinstance(interface, dict), 'Invalid UI interface')
    prompt = interface.get('default_prompt', '')
    require(isinstance(prompt, str) and '$product-development-coach' in prompt,
            'Default prompt must explicitly name this skill')
    summary = interface.get('short_description', '')
    require(isinstance(summary, str) and 25 <= len(summary) <= 64, 'Invalid UI summary')
    require(ui.get('policy', {}).get('allow_implicit_invocation') is True,
            'Automatic discovery policy changed')
    require((root / 'LICENSE').read_bytes() == (skill / 'LICENSE').read_bytes(),
            'License copies differ')
    expected = {'AGENTS.md', 'README.md', 'TODO.md', 'DECISIONS.md', 'HANDOFF.md',
                'SEO_GEO.md', 'SEO_GEO_LEDGER.md', 'RELEASE_CHECKLIST.md',
                'OPERATIONS.md', 'ANALYTICS.md'}
    require({p.name for p in (skill / 'templates').glob('*.md')} == expected,
            'Expected project templates missing or unexpected templates added')
    linked = set()
    files = [p for p in root.rglob('*') if p.is_file()
             and not {'.git', '__pycache__'}.intersection(p.relative_to(root).parts)]
    for path in files:
        require(path.suffix in ('.md', '.yaml', '.py') or path.name == 'LICENSE'
                or path.relative_to(root).as_posix() == 'evals/cases.json',
                f'Unexpected file type: {path.relative_to(root)}')
        text = path.read_text(encoding='utf-8')
        require(not text.startswith('\ufeff'), f'Unexpected BOM: {path.relative_to(root)}')
        if path.suffix == '.md':
            require(len(re.findall(r'^```', text, re.M)) % 2 == 0,
                    f'Unclosed code fence: {path.relative_to(root)}')
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                target_path = (path.parent / target.split('#')[0]).resolve()
                require(target_path.is_relative_to(root), f'Escaping link: {path.relative_to(root)}')
                require(target_path.exists(), f'Broken link: {path.relative_to(root)}: {target}')
                linked.add(target_path)
        if path.name != 'validate.py':
            for pattern in (r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}',
                            r'sk_(?:live|test)_[A-Za-z0-9]{16,}',
                            r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                            r'AKIA[0-9A-Z]{16}', r'C:\\Users\\Administrator'):
                require(not re.search(pattern, text),
                        f'Secret or machine-path candidate: {path.relative_to(root)}')
    for ref in (skill / 'references').glob('*.md'):
        require(ref.resolve() in linked, f'Undiscoverable reference: {ref.relative_to(root)}')
    print(f'PASS: {len(files)} files; YAML subset/schema, names, metadata, templates,')
    print('      local links, reference discovery, UTF-8, fences and secret-pattern scan.')
    print('LIMITS: no external URL status, host auto-trigger, production or exhaustive secret audit.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1],
                        help='Repository root; defaults to the parent of scripts/')
    args = parser.parse_args()
    try:
        validate(args.root)
    except (ValueError, KeyError, AttributeError, TypeError, UnicodeError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
