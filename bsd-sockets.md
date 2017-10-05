# I**ntroduction to Sockets**

**Berkeley sockets ** is an[ application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) \(API\) for [Internet sockets](https://en.wikipedia.org/wiki/Internet_socket) and[ Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) \(IPC\). It is commonly implemented as a[ library](https://en.wikipedia.org/wiki/Library_%28computing%29) of linkable modules. It originated with the 4.2 BSD [Unix](https://en.wikipedia.org/wiki/Unix) released in 1983.

A socket is an abstract representation \([handle](https://en.wikipedia.org/wiki/Handle_%28computing%29)\) for the local endpoint of a network communication path. The Berkeley sockets API represents it as a [file descriptor](https://en.wikipedia.org/wiki/File_descriptor) \([file handle](https://en.wikipedia.org/wiki/File_handle)\) in the[ Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) that provides a common interface for input and output to[ streams](https://en.wikipedia.org/wiki/Standard_streams) of data.

Berkeley sockets evolved with little modification from a [de facto standard](https://en.wikipedia.org/wiki/De_facto_standard) into a component of the[ POSIX](https://en.wikipedia.org/wiki/POSIX) specification. Therefore, the term ** POSIX sockets ** is essentially synonymous with Berkeley sockets. They are also known as **BSD sockets**, acknowledging the first implementation in the [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution).

* We will be using the BSD Socket API for networking
* Knowing BSD sockets will provide a foundation to do networking in almost any language/environment

\(Even Windows' Winsock library still follows the call pattern, even if Microsoft makes their function calls take a dozen more parameters\)

