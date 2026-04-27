import requests

def extract_npm_metadata(pkg):
    try:
        r = requests.get(f"https://registry.npmjs.org/{pkg}", timeout=5)
        if r.status_code != 200:
            return {"exists": False, "author": None, "versions": 0}

        data = r.json()

        return {
            "exists": True,
            "author": data.get("author"),
            "versions": len(data.get("versions", {}))
        }
    except:
        return {"exists": False, "author": None, "versions": 0}
