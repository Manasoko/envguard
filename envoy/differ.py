from file_checker import resolve_file_path


def diff_env_files(main_env: str, other_env: str) -> list[dict]:
    findings = []

    env1, resolve_errors = resolve_file_path(main_env)
    if env1 is None:
        return resolve_errors

    env2, resolve_errors = resolve_file_path(other_env)
    if env2 is None:
        return resolve_errors

    with open(env1, "r") as file:
        main_env_lines = file.readlines()

    with open(env2, "r") as file:
        other_env_lines = file.readlines()

    env_keys = set()

    for index, line in enumerate(other_env_lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue

        env_keys.add(stripped.split("=", 1)[0].strip())

    for index, line in enumerate(main_env_lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue

        env_key = stripped.split("=", 1)[0].strip()
        if env_key not in env_keys:
            findings.append(
                {
                    "line": 0,
                    "severity": "error",
                    "source": "differ",
                    "key": env_key,
                    "message": f"{env_key} exists in .env but is undocumented in .env.example",
                }
            )
    return findings
