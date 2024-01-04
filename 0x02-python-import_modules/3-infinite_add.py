#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum_of_args = sum(int(arg) for arg in argv[1:])  # Sum all arguments converted to integers
    print(sum_of_args)
