# TCP Flags

TCP uses a bit field to represent flags.



**NS **- Nonce Sum, used to counter an old method for an attacker attempting to "hide" traffic



**CWR **- Congestion Window Reduced, an acknowledgement of congestion notification \(ECE\)



**ECE **- Explicit Congestion Notification, notifies sender of network congestion, or that the remote side is ENC capable \(if sent along with SYN\)



**URG **- Urgent field is valid in this transmission



**ACK **- Acknowledgement field is valid. Is on almost all transmissions except for initial SYN



**PSH **- Requests data be pushed to application



**RST **- Resets the connection



**SYN **- Requests aSeqNo sync



**FIN **- No more data to send

