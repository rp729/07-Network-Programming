# Write a script that runs a command (like "ls -l", it can be any command you choose).

import subprocess
import os

def main():
    subprocess_command()
    os_command()

def subprocess_command():
    command = input("Enter Linux command: ")
    subprocess.call(f"{command}",shell=True)

def os_command():
    command = input("Enter Linux command: ")
    os.system(command)

main()