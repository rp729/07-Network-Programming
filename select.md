# Select\(\)

* Select\(\) is a potential solution for when you want to open multiple sockets for communication, but don't want your receive/send functions to block and hold up your program.
* Select is a Linux function call that operates on file descriptors. In Linux specifically, everything is a file. This means at it's core in Linux, a network socket is a file descriptor.
* Since it's a syscall, it works in C, Python, and any other language you can make syscalls from \(in Linux anyway\). Under the hood it is a wrapper for poll\(\).

---

### Socket Setup

We need to import select, and set our sockets to be non-blocking.

#### `import select`

#### `...`

#### `p1 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)`

#### `p1.setblocking(0)`

#### `p1.bind( ('', 2000) )`

#### `p1.listen(1)`

#### `p2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)`

#### `p2.setblocking(0)`

#### `p2.bind( ('', p2port) )`

#### `p2.listen(1)`

---

### Setting Up a Call

Select\(\) takes 3 parameters, each is a list of file descriptors.

The first parameter is for reads.

The second parameter is for writes.

The third parameter to see if there is anyfdsthat threw an exception.

FDs can be in multiple lists.

#### `# Sockets to which we expect to read`

#### `inputs = [ p1, p2 ]`

#### 

#### `# Sockets to which we expect to write`

#### `outputs = [ ]`

#### `readable, writable, exceptional =select.select(inputs, outputs, inputs)`

---

### Using It

You do NOT need to use all return values in the for-loops below. If you only care about reading, then omit the remaining two loops.

The returned lists may also be handled in any order. If you prioritize writes, handle that list first.

Remember that the parameters and return values are all Python lists. There is NO guarantee of order of sockets within those lists.

#### `socklist = [mysock1: ‘host1’, mysock2: ‘host1:8080’, mysock3: ‘host2-description’}`



#### `while True:`

#### `readable, writable, exceptional =select.select(inputs, outputs, inputs)`

#### `for s in readable:`

* #### `# compare s to your socket list to find out which one it is`
* #### `# read incoming data and handle it`

#### `for s in writeable:`

* #### `# compare s to your socket list to find out which one it is`
* #### `# identify data that goes to that socket, and write it`

#### `for s in exceptional:`

* #### `# compare s to your socket list to find out which one it is`
* #### `# handle the exception`
* #### `# You may have internal states to keep track of. Update them now`

\(e.g. is the user logged in? How far along in a buffer are you\)

