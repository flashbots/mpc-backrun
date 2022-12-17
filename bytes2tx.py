#!/usr/bin/env python3
# convert 64 bit integers to raw tx

from sys import argv, stdout
from json import loads

assert len(argv) == 2, "Usage: %s <json array>" % argv[0]
stdout.write("0x")
for i in loads(argv[1]):
    stdout.write(f"{i:#0{4}x}"[2:])
stdout.write("\n")

