#### Lab 5A

Write a TCP Server that will generate a random number from 0 to 100. Write TCP Client that will receive an input from the user \(number 0 to 100\) and send the guess to the server.  The server will then send back a message prompting the user to guess higher or lower.  If the user guesses the correct number, have the server send back a success message and when the client receives the success message it will break the connection.

-----------------------

#### Lab 5B

Write a UDP listener that listens on port 2222 for a string. Have the server split the string into words \(space separated\) and send each word to a random port from the list below.

If the random port picked has already been used to transmit, it is ok to use it again

Write a UDP receiver that sends a sentence over port 2222, then waits for the response traffic on all ports below and uses select\(\) to reconstruct the sentence as its sent back from the server, one word/port per line.

Portlist= 2345, 1789, 9999, 65233, 25000, 33912, 5901, 2223, 8768, 43848, 4432, 7292, 13666

::

\(Portxxxx\) The

\(Portyyyy\) quick

\(Port zzzz\) brown

---

#### Lab 5C

HTTP Client/Server Turtorial under construction.

