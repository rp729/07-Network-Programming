'''
3) Write a client server python program to send input from client to server, replace all the vowels with '#' and return
the string to client and print it
'''
import socket

#Class to create server and client connection
class NetConnect:
    #Default init function
    def __init__(self,hostname,port):
        self.hostname = hostname
        self.port = port

    def set_hostname(self,hostname):
        self.hostname = hostname

    def set_message(self,message):
        self.message = bytes(message, encoding="utf-8")

    def get_hostname(self):
        return self.hostname

    def get_port(self):
        return self.port

    #If message doesn't exist nothing will be returned
    def get_message(self):
        if self.message:
            return self.message
        else:
            return

    #Function to connect client
    def net_client(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.hostname,int(self.port)))
        # Receive the name of the server
        name = s.recv(80).decode()
        while True:
            # Create message
            self.set_message(input(f"Client@{name}: Enter message (type 'exit' to quit): "))
            # Send message to server
            s.send(self.get_message())
            # Recieve response from server
            data = s.recv(1056).decode()
            print(f'Server response: {data}')
            if data == 'exit':
                break
        s.close()
    def net_server(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.hostname,int(self.port)))
        print("Waiting on client...")
        s.listen(1)
        socket_,address = s.accept()
        print(f'Connection established from {address}')
        name = socket.gethostname()
        # Send server name to client
        socket_.send(name.encode())
        while True:
            message = socket_.recv(1056).decode()
            #Break connection if exit message is sent from client
            if message == 'exit':
                socket_.send('exit'.encode())
                break
            else:
                #List of vowels
                vowels = 'AEIOUaeiou'
                print(f"Message received: {message}")
                message = list(message)
                #Loop to covert vowels to #
                for i in message:
                    if i in vowels:
                        message[message.index(i)] = '#'
                message = ''.join(message)
                print(f"Results: {message}\nSending results to client...")
                #Send the new message back to the client
                socket_.send(message.encode())
        s.close()


#Main function
def main():
    user = input("1) Client \n2) Server \nResponse:")
    user = input_validation(user)
    if user == 1:
        pkt = packet_build()
        pkt.net_client()
    elif user == 2:
        pkt = packet_build()
        pkt.net_server()

#Create client or server
def packet_build():
    hostname = input("Enter hostname (default: localhost): ")
    if hostname == '':
        hostname = 'localhost'
    port = input("Enter port: ")
    nc = NetConnect(hostname,port)
    return nc

#Simple input validation for choosing either server or client
def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("ERROR! Enter a number: ")
    while int(num) != 1 and int(num) != 2:
        num = input("ERROR! Enter either 1 or 2: ")
        while str.isnumeric(num) == False:
            num = input("ERROR! Enter a number: ")
        num = int(num)
    return int(num)

main()