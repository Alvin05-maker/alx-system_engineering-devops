# Application server

In this project, I have setup an application server for the Airbnb clone project. This involved  setting up a Flask application and API service using `Gunicorn`. The application server efficiently manages business logic, API requests, and the generation of dynamic content.

## Features:
- Flask App and API Service:
    - Utilizes Gunicorn to serve the Flask application and - API service.
    - The application server handles diverse tasks, including - business logic processing and dynamic content - generation.
    - Traffic Forwarding with Nginx:

- `Nginx` is configured to forward incoming traffic to the backend service.

- A `systemd` unit service is set up to initiate the application server automatically during system boot.
Ensures continuous availability by starting the server as part of the system initialization process.

`PS` - all configuration files, and `systemd` scripts are is located in this repository folder

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240129%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240129T095833Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b586d81c4ae11730d09c94259777129c8d373b13f3fa17d23c76d219e7b5883)