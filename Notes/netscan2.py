#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    scapy.ls(scapy.ARP())

scan("10.0.3.0") # python3 issue (python 2 = 10.0.3.0/24)
