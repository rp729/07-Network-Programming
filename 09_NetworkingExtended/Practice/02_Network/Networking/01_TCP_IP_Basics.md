# An introduction to TCP/IP networking
This section offers an introduction to essential networking concepts, with a strong focus on the TCP/IP stack.

The following discussion is based on Internet Protocol version 4 (IPv4). Since the internet has run out of IPv4 addresses, a new version, IPv6, has been developed, which is intended to resolve this situation. However, although IPv6 is being used in a few areas, its deployment is progressing slowly and the majority of the internet will likely be using IPv4 for a while longer. We'll focus on IPv4 in this section, and then we will discuss the relevant changes in the IPv6 later. 

## Introduction to TCP/IP
TCP/IP is a set of protocols that were designed to work together to provide an end-to-end transmission of messages across interconnected networks. TCP provides transparent data transfers between end systems using the services of the lower network layer to move the packets between the two communicating systems. TCP is a protocol that works at the transport layer, while IP works at the network layer.

TCP is responsible for creating connections through a data flow. This process guarantees that the data is delivered to the destination without errors and in the same order in which they came out. It is also used to distinguish different applications in the same device.

IP is responsible for sending and receiving data in blocks. The shipment always does this to find the best route, but without guaranteeing that it reaches the destination.

Both protocols are used to solve the transmission of data that is generated in a network, either internally or externally. The union of these protocols is done to ensure that the information always arrives on the best route and in the correct way to the destination.

## The protocol stack, layer by layer
A protocol stack is organized in such a way that the highest level of communication resides in the top layer. Each layer in the stack is built on the services of the immediate lower layer.

The TCP/IP protocol stack has four layers, as follows:

Application layer: This layer manages the high-level protocols, including representation, coding, and dialogue control issues. It handles everything related to applications, and the data is packed appropriately for the next layer. It is a user process that cooperates with other processes on the same host or a different one. Examples of protocols at this layer are TELNET, File Transfer Protocol (FTP), and Simple Mail Transfer Protocol (SMTP).
Transport layer: This layer handles quality of service, reliability, flow control, and error correction. One of its protocols is the TCP, which provides reliable network communications that are oriented to the connection, unlike UDP, which is not connection oriented. It also provides data transfer. Example protocols include TCP (connection oriented) and UDP (non-connection oriented).
Network layer: The purpose of the internet layer is to send packets from the source of any network and make them reach their destination, regardless of the route they take to get there.
Network access layer: This is also called a host-to-host network layer. It includes the LAN and WAN protocols, and the details in the physical and data link layers of the OSI model. Also known as the link layer or data link layer, the network interface layer is the interface to the current network hardware.
The following diagram represents the TCP/IP protocol stack:

