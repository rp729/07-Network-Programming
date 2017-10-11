# setsockopt\(\) and getsockopt\(\)

Using socket options gives you some advanced options for sockets to do interesting things.



Options have a LEVEL, OPTION NAME, and a VALUE



* LEVEL can be the entire socket \(socket.SOL\_SOCKET\) or a specific protocol \(socket.IPPROTO\_IPV6\)
* The LEVEL specified determines what OPTION NAMEs are available to be set
* VALUES are assigned to the specified OPTION NAME



Unfortunately, options are scattered all over the place in documentation. Man pages are currently the best source or for a grouping of common ones, see the refs.

