import pytest

from testcontainers.compose import DockerCompose
from testcontainers.core.docker_client import DockerClient


def test_check_logs():
    with DockerCompose(".") as compose:
        # Starting docker
        docker = DockerClient()
        compose.wait_for("http://%s:8080/wd/hub" % docker.host())
        stdout, stderr = compose.get_logs()

        # Checks that the first line of index.html exists in the output (client should print it)
        f = open("./server/index.html")
        expects = f.readline()
        assert expects in stdout.decode()
