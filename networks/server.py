

# SOCK_STERAM = TCP is more reliable, but not as quick. Lets you know if every packet has succesfully been deliverd. (Transmission Control Protocol)
# SOCK_GRAM = UDP is non sequencial ( no roder), no guaranteed deliverance (User Datagram Protocol)

# End points are exactly that, communication end points between sockets. 

import socket as skt

HOST = "10.50.108.41"
PORT = 9090

server = skt.socket(skt.AF_INET, skt.SOCK_STREAM)  # socket for hosting
server.bind((HOST, PORT))

server.listen() # can pass the conecction limmit as an int

while True:
    communicatino_socket, address = server.accept() # individual socket for individual client; server endpoint
    print(f"Connnected to {address}")
    message = communicatino_socket.recv(1024).decode("utf-8")
    print(f"Message from client is: {message}")
    communicatino_socket.send(f"Got you message!".encode("utf-8"))
    print(f"Connection with {address} ended")