    1. 创建网络
    docker network create docker_network_test
    docker network ls

    2. app:
    docker build -t docker_flask_image:v1.0 .
    docker run --network docker_network_test --name docker_flask_name -d -p 9102:5000 docker_flask_image:v1.0

    3. mysql：
    docker build -t docker_mysql_image:v1.0 .
    docker run --network docker_network_test  --name docker_mysql_name -e MYSQL_ROOT_PASSWORD=123456 -p 9103:3306 -d docker_mysql_image:v1.0