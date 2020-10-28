library identifier: 'jenkins-shared@master', retriever: modernSCM(
 [$class: 'GitSCMSource',
  remote: 'https://github.com/AnmolSharma05/db_project.git',
 ])

pipeline {
 environment {
  appName = "server"
  registry = "7891486294/django-server"
  registryCredential = "7891486294"
  projectPath = "/jenkins/data/workspace/django-server"
 }

 agent any

 parameters {
  gitParameter name: 'RELEASE_TAG',
   type: 'PT_TAG',
   defaultValue: 'master'
 }

 stages {

  stage('Basic Information') {
   steps {
    sh "echo tag: ${params.RELEASE_TAG}"
   }
  }

  stage('Build Image') {
   steps {
    script {
     if (isMaster()) {
      dockerImage = docker.build "$registry:latest"
     } else {
      dockerImage = docker.build "$registry:${params.RELEASE_TAG}"
     }
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

def getBuildName() {
 "${BUILD_NUMBER}_$appName:${params.RELEASE_TAG}"
}

def isMaster() {
 "${params.RELEASE_TAG}" == "master"
}
