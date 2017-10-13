# User Datagram Protocol

UDP is connectionless and best effort delivery. Error checking is limited to a UDP checksum.



Being connectionless minimizes overhead.



Removing error checking, reordering, and other nice functionality from TCP increases speed since retransmissions do not occur and there is no need to wait for acknowledgements.



UDP is particularly well suited to protocols where a single message is sent the responses are also single messages:

*  DNS, DHCP, SNMP, RIP



Protocols and applications designed to handle a high volume of traffic can often internally handle some packet loss:

*  VOIP, Streaming Media, Video Games



