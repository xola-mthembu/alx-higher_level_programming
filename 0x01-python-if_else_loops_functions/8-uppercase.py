#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            # Convert to uppercase using ord() and chr()
            char = chr(ord(char) - 32)
        print(char, end="")
    print()  # Print a new line at the end

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
