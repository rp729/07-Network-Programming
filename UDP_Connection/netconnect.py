import socket
from pathlib import Path
import sys
from subprocess import call
import time


class NetConnect:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def set_hostname(self, hostname):
        self.hostname = hostname

    def set_message(self, message):
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

    def send_message(self,sock,message,ip,port):
        sock.sendto(message,(ip,port))

    def rec_message(self,sock):
        data, addr = sock.recvfrom(1024)
        return data, addr

    def client(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = "Connection Established".encode()
        name = self.hostname
        port = int(self.port)
        self.send_message(sock,message,name,port)

    def client_server(self,target=True):
        name = '127.0.0.1'
        port = int(self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((name, int(f'{port}1')))
        while target == True:
            data, addr = sock.recvfrom(1024)
            print(data.decode())
            time.sleep(0.2)
            target = False

    def server(self):
        name = self.hostname
        port = int(self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((name,port))
        while True:
            data, addr = sock.recvfrom(1024)
            if '.py' in data.decode() or '.c' in data.decode():
                file = open('text.txt', 'w')
                orig_stdout = sys.stdout
                sys.stdout = file
                call(["python3", f'toolkit/{data.decode()}'])
                sys.stdout = orig_stdout
                file.close()
                file = open('text.txt')
                print(file.read())
                file_read = file.read().encode()
                name = addr[0]
                port = int(f'{self.get_port()}1')
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.send_message(sock, file_read, name, port)
                name = addr[0]
                port = int(f'{self.get_port()}1')
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.send_message(sock, 'Ack'.encode(), name, port)
                print("STILL GOOD!")
            else:
                print(data.decode())
                self.send_message(sock,data,addr[0],int(f'{port}1'))

