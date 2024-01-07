#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers from a list, one integer per line
    """
    for number in my_list:
        print("{:d}".format(number))
