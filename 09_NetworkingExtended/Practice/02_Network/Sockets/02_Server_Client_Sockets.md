# Server socket methods

In a client-server architecture, there is one centralized server that provides service, 
and many clients request and receive service from the centralized server. Here are some methods you need to know:

* socket.bind(address): This method is used to connect the address (IP address, port number) to the socket. 
The socket must be open before connecting to the address.
* socket.listen(q): This method starts the TCP listener. The q argument defines the maximum number of lined-up connections.
* socket.accept(): The use of this method is to accept the connection from the client. Before using this method, 
the socket.bind(address) and socket.listen(q) methods must be used. The socket.accept() method returns two values:
client_socket and address, where client_socket is a new socket object used to send and receive data over the connection, 
and address is the address of the client. You will see examples later.

# Client socket methods
The only method dedicated to the client is the following:

socket.connect(address): This method connects the client to the server. The address argument is the address of the server.
