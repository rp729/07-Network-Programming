
# The socket module
Types and functions needed to work with sockets can be found in Python in the socket module. The socket module exposes all of the necessary pieces to quickly write TCP and UDP clients and servers. The socket module has almost everything you need to build a socket server or client. In the case of Python, the socket returns an object to which the socket methods can be applied.

This module comes installed by default when you install the Python distribution.

To check it, we can do so from the Python interpreter:

![image](https://user-images.githubusercontent.com/47218880/68703419-3d2b6c80-0550-11ea-8325-a055324c8c9b.png)

In this screenshot, we see all the constants and methods that we have available in this module. The constants we see in the first instance within the structure that has returned the object. Among the most-used constants, we can highlight the following:
```
socket.AF_INET
socket.SOCK_STREAM
```
A typical call to build a socket that works at the TCP level is:
```
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```

# Socket methods
These are the general socket methods we can use in both clients and servers:
```
socket.recv(buflen): This method receives data from the socket. The method argument indicates the maximum amount of data it can receive.
socket.recvfrom(buflen): This method receives data and the sender's address.
socket.recv_into(buffer): This method receives data into a buffer.
socket.recvfrom_into(buffer): This method receives data into a buffer.
socket.send(bytes): This method sends bytes data to the specified target.
socket.sendto(data, address): This method sends data to a given address.
socket.sendall(data): This method sends all the data in the buffer to the socket.
socket.close(): This method releases the memory and finishes the connection.

```
## Server socket methods
In a client-server architecture, there is a central server that provides services to a set of machines that connect. These are the main methods we can use from the point of view of the server:
```
socket.bind(address): This method allows us to connect the address with the socket, with the requirement that the socket must be open before establishing the connection with the address
socket.listen(count): This method accepts as a parameter the maximum number of connections from clients and starts the TCP listener for incoming connections
socket.accept(): This method allows us to accept connections from the client. This method returns two values: client_socket and client address. client_socket is a new socket object used to send and receive data. Before using this method, you must call the socket.bind(address) and socket.listen(q) methods
```
# Client socket methods
This is the socket method we can use in our socket client for connecting with the server:

socket.connect(ip_address): This method connects the client to the server IP address
We can obtain more information about this method with the help(socket) command. We learn that this method does the same as the connect_ex method and also offers the possibility of returning an error in the event of not being able to connect with that address.

We can obtain more information about these methods with the help(socket) command:

![image](https://user-images.githubusercontent.com/47218880/68703547-867bbc00-0550-11ea-9603-deb2a726e60f.png)

##  Basic client with the socket module
In this example, we are testing how to send and receive data from a website.Once the connection is established, we can send and receive data. Communication with the socket can be done very easily thanks to two functions, send () and recv (), used for TCP communications. For UDP communication, we use sendto (), and recvfrom ()

In this socket_data.py script, we create a socket object with the AF_INET and SOCK_STREAM parameters. We then connect the client to the remote host and send it some data. The last step is to receive some data back and print out the response. We use an infinite loop (while True) and we check whether the data variable is empty. If this condition occurs, we finish the loop.

You can find the following code in the socket_data.py file:
```python
import socket
print 'creating socket ...'
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'
print "connection with remote host"
s.connect(('www.google.com',80))
print 'connection ok'
s.send( 'GET /index.html HTML/1.1\r\n\r\n')
while 1:
   data=s.recv(128)
    print data
    if data== "":
        break
print 'closing the socket'
s.close()
```























