import requests
import tarfile
import tempfile
import os

PATTERNS = [
    "os.system",
    "subprocess",
    "eval(",
    "exec(",
    "requests.get(",
]

def download_package(pkg):
    try:
        data = requests.get(f"https://pypi.org/pypi/{pkg}/json").json()
        for rel in data.get("releases", {}).values():
            for file in rel:
                if file["filename"].endswith(".tar.gz"):
                    return file["url"]
    except:
        return None

def analyze_code(pkg):
    url = download_package(pkg)
    if not url:
        return []

    findings = []

    try:
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(requests.get(url).content)
        tmp.close()

        extract_dir = tempfile.mkdtemp()

        with tarfile.open(tmp.name) as tar:
            tar.extractall(path=extract_dir)

        for root, _, files in os.walk(extract_dir):
            for f in files:
                if f.endswith(".py"):
                    try:
                        with open(os.path.join(root, f), errors="ignore") as file:
                            content = file.read()
                            for p in PATTERNS:
                                if p in content:
                                    findings.append(p)
                    except:
                        pass

    except:
        return []

    return list(set(findings))
