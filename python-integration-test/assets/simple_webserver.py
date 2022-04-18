# This is our simple webserver
from http.server import HTTPServer, SimpleHTTPRequestHandler

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):   
        # This function handles a GET HTTP request and log the 
        # client adress along with the type of request.
        self.send_response(200) 
        client_adress = self.client_address
        print((client_adress, "GET"))
        return SimpleHTTPRequestHandler.do_get(self)


def main(server_class=HTTPServer, handler_class=RequestHandler):
    server_adress = ("127.0.0.1", 8080)
    httpd = server_class(server_adress, handler_class)
    print("Starting server...")
    httpd.serve_forever()


if __name__ == '__main__': main() 
