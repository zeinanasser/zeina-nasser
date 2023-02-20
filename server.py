import sys
import time#for roundtrip time
import socket #for my sockets(proxy,client,server)
HOST="" #empty string
PORT=8888#Accprding to google: "The default is 8080. Other common port numbers for HTTP proxies are 8888 and 8000.(I tried 8080 but it showed an error i dont know why ":))
#now let's create a function for the proxy server which acts like a bridge 
#between the client server and destination server
    #from google & from the slides given in class: "AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP"
PROXYSERVERSOCKET= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
PROXYSERVERSOCKET.bind((HOST,PORT))
PROXYSERVERSOCKET.listen()
print("proxy server can now listen to port")
        #while loop to keep on accepting connections 
while True:
    CLIENTSOC,CLIENTADD=PROXYSERVERSOCKET.accept()
    print("proxy server can now accept and receive from client")
         #now I need to know what is the client requesting    
    with CLIENTSOC:
            requestedmessage=CLIENTSOC.recv(1024).decode()  #from the slides in class but instead of naming it sentence i named it requested msg
            print("this is the requested message :)")
            #send the message from proxy to destination server, to do so I have to create a server socket with a host of
            #ip address(extracted from the client's requested message)
            IPaddress=requestedmessage
            requeststring=f"GEt / HTTP/1.1\r\nHost:{IPaddress}\r\n\r\n"
            print(time.time())
            try:
               
            
                DESTINATIONSERVER=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                DESTINATIONSERVER.connect((IPaddress,80))
                DESTINATIONSERVER.sendall(requeststring.encode()) #from the slides+ the help of google : I was confused whether to write send all or send)
                print("requested message was sent to this ip address", IPaddress)
                    #the destination server received the encoded message so it will return its result/respone back to the proxy server
                DESTINATIONRESOPNSE=DESTINATIONSERVER.recv(1024)
                    #now the proxy will forward this message back to the client
                print("The response is ",DESTINATIONRESOPNSE)
                CLIENTSOC.sendall(DESTINATIONRESOPNSE) #from the slides+ the help of google(I was confused whether to write send all or send)
                print("response was sent to the client")
                print(time.time())   
                print("now closed")
                DESTINATIONSERVER.close()
            except socket.error:   ##from google
                print("there's error ")
                error='HTTP/1.0 500 Internet server Error\n\n'.encode()
                CLIENTSOC.send(error)
            CLIENTSOC.close()
            
