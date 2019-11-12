#!/usr/bin/env python2

import sys
import struct
import time


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestamp = struct.unpack("<L", data[8:12])
time_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp[0]))
author  = struct.unpack("<8s", data[12:20])
section = struct.unpack("<L", data[20:24])

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: {}".format(time_datetime))
print("AUTHOR: {}".format(author[0]))
print("SECTION COUNT: {}".format(section[0]))



# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
offset = 24
for i in range(5):
    stype, slen = struct.unpack("<LL", data[offset:offset + 8])

    print("Section Type: {}".format(stype))
    print("Section Length: {}".format(slen))

    offset += 8

    if stype == 1:
        (message,) = struct.unpack("<{}s".format(slen), data[offset:offset + slen])

        if message[-1] == "=":
            message = base64.b64decode(message)
            print("ASCII: {}".format(message))
        else:
            print("ASCII: {}".format(message))

    if stype == 2:
        (message,) = struct.unpack("<{}s".format(slen), data[offset:offset + slen])
        print("UTF-8: {}".format(message))

    if stype == 3:
        (message,) = struct.unpack("<{}s".format(slen/4), data[offset:offset + slen/4])
        print("WORDS: {}".format(message))

    if stype == 4:
        for i in range(0, slen, 8):
            (message, ) = struct.unpack("<8s", data[offset + i, offset + i + 8])
            print("DWORDS: {}".format(message))

    if stype == 5:
         for i in range(0, slen, 8):
            (message, ) = struct.unpack("<8s", data[offset + i, offset + i + 8])
            print("DOUBLES: {}".format(message))

    if stype == 6:
        if slen == 16:
            (latitude, longitude) = struct.unpack("<dd", data[offset:offset + slen])
            print("Coordinates: ({}, {})".format(latitude, longitude))
        else:
            print("Wrong length, expected 16, got {}".format(slen))

    if stype == 7:
        (message,) = struct.unpack("<d", data[offset:offset+slen])
        print("REFERENCE: {}".format(message))

    if stype == 8:
        header = b"\x89\x50\x4E\x47\x0d\x0a\x1a\x0a"
        with open("embedded_png.png", "wb") as f:
            f.write(header)
            f.write(data[offset:offset + slen])

        print("PNG saved to embedded_png.png")

    if stype == 9:
        header = b"\x47\x49\x46\x38\x37\x61"
        with open("embedded_gif87.png", "wb") as f:
            f.write(header)
            f.write(data[offset:offset + slen])
        
        print("GIF87 saved to embedded_gif87.png")

    if stype == 10:
        header = b"\x47\x49\x46\x38\x39\x61"
        with open("embedded_gif89.png", "wb") as f:
            f.write(header)
            f.write(data[offset:offset + slen])

        print("GIF89 saved to embedded_gif89.png")

    offset += slen
