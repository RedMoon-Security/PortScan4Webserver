# RedWeb-Scanner

Visit us at (https://redmoonsecurity.com)

**A small python script to perform port scanning on a webserver. It resolves a domain name to an IP address and then uses nmap to scan the target using the most common ports for webservers.**

Below is a screenshot of the output (yes we did use googe.com for the example, it isn't a typo :-) )

![RedWeb-Scanner](https://user-images.githubusercontent.com/62467907/78455049-6209b300-769c-11ea-8015-9059b6865aa5.png)

## *Requirements*

You will need to have nmap installed on your system.

You will also need to install the **nmap** module for python using:

* sudo pip install python-nmap

## *Usage*

./RedWeb-Scanner.py [domain-name] or [IP address]

The script will do a reverse look-up for the IP if a domain name is provided and then run an nmap scan on the following ports:

#7  - Echo                     #143 - IMAP')                                           
#13 - Daytime                  #443 - HTTPS')
#21 - FTP                      #445 - Microsoft-ds')    
#22 - SSH                      #587 - SMTP SSL')
#23 - Telnet                   #993 - IMAP SSL')   
#25 - SMTP                     #995 - POP3 SSL')
#37 - Time                     #1723 - PPTP')
#43 - Nicname                  #2077 - WebDAV cPanel')
#53 - DNS                      #2082 - cPanel')
#70 - Gopher                   #2083 - cPanel SSL')
#79 - Finger                   #3306 - MySQL')
#80 - HTTP                     #3389 - MS WBT Server (RDP)')
#110 - POP3                    #5900 - VNC')
#111 - rpcbind                 #8008 - HTTP Alternate') 
#135 - msrpc                   #8080 - HTTP Alternate')
#139 - Netbios-ssn             #8333 - VMware Server Management & Bitcoin') 
