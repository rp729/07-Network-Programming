# Finding a service name, given the port and protocol
If you would like to discover network services, it may be helpful to determine what network services run on which ports using either the TCP or UDP protocol.

If you know the port number of a network service, you can find the service name using the getservbyport() socket class function from the socket library. You can optionally give the protocol name when calling this function.

Let us define a find_service_name() function, where the getservbyport() socket class function will be called with a few ports, for example, 80, 25. We can use Python's for-in loop construct.

Listing below shows finding_service_name as follows:
```python
#!/usr/bin/env python 

# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
 
def find_service_name(): 
    protocolname = 'tcp' 
    for port in [80, 25]: 
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))) 
     
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))) 
     
if __name__ == '__main__': 
    find_service_name() 
``` 
If you run this script, you will see the following output:
```python
$ python 1_4_finding_service_name.py 
    
Port: 80 => service name: http
Port: 25 => service name: smtp
Port: 53 => service name: domain
```    
This indicates that http, smtp, and domain services are running on the ports 80, 25, and 53 respectively.

## What's Happening:
In this script, the for-in statement is used to iterate over a sequence of variables. So for each iteration, we use one IP address to convert them in their packed and unpacked format.
