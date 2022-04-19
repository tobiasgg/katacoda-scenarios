#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
import socketserver


def main():
    # This handler prints any requests to the console
    handler = SimpleHTTPRequestHandler

    # Using port 8080 and the localhost address
    with socketserver.TCPServer(("", 8080), handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
