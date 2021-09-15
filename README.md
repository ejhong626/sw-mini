# sw-mini
Senior Mini Project
A barcode scanning application with nutritional info from FDA API.

# File Names
* env: virtual environment folder, keep in same directory as top folder for *server*
* server: contains most of the Django code

# Design Choices
![alt text](Design.png)
## Backend
The intial intent was to have a Django framework serving as a backend service for the ReactJS frontend to interact. The interaction would be mostly through HttpResponse and Url queries. At its current state, all interactions between the frontend and backend would operate as listed in the following:
* **User creates a recipe or log**: Sends HttpResponse to Backend with JSON in body, then invokes function through url call. JSON contains information on who made the instance and what ingredients are involved
* **User queries for their recipe or log**: Frontend would curl into a url linked to the user's username to retrieve the desired information
* **Frontend requests nutritional data for recipe or log**: Frontend curls to the url for the specific recipe/log, followed by a function name to get a JSONResponse

## Frontend

# Development
## Backend (Edward Hong)
### Django Framework
The backend started from Mozilla's article on making web frameworks, I chose [Django Framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks) since I had some experience dealing with it. I started implementing the models and views I planned in the Design image shown above and was successful in interacting with it through shell commands. 
Most of my time went into research on binding url patterns to the Django Views I designed. At its current state, I can navigate the framework with curl from shell and retrieve information with the appropriate commands.
(Post images of the functions working)
Once its completed to an operational state, I tried to deploy the project on Firebase. However, I found out that the framework I was developing was not suitable to deploy on Firebase, the host that we were trying to use. Firebase is more suitable for static content but the Django framework is designed to be dynamic. 

### Deploying Django framework on Firebase
The Firebase documentation provides a method to deploy a Django project on their website, and the process goes as follows. I would pair Google Cloud Run with Firebase to build the REST APIs as microservices. That is done by deploying the framework as an application packaged in a container image. Then, Firebase can direct HTTPS requests to the containerized app. ([Link](https://firebase.google.com/docs/hosting/cloud-run))
(Post images of containerizing app)

## Frontend (Eva Zhou)


# Findings


# Credits
**Front End Designer**: Eva Zhou
**Back End Designer**: Edward Hong
