from netconnect import *
if __name__ == '__main__':
    host = 'localhost'
    port = input(("Enter port :"))
    connect = NetConnect(host, port)
    connect.server()