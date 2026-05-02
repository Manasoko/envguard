import subprocess
import re
from patterns import PATTERNS


def scan_git_history() -> list[dict]:
    """Scan git history for secrets leaked in added lines."""
    findings: list[dict] = []

    process = subprocess.Popen(
        ["git", "log", "-p"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdout is not None

    current_commit: str = ""
    current_file: str = ""

    for raw_line in process.stdout:
        try:
            line = raw_line.decode("utf-8", errors="strict").rstrip("\n")
        except (UnicodeDecodeError, ValueError):
            continue

        if line.startswith("commit "):
            current_commit = line.split(" ", 1)[1].strip()
            continue

        if line.startswith("diff --git"):
            # "diff --git a/path/to/file b/path/to/file" → extract the b/ side
            parts = line.split(" b/", 1)
            if len(parts) == 2:
                current_file = parts[1]
            continue

        # Skip file headers
        if line.startswith("+++"):
            continue

        # Only process added lines (single leading "+")
        if not line.startswith("+"):
            continue

        scannable = line[1:]  # strip the leading "+"

        for pattern in PATTERNS:
            if re.search(pattern["pattern"], scannable):
                findings.append(
                    {
                        "line": 0,
                        "severity": pattern["severity"],
                        "source": "git_scanner",
                        "key": None,
                        "message": f"{pattern['name']} found in commit {current_commit} in file {current_file}",
                    }
                )

    process.stdout.close()
    return_code = process.wait()

    if return_code != 0:
        return [
            {
                "line": 0,
                "severity": "info",
                "source": "git_scanner",
                "key": None,
                "message": "Not a git repository or git is not installed",
            }
        ]

    return findings
