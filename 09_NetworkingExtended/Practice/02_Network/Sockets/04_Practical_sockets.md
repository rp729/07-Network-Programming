## Moving on to the practical
First, we will make a server-side program that offers a connection to the client and sends a message to the client. Run server1.py:
```python
import socket
host = "192.168.0.1" #Server address
port = 12345  #Port of Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind server 
s.listen(2) 
conn, addr = s.accept()  
print addr, "Now Connected"
conn.send("Thank you for connecting")
conn.close()
```
The preceding code is very simple; it is minimal code on the server side.

First, import the socket module and define the host and port number: 192.168.0.1 is the server's IP address. Socket.AF_INET defines the IPv4 protocol's family. Socket.SOCK_STREAM defines the TCP connection. The s.bind((host,port)) statement takes only one argument. It binds the socket to the host and port number. The s.listen(2) statement listens to the connection and waits for the client. The conn, addr = s.accept() statement returns two values: conn and addr. The conn socket is the client socket, as we discussed earlier. The conn.send() function sends the message to the client. Finally, conn.close() closes the socket. From the following examples and screenshot, you will understand conn better.

This is the output of the server1.py program:
```
G:\Python\Networking>python server1.py
```
Now, the server is in the listening mode and is waiting for the client:

Let's see the client-side code. Run client1.py:
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.1"  # server address
port =12345  #server port 
s.connect((host,port)) 
print s.recv(1024)
s.send("Hello Server")
s.close()
```
In the preceding code, two methods are new: s.connect((host,port)), which connects the client to the server, and s.recv(1024), which receives the strings sent by the server.

The output of client.py and the response of the server is shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68699423-a7d8aa00-0548-11ea-9451-e30cdcc0dcad.png)

The preceding screenshot of the output shows that the server accepted the connection from 192.168.0.11. Don't get confused by seeing the port 1789; it is the random port of the client. When the server sends a message to the client, it uses the conn socket, as mentioned earlier, and this conn socket contains the client IP address and port number.

The following diagram shows how the client accepts a connection from the server. The server is in the listening mode, and the client connects to the server. When you run the server and client program again, the random port gets changed. For the client, the server port 12345 is the destination port, and for the server, the client random port 1789 is the destination port.

![image](https://user-images.githubusercontent.com/47218880/68699455-b7f08980-0548-11ea-8cfe-669e1186f2af.png)

You can extend the functionality of the server using the while loop, as shown in the following program. Run the server2.py program:
```python
import socket 
host = "192.168.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
while True:
  conn, addr = s.accept()
  print addr, "Now Connected"
  conn.send("Thank you for connecting")
  conn.close()
