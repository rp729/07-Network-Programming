# Lab 3-1

## TCP Sockets in C

![](../.gitbook/assets/image%20%282%29.png)

### TCP Client:

First, import standard and socket realted libraries.

```text
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
```

Next, create the socket. 

```text
	int network_socket;
	network_socket = socket(AF_INET, SOCK_STREAM, 0);
```

> AF\_INET = IPv4 \| AF\_INET6 = IPv6
>
> SOCK\_STREAM = TCP \| SOCK\_DGRAM = UDP

Then, specify an address for the socket.

```text
	struct sockaddr_in server_address;  // socket struct called server_address
	server_address.sin_family = AF_INET; // address family
	server_address.sin_port = htons(30001); //converts the unsigned short int from 
		//"host" byte order to "network" byte order. host-to-network(PORT#)
	server_address.sin_addr.s_addr = INADDR_ANY; 
```

sin\_addr is a struct. So you want to access s\_addr within sin.addr 

INADDR\_ANY is the same as 0.0.0.0 basically telling the computer to connect to any available IPv4 address on the computer.

Finally, initiate the connection.

```text
	int connection_status;
	connection_status = connect(network_socket, (struct sockaddr *) &server_address, sizeof(server_address));
	
	//error checking connection to server
	if(connection_status == -1)
	{
		printf("Error with connection\n\n");
	}
```

\#include &lt;sys/types.h&gt;

\#include &lt;sys/socket.h&gt;

int connect\(int sockfd, struct sockaddr \*serv\_addr, int addrlen\);

* sockfd -  A file descriptor that specifies the socket for which the address should be set.
* serv\_addr - A _struct sockaddr_ containing the destination port and IP address.
* addrlen - Defines the length of the address being passed to the function.

If the client connects successfully, receive the information and print it out.

```text
	char server_response[256]; 
	recv(network_socket, &server_response, sizeof(server_response), 0);

	printf("The server sent the data: %s \n", server_response);
```

recv\(socket created, data from server / location, and size\) There is also an optional flags parameter.

Once all of the information has been sent and/or received, close the socket, passing the _network\_socket_ as an attribute to the _close\(\)_ function.

```text
close(network_socket);
```

#### TCP Client

```text
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {	
	
	// create the socket
	int network_socket;
	network_socket = socket(AF_INET, SOCK_STREAM, 0);
	
	//setup an address
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_addr.s_addr = INADDR_ANY;
	server_address.sin_port = htons(30001);

	int connection_status;
	connection_status = connect(network_socket, (struct sockaddr *) &server_address, sizeof(server_address));
	
	//error checking connection to server
	if(connection_status == -1)
	{
		printf("Error with connection\n\n");
	}
	
	//receive data from the server
	char server_response[256];
	recv(network_socket, &server_response, sizeof(server_response), 0);

	//print the server's response
	printf("The server sent the data: %s \n", server_response);
	
	close(network_socket);

	return 0;
}
```

## TCP Server

First, load the standard and socket libraries.

```text
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
```

Next, create the socket.

```text
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
```

Then, specify an address for the server.

```text
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(30001);
    server_address.sin_addr.s_addr = INADDR_ANY;
```

Then, bind the socket to the specified IP address and port where the server can then listen for connections.

```text
bind(server_socket, (struct sockaddr*) &server_address, sizeof(server_address));
listen(server_socket, 5);
```

Finally, accept the connection and send/receive data.

```text
    int client_socket;
    client_socket = accept(server_socket, NULL, NULL);
    send(client_socket, server_message, sizeof(server_message), 0);
```

After all transmissions have completed, close the socket.

```text
    close(server_socket);
```

#### TCP Server

```text
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>

int main() {

    char server_message[256] = "Successfully connected!";
    
    // create the server socket
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0);

    
    // define the server address
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(30001);
    server_address.sin_addr.s_addr = INADDR_ANY;

    // bind the socket to our specified IP and port
    bind(server_socket, (struct sockaddr*) &server_address, sizeof(server_address));

    listen(server_socket, 5);

    int client_socket;
    client_socket = accept(server_socket, NULL, NULL);
    
    // send the message
    send(client_socket, server_message, sizeof(server_message), 0);

    // close the socket
    close(server_socket);
    
    return 0;
}

```

