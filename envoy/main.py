from validator import validate_env_file
from scanner import scan_env_file
from differ import diff_env_files

results = []

results.append(validate_env_file("../fixtures/secrets.env"))
results.append(scan_env_file("../fixtures/secrets.env"))
results.append(diff_env_files("../fixtures/test.env", "../fixtures/test.env.example"))

for result in results:
    print(result)
