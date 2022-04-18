# This is the client that will perform the request
import http.client

class Client:
    def __init__(self):
        pass
    def GET_request(self, adress="localhost", port=8080):
        # Performs a GET request to the target adress on specified port number
        conn = http.client.HTTPSConnection(adress, port)
        conn.request("GET", "index.html")
        conn.close()

