# Writing a simple TCP echo client/server application
After testing with basic socket APIs in Python, let us create a TCP socket server and client now. Here, you will have the chance to utilize your basic knowledge gained in the previous scripts.

In this example, a server will echo whatever it receives from the client. We will use the Python argparse module to specify the TCP port from a command line. Both the server and client script will take this argument.

First, we create the server. We start by creating a TCP socket object. Then, we set the reuse address so that we can run the server as many times as we need. We bind the socket to the given port on our local machine. In the listening stage, we make sure we listen to multiple clients in a queue using the backlog argument to the listen() method. Finally, we wait for the client to be connected and send some data to the server. When the data is received, the server echoes back the data to the client.

Listing below shows how to write a simple TCP echo client/server application as follows:
```python
    #!/usr/bin/env python
  
    # This program is optimized for Python 2.7.12 
      and Python 3.5.2.
    # It may run on any other version with/without 
      modifications.
    
    
    import socket
    import sys
    import argparse
    
    host = 'localhost'
    data_payload = 2048
    backlog = 5 
    
    
    def echo_server(port):
        """ A simple echo server """
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, 
                          socket.SOCK_STREAM)
        # Enable reuse address/port 
        sock.setsockopt(socket.SOL_SOCKET, 
                      socket.SO_REUSEADDR, 1)
        # Bind the socket to the port
        server_address = (host, port)
        print ("Starting up echo server  on %s 
                     port %s" % server_address)
        sock.bind(server_address)
        # Listen to clients, backlog argument 
          specifies the max no. 
          of queued connections
        sock.listen(backlog) 
        while True: 
            print ("Waiting to receive message 
                    from client")
            client, address = sock.accept() 
            data = client.recv(data_payload) 
            if data:
                print ("Data: %s" %data)
                client.send(data)
                print ("sent %s bytes back 
                       to %s" % (data, address))
            # end connection
            client.close() 
    
    if __name__ == '__main__':
        parser = argparse.ArgumentParser
        (description='Socket Server Example')
        parser.add_argument('--port', 
        action="store", dest="port", type=int, 
                           required=True)
        given_args = parser.parse_args() 
        port = given_args.port
        echo_server(port)
```  
On the client side code, we create a client socket using the port argument and connect to the server. Then, the client sends the message, Test message. This will be echoed to the server, and the client immediately receives the message back in a few segments. Here, two try-except blocks are constructed to catch any exception during this interactive session.

Listing below shows the TCP echo client as follows:

```python
#!/usr/bin/env python 

# This program is optimized for Python 2.7.12
   and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
import sys 
 
import argparse 
 
host = 'localhost' 
 
def echo_client(port): 
    """ A simple echo client """ 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
     
    # Send data 
    try: 
        # Send data 
        message = "Test message. This will be 
                   echoed" 
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Received: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
     
if __name__ == '__main__': 
    parser = argparse.ArgumentParser
            (description='Socket Server Example') 
    parser.add_argument('--port', action="store", 
dest="port", type=int, required=True) 
    given_args = parser.parse_args()  
    port = given_args.port 
    echo_client(port) 
```
## What's Happening:

In order to see the client/server interactions, launch the following server script in one console:
```python
$ python 1_13a_echo_server.py --port=9900 
Starting up echo server  on localhost port 9900 
    
Waiting to receive message from client 
```  
Now, run the client from another Terminal as follows:
```python
$ python 1_13b_echo_client.py --port=9900 
Connecting to localhost port 9900 
Sending Test message. This will be echoed 
Received: Test message. Th 
Received: is will be echoe 
Received: d 
Closing connection to the server
```  
Upon receiving the message from the client, the server will also print something similar to the following message:
```
Data: Test message. This will be echoed 
sent Test message. This will be echoed 
bytes back to ('127.0.0.1', 42961) 
Waiting to receive message from client
```









