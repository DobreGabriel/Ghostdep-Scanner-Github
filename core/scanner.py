from detectors.similarity import check_typosquat
from detectors.metadata import extract_metadata
from detectors.npm import extract_npm_metadata
from detectors.code_analysis import analyze_code
from scoring.risk import compute_risk

def analyze_package(pkg, ecosystem):
    sim = check_typosquat(pkg)

    if ecosystem == "npm":
        meta = extract_npm_metadata(pkg)
        code = []
    else:
        meta = extract_metadata(pkg)
        code = analyze_code(pkg)

    risk = compute_risk(pkg, sim, meta)

    if code:
        risk["score"] += 20
        risk["reasons"].append("Suspicious code")

    return {
        "package": pkg,
        "ecosystem": ecosystem,
        "risk": risk,
        "code": code
    }
