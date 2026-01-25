from flask import Flask, request, jsonify
import pandas as pd
from services.recommendation_engine import recommend_schemes

app = Flask(__name__)

# Load dataset once at startup
SCHEMES_DF = pd.read_csv("ml/data/schemes_dataset.csv")

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "running",
        "message": "SchemeAssist AI Backend is live"
    })

@app.route("/recommend", methods=["POST"])
def recommend():
    """
    Input JSON:
    {
        "name": "Mayur",
        "age": 22,
        "income": 180000,
        "state": "Maharashtra",
        "category": "OBC"
    }
    """

    user_data = request.json

    required_fields = ["age", "income", "state", "category"]
    for field in required_fields:
        if field not in user_data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    user_profile = {
        "age": int(user_data["age"]),
        "income": int(user_data["income"]),
        "state": user_data["state"],
        "category": user_data["category"]
    }

    recommendations = recommend_schemes(user_profile, SCHEMES_DF)

    return jsonify({
        "user": user_profile,
        "total_recommendations": len(recommendations),
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(debug=True)
