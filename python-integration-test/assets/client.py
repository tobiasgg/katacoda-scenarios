# This is the client that will perform the request
import http.client

class Client:
    def GET_request(self, adress="127.0.0.1", port=8080):
        # Performs a GET request to the target adress on specified port number
        conn = http.client.HTTPSConnection(adress, port)
        conn.request("GET", "index.html")
        conn.close()

def main():
    client = Client()
    client.GET_request()

if __name__ == '__main__':
    main()
