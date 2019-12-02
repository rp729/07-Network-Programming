
## UDP versus TCP
The main difference between TCP and UDP is that TCP is oriented to connections, where once the connection is established, the data can be transmitted in both directions, while UDP is a simpler internet protocol, without the need for connections.

Now, we have to analyze the differences according to certain features:

**Differences in data transfer:** TCP ensures the orderly and reliable delivery of a series of data from the user to the server and vice versa. UDP is not dedicated to point-to-point connections and does not verify the availability of whoever receives the data.

**Reliability:** TCP is more reliable because it manages to recognize that the message was received and retransmits the packets that have been lost. UDP does not verify what the communication has produced because it does not have the ability to check the connection and retransmit the packets.

**Connection:** TCP is a protocol that's oriented toward the congestion control of the network and the reliability of the frames, while UDP is a non-connection oriented protocol that's designed to establish a rapid exchange of packets without the need to know whether the packets are arriving correctly.

**Transfer method:** TCP reads data as a sequence and the message is transmitted in defined segments. UDP messages are data packets that are sent individually and their integrity is verified upon arrival.

**How TCP and UDP work**: A TCP connection is established through the process of starting and verifying a connection. Once the connection has been established, it is possible to start the data transfer, and once the transfer is complete, the connection is completed by closing the established virtual circuits. UDP provides an unreliable service and the data may arrive unordered, duplicated, or incomplete, and it doesn't notify either the sender or receiver. UDP assumes that corrections and error checking are not necessary, avoiding the use of resources in the network interface.

**TCP and UDP applications**: TCP is used mainly when you need to use error correction mechanisms in the network interface, while UDP is mainly used in applications based on small requests from a large number of clients, for example, DNS and Voice Over IP (VoIP).
