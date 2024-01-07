#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers from a list in reverse order, one integer per line.
    """
    for number in reversed(my_list):
        print("{:d}".format(number))
