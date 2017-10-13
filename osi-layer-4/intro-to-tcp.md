# Intro to TCP

![](/assets/tcp.png)

* The OSI model is primarily a theory model.
* The TCP/IP Model is more practical oriented.
* Both are useful at different times. We are primarily concerned with OSI layers 2,3,4,7 in this class.

TCP is a connection oriented protocol that provides error checking and reliability of communication.



Most protocols commonly used on the internet use TCP, including HTTP, SMTP, and SSH.



TCP connections open with a handshake, data is transmitted, and then the connection is closed with a teardown.



TCP provides reliable transfer via:

* Correctly ordering packets received in arbitrary order.
* Validating received packets were not corrupt.
* Re-requesting packets that were corrupt or not received at all.
* Flow and congestion control.
* Requires positive acknowledgement before next data transmission.



