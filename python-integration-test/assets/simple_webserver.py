# This is our simple webserver
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    # This variable stores information about the previous requests
    # that has been made to the server
    server_address = ("127.0.0.1", 8080)
    httpd = server_class(server_address, handler_class)
    print("Starting server...")
    httpd.serve_forever()


if __name__ == "__main__": main()