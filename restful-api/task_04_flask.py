#!/usr/bin/python3
from flask import Flask, jsonify, request


# Create an instance of the Flask class
app = Flask(__name__)

# Initialize an empty dictionary to store user data
users = {}


@app.route("/")
def home():
    """
    Handles the root route of the Flask API.

    Returns:
        str: A welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Retrieves a list of usernames from the 'users' dictionary 
    and returns it as a JSON response.

    Returns:
        json: A JSON response containing a list of usernames.
    """
    # Convert the dictionary keys (usernames) to a list and return as JSON
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Provides the status of the API.

    Returns:
        str: The status message "OK".
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    Retrieves user information based on the provided username.

    Args:
        username (str): The username of the user to retrieve information for.

    Returns:
        json: The user information if found, or an error message 
              if the user is not found, with a 404 status code.
    """
    # Fetch the user data from the dictionary using the username
    user = users.get(username)
    if user:
        # If the user is found, return the user data as JSON
        return jsonify(user)
    else:
        # If the user is not found, return an error message with a 404 status
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the system.

    Returns:
        json: A JSON response with the following structure:
            - If the JSON data is invalid: {"error": "Invalid JSON data"}
            - If the username already exists: {"error": "Username already exists"}
            - If the user is successfully added: 
              {"message": "User added", "user": <user_data>}
            - If an exception occurs: {"error": <exception_message>}
    """
    # Get the JSON data from the incoming request
    new_user = request.get_json()

    # Extract the username from the new user data
    username = new_user.get("username")

    # Check if the username is provided
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Add the new user to the users dictionary
    users[username] = new_user

    # Return a success message along with the added user data
    return jsonify({"message": "User added", "user": users[username]}), 201


# Start the Flask application
if __name__ == "__main__":
    app.run()
