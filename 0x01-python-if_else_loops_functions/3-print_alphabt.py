#!/usr/bin/python3

# Constructing the alphabet string without 'e' and 'q' using list comprehension
alphabet = [chr(c) for c in range(97, 123) if c != 101 and c != 113]

# Using a single print function with string format to print the entire alphabet string
print("".join(alphabet))
