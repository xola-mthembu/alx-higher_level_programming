#!/usr/bin/python3

# Constructing the alphabet string using a loop
alphabet = ''.join([chr(letter) for letter in range(97, 123)])

# Printing the entire alphabet string in one go
print(f"{alphabet}", end='')
