import argparse

from .differ import diff_env_files
from .formatter import format_json, format_text
from .git_scanner import scan_git_history
from .scanner import scan_env_file
from .validator import validate_env_file

findings: list[dict] = []

parser = argparse.ArgumentParser(
    prog="envguard",
    description=(
        "envguard — a CLI tool for auditing .env files and scanning git history\n"
        "for accidentally committed secrets. Validates syntax, detects secret\n"
        "patterns, diffs against .env.example, and scans your full commit history\n"
        "for leaks. Zero external dependencies."
    ),
    epilog=(
        "examples:\n"
        "  envguard validate .env                   check .env for syntax errors\n"
        "  envguard scan .env                       scan .env for secret patterns\n"
        "  envguard diff .env .env.example          find undocumented keys\n"
        "  envguard history                         scan full git history\n"
        "  envguard validate .env --format json     output results as JSON\n"
        "  envguard scan .env --severity error      show only errors\n"
        "\n"
        "secret patterns detected:\n"
        "  AWS Access Keys, JWT Tokens, Database URLs,\n"
        "  Stripe Keys, Generic API Tokens, Hex Secrets\n"
        "\n"
        "severity levels:\n"
        "  error    — immediate risk, act now\n"
        "  warning  — potential issue, review recommended\n"
        "  info     — informational, use your judgement\n"
        "\n"
        "source code: https://github.com/yourusername/envguard"
    ),
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
subparsers = parser.add_subparsers(dest="command", help="Available commands")

validate_parser = subparsers.add_parser("validate", help="To validate your .env file")
validate_parser.add_argument("filepath", help="File to validate")

scan_parser = subparsers.add_parser("scan", help="To scan your .env file")
scan_parser.add_argument("filepath", help="File to scan")

diff_parser = subparsers.add_parser(
    "diff", help="To check if the .env and .env.example corelate"
)
diff_parser.add_argument("env_filepath", help="Your .env file")
diff_parser.add_argument("example_filepath", help="Your .env.example file")

subparsers.add_parser("history", help="Scan git history for leaked secrets")

parser.add_argument(
    "--format",
    choices=["text", "json"],
    default="text",
    help="Output format: 'text' or 'json' (default: text)",
)
parser.add_argument(
    "--severity",
    type=str,
    choices=["info", "warning", "error"],
    default="info",
    help="Filter logs by minimum severity: 'info', 'warning', or 'error' (default: info)",
)

def main():
    findings: list[dict] = []
    args = parser.parse_args()

    if args.command == "validate":
        findings.extend(validate_env_file(args.filepath))
    elif args.command == "scan":
        findings.extend(scan_env_file(args.filepath))
    elif args.command == "diff":
        findings.extend(diff_env_files(args.env_filepath, args.example_filepath))
    elif args.command == "history":
        findings.extend(scan_git_history())
    else:
        parser.print_help()
        exit(0)

    if args.format == "json":
        format_json(findings, min_severity=args.severity)
    else:
        format_text(findings, min_severity=args.severity)


if __name__ == "__main__":
    main()

