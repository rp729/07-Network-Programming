'''
https://www.journaldev.com/15911/python-super
'''
import socket
import threading

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

    def send_(self,s):
        while True:
            message = input("Enter message:")
            s.send(message.encode())

    def receive_(self,s):
        while True:
            message = s.recv(1024).decode()
            print(message)

    def net_client(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        name = s.recv(80).decode()
        t1 = threading.Thread(target=self.send_(s),name=1)
        t2 = threading.Thread(target=self.receive_(s),name=2)
        t1.start()
        t2.start()
        s.close()
    def net_server(self):
        print('Patiently waiting on client.')
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.hostname,int(self.port)))
        s.listen(1)
        socket_,address = s.accept()
        print(f'Connection established from {address}')
        name = socket.gethostname()
        socket_.send(name.encode())
        t1 = threading.Thread(target=self.send_(socket_),name=1)
        t2 = threading.Thread(target=self.receive_(socket_),name=2)
        t1.start()
        t2.start()
        s.close()



def main():
    user = input("1) Client \n2) Server \nResponse:")
    user = input_validation(user)
    if user == 1:
        pkt = packet_build()
        pkt.net_client()
    elif user == 2:
        pkt = packet_build()
        pkt.net_server()

def packet_build():
    hostname = input("Enter hostname: ")
    port = input("Enter port: ")
    nc = NetConnect(hostname,port)
    return nc

def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("ERROR! Enter a number: ")
    return int(num)


main()