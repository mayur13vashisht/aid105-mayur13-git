from flask import Blueprint, jsonify

recommendation_api = Blueprint("recommendation_api", __name__)

@recommendation_api.route("/recommend")
def recommend():
    return jsonify({"status": "Recommendation endpoint working"})

from routes.recommendation_routes import recommendation_api
app.register_blueprint(recommendation_api)
