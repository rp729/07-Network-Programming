from ascratch_fullduplex import *

if __name__ == '__main__':
    localhost = 'localhost'
    port = input("Enter port :")
    pkt = NetConnect(localhost, port)
    pkt.net_server()