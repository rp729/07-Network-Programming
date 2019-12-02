
# Extracting RFC information
The IETF landing page for RFCs is http://www.rfc-editor.org/rfc/, and reading through it tells us exactly what we want to know. We can access a text version of an RFC using a URL of the form http://www.rfc-editor.org/rfc/rfc741.txt. The RFC number in this case is 741. Therefore, we can get the text format of RFCs using HTTP.

At this point, we can build a Python script for downloading an RCF document from IETF, and then display the information that's returned by the service. We'll make it a Python script that just accepts an RFC number, downloads the RFC in text format, and then prints it to stdout.

The main modules that we can find in Python to make HTTP requests are urllib and requests, which work at a high level. We can also use the socket module if we want to work at a low level.

## Downloading an RFC with urllib
Now, we are going to write our Python script using the urllib module. For this, create a text file called RFC_download_urllib.py:
```python
#!/usr/bin/env python3

import sys, urllib.request
try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)
template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)
```
We can run the preceding code by using the following command:
```
$ python RFC_download_urllib.py 2324
```
This is the output of the previous script, where we can see the RFC description document:

![image](https://user-images.githubusercontent.com/47218880/68710683-9fd73500-055d-11ea-9913-89437345d7dd.png)

First, we import our modules and check whether an RFC number has been supplied on the command line. Then, we construct our URL by substituting the supplied RFC number. Next, the main activity, the urlopen() call, will construct an HTTP request for our URL, and then it will connect to the IETF web server and download the RFC text. Next, we decode the text to Unicode, and finally we print it out to the screen.
















