# HTTP Requests

#### **HTTP Requests**

* The only MANDATORY parts of an HTTP Request are the METHOD, the URL, HTTP version, and the host \(and any data you need to send if POSTING\).
* We will only discuss the methods GET and POST because they are almost exclusively what you will encounter, however others do exist.

---

#### Example 1

#### `GET /hello.htm HTTP/1.1`

#### `User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)`

#### `Host: www.example.com`

#### `Accept-Language:en-us`

#### `Accept-Encoding:gzip, deflate`

#### `Connection: Keep-Alive`

-------------------------------------------

#### Example 2

#### `POST /cgi-bin/process.cgiHTTP/1.1`

#### ` User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)`

#### ` Host: www.tutorialspoint.com`

#### ` Content-Type: application/x-www-form-urlencoded`

#### ` Content-Length: length`

#### ` Accept-Language:en-us`

#### ` Accept-Encoding:gzip, deflate`

#### ` Connection: Keep-Alive`



