#!/usr/bin/env python3
# convert raw tx to single bytes (represented as integers)

from sys import argv, stdout


USER_TX_MAX_LEN = 500

assert len(argv) == 2, "Usage: %s <tx>" % argv[0]
rawtx = argv[1].lstrip("0x")
assert len(rawtx) % 2 == 0, "tx has wrong length"

for i in [rawtx[j:j + 2] for j in range(0, len(rawtx), 2)]:
    stdout.write("%s " % int(i, 16))
for _ in range(0, len(rawtx) - USER_TX_MAX_LEN):
    stdout.write("0 ")
