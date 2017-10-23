![](/assets/sockopt.PNG)

There might be situations when you force the program to terminate and you want to restart it immediately after that. As a result of the ﬁrst program execution, the socket might be in a TIME WAIT state. It cannot be immediately reused and an error will be raised. 

This is the mechanism that should ensure that two different TCP sessions are not mixed up in the case that there are delayed packets belonging to the ﬁrst TCP session. Usually, this protection mechanism is not necessary because severe packet delays are not very likely in common networks. If you want to avoid seeing the 'address in use' error you can do it by setting the reuse address socket option: 

#### `s.setsockopt(socket.SOL SOCKET, socket.SO REUSEADDR, 1)`



