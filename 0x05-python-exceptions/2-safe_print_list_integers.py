#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers in a list.
    Args:
        my_list (list): The list to print integers from.
        x (int): The number of elements to access in my_list.
    Returns:
        The number of integers actually printed.
    """
    printed_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return printed_count
