# HTTP Status Codes

The status code is a three-digit integer, and the first digit identifies the general category of response.

Below are some common ones:

**100 Series, Informational**

* 100 Continue.

**200 Series, Successful responses**

* 200 OK - Your response will be in the data.

**300 Series, Redirection**

* 301 Moved Permanently - new URI likely provided in data.
* 307 Temporary Redirect - Use this new URI now and same METHOD to repeat the transaction.
* 308 Permanent Redirect - Use this new URI permanently and same METHOD to repeat the transaction.

**400 Series, Client Error**

* 400 Bad Request - Your request was not understood.
* 403 Forbidden - No access rights to URI
* 404 Not Found - No such URI
* 418 I'm a teapot - Coffee is poison!

**500 Series, Server Error**

* 500 Internal Server Error - Something probably errored/crashed while processing your request.
* 503 Server Unavailable - No server can handle the request at this time. May include a "Retry-After" key-value pair.

**A complete list of status codes is in the HTTP specification \(section 9 for HTTP 1.0, and section 10 for HTTP 1.1\).**

* **HTTP 1.0 \(RFC 1945\)--**[HTML](http://www.ics.uci.edu/pub/ietf/http/rfc1945.html), [text](http://www.ics.uci.edu/pub/ietf/http/rfc1945.txt), and [gzip'd PostScript](http://www.ics.uci.edu/pub/ietf/http/rfc1945.ps.gz)

* **HTTP 1.1 \(RFC 2616\)--**[HTML](http://www.w3.org/Protocols/rfc2616/rfc2616.html), [text](http://www.w3.org/Protocols/rfc2616/rfc2616.txt), [PostScript](ftp://ftp.isi.edu/in-notes/rfc2616.ps), and [PDF](http://www.w3.org/Protocols/HTTP/1.1/rfc2616.pdf)



