#!/usr/bin/python3

import socket#importing socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creating variable and using socket class from socket module and call methods AF_INET for IPv4 and SOCK_STREAM the type of connection like TCP where handshake is going on
s.settimeout(5)#making the script faster by setting timeout

host = input("Please enter the IP you want to scan: ")#creating host variable to get the IP address
port = int(input("Please enetr the port you want to scan: "))#creating variable to enter the port

def portScanner(port):#creating function portscanner
    if s.connect_ex((host, port)):#connect address however it returns error code (if open or closed) which terminates and gives our result and we have passed our values ip and port. In conclusion it sees if port is closed
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)#calling the fucntion portscannere and passing the value