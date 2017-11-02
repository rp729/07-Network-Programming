#### Lab 5A

Write a UDP listener that listens on port 2222 for a string. Have the server split the string into words \(space separated\) and send each word to a random port from the list below.



If the random port picked has already been used to transmit, it is ok to use it again



Write a UDP receiver that sends a sentence over port 2222, then waits for the response traffic on all ports below and uses select\(\) to reconstruct the sentence as its sent back from the server, one word/port per line.



Portlist= 2345, 1789, 9999, 65233, 25000, 33912, 5901, 2223, 8768, 43848, 4432, 7292, 13666

::



 \(Portxxxx\) The

 \(Portyyyy\) quick

 \(Port zzzz\) brown

 ...

#### Lab 5B

Turtorial under construction.

