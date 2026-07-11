import http.server
import socketserver
"""
This is a simple HTTP server that listens on port 8000 and responds with: "Hello, this is a simple API!" message for any GET request.
"""
class SimpleAPI_Handler(http.server.BaseHTTPRequestHandler):
    """
    A request handler class that handles GET requests and responds with a simple message.
    """
    def do_GET(self):
        """
        Handles GET requests by sending a 200 OK response and a simple message.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"name": "John", "age": 30, "city": "New York"}')
        
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "OK"}')

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


if __name__ == "__main__":
    """
    Starts the HTTP server.
    """
    with socketserver.TCPServer(("", 8000), SimpleAPI_Handler) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()