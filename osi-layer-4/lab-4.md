# Lab 4-2

### Performance Lab:

Create a TCP client using IPv4. Pack the following values in a struct using network byte order: 12345, 56789, &, \*, 0x7d0, 0b11111010000. Then send them to a TCP server and print the unpacked struct.

## Bonus:

### Lab 4A

Create a simple TCP chat server that connects to multiple clients using IPv4 and either Select\(\) or Threading. Then echo back data to all clients using broadcasts \(Use multiple VM's and track traffic in Wireshark\).

### Lab 4B

Create a Flood/DoS program \(Syn / Ack, [etc](https://en.wikipedia.org/wiki/Denial-of-service_attack#Reflected_.2F_spoofed_attack)...\) using Raw Sockets in C or Python, and IPv4. Get creative!

