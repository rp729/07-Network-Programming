'''
Use urllib to retrieve http://data.pr4e.org/romeo.txt and display up to 3000 characters, and counting the overall
characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of
the document contents.
'''

import urllib.request as request

count = 0
link = 'http://data.pr4e.org/romeo.txt'
document = request.urlopen(link)
for line in document:
    line.decode()
    count += len(line)
    if count < 50:
        print(line)
print(count)