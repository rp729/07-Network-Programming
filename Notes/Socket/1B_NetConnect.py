import socket

host='::1'

mysock=socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
addr=(host,5555)
mysock.connect(addr)

try:
    msg=b"hi, this is a test\n"
    mysock.sendall(msg)
except:
    print("Socket error ",e)
finally:
    mysock.close()