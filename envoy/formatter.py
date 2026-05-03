import json

SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}

SEVERITY_LABELS = {
    "error": "ERROR",
    "warning": "WARNING",
    "info": "INFO",
}


def format_text(findings: list[dict], min_severity: str = "info") -> None:
    """Print findings to stdout sorted by severity with a summary line."""
    filtered_findings = [
        f
        for f in findings
        if SEVERITY_ORDER.get(f["severity"], 3) <= SEVERITY_ORDER[min_severity]
    ]

    if not filtered_findings:
        print("No issues found")
        return

    sorted_findings = sorted(
        filtered_findings, key=lambda f: SEVERITY_ORDER.get(f["severity"], 3)
    )

    for f in sorted_findings:
        label = SEVERITY_LABELS.get(f["severity"], f["severity"])
        key = f["key"] if f["key"] is not None else "none"
        print(f"{label} | Line {f['line']} | source: {f['source']} | key: {key} | {f['message']}")

    errors = sum(1 for f in filtered_findings if f["severity"] == "error")
    warnings = sum(1 for f in filtered_findings if f["severity"] == "warning")
    info = sum(1 for f in filtered_findings if f["severity"] == "info")
    print(f"\nSummary: {errors} errors, {warnings} warnings, {info} info")


def format_json(findings: list[dict], min_severity: str = "info") -> None:
    """Serialize findings to JSON and print to stdout."""
    filtered_findings = [
        f
        for f in findings
        if SEVERITY_ORDER.get(f["severity"], 3) <= SEVERITY_ORDER[min_severity]
    ]
    print(json.dumps(filtered_findings, indent=2))
