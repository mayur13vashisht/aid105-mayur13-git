from flask import Blueprint, request, jsonify

user_api = Blueprint("user_api", __name__)

users = []  # temporary in-memory store

@user_api.route("/user", methods=["POST"])
def create_user():
    data = request.json

    required = ["name", "age", "income", "state", "category"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    users.append(data)
    return jsonify({
        "message": "User profile created successfully",
        "user": data
    }), 201


@user_api.route("/users", methods=["GET"])
def list_users():
    return jsonify({
        "total_users": len(users),
        "users": users
    })
