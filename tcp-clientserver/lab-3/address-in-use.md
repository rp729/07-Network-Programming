# **Socket Options**

If you encounter an error "Address in use", set the following socket option on your sockets \(both client and server\).



mysock.setsockopt\(socket.SOL\_SOCKET,socket.SO\_REUSEADDR, 1\)





You may have to wait out the initial timer \(or change your ports\).

