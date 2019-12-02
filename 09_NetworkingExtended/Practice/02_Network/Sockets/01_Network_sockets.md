Network sockets
A network socket address contains an IP address and port number. In a very simple way, a socket is a way to talk to other computers. By means of a socket, a process can communicate with another process over the network.

In order to create a socket, use the socket.socket() function that is available in the socket module. The general syntax of a socket function is as follows:
```python
s = socket.socket (socket_family, socket_type, protocol=0)
```
Here is the description of the parameters:
```
socket_family: socket.AF_INET, PF_PACKET
```
AF_INET is the address family for IPv4. PF_PACKET operates at the device driver layer. The pcap library for Linux uses PF_PACKET. You will see more details on PF_PACKET in Chapter 3, Sniffing and Penetration Testing. These arguments represent the address families and the protocol of the transport layer:
```
Socket_type : socket.SOCK_DGRAM, socket.SOCK_RAW,socket.SOCK_STREAM
```
The socket.SOCK_DGRAM argument depicts that UDP is unreliable and connectionless, and socket.SOCK_STREAM depicts that TCP is reliable and is a two-way, connection-based service. We will discuss socket.SOCK_RAW in Chapter 3, Sniffing and Penetration Testing.
```
protocol
```
Generally, we leave this argument; it takes 0 if not specified.
