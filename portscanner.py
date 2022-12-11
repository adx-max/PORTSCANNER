#!/bin/python3

#learnt this trick from the CyberMentor from TCM security, i just added  my own touches, hope you like it.

import pyfiglet
ascii_banner =pyfiglet.figlet_format("BenTech Security")
print(ascii_banner)
import sys
import socket
from datetime import datetime

#Define our target 
if len(sys.argv) ==2:
		target = socket.gethostbyname(sys.argv[1]) #Transate hostname to IPv4
else:
		print("Invalid amount of arguments.")
		print("Syntax: Python3 scanner.py <ip>")
		

print("MODE BY BigBen Bentech Security ")
print ('-----BenTech Security--------')
print ("Scanning target: "+target)
print("Time Started: "+str(datetime.now()))
print ('-' * 50)

try:
	for port in range(20,50): #changethis example (1, 65500) if you want to scan the port 1 upto 65500
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(2)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nBenTech Security Exiting Program.")
	sys.exit()
	
	
except socket.gaierror:
		Print("Hostname could not be resolved, try again")
		sys.exit()
		
except socket.error:
		print("could not connect to server")
		sys.exit()
		
print("Scanning finished, exiting now, Thank You for using my python")
