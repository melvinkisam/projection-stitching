import socket
import cv2

s = socket.socket()
s.bind((socket.gethostname(), 8888))

def serverCalls():         
    s.listen()
    print("Listening...")
    clientsocket, address = s.accept()
    f = open("receivedImage.png", "wb")
    with clientsocket:
        print("Connected by", address)
        
        while True:
            image = clientsocket.recv(1024)
            if str(image) == "b''":
                break
            f.write(image)
        print("Image received!")
        cv2.imshow("Output.png", image)

while True:    
    serverCalls()
