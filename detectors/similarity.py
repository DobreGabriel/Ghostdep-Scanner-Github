from difflib import SequenceMatcher
import unicodedata

POPULAR = ["requests", "numpy", "pandas", "flask", "django", "express", "react"]

def normalize(name: str) -> str:
    return unicodedata.normalize("NFKD", name)

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def check_typosquat(pkg: str):
    pkg_norm = normalize(pkg.lower())

    for legit in POPULAR:
        score = similarity(pkg_norm, legit)
        if score > 0.88 and pkg != legit:
            return {
                "target": legit,
                "score": round(score, 2)
            }

    return None
