#!/usr/bin/python3
# This program prints the ASCII alphabet in lowercase, not followed by a new line.
# It uses only one print function with string format, one loop, and tab indentations.

# Loop to print each letter
for letter in range(97, 123):
    print("{}".format(chr(letter)), end='')
