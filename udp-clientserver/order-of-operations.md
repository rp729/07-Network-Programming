# UDP Order of Operations

* **socket\(\)** – Get a socket descriptor
* **bind\(\)** – Specify SOURCE port \(Optional for client/sender, Mandatory server/reciever\)
* **sendto\(\)/recvfrom\(\)** – _Data transfer\*_
* **close\(\)** – Close the socket

There is **ONE **socket and **UDP **is connectionless

\(A UDP socket exists independently of any specific remote IP/PORT\)

* Both sending and receiving data occur on the same socket, even to/from different remote hosts.

You must track the source of incoming data and destination of outgoing data

* This info must be passed to **sendto\(\)** and is returned by **recvfrom\(\)**



It's usually easier to think of them as **"Senders"** and **"Receivers“**.

* If you want to receive traffic, you need bind to a port.



