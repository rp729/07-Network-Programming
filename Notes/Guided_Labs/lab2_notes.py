#!/usr/bin/env python

#This program is optimized for Python 2.7.12 and 3.5.2

import socket

def get_remote_machine_info():
    remote_host = 'duckssss'
    try:
        print("IP address of %s: %s"%(remote_host,
            socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print("%s:%s"%(remote_host,err_msg))

if __name__ == '__main__':
    get_remote_machine_info()
