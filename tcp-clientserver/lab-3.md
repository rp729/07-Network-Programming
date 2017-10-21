**Lab 2A**

Write a TCP server that receives a string, reverses order of the words, and sends it back to the client.

Write a TCP client to connect to and print the response \(build in both IPv4 and IPv6\).

**Lab 2B**

Write a simple socket program that will send back your machine's Host name and IP Address.

\(Don't forget to use your resources \(Pydocs, Man pages\).  You can also get formatting help from the python interpreter by using help\(socket.gethostname\) and help\(socket.gethostbyname\) after importing the socket module.\)

**Lab 2C**

Write a simple socket program that will pull the IP address from a remote website.

**Lab 2D**

Write a UDP sender that takes a dictionary, turns it into a JSON string, and sends it to a listener.

Write the UDP receiver to receive the JSON string and turns it back into a dictionary.

Validate by printing the type of your dictionary variable. \(Build in IPv4 and IPv6\)

**Lab 2E \(Bonus\)**

Write a UDP receiver that receives a string, and orders the words from longest to shortest in a new string.

That new string should be sent to the remote port+1.

\(i.e. the source port of message from the SENDER's POV\)

Write a UDP sender that sends the initial string, and receives the response from the receiver above.

Hint: The second step is intentionally ambiguous on how to proceed. There are multiple solutions.

\***Lab 2F**

[https://linux.die.net/man/8/arping](https://linux.die.net/man/8/arping)

Generate a valid ARP Request to your VM. Wireshark confirms it is not malformed/displays no errors, and your request produces a reply.

Ensure that you see both your frame and your VM's frame on Wireshark.

Ensure that you see the ARP Reply triggered by your ARP request in Wireshark.

