#### Lab 4A

Create a TCP chat server that connects to multiple clients using IPv4 and either Select\(\) or Threading. Then echo back data to all clients using broadcasts.

#### Lab 4B

Create an IPv6 UDP chat server using multicast to transmit to all clients.

Message strings should follow the following format:

**Username: TextGoes Here**

The receiver a should display recieved chats in the following format:

**Chatbot \(IPv6Addr\): The quick brown fox jumps over the lazy dogs**

\*\*Hints:

Ref: [http://man7.org/linux/man-pages/man7/ipv6.7.html](http://man7.org/linux/man-pages/man7/ipv6.7.html)

Using the reference set the following socket options, with a level of socket.IPPROTO\_IPV6:

**Receiver**

•Set the multicast hops to 5

**Sender**

•Set the socket's multicast group \(this is for the OS, it is \_NOT\_ IPv6 related\)

•The group is a value obtained by combining the following:

◦Packing the multicast IPv6 addr using socket.inet\_pton\(\)

◦Packing a 32 bit unsigned integer with the value 0, using struct.pack\(\)

---

socket timeouts

blocking/non-blocking

select, threading, concurrency

