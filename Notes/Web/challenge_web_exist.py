from urllib import request
from urllib import error

def main():
    web_check()

def web_check():
    url = input("Enter url (ex: google.com) :")
    url = f'https://www.{url}'
    try:
        request.urlopen(url)
        print("ITS GOOD!")
    except error.URLError as e:
        print(f"ERROR: {e.reason}")

main()
