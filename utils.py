import os
import json

def parse_requirements(path):
    deps = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                deps.append(line.split("==")[0])
    return deps

def parse_package_json(path):
    deps = []
    with open(path) as f:
        data = json.load(f)

    for section in ["dependencies", "devDependencies"]:
        if section in data:
            deps.extend(data[section].keys())

    return deps

def find_files(root):
    reqs, pkgs = [], []

    for r, _, files in os.walk(root):
        for f in files:
            if f == "requirements.txt":
                reqs.append(os.path.join(r, f))
            if f == "package.json":
                pkgs.append(os.path.join(r, f))

    return reqs, pkgs
