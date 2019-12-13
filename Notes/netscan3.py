#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    #scapy.ls(scapy.Ether())
    arp_request_broadcast.show()
    print(arp_request_broadcast.summary())

scan("10.0.3.0") # python3 issue (python 2 = 10.0.3.0/24)
