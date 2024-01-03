#!/usr/bin/python3

# Using a single loop to print numbers from 0 to 99 in the desired format
for num in range(100):
    if num < 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num))
