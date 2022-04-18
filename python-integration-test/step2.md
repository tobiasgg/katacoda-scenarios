# Our two software modules we want to test
In this step we will present the two software modules we want to perform integration testing on.
The first one, ..., is a simple python HTTP webserver that listens for HTTP requests on port 8000. If a request is made the server should log the request. This is the functionality we want to test later on. 

To build this application we have used the built in `http` python package. 

The second module, <insert_file_name>, simulates a client and performs an HTTP request to our server.

The "logging requests"-functionality of the server is the one we will test in our integration tests later on.

Since these two modules require some additional dependencies we will run the command
`pip install requirements.txt`{{execute}}
Which will install all python packages specified in the file `requirements.txt`.

