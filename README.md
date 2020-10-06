# Django CRUD App using Django Rest Framework and Docker Container
# DOCKER 
   Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package.

# DJANGO

  Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

# DJANGO ResTFramework
   Django REST framework is a powerful and flexible toolkit for building Web APIs.Django REST framework is a powerful and flexible toolkit for building Web APIs.

   Some reasons you might want to use REST framework:

   The Web browsable API is a huge usability win for your developers. Authentication policies including packages for OAuth1a and OAuth2. Serialization that supports both ORM and non-ORM data sources. Customizable all the way down - just use regular function-based views if you don't need the more powerful features. Extensive documentation, and great community support. Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

# MONGODB 
MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public Licens


 Getting Started
 ---------------
 ---------------
 Installation 
 ------------
   * Install Docker  (You can also go to docker installation Guide  [docker](https://docs.docker.com/engine/) )
   * After Cloning the Repo go to the Repo folder and run the following commnads to deploy and run the docker 
   * Docker-compose to start our App
    
     
   
    ```bash
        $ sudo apt-install docker
        $ sudo docker compose  up -d --build
     ```
    * Now our Containers are Up and running
    * To check the status of our containers  and get the Container ID for our app
     $ sudo docker ps 
     * Addind Json to our Mongodb server
     $ sudo docker exec -it <CONTAINER_ID> /bin/sh
     * In the shell
     $ python manage.py shell < add_data.py
     * EXIT from shell $ exit


  # CRUD operation 

  * open your browser 
     * Enter the following : 
        serveraddress/URLs  to perform Actions
    * 0.0.0.0:8000/URLS or 127.0.0.1:8000/URLS or localhost:8000/URLS

    |Methods | URLs             | Actions              |
    | ---    | -----------      | -------------------- |
    | GET    |	api/products/    |	get all products   | 
    | GET	 | api/products/:id |	get product by id  |
    | POST	 | api/products/    |	add new product    |
    | PUT	 | api/products/:id/| update product by id |
    | DELETE | api/products/:id/| remove product by id |
    | DELETE | api/products/ 	| remove all products  |
 # Web UI
  * Enter the following address to access the Api server
    https://0.0.0.0:8000  
  * To perform CRUD operations
    https://0.0.0.0:8000/URLS 
  
  # API Exposed Endpoints Screenshot Via POSTMAN
   * READ 
   * ![READ](https://github.com/adityasugandhi/Dockerize-DjangoRestApi/blob/master/Postman/Read.png)
   * DELETE
     ![DELETE](https://github.com/adityasugandhi/Dockerize-DjangoRestApi/blob/master/Postman/Delete%20Sucess.png)
   * Post_Delete
      ![Delete_Suceess](https://github.com/adityasugandhi/Dockerize-DjangoRestApi/blob/master/Postman/Delete.png)
   * Update
      ![UPDATE](https://github.com/adityasugandhi/Dockerize-DjangoRestApi/blob/master/Postman/Update.png)
  
 

# Additional Information
 * This app is configure to use Mongodb local server
 * I have included both configuration for local monogdb server and mongodb Atlas Cloud server
 * I have used data dump of 5000 customers 
   


 
 
