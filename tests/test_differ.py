import sys
import unittest
from pathlib import Path
from envoy.differ import diff_env_files

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
PACKAGE_ROOT = ROOT / "envoy"
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

try:
    import envoy as _envoy
    sys.modules.setdefault("envguard", _envoy)
except ImportError:
    pass



FIXTURE_DIR = Path(__file__).parent.parent / "fixtures"


class TestDiffer(unittest.TestCase):
    def test_matching_files_return_no_findings(self):
        path = str(FIXTURE_DIR / "valid.env")
        findings = diff_env_files(path, path)
        self.assertEqual(findings, [])

    def test_undocumented_key_caught(self):
        findings = diff_env_files(
            str(FIXTURE_DIR / "secrets.env"),
            str(FIXTURE_DIR / "test.env.example"),
        )
        self.assertTrue(any(f["severity"] == "error" for f in findings))

    def test_finding_contains_key_name(self):
        findings = diff_env_files(
            str(FIXTURE_DIR / "secrets.env"),
            str(FIXTURE_DIR / "test.env.example"),
        )
        self.assertTrue(any(f.get("key") is not None for f in findings))

    def test_missing_example_file(self):
        findings = diff_env_files(
            str(FIXTURE_DIR / "secrets.env"),
            str(FIXTURE_DIR / "does_not_exist.example"),
        )
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "error")