![image](https://user-images.githubusercontent.com/47218880/68701765-1a4b8900-054d-11ea-9a5e-34170b259435.png)

The IP is the most important protocol of the network layer. It is a non-connection oriented protocol that does not assume reliability of the lower layers. IP does not provide reliability, flow control, or error recovery. These functions must be provided by the upper level, in the transport layer with TCP as the transport protocol, or in the application layer if UDP is being used as the transport protocol. The message unit in an IP network is called an IP datagram. This is the basic unit of information that is transmitted from one side of the TCP/IP network to the other.

The application layer is where all of the user interaction with the computer and services occurs. As an example of this, any browser can work, even without the TCP/IP stack installed. Usually, we use browsers such as Google Chrome, Mozilla, Firefox, Internet Explorer, and Opera for communicating with this layer.

When initiating a query for a remote document, the HTTP protocol is used. Each time we request a communication of this type, the browser interacts with the application layer, which, in turn, serves as an interface between the user's applications and the protocol stack, which will provide communication with the help of the lower layers.

The responsibilities of the application layer are to identify and establish the communication availability of the target destination, as well as to determine the resources for that communication to exist. Some of the protocols of the application layer are as follows:
```
FTP
HTTP
Post Office Protocol version 3 (POP3)
Internet Message Access Protocol (IMAP)
SMTP
Simple Network Management Protocol (SNMP)
TELNET—TCP/IP Terminal Emulation Protocol
```

##  UDP
UDP is a non-connection oriented protocol. That is, when machine A sends packets to machine B, the flow is unidirectional. The data transfer is made without warning the recipient of machine B, and the recipient receives the data without sending a confirmation to the sender of machine A.

This is because the data that's sent by the UDP protocol does not allow you to transmit information related to the sender. Therefore, the recipient will not know about the sender's data, except their IP address. Let's have a look at some properties of the UDP protocols:

Unreliable: In UDP, there is no concept of packet retransmission. Therefore, when a UDP packet is sent, it is not possible to know whether the packet has reached its destination since there are no errors in the correction mechanism.
Not ordered: The order in which packages are sent and received cannot be determined.
Datagrams: The integrity of packet delivery is done individually and can only be checked to ensure that the packages arrived correctly.
Lightweight and speed: The UDP protocol does not provide error recovery services, so it offers a direct way to send and receive datagrams through an IP network. It is used when speed is an important factor in the transmission of information, for example, when streaming audio or video.

## TCP
The TCP protocol, unlike the UDP protocol, is connection oriented. When machine A sends data to machine B, machine B is informed of the arrival of this data and confirms its good reception.

Here, the CRC control of data intervenes, which is based on a mathematical equation that allows you to verify the integrity of the transmitted data. In this way, if the received data is corrupted, the TCP protocol allows the recipients to request the sender to send them again.

This protocol is one of the main protocols of the transport layer of the TCP/IP model, since, at the application level, it makes it possible to manage data coming from the lowest level of the model.

So, when data is provided to the IP protocol, it binds it in IP datagrams, fixing the field protocol with 6, so that you know in advance that the protocol is TCP. This protocol is connection oriented, so it allows two machines that are communicated to control the status of the transmission.

Several programs within a data network that are composed of computers can use TCP to create connections between them, by means of which they can send a data flow. Thus, the protocol guarantees that the data will be delivered to its destination. The most important thing to take into account is that it has no errors and maintains the order in which they are transmitted.

On the basis of the preceding example, we can devise the properties of TCP:

Reliable: The TCP protocol has the ability to manage the attempts that can be made to send a message if a packet is lost, and can resend those fragments that were not sent on the first attempt.
Ordered: The messages are delivered in a particular order.
Heavyweight: TCP has the ability to verify that the connection can be established through a socket before any packet can be sent, for which it uses three sending confirmation packets, called SYN, SYN-ACK, and ACK.

##  Protocol concepts and the problems that protocols solve
This section explains concepts regarding IP addresses and ports, network interfaces in a local machine, and other concepts related to protocols, such as Dynamic Host Configuration Protocol (DHCP) and DNS.

##IP addresses and ports
IP addresses are addresses that help to uniquely identify a device over the internet. A port is an endpoint for communication in an operating system.

When you connect to the internet, your device is assigned a public IP address, and each website you visit also has a public IP address. So far, we have used IPv4 as an addressing system. The main problem with this is that the internet is running out of IPv4 public address space and so it is necessary to introduce IPv6, which provides a larger address space. 

The following are the addresses for total IPv4 and IPv6 space:
```
Total IPv4 space: 4, 294, 967, 296 addresses
Total IPv6 space: 340, 282, 366, 920, 938, 463, 463, 374, 607, 431, 768, 211, 456 addresses
```
The ports are numerical values (between 0 and 65, 535) that are used to identify the processes that are being communicated. At each end, each process that intervenes in the communication process uses a single port to send and receive data.

In conjunction with this, two pairs of ports and IP addresses, you can identify two processes in a TCP/IP network. A system might be running thousands of services, but to uniquely identify a service on a system, the application requires a port number.

Port numbers are sometimes seen on the web or other URLs as well. By default, HTTP uses port 80, and HTTPS uses port 443, but a URL like http://www.domain.com:8080/path/ specifies that the web browser, instead of using default port 80, is connecting to port 8080 of the HTTP server.

### Some common ports are as follows:
```
22: Secure Shell (SSH)
23: Telnet remote login service
25: SMTP
53: Domain Name System (DNS) service
80: HTTP
```
Regarding IP addresses, we can differentiate two types, depending on whether they are for a public or private rank for the internal network of an organization:

* Private IP address: Ranges from 192.168.0.0 to 192.168.255.255, 172.16.0.0 to 172.31.255.255, or 10.0.0.0 to 10.255.255.255
* Public IP address: A public IP address is an IP address that your home or business router receives from your Internet Service Provider (ISP)




