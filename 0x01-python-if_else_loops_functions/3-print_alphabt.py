#!/usr/bin/python3

# ASCII values for 'a' to 'z'
for letter in range(97, 123):
    # Check if the letter is not 'e' and not 'q'
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end='')

# Print a newline character after all characters are printed
print()
