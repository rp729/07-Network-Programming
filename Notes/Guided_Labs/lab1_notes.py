import socket

host_name = socket.gethostname()
print(host_name)

print(socket.gethostbyname(host_name))


#Another way to get machine info:

'''
import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" %host_name)
    print("IP address: %s" %ip_address)

if __name__ == '__main__':
    print_machine_info()
'''
