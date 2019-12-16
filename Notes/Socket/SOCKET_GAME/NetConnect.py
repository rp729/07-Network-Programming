import socket
import random

host='localhost'

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=(host,5555)
mysock.connect(addr)
randnum = str(random.randint(1,100))

try:
    msg=bytes(randnum, encoding='utf-8')
    mysock.sendall(msg)
except:
    print("Socket error ")
'''finally:
    mysock.close()'''