# DHCP
IP addresses can be assigned to a device by a network administrator in one of two ways: statically, where the device's operating system is manually configured with the IP address, or dynamically, where the device's operating system is configured by using the DHCP.

When using DHCP, as soon as the device first connects to a network, it is automatically allocated an address by a DHCP server from a predefined pool. Some network devices, such as home broadband routers, provide a DHCP server service out of the box; otherwise, a DHCP server must be set up by a network administrator. DHCP is widely deployed, and it is particularly useful for networks where different devices may frequently connect and disconnect, such as public Wi-Fi hotspots or mobile networks.

DHCP environments require a DHCP server that's been configured with the appropriate parameters for the proposed network. The main DHCP parameters include the range or pool of available IP addresses, the correct subnet masks, and the gateway and server name addresses.

A DHCP server dynamically allocates IP addresses instead of having to depend on the static IP address and is responsible for assigning, leasing, reallocating, and renewing IP addresses. The protocol will assign an address that is available in a subnet or pool. This means that a new device can be added to a network without you having to manually assign it a unique IP address. DHCP can also combine static and dynamic IPs, and also determines how long an IP address is assigned to a device.

When a computer in a network wants to obtain a valid network configuration, usually when starting up the machine, it issues a DHCP Discover request. When this request—which is made through a UDP broadcast packet—reaches a DHCP server, a negotiation is established whereby the server grants the use of an IP, and other network parameters, to the client for a certain time.

It is important to take note of the following:
```
The client does not need to have the network interface configured to issue a DHCP Discover request.
The DHCP server can be on the same or a different subnet as the client will be on. If the client does not have network configuration, it cannot reach other subnets.
When the DHCP server receives the DHCP request, Discover obtains the Mac address of the client, which may affect the IP address assigned to the client.
The DHCP server grants network configuration to the client for a certain time. Before reaching the deadline, the client may try to renew the concession. If a concession occurs, the client must stop using the network configuration.
```
To make a DHCP request, you can use a client such as dhclient (native GNU/Linux) or the ipconfig/renew command (in the case of Windows). When a network configuration is obtained, the client uses it:

![image](https://user-images.githubusercontent.com/47218880/68702245-15d3a000-054e-11ea-9215-eb5f65f66cca.png)

# DNS
DNS allows for the association of domain names with IP addresses, which greatly facilitates access to the machines on the network. Without DNS, referring to a machine implies remembering your IP address. Working directly with IP addresses is not comfortable, because they are difficult to remember and because the IP address of a station can vary for different reasons. Whoever uses the domain name does not need to worry about these changes (although the DNS server must know the real IP in each case).

The domain name system is a distributed and hierarchical database, and although its main function is to associate domain names with IP addresses, it can also store other information. The DNS service is one of the pillars of the network, so its availability must be absolute. To achieve this, redundant servers are used and extensive caching is used to improve their performance.

The nslookup tool comes with most Linux and Windows systems and lets us query DNS on the command line, as follows:

![image](https://user-images.githubusercontent.com/47218880/68702275-27b54300-054e-11ea-9d99-67328343f97a.png)

We can use this command to request the IP address for the cnn.com domain:

![image](https://user-images.githubusercontent.com/47218880/68702373-54695a80-054e-11ea-9d1b-770894d81990.png)

With this command, we determined that the cnn.com host has an IP address. DNS distributes the work of looking up hostnames by using a hierarchical system of caching servers. Internet DNS services are a set of databases that are scattered on servers around the world. These databases indicate the IP that is associated with a name of a website. When we enter an address in the search engine, for example, cnn.com, the computer asks the DNS servers of the internet provider to find the IP address associated with cnn.com. If the servers do not have that information, a search is made with other servers that may have it.

When we run our preferred browser and write a web address in its address bar to access the content that's hosted on the site, the DNS service will translate these names into elements that can be understood and used for the equipment and systems that make up the internet.

On Windows computers, this system is configured by default to automatically use the DNS server of our internet service provider. At this point, we may have different DNS providers such as OpenDNS, UltraDNS, or Google DNS as an alternative, but we must always keep in mind that these providers offer us minimum security conditions to navigate. More information about configuration using Google DNS can be found at the following URL: https://developers.google.com/speed/public-dns/.

