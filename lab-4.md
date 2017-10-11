Lab 4A

struct

pack/unpack

host to network byte order

socket timeout

handling socket errors

modifying send.rec buffer size

---

1\) Generate a valid IPv6 Neighbor Solicitation to your classmate, that elicits a neighbor advertisement.

Ensure both the solicitation and advertisement are viewable in Wireshark

Valid means it conforms the RFC, Wireshark confirms it is not malformed/displays no errors, and your request produces a reply

Depending on the setup of an OS, there MIGHT be a timeout on how many Neighbor Advertisements can be sent out in a period of time. If there is nothing else wrong with your code, wait 2-3 mins and try again.

---

2\) Create a valid Neighbor Advertisement. You will only see the advertisement, there is no network reply.

Valid means it conforms the RFC, Wireshark confirms it is not malformed/displays no errors.

Validate with 'ip-6 neighbor show' on your classmate's system

---

3\)  Generate a valid IPv6 Router Solicitation to the class server, that elicits a router advertisement.

Ensure both the solicitation and advertisement are viewable in Wireshark

Valid means it conforms the RFC, Wireshark confirms it is not malformed/displays no errors, and your request produces a reply

-------------------------------------------------------

4\)  Generate a valid IPv6 Router Advertisement to the class server. Use a timeout of 256.



You will see your link-local IPv6 address show up on screen as a "default" route



Ensure the advertisement is viewable in Wireshark



Valid means it conforms the RFC, Wireshark confirms it is not malformed/displays no errors, and your request produces a route on the server \(will be displayed on screen\)



Your RA will put your link-local address on the screen as 'default'

------------------------------------------------------------

5\)  Create a raw socket that can handle ICMP traffic



Generate a ping packet and send it.



Validate you can receive the response on your initial socket.



Use struct to unpack the values into the ICMPv6 header. Print the name of each field, it's width, and the value

