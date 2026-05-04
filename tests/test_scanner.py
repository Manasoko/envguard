import sys
import unittest
from pathlib import Path
from envoy.patterns import PATTERNS
from envoy.scanner import scan_env_file

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
PACKAGE_ROOT = ROOT / "envoy"
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

try:
    import envoy as _envoy
    sys.modules.setdefault("envoy", _envoy)
except ImportError:
    pass



FIXTURE_DIR = Path(__file__).parent.parent / "fixtures"


class TestScanner(unittest.TestCase):
    def test_clean_file_returns_no_findings(self):
        findings = scan_env_file(str(FIXTURE_DIR / "test.env.example"))
        self.assertEqual(findings, [])

    def test_aws_key_detected(self):
        findings = scan_env_file(str(FIXTURE_DIR / "secrets.env"))
        self.assertTrue(any("AWS" in f["message"] for f in findings))

    def test_jwt_detected(self):
        findings = scan_env_file(str(FIXTURE_DIR / "secrets.env"))
        self.assertTrue(any("JWT" in f["message"] for f in findings))

    def test_database_url_detected(self):
        findings = scan_env_file(str(FIXTURE_DIR / "secrets.env"))
        self.assertTrue(
            any(
                "database" in f["message"].lower() or "postgres" in f["message"].lower()
                for f in findings
            )
        )

    def test_all_patterns_have_required_keys(self):
        for pattern in PATTERNS:
            self.assertIn("name", pattern)
            self.assertIn("pattern", pattern)
            self.assertIn("severity", pattern)
