#!/usr/bin/env groovy
import groovy.json.JsonOutput


def params_line(){
     def params = []
     for (param in this.args){
         params << param
     }
     if ( params.size() != 3){
         println "You have to put 4 params"
         println "For instance: get 5 + 9"
         return 1
    }
     return args
}

def request_post(params){
     String PORT = "8080"
     String ADDR = "127.0.0.1"
     def post = new URL("http://${ADDR.toString()}:${PORT.toString()}").openConnection();
     def message = ["operation":"${args[1]}","arg1":"${args[0]}","arg2":"${args[2]}"];
     String json = groovy.json.JsonOutput.toJson(message)
     post.setRequestMethod("POST");
     post.setDoOutput(true);
     post.setRequestProperty("Content-Type","application/json");
     post.getOutputStream().write(json.getBytes("UTF-8"));
     def postRC = post.getResponseCode();
     println(postRC);
     if(postRC == 200) {
         println(post.getInputStream().getText());
         }
}

def main() {
    def params = params_line()
    def result = request_post(params)
   }    
   main()

    
    
