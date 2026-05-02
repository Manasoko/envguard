from pathlib import Path


def resolve_file_path(filepath: str) -> tuple[Path | None, list[dict]]:
    """Return a Path for an existing file or a standardized error finding."""
    path = Path(filepath)
    if not path.exists():
        return None, [
            {
                "line": 0,
                "severity": "error",
                "message": f"File not found: {filepath}",
            }
        ]
    return path, []
