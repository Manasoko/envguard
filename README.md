# envguard
A zero-dependency Python CLI for auditing .env files and scanning git history for accidentally committed secrets.

Python 3.11+ | Zero Dependencies | MIT License

## WHY ENVGUARD
- Deleting a secret from a file does not remove it from git history, so audits must inspect commits as well as the current workspace.
- .env drift causes silent runtime failures when local and deployed credentials diverge and the app still loads without warning.
- Secrets have recognizable shapes, and regex-based detection can catch many exposed keys before they are pushed.

## INSTALLATION
```bash
git clone https://github.com/yourusername/envguard
cd envguard
pip install -e .
```
envguard is now available as a terminal command.

## COMMANDS
| Command | What it does | Example | Output |
| --- | --- | --- | --- |
| `validate` | Checks a .env file for secret patterns and invalid assignments. | `envguard validate .env` | Lists matches and severity per line. |
| `scan` | Scans the working tree or a file for leaked secret patterns. | `envguard scan .env` | Shows suspect values and file locations. |
| `diff` | Compares two env files to highlight added or removed keys. | `envguard diff .env .env.example` | Shows key changes and missing entries. |
| `history` | Scans git history for secrets that were committed in the past. | `envguard history` | Reports commits containing suspect secret patterns. |
| `--format` / `--severity` | Controls CLI output format and the minimum severity to report. | `envguard scan --format json --severity warning` | Produces filtered output according to format and severity. |

## PATTERN LIBRARY
| Pattern Name | Regex | Severity |
| --- | --- | --- |
| AWS Access Key | `\bAKIA[0-9A-Z]{16}\b` | error |
| JWT Token | `\b[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\b` | warning |
| Database URL | `\b[a-zA-Z]+://[^:\s]+:[^@\s]+@[^/\s]+` | warning |
| Stripe Key | `\bsk_live_[A-Za-z0-9]{24}\b` | error |
| Generic Hex Token | `\b[a-f0-9]{32}\b` | warning |

The pattern library is biased toward recall because exposed secrets in source history and env files are a larger risk than occasional false positives. That makes it better for early detection, even if some flagged values need manual review.

## DELIBERATE OMISSIONS
| Feature | Reason skipped |
| --- | --- |
| Auto-fix suggestions | Fixes can introduce invalid env values or hide the need for manual credential rotation. |
| IDE plugins | The project is a CLI audit tool, and editor integration would add separate packaging and maintenance overhead. |
| GitHub Actions integration | CI automation is useful, but the core artifact here is the local scanner and pattern library, not workflow configuration. |
| ML/semantic analysis | The tool is designed for zero dependencies and reliable regex detection; ML would break that constraint and add unpredictability. |

## RUNNING THE TESTS
```bash
python -m unittest discover tests
```
The test suite covers scanner behavior, git history detection, diff comparisons, and validator rules.

## PROJECT STRUCTURE
```text
envguard/               # Python package containing CLI logic and pattern definitions
  __init__.py           # Package marker
  differ.py             # Diff logic for comparing .env files
  file_checker.py       # File existence and path validation helpers
  formatter.py          # Output formatting for CLI reports
  git_scanner.py        # Git history scanning implementation
  main.py               # CLI entry point for the envguard command
  patterns.py           # Core regex pattern library used by the scanner
  scanner.py            # Secret detection and file scanning logic
  validator.py          # .env validation rules and line analysis
fixtures/               # Sample .env files used by tests
  duplicate.env
  empty_keys.env
  secrets.env
  test.env
  test.env.example
  unquoted.env
  valid.env
tests/                  # Unit tests for envguard components
  __init__.py
  test_differ.py
  test_git_scanner.py
  test_scanner.py
  test_validator.py
README.md               # Project README with usage, patterns, and structure
pyproject.toml          # Package metadata, dependencies, and CLI entry point
```