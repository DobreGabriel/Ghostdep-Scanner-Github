from datetime import datetime

def age_days(created):
    try:
        return (datetime.now() - datetime.fromisoformat(created)).days
    except:
        return None

def compute_risk(pkg, sim, meta):
    score = 0
    reasons = []

    if sim:
        score += 40
        reasons.append(f"Similar to {sim['target']}")

    if not meta["exists"]:
        score += 30
        reasons.append("Not found on registry")

    if meta.get("created"):
        age = age_days(meta["created"])
        if age is not None and age < 30:
            score += 20
            reasons.append("Recently created")

    if not meta.get("author"):
        score += 10
        reasons.append("Unknown author")

    level = "LOW"
    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"

    return {"score": score, "level": level, "reasons": reasons}
