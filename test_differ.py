from envoy.differ import diff_env_files

findings = diff_env_files("fixtures/test.env", "fixtures/test.env.example")
for finding in findings:
    print(finding)
