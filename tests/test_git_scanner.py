import os
import sys
import tempfile
import unittest
from pathlib import Path
from envguard.git_scanner import scan_git_history

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



class TestGitScanner(unittest.TestCase):
    def setUp(self):
        self.original_cwd = os.getcwd()

    def tearDown(self):
        os.chdir(self.original_cwd)

    def test_not_a_git_repo_returns_info_finding(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            findings = scan_git_history()

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "info")

    def test_valid_repo_returns_a_list(self):
        repo_root = Path(__file__).parent.parent
        os.chdir(repo_root)
        findings = scan_git_history()
        self.assertIsInstance(findings, list)
