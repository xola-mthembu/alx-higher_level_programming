#!/usr/bin/python3

# Construct the alpha string without 'e' and 'q' using list comprehension
alphabet = [chr(c) for c in range(97, 123) if c != 101 and c != 113]

# Use single print function with string format to print the entire alpha string
print("{}".format("".join(alphabet)), end='')
