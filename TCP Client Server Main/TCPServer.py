#Sockets initialize connection, sending and receiving of data. In technical point of view a socket is an internal endpoint for sending and receiving data.

#here we are using socket library

#importing socket module
#syntax: creating object, object will then call the socket function, in that socket fucntion we have parameters that needs to be specified
#parameters:socket family is specified in the form afinet, socket type using socstream

#afinet are used to specify IPv4 or IPv6
#socstream (TCP) and socdegram (UDP)

#!/usr/bin/python3

import socket

#creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

#binding the socket
serversocket.bind(('192.168.0.101', port))

#starting TCP listener
serversocket.listen(3)

while True:
    #starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from %s" % str(address))

    message = 'hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()