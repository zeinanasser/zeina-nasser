import sys
import time
import uuid#for macaddress
import socket #for my sockets(proxy,client,server)
               
HOST2='127.0.0.1'
PORT2=8888 #same as the port number of the proxy server that it is going to send the message to
ipaddress=input("please enter the ip address you want to access")

CLIENTSOC=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
CLIENTSOC.connect((HOST2,PORT2)) 

initialtime=time.time() #this corresponds to the time this link was sent to the proxy server
CLIENTSOC.sendall(ipaddress.encode())
    #now see the time the file was received by the proxy
DESTINATIONRESOPNSE=CLIENTSOC.recv(1024)
finaltime=time.time() #this is how we find the time (I doubled check on google if this is the syntax to find instant time)
RTT=finaltime-initialtime
print("round trip time is",RTT)
    
print ("The MAC address in formatted way is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
 # I got this from google because I don't know how to find mac address as a syntax :(
       
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:                                           ###this is from google I couldn't find anything else I know !!!!!! 
    print ("Strange error creating socket")
    sys.exit(1)
