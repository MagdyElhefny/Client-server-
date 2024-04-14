from socket import *
import threading

def client () :
    client=socket(AF_INET , SOCK_STREAM)

    host = "127.0.0.1"
    port = 7002
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



t2=threading.Thread(target=client ,args=())
t2.start()
t2.join() 

