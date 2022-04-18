# This is our simple webserver
from http.server import HTTPServer, SimpleHTTPRequestHandler

class RequestHandler(SimpleHTTPRequestHandler):    

    def do_GET(self):   
        # This function handles a GET HTTP request and log the 
        # client adress along with the type of request.
        self.send_response(200) 
        client_adress = SimpleHTTPRequestHandler.client_address
        self.request_history.append((client_adress, "GET"))
        print(self.request_history)

    def do_POST(self):   
        # This function handles a POST HTTP request and log the 
        # client adress along with the type of request.
        self.send_response(200) 
        client_adress = SimpleHTTPRequestHandler.client_address
        self.request_history.append((client_adress, "POST"))
        print(self.request_history)

class Server():
    def run(self, server_class=HTTPServer, handler_class=RequestHandler):
        self.request_history = []
        # This variable stores information about the previous requests 
        # that has been made to the server
        server_adress = ("0.0.0.0", 8080)
        httpd = server_class(server_adress, handler_class)
        print("Starting server...")
        httpd.serve_forever()


