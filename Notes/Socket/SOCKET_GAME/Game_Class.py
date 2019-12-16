'''
https://www.journaldev.com/15911/python-super
'''
import socket

class NetConnect:
    def __init__(self,hostname,port,message=bytes("",encoding="utf-8")):
        self.hostname = hostname
        self.port = port
        self.message = message

    def set_hostname(self,hostname):
        self.hostname = hostname

    def set_port(self,port):
        self.port = port

    def set_message(self,message):
        self.message = message

    def get_hostname(self):
        return self.hostname

    def get_port(self):
        return self.port

    def get_message(self):
        return self.message

class SendPkt(NetConnect):
    def __init__(self,hostname,port,message=None):
        super().__init__(hostname,port,message)
    def send_packet(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        s.sendall((self.message))
        s.shutdown(socket.SHUT_WR)
        while 1:
            data = s.recv(1024)
            if data == "":
                break
            print("Received:",repr(data))
            message = input("Enter message: ")
        print("Connection closed.")
        s.close()

def main():
    pkt_build = packet_build()
    packet_send = SendPkt(pkt_build.get_hostname(),pkt_build.get_port(),pkt_build.get_message())
    packet_send.send_packet()

def packet_build():
    hostname = input("Enter hostname: ")
    port = input("Enter port: ")
    message = input("Would you like to add a message? (y for yes): ")
    if message.lower() == 'y':
        message = input("Enter message: ")
        message = bytes(message,encoding='utf-8')
    else:
        message = bytes("",encoding="utf-8")
    nc = NetConnect(hostname,port,message)
    return nc


main()