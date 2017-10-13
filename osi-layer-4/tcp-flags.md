# TCP Header

![](/assets/MJB-TCP-Header-800x564.png)

---

# TCP Flags

![](/assets/tcphead.PNG)

##### TCP uses a bit field to represent flags.

**NS - Nonce Sum**, used to counter an old method for an attacker attempting to "hide" traffic.

**CWR - Congestion Window Reduced**, an acknowledgement of congestion notification \(ECE\).

**ECE - Explicit Congestion Notification**, notifies sender of network congestion, or that the remote side is ENC capable \(if sent along with SYN\).

**URG - Urgent field**, is valid in this transmission.

**ACK **- **Acknowledgement field**, is on almost all transmissions except for initial SYN.

**PSH **- Requests data be pushed to application.

**RST **- Resets the connection.

**SYN **- Requests a Seq No sync.

**FIN **- No more data to send.

---

#### PSH vs URG

**PSH **- Force the receiver to push all data to the process immediately. Used for interactive things where keystrokes should be processed relatively quickly by Layer 7.Netcatdoes this to force writing to the terminal. Telnet is another example

**URG **- Not well documented or implemented. Urgent pointer indicates how much data is urgent, from the beginning of the segment. Only the urgent data should be provided to the process in an out-of-band manner.

Neither has an API to actually set the value.

