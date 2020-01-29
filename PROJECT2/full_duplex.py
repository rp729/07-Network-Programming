'''
https://www.journaldev.com/15911/python-super
'''

#Functions required for program to function
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

    #Function to send message. Used by client and server
    def send_message(self,sock):
        while True:
            new_message = input()
            sock.send(new_message.encode())
            print("Type message below:")
            if new_message == 'exit':
                break

    #Function to receive messages. Used by client and server
    def receive_message(self,sock):
        while True:
            message = sock.recv(1024).decode()
            print(f"User response ==>:{message}")
            if message == 'exit':
                break

    #Client function
    def net_client(self):
        name = socket.gethostname()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        #Recieve server name
        name = s.recv(80).decode()
        print("Begin typing message to start conversation.")
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
        print("Begin typing message to start conversation.")
        t1 = threading.Thread(target=self.receive_message,args=[socket_,])
        t2 = threading.Thread(target=self.send_message,args=[socket_,])
        t1.start()
        t2.start()


#Main function
def main():
    user = input("1) Client \n2) Server \nResponse:")
    user = input_validation(user)
    if user == 1:
        pkt = packet_build()
        pkt.net_client()
    elif user == 2:
        pkt = packet_build()
        pkt.net_server()

#Build the socket connection endpoints
def packet_build():
    hostname = input("Enter hostname: ")
    port = input("Enter port: ")
    nc = NetConnect(hostname,port)
    return nc

#Simple input validation
def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("ERROR! Enter a number: ")
    return int(num)


main()