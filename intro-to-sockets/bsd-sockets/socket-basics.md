# Socket Basics

* **To create a socket:**

###### _import socket _

###### _s = socket.socket\(addr\_family, type\)_

* **Address Families:**

###### _socket.AF\_INET      Internet protocol \(IPv4\) _

###### _socket.AF\_INET6     Internet protocol \(IPv6\) _

* **Socket Types:**

###### _socket.SOCK\_STREAM  Connection based stream \(TCP\) _

###### _socket.SOCK\_DGRAM   Datagrams \(UDP\)_

#### Creating a socket is only the ﬁrst step

###### _s = socket\(AF\_INET, SOCK\_STREAM\) _

**Further use depends on application **

* **Server **- Listen for incoming connections 
* **Client **- Make an outgoing connection



