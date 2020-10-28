library identifier: 'jenkins-shared@master', retriever: modernSCM(
 [$class: 'GitSCMSource',
  remote: 'https://github.com/AnmolSharma05/db_project.git',
 ])

pipeline {
 environment {
  appName = "server"
  registry = "7891486294/django-server"
  registryCredential = "7891486294"
  projectPath = "/jenkins/data/workspace/project"
 }

 agent any

 stages {

  stage('Build Image') {
   steps {
    script {
      dockerImage = docker.build "$registry:latest"
     } 
    }
   }

  stage('Deploy Image') {
   steps {
    script {
      docker.withRegistry("$registryURL", registryCredential) {
      dockerImage.push()
      }
    }
   }
  }
 }
}

def getBuildName() {
 "${BUILD_NUMBER}_$appName:${params.RELEASE_TAG}"
}

def isMaster() {
 "${params.RELEASE_TAG}" == "master"
}
