# Serving HTTP requests from your machine
You would like to create your own web server. Your web server should handle client requests and send a simple hello message.

Python ships with a very simple web server that can be launched from the command line as follows:
```
$ python -m SimpleHTTPServer 8080
```
This will launch an HTTP web server on port 8080. You can access this web server from your browser by typing http://localhost:8080. This will show the contents of the current directory from where you run the preceding command. If there is any web server index file, for example, index.html, inside that directory, your browser will show the contents of index.html. However, if you like to have full control over your web server, you need to launch your customized HTTP server.

Listing below gives the following code for the custom HTTP web server:
```python
#!/usr/bin/env python 

# This program requires Python 3.5.2 or any later version 
# It may run on any other version with/without modifications. 
# 
# Follow the comments inline to make it run on Python 2.7.x. 
 
 
import argparse 
import sys 
 
from http.server import BaseHTTPRequestHandler, HTTPServer 
# Comment out the above line and uncomment the below for Python 2.7.x. 
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer 
 
DEFAULT_HOST = '127.0.0.1' 
DEFAULT_PORT = 8800 
 
 
class RequestHandler(BaseHTTPRequestHandler): 
    """ Custom request handler""" 
     
    def do_GET(self): 
        """ Handler for the GET requests """ 
        self.send_response(200) 
        self.send_header('Content-type','text/html') 
        self.end_headers() 
        # Send the message to browser 
        self.wfile.write("Hello from server!") 
        return 
     
 
class CustomHTTPServer(HTTPServer): 
    "A custom HTTP server" 
    def __init__(self, host, port): 
        server_address = (host, port) 
        HTTPServer.__init__(self, server_address, RequestHandler) 
         
 
def run_server(port): 
    try: 
        server= CustomHTTPServer(DEFAULT_HOST, port) 
        print ("Custom HTTP server started on port: %s" % port) 
        server.serve_forever() 
    except Exception as err: 
        print ("Error:%s" %err) 
    except KeyboardInterrupt: 
        print ("Server interrupted and is shutting down...") 
        server.socket.close() 
 
 
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Simple HTTP Server
              Example') 
    parser.add_argument('--port', action="store",
     dest="port", type=int, default=DEFAULT_PORT) 
    given_args = parser.parse_args()  
    port = given_args.port 
    run_server(port) 
```
The following screenshot shows a simple HTTP server:

![image](https://user-images.githubusercontent.com/47218880/68710079-87b2e600-055c-11ea-89b7-c2333bdf3628.png)

Serving HTTP Request from the Machine
If you run this web server and access the URL from a browser, this will send the one line text Hello from server! to the browser, as follows:
```
$ python 14_2_simple_http_server.py --port=8800
Custom HTTP server started on port: 8800
localhost - - [18/Apr/2013 13:39:33] "GET / HTTP/1.1" 200 -
localhost - - [18/Apr/2013 13:39:33] "GET /favicon.ico HTTP/1.1" 200 
```  
## What's Happening:

In this script, we created the CustomHTTPServer class inherited from the HTTPServer class. In the constructor method, the CustomHTTPServer class sets up the server address and port received as a user input. In the constructor, our web server's RequestHandler class has been set up. Every time a client is connected, the server handles the request according to this class.

The RequestHandler defines the action to handle the client's GET request. It sends an HTTP header (code 200) with a success message Hello from server! using the write() method.




























