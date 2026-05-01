from pathlib import Path


def validate_env_file(filepath: str) -> list[dict]:
    findings = []
    seen_keys = set()
    path = Path(filepath)


    if not path.exists():
        print(f"Validating .env file at: {filepath}")
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
            findings.append(
                {
                    "line": index,
                    "severity": "error",
                    "message": f"Malformed line (no '=' found): '{stripped}'",
                }
            )
            continue

        key, _, value = stripped.partition("=")
        key = key.strip()
        value = value.strip()

        if key in seen_keys:
            findings.append(
                {
                    "line": index,
                    "severity": "error",
                    "message": f"Duplicate key: '{key}'",
                }
            )
        else:
            seen_keys.add(key)
        
        if " " in value and not (value.startswith('"') and value.endswith('"')) \
                         and not (value.startswith("'") and value.endswith("'")):
            findings.append({
                "line": index,
                "severity": "warning",
                "message": f"Unquoted value with spaces for key '{key}': '{value}'"
            })
        
        if value == "":
            findings.append({
                "line": index,
                "severity": "warning",
                "message": f"Empty value for key '{key}'"
            })
    return findings
