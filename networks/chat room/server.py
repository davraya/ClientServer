import socket
import threading

"""
 SETTING UP THE SERVER
"""
 
server = socket.socket(
    socket.AF_INET,    #AF_INET means we are using an internet socket
    socket.SOCK_STREAM # SOCK_STREAM mean we will be using TCP Transmission Control Protocol
    ) 


host = "127.0.0.1" # IP-address for the host
port = 55555           # A port number that is free for our server
server.bind((host, port)) # setting those attributes for the server


server.listen() # Allowing the server to accept connections

clients = []
nicknames = []


# This function is ment to send message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# This fucntion won't stop running unless the try catches an exception which will remove the client which triggered the exception 
def handle(client):
    while True:
        try:
            message = client.recv(1024)  # passing number of bits
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(clients)
            client.close()
            nickname = nickname[index]
            broadcast(f"{nickname} left the chat!".encode("ascii")) # When we encode a string that means it is we transform that string to a specific format so that it is more efficient to transmit or store
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("nickname: ".encode("ascii"))    # Asking the client for its nickname
        nickname = client.recv(1024).decode("ascii")
        clients.append(client)

        print(f"Nickname fo the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode("ascii")) # Send to all clients within then server
        client.send("Conneceted to the server!".encode("ascii"))  # Send to a specific client

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening ...")
receive()








