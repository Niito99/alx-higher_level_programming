#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        if i == 0:
            b = 122
        b = int(122 - (2 * (i / 2)))
    else:
        b = int(90 - (2 * (i / 2)))
    print("{}".format((list(map(chr, range(b, b+1))))[0]), end='')
