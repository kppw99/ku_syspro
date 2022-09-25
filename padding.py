#!/usr/bin/python3

from sys import argv

if len(argv) < 3:
    print("please input filename and padding size!")
    print("- usage: ./padding.py [filename] [padding size]")
    exit(1)

with open(argv[1], 'rb') as fp:
    data = fp.read()
    size = int(argv[2])
    if size < len(data):
        print("please input large padding size than original size!")
        print("- original size:", len(data))
        exit(1)
    data += b'\x00' * (size - len(data))

with open(argv[1] + '_padding', 'wb') as fp:
    fp.write(data)

