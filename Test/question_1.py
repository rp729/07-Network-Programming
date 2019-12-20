'''
1) Write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read
the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the
sum of the numbers in the file and enter the sum below: Here are two files for this assignment. One is a sample file
where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_57128.json (Sum ends with 10)
You do not need to save these files to your folder since your program will read the data directly from the URL.
'''

#Imported modules to run the code successfully
from urllib import request #Used in function to verify url exists
from urllib import error #Error message if url doesn't exist ex: https://www.python.ogr
import requests #Used to pull the json file

#Main function that runs the code
def main():
    sum_count()

#Engine to count the sum of the count
def sum_count():
    url = input("Enter URL: ")
    url = url_verify(url)
    if url != None:
        r = requests.get(url)
        #req = r.content[0:-1] This variable is purely for trouble shooting
        #print(req) This print statement is purely for trouble shooting
        response = r.json()
        sum = 0
        for i in range(len(response['comments'])):
            sum += response['comments'][i]['count']
        print(sum)
    else:
        return

#Basic verification of url we learned in class
def url_verify(url):
    try:
        request.urlopen(url)
        return url
    except error.URLError as e:
        print(f"ERROR: {e.reason}")
        return None

main()