pipeline {
   agent any

 

   stages {
      stage('Pull') {
          steps {
              echo 'pulling now'   
          }
      }
      stage('Test') {
          steps {
              echo 'testing now'
          }
      }
      stage('Build') {
         steps {
           echo 'building now '
         }

         post {
            success {
               echo 'sucesss full'
            }
         }
      }
   }
}
