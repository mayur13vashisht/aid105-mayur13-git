def calculate_score(user, scheme):
    score = 0

    if scheme.min_income <= user.income <= scheme.max_income:
        score += 30
    if scheme.state == "ALL" or scheme.state == user.state:
        score += 25
    if scheme.category == user.category:
        score += 20
    if scheme.min_age <= user.age <= scheme.max_age:
        score += 15

    score += 10  # deadline active
    return score
