# Creating and running our integration tests 
Now it is finally time to create our integration tests using `testcontainers`, we create a new file, called `integration-test.py`{{open}} where we import the package and use the DockerCompose submodule.

In this test case we want to make sure that the client prints the received information from the server.

To run the test we use the python package `pytest`. We install this package by running the following command:
`pip install pytest`{{execute}}.

With `pytest` installed we can now run our tests:
`pytest integration-test.py`{{execute}} 