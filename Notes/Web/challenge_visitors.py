import urllib
import requests

link = 'https://analytics.usa.gov/data/live/realtime.json'
r = requests.get(link)
req = r.content[0:400]
response = r.json()

print(req)
print(response['data'][0]['active_visitors'])