import pytest

from testcontainers.compose import DockerCompose
from testcontainers.core.docker_client import DockerClient


def test_check_logs():
    with DockerCompose(".") as compose:
        docker = DockerClient()
        compose.wait_for("http://%s:8080/wd/hub" % docker.host())
        stdout, stderr = compose.get_logs()
        f = open("./server/index.html")
        expects = f.readline()
        assert expects in stdout.decode()
