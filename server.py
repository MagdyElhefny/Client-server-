from socket import *
import threading

def server() :
    server =socket(AF_INET , SOCK_STREAM)

    host = "127.0.0.1"
    port = 7002

    server.bind((host,port))
    server.listen(5)
    print("Socket is listening")
    client =server.accept()
    print("Connected to client")
    while True :  
            x=client.recv(2048)
            print("client : ",x.decode('utf-8'))  
            y=input(" server : ")
            client.send(y.encode('utf-8'))
            if y.upper() == "END":
                break
            
        
    client.close()

t1=threading.Thread(target=server ,args=())
t1.start()
t1.join() 


  