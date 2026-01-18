from services.eligibility_engine import calculate_score

def recommend(user, schemes):
    results = []
    for scheme in schemes:
        score = calculate_score(user, scheme)
        if score >= 50:
            results.append((scheme.name, score))
    return sorted(results, key=lambda x: x[1], reverse=True)
