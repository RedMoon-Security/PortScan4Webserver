#!/usr/bin/python

# Resolves a domain name to an IP address
# Takes the IP address and passes it to nmap that scans the web server for the most common web server ports
# Prints out the status (open/closed/filtered) 
# If the port is open the program will attempt to find the Product/Software running on the port as well as the version

import sys
import nmap
import socket


print("\nUsage: Enter a domain or IP address at the prompt\n")
domain = raw_input ("IP address or Domain: ")
IP_address = socket.gethostbyname(domain)

target = str(IP_address)
ports = [7,13,21,22,23,25,37,43,53,70,79,80,110,111,135,139,143,161,443,445,587,993,995,1723,2077,2082,2083,3306,3389,5900,8008,8080,8333]
# Add/remove additional ports as you see fit (These are the most common web server ports)

scanning = nmap.PortScanner()

print( ' ')    
print("Author: Warren Vos <info@redmoonsecurity.com>")
print("GitHub: https://github.com/RedMoon-Security/RedWebScanner")
    
print( ' ')
print( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@               @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@')
print( '@@@@@@@   @@@@@@@@@         @@@@@@@@@@@      @@@@@@@@@                       @@@@@@@@@       @@@@@@@@@@@@@@     @@@@@@@')
print( '@@@@@@@   @@@@@@@@@           @@@@@@@@@@     @@@@@@@@@                       @@@@@@@@@           @@@@@@@@@@@    @@@@@@@')
print( '@@@@@@@   @@@@@@@@@           @@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@             @@@@@@@@@    @@@@@@@')
print( '@@@@@@@   @@@@@@@@@       @@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@             @@@@@@@@@@   @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@             @@@@@@@@@,   @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@                       @@@@@@@@@            @@@@@@@@@@    @@@@@@@')
print( '@@@@@@@   @@@@@@@@@    @@@@@@@@@@@           @@@@@@@@@                       @@@@@@@@@          @@@@@@@@@@@     @@@@@@@')
print( '@@@@@@@   @@@@@@@@@      @@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@')
print( '@@@@@@@   @@@@@@@@@        @@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@')
print( '@@@@@@@   @@@@@@@@@         @@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@            @@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@   @@@@@@@           @@@@@@@            @@@@@@@@@@                  @@@@@@@@@@           @@@@@@@         @@@@@@@')
print( '@@@@@@@   @@@@@@@@@        @@@@@@@@        @@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@       @@@@@@@@@       @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@     @@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@     @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@ @@@@@@@@@@@@    @@@@@@@@          @@@@@@@    @@@@@@@          @@@@@@@    @@@@@@@@@@@@@   @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@            @@@@@@@  @@@@@@@            @@@@@@@   @@@@@@@@@@@@@@@ @@@@@@@')
print( '@@@@@@@   @@@@@@@ @@@@@@@@@  @@@@@@    @@@@@@@            @@@@@@@  @@@@@@@            @@@@@@@   @@@@@@@  @@@@@@@@@@@@@@')
print( '@@@@@@@   @@@@@@@   @@@@@    @@@@@@    @@@@@@@@          @@@@@@@    @@@@@@@          @@@@@@@@   @@@@@@@    @@@@@@@@@@@@')
print( '@@@@@@@   @@@@@@@     @@     @@@@@@     @@@@@@@@@@    @@@@@@@@@      @@@@@@@@@    @@@@@@@@@     @@@@@@@      @@@@@@@@@@')
print( '@@@@@@@   @@@@@@@            @@@@@@       @@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@      @@@@@@@        @@@@@@@@')
print( '@@@@@@@   @@@@@@@            @@@@@@           @@@@@@@@@@@@                @@@@@@@@@@@@          @@@@@@@          @@@@@@')
print( '                                                                                                                       ')
print( '                                                                                                                       ')
print( ' @@@@@@@        @@@@@@@@         @@@@@@@@        @@@   @@@        @@@@@@@@@        @@@       @@@@@@@@@        @@@  @@@ ')
print( '@@@@@@          @@@@@@@@        @@@              @@@   @@@        @@@    @@@       @@@          @@@            @@@@@@  ')
print( '     @@@@       @@@             @@@              @@@   @@@        @@@@@@@          @@@          @@@              @@    ')
print( '@@@@@@@@        @@@@@@@@@        @@@@@@@@         @@@@@@@         @@@   @@@        @@@          @@@              @@    ')
print(' ')

print("\nScanning " + target + " (" + (str(domain)) + ") using the following common web server ports:")
print(" ")

print('# 7  - Echo                     # 143 - IMAP')                                           
print('# 13 - Daytime                  # 443 - HTTPS')
print('# 21 - FTP                      # 445 - Microsoft-ds')    
print('# 22 - SSH                      # 587 - SMTP SSL')
print('# 23 - Telnet                   # 993 - IMAP SSL')   
print('# 25 - SMTP                     # 995 - POP3 SSL')
print('# 37 - Time                     # 1723 - PPTP')
print('# 43 - Nicname                  # 2077 - WebDAV cPanel')
print('# 53 - DNS                      # 2082 - cPanel')
print('# 70 - Gopher                   # 2083 - cPanel SSL')
print('# 79 - Finger                   # 3306 - MySQL')
print('# 80 - HTTP                     # 3389 - MS WBT Server (RDP)')
print('# 110 - POP3                    # 5900 - VNC')
print('# 111 - rpcbind                 # 8008 - HTTP Alternate') 
print('# 135 - msrpc                   # 8080 - HTTP Alternate')
print('# 139 - Netbios-ssn             # 8333 - VMware Server Management & Bitcoin') 
print(" ")
print('Results:')
print('-' * 50 + '\n')

for port in ports:
    portscan = scanning.scan(target,str(port))
    print("Port " + str(port) + " is " + portscan['scan'][target]['tcp'][port]['state'])
    if len(portscan['scan'][target]['tcp'][port]['product']) <= 0:
        pass
    else:
        print('-' * 50)
        print("*Running " + portscan['scan'][target]['tcp'][port]['product'])
    if len(portscan['scan'][target]['tcp'][port]['version']) <= 0:
        print(" ")
    else:
        print("*"+ portscan['scan'][target]['tcp'][port]['product'] + " is version " + portscan['scan'][target]['tcp'][port]['version'])
        print('-' * 50)
        print('')

