from simple_webserver import Server
from client import Client
from testcontainers import DockerCompose

def main():
    with DockerCompose("/home/project",
                   compose_file_name=["docker-compose-1.yml", "docker-compose-2.yml"],
                   pull=True) as compose:
    host = compose.get_service_host("hub", 4444)
    port = compose.get_service_port("hub", 4444)
    driver = webdriver.Remote(
        command_executor=("http://{}:{}/wd/hub".format(host,port)),
        desired_capabilities=CHROME,
    )
    driver.get("http://automation-remarks.com")
    stdout, stderr = compose.get_logs()
    if stderr:
        print("Errors\n:{}".format(stderr))
        
    server = Server()
    client = Client()
    server.run()
    client.GET_request()


if __name__ == '__main__': main()