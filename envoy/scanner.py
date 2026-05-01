from pathlib import Path
from patterns import PATTERNS
import re


def scanner(filepath: str) -> list[dict]:
    findings = []
    path = Path(filepath)

    if not path.exists():
        return [
            {"line": 0, "severity": "error", "message": f"File not found: {filepath}"}
        ]

    with open(path, "r") as file:
        lines = file.readlines()

    for index, line in enumerate(lines, start=1):
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue

        key, _, value = stripped.partition("=")
        key = key.strip()
        value = value.strip()

        for pattern in PATTERNS:
            match = re.search(pattern["pattern"], value)
            if match:
                findings.append(
                    {
                        "line": index,
                        "severity": pattern["severity"],
                        "source": "scanner",
                        "key": key,
                        "message": f"{pattern['name']} detected",
                    }
                )

    return findings
