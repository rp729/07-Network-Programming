# Internet Control Message Protocol



A "helper" protocol that supports IP, provides information, and error reporting.



Many messages have been deprecated, reserved, or are obsolete.



Each message has a Type, and each type may have several Codes.

------------------------------------

Type 0 Echo Reply:

* Ping



Type 3 Destination Unreachable:

* Code 0 Destination Network Unreachable
* Code 1 Destination Host Unreachable
* Code 3 Destination Port Unreachable \(NOTE: See Layer 4 for slight modification regarding TCP\)



Type 8 - Echo Request:

* Ping



Type 11 Time Exceeded:

* Code 0 TTL Exceeded
* Code 1 Fragment Reassembly Time Exceeded



Type 30 Traceroute:

* Deprecated



