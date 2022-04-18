from testcontainers.compose import DockerCompose

def main():
    with DockerCompose(".", compose_file_name=["docker-compose.yml"]) as compose:
        stdout, stderr = compose.get_logs()
        print(stdout)



if __name__ == '__main__': main()