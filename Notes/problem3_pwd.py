#Write a script that runs a command to display your current directory.

import subprocess

command = input("Type in 'pwd': ")
subprocess.call(f"{command}",shell=True)