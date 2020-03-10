#!/usr/bin/env groovy
   
    Map<String, String> parameters = new LinkedHashMap<>();

    def request = "nothing"
   
    for (String arg : args) {
        String[] parts = arg.split("=", 2);
        String key = parts[0];
        if (key.startsWith("--")) {
            key = key.substring(2);
        } else {
            key = key.substring(1);
        }
        
        String value = parts[1];
       if (key=="request"){
           request = value
       } 
       
           
        parameters.put(key, value);
       }
       if (request=="Post"){
           request_post(parameters)
       }
       if (request=="Get"){
           request_get(parameters)
       }
       

   def request_post(parameters){
        System.out.println(parameters);  
        def baseUrl = new URL("http://172.18.214.37:9000")
   
        def queryString = parameters
        def connection = baseUrl.openConnection()
        connection.with {
        doOutput = true
        requestMethod = 'POST'
        outputStream.withWriter { writer ->
        writer << queryString
        }
   
        println(connection.getInputStream().getText());
        }
       } 
    def request_get(parameters){
        def get = new URL("http://172.18.214.37:9000/api/add/5/6").openConnection()
    if (get.getResponseCode().equals(200)){
        println(get.getInputStream().getText());
    }   
    }
