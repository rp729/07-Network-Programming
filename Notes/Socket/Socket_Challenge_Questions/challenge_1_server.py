#07-Network-Programming/09_NetworkingExtended/02_Network/Guided_labs/06_Network_programming.md

#!/usr/bin/env python

# This program is optimized for Python 2.7.12
# It may run on any other version with/without

import socket
import sys
import argparse

def get_host():
    host = input("Enter host (default = localhost): ")
    if host == '':
        return 'localhost'
    else:
        return host

data_payload = 2048
backlog = 5


def echo_server(port):
    host = get_host()
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument
    sock.listen(backlog)
    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print("Data: %s" % data)
            client.send(data)
            print("sent %s bytes back to % s" % (data, address))
            # end connection
            client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port',action="store", dest="port", type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
