# Struct Module

Struct allows you to pack values into specified data types/sizes andendianess. Packed data is represented by a string of hex bytes.

Struct will also unpack data from the hex string and provide you a tuple of the values.

Packing is used to prepare structured binary data such as a protocol header or a message format. This data can then be referenced like a struct in C, or sent across the wire.

It uses a format string and variable arguments \(like print or printf in C\)

`>>> from struct import *`

`>>> pack('hhl', 1, 2, 3)`

`'\x00\x01\x00\x02\x00\x00\x00\x03'`

`>>> unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')`

`(1, 2, 3)`

