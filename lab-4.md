# Layer 3 Labs

---

#### **Lab 3A**

Write a UDP sender that takes a dictionary, turns it into a JSON string, and sends it to a listener.

Write the UDP receiver to receive the JSON string and turns it back into a dictionary.

Validate by printing the type of your dictionary variable \(Build in IPv4 and IPv6\).

#### Lab 3B

Using the struct package from the python library, pack the values \(1, 2, -3, -4\) as the following data types \(unsigned short, unsigned int, signed short, signed int\)

1 as an unsigned short

2 as an unsigned int

-3 as a signed short

-4 as a signed int

Write a TCP client that packs those values, sends the packed string to a server.

Write a TCP server that receives the string, unpacks it using little endian and prints it, then unpacks it again using big endian and prints it.

#### Lab 3C

Write a UDP receiver that receives a string, and orders the words from longest to shortest in a new string.

That new string should be sent to the remote port+1.

\(i.e. the source port of message from the SENDER's POV\)

Write a UDP sender that sends the initial string, and receives the response from the receiver above \(you can use multiple receivers or combine them\).

Hint: The second step is intentionally ambiguous on how to proceed. There are multiple solutions.

---



