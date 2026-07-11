from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/", methods=["GET"])
def home():
    """Handles GET requests to the root endpoint."""
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def get_status():
    """Returns a simple status message."""
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Returns a single user's data, or 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user from the posted JSON body."""
    incoming = request.get_json(silent=True)

    if incoming is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = incoming.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = incoming
    return jsonify({"message": "User added", "user": incoming}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)