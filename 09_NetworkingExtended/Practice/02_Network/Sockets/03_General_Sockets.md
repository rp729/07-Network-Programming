# General socket methods
The general socket methods are as follows:

* socket.recv(bufsize): This method receives a TCP message from the socket. The bufsize argument defines the maximum data it can receive at any one time.
* socket.recvfrom(bufsize): This method receives data from the socket. The method returns a pair of values: the first value gives the received data, and the second value gives the address of the socket sending the data.
* socket.recv_into(buffer): This method receives data less than or equal to buffer. The buffer parameter is created by the bytearray() method. We will discuss it in an example later.
* socket.recvfrom_into(buffer): This method obtains data from the socket and writes it into the buffer. The return value is a pair (nbytes, address), where nbytes is the number of bytes received, and the address is the address of the socket sending the data.

```
NOTE
Be careful while using the socket.recv from_into(buffer) method in older versions of Python. Buffer overflow vulnerability has been found in this method. The name of this vulnerability is CVE-2014-1912, and its vulnerability was published on February 27, 2014. Buffer overflow in the socket.recvfrom_into function in Modules/socketmodule.c in Python 2.5 before 2.7.7, 3.x before 3.3.4, and 3.4.x before 3.4rc1 allows remote attackers to execute arbitrary code via a crafted string.

```
* socket.send(bytes): This method is used to send data to the socket. Before sending the data, ensure that the socket is connected to a remote machine. It returns the number of bytes sent.
* socket.sendto(data, address): This method is used to send data to the socket. Generally, we use this method in UDP. UDP is a connectionless protocol; therefore, the socket should not be connected to a remote machine, and the address argument specifies the address of the remote machine. The return value gives the number of bytes sent.
* socket.sendall(data): As the name implies, this method sends all data to the socket. Before sending the data, ensure that the socket is connected to a remote machine. This method ceaselessly transfers data until an error is seen. If an error is seen, an exception would rise, and socket.close() would close the socket.
Now it is time for the practical; no more mundane theory.
