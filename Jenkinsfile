node{
    def server = Artifactory.server "Art"
    def client = Artifactory.newConanClient()
    def name = client.remote.add server: server, repo: "conan-local"

    stage("Get recipe"){
        checkout scm
    }
    stage("Get dependencies and publish build info"){
        sh "mkdir -p build"
        dir ('build') {
          def b = client.run(command: "install .. --build missing")
          server.publishBuildInfo b
        }
    }
    stage("Create package"){
        client.run(command: "create . user/test -s arch=x86_64")
    }
    stage("Upload packages"){
        String command = "upload TestC* --all -r ${name} --confirm"
        def b = client.run(command: command)
    }
}
