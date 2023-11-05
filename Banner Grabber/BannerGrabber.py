#!/usr/bin/python3

#BannerGrabber can be used for creating vulnerability scanner

import socket #importing socket module

#banner grabbing fucntion
def banner(ip, port):#creating banner function and accepting parameter ip and port
    s = socket.socket()#intialiazing socket module using socket class
    s.connect((ip, int(port)))#connecting to ip and port connect class from socket
    s.settimeout(5)#setting timeout
    print(s.recv(1024).decode("utf-8"))#printing the banner without 'string 'b', 'r' and 'n'


def main(): #first creating fucntion for ip_addr
    ip = input("Please enter the IP: ")#creating variable to input ip_addr
    port = str(input("Please enter the port: "))#creating variable input port which is converted into string
    banner(ip,port)#calling the function banner

main()#will give us banner function 