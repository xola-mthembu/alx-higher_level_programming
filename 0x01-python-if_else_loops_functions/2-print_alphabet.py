#!/usr/bin/python3
# This program prints the ASCII alpha in lowercase, not followed by a new line.
# It uses only one print funct with string format, one loop, and tab indentations.

# Loop to print each letter
for letter in range(97, 123):
    print("{}".format(chr(letter)), end='')
