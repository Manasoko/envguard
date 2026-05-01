from validator import validate_env_file
from scanner import scanner

reuslts = []

reuslts.append(validate_env_file("../fixtures/secrets.env"))
reuslts.append(scanner("../fixtures/secrets.env"))

print(reuslts)
