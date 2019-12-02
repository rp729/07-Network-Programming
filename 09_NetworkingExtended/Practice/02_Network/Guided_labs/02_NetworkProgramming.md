
# Retrieving a remote machine's IP address
Sometimes, you need to translate a machine's hostname into its corresponding IP address, for example, a quick domain name lookup. This recipe introduces a simple function to do that.

If you need to know the IP address of a remote machine, you can use a built-in library function, gethostbyname(). In this case, you need to pass the remote hostname as its parameter.

In this case, we need to call the gethostbyname() class function. Let's have a look at this short code snippet.

Listing 1.2 shows how to get a remote machine's IP address as follows:
```python
    #!/usr/bin/env python
    
    # This program is optimized for Python 2.7.12 and 
      Python 3.5.2.
    # It may run on any other version with/without 
      modifications.
    
    
    import socket
    
    def get_remote_machine_info():
        remote_host = 'www.python.org'
        try:
            print ("IP address of %s: %s" %(remote_host, 
            socket.gethostbyname(remote_host)))
        except socket.error as err_msg:
            print ("%s: %s" %(remote_host, err_msg))
    
    if __name__ == '__main__':
        get_remote_machine_info()
```  
If you run the preceding code it gives the following output:
```python
$ python 1_2_remote_machine_info.py 
IP address of www.python.org: 151.101.36.223
```
## What's Happening:
This script wraps the gethostbyname() method inside a user-defined function called get_remote_machine_info(). In this recipe, we introduced the notion of exception handling. As you can see, we wrapped the main function call inside a try-except block. This means that, if some error occurs during the execution of this function, this error will be dealt with by this try-except block.

For example, let's change the remote_host value and replace https://www.python.org/ with something non-existent, for example, www.pytgo.org:
```python
#!/usr/bin/env python

# This program is optimized for Python 2.7.12 and 
  Python 3.5.2.
# It may run on any other version with/without 
  modifications.
    
    import socket
    
    def get_remote_machine_info():
        remote_host = 'www.pytgo.org'
        try:
            print ("IP address of %s: %s" %
                  (remote_host, 
            socket.gethostbyname(remote_host)))
        except socket.error as err_msg:
            print ("%s: %s" %(remote_host, err_msg))
    
    if __name__ == '__main__':
        get_remote_machine_info()
```  
Now run the following command:
```python
$ python 1_2_remote_machine_info.py 
www.pytgo.org: [Errno -2] Name or service not known
```
  
The try-except block catches the error and shows the user an error message that there is no IP address associated with the hostname, www.pytgo.org.
