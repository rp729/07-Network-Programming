#### Lab 3A

Create a TCP Echo Server that mimmicks and sends back all of the data received from the client.

You will be usingstruct.pack\(\) to simulate a binary protocol.

#### Lab 3B.1

Pack the values \(1, 2, -3, -4\) as the following data types \(unsigned short, unsignedint, signed short, signedint\)

1 as an unsigned short

2 as an unsignedint

-3 as a signed short

-4 as a signedint

Write a TCP client that packs those values, sends the packed string to a server.

Write a TCP server that receives the string, unpacks it using little endian and prints it, then unpacks it again using big endian and prints it.

#### Lab 3B.2

Create a TCP client.  Pack the following values using network byte order: 12345, 56789, &, \*, 0x7d0, 0b11111010000. Send the packed hex to the TCP echo server.  Have the server unpack and send the values back to the client. Notice which values have changed and why.

Q1\) Which unpacked are the same?



Q2\) Why are they the same? Does it matter whatEndianessyour system is using?



Q3\) Assume I repeat this lab with a client on a little-endian architecture, and the server on a big-endian architecture. How will the files change? Why?



Q4\) How can I be sure that the data I send is properly received on any endian machine?

#### Lab 3B

Write a UDP receiver that receives a string, and orders the words from longest to shortest in a new string.

That new string should be sent to the remote port+1.

\(i.e. the source port of message from the SENDER's POV\)

Write a UDP sender that sends the initial string, and receives the response from the receiver above.

Hint: The second step is intentionally ambiguous on how to proceed. There are multiple solutions.

---

host to network byte order

buffer sizes

socket timeout

handling socket errors

Router Solicitation, Neighbor Solicitation, and Redirect message

