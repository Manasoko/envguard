import json

SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}

SEVERITY_LABELS = {
    "error": "ERROR",
    "warning": "WARNING",
    "info": "INFO",
}


def format_text(findings: list[dict]) -> None:
    """Print findings to stdout sorted by severity with a summary line."""
    if not findings:
        print("No issues found")
        return

    sorted_findings = sorted(
        findings, key=lambda f: SEVERITY_ORDER.get(f["severity"], 3)
    )

    for f in sorted_findings:
        label = SEVERITY_LABELS.get(f["severity"], f["severity"])
        key = f["key"] if f["key"] is not None else "none"
        print(f"{label} | Line {f['line']} | source: {f['source']} | key: {key} | {f['message']}")

    errors = sum(1 for f in findings if f["severity"] == "error")
    warnings = sum(1 for f in findings if f["severity"] == "warning")
    info = sum(1 for f in findings if f["severity"] == "info")
    print(f"\nSummary: {errors} errors, {warnings} warnings, {info} info")


def format_json(findings: list[dict]) -> None:
    """Serialize findings to JSON and print to stdout."""
    print(json.dumps(findings, indent=2))
