# Introduction to Hyper Text Transport Protocol

**HTTP is a string based protocol.**

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

* An HTTP line break is a carriage return followed by a newline \(\r\n\).
* A blank line with a single \r\n signifies the end of a header.

**This ends a request, and separates the data from the header in a response.**



