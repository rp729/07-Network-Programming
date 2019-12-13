#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast,timeout=1)[0]
    #print(answered_list.summary())
    
    print('IP\t\t\tMAC ADDRESS\n-----------------------------------------------------')
    for element in answered_list:
        print(element[1].psrc + "\t\t"+element[1].hwsrc)
        
        print("-----------------------------------------------------")

scan("10.0.2.2/24") # python3 issue (python 2 = 10.0.3.0/24)
