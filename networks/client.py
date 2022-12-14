import socket as skt

HOST = "10.50.108.41"
PORT = 9090

socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)  # we concect and send with the same socket; client endpoint
socket.connect((HOST, PORT)) 

socket.send("Hello World".encode("utf-8"))
print(socket.recv(1024)) # message received from the server

