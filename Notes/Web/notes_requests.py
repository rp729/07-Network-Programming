import requests

link = "http://www.python-requests.org"

r = requests.get(link)
dir(r)
#    Display attributes

print(type(r))

r.url
#    URL of response object

r.status_code
#    Status code

'''
100 - informal
200 - success
300 - ?
'''

r.history
#    Status code of history events


r.headers
#    response headers with information about server, date, etc...
r.headers['Content-Type']
#    specific header information grab

r.request.headers

r.encodeing
#    response encoding

r.content[0:400]
#    400 bytes of characters

r.text[0:400]
#    sub string that is 400 string characters from response

r = requests.get(link,stream=True) 
#    raw responsed

r = raw.read(100)
#     read the first 100 characters from raw response


link = "https://feeds.citibikenyc.com/stations/stations.json"
response = requests.get(link).json()

for i in range(10):
    print('Station: ', response['stationBeanList'[i]['stationName'])

r = requests.get('https://api.github.com/user', auth=('myemail.mail.com','password'))
r.status_code

r.url

r.request
