# This is our simple webserver
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Server:
    def __init__(self):
        self.access = False
    
    def run(self, server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
        server_adress = ("0.0.0.0", 8000)
        httpd = server_class(server_adress, handler_class)
        print("Starting server...")
        httpd.serve_forever()


