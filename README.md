# CS361-Microservice
Microservice for Thomas Hausfeld in CS361
# Usage
When this microservice recieves a JSON file through ZeroMQ, if the file contains a valid state, then a pokemon go fun fact relating to that state is returned in a JSON file to the client.
# Example calls for ZeroMQ
Call using Oregon 
```
socket.send_json({"state": "Oregon"})
```
Recieve
```
reply = socket.recv_json()
```
#UML Sequence Diagram

![alt text](UML.JPG)
