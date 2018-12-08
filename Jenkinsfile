pipeline {
    agent {
        node {
          label "3s-Server-Test"
        }
    }
    stages {
        stage("build-app-image") {
            steps{
                dir("app"){
                    echo "构建镜像ing"
                    sh "docker build -t hub.mobvista.com/xihong_test/docker_flask_image:v${env.BUILD_ID} ."
                }
            }
        }
        stage("build-mysql-image") {
            steps{
                dir("db"){
                    echo "构建镜像ing"
                    sh "docker build -t hub.mobvista.com/xihong_test/docker_mysql_image:v${env.BUILD_ID} ."
                }
            }
        }
        stage("push-image") {
            steps{
                echo "推送镜像ing"
                sh "docker push hub.mobvista.com/xihong_test/docker_flask_image:v${env.BUILD_ID}"
                sh "docker push hub.mobvista.com/xihong_test/docker_mysql_image:v${env.BUILD_ID}"
            }
        }
    }
}

