## EK
=====================

This repo contains the server (remote) and client of the Assignment


### Requirements:
#### Remote:
The Remote part of the app needs **npm** and **node** to function. 
To be able to connect the DB you need either docker or mongodb installed locally.
In either case "mongo" must be reachable on localhost:28000.

to easily install the remote brachn run sh remote/start.sh. This creates a docker container with mongdb installed
as "mongo_nodeapp_prieger".
The server runs on port 9001.
To verifiy that the server is running: GET http://localhost:9001/api/test
To verify that the docker container with the user table is installed: GET  http://localhost:9001/api/users  
this shows the list of all usernames.

#### Client:
The client application is packaged via pyinstall so that no additional dependencies are required when running the app
However for the purpose of developing the app ypu should run **make install** (this installs pyqt5, pyinsaller and websocket-client using **pip3**)
This requires pip3 to be availible. 
To build the app via pyinstall run **make build**
To run the app use python3 client/main.py

The build files are located in client/build
