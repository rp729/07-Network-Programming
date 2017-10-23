# **Socket Options**

If you encounter an error **"Address in use"**, set the following socket option on your sockets \(both client and server\).

#### `mysock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)`

You may have to wait out the initial timer \(or change your ports\).

#### See Also: _Reusing Socket Addresses_ in _Advanced Functionality._



