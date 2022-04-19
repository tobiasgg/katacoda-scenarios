# Integration testing in python using the testcontainers package

This tutorial aims to show how to perform integration testing between containers in using the python package `testcontainers`. 

You will learn about the following:
1. Introduction to Integration testing.
2. The `testcontainers` python package and how to install it.
3. An approach to perform integration testing on an application with two parts deployed on seperate containers.

Testcontainers is a python package used for [integration testing](https://en.wikipedia.org/wiki/Integration_testing) between [containers](https://en.wikipedia.org/wiki/OS-level_virtualization). 

Integration testing is the art of testing the combination individual software modules as a group. In our case we will deploy two software modules on different containers and then use the `testcontainers` package to perform integration testing on both modules combined.

To learn more please visit the [testcontainers documentation](https://testcontainers-python.readthedocs.io/en/latest/).