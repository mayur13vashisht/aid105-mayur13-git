from datetime import datetime

def calculate_eligibility_score(user, scheme):
    """
    Calculates eligibility score (0–100) and returns
    both score and explanation list.
    """

    score = 0
    reasons = []

    # 1. Income Check (30 points)
    if scheme["min_income"] <= user["income"] <= scheme["max_income"]:
        score += 30
        reasons.append("Income falls within eligible range (+30)")
    else:
        reasons.append("Income does not match eligibility range (+0)")

    # 2. State Match (25 points)
    if scheme["state"] == "ALL" or scheme["state"].lower() == user["state"].lower():
        score += 25
        reasons.append("State eligibility matched (+25)")
    else:
        reasons.append("State not eligible for this scheme (+0)")

    # 3. Category Match (20 points)
    if scheme["category"].lower() == user["category"].lower():
        score += 20
        reasons.append("Category eligibility matched (+20)")
    else:
        reasons.append("Category does not match (+0)")

    # 4. Age Check (15 points)
    if scheme["min_age"] <= user["age"] <= scheme["max_age"]:
        score += 15
        reasons.append("Age criteria satisfied (+15)")
    else:
        reasons.append("Age not within scheme limits (+0)")

    # 5. Deadline Urgency (10 points)
    try:
        deadline_date = datetime.strptime(scheme["deadline"], "%Y-%m-%d")
        days_left = (deadline_date - datetime.today()).days

        if days_left >= 0:
            score += 10
            reasons.append(f"Scheme active, {days_left} days left (+10)")
        else:
            reasons.append("Scheme deadline passed (+0)")
    except:
        reasons.append("Invalid deadline format (+0)")

    return score, reasons
