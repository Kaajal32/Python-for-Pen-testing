#!/usr/bin/python3

import nmap #importing nmap module

scanner = nmap.PortScanner()#creating variable to call the Portscanner class
print("Welcome, this is a simple nmap automation too")#printing welcome message
print("<---------------------------------------------------->")#printing for creating divider

ip_addr = input("Please enter the IP address you want to scan: ")#prompting user to enter ip address by creating variable ip_addr
print("The IP you entered is", ip_addr)#printing out user input
type(ip_addr)#type is going to be of variable

resp = input("""\nPlease enter the type of scan you want to run
            1)SYN ACK Scan
            2)UDP Scan
            3)Comprehensive Scan \n""")#creating variable resp to will give option to user the type scan that they want to run
print("You have selected option: ", resp)#printing users response

#creating if statement for options
if resp == '1':
    print("Nmap version: ", scanner.nmap_version())#printing nmap version
    scanner.scan(ip_addr, '1-1024', '-v -sS')#initialize the scanner variable to get ip_addr, specifying port range and specify the arguments, verbose the output and perform SYN ACK scan denoted by "-sS"
    print(scanner.scaninfo())#scaninfo will display various information like tcp, the services and the method
    print("IP status:", scanner[ip_addr].state())#printing ip status: up or down by using state method that comes with nmap
    print(scanner[ip_addr].all_protocols())#printing all the protocols
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())#displaying open ports using keys method
elif resp == '2':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')#udp scan
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')#comprehensive scan, it also scan operating system you are working on
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")