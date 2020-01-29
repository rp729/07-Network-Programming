
#Functions required for program to function
import socket
import threading
from pathlib import Path

class NetConnect:
    def __init__(self,hostname,port):
        self.hostname = hostname
        self.port = port

    def set_hostname(self,hostname):
        self.hostname = hostname

    def set_message(self,message):
        self.message = bytes(message, encoding="utf-8")

    def get_hostname(self):
        return self.hostname

    def get_port(self):
        return self.port

    def get_message(self):
        if self.message:
            return self.message
        else:
            return

    def get_sock(self):
        return self.sock

    #Function to send message. Used by client and server
    def send_message(self,sock,message=''):
        while True:
            if message == '':
                new_message = input()
                sock.send(new_message.encode())
                print("Type message below:")
            else:
                sock.send(message.encode())
            '''if new_message == 'exit':
                break'''

    #Function to receive messages. Used by client and server
    def receive_message(self,sock):
        while True:
            message = sock.recv(1024).decode()
            print(message)
            if message == 'exit':
                break

    def receive_message_server(self,sock):
        while True:
            message = sock.recv(1024).decode()
            message2 = exec(Path(f'toolkit/{message}').read_text())
            self.send_message(message2)
            if message == 'exit':
                break

    #Client function
    def net_client(self):
        name = socket.gethostname()
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s = self.sock
        s.connect((self.hostname,int(self.port)))
        #Recieve server name
        name = s.recv(80).decode()
        print(f"Connected to {name}")
        t1 = threading.Thread(target=self.send_message,args=[s,])
        t2 = threading.Thread(target=self.receive_message,args=[s,])
        t1.start()
        t2.start()

    #Server function
    def net_server(self):
        print('Patiently waiting on client.')
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.hostname,int(self.port)))
        s.listen(1)
        socket_,address = s.accept()
        print(f'Connection established from {address}')
        #Send name to cient
        name = socket.gethostname()
        socket_.send(name.encode())
        t1 = threading.Thread(target=self.receive_message_server,args=[socket_,])
        t2 = threading.Thread(target=self.send_message,args=[socket_,])
        t1.start()
        t2.start()
