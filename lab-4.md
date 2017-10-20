# Lab 4A

struct pack/unpack

host to network byte order

buffer sizes

socket timeout

handling socket errors

modifying send.rec buffer size

echo server

file transfer

## Functions vs. Struct Class

There are a set of module-level functions for working with structured values, and there is also theStructclass \(new in Python 2.5\). Format specifiers are converted from their string format to a compiled representation, similar to the way regular expressions are. The conversion takes some resources, so it is typically more efficient to do it once when creating aStructinstance and call methods on the instance instead of using the module-level functions. All of the examples below use theStructclass.

## Packing and Unpacking

Structs support\_packing\_data into strings, and\_unpacking\_data from strings using format specifiers made up of characters representing the type of the data and optional count and endian-ness indicators. For complete details, refer to the standard library documentation.

In this example, the format specifier calls for an integer or long value, a two character string, and a floating point number. The spaces between the format specifiers are included here for clarity, and are ignored when the format is compiled.

```
import struct 
import binascii

values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values
print 'Format string  :', s.format
print 'Uses           :', s.size, 'bytes'
print 'Packed Value   :', binascii.hexlify(packed_data)
```

The example converts the packed value to a sequence of hex bytes for printing with binascii.hexlify\(\), since some of the characters are nulls.

```
$ python struct_pack.py

Original values: (1, 'ab', 2.7)
Format string  : I 2s f
Uses           : 12 bytes
Packed Value   : 0100000061620000cdcc2c40
```

If we pass the packed value to unpack\(\), we get basically the same values back \(note the discrepancy in the floating point value\).

```
import struct
import binascii

packed_data = binascii.unhexlify('0100000061620000cdcc2c40')

s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print'Unpacked Values:', unpacked_data
```

```
$ python struct_unpack.py

Unpacked Values: (1, 'ab', 2.700000047683716)
```

## Endianness

By default values are encoded using the native C library notion of “endianness”. It is easy to override that choice by providing an explicit endianness directive in the format string.

```
import struct
import binascii

values = (1, 'ab', 2.7)
print 'Original values:', values

endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network'),
    ]

for code, name in endianness:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print
    print 'Format string  :', s.format, 'for', name
    print 'Uses           :', s.size, 'bytes'
    print 'Packed Value   :', binascii.hexlify(packed_data)
    print 'Unpacked Value :', s.unpack(packed_data)
```

```
$ python struct_endianness.py

Original values: (1, 'ab', 2.7)

Format string  : @ I 2s f for native, native
Uses           : 12 bytes
Packed Value   : 0100000061620000cdcc2c40
Unpacked Value : (1, 'ab', 2.700000047683716)

Format string  : = I 2s f for native, standard
Uses           : 10 bytes
Packed Value   : 010000006162cdcc2c40
Unpacked Value : (1, 'ab', 2.700000047683716)

Format string  : < I 2s f for little-endian
Uses           : 10 bytes
Packed Value   : 010000006162cdcc2c40
Unpacked Value : (1, 'ab', 2.700000047683716)

Format string  : > I 2s f for big-endian
Uses           : 10 bytes
Packed Value   : 000000016162402ccccd
Unpacked Value : (1, 'ab', 2.700000047683716)

Format string  : ! I 2s f for network
Uses           : 10 bytes
Packed Value   : 000000016162402ccccd
Unpacked Value : (1, 'ab', 2.700000047683716)
```

## Buffers

Working with binary packed data is typically reserved for highly performance sensitive situations or passing data into and out of extension modules. In such situations, you can optimize by avoiding the overhead of allocating a new buffer for each packed structure. Thepack\_into\(\)andunpack\_from\(\)methods support writing to pre-allocated buffers directly.

```
import struct
import binascii

s = struct.Struct('I 2s f')
values = (1, 'ab', 2.7)
print 'Original:', values

print
print 'ctypes string buffer'

import ctypes
b = ctypes.create_string_buffer(s.size)
print 'Before  :', binascii.hexlify(b.raw)
s.pack_into(b, 0, *values)
print 'After   :', binascii.hexlify(b.raw)
print 'Unpacked:', s.unpack_from(b, 0)

print
print 'array'

import array
a = array.array('c', '\0' *s.size)
print 'Before  :', binascii.hexlify(a)
s.pack_into(a, 0, *values)
print 'After   :', binascii.hexlify(a)
print 'Unpacked:', s.unpack_from(a, 0)
```

The _ size _ attribute of the Struct tells us how big the buffer needs to be.

```
$ python struct_buffers.py

Original: (1, 'ab', 2.7)

ctypes string buffer
Before  : 000000000000000000000000
After   : 0100000061620000cdcc2c40
Unpacked: (1, 'ab', 2.700000047683716)

array
Before  : 000000000000000000000000
After   : 0100000061620000cdcc2c40
Unpacked: (1, 'ab', 2.700000047683716)
```

#### See also:

**struct:** The standard library documentation for this module. \(https://docs.python.org/2.7/library/struct.html\)

**array:** The array module, for working with sequences of fixed-type values. \(https://docs.python.org/2/library/array.html\)

**binascii: ** The binascii module, for producing ASCII representations of binary data. 

\(https://docs.python.org/2/library/binascii.html\)

**WikiPedia: Endianness** - Explanation of byte order and endianness in encoding. \(https://en.wikipedia.org/wiki/Endianness\)

_**In-Memory Data Structures: **_ More tools for working with data structures. 

