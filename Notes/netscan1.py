#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)
    #print(arp_request.summary())

scan("10.0.3.0/24")
