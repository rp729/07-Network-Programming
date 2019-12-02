# Downloading an RFC with requests
Now, are going to create the same script but, instead of using urllib, we are going to use the requests module. For this, create a text file called RFC_download_requests.py:
```python
#!/usr/bin/env python3

import sys, requests
try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)
template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc = requests.get(url).text
print(rfc)
```
We can simplify the previous script using the requests module. The main difference with the requests module is that we use the get method for the request and access the text property to get information about the specific RFC.


# Downloading an RFC with the socket module
Now, we are going to create the same script but, instead of using urllib or requests, we are going to use the socket module for working at a low level. For this, create a text file called RFC_download_socket.py:
```python
#!/usr/bin/env python3

import sys, socket
try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)

host = 'www.rfc-editor.org'
port = 80
sock = socket.create_connection((host, port))

req = ('GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
'Host: {host}:{port}\r\n'
'User-Agent: Python {version}\r\n'
'Connection: close\r\n'
'\r\n'
)

req = req.format(rfcnum=rfc_number,host=host,port=port,version=sys.version_info[0])
sock.sendall(req.encode('ascii'))
rfc_bytes = bytearray()

while True:
 buf = sock.recv(4096)
 if not len(buf):
     break
 rfc_bytes += buf
rfc = rfc_bytes.decode('utf-8')
print(rfc)
```
The main difference here is that we are using a socket module instead of urllib or requests. Socket is Python's interface for the operating system's TCP and UDP implementation. We have to tell socket which transport layer protocol we want to use. We do this by using the socket.create_connection() convenience function. This function will always create a TCP connection. For establishing the connection, we are using port 80, which is the standard port number for web services over HTTP.

Next, we deal with the network communication over the TCP connection. We send the entire request string to the server by using the sendall() call. The data that's sent through TCP must be in raw bytes, so we have to encode the request text as ASCII before sending it.

Then, we piece together the server's response as it arrives in the while loop. Bytes that are sent to us through a TCP socket are presented to our application in a continuous stream. So, like any stream of unknown length, we have to read it iteratively. The recv() call will return the empty string after the server sends all of its data and closes the connection. Finally, we can use this as a condition for breaking out and printing the response.
