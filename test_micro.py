import zmq
import random
import time

# function for selecting a random state
def random_state():
    states = [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
            "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
            "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
            "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
            "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
            "New Hampshire", "New Jersey", "New Mexico", "New York",
            "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
            "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
            "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
            "West Virginia", "Wisconsin", "Wyoming"
            ]
    return random.choice(states)

# ZeroMQ setup
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    # sends random state as a JSON 
    state = random_state()
    print("Sending JSON containing the state: ", state)
    socket.send_json({"state": state})

    # returns
    reply = socket.recv_json()
    print("Reply: ", reply)

    time.sleep(5)