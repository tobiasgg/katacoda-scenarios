# Creating and running our integration tests 
Now it is finally time to create our integration tests using `testcontainers`, we create a new file, called `integration_test.py` where we import the package.

In this test case we want to make sure that the request being made by module 2 to the server in module 1 is in fact logged in the `server.request_history` variable.

We run the integration test using the following command:
`python /integration_test.py`{{execute}} 