```
The preceding code is the same as the previous one, just the infinite while loop is added.

Run the server2.py program, and from the client, run client1.py.

The output of server2.py is shown here:

![image](https://user-images.githubusercontent.com/47218880/68699501-ce96e080-0548-11ea-87ac-e102814fc6c1.png)


One server can give service to many clients. The while loop keeps the server program alive and does not allow the code to end. You can set a connection limit to the while loop; for example, set while i>10 and increment i with each connection.

Before proceeding to the next example, the concept of bytearray should be understood. The bytearray array is a mutable sequence of unsigned integers in the range of 0 to 255. You can delete, insert, or replace arbitrary values or slices. The bytearray array's objects can be created by calling the built-in bytearray array.

The general syntax of bytearray is as follows:
```python
bytearray([source[, encoding[, errors]]])
```
Let's illustrate this2 with an example:
```python
>>> m = bytearray("Mohit Mohit")
>>> m[1]
111
>>> m[0]
77
>>> m[:5]= "Hello"
>>> m
bytearray(b'Hello Mohit')
>>>
```
This is an example of the slicing of bytearray.

Now, let's look at the splitting operation on bytearray():
```python
>>> m = bytearray("Hello Extra")
>>> m
bytearray(b'Hello Extra')
>>> m.split()
[bytearray(b'Hello'), bytearray(b'Extra')]
```
The following is the append operation on bytearray():
```python
>>> m.append(33)
>>> m
bytearray(b'Hello Extra!')
>>> bytearray(b'Hello World!')
```
The next example is of s.recv_into(buff). In this example, we will use bytearray() to create a buffer to store data.

First, run the server-side code. Run server3.py:
```python
import socket
host = "192.168.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print "connected by", addr
conn.send("Thanks")
conn.close()
```
The preceding program is the same as the previous one. In this program, the server sends Thanks, six characters.

Let's run the client-side program. Run client3.py:
```python
import socket
host = "192.168.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
buf = bytearray("-" * 30) # buffer created
print "Number of Bytes ",s.recv_into(buf) 
print buf
s.close
```
In the preceding program, a buf parameter is created using bytearray(). The s.recv_into(buf) statement gives us the number of bytes received. The buf parameter gives us the string received.

The output of client3.py and server3.py is shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68699734-482ece80-0549-11ea-8182-833eaa8e5f7f.png)

Our client program successfully received 6 bytes of string, Thanks. Now, you must have got an idea of bytearray(). I hope you will remember it.

This time I will create a UDP socket.

Run udp1.py, and we will discuss the code line by line:
```python
import socket
host = "192.168.0.1"
port = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
data, addr = s.recvfrom(1024)
print "received from ",addr
print "obtained ", data
s.close()
```
socket.SOCK_DGRAM creates a UDP socket, and data, addr = s.recvfrom(1024) returns two things: first is the data and second is the address of the source.

Now, see the client-side preparations. Run udp2.py:
```python
import socket
host = "192.168.0.1"
port = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print s.sendto("hello all",(host,port))
s.close()
```
Here, I used the UDP socket and the s.sendto() method, as you can see in the definition of socket.sendto(). You know very well that UDP is a connectionless protocol, so there is no need to establish a connection here.

The following screenshot shows the output of udp1.py (the UDP server) and udp2.py (the UDP client):

![image](https://user-images.githubusercontent.com/47218880/68699830-72808c00-0549-11ea-904c-875502e2ef6a.png)

The server program successfully received data.

Let us assume that a server is running and there is no client start connection, and that the server will have been listening. So, to avoid this situation, use socket.settimeout(value).

Generally, we give a value as an integer; if I give 5 as the value, it would mean wait for 5 seconds. If the operation doesn't complete within 5 seconds, then a timeout exception would be raised. You can also provide a non-negative float value.

For example, let's look at the following code:
```python
import socket
host = "192.168.0.1"
port = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.settimeout(5)
data, addr = s.recvfrom(1024)
print "recevied from ",addr
print "obtained ", data
s.close()
```
I added one line extra, that is, s.settimeout(5). The program waits for 5 seconds; only after that it will give an error message. Run udptime1.py.

The output is shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68699898-90e68780-0549-11ea-89a3-836694b27434.png)

The program shows an error; however, it does not look good if it gives an error message. The program should handle the exceptions.

## Socket exceptions
In order to handle exceptions, we'll use the try and except blocks. The next example will tell you how to handle the exceptions. Run udptime2.py:
```python
import socket
host = "192.168.0.1"
port = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
  
  s.bind((host,port))
  s.settimeout(5)
  data, addr = s.recvfrom(1024)
  print "recevied from ",addr
  print "obtained ", data
  s.close()
  
