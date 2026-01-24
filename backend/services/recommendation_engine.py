from .eligibility_engine import calculate_eligibility_score

def recommend_schemes(user, schemes_df):
    """
    Generates ranked scheme recommendations with explanations.
    """

    recommendations = []

    for _, scheme in schemes_df.iterrows():
        scheme_data = {
            "min_income": scheme["min_income"],
            "max_income": scheme["max_income"],
            "min_age": scheme["min_age"],
            "max_age": scheme["max_age"],
            "state": scheme["state"],
            "category": scheme["category"],
            "deadline": scheme["deadline"]
        }

        score, reasons = calculate_eligibility_score(user, scheme_data)

        if score >= 50:
            recommendations.append({
                "scheme_id": scheme["scheme_id"],
                "scheme_name": scheme["scheme_name"],
                "score": score,
                "explanation": reasons
            })

    # Rank by score (high → low)
    recommendations.sort(key=lambda x: x["score"], reverse=True)

    return recommendations
