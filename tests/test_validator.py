import sys
import unittest
from pathlib import Path
from envguard.validator import validate_env_file

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
PACKAGE_ROOT = ROOT / "envguard"
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

try:
    import envguard as _envguard

    sys.modules.setdefault("envguard", _envguard)
except ImportError:
    pass
FIXTURE_DIR = Path(__file__).parent.parent / "fixtures"


class TestValidator(unittest.TestCase):
    def test_valid_file_returns_no_findings(self):
        findings = validate_env_file(str(FIXTURE_DIR / "valid.env"))
        self.assertEqual(findings, [])

    def test_duplicate_keys_caught(self):
        findings = validate_env_file(str(FIXTURE_DIR / "duplicate.env"))
        error_findings = [f for f in findings if f["severity"] == "error"]
        self.assertEqual(len(error_findings), 2)
        self.assertTrue(all(f["severity"] == "error" for f in error_findings))

    def test_unquoted_spaces_caught(self):
        findings = validate_env_file(str(FIXTURE_DIR / "unquoted.env"))
        warning_findings = [f for f in findings if f["severity"] == "warning"]
        self.assertEqual(len(warning_findings), 3)
        self.assertTrue(all(f["severity"] == "warning" for f in warning_findings))

    def test_empty_values_caught(self):
        findings = validate_env_file(str(FIXTURE_DIR / "empty_keys.env"))
        warning_findings = [f for f in findings if f["severity"] == "warning"]
        self.assertEqual(len(warning_findings), 2)
        self.assertTrue(all(f["severity"] == "warning" for f in warning_findings))

    def test_file_not_found(self):
        missing_path = FIXTURE_DIR / "does_not_exist.env"
        findings = validate_env_file(str(missing_path))
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "error")
        self.assertEqual(findings[0]["line"], 0)
