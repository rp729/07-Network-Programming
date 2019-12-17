'''
https://www.journaldev.com/15911/python-super
'''
import socket
import random

class NetConnect:
    def __init__(self,hostname,port):
        self.hostname = hostname
        self.port = port

    def set_hostname(self,hostname):
        self.hostname = hostname

    def set_port(self,port):
        self.port = port

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

class NetClient(NetConnect):
    def __init__(self,hostname,port):
        super().__init__(hostname,port)
    def send_packet(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        print("Get ready to ride the bull!")
        while True:
            guess = input("Enter number: ")
            s.send(guess.encode())
            data = s.recv(80).decode()
            print(data)
            if data == "found the secret":
                break
            print("Received:",repr(data))
        print("Connection closed.")
        s.close()

class NetServer(NetConnect):
    def __init__(self,hostname,port):
        super().__init__(hostname, port)
    def secret(self):
        secret_num = random.randint(1,10)
        print(f"The secret number is {secret_num}")
        return secret_num
    def connect(self):
        num = self.secret()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #Find difference of bind and connect
        s.bind((self.hostname,int(self.port)))
        #What does the 1 stand for?
        s.listen(1)
        socket_,address = s.accept()
        #print(socket_)
        print(f"Connection establisghed from {address}")
        while True:
            print('Dealer waits for a guess')
            guess = socket_.recv(80).decode()
            print(f"Dealer received {guess}")
            if int(guess) < num:
                reply = 'too low'
            elif int(guess) > num:
                reply = 'too high'
            else:
                reply = 'found the secret'
            socket_.send(reply.encode())
            if reply == 'found the secret':
                break
        s.close()


def main():
    print("Please choose from the following:\n"
          "1) Player\n"
          "2) Dealer")
    user = input("Response: ")
    user = input_validation(user)
    if user == 1:
        pkt = packet_build()
        client = NetClient(pkt.get_hostname(),pkt.get_port())
        client.send_packet()
    elif user == 2:
        pkt = packet_build()
        server = NetServer(pkt.get_hostname(),pkt.get_port())
        server.connect()

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