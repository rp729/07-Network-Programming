# Downloading data from an HTTP server
You would like to write a simple HTTP client to fetch some data from any web server using the native HTTP protocol. This can be the very first steps towards creating your own HTTP browser.

Let us access https://www.python.org/ with our Pythonic minimal browser.

You may need to install urllib module for the relevant Python versions:
```
$ sudo pip2 install urllib  
```
Listing below explains the following code for a simple HTTP client:
```python
#!/usr/bin/env python 

# This program requires Python 3.5.2 or any later version 
# It may run on any other version with/without modifications. 
# 
# Follow the comments inline to make it run on Python 2.7.x. 
 
import argparse 
 
import urllib.request 
# Comment out the above line and uncomment the below for Python 2.7.x. 
#import urllib2 
 
REMOTE_SERVER_HOST = 'http://www.cnn.com' 
 
class HTTPClient: 
 
    def __init__(self, host): 
        self.host = host 
 
    def fetch(self): 
        response = urllib.request.urlopen(self.host) 
        # Comment out the above line and uncomment the below for 
          Python 2.7.x. 
        #response = urllib2.urlopen(self.host) 
 
        data = response.read() 
        text = data.decode('utf-8') 
        return text 
 
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='HTTP Client Example') 
    parser.add_argument('--host', action="store",
     dest="host",  default=REMOTE_SERVER_HOST) 
 
    given_args = parser.parse_args()  
    host = given_args.host 
    client = HTTPClient(host) 
    print (client.fetch()) 
```
This script will by default fetch a page from http://www.cnn.com. You can run this recipe with or without the host argument. You may choose to fetch any specific web page by passing the URL as an argument. If this script is executed, it will show the following output:
```
$  python 14_1_download_data.py --host=http://www.python.org  
<!doctype html> 
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]--> 
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]--> 
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]--> 
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]--> 
 
<head> 
    <meta charset="utf-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
 
    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/
                               jquery/1.8.2/jquery.min.js"> 
 
    <meta name="application-name" content="Python.org"> 
    <meta name="msapplication-tooltip" content="The official
     home of the Python Programming Language"> 
    <meta name="apple-mobile-web-app-title" content="Python.org"> 
    <meta name="apple-mobile-web-app-capable" content="yes"> 
    <meta name="apple-mobile-web-app-status-bar-style" content="black"> 
 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <meta name="HandheldFriendly" content="True"> 
    <meta name="format-detection" content="telephone=no"> 
    <meta http-equiv="cleartype" content="on"> 
 
.... 
```
The following is the screenshot of the program:

![image](https://user-images.githubusercontent.com/47218880/68708681-d317c500-0559-11ea-83a0-9e71403d2900.png)

Download Data from an HTTP Server
This recipe will also work for any page in the sites. Not just the home page:

$ python 14_1_download_data.py --host=https://www.python.org/downloads/ 
<!doctype html> 
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]--> 
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]--> 
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]--> 
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]--> 
 
... 
    <title>Download Python | Python.org</title> 
.... 
 
If you run this script with an invalid path, it will show the following server response:
```
$ python 14_1_download_data.py --host=https://www.python.org/downloads222/
Traceback (most recent call last):
File "14_1_download_data.py", line 39, in <module>
print (client.fetch())
File "14_1_download_data.py", line 24, in fetch
response = urllib.request.urlopen(self.host)
File "/usr/lib/python3.5/urllib/request.py", line 163, in urlopen return opener.open(url, data, timeout)
File "/usr/lib/python3.5/urllib/request.py", line 472, in open response = meth(req, response)
File "/usr/lib/python3.5/urllib/request.py", line 582, in http_response
'http', request, response, code, msg, hdrs)
File "/usr/lib/python3.5/urllib/request.py", line 510, in error
return self._call_chain(*args)
File "/usr/lib/python3.5/urllib/request.py", line 444, in _call_chain
result = func(*args)
File "/usr/lib/python3.5/urllib/request.py", line 590, in http_error_default
raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: OK 
```
This script defines an urllib.request module that fetches data from the remote host. urllib.request.urlopen() opens the given web page and fetches it. Since it comes with Python 3, it does not support Python 2. However, you may install and use urllib for Python 2 as we elaborated before.










