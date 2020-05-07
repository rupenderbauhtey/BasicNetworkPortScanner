import sys
import socket 
from date time import datetime
#define a target 
if len(sys.argv)==2
	target = socket.gethostnamebyname(sys.argv[1]) #translate host name to ip address 
	
esle: 
	print ("invalid amount of arguments")
	print (" Syntax: pyhton3 scanner.pu <ip>")

#add a pretty banner 
print("-"*50)
print( "scanning target " + target)
print ("time started : " + str(datetime.now()))
print("-"*50)

try:
	for port in range (1,100):
		s=socket.socket(socket.AF_NET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target, port))
		if result==0:
			print("port {} is open" .format(port))
		s.close()
except KeyInterrupt:
	print("exiting program")
	s.exit()
except socket.gaierror:
	print("hostname could not be resolved")
	s.exit()
except socket.error:
	print("could not connect to server")
	s.exit()
