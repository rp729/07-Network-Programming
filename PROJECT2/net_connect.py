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
        if message == 'exit':
            sock.close()

    def net_client(self):
        name = socket.gethostname()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        name = s.recv(80).decode()
        print(f"Connected to {name}")

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