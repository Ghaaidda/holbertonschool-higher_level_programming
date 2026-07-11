from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
data = {}

@app.route("/", methods=["GET"])
def home():
    """
    Handles GET requests to the root endpoint and responds with a simple message.
    """
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    """
    Handles GET requests to the /data endpoint and responds with JSON data.
    """
    response = requests.get("http://localhost:8000/data")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Could not fetch data"}), response.status_code

@app.route("/status", methods=["GET"])
def get_status():
    """
    Handles GET requests to the /status endpoint and responds with a status message.
    """
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Handles GET requests to the /users/<username> endpoint and responds with user data.
    """
    response = requests.get(f"http://localhost:8000/users/{username}")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles POST requests to the /add_user endpoint and adds a new user.
    """
    incoming_data = request.get_json()
    response = requests.post("http://localhost:8000/add_user", json=incoming_data)

    if response.status_code == 200:
        response_data = response.json()
        data[response_data.get("name")] = response_data
        return jsonify({"message": "User added successfully"}), 201
    elif response.status_code == 400:
        return jsonify({"error": "Invalid JSON"}), 400
    elif response.status_code == 409:
        return jsonify({"error": "User already exists"}), 409
    else:
        return jsonify({"error": "Unexpected error"}), response.status_code

if __name__ == "__main__":
    """
    Starts the Flask application.
    """
    app.run(debug=True, port=5000)