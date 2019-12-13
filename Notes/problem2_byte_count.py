#Write a script that runs a command and captures the number of bytes in a print statement.
import sys
import subprocess

def main():
    file = open('byte_count.txt','w')
    command = input("Enter Linux command: ")
    subprocess.call(f"{command}",shell=True,stdout=file)
    file = open('byte_count.txt','r')
    print(f'Number of bytes: {byte_count(file.read())}')

def byte_count(item):
    return sys.getsizeof(item)

main()