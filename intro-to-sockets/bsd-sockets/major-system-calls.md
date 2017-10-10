![](/assets/systemcalls.PNG)A **CONNECTION **is a unique combination of:

* Client IP
* Client Port
* Server IP
* Server Port



If any one of these changes, it must be a different connection.



A connection is established between a TCP client and TCP server when the client uses connect\(\) to establish a connection to a TCP server listening. The result of that connection is the socket returned by accept\(\).

