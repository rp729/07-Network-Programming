# Lab 5-1

## HTTP Client and Server in C

Some of the standardized RFCs are:

HTTP/1.1 →Initially it is [RFC 2616](http://www.rfc-editor.org/info/rfc2616) but later replaced by [RFC 7230](http://www.rfc-editor.org/info/rfc7230), [RFC 7231](http://www.rfc-editor.org/info/rfc7231), [RFC 7232](http://www.rfc-editor.org/info/rfc7232), [RFC 7233](http://www.rfc-editor.org/info/rfc7233), [RFC 7234](http://www.rfc-editor.org/info/rfc7234), [RFC 7235](http://www.rfc-editor.org/info/rfc7235). So, we need to read from RFC 7230 to RFC 7235 to implement basic workings of HTTP.

HTTP/2 → [RFC 7540](http://www.rfc-editor.org/info/rfc7540) and [RFC 7541](http://www.rfc-editor.org/info/rfc7541)

#### HTTP Server:

1. Create
2. Define
3. Bind
4. Listen
5. Accept
6. Send/Receive
7. Close

A socket, `server_fd`, is created with the _socket_ system call:

```text
int server_fd = socket(domain, type, protocol);
```

Domain - Address Family: AF\_INET\(IPv4\) \|  AF\_INET6 \(IPv6\)

Type: SOCK\_STREAM \(TCP\)  \|  SOCK\_DGRAM \(UDP\)  \|  SOCK\_RAW \(RAW\)

Protocol - Only used for specific Address Families that support multiple protocols.

**Create:**

```text
#include <sys/socket.h>
...
...
if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
{
    perror(“cannot create socket”); 
    return 0; 
}
```

**Define and Bind:**

```text
struct sockaddr_in address;
const int PORT = 8080; 

memset((char *)&address, 0, sizeof(address)); 
address.sin_family = AF_INET; 
address.sin_addr.s_addr = htonl(INADDR_ANY); //0.0.0.0
address.sin_port = htons(PORT); 

if (bind(server_fd,(struct sockaddr *)&address,sizeof(address)) < 0) 
{ 
    perror(“bind failed”); 
    return 0; 
}
```

**Listen:**

```text
int listen(int socket, int backlog);
```

**Accept:**

```text
                1                                  2                              3     
int accept(int socket, struct sockaddr *restrict address, socklen_t *restrict address_len);
```

1. Socket created for accepting connection in the _listen_ function.
2. The address structure that gets filed in with the client's IP.
3. Length of the Address Structure.

```text
if (listen(server_fd, 3) < 0) //error handling
{ 
    perror(“In listen”); 
    exit(EXIT_FAILURE); 
}
```

```text
if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen))<0)
{
    perror("In accept");            //error handling
    exit(EXIT_FAILURE);        
}
```

![](../.gitbook/assets/image%20%283%29.png)



