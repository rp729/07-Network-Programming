import socket

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
    def send_message(self,sock):
        print()
        new_message = input("Enter message: ")
        sock.send(new_message.encode())
        print("Waiting on response...")

    def receive_message(self,sock):
        print()
        message = sock.recv(1024).decode()
        print(f"=>:{message}")

    def net_client(self):
        name = socket.gethostname()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        name = s.recv(80).decode()
        print("Avaliable services:")
        while True:
            self.send_message(s)
            rec = self.receive_message(s)
            if rec == "exit":
                break
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
        while True:
            rec = self.receive_message(socket_)
            if rec == 'exit':
                break
            self.send_message(socket_)
        socket_.close()



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