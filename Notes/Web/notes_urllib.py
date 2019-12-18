import urllib.request

dir(urllib.request) #List features available for urllib.request

link = 'https://www.google.com'

linkRequest = urllib.request.urlopen(link)
#TYPE: http.client

linkResponse = urllib.request.urlopen(link).read()
#TYPE: bytes

linkRequest.getcode()
#200

linkRequest.geturl()
#'https://www.google.com'

linkRequest._method
#'GET'


linkRequest.getheaders()
#Tons of crap

linkRequest.getheader("Content-Type")
#text/html; charset-ISO-8859-1

linkRequest.info()["Content-Type"]
#text/html; charset=ISO-8859-1

#==============================


import urllib.request as request
import urllib.error as error
try:
    request.urlopen("http://www.python.org")
except error.URLError as e:
    print("Error Occurred: ", e.reason)


#=============================

import urllib.parse as urlparse

print(dir(urlparse))

amazonUrl = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Pearson+Books'

print(urlparse.urlsplit(amazonUrl))
print(urlparse.urlsplit(amazonUrl).scheme)
print(urlparse.urlparse(amazonUrl))

data = {'param1':'value1','param2':'value2'}
urlparse.urlencode(data)

urlparse.parse_qs(urlparse.urlencode(data))

urlparse.urlencode(data).encode('utf-8')
#bytes

urlparse.urljoin('http://localhost:8080/~cache/','data file')

#============================

import urllib.robotparser as robot

par = robot.RobotFileParser()
par.set_url('https://www.samsclub.com/robots.txt')
par.read()
print(par)


par.can_fetch('*','https://www.samsclub.com/friend')

