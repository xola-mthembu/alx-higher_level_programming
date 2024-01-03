#!/usr/bin/python3

def islower(c):
    # Check if the character 'c' is lowercase
    return ('a' <= c <= 'z')

if __name__ == "__main__":
    test_cases = ['a', 'H', 'A', '3', 'g', '"']
    for case in test_cases:
        result = "lower" if islower(case) else "upper"
        print("{} is {}".format(case, result))
