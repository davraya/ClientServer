


# Overview

This is program is a Chat Room which is consider a client server communication. When ran in different terminals (the clients and server programs) they can communicate. I put his together because I wanted to be more familiar with sockets and networking in general. 

[Software Demo Video](https://youtu.be/PiC75gvo9Xg) 

# Network Communication

I used what is known as client/server networking. This means there was an intermediate program or device that linked all the clients. Transmission Control Protocol (TCP) was used for this networking program. TCP has some nice features that User Datagram Protocol (UDP) lack, but that doesn't mean one is better then. TCP breaks downs data into smaller packets and ensures both endpoint are connected. TCP is more reliable for this two reasons, but it is slower. In order to send this packets efficiently encoding (transforming the data into another format) and decoding (changing the data back into its original format).

Port Number used: 55555
Format: ascii

# Development Environment

I used Python and its socket and threading libraries. 

# Useful Websites

* [Video Tuorial I used](https://www.youtube.com/watch?v=YwWfKitB8aA)
* [Python's official documentation for the socket library](https://docs.python.org/3/library/socket.html)

# Future Work
* It will interesting to learn how to send other type of data that is no just text. Like pictures and audios.
*  
