#!/usr/bin/python3

"""This script implements a simple HTTP server that responds to GET requests
with either plain text or JSON data, depending on the requested path."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Define the port for the server
PORT = 8000


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests based on the requested path."""

        if self.path == '/':
            # Respond to the root path with a greeting message
            self._send_response(200, "Hello, this is a simple API!")

        elif self.path == '/data':
            # Respond to '/data' path with a JSON object
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_response(200, json.dumps(data), 'application/json')

        elif self.path == '/info':
            # Respond to '/info' path with API version
            # and description in JSON format
            info = (
                '{"version": "1.0", '
                '"description": "A simple API built with http.server"}'
            )
            self._send_response(200, info)

        elif self.path == '/status':
            # Respond to '/status' path with a simple status message
            self._send_response(200, "OK")

        else:
            # Respond with 404 Not Found for any other paths
            self._send_response(404, "404 Not Found")

    def _send_response(self, status_code, message, content_type='text/plain'):
        """
        Helper function to send an HTTP response.

        Args:
            status_code (int): The HTTP status code to send.
            message (str): The message to send in the response body.
            content_type (str): The content type of the response
            (default: 'text/plain').
        """
        # Send the HTTP status code
        self.send_response(status_code)
        # Set the content type
        self.send_header('Content-type', content_type)
        # End the headers section
        self.end_headers()
        # Write the message to the response
        self.wfile.write(message.encode('utf-8'))


def run():
    """Start the HTTP server on the specified port."""
    # Create and start the HTTP server with the custom handler
    httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
    # Inform the user of the server's status
    print(f"Server running on port {PORT}")
    # Run the server indefinitely
    httpd.serve_forever()


if __name__ == "__main__":
    # Execute the run function if the script is run directly
    run()
