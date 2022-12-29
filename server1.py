import socket       
from threading import *

# Socket oluşturulması
s = socket.socket()          
 
# Bağlanılacak adres ve port
host = "127.0.0.1"
port = 12345        

s.connect((host,port))

while True:

    clientMessage = input("Mesaj :")
    
    s.send(clientMessage.encode('utf8'))
    
    



    def recvMessage():
        while True:
            serverMessage = s.recv(1024).decode('utf8')
            print(serverMessage)




    recThread = Thread(target=recvMessage)
    recThread.daemon=True
    recThread.start()
