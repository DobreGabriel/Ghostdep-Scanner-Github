import requests
from functools import lru_cache

@lru_cache(maxsize=500)
def get_pypi(pkg):
    try:
        r = requests.get(f"https://pypi.org/pypi/{pkg}/json", timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def extract_metadata(pkg):
    data = get_pypi(pkg)

    if not data:
        return {"exists": False, "author": None, "created": None}

    info = data["info"]
    releases = data["releases"]

    dates = []
    for rel in releases.values():
        for file in rel:
            if "upload_time" in file:
                dates.append(file["upload_time"])

    return {
        "exists": True,
        "author": info.get("author"),
        "created": min(dates) if dates else None
    }
