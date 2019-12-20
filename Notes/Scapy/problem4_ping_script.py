import os
import subprocess
os.sys.path.append('/home/osboxes/07-Network-Programming/venv/lib/python3.7/site-packages')
from scapy.all import *

def main():
    scapy_ping()
    linux_ping()

def scapy_ping():
    dst_ip = input("Enter the IP you wish to ping:")
    pkt = IP(dst=dst_ip)/ICMP()/"hello world"
    print("Sending ICMP packet with Scapy")
    send(pkt)

def linux_ping():
    dst_ip = input("Enter the IP you wish to ping:")
    print("Sending ICMP packet with Linux")
    subprocess.call(f'ping -c 1 {dst_ip}',shell=True)

main()