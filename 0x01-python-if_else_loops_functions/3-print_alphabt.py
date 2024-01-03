#!/usr/bin/python3

# Printing the entire alphabet string without 'e' and 'q' using string format
print("".join(chr(c) for c in range(97, 123) if c != 101 and c != 113), end='')

# Printing a newline character
print()