except socket.timeout :
  print "Client not connected"
  s.close()
  ```
  
The output is shown in the following screenshot:
![image](https://user-images.githubusercontent.com/47218880/68699945-ac519280-0549-11ea-88e8-1764facabf06.png)

In the try block, I put my code, and from the except block, a customized message is printed if any exception occurs.

Different types of exceptions are defined in Python's socket library for different errors. These exceptions are described here:

* exception socket.herror: This block catches the address-related error.
* exception socket.timeout: This block catches the exception when a timeout on a socket occurs, which has been enabled by settimeout(). In the previous example you can see that we used socket.timeout.
* exception socket.gaierror: This block catches any exception that is raised due to getaddrinfo() and getnameinfo().
* exception socket.error: This block catches any socket-related errors. If you are not sure about any exception, you could use this. In other words, you can say that it is a generic block and can catch any type of exception.


## Useful socket methods
So far, you have gained knowledge of socket and client-server architecture. At this level, you can make a small program of networks. However, the aim of this module is to test the network and gather information. Python offers very beautiful as well as useful methods to gather information. First, import socket and then use these methods:

socket.gethostbyname(hostname): This method converts a hostname to the IPv4 address format. The IPv4 address is returned in the form of a string. Here is an example:
```python
>>> import socket
>>> socket.gethostbyname('thapar.edu')
'220.227.15.55'
>>>
>>> socket.gethostbyname('google.com')
'173.194.126.64'
>>>
```
I know you are thinking about the nslookup command. Later, you will see more magic.

socket.gethostbyname_ex(name): This method converts a hostname to the IPv4 address pattern. However, the advantage over the previous method is that it gives all the IP addresses of the domain name. It returns a tuple (hostname, canonical name, and IP_addrlist) where the hostname is given by us, the canonical name is a (possibly empty) list of canonical hostnames of the server for the same address, and IP_addrlist is a list all the available IPs of the same hostname. Often, one domain name is hosted on many IP addresses to balance the load of the server. Unfortunately, this method does not work for IPv6. I hope you are well acquainted with tuple, list, and dictionary. Let's look at an example:
```python
>>> socket.gethostbyname_ex('thapar.edu')
('thapar.edu', [], ['14.139.242.100', '220.227.15.55'])
>>> socket.gethostbyname_ex('google.com')
>>>
('google.com', [], ['173.194.36.64', '173.194.36.71', '173.194.36.73', '173.194.36.70', '173.194.36.78', '173.194.36.66', '173.194.36.65', '173.194.36.68', '173.194.36.69', '173.194.36.72', '173.194.36.67'])
>>>
```
It returns many IP addresses for a single domain name. It means one domain such as thapar.edu or google.com runs on multiple IPs.

socket.gethostname(): This returns the hostname of the system where the Python interpreter is currently running:
```python
>>> socket.gethostname()
'eXtreme'
```
To glean the current machine's IP address by socket module, you can use the following trick using gethostbyname(gethostname()):
```python
>>> socket.gethostbyname(socket.gethostname())
'192.168.10.1'
>>>
```
You know that our computer has many interfaces. If you want to know the IP address of all the interfaces, use the extended interface:.
```python
>>> socket.gethostbyname_ex(socket.gethostname())
('eXtreme', [], ['10.0.0.10', '192.168.10.1', '192.168.0.1'])
>>>
```
It returns one tuple containing three elements: first is the machine name, second is a list of aliases for the hostname (empty in this case,) and third is the list of IP addresses of interfaces.

socket.getfqdn([name]): This is used to find the fully qualified name, if it's available. The fully qualified domain name consists of a host and domain name; for example, beta might be the hostname, and example.com might be the domain name. The fully qualified domain name (FQDN) becomes beta.example.com:.
```python
>>> socket.getfqdn('facebook.com')
'edge-star-shv-12-frc3.facebook.com'
```
In the preceding example, edge-star-shv-12-frc3 is the hostname, and facebook.com is the domain name. In the following example, FQDN is not available for thapar.edu:
```python
>>> socket.getfqdn('thapar.edu')
'thapar.edu'
```
If the name argument is blank, it returns the current machine name:
```python
>>> socket.getfqdn()
'eXtreme'
>>>
```
socket.gethostbyaddr(ip_address): This is like a "reverse" lookup for the name. It returns a tuple (hostname, canonical name, and IP_addrlist) where hostname is the hostname that responds to the given ip_address, the canonical name is a (possibly empty) list of canonical names of the same address, and IP_addrlist is a list of IP addresses for the same network interface on the same host:
```python
>>> socket.gethostbyaddr('173.194.36.71')
('del01s06-in-f7.1e100.net', [], ['173.194.36.71'])

