#!/usr/bin/python3

# Using a single loop to print the ASCII alpha in lowercase (except 'q' and 'e')
for letter in range(97, 123):  # ASCII values for 'a' to 'z'
    if letter != 101 and letter != 113:  # ASCII values for 'e' and 'q'
        print("{}".format(chr(letter)), end='')
