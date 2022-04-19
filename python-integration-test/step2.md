# Our two software modules we want to test
In this step we will present the two software modules we want to perform integration testing on.

The first one, `/server/simple_webserver.py`{{open}}, is a simple python TCP-server that listens for TCP-connections on port 8080. If a connection is established the server prints the request to the standard output.

To build this application we have used the built in `socketserver` python package. To read the documentation of this package visit this [link](https://docs.python.org/3/library/socketserver.html)

The second module, `/client/client.py`{{open}}, simulates a client that establishes a connection with the server. After establishing a connection the client sends a "GET-request" and prints the received content to standard output.

The printing-functionality of the client is the one we will test in our integration tests later on.


