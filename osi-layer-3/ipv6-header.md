# IPv6 Header

![](/assets/ipv6header.png)

Version – Set 6 for IPv6.

Traffic Class – Categorizes traffic forQoSpurposes. ECN is last 3 bits..

Flow Label – Request special handling by routers. May not be honored.

Payload Length – Size of payload in OCTETS. Including any extension headers.

Next Header – Layer 4 header of payload. Uses same values as IPv4's protocol field.

Hop Limit – Same as TTL.

Source / Destination - Do not change during routing.

---

##### IPv6 Headers are identified by number. They are not required to be used, however they provide useful features that were absent or poorly implemented in IPv4.

0 = Hop-by-Hop Options - Options that need to be examined by all devices on the path.

60 = Destination Options \(before routing header\) - Options that need to be examined only by the destination of the packet.

43 = Routing - Methods to specify the route for a datagram \(used with Mobile IPv6\).

44 = Fragment - Contains parameters for fragmentation of datagrams.

51 = Authentication Header \(AH\) - Contains information used to verify the authenticity of most parts of the packet.

50 = Encapsulating Security Payload \(ESP\) - Carries encrypted data for secure communication.

135 = Mobility \(currently without upper-layer header\) - Parameters used with Mobile IPv6.

