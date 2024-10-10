#!/usr/bin/python3

"""This script implements a simple API using Flask with JWT and basic
authentication to manage user roles and access control."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

# Initialize the Flask application and configure the secret key for JWT
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Set up basic authentication and JWT manager
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Predefined users with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Validate the user's credentials.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        dict: The user's information if the credentials are valid.
        None: If the credentials are invalid.
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    A route that requires basic authentication.

    Returns:
        str: A success message indicating access is granted.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate the user and generate a JWT token if valid.

    Expects JSON input with username and password.

    Returns:
        dict: JSON response with JWT token if authentication is successful.
        dict: JSON response with error message if authentication fails.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = verify_password(username, password)

    if user:
        # Create and return a JWT token for the authenticated user
        access_token = create_access_token(
            identity={
                'username': username,
                'role': user['role']})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    A route that requires a valid JWT for access.

    Returns:
        str: A success message indicating access is granted.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    A route restricted to admin users only.

    Returns:
        str: A success message indicating admin access is granted.
        dict: JSON response with an error message if the user is not an admin.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle cases of missing or invalid JWT tokens.

    Args:
        err (str): The error message.

    Returns:
        dict: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle cases of invalid JWT tokens.

    Args:
        err (str): The error message.

    Returns:
        dict: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle cases of expired JWT tokens.

    Args:
        err (str): The error message.

    Returns:
        dict: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle cases of revoked JWT tokens.

    Args:
        err (str): The error message.

    Returns:
        dict: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle cases where a fresh JWT token is required.

    Args:
        err (str): The error message.

    Returns:
        dict: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
