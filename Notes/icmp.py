#!/usr/bin/python

from scapy.all import *

dst_ip = "10.0.2.2"
pkt = IP(dst=dst_ip)/ICMP()/"hello world"
send(pkt)

