#!/usr/bin/python3

# Using a single print function and a loop to print the alphabet except 'q' and 'e'
for letter in range(97, 123):  # ASCII values from 'a' (97) to 'z' (122)
    if chr(letter) not in ['q', 'e']:
        print(f"{chr(letter)}", end='')
