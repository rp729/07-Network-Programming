#!/usr/bin/env python3

import optparse
import random
import subprocess
from datetime import datetime

def mac():
    mac_chars = '0123456789ABCDEF'
    return mac_chars[random.randint(0,len(mac_chars)-1)]

#Establish vars
mac_addr = f'{mac()}{mac()}:{mac()}{mac()}:{mac()}{mac()}:{mac()}{mac()}:{mac()}{mac()}:{mac()}{mac()}'
interface = "eth0"

#Random print statement
print(f"Changing MAC Addr for {interface}")

#Run script
subprocess.call("ifconfig eth0 down",shell=True)
subprocess.call(f"ifconfig eth0 hw ether {mac_addr}",shell=True)
subprocess.call("ifconfig eth0 up",shell=True)
subprocess.call("ifconfig",shell=True)

#Record latest MAC:
file = open("mac_history.txt","a")
file.write(f"{datetime.now()} : {mac_addr}\n")


parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="Interface to change mac address")
parser.add_option("-m","--mac",dest="new_mac",help="add the new mac address")

(options,arguments)=parser.parse_args()

