'''
https://www.journaldev.com/15911/python-super
UDP: https://wiki.python.org/moin/UdpCommunication
'''
import socket

class NetConnect:
    def __init__(self,hostname,port,user1=None,user2=None):
        self.hostname = hostname
        self.port = port
        self.user1 = user1
        self.user2 = user2

    def set_hostname(self,hostname):
        self.hostname = hostname

    def set_port(self,port):
        self.port = port

    def set_message(self,message):
        self.message = bytes(message, encoding="utf-8")

    def set_user1(self,user1):
        self.user1 = user1

    def set_user2(self,user2):
        self.user2 = user2

    def get_user1(self):
        return self.user1

    def get_user2(self):
        return self.user2

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
        self.user1 = input("Player 1, enter your team name: ")
        s.send(self.user1.encode())
        self.user2 = input("Player 2, enter your team name: ")
        s.send(self.user2.encode())
        print("Get ready to ride the bull!")
        while True:
            move = input("Enter move: ")
            s.send(move.encode())
            data = s.recv(80).decode()
            print(data)
            if data == "found the secret":
                break
            print("Received:",repr(data))
        print("Connection closed.")
        s.close()

class NetServer(NetConnect):
    def __init__(self,hostname,port,user1=None,user2=None):
        super().__init__(hostname, port, user1, user2)

    def rpc(self,socket_):
        user1_pts = 0
        user2_pts = 0
        print("Waiting on players.")
        while user1_pts < 3 and user2_pts < 3:
            print('First player to 3 points wins!')
            print(f'{self.user1} : {user1_pts} points')
            print(f'{self.user2} : {user2_pts} points')
            print(f'{self.user1} YOUR UP!')
            move1 = socket_.recv(80).decode()
            next = socket_.send("next".encode())
            print(f"{self.user1} chose {move1}")
            print(f'{self.user2} YOUR UP!')
            move2 = socket_.recv(80).decode()
            print(f"{self.user1} chose {move2}")
            if move1 == 'rock' and move2 == 'paper':
                user2_pts += 1
                reply = f"Player 2 WINS! {move2} beats {move1}"
            elif move1 == 'paper' and move2 == 'scissors':
                user2_pts += 1
                reply = f"Player 2 WINS! {move2} beats {move1}"
            elif move1 == 'scissors' and move2 == 'rock':
                user2_pts += 1
                reply = f"Player 2 WINS! {move2} beats {move1}"
            elif move1 == move2:
                reply = f"TIE! No points awarded. You both chose {move1}"
            else:
                user1_pts += 1
                reply = f"Player 1 WINS! {move1} beats {move2}"
            socket_.send(reply.encode())
            if reply == 'found the secret':
                break

    def connect(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.hostname,int(self.port)))
        s.listen(1)
        socket_,address = s.accept()
        print(f"Connection establisghed from {address}")
        self.user1 = socket_.recv(80).decode()
        self.user2 = socket_.recv(80).decode()
        self.rpc(socket_)
        s.close()


def main():
    user = input("1) Player \n2) Server \nResponse:")
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

def players():
    player1 = input("Player 1, Enter your team name: ")
    player2 = input("Player 2, Enter your team name: ")
    return player1, player2

main()