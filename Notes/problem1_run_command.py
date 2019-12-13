# Write a script that runs a command (like "ls -l", it can be any command you choose).

import subprocess

command = input("Enter Linux command: ")
subprocess.call(f"{command}",shell=True)