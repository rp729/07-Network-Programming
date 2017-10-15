# HTTP Status Codes

Status codes are a 3 digit number to tell you the result of the transaction.

Below are some common ones:

**100 Series, Informational**

100 Continue.



**200 Series, Successful responses**

200 OK - Your response will be in the data.



**300 Series, Redirection**

301 Moved Permanently - new URI likely provided in data.

307 Temporary Redirect - Use this new URI now and same METHOD to repeat the transaction.

308 Permanent Redirect - Use this new URI permanently and same METHOD to repeat the transaction.



**400 Series, Client Error**

400 Bad Request - Your request was not understood.

403 Forbidden - No access rights to URI

404 Not Found - No such URI

418 I'm a teapot - Coffee is poison!



**500 Series, Server Error**

500 Internal Server Error - Something probably errored/crashed while processing your request.

503 Server Unavailable - No server can handle the request at this time. May include a "Retry-After" key-value pair.