>>> socket.gethostbyaddr('119.18.50.66')

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    socket.gethostbyaddr('119.18.50.66')
herror: [Errno 11004] host not found
```
It shows an error in the last query because reverse DNS lookup is not present.

socket.getservbyname(servicename[, protocol_name]): This converts any protocol name to the corresponding port number. The Protocol name is optional, either TCP or UDP. For example, the DNS service uses TCP as well as UDP connections. If the protocol name is not given, any protocol could match:
```python
>>> import socket
>>> socket.getservbyname('http')
80
>>> socket.getservbyname('smtp','tcp')
25
>>>
```
socket.getservbyport(port[, protocol_name]): This converts an Internet port number to the corresponding service name. The protocol name is optional, either TCP or UDP:
```python
>>> socket.getservbyport(80)
'http'
>>> socket.getservbyport(23)
'telnet'
>>> socket.getservbyport(445)
'microsoft-ds'
>>>
```
socket.connect_ex(address): This method returns an error indicator. If successful. it returns 0; otherwise, it returns the errno variable. You can take advantage of this function to scan the ports. Run the connet_ex.py program:
```python
import socket
rmip ='127.0.0.1'
portlist = [22,23,80,912,135,445,20]

for port in portlist:
  sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  result = sock.connect_ex((rmip,port))
  print port,":", result
  sock.close()
```
The output is shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68700281-3e599b00-054a-11ea-821a-e03ee4954adf.png)

The preceding program output shows that ports 80,912,135 and 445 are open. This is a rudimentary port scanner. The program is using the IP address 127.0.0.1; this is a loop back address, so it is impossible to have any connectivity issues. However, when you have issues, perform this on another device with a large port list. This time you will have to use socket.settimeout(value):
```python
socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
```
This socket method converts the host and port arguments into a sequence of five tuples.

Let's take a look at the following example:
```python
>>> import socket
>>> socket.getaddrinfo('www.thapar.edu', 'http')
[(2, 1, 0, '', ('220.227.15.47', 80)), (2, 1, 0, '', ('14.139.242.100', 80))]
>>>
```
output 2 represents the family, 1 represents the socket type, 0 represents the protocol, '' represents canonical name, and ('220.227.15.47', 80) represents the 2socket address. However, this number is difficult to comprehend. Open the directory of the socket.

Use the following code to find the result in a readable form:
```python
import socket
def get_protnumber(prefix):
  return dict( (getattr(socket, a), a)
    for a in dir(socket)
      if a.startswith(prefix))

proto_fam = get_protnumber('AF_')
types = get_protnumber('SOCK_')
protocols = get_protnumber('IPPROTO_')

for res in socket.getaddrinfo('www.thapar.edu', 'http'):

  family, socktype, proto, canonname, sockaddr = res

  print 'Family        :', proto_fam[family]
  print 'Type          :', types[socktype]
  print 'Protocol      :', protocols[proto]
  print 'Canonical name:', canonname
  print 'Socket address:', sockaddr
```
The output of the code is shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68700369-6812c200-054a-11ea-897b-8b3dc6fdb7db.png)

The upper part makes a dictionary using the AF_, SOCK_, and IPPROTO_ prefixes that map the protocol number to their names. This dictionary is formed by the list comprehension technique.

The upper part of the code might sometimes be confusing, but we can execute the code separately as follows:
```python
>>> dict(( getattr(socket,n),n) for n in dir(socket) if n.startswith('AF_'))
{0: 'AF_UNSPEC', 2: 'AF_INET', 6: 'AF_IPX', 11: 'AF_SNA', 12: 'AF_DECnet', 16: 'AF_APPLETALK', 23: 'AF_INET6', 26: 'AF_IRDA'}
```
Now, this is easy to understand. This code is usually used to get the protocol number:
```python
for res in socket.getaddrinfo('www.thapar.edu', 'http'):
```
The preceding line of code returns the five values, as discussed in the definition. These values are then matched with their corresponding dictionary.


