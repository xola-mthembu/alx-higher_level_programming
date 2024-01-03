#!/usr/bin/python3
alphabet = "".join(
    chr(i) if i % 2 == 0 else chr(i - 32) for i in range(122, 96, -1)
)
print("{}".format(alphabet), end='')
