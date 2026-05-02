from validator import validate_env_file
from scanner import scan_env_file
from differ import diff_env_files
from git_scanner import scan_git_history
from formatter import format_text

findings: list[dict] = []

findings.extend(validate_env_file("../fixtures/secrets.env"))
findings.extend(scan_env_file("../fixtures/secrets.env"))
findings.extend(diff_env_files("../fixtures/test.env", "../fixtures/test.env.example"))
findings.extend(scan_git_history())

format_text(findings)
