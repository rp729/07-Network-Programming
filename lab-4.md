#### Lab 3A

Create a TCP Echo Server that mimmicks and sends back all of the data received from the client.

#### Lab 3C

Create a TCP client.  Pack the following values using network byte order: 12345, 56789, &, \*, 0x7d0, 0b11111010000. Send the packed hex to the TCP echo server.  Have the server unpack and send the values back to the client. Notice which values have changed and why.

#### Lab 3B

Write a UDP receiver that receives a string, and orders the words from longest to shortest in a new string.

That new string should be sent to the remote port+1.

\(i.e. the source port of message from the SENDER's POV\)

Write a UDP sender that sends the initial string, and receives the response from the receiver above.

Hint: The second step is intentionally ambiguous on how to proceed. There are multiple solutions.

-------------------------

host to network byte order

buffer sizes

socket timeout

handling socket errors

