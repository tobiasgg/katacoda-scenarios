# Setting up Docker Compose
We will use [Docker Compose](https://docs.docker.com/compose/) to containerize our application. Docker Compose is a tool for defining and running multi-container Docker applications. To configure Docker Compose we have created the file `docker-compose.yml`{{open}}. In this file we have specified what containers should be built and in what order. In our case we first build the `server`container, which is specified in `/server/Dockerfile.server`{{open}}, and afterwards the `client`container, which is specified in `/client/Dockerfile.client`{{open}}.

We build our containers by running
`docker-compose build`{{execute}}

To read more about what Docker is and its uses please visit the [Docker website](https://docs.docker.com/get-started/overview/). We will use Docker Compose as it is one of the multi-container tools that the `testcontainers` package has support for. 

The `testcontainers`package also has support for 
* Selenium Grid containers
* Selenium Standalone containers
* MySql Db containers
* MariaDb containers
* Neo4j containers
* OracleDb containers
* PostgreSQL Db containers
* ClickHouse containers
* Microsoft SQL Server containers
* LocalStack
* RabbitMQ

Please read the [testcontainers documentation](https://testcontainers-python.readthedocs.io/en/latest/) for more information about how to use these container tools togheter with `testcontainers`.