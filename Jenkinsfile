pipeline{
    agent any
    stages{
        stage('build'){
            dockerImage = docker.build "7891486294/capstone2:latest"
        }
        stage('deploy'){
            docker.withRegistry("https://hub.docker.com/repository/docker/7891486294/capstone2",7891486294){
                dockerImage.push()
            }
        }
    }
}
