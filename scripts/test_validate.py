"""Regression tests for validation failures. Uses only disposable repository copies."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'validate.py'
SKILL = Path('skills/product-development-coach')


class ValidatorRegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skill-validator-test-')
        self.addCleanup(self.temp.cleanup)
        self.copy = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.copy, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def run_check(self, *, optimized=False):
        command = [sys.executable, '-B']
        if optimized:
            command.append('-O')
        command.extend([str(SCRIPT), str(self.copy)])
        return subprocess.run(command, capture_output=True, text=True, encoding='utf-8',
                              env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}, timeout=20)

    def expect_failure(self, clue, *, optimized=False):
        result = self.run_check(optimized=optimized)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(clue, result.stderr)
        self.assertNotIn('PASS:', result.stdout)

    def test_valid_repository_passes_in_both_modes(self):
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                result = self.run_check(optimized=optimized)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn('LIMITS:', result.stdout)

    def test_broken_link_is_rejected_in_both_modes(self):
        path = self.copy / 'README.md'
        path.write_text(path.read_text(encoding='utf-8') + '\n[Broken](missing-file.md)\n',
                        encoding='utf-8')
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                self.expect_failure('Broken link', optimized=optimized)

    def test_link_cannot_escape_repository(self):
        path = self.copy / 'README.md'
        path.write_text('[Escape](../outside.md)\n', encoding='utf-8')
        self.expect_failure('Escaping link')

    def test_wrong_skill_name_is_rejected(self):
        path = self.copy / SKILL / 'SKILL.md'
        path.write_text(path.read_text(encoding='utf-8').replace(
            'name: product-development-coach', 'name: another-skill', 1), encoding='utf-8')
        self.expect_failure('Skill name must match')

    def test_duplicate_yaml_key_is_rejected(self):
        path = self.copy / SKILL / 'agents/openai.yaml'
        path.write_text(path.read_text(encoding='utf-8') + 'policy:\n', encoding='utf-8')
        self.expect_failure('duplicate key')

    def test_missing_template_is_rejected(self):
        (self.copy / SKILL / 'templates/HANDOFF.md').unlink()
        self.expect_failure('Expected project templates')

    def test_mismatched_license_is_rejected(self):
        (self.copy / SKILL / 'LICENSE').write_text('Not the same license\n', encoding='utf-8')
        self.expect_failure('License copies differ')

    def test_invalid_utf8_is_rejected(self):
        (self.copy / 'README.md').write_bytes(b'\xff\xfe')
        self.expect_failure('FAIL:')

    def test_orphan_reference_is_rejected(self):
        (self.copy / SKILL / 'references/orphan.md').write_text('# Orphan\n', encoding='utf-8')
        self.expect_failure('Undiscoverable reference')

    def test_secret_candidate_is_rejected_without_echoing_value(self):
        candidate = 'gh' + 'p_' + 'x' * 25
        (self.copy / 'README.md').write_text(candidate, encoding='utf-8')
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Secret or machine-path candidate', result.stderr)
        self.assertNotIn(candidate, result.stdout + result.stderr)

    def test_invalid_yaml_does_not_echo_its_value(self):
        candidate = 'gh' + 'p_' + 'x' * 25
        path = self.copy / SKILL / 'agents/openai.yaml'
        path.write_text('- ' + candidate + '\n', encoding='utf-8')
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unsupported YAML syntax at line', result.stderr)
        self.assertNotIn(candidate, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
