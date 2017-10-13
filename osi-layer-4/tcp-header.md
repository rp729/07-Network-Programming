# TCP Header

![](/assets/MJB-TCP-Header-800x564.png)

**Source Port **– sending port



**Destination Port **– Receiving port



**Sequence Number **– Initially random. Each new transmission adds the size of the data



**Acknowledgment Number **– The next byte expected to be received.



**Data offset** - Size of TCP header in 32bit words



**Reserved **– 0's



**Flags **– Bit mask of all TCP flags



**Window size** – Max number of bytes receiver can handle



**Checksum **– Checksum of header and data



**Urgent Pointer** – Only valid if URG flag set



**Options **– Allows for expanded uses

