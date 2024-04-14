from socket import *
import threading
server =socket(AF_INET , SOCK_STREAM)

host = "127.0.0.1"
port = 7002

def server_s ():
    

    server.bind((host,port))
    server.listen(5)
    print("Socket is listening")
    client , addres =server.accept()
    print("Connected to client")
    while True:
        x=client.recv(2048)
        print("client : ",x.decode('utf-8'))
        y=input(" server : ")
        client.send(y.encode('utf-8'))
        
        if y.upper() == "END":
            break

    client.close()



def client():
    client=socket(AF_INET , SOCK_STREAM)
    
    client.connect((host , port ))
    print("Connected to server ")

    while True:
        y=input("client : ")
        client.send(y.encode('utf-8'))
        x=client.recv(2048) 
        print("server : ",x.decode('utf-8'))
        if y.upper() == "END":
            break
    
    client.close()   

t1=threading.Thread(target=server_s ,args=())
t2=threading.Thread(target=client , args=())


t1.start()
t2.start()

t1.join()
t2.join()


