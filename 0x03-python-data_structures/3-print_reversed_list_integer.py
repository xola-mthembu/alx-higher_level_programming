#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    This function prints all integers in a list in reverse order.
    Each integer is printed on a new line.
    """
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))

if __name__ == "__main__":
    # This is an example usage that you can test locally
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
