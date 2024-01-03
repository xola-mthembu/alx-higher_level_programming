#!/usr/bin/python3

# Using two nested loops to print all possible combinations of two digits
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 < 8:
            print("{:d}{:d}, ".format(num1, num2), end='')
        else:
            print("{:d}{:d}".format(num1, num2))
