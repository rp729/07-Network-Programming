# Printing your machine's name and IPv4 address
Sometimes, you need to quickly discover some information about your machine, for example, the hostname, IP address, number of network interfaces, and so on. This is very easy to achieve using Python scripts.

As this script is very short, you can try this in the Python interpreter interactively.

First, we need to import the Python socket library with the following command:
```python
>>> import socket  
```
Then, we call the gethostname() method from the socket library and store the result in a variable as follows:
```python
>>> host_name = socket.gethostname()
>>> print "Host name: %s" %host_name
Host name: llovizna
>>> print "IP address: %s" 
%socket.gethostbyname(host_name)
IP address: 127.0.1.1
```  
The entire activity can be wrapped in a free-standing function, print_machine_info(), which uses the built-in socket class methods.

We call our function from the usual Python __main__ block. During runtime, Python assigns values to some internal variables such as __name__. In this case, __name__ refers to the name of the calling process. When running this script from the command line, as shown in the following command, the name will be __main__. But it will be different if the module is imported from another script. This means that, when the module is called from the command line, it will automatically run our print_machine_info function; however, when imported separately, the user will need to explicitly call the function.

Listing 1.1 shows how to get our machine info, as follows:
```python
#!/usr/bin/env python

# This program is optimized for Python 2.7.12
   and Python 3.5.2.
# It may run on any other version with/without 
  modifications.
    
    import socket
    
    
    def print_machine_info():
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print ("Host name: %s" %host_name)
        print ("IP address: %s" %ip_address)
    
    if __name__ == '__main__':
        print_machine_info()
```  
In order to run this recipe, you can use the provided source file from the command line as follows:

```python
$python 1_1_local_machine_info.py  
```
On my machine, the following output is shown:

```python
Host name: 90cos
IP address: 127.0.1.1
```
The hostname is what you assigned to your computer when you configured your operating system. This output will be different on your machine depending on the system's host configuration. Here hostname indicates where the Python interpreter is currently executing.

