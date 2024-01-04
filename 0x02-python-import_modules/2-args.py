#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_count = len(argv) - 1  # Subtract 1 to exclude the script name
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
