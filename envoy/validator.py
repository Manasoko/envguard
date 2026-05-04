from .file_checker import resolve_file_path

source = "validation"


def validate_env_file(filepath: str) -> list[dict]:
    findings = []
    seen_keys = set()
    path, resolve_errors = resolve_file_path(filepath)
    if path is None:
        return resolve_errors

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
                    "source": source,
                    "key": "unknown",
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
                    "source": source,
                    "key": key,
                    "message": f"Duplicate key: '{key}'",
                }
            )
        else:
            seen_keys.add(key)

        if (
            " " in value
            and not (value.startswith('"') and value.endswith('"'))
            and not (value.startswith("'") and value.endswith("'"))
        ):
            findings.append(
                {
                    "line": index,
                    "severity": "warning",
                    "source": source,
                    "key": key,
                    "message": f"Unquoted value with spaces for key '{key}': '{value}'",
                }
            )

        if value == "":
            findings.append(
                {
                    "line": index,
                    "severity": "warning",
                    "message": f"Empty value for key '{key}'",
                }
            )
    return findings
