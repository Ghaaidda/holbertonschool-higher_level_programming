from flask import Flask, jsonify, request

app = Flask(__name__)
data = {}

@app.route("/", methods=["GET"])
def home():
    """Handles GET requests to the root endpoint."""
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    """Returns all stored user data as JSON."""
    return jsonify(data)

@app.route("/status", methods=["GET"])
def get_status():
    """Returns a simple status message."""
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Returns a single user's data, or 404 if not found."""
    user = data.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user from the posted JSON body."""
    incoming = request.get_json(silent=True)

    if not incoming or "name" not in incoming:
        return jsonify({"error": "Invalid JSON"}), 400

    username = incoming["name"]
    if username in data:
        return jsonify({"error": "User already exists"}), 409

    data[username] = incoming
    return jsonify({"message": "User added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)