# Integration testing in python using the testcontainers package
In general, large software projects are split up into smaller modules that can be deployed on different containers. Since integration testing is an important part of testing the quality of software, being able to test different containers in unison is very important. This tutorial aims to show how this can be done using Docker and the python package `testcontainers`. 

You will learn about the following:
1. Introduction to Integration testing.
2. The `testcontainers` python package and how to install it.
3. An approach to perform integration testing on an application with two parts deployed on seperate containers.

A small prerequisite for this course is basic knowledge of Docker and containers.

Testcontainers is a python package used for [integration testing](https://en.wikipedia.org/wiki/Integration_testing) between [containers](https://en.wikipedia.org/wiki/OS-level_virtualization). 

Integration testing is the art of testing the combination individual software modules as a group. In our case we will deploy two software modules on different containers and then use the `testcontainers` package to perform integration testing on both modules combined.

To learn more please visit the [testcontainers documentation](https://testcontainers-python.readthedocs.io/en/latest/).

Good luck! 