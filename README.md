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

(These are the most common web server ports that we come accross but you are able to add and remove as you like)

* 7  - Echo
* 13 - Daytime
* 21 - FTP
* 22 - SSH
* 23 - Telnet
* 25 - SMTP
* 37 - Time
* 43 - Nicname
* 53 - DNS
* 70 - Gopher
* 79 - Finger
* 80 - HTTP
* 110 - POP3
* 111 - rpcbind
* 135 - msrpc
* 139 - Netbios-ssn
* 143 - IMAP
* 443 - HTTPS
* 445 - Microsoft-ds
* 587 - SMTP SSL
* 993 - IMAP SSL
* 995 - POP3 SSL
* 1723 - PPTP
* 2077 - WebDAV cPanel
* 2082 - cPanel
* 2083 - cPanel SSL
* 3306 - MySQL
* 3389 - MS WBT Server (RDP)
* 5900 - VNC
* 8008 - HTTP Alternate
* 8080 - HTTP Alternate
* 8333 - VMware Server Management & Bitcoin
