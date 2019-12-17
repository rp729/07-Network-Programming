#!/usr/bin/env python

import socket

send_buff = 4096
recv_buff = 4096

def modify_buff_size():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #Get the size fo the socket's send buffer
    buff_size = s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print("Buffer size [Before]:%d"%buff_size)

    s.setsockopt(socket.SOL_TCP,
                 socket.TCP_NODELAY,1)

    s.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_SNDBUF,
            send_buff)
    s.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_RCVBUF,
            recv_buff)
    buff_size = s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print("Buffer size [After]:%d" %buff_size)

if __name__ == '__main__':
    modify_buff_size()
