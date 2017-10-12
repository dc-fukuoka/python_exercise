#!/usr/bin/env python3

import struct

if __name__ == "__main__":
    with open("test.dat", "rb") as f:
        data = f.read()
        res = struct.unpack_from("<IIl8s", data, offset=0)
        
    for i in range(4):
        if i < 3:
            print("res[", i, "]:", res[i])
        else:
            print("res[", i, "]:", res[i].decode("utf-8"))
