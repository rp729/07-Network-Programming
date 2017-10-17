# Introduction to Hyper Text Transport Protocol

HTTP stands for **Hypertext Transfer Protocol**. It's the network protocol used to deliver virtually all files and other data \(collectively called resources\) on the World Wide Web, whether they're HTML files, image files, query results, or anything else. Usually, HTTP takes place through TCP/IP sockets \(and this tutorial ignores other possibilities\).

A browser is an HTTP client because it sends requests to an HTTP server \(Web server\), which then sends responses back to the client. The standard \(and default\) port for HTTP servers to listen on is 80, though they can use any port.  \(HTTP a stateless protocol, i.e. not maintaining any connection information between transactions\).

**HTTP Requests are sent with several broad categories of information:**

* The resource requested and it's location \(index.html at example.com\).
* Information about the expected result \(type of data, language, etc\).
* Any supplemental data needed to process the request \(form data, parameters, etc\).

**HTTP Responses usually contain:**

* The result of the transaction \(status codes\).
* Metadata about the transaction \(date, webserver, content length and type\).
* The data.

---

#### HTTP Line Breaks

* An HTTP line break is a carriage return \(CRLF\) followed by a newline \(\r\n\).
* A blank line with a single \r\n signifies the end of a header.

**This ends a request, and separates the data from the header in a response.**

**CR** and **LF** are control characters, respectively coded 0x0D \(13 decimal\) and 0x0A \(10 decimal\). They are used to mark a line break in a text file. As you indicated, Windows uses two characters the **CR LF** sequence; Unix only uses **LF** and the old MacOS \( pre-OSX MacIntosh\) used **CR.**

