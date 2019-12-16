#Write a script that runs a command to display your current directory.

import subprocess
import os

def main():
    subprocess_pwd()
    os_pwd()

def subprocess_pwd():
    command = 'pwd'
    subprocess.call(f"{command}",shell=True)

def os_pwd():
    command = 'pwd'
    os.system(command)

main()