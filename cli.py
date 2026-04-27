import typer
from core.scanner import analyze_package
from core.repo import clone_repo
from utils import find_files, parse_requirements, parse_package_json

app = typer.Typer()

@app.command()
def scan_repo(path: str):
    results = []

    reqs, pkgs = find_files(path)

    for r in reqs:
        for dep in parse_requirements(r):
            results.append(analyze_package(dep, "pypi"))

    for p in pkgs:
        for dep in parse_package_json(p):
            results.append(analyze_package(dep, "npm"))

    for r in results:
        print(f"\n📦 {r['package']} ({r['ecosystem']})")
        print(f"Risk: {r['risk']['level']} ({r['risk']['score']})")
        for reason in r["risk"]["reasons"]:
            print(" -", reason)

@app.command()
def scan_pkg(pkg: str, ecosystem: str = "pypi"):
    result = analyze_package(pkg, ecosystem)

    print(f"\n📦 {result['package']} ({result['ecosystem']})")
    print(f"Risk: {result['risk']['level']} ({result['risk']['score']})")

    for r in result["risk"]["reasons"]:
        print(" -", r)

@app.command()
def scan(url: str):
    if url.startswith("http"):
        path = clone_repo(url)
        scan_repo(path)
    else:
        scan_repo(url)

if __name__ == "__main__":
    app()
