import http.server
import socketserver

# Define the handler for the HTTP requests
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple HTTP server!")

# Set the port for the server to listen on
PORT = 8000

# Create the server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    # Start serving indefinitely
    httpd.serve_forever()


