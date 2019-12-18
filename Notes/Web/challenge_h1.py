#Create a python script to extract h1 tag from example.com or any site.
import requests
from bs4 import BeautifulSoup

def main():
    web_scrape()

def web_scrape():
    url = input("Enter name of website (ex: google.com) :")
    url = f'https://{url}'
    option = input("Choose from the following options: \n1) Print\n2) Scrape\nResponse :")
    option = input_validation(option)
    reqs = requests.get(url)
    if option == 1:
        soup = BeautifulSoup(reqs.text,'html.parser')
        print(soup.prettify())
    elif option == 2:
        tags = input("How many tags would you like to scrape? \nResponse :")
        tags = input_validation(tags)
        tag_list = []
        for i in range(tags):
            tag = input(f"({i+1} of {tags}) Enter tag :")
            tag_list.append(tag)
        soup = BeautifulSoup(reqs.text,'html.parser')
        for heading in soup.find_all(tag_list):
            print(f'{heading.name} {heading.text.strip()}')

def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("Invalid input! Enter an integer :")
    return int(num)

main()